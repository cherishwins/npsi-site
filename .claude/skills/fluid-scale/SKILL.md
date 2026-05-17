---
name: fluid-scale
description: >-
  Identity-anchored fluid responsive design system. Converts hard-pixel
  typography and spacing into a single continuous clamp() scale where each
  clamp's MAX equals the brand's existing desktop value and its MIN equals the
  existing small-screen value — so a live, brand-locked product renders
  pixel-identical at both anchor widths and only gains smooth interpolation in
  between (zero visual risk to adopt). Bundles ch-based measure, ISO-216 / A4
  print, accessibility-safe zoom (mandatory rem term), and palette / zero-JS
  guardrails, plus a clamp generator script and a review checklist. Use when
  building or auditing responsive CSS; designing a type or spacing scale; fluid
  typography; viewport / iPhone scaling; clamp(); modular scale; print
  stylesheets; or migrating an existing brand to fluid type without a redesign.
license: Complete terms in LICENSE.txt
metadata:
  npsi.origin: cherishwins/npsi-site
  npsi.version: "1.0"
---

# Fluid Scale — identity-anchored responsive system

The technique (fluid type via `clamp()`, modular scale, ISO 216) is public
prior art — Utopia.fyi, Tim Brown's modular scale, the ISO 216 √2 paper ratio.
**What this skill encodes is the discipline, not the math:** a repeatable
protocol to make fluid scaling *safe to adopt on an existing brand* and to keep
it accessible, print-correct, and JS-free. Apply it verbatim; do not improvise.

## When to use

- Any responsive CSS work: type scale, spacing rhythm, container padding.
- Migrating a hard-pixel + media-query stylesheet to fluid scaling.
- A brand-locked product where a visual redesign is **not** wanted, but
  in-between/large/small viewports look bad.
- Writing or fixing a print stylesheet for document-grade output.

## When NOT to use

- Greenfield with no established sizes and no brand constraint — a plain
  modular scale (pick a ratio, e.g. 1.2) is simpler; you don't need anchoring.
- Pixel-art / canvas / fixed-canvas layouts where scaling is undesirable.

## The core idea: identity-anchored clamp

A naive fluid scale picks arbitrary min/max and **changes how the site looks**.
On a live brand that is a redesign and a risk. Instead:

> For every size, set `clamp()` so **`max` = the current desktop value** and
> **`min` = the current small-screen value**. The two anchor widths then render
> *pixel-identical to today*. You only add smooth interpolation between them
> and graceful behaviour below the small anchor. Nothing a stakeholder has
> approved changes. Adoption is reversible and review-trivial.

This is the whole differentiator. Preserve it.

## The math (exact, not hand-tuned)

Given a size that should be `minPx` at viewport `Wmin` and `maxPx` at viewport
`Wmax`, the fluid middle term is the line through those two points:

```
slope  m   = (maxPx - minPx) / (Wmax - Wmin)        # px per px-of-viewport
vw term     = m * 100                                # in vw units
rem term    = (minPx - m * Wmin) / ROOT_PX           # ROOT_PX = 16
result      = clamp(minPx, <rem>rem + <vw>vw, maxPx)
```

**The `rem` term is mandatory.** A `clamp()` whose fluid part is *vw only*
does not respond to the user's browser font-size and fails WCAG 1.4.4
(text must scale to 200%). Always keep the `rem` component — it carries the
user's zoom; `vw` carries the viewport. Never emit a vw-only clamp.

Use the bundled generator instead of doing this by hand:

```
python3 scripts/clamp.py --min 32 --max 44 --wmin 360 --wmax 1280 --name fs-h1
# → --fs-h1: clamp(32px, 1.707rem + 1.304vw, 44px);
```

Run it once per size and paste the tokens into `:root`.

## Procedure

1. **Inventory.** Read the existing stylesheet. For each role (body, lede,
   h1, h1-large, subtitle, h2/h3, card title, prose, section gap, opener gap,
   container padding) record two numbers: the **desktop** value and the
   **small-screen** value (usually whatever the `max-width` media query
   already declares). These are your anchors — they are the approved identity.
2. **Pick anchor viewports.** Default `Wmin = 360`, `Wmax = 1280`. Use the
   project's real min device width if it differs (e.g. 320).
3. **Generate tokens.** Run `scripts/clamp.py` for every role. Put all of them
   in `:root` as `--fs-*` (type) and `--space-*` (rhythm). Make container
   padding fluid too: `--pad-x: clamp(<mob>px, <slope>vw, <desk>px)`.
4. **Wire up.** Replace every hard-pixel `font-size` / spacing with
   `var(--…)`. One declaration per role, no duplicates.
5. **Collapse the media query.** Delete every per-breakpoint `font-size`
   override — the scale handles them now. The remaining `@media` block must be
   **layout-only**: stack flex containers, drop multi-column grids to one
   column, hide non-essential chrome. This is a net code reduction; if the
   media block didn't shrink, something was left hard-coded.
6. **Measure.** Set the prose container max-width in **`ch`**, not px:
   `--max-w: 70ch` (keep line length in the 66–75ch readability band at any
   zoom). Wide/layout containers may stay in px.
7. **Print.** Paste the A4 block (below) — do not write an ad-hoc one.
8. **Accessibility pass.** Apply the guardrail block (below).
9. **Verify.** Serve locally; confirm at `Wmin`, `Wmax`, and one mid width
   (e.g. 768) plus 200% browser zoom. The two anchors must match the old
   design exactly.

## ISO-216 / A4 print block (paste verbatim)

```css
@page { size: A4; margin: 18mm 16mm; }
@media print {
  html { scroll-behavior: auto; }
  /* hide interactive chrome */
  .masthead, .site-footer, nav, .wp-card-actions, .toc { display: none; }
  body { background: #fff; color: #000; font-size: 10.5pt; line-height: 1.5; }
  main { max-width: 100%; padding: 0; }
  a { color: #000; border-bottom: none; }
  /* surface external destinations on paper */
  .prose a[href^="http"]::after { content: " <" attr(href) ">";
    font-size: 8pt; color: #555; word-break: break-all; }
  h1, h2, h3, h4 { color: #000; break-after: avoid; }
  p, blockquote, li { orphans: 3; widows: 3; }
  blockquote, figure, .card, .pull { break-inside: avoid; }
}
```

Document proportion token, for any element that must hold true A4 shape
(covers, framed figures) without layout shift:

```css
:root { --ratio-a4: 1 / 1.4142; }   /* ISO 216, the Lichtenberg √2 ratio */
.aspect-a4 { aspect-ratio: var(--ratio-a4); }
```

Note: US **Letter** (8.5×11, ratio ≈ 1.294) is *not* √2 and is not
self-similar under folding. Standardise on A4 for document output; only switch
to Letter if a North-American print workflow explicitly requires it.

## Accessibility & reliability guardrails (always include)

```css
html { scroll-padding-top: 96px; }        /* sticky-header anchor fix; tune to header height */
:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
  }
}
h1, h2, h3, .card-title { text-wrap: balance; }
p, .lede { text-wrap: pretty; }
.prose { overflow-wrap: break-word; hyphens: auto; }   /* long technical strings on mobile */
```

## Hard guardrails

- **Keep the `rem` term in every clamp.** Vw-only = broken zoom. Non-negotiable.
- **No new colours, no new typefaces, no JavaScript.** This skill is a CSS-only
  transform. If a brand spec defines a palette, the scale must not touch it.
- **No per-breakpoint `font-size`.** The whole point is one continuous source
  of truth. If you're tempted to add `@media { h1 { font-size: … } }`, you've
  abandoned the system.
- **Anchors are the approved identity.** Do not "improve" the desktop or mobile
  values while migrating — that smuggles a redesign past review. Migrate first
  (identical at anchors), propose value changes separately.
- **Document the system** in the project's CLAUDE.md / style guide so future
  edits add `clamp()` tokens instead of reintroducing pixels.

## Review checklist

- [ ] Every type/space role is a single `var(--…)` backed by a `clamp()` token.
- [ ] Every clamp has a `rem` term (zoom-safe) and `px` floor/ceiling.
- [ ] `max` == prior desktop value; `min` == prior small-screen value (spot-check 3).
- [ ] `@media` block contains layout only — zero `font-size` declarations.
- [ ] Prose width in `ch`, in the 66–75ch band.
- [ ] `@page { size: A4 }` present; pull-quotes/figures/cards `break-inside: avoid`.
- [ ] `scroll-padding-top`, `:focus-visible`, `prefers-reduced-motion` present.
- [ ] No new colour/font/JS introduced.
- [ ] Rendered identical to old design at both anchor widths + at 200% zoom.
- [ ] System documented in the project's memory file.

## Canonical reference implementation

`reference/npsi-tokens.css` is the production `:root` block from
`cherishwins/npsi-site` — a correct, shipped instance of this protocol. Use it
as the shape to emit; regenerate the numbers per project with `scripts/clamp.py`.
