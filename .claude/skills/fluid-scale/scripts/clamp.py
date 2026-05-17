#!/usr/bin/env python3
"""
clamp.py — identity-anchored fluid CSS clamp() generator.

Given a size that should be `min` px at viewport `wmin` and `max` px at
viewport `wmax`, emit a CSS custom property whose fluid term is the straight
line through those two anchor points, expressed as `<rem> + <vw>`.

The rem term is always present so the value still responds to the user's
browser font size (WCAG 1.4.4 — text must scale to 200%). A vw-only clamp is
never emitted.

Usage:
    python3 clamp.py --min 32 --max 44 --wmin 360 --wmax 1280 --name fs-h1
    python3 clamp.py --min 16 --max 17 --name fs-body            # default anchors
    python3 clamp.py --batch roles.tsv                           # name<TAB>min<TAB>max per line

No dependencies. Python 3.6+.
"""
import argparse
import sys

ROOT_PX = 16.0  # CSS root font-size assumption (1rem). Do not change lightly.


def clamp(name, lo, hi, wmin, wmax, root_px=ROOT_PX):
    if hi < lo:
        lo, hi = hi, lo
    if wmax == wmin:
        raise ValueError("wmin and wmax must differ")
    # line through (wmin, lo) and (wmax, hi): size = lo + m*(W - wmin)
    m = (hi - lo) / (wmax - wmin)        # px per px-of-viewport
    vw = m * 100.0                       # coefficient in vw units
    rem = (lo - m * wmin) / root_px      # constant part, in rem
    expr = f"clamp({_px(lo)}, {rem:.4g}rem + {vw:.4g}vw, {_px(hi)})"
    prop = name if name.startswith("--") else f"--{name}"
    return f"  {prop}: {expr};"


def _px(v):
    return f"{v:g}px"


def main(argv=None):
    p = argparse.ArgumentParser(description="Identity-anchored fluid clamp() generator")
    p.add_argument("--min", type=float, help="small-screen (floor) value, px")
    p.add_argument("--max", type=float, help="desktop (ceiling) value, px")
    p.add_argument("--wmin", type=float, default=360.0, help="lower anchor viewport px (default 360)")
    p.add_argument("--wmax", type=float, default=1280.0, help="upper anchor viewport px (default 1280)")
    p.add_argument("--name", default="fs-x", help="token name (with or without leading --)")
    p.add_argument("--batch", help="TSV file: name<TAB>min<TAB>max per line")
    a = p.parse_args(argv)

    lines = []
    if a.batch:
        with open(a.batch) as fh:
            for raw in fh:
                raw = raw.strip()
                if not raw or raw.startswith("#"):
                    continue
                name, lo, hi = raw.split("\t")
                lines.append(clamp(name, float(lo), float(hi), a.wmin, a.wmax))
    else:
        if a.min is None or a.max is None:
            p.error("--min and --max are required (or use --batch)")
        lines.append(clamp(a.name, a.min, a.max, a.wmin, a.wmax))

    print(":root {")
    print("\n".join(lines))
    print("}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
