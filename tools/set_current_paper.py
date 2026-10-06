#!/usr/bin/env python3
"""Make a working paper the current paper, sitewide, in one command.

    python3 tools/set_current_paper.py 12 --title "Title of the Paper" \
        --version v1.0 --month "October 2026"

Run it after wp12/index.html exists and is listed in sitemap.xml. It does the
mechanical part of a current-paper change and nothing else:

  1. any link labelled "current Working Paper" (the 404 page has one) points
     at /wp12/;
  2. every previous-paper banner names the new current paper;
  3. the paper that was current gains the standard previous-paper banner
     (one sentence; add a companion sentence by hand if the paper needs one);
  4. sitemap.xml gives the new paper priority 0.9 and the old one 0.7;
  5. registry.json records the new current paper, and /papers/, the home
     page lists and every document's breadcrumb are re-rendered from it.

Since October 2026 the primary nav no longer names the current paper (it is
Papers · Briefings · Ledger · Commentary · About; tools/registry.py --nav
writes it). The home page's current card, the commentary section, llms.txt /
llms-full.txt and the CLAUDE.md index carry prose and stay hand-edited (see
the npsi-publish skill). Update the home card before running this, then:
python3 tools/sitecheck.py --fix-sitemap && python3 tools/sitecheck.py
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", ".claude", ".agents", ".github", "tools", "figures", "node_modules"}
CURRENT_LABEL = re.compile(r'<a href="/wp\d+/">(current [Ww]orking [Pp]aper)</a>')
BANNER = re.compile(r'The current working paper is <a href="/wp\d+/">Working Paper No\.&nbsp;\d+ — '
                    r'<em>[^<]*</em></a> \([^)]*\)')


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("number", type=int)
    ap.add_argument("--title", required=True, help="the paper's title, as plain text")
    ap.add_argument("--version", required=True, help="e.g. v1.0")
    ap.add_argument("--month", required=True, help='release month for the banner, e.g. "October 2026"')
    a = ap.parse_args()

    new = a.number
    new_page = ROOT / f"wp{new}" / "index.html"
    if not new_page.is_file():
        sys.exit(f"wp{new}/index.html does not exist; build the paper first")
    sys.path.insert(0, str(ROOT / "tools"))
    import registry  # noqa: E402  (tools/registry.py)
    reg = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
    if not reg.get("current"):
        sys.exit("registry.json names no current paper; run tools/registry.py --extract first")
    old = int(reg["current"][2:])
    if old == new:
        sys.exit(f"WP{new} is already the current paper")

    title = a.title.replace("&", "&amp;")
    sentence = (f'The current working paper is <a href="/wp{new}/">Working Paper No.&nbsp;{new} — '
                f'<em>{title}</em></a> ({a.version}, {a.month})')

    pages = sorted(p for p in ROOT.rglob("*.html") if not (set(p.relative_to(ROOT).parts) & SKIP))
    banners = 0
    for p in pages:
        s = p.read_text(encoding="utf-8")
        s2 = s
        if p != new_page:
            s2, b = BANNER.subn(sentence, s2)
            banners += b
        s2 = CURRENT_LABEL.sub(lambda mm: f'<a href="/wp{new}/">{mm.group(1)}</a>', s2)
        if s2 != s:
            p.write_text(s2, encoding="utf-8")

    old_page = ROOT / f"wp{old}" / "index.html"
    s = old_page.read_text(encoding="utf-8")
    inserted = False
    if "You are reading a previous working paper." not in s:
        anchor = '<aside class="wp-meta-block"'
        if s.count(anchor) != 1:
            sys.exit(f"wp{old}/index.html: no unique metadata block to place the banner before; add it by hand")
        banner = ('<aside class="standard screen-only" style="margin-bottom: 36px;">\n'
                  '  <h4>You are reading a previous working paper.</h4>\n'
                  f'  <p>{sentence}.</p>\n'
                  '</aside>\n\n')
        old_page.write_text(s.replace(anchor, banner + anchor, 1), encoding="utf-8")
        inserted = True

    sm_path = ROOT / "sitemap.xml"
    sm = sm_path.read_text(encoding="utf-8")
    for num, prio in ((new, "0.9"), (old, "0.7")):
        sm, n = re.subn(rf"(<loc>https://npsi\.ca/wp{num}/</loc>\s*<lastmod>[^<]+</lastmod>\s*<priority>)[\d.]+(</priority>)",
                        rf"\g<1>{prio}\g<2>", sm)
        if not n:
            print(f"note: https://npsi.ca/wp{num}/ is not in sitemap.xml yet; add it, then rerun or set priority by hand")
    sm_path.write_text(sm, encoding="utf-8")

    # registry: the new paper is current, the old one is not; re-render what
    # derives from it (index pages, home lists, breadcrumbs).
    fresh = registry.build()
    fresh["current"] = f"wp{new}"
    for d in fresh["documents"]:
        if d["line"] == "WP" and d["status"] == "current":
            d["status"] = "published"
        if d["folder"] == f"wp{new}":
            d["status"] = "current"
    (ROOT / "registry.json").write_text(json.dumps(fresh, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    registry.render()
    registry.apply_doc_nav()

    print(f"current paper WP{old} -> WP{new}: {banners} banners updated"
          + (f", banner added to wp{old}" if inserted else "") + ", registry and index pages re-rendered")
    print("next: home cards, commentary, llms files, CLAUDE.md index; then "
          "python3 tools/sitecheck.py --fix-sitemap && python3 tools/sitecheck.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
