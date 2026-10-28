#!/usr/bin/env python3
"""Tell IndexNow search engines (Bing, Naver, Yandex, Seznam, Yep) that pages changed.

    python3 tools/indexnow.py --since <commit>     # the pages and PDFs changed since that commit
    python3 tools/indexnow.py --all                # every page and PDF in sitemap.xml
    python3 tools/indexnow.py --dry-run --all      # print the list, send nothing

IndexNow lets a site announce a change instead of waiting to be recrawled. One
submission to api.indexnow.org is shared with every participating engine; Bing's
index also feeds Copilot and ChatGPT search. The key is public by design: the
engines confirm ownership by fetching https://npsi.ca/<key>.txt, which holds the key.

Run by .github/workflows/indexnow.yml after each production deploy of main.
Standard library only; repository only.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = "npsi.ca"
KEY = "321437bffbf88535cb7beeaddd237764"
ENDPOINT = "https://api.indexnow.org/indexnow"


def url_for(path: str) -> str | None:
    """A deployed page or PDF path -> its public URL; anything else -> None."""
    if path.startswith((".", "tools/", "figures/")) or path == "404.html":
        return None
    if path == "index.html":
        return f"https://{HOST}/"
    if path.endswith("/index.html"):
        return f"https://{HOST}/{path[: -len('index.html')]}"
    if path.endswith(".pdf"):
        return f"https://{HOST}/{path}"
    if path in ("llms.txt", "llms-full.txt"):
        return f"https://{HOST}/{path}"
    return None


def changed_since(rev: str) -> list[str]:
    out = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AMR", rev, "HEAD"],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    urls = [url_for(p) for p in out.split()]
    return sorted({u for u in urls if u})


def everything() -> list[str]:
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    return sorted(set(re.findall(r"<loc>([^<]+)</loc>", sm)))


def submit(urls: list[str]) -> int:
    body = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": f"https://{HOST}/{KEY}.txt",
        "urlList": urls,
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow: {r.status} for {len(urls)} URL(s)")
            return 0
    except urllib.error.HTTPError as e:
        # 422: URLs not on the host or key mismatch; 403: key file not found yet;
        # 429: too many requests. None of these is worth failing a deploy over.
        print(f"IndexNow: HTTP {e.code} {e.read().decode(errors='replace')[:200]}")
        return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--since", metavar="REV", help="submit pages and PDFs changed since this commit")
    g.add_argument("--all", action="store_true", help="submit every URL in sitemap.xml")
    ap.add_argument("--dry-run", action="store_true", help="print the URLs, send nothing")
    a = ap.parse_args()
    urls = everything() if a.all else changed_since(a.since)
    for u in urls:
        print(u)
    if not urls:
        print("IndexNow: nothing to submit")
        return 0
    if a.dry_run:
        return 0
    return submit(urls[:10000])


if __name__ == "__main__":
    sys.exit(main())
