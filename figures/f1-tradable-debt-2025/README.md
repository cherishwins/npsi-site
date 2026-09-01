# Figure 1 · World tradable debt, 2025

Treemap of debt securities outstanding by country or region of issuer at
year-end 2025, with a decade-shift strip comparing 2015 and 2025.

## Build

```sh
python3 gen.py index.html   # regenerate the HTML from the data
./render.sh figure.png      # render to a 1200x1500 PNG
```

`gen.py` holds the data in `SERIES` and `DECADE`. Everything else on the
figure is computed from it: shares, the US-to-EU ratio, the margin over the
EU and China combined, the four-largest subtotal, bar widths, decade deltas,
and the treemap geometry. Change a number in one place and the whole figure
follows.

## Why it is generated rather than hand-built

The first version of this figure was hand-built, and carried two claims that
did not reconcile against its own cells: it said the United States held
`+$1.3T` more than the EU and China combined when the cells give `+$1.4T`,
and that the four largest issuers held `$131.8T` while printing `$131.9T, or
82.1%`. Both came from computing prose against unrounded source figures while
the cells showed rounded ones. Deriving every figure from one table removes
that whole class of defect.

Cell areas were also off. Hand-placement had the smaller rectangles running
10 to 35 percent under their true area, so the treemap did not mean what it
said. The layout is now solved from a grouping tree, and `gen.py` prints
area-against-value for every cell on each run.

## Rendering gotcha

`render.sh` uses a **1200x1600** viewport and crops to 1500. Rendering
headless Chromium at a viewport exactly equal to the page height silently
drops the last band: the NPSI wordmark and signature block paint zero pixels
while still reporting `visibility: visible` and correct geometry to
`getComputedStyle`. If the wordmark goes missing from a render, this is why.

## Checks that run on each build

- `gen.py` prints every derived claim, and cell area against cell value.
- `gen.py` prints the contrast ratio of every fill and ink pair. All must
  clear 4.5:1. This is why Bronze is not a series fill; against Cream or
  Navy it reaches only 3.7:1.
- Overflow audit: no cell content may exceed its box. Run it with
  `audit.js` injected before `</body>` and read `document.title`.

## Sources

Bank for International Settlements debt securities statistics, as compiled in
the SIFMA Capital Markets Fact Book, 2026 edition, Tables 1 and 2. US
Treasury securities outstanding from Table 27.

The 2026 edition is confirmed to exist and to be the current one. The
individual table numbers and values have **not** been checked against the
Fact Book itself and should be before the figure is published.

## Colour

Navy ground, per §3 "Two grounds" of `NPSI-brand-specification.md`. The
series ramp is Cream primary, Teal secondary, Deep Teal tertiary, which is
the navy-ground inversion of the Navy/Bronze/Teal order in that section.
