#!/usr/bin/env python3
"""Write the full text of every published document as Markdown, for machine readers.

    python3 tools/fulltext.py            # write <folder>/index.html.md for every document
    python3 tools/fulltext.py --check    # fail if any file is missing or out of date

Each document's reading view (<folder>/index.html) is converted to clean Markdown at
<folder>/index.html.md, the address the llms.txt convention gives the Markdown edition of
a page whose URL ends in a slash. An agent reading /sb10/index.html.md gets the text,
tables, sources and figure descriptions without the styling, navigation and inline SVG,
at a fraction of the size, with the citation, licence and canonical URL stated in its
front matter.

The Markdown is derived, never edited by hand: registry.py --all regenerates it, and
--check (run by registry.py --check, and so by sitecheck.py) fails when a page has
changed and its Markdown has not. The reading view and the PDF remain the editions of
record. Figures are given as their accessible descriptions (the SVG's aria-label).
Repository only; the .md files it writes are deployed.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://npsi.ca"
LICENCE = "https://creativecommons.org/licenses/by/4.0/"

BLOCK = {
    "p", "div", "section", "article", "aside", "figure", "figcaption", "header", "footer",
    "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li", "dl", "dt", "dd", "table",
    "thead", "tbody", "tfoot", "tr", "td", "th", "caption", "colgroup", "col",
    "blockquote", "hr", "pre", "nav", "details", "summary", "main",
}
VOID = {"br", "hr", "img", "col", "meta", "link", "input", "wbr", "source"}
SKIP_TAGS = {"script", "style", "button", "template", "noscript"}
SKIP_CLASSES = {"doc-nav", "toc", "meridian", "wp-card-actions"}


class Node:
    __slots__ = ("tag", "attrs", "children", "parent")

    def __init__(self, tag: str, attrs: dict, parent: "Node | None") -> None:
        self.tag, self.attrs, self.children, self.parent = tag, attrs, [], parent

    @property
    def classes(self) -> set[str]:
        return set((self.attrs.get("class") or "").split())


class Tree(HTMLParser):
    """A forgiving DOM: enough structure to walk <main> in order."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", {}, None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag, {k: (v or "") for k, v in attrs}, self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, {k: (v or "") for k, v in attrs}, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def find(node: Node, tag: str) -> Node | None:
    for c in node.children:
        if isinstance(c, Node):
            if c.tag == tag:
                return c
            hit = find(c, tag)
            if hit:
                return hit
    return None


def skipped(n: Node) -> bool:
    return (
        n.tag in SKIP_TAGS
        or bool(n.classes & SKIP_CLASSES)
        or n.attrs.get("aria-hidden") == "true"
        or "hidden" in n.attrs
    )


def absolute(href: str, base: str) -> str:
    if href.startswith(("http://", "https://", "mailto:")):
        return href
    if href.startswith("/"):
        return SITE + href
    return SITE + base + href


def is_block(n) -> bool:
    if not isinstance(n, Node):
        return False
    if n.tag in BLOCK:
        return True
    return any(is_block(c) for c in n.children)


class Renderer:
    def __init__(self, base: str) -> None:
        self.base = base  # the document's path, e.g. /sb10/

    # inline -------------------------------------------------------------------
    def inline(self, nodes) -> str:
        out = []
        for n in nodes:
            if isinstance(n, str):
                out.append(re.sub(r"\s+", " ", n.replace(" ", " ")))
                continue
            if skipped(n):
                continue
            t = n.tag
            if t == "br":
                out.append("  \n")
            elif t == "svg":
                out.append(self.svg_label(n))
            elif t == "img":
                alt = n.attrs.get("alt", "").strip()
                if alt:
                    out.append(f"![{alt}]({absolute(n.attrs.get('src', ''), self.base)})")
            elif t == "cite" and n.parent is not None and n.parent.tag == "blockquote":
                out.append("  \n— " + wrap(self.inline(n.children).strip(), "*"))
            elif t in ("em", "i", "cite"):
                out.append(wrap(self.inline(n.children), "*"))
            elif t in ("strong", "b"):
                out.append(wrap(self.inline(n.children), "**"))
            elif t == "s":
                out.append(wrap(self.inline(n.children), "~~"))
            elif t == "code":
                inner = self.inline(n.children).strip()
                out.append(f"`{inner}`" if inner else "")
            elif t == "sup":
                inner = self.inline(n.children).strip()
                out.append(f"[{inner}]" if inner.isdigit() else f"^{inner}")
            elif t == "q":
                out.append(f"“{self.inline(n.children).strip()}”")
            elif t == "a":
                text = self.inline(n.children).strip()
                href = n.attrs.get("href", "")
                if not href or href.startswith("#") or not text:
                    out.append(text)
                else:
                    url = absolute(href, self.base)
                    out.append(text if text == url else f"[{text}]({url})")
            else:
                out.append(self.inline(n.children))
        return "".join(out)

    def svg_label(self, n: Node) -> str:
        label = n.attrs.get("aria-label", "").strip()
        if not label:
            title = find(n, "title")
            label = self.inline(title.children).strip() if title else ""
        return f"[Figure: {label}]" if label else ""

    # blocks -------------------------------------------------------------------
    def blocks(self, n: Node) -> list[str]:
        """Render a container's children as a list of Markdown blocks."""
        out: list[str] = []
        run: list = []

        def flush():
            text = escape_lead(clean(self.inline(run)))
            if text:
                out.append(text)
            run.clear()

        for c in n.children:
            if isinstance(c, Node) and skipped(c):
                continue
            if isinstance(c, Node) and c.tag == "svg":
                flush()
                label = self.svg_label(c)
                if label:
                    out.append(label)
            elif is_block(c):
                flush()
                out.extend(self.block(c))
            else:
                run.append(c)
        flush()
        return out

    def block(self, n: Node) -> list[str]:
        t = n.tag
        if t in ("h1", "h2", "h3", "h4", "h5", "h6"):
            text = clean(self.inline(n.children))
            return [f"{'#' * int(t[1])} {text}"] if text else []
        if t == "hr":
            return ["---"]
        if t in ("ul", "ol"):
            return [self.list_(n)]
        if t == "dl":
            return [self.dl(n)]
        if t == "table":
            return self.table(n)
        if t == "blockquote":
            inner = "\n\n".join(self.blocks(n))
            return ["\n".join("> " + line if line else ">" for line in inner.split("\n"))]
        if t == "pre":
            return ["```\n" + text_of(n).strip("\n") + "\n```"]
        if t == "figcaption":
            text = "\n\n".join(self.blocks(n))
            return [text] if text else []
        return self.blocks(n)

    def list_(self, n: Node) -> str:
        ordered = n.tag == "ol"
        start = int(n.attrs.get("start") or 1) if ordered else 1
        lines = []
        i = start
        for li in n.children:
            if not isinstance(li, Node) or li.tag != "li" or skipped(li):
                continue
            parts = self.blocks(li)
            if not parts:
                continue
            marker = f"{i}." if ordered else "-"
            pad = " " * (len(marker) + 1)
            body = "\n\n".join(parts).split("\n")
            lines.append(f"{marker} {body[0]}")
            lines.extend((pad + line) if line else "" for line in body[1:])
            i += 1
        return "\n".join(lines)

    def dl(self, n: Node) -> str:
        lines, term = [], None
        for c in n.children:
            if not isinstance(c, Node) or skipped(c):
                continue
            if c.tag == "dt":
                term = clean(self.inline(c.children))
            elif c.tag == "dd":
                body = " ".join(self.blocks(c))
                lines.append(f"- **{term}:** {body}" if term else f"- {body}")
                term = None
            elif c.tag == "div":  # <div><dt/><dd/></div> groupings
                inner = self.dl(c)
                if inner:
                    lines.append(inner)
        return "\n".join(lines)

    def table(self, n: Node) -> list[str]:
        out = []
        cap = find(n, "caption")
        if cap:
            text = clean(self.inline(cap.children))
            if text:
                out.append(f"*{text}*")
        rows = []
        for tr in iter_rows(n):
            cells = []
            for c in tr.children:
                if isinstance(c, Node) and c.tag in ("td", "th") and not skipped(c):
                    text = " ".join(self.blocks(c)).replace("\n", " ").replace("|", "\\|")
                    cells.append(text.strip())
                    for _ in range(int(c.attrs.get("colspan") or 1) - 1):
                        cells.append("")
            if cells:
                rows.append(cells)
        if not rows:
            return out
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        out.append("\n".join(
            ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
            + ["| " + " | ".join(r) + " |" for r in rows[1:]]
        ))
        return out


def iter_rows(n: Node):
    for c in n.children:
        if isinstance(c, Node):
            if c.tag == "tr":
                yield c
            elif c.tag in ("thead", "tbody", "tfoot"):
                yield from iter_rows(c)


def text_of(n) -> str:
    if isinstance(n, str):
        return n
    return "".join(text_of(c) for c in n.children)


def wrap(text: str, mark: str) -> str:
    stripped = text.strip()
    if not stripped:
        return text
    lead = text[: len(text) - len(text.lstrip())]
    trail = text[len(text.rstrip()):]
    return f"{lead}{mark}{stripped}{mark}{trail}"


def escape_lead(text: str) -> str:
    """Keep a paragraph that opens with Markdown syntax (">99%", "1. ", "# ") a paragraph."""
    out = []
    for line in text.split("\n"):
        m = re.match(r"(\d+)([.)]\s)", line)
        if m:
            line = m.group(1) + "\\" + line[len(m.group(1)):]
        elif re.match(r"(>|#{1,6}\s|[-+*]\s)", line):
            line = "\\" + line
        out.append(line)
    return "\n".join(out)


def clean(text: str) -> str:
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    joined = "\n".join(lines).strip()
    return joined.replace(" \n", "  \n") if "  \n" in text else joined


# front matter -------------------------------------------------------------------

def registry() -> dict:
    return json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))


def label(d: dict, lines: dict) -> str:
    if d["line"] == "PL":
        return f"The Pacific Ledger №{d['number']:02d}"
    return f"NPSI {lines[d['line']]['singular']} No. {d['number']}"


def yaml_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def front_matter(d: dict, reg: dict, page: str) -> str:
    lines = reg["lines"]
    url = SITE + d["url"]
    ident = d["serial"] or f"{d['accession']} (accession number; publication serial pending)"
    desc = re.search(r'<meta name="description" content="([^"]*)"', page)
    year = (d.get("released") or "")[:4]
    version = d.get("version") or "as issued"
    cite_id = d["serial"] or d["accession"]
    cite = (f"James, J. ({year}). {d['title']} ({label(d, lines)}, {cite_id}"
            f"{', ' + d['version'] if d.get('version') else ''}). "
            f"North Pacific Strategy Initiative. {url}")
    fm = [
        "---",
        f"title: {yaml_str(d['title'])}",
    ]
    if d.get("subtitle"):
        fm.append(f"subtitle: {yaml_str(d['subtitle'])}")
    fm += [
        f"series: {yaml_str(lines[d['line']]['name'])}",
        f"number: {d['number']}",
        f"identifier: {yaml_str(ident)}",
        f"version: {yaml_str(version)}",
        f"published: {yaml_str(d.get('released') or '')}",
        f"status: {d['status']}",
    ]
    if d.get("superseded_by"):
        fm.append(f"superseded_by: {yaml_str(SITE + '/' + d['superseded_by'] + '/')}")
    if d.get("supersedes"):
        fm.append(f"supersedes: {yaml_str(SITE + '/' + d['supersedes'] + '/')}")
    fm += [
        'author: "Jesse James"',
        'publisher: "North Pacific Strategy Initiative"',
        f"canonical_url: {yaml_str(url)}",
    ]
    if d.get("files"):
        fm.append("pdf:")
        fm += [f"  - {yaml_str(SITE + f)}" for f in d["files"]]
    if desc:
        fm.append(f"description: {yaml_str(html.unescape(desc.group(1)))}")
    fm += [
        f'license: "CC-BY-4.0 ({LICENCE})"',
        f"cite_as: {yaml_str(cite)}",
        "---",
        "",
        f"> Machine-readable full text of {label(d, lines)}, *{d['title']}*, from the reading view at "
        f"{url}. The reading view and the PDF are the editions of record; figures are given as their "
        "text descriptions. The text is licensed CC-BY-4.0: quote it, summarise it, translate it, "
        "share it and use it, including in AI systems and their answers, with attribution to the "
        f"author and a link to {url}. The NPSI name and wordmark are not licensed. Register of every "
        "NPSI document: https://npsi.ca/registry.json · index for machine readers: https://npsi.ca/llms.txt",
        "",
    ]
    return "\n".join(fm)


def render(d: dict, reg: dict) -> str:
    page = (ROOT / d["folder"] / "index.html").read_text(encoding="utf-8")
    tree = Tree()
    tree.feed(page)
    main = find(tree.root, "main")
    body = "\n\n".join(Renderer(d["url"]).blocks(main))
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return front_matter(d, reg, page) + "\n" + body + "\n"


def published(reg: dict) -> list[dict]:
    return [d for d in reg["documents"] if d.get("status") in ("published", "current", "superseded")]


def write(reg: dict) -> None:
    for d in published(reg):
        out = ROOT / d["folder"] / "index.html.md"
        out.write_text(render(d, reg), encoding="utf-8")
    print(f"fulltext: {len(published(reg))} Markdown editions written")


def check(reg: dict) -> int:
    errors = 0
    for d in published(reg):
        out = ROOT / d["folder"] / "index.html.md"
        if not out.exists() or out.read_text(encoding="utf-8") != render(d, reg):
            print(f"ERROR {out.relative_to(ROOT)} is missing or out of date; run tools/fulltext.py")
            errors += 1
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="fail if any Markdown edition is missing or stale")
    a = ap.parse_args()
    reg = registry()
    if a.check:
        return 1 if check(reg) else 0
    write(reg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
