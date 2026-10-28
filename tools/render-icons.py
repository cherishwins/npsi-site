#!/usr/bin/env python3
"""Render the NPSI square mark: favicon SVG, root favicon.ico and the PNG icons.

    python3 tools/render-icons.py

The NP monogram is drawn as outlined paths taken from the vendored Source Serif 4
Bold (tools/fonts/), so every browser, tab and platform shows the brand face. An SVG
favicon cannot load web fonts: with live <text> it fell back to whatever serif the
reader's system had.

Two layouts of the same mark, on the dark identity (cream NP, bronze meridian, navy):

  tab   the small-size layout: NP fills about three-quarters of the square so it
        reads at 16 px. Written to assets/img/favicon.svg, favicon-32.png,
        favicon.png (48 px) and /favicon.ico (16, 32, 48), which non-browser
        clients such as feed readers, chat unfurlers and search favicon fetchers
        request at the root.
  app   the home-screen layout, with generous clear space: apple-touch-icon.png
        (180), icon-192.png and icon-512.png. The 512 is also the manifest's
        maskable icon (the mark sits inside Android's 80% safe circle) and the
        logo the JSON-LD names for the imprint; npsi-logo-1080.png is the same
        mark for profiles and directories that want a larger square logo.

Needs fontTools and Pillow (pip install fonttools pillow) and resvg (fetched by npx,
as tools/render-og.sh does). Repository only; never deployed.
"""
from __future__ import annotations

import io
import subprocess
import tempfile
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"
FONT = ROOT / "tools" / "fonts" / "SourceSerif4-Bold.ttf"

NAVY, CREAM, BRONZE = "#081C30", "#F4EFE3", "#C08D60"


def monogram(scale: float, x: float, baseline: float, tracking: float = 0.0) -> str:
    """SVG path data for 'NP' with its left ink edge at x and its baseline at baseline."""
    font = TTFont(FONT)
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]
    n, p = cmap[ord("N")], cmap[ord("P")]
    lsb = hmtx[n][1]
    pen = SVGPathPen(glyphs)
    cursor = x - lsb * scale
    for name in (n, p):
        # font units are y-up; flip into SVG space
        glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, cursor, baseline)))
        cursor += hmtx[name][0] * scale + tracking
    return pen.getCommands()


def ink_width(scale: float, tracking: float = 0.0) -> float:
    font = TTFont(FONT)
    cmap, hmtx = font.getBestCmap(), font["hmtx"]
    n, p = cmap[ord("N")], cmap[ord("P")]
    xmax_p = font["glyf"][p].xMax
    return (hmtx[n][0] - hmtx[n][1]) * scale + tracking + xmax_p * scale


def mark_svg(layout: str) -> str:
    cap = 657  # Source Serif 4 Bold cap height in font units (N and P top at 657)
    if layout == "tab":
        scale, tracking = 0.0172, 0.0
        width = ink_width(scale, tracking)
        x0 = (32 - width) / 2
        rule_y, tick, mid, stroke = 8.6, 1.9, 1.2, 1.3
        baseline = 25.0
    else:  # app: the proportions of the original square mark
        scale, tracking = 0.011, 0.5
        width = ink_width(scale, tracking)
        x0 = (32 - width) / 2
        rule_y, tick, mid, stroke = 13.0, 1.5, 1.2, 0.75
        baseline = 24.0
    x1 = x0 + width
    if layout == "app":
        x0r, x1r = 6.0, 26.0
    else:
        x0r, x1r = x0, x1
    xm = (x0r + x1r) / 2
    d = monogram(scale, x0, baseline, tracking)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <title>North Pacific Strategy Initiative</title>
  <rect width="32" height="32" fill="{NAVY}"/>
  <g stroke="{BRONZE}" stroke-width="{stroke}">
    <line x1="{x0r:.2f}" y1="{rule_y}" x2="{x1r:.2f}" y2="{rule_y}"/>
    <line x1="{x0r:.2f}" y1="{rule_y - tick:.2f}" x2="{x0r:.2f}" y2="{rule_y + tick:.2f}"/>
    <line x1="{xm:.2f}" y1="{rule_y - mid:.2f}" x2="{xm:.2f}" y2="{rule_y + mid:.2f}"/>
    <line x1="{x1r:.2f}" y1="{rule_y - tick:.2f}" x2="{x1r:.2f}" y2="{rule_y + tick:.2f}"/>
  </g>
  <path fill="{CREAM}" d="{d}"/>
</svg>
"""


def rasterise(svg: str, size: int) -> Image.Image:
    with tempfile.TemporaryDirectory() as tmp:
        src, out = Path(tmp) / "mark.svg", Path(tmp) / "mark.png"
        src.write_text(svg, encoding="utf-8")
        subprocess.run(
            ["npx", "--yes", "resvg-cli", "--no-system-font", "--fit-width", str(size), str(src), str(out)],
            check=True, capture_output=True,
        )
        return Image.open(io.BytesIO(out.read_bytes())).convert("RGBA")


def save_png(img: Image.Image, path: Path) -> None:
    img.convert("RGB").save(path, optimize=True)
    print(f"wrote {path.relative_to(ROOT)} ({img.width}x{img.height})")


def main() -> None:
    tab, app = mark_svg("tab"), mark_svg("app")
    (IMG / "favicon.svg").write_text(tab, encoding="utf-8")
    print("wrote assets/img/favicon.svg")
    save_png(rasterise(tab, 32), IMG / "favicon-32.png")
    save_png(rasterise(tab, 48), IMG / "favicon.png")
    sizes = [rasterise(tab, s).convert("RGB") for s in (48, 32, 16)]
    sizes[0].save(ROOT / "favicon.ico", sizes=[(48, 48), (32, 32), (16, 16)], append_images=sizes[1:])
    print("wrote favicon.ico (48, 32, 16)")
    save_png(rasterise(app, 180), IMG / "apple-touch-icon.png")
    save_png(rasterise(app, 192), IMG / "icon-192.png")
    save_png(rasterise(app, 512), IMG / "icon-512.png")
    # The square logo for profiles and directories (Google Business Profile,
    # ORCID, Zenodo, LinkedIn): 1080 px, saved unoptimised so the file stays
    # above the 10 KB floor some uploaders enforce.
    logo = rasterise(app, 1080).convert("RGB")
    logo.save(IMG / "npsi-logo-1080.png")
    print(f"wrote assets/img/npsi-logo-1080.png ({logo.width}x{logo.height})")


if __name__ == "__main__":
    main()
