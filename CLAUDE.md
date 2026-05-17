# CLAUDE.md

> This file is read by Claude Code at the start of every session in this repository. Keep it accurate. When the project's structure or conventions change, update this file in the same commit.

## What this repository is

The institutional website of the **North Pacific Strategy Initiative (NPSI)** — an independent research imprint publishing reference-grade working papers on Pacific sovereignty, bilateral financial architecture, and the defensive options available to middle powers in a period of dollar-system stress.

**Live at:** `npsi.ca` — registered for ten years through CIRA, the canonical domain. The `.ca` is strategic, not a fallback: CIRA verifies Canadian presence (blocks typosquatters by registry policy), the long registration signals permanence, and the domain matches the imprint's editorial seat in Victoria, BC. Defensive redirects from `npsi.org` and similar are optional, not required.
**Editor:** Jesse James (`jesse@fitforgov.com`). The institutional aliases `editor@npsi.ca` and `commentary@npsi.ca` are reserved for future activation once forwarding is configured at the registrar (Cloudflare Email Routing or equivalent); until then, all editorial correspondence runs through `jesse@fitforgov.com` to ensure mail actually delivers.
**LinkedIn:** [`linkedin.com/company/north-pacific-strategy-initiative`](https://www.linkedin.com/company/north-pacific-strategy-initiative/) — the imprint's institutional social presence.
**Scope of the site:** 9 pages plus a 404 — home, four working-paper reading views (No. 1 *The Bilateral Foundation*, No. 2, No. 3, No. 4 *The Addition Paradox* — the current paper), about, engage, commentary index, colophon. Static HTML and CSS, no JavaScript framework.

**Working-paper titles (canonical):** WP1 = *The Bilateral Foundation* (retitled May 2026; was *A Canada–Korea Pacific Infrastructure Facility* — that phrase is now reserved for the CKPIF *instrument* in body prose, not the paper title). WP2 = *A Canada–United States Energy and Compute Compact*. WP3 = *A Canada–Korea Pacific Defence-Industrial Corridor*. WP4 = *The Addition Paradox*. The "Working Paper" nav link sitewide points to the current paper, **`/wp4/`**.

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

### Color tokens (CSS variables in `assets/css/site.css`)

| Token | Hex | Use |
|---|---|---|
| `--navy` | `#0E2B47` | Primary ink; wordmark, headings, dominant typography |
| `--navy-deep` | `#081C30` | Hover states only |
| `--bronze` | `#A47148` | Accents — meridian rules, italic descriptors, KPI numbers, accent borders. Never used as fill. Maximum ~5% of any composition. |
| `--teal` | `#3D6A78` | Section markers, classification lines, monospace metadata |
| `--cream` | `#F4EFE3` | Page background. NEVER use pure white as page background. |
| `--paper` | `#FBF8EF` | Card and figure backgrounds, slightly lighter than cream |
| `--ink` | `#1A1A1A` | Body text. NEVER use pure black. |
| `--rule` | `#C4B79B` | Dashed and thin rules between sections |

**Restrictions, hard:**
- Never introduce red. Both the Canadian and Korean flags use red; using it conflates the imprint with national branding.
- Never introduce a green, purple, or any non-palette accent. The four-color palette is total.
- Never use pure white (`#FFF`) as a page background. Cream is the paper.
- Never use pure black (`#000`). `--ink` is the floor.

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
- Never recolor. Pacific Navy on Document Cream. Period.
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

The "Working Paper" nav link points to the **current** working paper (currently `/wp4/`); previous papers remain accessible by direct URL and via the home-page archive. The current page's nav link gets `class="active"` (adds the bronze underline). The masthead is sticky on scroll with a subtle blur backdrop on the cream.

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
        Editor: Jesse James  ·  <a href="mailto:jesse@fitforgov.com">jesse@fitforgov.com</a><br>
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
│   ├── index.html                   Working Paper No. 1 — *The Bilateral Foundation* — full reading view (previous paper; banner points to WP4)
│   └── working-paper.pdf            full PDF release (present; direct download, no email gate)
├── wp2/
│   └── index.html                   Working Paper No. 2 — full reading view (previous paper)
├── wp3/
│   └── index.html                   Working Paper No. 3 — full reading view (previous paper)
├── wp4/
│   ├── index.html                   Working Paper No. 4 — *The Addition Paradox* — full reading view (CURRENT paper)
│   └── working-paper.pdf            full PDF release (present; direct download, no email gate)
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
7. Build the OG image at `assets/img/wp[N]-og.png` (1200×630, NPSI register, three stat blocks, no red, no flags). Build hand-coded SVG figures into `assets/img/` and reference via `<figure><img></figure>` in the paper.
8. Update the GitHub repository at `github.com/npsi-pacific/working-paper-[N]` (when the imprint org is provisioned; until then, the working repo is `cherishwins/npsi-site`).
9. Working paper IDs follow the format `NPSI-WP-NNN` (zero-padded to three digits).
10. Versions follow `vM.m[.p]` — major versions for substantive revisions, minor for named-commentary integration, patch for errata. Pre-publication drafts use `v0.x` until v1.0 is released.

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

An energy thesis for Canada — the **current** working paper, v1.0 published 15 May 2026. Four parts plus executive summary: The Diagnosis, The Chokepoint Migration, The Canadian Thesis, The Verdict. Key facts that should remain consistent across any future edits:

- **Core thesis:** the global energy transition did not substitute, it *added*. 2024 saw a record 858 TWh of new clean electricity *and* record fossil combustion; global electricity demand grew 1,172 TWh (clean supplied 858, fossil supplied the remaining 314); power-sector CO₂ ≈ 14.6 Gt; coal ≈ 10,613 TWh and forecast largest single source through the mid-2030s; clean-energy investment ≈ US$2 trillion in 2024 (≈2× fossil); upstream oil investment ≈ US$570 bn (highest since 2017).
- **Chokepoint migration:** clean-tech refining/assembly concentration in a single nation — polysilicon ≈ 95%, lithium cells ≈ 80%, NdFeB magnets ≈ 90%. Framed as concentration risk, **not** anti-clean-energy and **not** named beyond "a single nation / the People's Republic of China" as the paper does.
- **Four Canadian assets (one hand):** 3rd-largest oil reserves with lowest-carbon barrel (oil-sands intensity −33% since 2009); largest per-capita clean electricity in the industrial democracies (hydro > 380 TWh/yr); 2nd-largest high-grade uranium reserves (Athabasca Basin, 10–100× global mean grade); only G7 nation with simultaneous Pacific and Atlantic deepwater export capacity (Kitimat, Prince Rupert, Vancouver within ~5 sailing days of Yokohama/Busan/Shanghai).
- Positioned as the strategic preface to the three-rail architecture: WP1 (financial), WP2 (energy/compute), WP3 (defence-industrial).
- Editorial-voice note: the paper uses sustained funeral/inheritance metaphor ("the casket will remain closed"). Preserve it; it is intentional register, not drift. **No red** in the site rendering even though the source PDF cover uses a maroon accent — the HTML reading view uses the four-colour palette only.
- Author: Jesse James; v1.0 published 15 May 2026.
- PDF: `wp4/working-paper.pdf` — direct download, no email gate (matches WP1).

## Other NPSI projects in scope

- **Briefing Note No. 1** (`NPSI-BN-001`, two-part document on Canadian voter files and the privacy asymmetry) — exists as PDFs, not yet integrated into the site. If asked to integrate, create `bn1/index.html` modeled on `wp1/index.html` with adjustments for the briefing-note format.
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
