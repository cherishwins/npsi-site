#!/usr/bin/env python3
"""Fill missing document metadata (Title, Author, Subject, Keywords) in the release PDFs.

    python3 tools/pdf-metadata.py            # report what each PDF carries and what would change
    python3 tools/pdf-metadata.py --write    # write the missing fields

Search engines, Google Scholar, reference managers and AI systems read a PDF's own
Title and Author before anything else; a PDF without them is listed under its file
name, and the WP1 essay edition named its author "python-docx". This tool fills only
fields that are empty or carry a tool's name, from the register and the document
page (title, number, subtitle, citation_keywords). It never touches a page: the
content streams are rewritten byte-for-byte as they were, and --write checks that
every page's extracted text is unchanged.

WP10 is skipped: it remains available unaltered, by its successor's commitment.
Needs pikepdf (pip install pikepdf) and pdftotext; repository only.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import pikepdf

ROOT = Path(__file__).resolve().parent.parent
UNALTERED = {"wp10"}          # never edited, not even its metadata
TOOL_NAMES = re.compile(r"^(python-docx|microsoft word.*|untitled|document\d*|)$", re.I)


def label(d: dict, lines: dict) -> str:
    if d["line"] == "PL":
        return f"The Pacific Ledger №{d['number']:02d}"
    return f"NPSI {lines[d['line']]['singular']} No. {d['number']}"


def wanted(d: dict, lines: dict, pdf: Path) -> dict:
    page = (ROOT / d["folder"] / "index.html").read_text(encoding="utf-8")
    kw = re.search(r'<meta name="citation_keywords" content="([^"]*)"', page)
    title = d["title"]
    if pdf.stem == "contractor-checklist":   # SB10's companion is its own title
        title = "Before the First of January"
    full = (f"{label(d, lines)} · North Pacific Strategy Initiative" if d["line"] == "PL"
            else f"{title} · {label(d, lines)}")
    return {
        "/Title": full,
        "/Author": "Jesse James",
        "/Subject": (d.get("subtitle") or "").strip(),
        "/Keywords": html.unescape(kw.group(1)).replace(";", ",") if kw else "",
    }


def text_of(pdf: Path) -> str:
    return subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True,
                          text=True, check=True).stdout


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--write", action="store_true", help="write the missing fields")
    a = ap.parse_args()
    reg = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
    changed = 0
    for d in reg["documents"]:
        if d["folder"] in UNALTERED:
            continue
        for f in d["files"]:
            pdf = ROOT / f.lstrip("/")
            want = wanted(d, reg["lines"], pdf)
            with pikepdf.open(pdf) as doc:
                info = {k: str(v) for k, v in doc.docinfo.items()}
                fill = {k: v for k, v in want.items()
                        if v and TOOL_NAMES.match(info.get(k, "").strip())}
                if not fill:
                    continue
                changed += 1
                print(f"{f}: " + "; ".join(f"{k[1:]} = {v[:60]!r}" for k, v in fill.items()))
                if not a.write:
                    continue
                before = text_of(pdf)
                for k, v in fill.items():
                    doc.docinfo[k] = v
                with doc.open_metadata(set_pikepdf_as_editor=False) as xmp:
                    xmp.load_from_docinfo(doc.docinfo, delete_missing=False)
                with tempfile.NamedTemporaryFile(suffix=".pdf", dir=pdf.parent, delete=False) as tmp:
                    out = Path(tmp.name)
                doc.save(out, preserve_pdfa=True)
            if text_of(out) != before:
                out.unlink()
                print(f"ERROR {f}: text changed on save; left as it was")
                return 1
            out.replace(pdf)
    print(f"{changed} PDF(s) {'updated' if a.write else 'to update (run with --write)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
