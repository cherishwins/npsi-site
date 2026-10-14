#!/usr/bin/env python3
"""Vendor the site's web fonts: the exact woff2 files Google Fonts serves, self-hosted.

    python3 tools/vendor-fonts.py          # refresh assets/fonts/*.woff2 and assets/css/fonts.css

Fetches the Google Fonts stylesheet for the four site faces as a modern browser
would, keeps the latin and latin-ext slices of Source Serif 4, Source Sans 3 and
JetBrains Mono, and only those Noto Serif KR slices that cover Hangul actually
set on the site (scanned from every page). Each file is downloaded once, named
deterministically, and declared in assets/css/fonts.css with the same
font-weight range and unicode-range Google declared, so rendering is identical
and a slice is fetched only when a page uses its glyphs. All four faces are
under the SIL Open Font License; assets/fonts/OFL.txt accompanies them.

Re-run when a face or weight is added to FAMILIES. Pages link
/assets/css/fonts.css once; they never link Google.
"""
import glob, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'assets', 'fonts')
OUT_CSS = os.path.join(ROOT, 'assets', 'css', 'fonts.css')
FAMILIES = ('family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400;1,8..60,600'
            '&family=Source+Sans+3:ital,wght@0,400;0,500;0,600;1,400'
            '&family=JetBrains+Mono:wght@400;500'
            '&family=Noto+Serif+KR:wght@400;600')
CSS_URL = 'https://fonts.googleapis.com/css2?' + FAMILIES + '&display=swap'
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/129.0 Safari/537.36')  # a woff2-capable browser: Google serves variable woff2 + unicode-range
LATIN_SUBSETS = {'latin', 'latin-ext'}
SLUG = {'Source Serif 4': 'source-serif-4', 'Source Sans 3': 'source-sans-3',
        'JetBrains Mono': 'jetbrains-mono', 'Noto Serif KR': 'noto-serif-kr'}


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def site_hangul():
    cps = set()
    for p in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True):
        if '/.git/' in p:
            continue
        t = open(p, encoding='utf-8').read().split('<body', 1)[-1]
        t = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', t, flags=re.S)
        cps |= {ord(ch) for ch in t if '가' <= ch <= '힣' or 'ㄱ' <= ch <= 'ㆎ'}
    return cps


def covers(unicode_range, cps):
    for r in unicode_range.split(','):
        r = r.strip()[2:]
        if '?' in r:
            lo = int(r.replace('?', '0'), 16); hi = int(r.replace('?', 'F'), 16)
        elif '-' in r:
            a, z = r.split('-'); lo, hi = int(a, 16), int(z, 16)
        else:
            lo = hi = int(r, 16)
        if any(lo <= c <= hi for c in cps):
            return True
    return False


def main():
    css = fetch(CSS_URL).decode('utf-8')
    hangul = site_hangul()
    blocks = re.findall(r'(?:/\* ([\w-]+) \*/\s*)?@font-face \{(.*?)\}', css, re.S)
    keep, files = [], {}
    for label, body in blocks:
        fam = re.search(r"font-family: '([^']+)'", body).group(1)
        url = re.search(r'url\(([^)]+)\)', body).group(1)
        rng = re.search(r'unicode-range: ([^;]+);', body).group(1)
        if fam == 'Noto Serif KR':
            if not covers(rng, hangul):
                continue
            label = label or 'kr-' + re.search(r'/([^/]+)\.woff2', url).group(1)[-6:]
        elif label not in LATIN_SUBSETS:
            continue
        style = re.search(r'font-style: (\w+)', body).group(1)
        weight = re.search(r'font-weight: ([\d ]+)', body).group(1).strip()
        key = url
        if key not in files:
            name = f"{SLUG[fam]}-{'italic' if style == 'italic' else 'roman'}-{label}.woff2"
            if fam == 'Noto Serif KR':
                name = f"{SLUG[fam]}-{weight.split()[0]}-{label}.woff2"
            files[key] = name
        keep.append((fam, style, weight, files[key], rng))
    # Google emits one @font-face per requested instance, all pointing at the same
    # variable file. Declare each file once with the weight RANGE those instances
    # span, so the browser draws 600 and 700 from the wght axis instead of
    # synthesising bold from a single 400 declaration.
    span, order = {}, []
    for fam, style, weight, name, rng in keep:
        k = (fam, style, name)
        lo, hi = (int(w) for w in (weight.split() * 2)[:2])
        if k not in span:
            span[k] = [lo, hi, rng]; order.append(k)
        else:
            span[k][0] = min(span[k][0], lo); span[k][1] = max(span[k][1], hi)
    decls = []
    for fam, style, name in order:
        lo, hi, rng = span[(fam, style, name)]
        decls.append((fam, style, f'{lo}' if lo == hi else f'{lo} {hi}', name, rng))
    os.makedirs(OUT_DIR, exist_ok=True)
    total = 0
    for url, name in files.items():
        path = os.path.join(OUT_DIR, name)
        data = fetch(url)
        open(path, 'wb').write(data)
        total += len(data)
        print(f'{len(data) // 1024:5d} KB  {name}')
    lic = os.path.join(ROOT, 'tools', 'fonts', 'OFL.txt')
    if os.path.exists(lic):
        open(os.path.join(OUT_DIR, 'OFL.txt'), 'w').write(open(lic).read())
    out = ['/* Self-hosted web fonts: the woff2 files Google Fonts serves for the four site faces,',
           '   vendored by tools/vendor-fonts.py. Do not edit by hand; re-run the tool.',
           '   Source Serif 4, Source Sans 3, JetBrains Mono, Noto Serif KR: SIL Open Font License,',
           '   see /assets/fonts/OFL.txt. Each slice downloads only when a page sets its glyphs. */', '']
    for fam, style, weight, name, rng in decls:
        out.append('@font-face {')
        out.append(f"  font-family: '{fam}';")
        out.append(f'  font-style: {style};')
        out.append(f'  font-weight: {weight};')
        out.append('  font-display: swap;')
        out.append(f"  src: url('/assets/fonts/{name}') format('woff2');")
        out.append(f'  unicode-range: {rng};')
        out.append('}')
    open(OUT_CSS, 'w').write('\n'.join(out) + '\n')
    print(f'{len(files)} files, {total // 1024} KB total; {len(decls)} @font-face rules -> {os.path.relpath(OUT_CSS, ROOT)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
