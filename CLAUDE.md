# CLAUDE.md

> This file is read by Claude Code at the start of every session in this repository. Keep it accurate. When the project's structure or conventions change, update this file in the same commit.

## What this repository is

The institutional website of the **North Pacific Strategy Initiative (NPSI)** — an independent research imprint publishing reference-grade working papers on Pacific sovereignty, bilateral financial architecture, and the defensive options available to middle powers in a period of dollar-system stress.

**Live at:** `npsi.ca` — registered for ten years through CIRA, the canonical domain. The `.ca` is strategic, not a fallback: CIRA verifies Canadian presence (blocks typosquatters by registry policy), the long registration signals permanence, and the domain matches the imprint's editorial seat in Victoria, BC. Defensive redirects from `npsi.org` and similar are optional, not required.
**Editor:** Jesse James (`editor@npsi.ca`). Standardized June 2026 (PR #24): all site-facing editorial correspondence — footers, JSON-LD, commentary mailtos, security.txt, humans.txt, CITATION.cff — uses the institutional alias `editor@npsi.ca`. The `commentary@npsi.ca` alias remains reserved for future activation. The personal address `jesse@fitforgov.com` no longer appears on the site.
**LinkedIn:** [`linkedin.com/company/north-pacific-strategy-initiative`](https://www.linkedin.com/company/north-pacific-strategy-initiative/) — the imprint's institutional social presence.
**Scope of the site:** 18 pages plus a 404 — home, nine working-paper views (No. 1 *The Bilateral Foundation*, No. 2, No. 3, No. 4 *The Addition Paradox*, No. 5 *Sovereign Compute North*, No. 7 *Dazzle 2.0*, No. 9 *The Counterparty Problem*, No. 10 *Fair Use for We, IP Theft for Thee*, No. 11 *Rated AAA by the Issuer*), one technical-briefing reading view (TB No. 1 *The Verified Sky*), one briefing-note reading view (BN No. 1 *The Voter File*), two special-briefing views (SB No. 1 *Zero Secrets*, SB No. 2 *The Three Doors*), about, engage, commentary index, colophon. Static HTML and CSS, no JavaScript framework.

**Working-paper titles (canonical):** WP1 = *The Bilateral Foundation* (retitled May 2026; was *A Canada–Korea Pacific Infrastructure Facility* — that phrase is now reserved for the CKPIF *instrument* in body prose, not the paper title). WP2 = *A Canada–United States Energy and Compute Compact*. WP3 = *A Canada–Korea Pacific Defence-Industrial Corridor*. WP4 = *The Addition Paradox*. WP5 = *Sovereign Compute North* (published 27 May 2026; `wp5/working-paper.pdf` is the canonical release, `wp5/index.html` carries the full reading view. Co-issued with Fit For Gov; companion to SB1). WP7 = *Dazzle 2.0* (first paper in the NPSI Counter-Autonomy series). WP9 = *The Counterparty Problem* (published 27 July 2026; reading view only, no PDF yet). WP10 = *Fair Use for We, IP Theft for Thee* (Technical Series; published 26 July 2026; `wp10/working-paper.pdf` is the canonical release; **superseded by WP11** — remains available unaltered with a correction notice attached, per WP11's own commitment; never quietly edit WP10). WP11 = *Rated AAA by the Issuer* (Technical Series; published 28 July 2026; full reading view + `wp11/working-paper.pdf`, 18 pp.; supersedes WP10 with four itemised corrections at its §1). Numbering is the author's: WP6 and WP8 remain unreleased, so the archive carries intentional gaps at 6 and 8.

**Current paper: WP11** (published to the site 29 July 2026; WP9 held the slot for a few hours the same day before WP11 arrived). The "Working Paper" nav link sitewide points to **`/wp11/`**; WP9 and WP7 carry the standard previous-paper banner; WP10 carries a supersession notice instead. The archive runs WP9 (27 Jul) → WP10 (26 Jul) → WP7 (12 Jul) with day-level dates. Papers are ordered by publication date and nothing else.

**PDF-first releases (WP5, SB2):** the PDF is the canonical release document; each page also carries a **full reading view** (ported July 2026 from the release PDFs) plus complete metadata (Highwire + JSON-LD with `encoding`) and the direct download. **Korean rollout kit:** the `npsi-korean-translation` skill is installed at `.claude/skills/npsi-korean-translation/` (register rules, glossary + WP3 supplement, QA checklist) — consult it before publishing any Korean text.

## What this site is *not*

These constraints are non-negotiable. They are the brand discipline. Drift on any of them costs the imprint its credibility:

- **Not an advocacy site.** No campaign-style copy. No CTAs that pressure. No "subscribe to learn more" language.
- **Not a personal platform.** The editor signs the work, the imprint hosts it. Don't write content as if Jesse is the brand.
- **Not a content stream.** Working papers publish when substantive material is ready. There is no cadence. The site does not need a blog, news section, or tag cloud.
- **Not a consulting page.** No services menu, no "work with us," no rates.
- **Not a tracking surface.** No cookies, no fingerprinting, no Google Analytics or any equivalent product that profiles visitors. The site uses **Umami** (cookieless, no personally-identifying data, GDPR-compliant by design); the analytics dashboard is itself shareable as a public URL, which fits the editorial-transparency posture rather than violating it. Adding any other third-party script — fonts excepted — requires the same discipline check.
- **Not a movement.** No flags, no national symbols, no slogans. Treaty-document register only.
- **Not a JavaScript framework SPA.** No React, no Vue, no Next.js, no build step. Plain HTML and CSS, hand-authored. Adding a framework would slow the site, add tracking surface, and break the institutional aesthetic.

If a proposed change would push the site toward any of the above, stop and flag it before implementing.

## Visual identity — the rules

### The dark identity (adopted July 2026)

In July 2026 the imprint adopted a **dark-first identity** at the editor's direction: the same four-colour brand, inverted. Document Cream became the ink; Pacific Navy became the paper. Nothing else changed — same wordmark geometry, same three typefaces, same bronze meridian, same chrome. Token *names* in `site.css` kept their light-era *roles* (`--navy` is still "primary ink", `--cream` is still "page background"); only the values flipped, so every page-scoped component inherits the theme untouched. **Print re-inverts to the light palette** inside `@media print` — the reference document still prints as paper. Figure SVGs, OG cards, and all raster icons were re-rendered in the dark identity.

### Color tokens (CSS variables in `assets/css/site.css`)

| Token | Hex (screen, dark) | Hex (print, light) | Role |
|---|---|---|---|
| `--navy` | `#F4EFE3` | `#0E2B47` | Primary ink; wordmark, headings, dominant typography |
| `--navy-deep` | `#FFFDF6` | `#081C30` | Hover states only |
| `--bronze` | `#C08D60` | `#A47148` | Accents — meridian rules, italic descriptors, KPI numbers, accent borders. Never used as large fill. Maximum ~5% of any composition. |
| `--teal` | `#7FA8B5` | `#3D6A78` | Section markers, classification lines, monospace metadata |
| `--cream` | `#081C30` | `#FFFFFF` | Page background |
| `--paper` | `#0F2A44` | `#FBF8EF` | Card and figure backgrounds, lifted one step from the page |
| `--ink` | `#D9D3C6` | `#1A1A1A` | Body text. NEVER pure white, NEVER pure black. |
| `--rule` | `#2E4A63` | `#C4B79B` | Dashed and thin rules between sections |

**Restrictions, hard:**
- Never introduce red. Both the Canadian and Korean flags use red; using it conflates the imprint with national branding.
- Never introduce a green, purple, or any non-palette accent. The four-color palette is total. (When porting drafts that arrive with rust/green/gold accents, map rust→bronze, green→teal, gold→bronze — precedent: WP7 figures.)
- Never use pure white (`#FFF`) or pure black (`#000`) for text or grounds on screen. The cream-family inks and navy-family grounds are the range.
- The masthead backdrop is `rgba(8, 28, 48, 0.92)` with blur — keep it in the navy family.

### Typography

Three typefaces, loaded from Google Fonts. Do not add a fourth without serious reason.

| Family | Use |
|---|---|
| **Source Serif 4** | Display, body, italic descriptors. The voice of the imprint. |
| **Source Sans 3** | Sans-serif body when needed (rare). UI labels. |
| **JetBrains Mono** | Classification lines, page metadata, document IDs, KPI numbers, code |
| **Noto Serif KR / Noto Sans KR** | Korean script when bilingual content appears |

**Hard rules:**
- Never use Inter, Roboto, Arial, Helvetica, system-default sans, or any "AI default" font. They read as not-quite-serious immediately.
- Never bold body text for emphasis. Italic in Source Serif 4 carries emphasis. Bold is reserved for proper nouns and section titles.
- Letter-spacing on small caps must be 0.14–0.22em depending on size. Generous tracking is part of the institutional register.

### Wordmark and small-format mark

- **Full wordmark** (in `assets/img/npsi-wordmark.svg`): used on document covers, cover banners, the site masthead in some contexts. Three-line stack: `NORTH PACIFIC STRATEGY INITIATIVE` in Pacific Navy small caps, italic descriptor in Treaty Bronze, mono volume marker in Maritime Teal. Three-tick meridian rule above.
- **Compact masthead** (in `assets/img/npsi-masthead.svg`): used at the top of every page header — wordmark only with thin bronze rule below. No descriptor.
- **Square mark** (in `assets/img/favicon.svg` and the LinkedIn assets): for square/circle constraints — favicon, LinkedIn profile mark, future Slack/social where required. "NP" monogram in Pacific Navy with meridian above and mono volume marker below.

**Wordmark rules, hard:**
- Never recolor outside the brand pair. On screen (dark identity): Document Cream on Pacific Navy. In print and light-era contexts: Pacific Navy on Document Cream. No third combination.
- Never combine with national flags or symbols.
- Never pair with an additional icon, symbol, mascot, or graphic mark.
- Maintain clear-space margin equal to the height of the wordmark on all four sides.

## Document chrome — the recurring pattern

Every page, every document, every figure carries the same chrome. If you're building a new page, copy the chrome verbatim from an existing page (`/wp1/index.html` is the canonical reference). The chrome is the brand; deviation reads as a different publication.

### Page header (every page)

```html
<header class="masthead">
  <div class="masthead-inner">
    <a href="/" class="masthead-mark">NORTH PACIFIC STRATEGY INITIATIVE</a>
    <nav class="nav" aria-label="Primary navigation">
      <a href="/wp4/">Working Paper</a>
      <a href="/about/">About</a>
      <a href="/engage/">Engage</a>
      <a href="/commentary/">Commentary</a>
    </nav>
    <div class="nav-volume">VOL. I  ·  EST. MMXXVI</div>
  </div>
</header>
```

The "Working Paper" nav link points to the **current** working paper (currently `/wp11/`); previous papers remain accessible by direct URL and via the home-page archive. The current page's nav link gets `class="active"` (adds the bronze underline). The masthead is sticky on scroll with a subtle blur backdrop on the cream.

### Page opener (every content page)

```html
<div class="opener">
  <div class="meridian"><span></span></div>
  <div class="doc-class">[Page-specific classification line, mono small caps, bronze]</div>
  <h1>[Page title]</h1>
  <div class="subtitle">[Italic subtitle in bronze]</div>
  <p class="lede">[First lede paragraph]</p>
  <p class="lede">[Second lede paragraph if needed]</p>
</div>
```

The meridian rule with three ticks (`<span>` is the middle tick) appears at the top of every opener. It's the visual signature.

### Page footer (every page)

```html
<footer class="site-footer">
  <div class="colophon">
    <div class="colophon-left">
      <div class="colophon-mark">NORTH PACIFIC STRATEGY INITIATIVE</div>
      <div class="colophon-tag">Working Papers on Pacific Sovereignty &amp; Bilateral Architecture</div>
      <div class="colophon-text">
        Editor: Jesse James  ·  <a href="mailto:editor@npsi.ca">editor@npsi.ca</a><br>
        Working paper text: <a href="https://creativecommons.org/licenses/by/4.0/">CC-BY-4.0</a>. The imprint and wordmark are not licensed.
      </div>
    </div>
    <div class="colophon-right">
      VOL. I<br>
      EST. MMXXVI<br>
      <a href="https://github.com/npsi-pacific">GITHUB</a>  ·  <a href="https://www.linkedin.com/company/north-pacific-strategy-initiative/">LINKEDIN</a>  ·  <a href="/colophon/">COLOPHON</a>
    </div>
  </div>
</footer>
```

## Editorial voice

The site copy and any working-paper prose hosted here follow the same disciplines:

- **Analytical and direct.** Sentences carry their weight. No adverbial inflation. No exclamation marks.
- **No first person in working-paper body text.** The editor signs in transmittals; in published prose, the analytical voice is third-person and disciplined.
- **Honest about uncertainty.** Indicative numbers are flagged as such ("indicative," "approximately," "subject to"). Avoid the false-precision register of consultancy decks.
- **No anti-American framing.** NPSI takes no position critical of the United States. The thesis is *counterparty-risk diversification* and *additive financial architecture*, not antagonism. Drift here breaks the entire placement strategy.
- **The Korea convention.** In body text, "Korea" refers to the geographic and civilizational entity in academic convention. In matters of protocol — transmittal letters, formal correspondence, official invitations — the formal "Republic of Korea" is used. Preserve this distinction in any new content.
- **Sources for every factual claim.** Citations follow standard policy-paper convention. Web sources include URL.

## File structure (top-level)

```
npsi-site/
├── CLAUDE.md                        ← this file
├── README.md                        institutional landing for the GitHub repo
├── DEPLOYMENT.md                    deployment instructions for Cloudflare Pages / Netlify / Vercel
├── index.html                       home — current working paper, archive, the imprint
├── 404.html                         not-found page
├── about/index.html                 about NPSI
├── engage/index.html                contribution standards
├── commentary/index.html            named commentary index, per paper
├── colophon/index.html              technical colophon
├── wp1/
│   ├── index.html                   Working Paper No. 1 — *The Bilateral Foundation* — full reading view (previous paper; banner points to WP7)
│   └── working-paper.pdf            full PDF release (present; direct download, no email gate)
├── wp2/
│   └── index.html                   Working Paper No. 2 — full reading view (previous paper)
├── wp3/
│   └── index.html                   Working Paper No. 3 — full reading view (previous paper)
├── wp4/
│   ├── index.html                   Working Paper No. 4 — *The Addition Paradox* — full reading view (previous paper; banner points to WP7)
│   └── working-paper.pdf            full PDF release (present; direct download, no email gate)
├── wp5/
│   ├── index.html                   Working Paper No. 5 — *Sovereign Compute North* — full reading view (PDF canonical)
│   └── working-paper.pdf            canonical v1.0 release (19 pp., direct download)
├── wp7/
│   ├── index.html                   Working Paper No. 7 — *Dazzle 2.0* — full reading view (previous paper; banner points to WP9)
│   └── working-paper.pdf            v1.0 PDF (generated from the reading view; direct download)
├── wp9/
│   └── index.html                   Working Paper No. 9 — *The Counterparty Problem* — full reading view (previous paper; banner points to WP11; no PDF yet)
├── wp10/
│   ├── index.html                   Working Paper No. 10 — *Fair Use for We, IP Theft for Thee* — release page (PDF canonical; superseded by WP11, notice attached)
│   └── working-paper.pdf            canonical v1.0 release (17 pp., direct download, unaltered)
├── wp11/
│   ├── index.html                   Working Paper No. 11 — *Rated AAA by the Issuer* — full reading view (CURRENT paper)
│   └── working-paper.pdf            canonical v1.0 release (18 pp., direct download)
├── sb2/
│   ├── index.html                   Special Briefing No. 2 — *The Three Doors* — full reading view (PDF canonical)
│   └── special-briefing.pdf         canonical v1.0 release (10 panels, direct download)
├── tb1/
│   ├── index.html                   Technical Briefing No. 1 — *The Verified Sky* — full reading view
│   └── technical-briefing.pdf       full PDF release (direct download, no email gate)
├── bn1/
│   ├── index.html                   Briefing Note No. 1 — *The Voter File* — full reading view
│   └── briefing-note.pdf            full PDF release (direct download, no email gate)
├── sb1/
│   ├── index.html                   Special Briefing No. 1 — *Zero Secrets* — full reading view
│   └── special-briefing.pdf         full PDF release (direct download, no email gate)
├── llms.txt                         LLM-crawler index (llms.txt convention): imprint summary + canonical URL and one-line abstract per paper
└── assets/
    ├── css/site.css                 shared stylesheet, fully tokenized
    └── img/
        ├── npsi-wordmark.svg        full wordmark
        ├── npsi-masthead.svg        compact masthead
        ├── favicon.svg              square mark
        ├── ckpif-architecture.svg   Figure A from WP1
        ├── wp2-og.svg/.png          WP2 Open Graph share card (1200×630)
        ├── wp2-architecture.svg     WP2 Figure A — three-rail Pacific architecture
        ├── wp2-bifurcation.svg      WP2 Figure B — training and inference bifurcation
        ├── wp2-capacity-gap.svg     WP2 Figure C — U.S. capacity gap by 2028
        ├── wp2-compact.svg          WP2 Figure D — six-layer compact architecture
        ├── wp2-indigenous.svg       WP2 Figure E — Series II tranche structure
        ├── tb1-og.svg/.png          TB1 Open Graph share card (1200×630)
        ├── bn1-og.svg/.png          BN1 Open Graph share card (1200×630)
        ├── sb1-og.svg/.png          SB1 Open Graph share card (1200×630)
        └── og-default.png/.svg      site-wide Open Graph share preview (1200×630)
```

## Conventions for changes

### When adding a new page

1. **Copy `about/index.html` as the template.** It has the cleanest structure of the existing pages.
2. Update the `<title>`, meta description, OG tags.
3. Set the active nav link with `class="active"`.
4. Use the existing CSS — do not add new tokens or new components without flagging.
5. Maintain the page footer verbatim.
6. Verify mobile rendering at 390px viewport (iPhone-class).

### When adding a new working paper

1. Create `wp[N]/index.html`, modeled on `wp1/index.html` (the canonical chrome reference).
2. **Update the home page's "Current Working Paper" card** with the new paper. Move the previously-current paper's card into the "Previous Working Papers" section on the home page (if it doesn't exist yet, create it directly below the Current card).
3. **Update the nav `Working Paper` link sitewide** to point to the new paper (`/wp[N]/`). The four-link nav is intentional restraint — *never add a fifth link.* Previous papers remain accessible via direct URL and the home-page archive.
4. **Add a "previous paper" banner near the top of the prior paper's page**, pointing readers to the current paper. The banner uses the `<aside class="standard">` pattern with an `<h4>` and a one-sentence pointer.
5. Add a new section to `commentary/index.html` for the new paper's commentary collection (above the previous paper's section). Open for submission.
6. Drop release files into `wp[N]/` (`working-paper.pdf`, `executive-brief.pdf`, figure files).
7. **OG card pipeline.** Hand-code `assets/img/wp[N]-og.svg` (1200×630, NPSI register, three stat blocks, no red, no flags) using `wp1-og.svg` / `wp4-og.svg` as the template. Render to PNG with `npx --yes resvg-cli assets/img/wp[N]-og.svg assets/img/wp[N]-og.png`. The PNG is what `og:image` must reference — social platforms (Twitter, Facebook, LinkedIn) require raster. The SVG is the source of truth; commit both. Build hand-coded SVG figures into `assets/img/` and reference via `<figure><img></figure>` in the paper.
8. **JSON-LD ScholarlyArticle.** Add a `<script type="application/ld+json">` block to the paper's `<head>`, mirroring the WP1–WP4 pattern (`@type: ScholarlyArticle`, `headline`, `datePublished`, `identifier: NPSI-WP-NNN`, `issueNumber`, `image` pointing to wp[N]-og.png, `license`, `keywords`, `abstract`, `author`, `publisher`, `isPartOf: NPSI Working Papers`, and `encoding` carrying the PDF when released). This is what Google's Knowledge Graph, Bing, and academic crawlers index beyond the Highwire `citation_*` tags.
9. Update the GitHub repository at `github.com/npsi-pacific/working-paper-[N]` (when the imprint org is provisioned; until then, the working repo is `cherishwins/npsi-site`).
10. Working paper IDs follow the format `NPSI-WP-NNN` (zero-padded to three digits).
11. Versions follow `vM.m[.p]` — major versions for substantive revisions, minor for named-commentary integration, patch for errata. Pre-publication drafts use `v0.x` until v1.0 is released.
12. **Add `wp[N]/` and `wp[N]/working-paper.pdf` (if released) to `sitemap.xml`** with the release date as `lastmod`. Bump the previous paper's `<priority>` down a notch and the new paper's up to `0.9`. The home-page `<lastmod>` should be updated to the release date as well.

### Page chrome — three pieces every page carries

The skip-link, the masthead, and the footer are the page-chrome trio. New pages must include all three verbatim:

```html
<body>

<a href="#main" class="skip-link">Skip to content</a>

<header class="masthead">...</header>

<main id="main" tabindex="-1">
  ...
</main>

<footer class="site-footer">...</footer>
```

The skip-link is keyboard-only (hidden until focused); `<main id="main" tabindex="-1">` is the focus target. Both come from `.skip-link` rules in `site.css` and must not be styled per-page.

### Site infrastructure (well-known files)

- **`vercel.json`** — HTTP headers (CSP, HSTS, X-Frame-Options, Permissions-Policy, Referrer-Policy, X-Content-Type-Options, long-cache on immutable assets). Updating CSP requires also updating the `script-src` allowlist if a new third-party script is added. The Umami analytics domain (`cloud.umami.is`) is allowlisted; nothing else may run a script.
- **`sitemap.xml`** + **`robots.txt`** — discoverability plumbing for crawlers, Internet Archive, Google Scholar.
- **`humans.txt`** at site root — editorial/technical credits.
- **`llms.txt`** at site root — LLM-crawler index per the llms.txt convention: imprint summary, canonical URL and one-line abstract per paper. Update it whenever a paper or briefing is added or retitled.
- **`.well-known/security.txt`** — RFC 9116 contact for security researchers. Bump the `Expires:` field annually.
- **`CITATION.cff`** at repo root — renders GitHub's "Cite this repository" widget for academic reuse.

### When fixing or improving CSS

- Never introduce a new color outside the four-color palette.
- Never introduce a new typeface.
- Never add JavaScript dependencies, build tooling, or framework imports.
- Test changes in both desktop (1280px) and mobile (390px) viewports before considering done.
- **Use the fluid scale, not hard pixels.** Type and space are a continuous `clamp()` system in `site.css` (`--fs-*`, `--space-*`, fluid `--pad-x`); each clamp's max is the desktop identity and its min is the small-screen identity, so the look is pixel-identical at 1280px and 390px and interpolates between. Add new sizes as `clamp()` tokens in `:root`; do not hard-code a px size and do not add per-breakpoint font-size overrides — the `@media (max-width: 820px)` block is layout-only by design. Measure (line length) is set in `ch` via `--max-w`; keep it in the 66–75ch readability band. Print is A4 (`@page { size: A4 }`) — preserve the keep-together rules on `.pull/.wp-card/figure/.wp-meta-block`.

### When updating copy

- Read the relevant section of the brand specification (`/mnt/user-data/outputs/npsi-kit/10-NPSI-brand-specification.md` if available, or refer to the editorial-voice section above) before drafting.
- Match the existing register. The imprint speaks one way; new copy must speak that same way.
- For Korean-language content: bilingual audit table required (Korean left, English literal translation right). No Western framing in Korean text.

## Deployment

The site deploys to **Cloudflare Pages** (recommended) as plain static files. No build step. The `DEPLOYMENT.md` file covers DNS, email aliases, and pre-launch checks.

To preview locally:
```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Working-paper substance — canonical references

### Working Paper No. 1 — A Canada–Korea Pacific Infrastructure Facility (`wp1/index.html`)

Proposes the CKPIF — a treaty-based supranational issuer for Pacific corridor infrastructure. Key facts that should remain consistent across any future edits:

- 50/50 Canada–Korea ownership, Luxembourg seat, English law, LCIA arbitration
- Indicative programme size US$25–40 billion over 5–7 years
- Indicative pricing +50–80 bp over 30Y UST at launch
- Several (not joint) sovereign guarantees
- Indigenous Series I tranche, 10–15% of programme, +25 bp ratchet protection
- KPI architecture follows ICMA Sustainability-Linked Bond Principles, 25 bp step calibration
- Tokenised pilot tranche US$200–500 m on Project Agorá-class infrastructure (BoK is a participant)
- BoC–BoK standing swap line, signed November 2017, no expiry, no preset limit — the institutional foundation
- Author: Jesse James (editor); v1.0 published April 2026

### Working Paper No. 2 — A Canada–United States Energy and Compute Compact (`wp2/index.html`)

Proposes the **Compact** — a treaty-grade bilateral architecture pairing Canadian dispatchable generation with the U.S. grid through ultra-high-voltage transmission, siting AI training on Canadian hydro and preserving inference at the U.S. urban edge. Companion to WP1; financed through the same CKPIF supranational vehicle (Phase 2). Key facts:

- Canada–U.S. bilateral, several (not joint) liability, English law, LCIA arbitration; survives CUSMA non-renewal
- U.S. structural capacity gap: ~44 GW required by 2028 vs ~25 GW deliverable = 19 GW shortfall
- Combined dispatchable Canadian hydro: Hydro-Québec 37,370 MW + BC Hydro 13,200 MW + Manitoba Hydro 5,500 MW = ~56,000 MW
- AI training/inference bifurcation: training latency-agnostic (~25% CAGR); inference sub-50 ms latency (~79% CAGR); 80% of total AI critical-IT load is inference by 2030
- Three corridor candidates: Saguenay/Côte-Nord (QC), Peace River/Bennett (BC), Northern Manitoba
- CUSMA July 2026 review is the timing peg; v1.0 target pre-1-July-2026
- Indigenous Series II tranche (parallel to WP1 Series I), 10–15% of compact capex, +25 bp ratchet
- Three-rail Pacific architecture: financial rail (Korea, WP1) + energy/compute rail (U.S., WP2) + critical-minerals rail (cross-cutting)
- Author: Jesse James (editor); v1.0 published May 2026

If new content cites different numbers, structure, or framing for either CKPIF or the Compact without explicit reason, that's a drift to flag.

- **Working Paper No. 3 — A Canada–Korea Pacific Defence-Industrial Corridor** (`wp3/index.html`, in pre-publication draft as of May 2026) — submarine procurement, industrial offsets, and the third rail of middle-power sovereignty; pairs with WP1 (financial) and WP2 (energy/compute) to complete the three-rail Pacific architecture; v1.0 target pre-23 May 2026.

  Key facts that should remain consistent (revised 6 May 2026 against primary-source memo in `.editor/research/wp-source-memo-2026-05-06.md`):
  - **CPSP programme size:** envelope not officially published by Government of Canada. Trade-press estimates range CAD 12B–43B (Sault Ste. Marie News Jan 2026; CBC; 19FortyFive Dec 2025; Seoul Economic Daily Mar 2026). Correct framing: *"envelope to be set by the Defence Investment Agency under Canada's Defence Industrial Strategy (17 February 2026)."* **Do not adopt any single figure (CAD 40B, CAD 100B, CAD 60B) as authoritative.** Up to 12 submarines by 2035.
  - **KSS-III** (Hanwha Ocean Dosan Ahn Chang-ho class), 3,000 t surface / ~3,750 t submerged, diesel-electric AIP, lithium-ion batteries, vertical launch system. **The KSS-III itself has not yet been exported.** Korean export track record to date: Indonesian Type 209 derivatives 2011–2024 (2019 follow-on cancelled by Indonesia in favour of Naval Group's Scorpène). Canadian award would be the first KSS-III export.
  - **Hanwha bid offsets:** Hanwha-Algoma binding MOU signed 26 January 2026 (USD 250M / CAD 345M aggregate; USD 200M Sault Ste. Marie beam mill + USD 50M CPSP-related steel; binding but conditional on CPSP award; 3.0% Algoma-to-Hanwha-Ocean royalty on beam-mill net sales for 10 years post-commissioning). Hanwha–APMA MOU signed 29 April 2026 in Vaughan, Ontario, at a Martinrea facility (conditional Canadian-majority JV; K9 Thunder, K10, Redback IFV, Chunmoo MLRS, AGVs). **Distinguish binding (Algoma) from conditional (APMA) MOUs.**
  - **ROK Navy port visit and joint exercise window** (NB: official RCN/DAPA framing is "port visit and combined exercises," not "demonstration" — "demonstration" is NPSI editorial framing): ROKS Dosan Ahn Chang-ho departed Jinhae 25 March 2026; arrives CFB Esquimalt 23 May 2026; combined ASW/MPA exercises with RCN and RCAF in MARPAC area through 2 June; accompanied by ROKS Daejeon (frigate); two RCN submariners embarked at Hawaii via REGULUS programme; en route to RIMPAC 2026.
  - **HBM market share:** Q3 2025 Counterpoint estimates SK Hynix ~53%, Samsung ~35%, Micron ~11%. **Treat as quarterly research-vendor estimates, not government data.** Defensible formulation: "SK Hynix and Samsung jointly produce more than 75% of global HBM, with SK Hynix in the lead position as of Q3 2025." Pair with Korea Zinc–Lockheed Martin germanium MOU (Aug 2025, USD ~140B KRW Onsan plant) and JEDEC HBM4 specification (April 2025) for technical anchoring.
  - **CKFTA** in force 1 January 2015 (Bill C-41 Royal Assent 26 November 2014); full implementation 1 January 2032 (99.75% bilateral tariffs eliminated).
  - **30 October 2025 Carney–Lee Joint Statement** establishing the Security and Defence Cooperation Partnership (SDCP) — first of its kind for Canada in the Indo-Pacific.
  - **25 February 2026 second 2+2 Ministerial:** Classified Information Protection Agreement signed (not yet in force; track entry-into-force notice); Defence Cooperation Agreement negotiations launched; SDCP Action Plan in development; first Canada-Korea Cyber Policy Consultations March 2026; Canada-Korea Space Security Dialogue committed; next 2+2 in ROK 2028.
  - **19 August 2025 PSPC release** confirmed Hanwha Ocean and TKMS as the two qualified suppliers; 25 RFI responses received Sep 2024–Feb 2025; first delivery NLT 2035.
  - **Anchor research document:** Julie Kim, *The Future of Canada-ROK Defence Cooperation*, CGAI Policy Perspective, April 2025 (ISBN 978-1-77397-337-1) — substantially out of date for late-2025 / Q1-2026 events; treat as contemporaneous baseline.
  - January 2026 Canada–Korea Industrial Cooperation Committee MOU on co-mining and co-production.
  - FORGE plurilateral framework — Korea-chaired through mid-2026.
  - Author: Jesse James (editor); v1.0 published May 2026.

### Working Paper No. 4 — The Addition Paradox (`wp4/index.html`)

An energy thesis for Canada — v1.0 published 15 May 2026. Four parts plus executive summary: The Diagnosis, The Chokepoint Migration, The Canadian Thesis, The Verdict. Key facts that should remain consistent across any future edits:

- **Core thesis:** the global energy transition did not substitute, it *added*. 2024 saw a record 858 TWh of new clean electricity *and* record fossil combustion; global electricity demand grew 1,172 TWh (clean supplied 858, fossil supplied the remaining 314); power-sector CO₂ ≈ 14.6 Gt; coal ≈ 10,613 TWh and forecast largest single source through the mid-2030s; clean-energy investment ≈ US$2 trillion in 2024 (≈2× fossil); upstream oil investment ≈ US$570 bn (highest since 2017).
- **Chokepoint migration:** clean-tech refining/assembly concentration in a single nation — polysilicon ≈ 95%, lithium cells ≈ 80%, NdFeB magnets ≈ 90%. Framed as concentration risk, **not** anti-clean-energy and **not** named beyond "a single nation / the People's Republic of China" as the paper does.
- **Four Canadian assets (one hand):** 3rd-largest oil reserves with lowest-carbon barrel (oil-sands intensity −33% since 2009); largest per-capita clean electricity in the industrial democracies (hydro > 380 TWh/yr); 2nd-largest high-grade uranium reserves (Athabasca Basin, 10–100× global mean grade); only G7 nation with simultaneous Pacific and Atlantic deepwater export capacity (Kitimat, Prince Rupert, Vancouver within ~5 sailing days of Yokohama/Busan/Shanghai).
- Positioned as the strategic preface to the three-rail architecture: WP1 (financial), WP2 (energy/compute), WP3 (defence-industrial).
- Editorial-voice note: the paper uses sustained funeral/inheritance metaphor ("the casket will remain closed"). Preserve it; it is intentional register, not drift. **No red** in the site rendering even though the source PDF cover uses a maroon accent — the HTML reading view uses the four-colour palette only.
- Author: Jesse James; v1.0 published 15 May 2026.
- PDF: `wp4/working-paper.pdf` — direct download, no email gate (matches WP1).

### Working Paper No. 7 — Dazzle 2.0 (`wp7/index.html`)

v1.0 published 12 July 2026 — the first paper in the **NPSI Counter-Autonomy series** (the contest between machine autonomy and its countermeasures). Numbered WP7 by the author; WP5 (*Sovereign Compute North*) published 27 May 2026, so only WP6 remains forthcoming — an intentional single-number gap. Eight sections plus executive summary. Key facts that should remain consistent:

- **Core assessment:** the viral claim about Russia's "zebra"-painted logistics trucks is *real at its root and inflated at its tip*. Trucks confirmed via imagery since ~31 May 2026 (TWZ, RFE/RL, France 24, Defense Express, Militarnyi); anti-machine-vision intent is analyst consensus; **zero published controlled tests** show an effect on a named detector.
- **Evidence-tier discipline is the paper's spine:** every load-bearing claim is tagged Confirmed / Plausible / Speculation / Hype in the §2 table. Preserve the tags; they are the register.
- **Mechanism:** most plausibly out-of-distribution confusion (Humphreys), not an engineered adversarial attack. Proven ceiling: Eykholt et al. CVPR 2018 (84.8% field misclassification); Brown et al. 2017 adversarial patches; Thys/Van Ranst/Goedemé 2019; CAMOU/DAS/FCA vehicle textures. Three gaps separate crude stripes from that ceiling: optimization, physical robustness, transferability.
- **The durable finding is cost asymmetry**, anchored to Schuyler Moore (then CENTCOM CTO, CSIS, September 2024): the aircraft-tire tactic worked and the retraining loop was up to six months. Paint iterates in hours.
- **Procurement recommendations (five):** multi-sensor seekers (EO + thermal/IR); human-on-the-loop authorization; edge-retrainable models with organic labeling; adversarial/OOD inputs in acceptance testing; no single-vendor black-box ATR. Canadian pegs: Switchblade 300/600 to Latvia brigade, Minerva Initiative, CALM/CADUC.
- **Historical frame:** 1917 Wilkinson dazzle attacked *geometric estimation* by a human; 2026 zebra attacks *object classification* by a machine. Analogy, never equivalence (Lovell/Sharman/Meese 2024: ~10° perceptual twist only).
- Register: hostile-read discipline — the paper concedes weak links before an opponent can (§7 Guardrails). Analysis, not intelligence; no classification.
- Figures A–D are inline SVGs in the dark palette (out-of-palette draft colours were mapped rust→bronze, green→teal, gold→bronze).
- Author: Jesse James; v1.0 published 12 July 2026. PDF released 23 July 2026 at `wp7/working-paper.pdf` — generated from the reading view via Chromium print-to-PDF (A4, print palette re-inversion, running header/footer, 10 pp.); regenerate the same way after any substantive edit to the reading view.

### Technical Briefing No. 1 — The Verified Sky (`tb1/index.html`)

The first of the **Technical Briefings** — a companion line to the Working Papers addressing the engineering substrate beneath the policy architecture. Document IDs follow `NPSI-TB-NNN`. The reading view uses the standard site chrome (masthead, skip-link, footer verbatim) plus page-scoped, `tb-`-prefixed components in an inline `<style>` block (verification ledger, data tables, KPI row, footnotes, series index, endmark) — all on the four-colour palette and the three site typefaces. Technical briefings do **not** join the four-link nav; they are reached from the home page's "Technical Briefings" section and direct URL. Key facts that should remain consistent:

- Subject: sensing, certainty, and the law of automated airspace awareness — computer-vision and sensor-fusion state of the art 2025–2026 for monitoring a defined airspace volume.
- Signature element: the **verification ledger** — seven conditions (class, size, altitude, kinematics, window, geofence, persistence) that must all pass before any action fires; two-sensor corroboration as the industry standing rule.
- Benchmark honesty: Anti-UAV410 state accuracy plateaued in the low-to-mid 60s since 2023; CST Anti-UAV (realistic tiny targets) best method 35.92% — realistic small-and-distant performance is roughly half of headline performance.
- Legal line (Canada): detection, tracking, evidence, and notification are lawful for civil operators; jamming/spoofing (Radiocommunication Act ss. 4(4), 9(1)(b)), takeover (Criminal Code ss. 342.1–342.2), and physical downing (Aeronautics Act, CARs Part IX) are not. Transport Canada NPA 2026-005 (8 June 2026) proposes mandatory Remote ID on ASTM F3411; comment window to 9 September 2026.
- Register: technical and regulatory survey, explicitly not legal advice (standing caveat block); no first person; conservative forecast framing ("treat a breakout as upside, never as the plan").
- Author: Jesse James; v1.0 published 11 June 2026. PDF: `tb1/technical-briefing.pdf` (direct download, no email gate). OG card `assets/img/tb1-og.svg/.png` follows the WP pipeline.

### Briefing Note No. 1 — The Voter File (`bn1/index.html`)

The first of the **Briefing Notes** — the imprint's short-form line: a single mechanism, documented end to end, in under twenty minutes of reading. Document IDs follow `NPSI-BN-NNN`. Standard site chrome plus page-scoped, `bn-`-prefixed components (the **file card** — an illustrative five-layer voter record — data tables, footnotes, series index, endmark). Briefing notes do not join the four-link nav; reached from the home page's "Briefing Notes" section and direct URL. Key facts that should remain consistent:

- Subject: the five-layer Canadian federal voter file (statutory spine from the Elections Canada list of electors; canvassing layer; public-records layer; commercial layer; modelled scores) and the privacy asymmetry that governs it.
- Legal chronology: PIPEDA never applied (commercial-activity scope); Bill C-76 (2018) required only a published privacy policy; BC OIPC Order P22-02 (2022) and the 2024 BC Supreme Court judicial review found BC PIPA could apply; **Bill C-4 Part 4 (royal assent March 2026)** replaced the CEA regime and excluded federal parties from provincial/territorial privacy law retroactive to 2000. Senate's three-year sunset amendment rejected; Green Party the sole party opposed.
- Register: structural survey, explicitly non-partisan (standing caveat block); the illustrative record is fictional and labelled as such.
- Author: Jesse James; v1.0 published 11 June 2026. PDF: `bn1/briefing-note.pdf`. OG card `assets/img/bn1-og.svg/.png`.

### Special Briefing No. 1 — Zero Secrets (`sb1/index.html`)

The first of the **Special Briefings** — single-issue strategic assessments published when an exposure demands attention outside the working-paper cycle. Document IDs follow `NPSI-SB-NNN`. Standard site chrome plus page-scoped, `sb-`-prefixed components (the **hollow redaction bar** "NOTHING LEFT TO REDACT" — the signature device, rendered in bronze — executive-summary block, findings list, stat grid, staged recommendations with benchmark lines, caveats, sources). **The source draft arrived in a midnight/gold theme set in Inter; it was ported to the four-colour palette and site typefaces per the brand rules. (The site later adopted its own dark identity in July 2026 — in the NPSI palette, not the draft's. The ban on Inter and on out-of-palette gold accents stands.)** Key facts that should remain consistent:

- Core claim: data residency is not data sovereignty — under the CLOUD Act (18 U.S.C. §2713) and FISA 702, US jurisdiction follows corporate ownership, not server location; no Canada–US CLOUD Act bilateral exists.
- Anchor evidence: Microsoft France testimony before the French Senate, 10 June 2025 ("No, I cannot guarantee that"); SSC evaluation (federal Azure use ≈4× AWS); Maven Smart System / Operation Epic Fury (13,000 targets in 38 days) as capability-class indicator; Operation Dunhammer; Duke data-broker study ($0.12/record); Starlink-Crimea; AI Diffusion Rule rescission.
- Federal response audited: $2B Sovereign AI Compute Strategy; "AI for All" (June 4, 2026, ~$2.3B); Cohere flagship operated by CoreWeave (the counter-template); Microsoft C$19B commitment vs. its own sworn testimony.
- Recommendations: control-based definition of sovereign cloud (jurisdictional, operational, cryptographic, audit); classified/Protected B migration; ICA strengthening; Canadian-owned-and-operated SCIP awards; champion retention via the $500M Canadian Tech Growth Fund.
- Register: caveats section states the strongest counter-cases fairly (cost, Five Eyes, free-riding) and publishes methodological uncertainty. Companion to WP5 *Sovereign Compute North* (published 27 May 2026, `wp5/`).
- Author: Jesse James; v1.0 published 11 June 2026. PDF: `sb1/special-briefing.pdf` (direct download, no email gate). OG card `assets/img/sb1-og.svg/.png`.

### Working Paper No. 9 — The Counterparty Problem (`wp9/index.html`)

U.S. commitment reliability assessed as two separate questions. v1.0 published 27 July 2026; reading view only (no PDF release yet). Key facts that should remain consistent:

- **Core finding:** "U.S. reliability" is two questions, not one. Definition A (formal withdrawal/repudiation of binding or quasi-binding commitments): ~15 significant instances since 2001, clustered 2017–2020 and 2025–2026. Definition B (stated intent/MoU that never converted): **no honest base rate exists** — no registry of U.S. MoUs; the paper deliberately declines to state a rate. Never let an edit introduce a fabricated conversion percentage.
- **The anchor case:** PIF–EXIM MoU, 24 July 2026 — framework of up to $15 billion; explicitly non-binding. EXIM's charter expires **31 December 2026**; S. 3772 (Warner–Cramer, 10-year extension, retains $135B cap per CRS) in committee with no markup; House discussion draft proposes 5 years. The $205 billion cap figure is a sponsor's goal, not enacted text.
- **The quantified precedent:** EXIM board-quorum lapse 20 July 2015 – 9 May 2019; financing declined ~85% 2014–2019 (NBER w32019); $1 of EXIM financing ≈ $4.50 of exports; stranded counterparties named (Pemex, Boeing/Ethiopian, GE plant to Canada, $3.5bn Egyptian petrochemical).
- **Balance is load-bearing:** the fair-reading section concedes democratic policy alternation, the honoured-commitment record (NATO Article 5, Bretton Woods, Japan/Korea treaties), and that other states have worse records. The framing is counterparty-risk pricing, not anti-American critique — this paper sits closest to that line; preserve the concessions verbatim in any edit.
- Contested figures are reported, not resolved (China export-credit volumes; Senate hearing date discrepancy).
- Author: Jesse James; v1.0 published 27 July 2026. Companions: WP1 (counterparty-diversification thesis), SB2 (EXIM SCRI door).

### Working Paper No. 10 — Fair Use for We, IP Theft for Thee (`wp10/index.html`)

First working paper published under the **Technical Series** banner. v1.0 published 26 July 2026; **PDF-first release** — `wp10/working-paper.pdf` (17 pp.) is canonical; the site page carries abstract, key findings, method and download; full reading view to follow. Key facts that should remain consistent:

- **Core finding:** "open source" has no enforced meaning in AI. OSAID v1.0 (October 2024) adopted as a binding criterion by no regulator or procurement authority located in the survey; of eleven model families surveyed, three meet the definition (OLMo 2, Pythia/GPT-NeoX, arguably BLOOM) — none at frontier scale.
- **Licence-text discipline:** the tier table resolves licences **per model version, not per vendor** (Mistral and Qwen mix licences in their own lineups). Llama 4's licence withholds rights from EU-domiciled persons/companies — inside a product marketed as open source, in the jurisdiction offering the open-source exemption (EU AI Act Art. 53(2); exemption partial, evaporates above 10^25 FLOPs).
- **The three-category separation** (the paper's spine): (1) taking model weights = theft, uncontested; (2) training on scraped outputs = contested, litigated; (3) acquiring pirated corpora = adjudicated against the lab. The $1.5bn Bartz v. Anthropic settlement (final approval 20 July 2026) is category 3; Judge Alsup's June 2025 ruling that training on lawfully acquired books is fair use still stands. Thomson Reuters v. Ross (Bibas J, 11 Feb 2025) is the strongest doctrinal thread: fair use collapses on market substitution.
- **Evidence-grade system:** VERIFIED / CORROBORATED / ATTRIBUTED / UNDETERMINED. The Sacks public-vs-private allegation is graded ATTRIBUTED and excluded from findings. All podcast revenue figures excluded. Preserve the grades in any edit; they are the register.
- **Author's disclosure** (in the PDF and noted on the page): drafted with assistance from Claude, made by Anthropic, whose conduct §6 examines. Do not remove.
- Not anti-American and not anti-Anthropic: the finding is an asymmetry of characterisation, and §9 states every counter-position "unweakened."
- Author: Jesse James; v1.0 published 26 July 2026.

### Working Paper No. 11 — Rated AAA by the Issuer (`wp11/index.html`)

Second paper in the **Technical Series**. v1.0 published 28 July 2026; full reading view plus `wp11/working-paper.pdf` (18 pp.). **Supersedes WP10** — the supersession is apparatus, not erasure: WP10 stays live and unaltered with a notice. Key facts that should remain consistent:

- **Correction discipline is the paper's identity:** four itemised corrections to WP10 at §1 (53 not 54 objections in Bartz; the "3.75 multiplier" withdrawn as unsourced; the Llama 4 EU exclusion sits in the Acceptable Use Policy, scoped to multimodal models, with an end-user carve-out; and the framing correction). The WP10 finding that survives verbatim: Anthropic's 23 Feb 2026 distillation post contains no instance of "IP theft," "intellectual property," "theft," or "copyright."
- **The framing correction (most consequential):** WP10 cast Anthropic as driving a restriction push; Amodei's 27 July 2026 position paper states "Anthropic has never advocated for a ban on open-weights models." The honest characterisation the paper lands on: Anthropic is the most restriction-friendly major lab on open weights *and* it has not called for a ban — both halves true, WP10 published only the first.
- **Core finding:** both camps (the 24 July Nvidia-hosted ~75-signatory letter and Anthropic) reject a categorical ban in writing; the real leverage is in who defines "sufficiently capable" — a capability threshold that falls disproportionately on open releases because guardrails cannot be reimposed after weights ship.
- **The analogy:** issuer-pays credit ratings (NRSRO regime from 2006, resolved by Dodd-Frank Title IX after systemic failure). Four-market base-rate table: organic (statute, ~12 yrs), Energy Star (certifier hardening after GAO-10-470's gas-powered alarm clock), credit ratings (statute after crisis), "natural" (never resolved; decayed into litigation-magnet marketing).
- **Forecast with probabilities and named falsifiers** (§5): label decays 45% · certifier gets teeth 20% · capability capture 25% · certifier captured 10%. Each branch names the observable event that moves it; preserve the falsifiers in any edit — a forecast nothing can falsify is not a forecast.
- **Author's disclosure** (§2 inset): drafted with assistance from Claude (Anthropic), whose statements the paper examines; the §1 framing correction ran *against* Anthropic. Do not remove.
- §7 names the jurisdictional cascade as the intended subject of **WP12** (not yet written).
- Author: Jesse James; v1.0 published 28 July 2026.

## Series pieces in flight (not yet on the site)

- **SB3 — reserved** for *The Ledger With One Entry* (Venezuelan oil revenue under U.S. custody; 39-pp. paper exists off-site, LinkedIn carousel released July 2026 with placeholder ID "NPSI-SB-NNN"). Integrate when the editor supplies the source document; assign `NPSI-SB-003`.
- **An unnamed Nord Stream accountability piece** — five finished dark-identity figures exist (three courts: Warsaw/Karlsruhe/London; €16.9bn asset cost; MV AfD polling); no document or number yet.
- **NPSI-X dossier line** — *Follow the Money* (EU revenue, `NPSI-X-2607`, 23 July 2026) uses a separate "open-source investigative dossier" ID scheme (`NPSI-X-NNNN`) and is not part of the working-paper series; no site presence yet and none implied.

## Other NPSI projects in scope

- **Briefing Note No. 1** (`NPSI-BN-001`, Canadian voter files and the privacy asymmetry) — **integrated June 2026** as `bn1/index.html` with `bn1/briefing-note.pdf`; see "Briefing Note No. 1 — The Voter File" above for the canonical-fact list.
- **Briefing Note No. 2 — Confederation Mathematics** (`NPSI-BN-002`, forthcoming) — empirical constraints on provincial secession in 2026 (Quebec + Alberta), forensic two-part briefing-note format. Source material drafted, not yet integrated. If asked to integrate, create `bn2/index.html` modeled on `wp1/index.html` with briefing-note format. Cited in WP2 §10 as forthcoming.
- **Working Paper No. 3 — Pacific Defence-Industrial Corridor** (`NPSI-WP-003`, v1.0 published May 2026) — see "Working-paper substance" above for canonical-fact list. Released ahead of the 23 May 2026 ROK Navy operational demonstration at CFB Esquimalt and the June 2026 CPSP final-contractor decision.
- **LinkedIn Company Page** assets exist in a sibling directory (`npsi-linkedin/`). Not part of this repo.

## What to ask before doing

When the request is ambiguous, ask Jesse rather than guess. Specifically:

- New domain name → confirm before find-and-replace (the kit was built for `npsi.ca`).
- New visual element → confirm it fits the brand spec.
- New content section → confirm the editorial register before drafting.
- New page in the navigation → confirm the addition (the four-link nav is intentional restraint).

When the request is concrete and within established patterns (typo fix, copy refinement, new working paper following the established structure), execute without asking.

## What "done" looks like

A change is done when:

1. It renders correctly at 1280px desktop and 390px mobile.
2. It passes the brand-spec checklist above (color, typography, chrome).
3. The HTML validates (no broken tags, no orphaned elements).
4. All internal links resolve.
5. The change is consistent with the editorial voice.
6. If applicable, this `CLAUDE.md` is updated to reflect any new convention.

---

*This file is the institutional memory of the project. Updating it is part of any non-trivial change.*
