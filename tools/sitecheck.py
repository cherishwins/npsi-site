#!/usr/bin/env python3
"""sitecheck — the publish gate for npsi.ca.

Run from the repository root before every commit that touches a page:

    python3 tools/sitecheck.py              # structure, links, metadata, sitemap
    python3 tools/sitecheck.py --external   # also probe every outbound URL
    python3 tools/sitecheck.py --fix-sitemap  # refresh sitemap lastmod just before committing

Standard library only; no build step, nothing here is deployed (tools/ is in
.vercelignore). Exit status is 1 when any ERROR is reported, 0 otherwise.
WARN lines are judgement calls for the editor; they never fail the gate.

What it checks, per page:
  chrome    skip-link, <main id="main" tabindex="-1">, the four-link nav
            pointing at the current paper, the footer matching the home page
  links     every internal href/src resolves to a file; every #fragment
            resolves to an id on the target page
  metadata  <title>, description, canonical (absolute, trailing slash),
            og:url == canonical, og:image file exists, JSON-LD parses,
            citation_pdf_url / JSON-LD encoding point at real files
  markup    unbalanced tags, duplicate ids, <img> without alt
  brand     hex colours in page <style> blocks outside the site.css palette,
            font families outside the three site faces, inline px font sizes
  text      placeholder markers (TODO, TK, lorem, XX) and exclamation marks
            in body text
Site-wide: links labelled "current paper" point at it, every released PDF is
linked from the home page, og:image dimensions match the PNG, sitemap.xml lists
every page and PDF with each <lastmod> equal to the file's last commit date,
and llms.txt / llms-full.txt mention every page. Paths in .vercelignore are
not deployed, so they are not checked.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://npsi.ca"
SKIP_DIRS = {".git", ".claude", ".agents", ".github", "tools", "node_modules"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "source", "track", "wbr"}
# Elements whose end tag HTML lets an author omit; never report them unclosed.
OPTIONAL_END = {"p", "li", "dt", "dd", "tr", "td", "th", "thead", "tbody",
                "tfoot", "option", "colgroup", "rt", "rp", "optgroup"}
ALLOWED_FONTS = {"source serif 4", "source sans 3", "jetbrains mono",
                 "noto serif kr", "noto sans kr", "serif", "sans-serif",
                 "monospace", "inherit", "georgia", "times new roman",
                 "source serif pro", "source sans pro", "ibm plex mono",
                 "sf mono", "menlo", "consolas", "eb garamond", "system-ui",
                 "-apple-system", "helvetica neue", "initial", "unset"}
SVG_TAGS = {"svg", "g", "path", "rect", "circle", "ellipse", "line",
            "polyline", "polygon", "text", "tspan", "defs", "marker", "use",
            "clippath", "lineargradient", "radialgradient", "stop", "pattern",
            "title", "desc", "symbol", "mask", "foreignobject", "textpath"}

errors: list[str] = []
warns: list[str] = []


def err(where: str, msg: str) -> None:
    errors.append(f"ERROR {where}: {msg}")


def warn(where: str, msg: str) -> None:
    warns.append(f"WARN  {where}: {msg}")


class Page(HTMLParser):
    """One pass over a page, keeping what the checks need."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.elements: list[tuple[str, dict, int]] = []
        self.ids: dict[str, int] = {}
        self.dup_ids: list[tuple[str, int]] = []
        self.stack: list[tuple[str, int]] = []
        self.balance: list[str] = []
        self.title = ""
        self.meta: dict[str, str] = {}
        self.links: dict[str, str] = {}
        self.jsonld: list[tuple[str, int]] = []
        self.styles: list[tuple[str, int]] = []
        self.text: list[tuple[str, int]] = []
        self._in: str | None = None
        self._buf: list[str] = []
        self._buf_line = 0
        self._capture: dict[str, list] = {}   # name -> [depth, parts]
        self.captured: dict[str, str] = {}
        self._skip_text = 0                   # inside script/style/svg

    # -- helpers ---------------------------------------------------------
    def _open_capture(self, name: str) -> None:
        self._capture[name] = [len(self.stack), []]

    def handle_starttag(self, tag, attrs):
        a = {k: (v if v is not None else "") for k, v in attrs}
        line = self.getpos()[0]
        self.elements.append((tag, a, line))
        if "id" in a:
            if a["id"] in self.ids:
                self.dup_ids.append((a["id"], line))
            else:
                self.ids[a["id"]] = line
        if tag == "a" and "name" in a:
            self.ids.setdefault(a["name"], line)
        if tag == "meta":
            key = a.get("property") or a.get("name")
            if key and key not in self.meta:
                self.meta[key] = a.get("content", "")
        if tag == "link" and "rel" in a:
            self.links.setdefault(a["rel"], a.get("href", ""))
        if tag == "title":
            self._in, self._buf = "title", []
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in, self._buf, self._buf_line = "jsonld", [], line
        if tag == "style":
            self._in, self._buf, self._buf_line = "style", [], line
        if tag in ("script", "style") or tag == "svg":
            self._skip_text += 1
        cls = a.get("class", "").split()
        if tag == "nav" and "nav" in cls:
            self._open_capture("nav")
        if tag == "footer" and "site-footer" in cls:
            self._open_capture("footer")
        if tag not in VOID:
            self.stack.append((tag, line))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self.stack and self.stack[-1][0] == tag:
            self.stack.pop()

    def handle_endtag(self, tag):
        line = self.getpos()[0]
        if tag in ("script", "style") or tag == "svg":
            self._skip_text = max(0, self._skip_text - 1)
        if self._in == "title" and tag == "title":
            self.title = "".join(self._buf).strip()
            self._in = None
        if self._in == "jsonld" and tag == "script":
            self.jsonld.append(("".join(self._buf), self._buf_line))
            self._in = None
        if self._in == "style" and tag == "style":
            self.styles.append(("".join(self._buf), self._buf_line))
            self._in = None
        if tag in VOID:
            return
        # pop to the matching open tag, reporting anything skipped over
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for t, l in self.stack[i + 1:]:
                    if t not in OPTIONAL_END and t not in SVG_TAGS:
                        self.balance.append(f"<{t}> opened at line {l} closed implicitly by </{tag}> at line {line}")
                del self.stack[i:]
                break
        else:
            if tag not in OPTIONAL_END:
                self.balance.append(f"stray </{tag}> at line {line}")
        for name, (depth, parts) in list(self._capture.items()):
            if len(self.stack) <= depth:
                self.captured[name] = " ".join("".join(parts).split())
                del self._capture[name]

    def handle_data(self, data):
        if self._in:
            self._buf.append(data)
        for name, cap in self._capture.items():
            cap[1].append(data)
        if not self._skip_text and data.strip():
            self.text.append((data, self.getpos()[0]))


def site_path(url_path: str) -> Path | None:
    """Map a site URL path to the file that serves it, or None."""
    p = unquote(url_path)
    if not p.startswith("/"):
        return None
    target = ROOT / p.lstrip("/")
    if p.endswith("/"):
        target = target / "index.html"
    if target.is_file():
        return target
    if (target / "index.html").is_file():
        return target / "index.html"
    return None


def url_of(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def git_date(path: Path) -> str:
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(path)],
                         cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return out


def fix_sitemap() -> int:
    """Rewrite every <lastmod> to the file's last commit date; files with
    uncommitted changes get today's date, because the commit about to be made
    is the one that changes them. Run it immediately before committing."""
    dirty = set(subprocess.run(["git", "diff", "--name-only", "HEAD"], cwd=ROOT,
                               capture_output=True, text=True).stdout.split())
    today = subprocess.run(["date", "-u", "+%Y-%m-%d"], capture_output=True, text=True).stdout.strip()
    path = ROOT / "sitemap.xml"
    sm = path.read_text(encoding="utf-8")
    changed = 0

    def repl(m: re.Match) -> str:
        nonlocal changed
        f = site_path(urlparse(m.group(1)).path)
        if f is None:
            return m.group(0)
        rel = f.relative_to(ROOT).as_posix()
        date = today if rel in dirty else (git_date(f) or m.group(2))
        if date != m.group(2):
            changed += 1
        return m.group(0).replace(f"<lastmod>{m.group(2)}</lastmod>", f"<lastmod>{date}</lastmod>")

    sm = re.sub(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", repl, sm)
    path.write_text(sm, encoding="utf-8")
    print(f"sitemap.xml: {changed} lastmod value(s) updated")
    return 0


def deploy_ignored() -> set[str]:
    """Top-level names excluded from the deploy by .vercelignore."""
    names = set()
    for line in (ROOT / ".vercelignore").read_text(encoding="utf-8").splitlines():
        line = line.strip().strip("/")
        if line and not line.startswith("#") and "*" not in line:
            names.add(line.split("/")[0])
    return names


def png_size(path: Path) -> tuple[int, int] | None:
    head = path.read_bytes()[:24]
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big")


def palette() -> set[str]:
    css = (ROOT / "assets/css/site.css").read_text(encoding="utf-8")
    hexes = set()
    for m in re.finditer(r"#[0-9A-Fa-f]{3,8}\b", css):  # tokens plus the print block's literals
        h = m.group(0).upper()
        hexes.add("#" + "".join(c * 2 for c in h[1:]) if len(h) == 4 else h)
    return hexes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--external", action="store_true",
                    help="probe every outbound http(s) URL (slow; needs network)")
    ap.add_argument("--quiet", action="store_true", help="print only problems")
    ap.add_argument("--fix-sitemap", action="store_true",
                    help="rewrite sitemap <lastmod> values from git (uncommitted files get today), then exit")
    args = ap.parse_args()
    if args.fix_sitemap:
        return fix_sitemap()

    skip = SKIP_DIRS | deploy_ignored()
    pages = sorted(p for p in ROOT.rglob("*.html")
                   if not (set(p.relative_to(ROOT).parts) & skip))
    parsed: dict[Path, Page] = {}
    for p in pages:
        pg = Page()
        pg.feed(p.read_text(encoding="utf-8"))
        pg.close()
        parsed[p] = pg

    home = parsed[ROOT / "index.html"]
    ref_footer = home.captured.get("footer", "")
    # The home page's nav names the current paper; every page must agree.
    current_wp = next((a.get("href") for t, a, _ in home.elements
                       if t == "a" and a.get("href", "").startswith("/wp")), None)
    allowed_hex = palette()
    external: dict[str, list[str]] = {}

    for p, pg in parsed.items():
        where = p.relative_to(ROOT).as_posix()
        is_404 = p.name == "404.html"

        # chrome -----------------------------------------------------------
        if not any(t == "a" and a.get("href") == "#main" and "skip-link" in a.get("class", "")
                   for t, a, _ in pg.elements):
            err(where, "missing skip-link <a href=\"#main\" class=\"skip-link\">")
        if not any(t == "main" and a.get("id") == "main" and a.get("tabindex") == "-1"
                   for t, a, _ in pg.elements):
            err(where, "missing <main id=\"main\" tabindex=\"-1\">")
        nav_text = pg.captured.get("nav")
        if nav_text is None:
            err(where, "missing primary <nav class=\"nav\">")
        elif nav_text != "Working Paper About Engage Commentary":
            err(where, f"nav text is '{nav_text}', expected the four-link nav")
        nav_wp = None
        for i, (t, a, _) in enumerate(pg.elements):
            if t == "nav" and "nav" in a.get("class", "").split():
                nav_wp = next((a2.get("href") for t2, a2, _ in pg.elements[i + 1:]
                               if t2 == "a"), None)
                break
        if current_wp and nav_wp != current_wp:
            err(where, f"nav 'Working Paper' points to {nav_wp}, current paper is {current_wp}")
        if pg.captured.get("footer") != ref_footer:
            err(where, "footer differs from the home page footer")

        # metadata ---------------------------------------------------------
        if not pg.title:
            err(where, "empty <title>")
        if not pg.meta.get("description"):
            err(where, "missing meta description")
        canon = pg.links.get("canonical", "")
        expected = SITE + url_of(p)
        if not is_404:
            if canon != expected:
                err(where, f"canonical '{canon}' != expected '{expected}'")
            ogurl = pg.meta.get("og:url", "")
            if ogurl and ogurl != canon:
                warn(where, f"og:url '{ogurl}' differs from canonical '{canon}'")
            ogimg = pg.meta.get("og:image", "")
            if not ogimg:
                err(where, "missing og:image")
            elif ogimg.startswith(SITE) and not site_path(urlparse(ogimg).path):
                err(where, f"og:image file missing: {ogimg}")
            elif ogimg.endswith(".svg"):
                err(where, "og:image is SVG; social platforms need PNG")
            else:
                f = site_path(urlparse(ogimg).path)
                size = png_size(f) if f else None
                declared = (pg.meta.get("og:image:width"), pg.meta.get("og:image:height"))
                if size and all(declared) and declared != (str(size[0]), str(size[1])):
                    err(where, f"og:image is {size[0]}x{size[1]} but the page declares {declared[0]}x{declared[1]}")
        for raw, line in pg.jsonld:
            try:
                data = json.loads(raw)
            except json.JSONDecodeError as e:
                err(where, f"JSON-LD at line {line} does not parse: {e}")
                continue
            blob = json.dumps(data)
            for u in re.findall(r'"(https://npsi\.ca/[^"]*)"', blob):
                if not site_path(urlparse(u).path) and urlparse(u).fragment == "":
                    err(where, f"JSON-LD references missing file: {u}")
        pdf = pg.meta.get("citation_pdf_url")
        if pdf and not site_path(urlparse(pdf).path):
            err(where, f"citation_pdf_url points at a missing file: {pdf}")

        # links ------------------------------------------------------------
        for t, a, line in pg.elements:
            for attr in ("href", "src"):
                u = a.get(attr)
                if not u or t in ("link",) and attr == "href" and a.get("rel") in ("preconnect", "dns-prefetch"):
                    continue
                if u.startswith(("mailto:", "tel:", "data:", "javascript:")):
                    if u.startswith("javascript:"):
                        err(where, f"javascript: URL at line {line}")
                    continue
                parsed_u = urlparse(u)
                if parsed_u.netloc == "github.com" and "/commits/" in parsed_u.path and parsed_u.path.endswith("/"):
                    err(where, f"line {line}: GitHub answers 400 to a commit-history URL with a trailing slash: {u}")
                if parsed_u.scheme in ("http", "https"):
                    if parsed_u.netloc in ("npsi.ca", "www.npsi.ca"):
                        if not site_path(parsed_u.path or "/"):
                            err(where, f"line {line}: absolute npsi.ca link to missing file {u}")
                    else:
                        external.setdefault(u, []).append(f"{where}:{line}")
                    continue
                if u == "#":
                    err(where, f"line {line}: placeholder href=\"#\"")
                    continue
                full = urljoin(url_of(p), u)
                fp = urlparse(full)
                target = site_path(fp.path) if fp.path else p
                if target is None:
                    err(where, f"line {line}: broken internal link {u}")
                    continue
                if fp.fragment and target.suffix == ".html":
                    tpg = parsed.get(target)
                    if tpg is not None and unquote(fp.fragment) not in tpg.ids:
                        err(where, f"line {line}: anchor #{fp.fragment} not found in {url_of(target)}")

        # markup -----------------------------------------------------------
        for b in pg.balance:
            err(where, f"tag balance: {b}")
        for t, l in pg.stack:
            if t not in ("html", "body", "head") and t not in OPTIONAL_END:
                err(where, f"<{t}> opened at line {l} never closed")
        for i, l in pg.dup_ids:
            err(where, f"duplicate id '{i}' at line {l}")
        for t, a, l in pg.elements:
            if t == "img" and "alt" not in a:
                err(where, f"<img> without alt at line {l}")
            st = a.get("style", "")
            if re.search(r"font-size:\s*[\d.]+px", st):
                warn(where, f"line {l}: inline px font-size ({st.strip()}) bypasses the fluid scale")

        # brand ------------------------------------------------------------
        for css, line in pg.styles:
            for m in re.finditer(r"#[0-9A-Fa-f]{3,8}\b", css):
                h = m.group(0).upper()
                if len(h) == 4:
                    h = "#" + "".join(c * 2 for c in h[1:])
                if h not in allowed_hex and h not in ("#FFFFFF", "#000000"):
                    lineno = line + css[: m.start()].count("\n")
                    warn(where, f"line {lineno}: colour {m.group(0)} is not a site.css palette token")
            for m in re.finditer(r"font-family:\s*([^;}]+)", css):
                fams = [f.strip().strip("'\"").lower() for f in m.group(1).split(",")]
                bad = [f for f in fams if f and not f.startswith("var(") and f not in ALLOWED_FONTS]
                if bad:
                    lineno = line + css[: m.start()].count("\n")
                    err(where, f"line {lineno}: font family outside the site faces: {', '.join(bad)}")

        # text -------------------------------------------------------------
        for data, line in pg.text:
            if re.search(r"\b(TODO|TBD|lorem ipsum|XX+)\b|\[citation", data, re.I) and "TBD" not in where:
                warn(where, f"line {line}: placeholder marker in text: {data.strip()[:80]!r}")
            if re.search(r"\bTK\b", data):
                warn(where, f"line {line}: possible 'TK' placeholder: {data.strip()[:80]!r}")
            if "!" in data and not re.search(r"<!|!=|!\[", data):
                warn(where, f"line {line}: exclamation mark in text: {data.strip()[:80]!r}")
            m = re.search(r"\b(\w+)\s+\1\b", data, re.I)
            if m and m.group(1).lower() not in ("that", "had", "is", "no", "very", "bye"):
                warn(where, f"line {line}: doubled word '{m.group(0)}'")

    # links whose text names the current paper must point at it ----------
    cur_re = re.compile(r'<a\s[^>]*href="([^"]+)"[^>]*>\s*current (working )?paper', re.I)
    for p in pages:
        for m in cur_re.finditer(p.read_text(encoding="utf-8")):
            if m.group(1).startswith("#"):
                continue  # in-page jump link
            if current_wp and m.group(1) not in (current_wp, current_wp.rstrip("/")):
                err(p.relative_to(ROOT).as_posix(), f"link labelled 'current paper' points to {m.group(1)}, not {current_wp}")

    # every released PDF is reachable from the home page ------------------
    home_html = (ROOT / "index.html").read_text(encoding="utf-8")
    for pdf in sorted(ROOT.glob("*/*.pdf")):
        if pdf.parent.name in skip:
            continue
        if url_of(pdf) not in home_html:
            err("index.html", f"no download link to {url_of(pdf)}")

    # sitemap -----------------------------------------------------------
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    entries = re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", sm)
    listed = {}
    for loc, lastmod in entries:
        f = site_path(urlparse(loc).path)
        if f is None:
            err("sitemap.xml", f"{loc} does not resolve to a file")
            continue
        listed[f] = loc
        gd = git_date(f)
        if gd and gd != lastmod:
            err("sitemap.xml", f"{loc} lastmod {lastmod} but file last changed {gd}")
    for p in pages:
        if p.name == "404.html":
            continue
        if p not in listed:
            err("sitemap.xml", f"page {url_of(p)} is not listed")
    for pdf in sorted(ROOT.glob("*/*.pdf")):
        if pdf not in listed:
            err("sitemap.xml", f"PDF {url_of(pdf)} is not listed")

    # llms indexes -------------------------------------------------------
    for name in ("llms.txt", "llms-full.txt"):
        txt = (ROOT / name).read_text(encoding="utf-8")
        for p in pages:
            if p.name == "404.html":
                continue
            u = SITE + url_of(p)
            if u not in txt and u.rstrip("/") not in txt:
                warn(name, f"no mention of {u}")

    # external links ------------------------------------------------------
    if args.external:
        ctx = ssl.create_default_context()

        def probe(u: str) -> tuple[str, str]:
            headers = {"User-Agent": "Mozilla/5.0 (npsi.ca sitecheck; editor@npsi.ca)"}
            for method in ("HEAD", "GET"):
                try:
                    req = urllib.request.Request(u, method=method, headers=headers)
                    with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
                        return u, str(r.status)
                except urllib.error.HTTPError as e:
                    if method == "HEAD" and e.code in (403, 405, 400, 404, 429, 501):
                        continue
                    return u, str(e.code)
                except Exception as e:  # noqa: BLE001 - report every failure
                    if method == "HEAD":
                        continue
                    return u, type(e).__name__
            return u, "?"

        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:
            for u, status in ex.map(probe, sorted(external)):
                if not status.startswith(("2", "3")):
                    where = ", ".join(external[u][:3])
                    level = err if status in ("404", "410") else warn
                    level(where, f"external {status}: {u}")

    if not args.quiet:
        print(f"sitecheck: {len(pages)} pages, {len(entries)} sitemap entries, "
              f"{len(external)} distinct external URLs, current paper {current_wp}")
    for line in errors + warns:
        print(line)
    print(f"\n{len(errors)} error(s), {len(warns)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
