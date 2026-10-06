#!/usr/bin/env python3
"""registry — the document register for npsi.ca.

    python3 tools/registry.py --extract   # rebuild registry.json from the document pages
    python3 tools/registry.py --check     # fail if any page disagrees with registry.json
    python3 tools/registry.py --list      # print the register, by number, to the terminal

registry.json at the site root is the single public list of every published
NPSI document. The index pages (/papers/, /briefings/, /register/), the
breadcrumb and previous/next links on document pages, llms.txt and the
sitemap are expected to agree with it; `--check` is run by sitecheck.py so a
page cannot be published that the register does not know about.

Two identifiers, by design (adopted October 2026):

  serial     the publication serial, NPSI-WP-NNN (and TB, BN, SB, PL), assigned
             by the editor alone at publication, sequential, never reused.
  accession  the intake number, NPSI-YYYYMMDD-X, assigned by machine when a
             draft enters the system, immutable. Documents released before a
             serial was assigned carry only an accession number and show
             "serial pending" on the register.

Standard library only; nothing here is deployed (tools/ is in .vercelignore).
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry.json"
FOLDER = re.compile(r"^(wp|tb|bn|sb|pl)(\d+)$")
SERIAL = re.compile(r"^NPSI-(WP|TB|BN|SB|PL)-(\d{3})$")
ACCESSION = re.compile(r"^NPSI-(\d{8})(?:-([A-Z]))?$")

LINES = {
    "WP": {"name": "Working Papers", "singular": "Working Paper", "serial": "NPSI-WP-NNN",
           "index": "/papers/", "pdf": "working-paper.pdf",
           "description": "Long-form, sourced, version-numbered documents intended for senior policy, fiduciary and academic readers. Published when substantive material is ready; there is no cadence."},
    "TB": {"name": "Technical Briefings", "singular": "Technical Briefing", "serial": "NPSI-TB-NNN",
           "index": "/briefings/", "pdf": "technical-briefing.pdf",
           "description": "A companion line to the Working Papers, addressing the engineering substrate beneath the policy architecture."},
    "BN": {"name": "Briefing Notes", "singular": "Briefing Note", "serial": "NPSI-BN-NNN",
           "index": "/briefings/", "pdf": "briefing-note.pdf",
           "description": "The imprint’s short-form line: a single mechanism, documented end to end, in under twenty minutes of reading."},
    "SB": {"name": "Special Briefings", "singular": "Special Briefing", "serial": "NPSI-SB-NNN",
           "index": "/briefings/", "pdf": "special-briefing.pdf",
           "description": "Single-issue strategic assessments, published when an exposure demands attention outside the working-paper cycle."},
    "PL": {"name": "The Pacific Ledger", "singular": "Pacific Ledger issue", "serial": "NPSI-PL-NNN",
           "index": "/ledger/", "pdf": "pacific-ledger.pdf",
           "description": "A monthly account of the Canada–Korea relationship. Every entry sourced, both sides of the account kept."},
}

# The primary navigation, sitewide (adopted October 2026, replacing the
# four-link nav that exposed only the current paper). `active` names the
# pages and document lines each link covers.
NAV = [
    ("/papers/", "Papers", {"papers", "WP"}),
    ("/briefings/", "Briefings", {"briefings", "TB", "BN", "SB"}),
    ("/ledger/", "Ledger", {"ledger", "PL"}),
    ("/commentary/", "Commentary", {"commentary"}),
    ("/about/", "About", {"about"}),
]
DEPLOY_SKIP = {".git", ".claude", ".agents", ".github", "tools", "figures", "node_modules"}
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]

# Numbers the editor has reserved but never released. The register lists them
# so a reader scanning the archive knows the gaps are intentional.
NEVER_ISSUED = [{"line": "WP", "number": 6}, {"line": "WP", "number": 8}]


def clean(s: str | None) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def first(rx: str, s: str) -> str | None:
    m = re.search(rx, s, re.S)
    return m.group(1) if m else None


def extract(folder: Path) -> dict:
    """Read one document page's own metadata. Nothing is guessed: every field
    comes from a tag the page already carries for citation or sharing."""
    s = (folder / "index.html").read_text(encoding="utf-8")
    m = FOLDER.match(folder.name)
    line, number = m.group(1).upper(), int(m.group(2))
    ident = first(r'name="dc.identifier" content="([^"]+)"', s) or ""
    serial = accession = None
    if SERIAL.match(ident):
        serial = ident
    elif ACCESSION.match(ident):
        accession = ident
    pub = first(r'name="citation_publication_date" content="([^"]+)"', s) or ""
    released = pub.replace("/", "-")  # 2026/07/28 -> 2026-07-28; 2026/05 -> 2026-05
    doc = {
        "line": line,
        "number": number,
        "serial": serial,
        "accession": accession,
        "folder": folder.name,
        "url": f"/{folder.name}/",
        "title": clean(first(r"<h1[^>]*>(.*?)</h1>", s)),
        "subtitle": clean(first(r'class="subtitle">(.*?)</div>', s)) or None,
        "version": first(r"<dt>Version</dt>\s*<dd><code>([^<]+)</code>", s),
        "released": released,
        "series": None,
        "status": "published",
        "pdf": first(r'rel="alternate" type="application/pdf" href="([^"]+)"', s),
        "files": [f"/{folder.name}/{f.name}" for f in sorted(folder.glob("*.pdf"))],
        "supersedes": None,
        "superseded_by": None,
    }
    series = clean(first(r"<dt>Series</dt>\s*<dd>(.*?)</dd>", s))
    # Several pages explain the line itself in the Series row ("Special
    # Briefing — single-issue…"); keep only a named series within the line.
    if series:
        name = re.split(r"\s[—·]\s", series)[0].strip()
        name = re.sub(r"^NPSI\s+", "", name)
        if name and not re.match(r"^(Working Paper|Technical Briefing|Briefing Note|Special Briefing|Pacific Ledger)", name):
            doc["series"] = name
    sup = first(r"<dt>Supersedes</dt>\s*<dd>\s*<a href=\"/(wp\d+)/\"", s)
    if sup:
        doc["supersedes"] = sup
    supby = first(r"<dt>Superseded by</dt>\s*<dd>\s*<a href=\"/(wp\d+)/\"", s)
    if supby:
        doc["superseded_by"] = supby
        doc["status"] = "superseded"
    # A release file the page never declared as rel="alternate" (WP2, WP3,
    # WP9 at October 2026) is still the paper's PDF if it carries the line's
    # conventional name.
    conventional = f"/{folder.name}/{LINES[line]['pdf']}"
    if not doc["pdf"] and conventional in doc["files"]:
        doc["pdf"] = conventional
    if line == "PL":
        doc["version"] = doc["version"] or None
    return doc


def current_paper() -> str | None:
    """The current working paper is whichever the home page's current card
    names; set_current_paper.py keeps that card and the registry in step."""
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    m = re.search(r'<section id="current">.*?<a class="btn" href="/(wp\d+)/"', home, re.S)
    if m:
        return m.group(1)
    if REGISTRY.is_file():
        return json.loads(REGISTRY.read_text(encoding="utf-8")).get("current")
    return None


def folders() -> list[Path]:
    return sorted((p for p in ROOT.iterdir() if p.is_dir() and FOLDER.match(p.name)),
                  key=lambda p: (p.name[:2], int(p.name[2:])))


def build() -> dict:
    docs = [extract(f) for f in folders()]
    cur = current_paper()
    for d in docs:
        if d["folder"] == cur:
            d["status"] = "current"
    docs.sort(key=lambda d: (d["line"], d["number"]))
    return {
        "imprint": "North Pacific Strategy Initiative",
        "url": "https://npsi.ca/",
        "generated": date.today().isoformat(),
        "identifiers": {
            "serial": "Publication serial, assigned by the editor alone at publication; sequential within its line; never reused.",
            "accession": "Intake number, NPSI-YYYYMMDD-X, assigned when a document enters the system; immutable. A document may carry an accession number before a serial is assigned.",
        },
        "current": cur,
        "lines": LINES,
        "never_issued": NEVER_ISSUED,
        "documents": docs,
    }


def by_date(docs: list[dict]) -> list[dict]:
    """Publication order, newest first; ties (month-only dates) break by number."""
    return sorted(docs, key=lambda d: (d["released"], d["number"]), reverse=True)


def check() -> int:
    if not REGISTRY.is_file():
        print("ERROR registry.json missing; run tools/registry.py --extract")
        return 1
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    want = {d["folder"]: d for d in reg["documents"]}
    have = {f.name: extract(f) for f in folders()}
    errors = 0
    for name in sorted(set(want) | set(have)):
        if name not in want:
            print(f"ERROR {name}/ is on the site but not in registry.json")
            errors += 1
            continue
        if name not in have:
            print(f"ERROR registry.json lists {name}/ but the folder does not exist")
            errors += 1
            continue
        w, h = want[name], have[name]
        for k in ("line", "number", "serial", "accession", "title", "version", "released", "pdf",
                  "files", "supersedes", "superseded_by"):
            if w.get(k) != h.get(k):
                print(f"ERROR {name}: registry says {k}={w.get(k)!r}, page says {h.get(k)!r}")
                errors += 1
    cur = reg.get("current")
    if cur and want.get(cur, {}).get("status") != "current":
        print(f"ERROR registry current={cur} but that document's status is not 'current'")
        errors += 1
    for d in reg["documents"]:
        if d["serial"] and not SERIAL.match(d["serial"]):
            print(f"ERROR {d['folder']}: malformed serial {d['serial']}")
            errors += 1
        if d["serial"] and int(d["serial"][-3:]) != d["number"]:
            print(f"ERROR {d['folder']}: serial {d['serial']} does not match number {d['number']}")
            errors += 1
    serials = [d["serial"] for d in reg["documents"] if d["serial"]]
    for s in sorted(set(serials)):
        if serials.count(s) > 1:
            print(f"ERROR serial {s} is assigned to more than one document")
            errors += 1
    print(f"registry: {len(reg['documents'])} documents, {errors} errors")
    return 1 if errors else 0


def listing() -> None:
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    for line, meta in LINES.items():
        docs = [d for d in reg["documents"] if d["line"] == line]
        gaps = [g["number"] for g in reg["never_issued"] if g["line"] == line]
        if not docs:
            continue
        print(f"\n{meta['name']}")
        for n in range(1, max(d["number"] for d in docs) + 1):
            d = next((x for x in docs if x["number"] == n), None)
            if d:
                ident = d["serial"] or f"{d['accession']} (serial pending)"
                print(f"  {n:>3}  {ident:32} {d['released']:10} {d['version'] or '':7} {d['status']:10} {d['title']}")
            elif n in gaps:
                print(f"  {n:>3}  {'never issued':32}")
            else:
                print(f"  {n:>3}  {'UNACCOUNTED':32}")


# ---------------------------------------------------------------- rendering

def esc(s: str | None) -> str:
    return html.escape(s or "", quote=True)


def nice_date(iso: str) -> str:
    """2026-07-28 -> 28 July 2026; 2026-05 -> May 2026."""
    parts = iso.split("-")
    if len(parts) == 3:
        return f"{int(parts[2])} {MONTHS[int(parts[1]) - 1]} {parts[0]}"
    if len(parts) == 2:
        return f"{MONTHS[int(parts[1]) - 1]} {parts[0]}"
    return iso


def ident_label(d: dict) -> str:
    if d["serial"]:
        return d["serial"]
    return f"{d['accession']} · serial pending"


def ident_cell(d: dict) -> str:
    """Register cell: the identifier in <code>, a pending note outside it so
    the note can wrap while the identifier never does."""
    if d["serial"]:
        return f"<code>{esc(d['serial'])}</code>"
    return f"<code>{esc(d['accession'])}</code> <span class=\"pending\">serial pending</span>"


def status_label(d: dict) -> str:
    return {"current": "Current", "superseded": "Superseded", "published": "Published"}[d["status"]]


def deployed_pages() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.html") if not (set(p.relative_to(ROOT).parts) & DEPLOY_SKIP))


def page_key(p: Path) -> str:
    """Which nav entry a page belongs to: a line code for document pages, the
    folder name for institutional pages, '' for home and 404."""
    rel = p.relative_to(ROOT)
    if len(rel.parts) == 1:
        return ""
    m = FOLDER.match(rel.parts[0])
    return m.group(1).upper() if m else rel.parts[0]


def nav_html(key: str, indent: str = "    ") -> str:
    lines = [f'{indent}<nav class="nav" aria-label="Primary navigation">']
    for href, label, keys in NAV:
        active = ' class="active"' if key in keys else ""
        lines.append(f'{indent}  <a href="{href}"{active}>{label}</a>')
    lines.append(f"{indent}</nav>")
    return "\n".join(lines)


NAV_BLOCK = re.compile(r'[ \t]*<nav class="nav" aria-label="Primary navigation">.*?</nav>', re.S)


def apply_nav() -> int:
    """Rewrite the masthead nav on every deployed page. Idempotent."""
    n = 0
    for p in deployed_pages():
        s = p.read_text(encoding="utf-8")
        s2, k = NAV_BLOCK.subn(lambda m: nav_html(page_key(p)), s, count=1)
        if k != 1:
            print(f"WARN {p.relative_to(ROOT)}: masthead nav not found")
            continue
        if s2 != s:
            p.write_text(s2, encoding="utf-8")
            n += 1
    print(f"nav: {n} pages rewritten")
    return 0


DOC_NAV = re.compile(r'\n?<!-- doc-nav -->.*?<!-- /doc-nav -->\n?', re.S)
MAIN_OPEN = '<main id="main" tabindex="-1">\n'


def doc_nav_html(d: dict, prev: dict | None, nxt: dict | None) -> str:
    line = LINES[d["line"]]
    crumb_index = f'<a href="{line["index"]}">{esc(line["name"])}</a>'
    here = f'No. {d["number"]}' if d["line"] != "PL" else f'№ {d["number"]:02d}'
    parts = [f'<div class="doc-nav-crumb"><a href="/">NPSI</a> <span aria-hidden="true">›</span> '
             f'{crumb_index} <span aria-hidden="true">›</span> <span aria-current="page">{here}</span></div>']
    links = []
    if prev:
        links.append(f'<a rel="prev" href="{prev["url"]}"><span aria-hidden="true">←</span> '
                     f'No. {prev["number"]} · {esc(prev["title"])}</a>')
    if nxt:
        links.append(f'<a rel="next" href="{nxt["url"]}">No. {nxt["number"]} · {esc(nxt["title"])} '
                     f'<span aria-hidden="true">→</span></a>')
    if links:
        parts.append('<div class="doc-nav-links">' + "".join(links) + "</div>")
    return ('<!-- doc-nav -->\n<nav class="doc-nav" aria-label="Document navigation">\n  '
            + "\n  ".join(parts) + "\n</nav>\n<!-- /doc-nav -->\n")


def apply_doc_nav() -> int:
    """Insert or refresh the breadcrumb and previous/next links on every
    document page. Order within a line is publication date (the house rule),
    oldest to newest, so "next" is the later publication. Idempotent."""
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    n = 0
    for line in LINES:
        docs = sorted((d for d in reg["documents"] if d["line"] == line),
                      key=lambda d: (d["released"], d["number"]))
        for i, d in enumerate(docs):
            prev = docs[i - 1] if i > 0 else None
            nxt = docs[i + 1] if i + 1 < len(docs) else None
            p = ROOT / d["folder"] / "index.html"
            s = p.read_text(encoding="utf-8")
            s2 = DOC_NAV.sub("", s)
            if MAIN_OPEN not in s2:
                print(f"WARN {d['folder']}: <main> opening tag not found")
                continue
            s2 = s2.replace(MAIN_OPEN, MAIN_OPEN + "\n" + doc_nav_html(d, prev, nxt), 1)
            if s2 != s:
                p.write_text(s2, encoding="utf-8")
                n += 1
    print(f"doc-nav: {n} document pages rewritten")
    return 0


def chrome() -> tuple[str, str, str]:
    """Head boilerplate (minus the page-specific tags), masthead, and footer,
    copied from /about/ so the generated pages carry the chrome verbatim."""
    s = (ROOT / "about" / "index.html").read_text(encoding="utf-8")
    head = re.search(r'(<link rel="icon".*?)</head>', s, re.S).group(1).rstrip()
    footer = re.search(r'<footer class="site-footer">.*?</footer>', s, re.S).group(0)
    return head, "", footer


def page_shell(path: str, title: str, description: str, key: str, body: str) -> str:
    head, _, footer = chrome()
    url = f"https://npsi.ca{path}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)} · North Pacific Strategy Initiative</title>
<meta name="description" content="{esc(description)}">

<meta property="og:title" content="{esc(title)} · NPSI">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://npsi.ca/assets/img/og-default.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="North Pacific Strategy Initiative">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">

<link rel="canonical" href="{url}">

{head}
</head>
<body>

<a href="#main" class="skip-link">Skip to content</a>

<header class="masthead">
  <div class="masthead-inner">
    <a href="/" class="masthead-mark">NORTH PACIFIC STRATEGY INITIATIVE</a>
{nav_html(key)}
    <div class="nav-volume">VOL.&nbsp;I  ·  EST.&nbsp;MMXXVI</div>
  </div>
</header>

<main id="main" tabindex="-1">

{body}
</main>

{footer}

</body>
</html>
"""


def item_html(d: dict, line: str) -> str:
    """One row of an index list: meta line, linked title, subtitle, files."""
    meta = [f"No. {d['number']}"]
    if d["series"]:
        meta.append(d["series"])
    if d["version"]:
        meta.append(d["version"])
    meta.append(nice_date(d["released"]))
    if d["status"] != "published":
        meta.append(status_label(d))
    files = [f'<a href="{d["url"]}">Read</a>']
    if d["pdf"]:
        files.append(f'<a href="{d["pdf"]}">PDF</a>')
    for extra in d.get("files", []):
        if extra != d["pdf"]:
            label = "PDF, print edition" if extra.endswith("-print.pdf") else f"PDF, {Path(extra).stem.replace('-', ' ')}"
            files.append(f'<a href="{extra}">{esc(label)}</a>')
    sub = f"\n      <p>{esc(d['subtitle'])}</p>" if d["subtitle"] else ""
    return f"""    <div class="ledger-item">
      <div class="wp-card-meta">{esc("  ·  ".join(meta))}</div>
      <h4><a href="{d["url"]}">{esc(d["title"])}</a></h4>{sub}
      <p class="index-files">{" · ".join(files)}</p>
    </div>"""


def card_html(d: dict, line: str, label: str) -> str:
    meta = [f"No. {d['number']}"]
    if d["series"]:
        meta.append(d["series"])
    if d["version"]:
        meta.append(d["version"])
    meta.append(nice_date(d["released"]))
    pdf = (f'\n      <a class="btn btn-bronze" href="{d["pdf"]}">Download {label} (PDF)</a>' if d["pdf"] else "")
    sub = f'\n    <div class="wp-card-subtitle">{esc(d["subtitle"])}</div>' if d["subtitle"] else ""
    return f"""  <article class="wp-card">
    <div class="wp-card-meta">{esc("  ·  ".join(meta))}</div>
    <h3 class="wp-card-title">{esc(d["title"])}</h3>{sub}
    <div class="wp-card-actions">
      <a class="btn" href="{d["url"]}">Read {label}</a>{pdf}
    </div>
  </article>"""


def render_papers(reg: dict) -> str:
    docs = [d for d in reg["documents"] if d["line"] == "WP"]
    cur = next((d for d in docs if d["status"] == "current"), None)
    rest = [d for d in by_date(docs) if d is not cur]
    gaps = sorted(g["number"] for g in reg["never_issued"] if g["line"] == "WP")
    gap_note = ""
    if gaps:
        nums = " and ".join(f"No. {g}" for g in gaps)
        gap_note = (f"\n  <p>The numbering is the author’s: {nums} were reserved and never released, so the "
                    f"archive carries intentional gaps. Nothing has been withdrawn; the <a href=\"/register/\">number "
                    f"register</a> lists every serial ever assigned, and the git history is the audit trail.</p>")
    body = f"""<div class="opener">
  <div class="meridian"><span></span></div>
  <div class="doc-class">Working Papers · NPSI-WP-NNN</div>
  <h1>Working Papers</h1>
  <div class="subtitle">{esc(LINES["WP"]["description"].split(". ")[0])}.</div>
  <p class="lede">{len(docs)} working papers published since May 2026, listed by publication date, newest first. Each is version-numbered and placed under public version control; errata are published as patch versions. Named commentary on any paper is welcomed at <a href="/commentary/">Commentary</a>.</p>
</div>
"""
    if cur:
        body += f"""
<section id="current">
  <h2>Current Working Paper</h2>
{card_html(cur, "WP", "Working Paper")}
</section>
"""
    body += f"""
<section id="all">
  <h2>All Working Papers</h2>{gap_note}
  <div class="ledger ledger-list">
{chr(10).join(item_html(d, "WP") for d in ([cur] if cur else []) + rest)}
  </div>
</section>
"""
    return body


def render_briefings(reg: dict) -> str:
    body = f"""<div class="opener">
  <div class="meridian"><span></span></div>
  <div class="doc-class">Briefings · Technical · Notes · Special</div>
  <h1>Briefings</h1>
  <div class="subtitle">Three shorter lines beside the Working Papers.</div>
  <p class="lede">Technical Briefings address the engineering substrate beneath the policy architecture. Briefing Notes document a single mechanism end to end. Special Briefings are single-issue assessments published when an exposure demands attention outside the working-paper cycle. Each line is numbered separately; see the <a href="/register/">number register</a>.</p>
</div>
"""
    for line, anchor, label in (("SB", "special", "Special Briefing"), ("TB", "technical", "Technical Briefing"),
                                ("BN", "notes", "Briefing Note")):
        docs = by_date([d for d in reg["documents"] if d["line"] == line])
        if not docs:
            continue
        body += f"""
<section id="{anchor}">
  <h2>{esc(LINES[line]["name"])}</h2>
  <p>{esc(LINES[line]["description"])}</p>
  <div class="ledger ledger-list">
{chr(10).join(item_html(d, line) for d in docs)}
  </div>
</section>
"""
    return body


def render_register(reg: dict) -> str:
    body = f"""<div class="opener">
  <div class="meridian"><span></span></div>
  <div class="doc-class">Number Register · every identifier the imprint has assigned</div>
  <h1>The Number Register</h1>
  <div class="subtitle">A ledger records both sides. So does the register.</div>
  <p class="lede">Every NPSI document carries a <em>publication serial</em> (<code>NPSI-WP-NNN</code> and the equivalent for each line), assigned by the editor at publication, sequential within its line and never reused. A document may also carry an <em>accession number</em> (<code>NPSI-YYYYMMDD-X</code>), assigned when it entered the system and never changed. Both appear here. Numbers reserved and never released are listed as such; nothing is withdrawn silently. The machine-readable form is <a href="/registry.json"><code>registry.json</code></a>.</p>
</div>
"""
    for line, meta in LINES.items():
        docs = [d for d in reg["documents"] if d["line"] == line]
        if not docs:
            continue
        gaps = {g["number"] for g in reg["never_issued"] if g["line"] == line}
        rows = []
        for n in range(1, max(d["number"] for d in docs) + 1):
            d = next((x for x in docs if x["number"] == n), None)
            if d:
                rows.append(f"""      <tr>
        <td class="num">{n}</td>
        <td>{ident_cell(d)}</td>
        <td><a href="{d["url"]}">{esc(d["title"])}</a></td>
        <td>{esc(nice_date(d["released"]))}</td>
        <td>{esc(d["version"] or "—")}</td>
        <td>{esc(status_label(d))}</td>
      </tr>""")
            elif n in gaps:
                rows.append(f"""      <tr class="never">
        <td class="num">{n}</td>
        <td><code>{esc(meta["serial"].replace("NNN", f"{n:03d}"))}</code></td>
        <td>Reserved, never released</td>
        <td>—</td><td>—</td><td>Never issued</td>
      </tr>""")
        anchor = line.lower()
        body += f"""
<section id="{anchor}">
  <h2>{esc(meta["name"])} <span class="register-serial">{esc(meta["serial"])}</span></h2>
  <div class="register-wrap">
    <table class="register">
      <thead><tr><th>No.</th><th>Identifier</th><th>Title</th><th>Released</th><th>Version</th><th>Status</th></tr></thead>
      <tbody>
{chr(10).join(rows)}
      </tbody>
    </table>
  </div>
</section>
"""
    body += """
<section id="rules">
  <h2>How numbers are assigned</h2>
  <div class="standard">
    <h4>Serials are the editor’s alone.</h4>
    <p>No serial is assigned by anyone or anything other than the editor, and none is assigned before publication. A document released before its serial is assigned carries its accession number and is listed here as <em>serial pending</em> until the editor rules.</p>
  </div>
  <div class="standard">
    <h4>Accession numbers are permanent.</h4>
    <p>The accession number records the date a document entered the system and distinguishes documents that entered the same day by a letter suffix. It never changes, even after a serial is assigned, and it is printed on the release.</p>
  </div>
  <div class="standard">
    <h4>Gaps are declared.</h4>
    <p>A number that was reserved and never released stays on the register as such. The archive is ordered by publication date; the register is ordered by number. Both are kept.</p>
  </div>
</section>
"""
    return body


def compact_item(d: dict) -> str:
    """One line of a home-page list: number, title, date; no abstract."""
    line = LINES[d["line"]]
    tag = {"WP": "No.", "TB": "TB No.", "BN": "BN No.", "SB": "SB No.", "PL": "\u2116"}[d["line"]]
    meta = f"{tag} {d['number']}  \u00b7  {nice_date(d['released'])}"
    if d["status"] == "superseded":
        meta += "  \u00b7  Superseded"
    return (f'    <div class="ledger-item">\n      <div class="wp-card-meta">{esc(meta)}</div>\n'
            f'      <h4><a href="{d["url"]}">{esc(d["title"])}</a></h4>\n    </div>')


def render_home_lists(reg: dict) -> int:
    """Refresh the two compact lists on the home page between their markers:
    previous working papers (all but the current one) and all briefings."""
    p = ROOT / "index.html"
    s = p.read_text(encoding="utf-8")
    docs = reg["documents"]
    archive = [d for d in by_date(d for d in docs if d["line"] == "WP") if d["status"] != "current"]
    briefs = by_date(d for d in docs if d["line"] in ("SB", "TB", "BN"))
    blocks = {
        "archive-list": '  <div class="ledger">\n' + "\n".join(compact_item(d) for d in archive) + "\n  </div>",
        "briefings-list": '  <div class="ledger">\n' + "\n".join(compact_item(d) for d in briefs) + "\n  </div>",
    }
    n = 0
    for name, body in blocks.items():
        rx = re.compile(rf"<!-- {name} -->.*?<!-- /{name} -->", re.S)
        s, k = rx.subn(lambda m: f"<!-- {name} -->\n{body}\n<!-- /{name} -->", s, count=1)
        if k != 1:
            print(f"WARN index.html: markers for {name} not found")
        n += k
    p.write_text(s, encoding="utf-8")
    print(f"home: {n} lists refreshed")
    return 0


def render() -> int:
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    render_home_lists(reg)
    pages = {
        "papers": ("/papers/", "Working Papers",
                   "Every NPSI working paper, by publication date: the current paper, the archive, and the numbering.",
                   "papers", render_papers(reg)),
        "briefings": ("/briefings/", "Briefings",
                      "NPSI Technical Briefings, Briefing Notes and Special Briefings, by publication date.",
                      "briefings", render_briefings(reg)),
        "register": ("/register/", "The Number Register",
                     "Every identifier the North Pacific Strategy Initiative has assigned: publication serials, accession numbers, and reserved numbers never released.",
                     "register", render_register(reg)),
    }
    for folder, (path, title, desc, key, body) in pages.items():
        out = ROOT / folder / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(page_shell(path, title, desc, key, body), encoding="utf-8")
        print(f"rendered {folder}/index.html")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--extract", action="store_true", help="rebuild registry.json from the document pages")
    g.add_argument("--check", action="store_true", help="fail if any page disagrees with registry.json")
    g.add_argument("--list", action="store_true", help="print the register")
    g.add_argument("--render", action="store_true", help="write /papers/, /briefings/ and /register/ from the registry")
    g.add_argument("--doc-nav", action="store_true", help="refresh breadcrumb and previous/next on document pages")
    g.add_argument("--nav", action="store_true", help="rewrite the masthead nav on every deployed page")
    g.add_argument("--all", action="store_true", help="extract, render, doc-nav, nav, then check")
    a = ap.parse_args()
    if a.extract or a.all:
        reg = build()
        REGISTRY.write_text(json.dumps(reg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote registry.json: {len(reg['documents'])} documents, current={reg['current']}")
        if not a.all:
            return 0
    if a.render or a.all:
        render()
    if a.doc_nav or a.all:
        apply_doc_nav()
    if a.nav or a.all:
        apply_nav()
    if a.check or a.all:
        return check()
    if a.list:
        listing()
    return 0


if __name__ == "__main__":
    sys.exit(main())
