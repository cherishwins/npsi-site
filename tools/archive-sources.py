#!/usr/bin/env python3
"""Archive every external source the site cites, so a citation outlives its URL.

    python3 tools/archive-sources.py --check     # which cited URLs have a Wayback snapshot (read-only)
    python3 tools/archive-sources.py --save      # ask the Internet Archive to capture the ones that do not
    python3 tools/archive-sources.py --report    # print the manifest as a table
    add --self to any of these to include the site's own pages from sitemap.xml

The manifest, tools/archive-manifest.json, records for each cited URL the newest
snapshot the Archive holds (timestamp and archive URL) and when it was last checked.
tools/ is never deployed; the manifest is a record, not a page. --save uses the
Save Page Now endpoint and is rate-limited by the Archive; run it from a network
that can reach web.archive.org (GitHub Actions does, see .github/workflows/).

No page is modified by this tool. Citations stay as the author wrote them.
"""
import argparse, glob, html, json, os, re, sys, time, urllib.parse, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, 'tools', 'archive-manifest.json')
SKIP_HOSTS = ('npsi.ca', 'fonts.googleapis.com', 'fonts.gstatic.com', 'cloud.umami.is',
              'creativecommons.org', 'github.com', 'www.linkedin.com', 'web.archive.org', 'schema.org')
UA = 'npsi-site archive tool (+https://npsi.ca/colophon/)'


def cited_urls():
    """Every distinct http(s) href in the site's pages, with the pages that cite it."""
    where = {}
    pages = sorted(p for p in glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True)
                   if '/figures/' not in p and '/.git/' not in p)
    for p in pages:
        s = open(p, encoding='utf-8').read()
        s = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', s, flags=re.S)
        for u in re.findall(r'href="(https?://[^"]+)"', s):
            u = html.unescape(u).strip()
            host = urllib.parse.urlsplit(u).netloc.lower()
            if any(host == h or host.endswith('.' + h) for h in SKIP_HOSTS):
                continue
            where.setdefault(u, set()).add(os.path.relpath(os.path.dirname(p), ROOT) or '.')
    return {u: sorted(v) for u, v in where.items()}


def own_pages():
    """The site's own URLs from sitemap.xml, so the publications themselves get captured."""
    sm = os.path.join(ROOT, 'sitemap.xml')
    if not os.path.exists(sm):
        return []
    return re.findall(r'<loc>(https?://[^<]+)</loc>', open(sm, encoding='utf-8').read())


def load_manifest():
    if os.path.exists(MANIFEST):
        return json.load(open(MANIFEST, encoding='utf-8'))
    return {'generated': None, 'sources': {}}


def save_manifest(m):
    m['generated'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    json.dump(m, open(MANIFEST, 'w', encoding='utf-8'), indent=1, ensure_ascii=False, sort_keys=True)
    print(f'wrote {os.path.relpath(MANIFEST, ROOT)}: {len(m["sources"])} sources')


def get(url, timeout=25):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.headers, r.read()


def availability(u):
    """Newest snapshot per the Wayback availability API, or None."""
    q = 'https://archive.org/wayback/available?url=' + urllib.parse.quote(u, safe='')
    try:
        _, _, body = get(q)
        snap = json.loads(body).get('archived_snapshots', {}).get('closest')
        if snap and snap.get('available'):
            return {'timestamp': snap['timestamp'], 'archive_url': snap['url']}
    except Exception as e:  # network, JSON, rate limit: record nothing, keep going
        print(f'  ? {u[:80]} ({type(e).__name__})', file=sys.stderr)
    return None


def save_page(u):
    """Ask Save Page Now to capture u. Returns the archive URL or None."""
    try:
        _, headers, _ = get('https://web.archive.org/save/' + u, timeout=90)
        loc = headers.get('Content-Location') or headers.get('Location')
        if loc:
            return 'https://web.archive.org' + loc if loc.startswith('/') else loc
    except urllib.error.HTTPError as e:
        print(f'  ! {u[:80]} HTTP {e.code}', file=sys.stderr)
    except Exception as e:
        print(f'  ! {u[:80]} ({type(e).__name__})', file=sys.stderr)
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true', help='look up snapshots for every cited URL')
    ap.add_argument('--save', action='store_true', help='capture URLs that have no snapshot (or --all)')
    ap.add_argument('--all', action='store_true', help='with --save: capture every URL, not only missing ones')
    ap.add_argument('--self', action='store_true', help="include the site's own pages (from sitemap.xml)")
    ap.add_argument('--report', action='store_true', help='print the manifest')
    ap.add_argument('--delay', type=float, default=1.5, help='seconds between Archive requests')
    a = ap.parse_args()
    if not (a.check or a.save or a.report):
        ap.print_help(); return 2

    cited = cited_urls()
    if a.self:
        for u in own_pages():
            cited.setdefault(u, ['(npsi.ca)'])
    m = load_manifest()
    src = m['sources']
    for u, pages in cited.items():
        src.setdefault(u, {})['cited_by'] = pages
    for u in [u for u in src if u not in cited]:
        src[u]['cited_by'] = []  # no longer cited; kept for the record

    if a.check:
        print(f'checking {len(cited)} cited URLs against the Wayback Machine')
        for i, u in enumerate(sorted(cited), 1):
            snap = availability(u)
            src[u]['checked'] = time.strftime('%Y-%m-%d', time.gmtime())
            if snap:
                src[u].update(snap)
            print(f'{i:4d} {"ok " if snap else "---"} {u[:100]}')
            time.sleep(a.delay)
        save_manifest(m)

    if a.save:
        todo = sorted(u for u in cited if a.all or not src[u].get('archive_url'))
        print(f'asking Save Page Now to capture {len(todo)} URLs')
        for i, u in enumerate(todo, 1):
            loc = save_page(u)
            if loc:
                src[u]['archive_url'] = loc
                src[u]['saved'] = time.strftime('%Y-%m-%d', time.gmtime())
            print(f'{i:4d} {"ok " if loc else "---"} {u[:100]}')
            time.sleep(max(a.delay, 6))  # SPN asks for several seconds between captures
        save_manifest(m)

    if a.report:
        have = sum(1 for u in cited if src.get(u, {}).get('archive_url'))
        print(f'{len(cited)} cited URLs, {have} with a snapshot, {len(cited) - have} without')
        for u in sorted(cited):
            r = src.get(u, {})
            print(f'{"ok " if r.get("archive_url") else "---"} {r.get("timestamp", "")[:8]:8s} {u[:90]}  <- {", ".join(r.get("cited_by", []))}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
