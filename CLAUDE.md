# CLAUDE.md

> This file is read by Claude Code at the start of every session in this repository. Keep it accurate. When the project's structure or conventions change, update this file in the same commit.

## What this repository is

The institutional website of the **North Pacific Strategy Initiative (NPSI)** — an independent research imprint publishing reference-grade working papers on Pacific sovereignty, bilateral financial architecture, and the defensive options available to middle powers in a period of dollar-system stress.

**Live at:** `npsi.ca` — registered for ten years through CIRA, the canonical domain. The `.ca` is strategic, not a fallback: CIRA verifies Canadian presence (blocks typosquatters by registry policy), the long registration signals permanence, and the domain matches the imprint's editorial seat in Victoria, BC. Defensive redirects from `npsi.org` and similar are optional, not required.
**Editor:** Jesse James (`editor@npsi.ca`). Standardized June 2026 (PR #24): all site-facing editorial correspondence — footers, JSON-LD, commentary mailtos, security.txt, humans.txt, CITATION.cff — uses the institutional alias `editor@npsi.ca`. The `commentary@npsi.ca` alias remains reserved for future activation. The personal address `jesse@fitforgov.com` no longer appears on the site.
**LinkedIn:** [`linkedin.com/company/north-pacific-strategy-initiative`](https://www.linkedin.com/company/north-pacific-strategy-initiative/) — the imprint's institutional social presence.
**Scope of the site:** 33 pages plus a 404 — home, the three index pages (`/papers/`, `/briefings/`, `/register/`), nine working-paper views (No. 1 *The Bilateral Foundation*, No. 2, No. 3, No. 4 *The Addition Paradox*, No. 5 *Sovereign Compute North*, No. 7 *Dazzle 2.0*, No. 9 *The Counterparty Problem*, No. 10 *Fair Use for We, IP Theft for Thee*, No. 11 *Rated AAA by the Issuer*), two technical-briefing reading views (TB No. 1 *The Verified Sky*, TB No. 2 *Running Silent*), one briefing-note reading view (BN No. 1 *The Voter File*), nine special-briefing views (SB No. 1 *Zero Secrets*, SB No. 2 *The Three Doors*, SB No. 3 *The Ledger With One Entry*, SB No. 4 *The Tollgate Markets*, SB No. 5 *One Day, Four Names*, SB No. 6 *The Walk-Away Price*, SB No. 8 *The Authored State*, SB No. 9 *Settled in Cash*, SB No. 10 *The 2027 Cliff*, with its companion checklist *Before the First of January*; No. 7 is reserved for a document whose source has not arrived), two Pacific Ledger issues (№01, July 2026; №02, October 2026) plus the `/ledger/` issue index, about, engage, commentary index, disclosure, colophon. Static HTML and CSS, no JavaScript framework. **`registry.json`** at the root is the public register of every published document (see *The register*, below); **`feed.xml`** is its Atom feed, and every document's full text is published in Markdown at **`<folder>/index.html.md`** for machine readers (see *Machine readers*, below).

**Working-paper titles (canonical):** WP1 = *The Bilateral Foundation* (retitled May 2026; was *A Canada–Korea Pacific Infrastructure Facility* — that phrase is now reserved for the CKPIF *instrument* in body prose, not the paper title). WP2 = *A Canada–United States Energy and Compute Compact*. WP3 = *A Canada–Korea Pacific Defence-Industrial Corridor*. WP4 = *The Addition Paradox*. WP5 = *Sovereign Compute North* (published 27 May 2026; `wp5/working-paper.pdf` is the canonical release, `wp5/index.html` carries the full reading view. Co-issued with Fit For Gov; companion to SB1). WP7 = *Dazzle 2.0* (first paper in the NPSI Counter-Autonomy series). WP9 = *The Counterparty Problem* (published 27 July 2026; `wp9/working-paper.pdf` generated from the reading view 29 July 2026). WP10 = *Fair Use for We, IP Theft for Thee* (Technical Series; published 26 July 2026; `wp10/working-paper.pdf` is the canonical release; **superseded by WP11** — remains available unaltered with a correction notice attached, per WP11's own commitment; never quietly edit WP10). WP11 = *Rated AAA by the Issuer* (Technical Series; published 28 July 2026; full reading view + `wp11/working-paper.pdf`, 18 pp.; supersedes WP10 with four itemised corrections at its §1). Numbering is the author's: WP6 and WP8 remain unreleased, so the archive carries intentional gaps at 6 and 8.

**Current paper: WP11** (v1.0.1 on the page since the 14 October 2026 errata; the PDF stays v1.0; published to the site 29 July 2026; WP9 held the slot for a few hours the same day before WP11 arrived). `registry.json` names it (`"current": "wp11"`), the home page's current card and `/papers/` lead with it; WP9 and WP7 carry the standard previous-paper banner; WP10 carries a supersession notice instead. Since October 2026 the primary nav does not point at the current paper. The archive runs WP9 (27 Jul) → WP10 (26 Jul) → WP7 (12 Jul) with day-level dates. Papers are ordered by publication date and nothing else.

**Disclosure regime (adopted 29 July 2026, editor's direction):** the imprint replaced its purity claims with a standing declaration of interests at **`/disclosure/`** — written in a securities-disclosure register: who writes and funds the imprint (one person), every outside interest touching published subject matter, and which papers each touches. Rules that follow from it:

- `/disclosure/` is linked from the **footer colophon sitewide** (GITHUB · LINKEDIN · LEDGER · DISCLOSURE · COLOPHON) and from `/about/` — **never from the primary nav**.
- Papers touching a declared interest carry their own `aside.standard` note: WP5 (co-issuance with Fit For Gov, the editor's civic-technology practice), SB2 (no engagement sought), TB1 (written independently, no client; adjacent-interest note), TB2 (the same applied-intelligence interest: it assesses Palantir's Gotham and Gaia and the Maven Smart System; it also states its AI assistance), SB5 (the Korean-reunification interest; the briefing's first-person voice), and since 14 October 2026 SB1, SB3, PL1, PL2, SB6 and SB8 (the energy-facilitation interest, described and never named; SB6 also declares the Korea Pro commission and AI assistance), and since 17 October SB9 (the energy-facilitation interest, the adjacent applied-intelligence interest, AI assistance, and its first-person voice) and since 28 October SB10 (the same interests, AI assistance, and its signed first-person close). Keep these notes when editing those pages.
- Independence claims on the maintained pages (home, `/about/`, `/engage/`, `/disclosure/`) are scoped to NPSI's own documents. The editor's paid external writing is the declared exception, so never restore an absolute "none has ever been accepted or sought". Dated documents (e.g. SB2's July note) speak as of their date and are not edited for this.
- `/about/` no longer claims "not affiliated with any commercial entity," "takes no position on questions internal to the Korean peninsula," or an unqualified content-cadence promise — those were replaced 29 July with disclosure-true language. Do not reintroduce purity claims the corpus contradicts.
- **The graduated-system rule:** the editor's separate Korean-reunification advocacy platform is *described but never named or linked* on npsi.ca — NPSI exists as a distinct register precisely so readers can encounter the analytical work first. Never name that platform on this site.
- Quality gates on `/about/` are scoped: Gates 1, 3, 4, 5 apply to every document; Gate 2's financial-architecture vocabulary applies to the architecture papers (1, 2, 3, 5), with the technical/open-source series held to their in-document evidence-grading disciplines.
- The public numbering note (gaps at 6 and 8, nothing withdrawn, git history as audit trail) lives on `/about/` and `/disclosure/`.
- Declared interests as first published: Fit For Gov; enterprise software / applied-intelligence work; Western operations for an international energy facilitation firm (never name the firm — deal-sensitive); Korean reunification advocacy (described, unnamed); Sagkeeng (Ojibway) ancestry as standpoint for WP1/WP2's Indigenous co-ownership provisions; external writing (Korea Pro commissioned essay, July 2026 — **paid**; `/disclosure/` §6 corrected 5 Oct 2026 after first saying no compensation had been arranged); AI drafting assistance (Claude), disclosed in-paper where material.

**PDF-first releases (WP5, SB2, SB4, SB5):** the PDF is the canonical release document; each page also carries a **full reading view** (WP5 and SB2 ported July 2026 from the release PDFs; SB4 and SB5 ported 14 October 2026 from their corrected v1.0.1 releases, with figures as inline SVG on site tokens) plus complete metadata (Highwire + JSON-LD with `encoding`) and the direct download. When porting from an author's HTML source, check its edition against the release PDF first: the SB5 source was the uncorrected v1.0, and the PDF is the text authority. **The Ledger's cadence (14 October 2026):** the Ledger no longer calls itself monthly on the maintained pages; `/ledger/`, the home card and both llms files say issues close when the account warrants one (№01 closed 28 July 2026, №02 closed 1 October 2026). PL1's own dated text keeps its July promise. Do not reintroduce a cadence promise. **Korean rollout kit:** the `npsi-korean-translation` skill is installed at `.claude/skills/npsi-korean-translation/` (register rules, glossary + WP3 supplement, QA checklist) — consult it before publishing any Korean text.

## The register (adopted October 2026)

Every published document is listed in **`registry.json`** at the site root, extracted from each page's own citation metadata by `tools/registry.py` and checked by the gate: a page that disagrees with the register fails `sitecheck`. The register page **`/register/`** renders it for readers; `/papers/` and `/briefings/` are rendered from it; the home page's two compact lists, the commentary table on `/commentary/` and every document's breadcrumb and previous/next links are rendered from it.

**Two identifiers, never confused:**

- **Publication serial** — `NPSI-WP-NNN` (and TB, BN, SB, PL). Assigned by the editor alone, at publication, sequential within its line, never reused. **Claude never mints one.** A document the editor has not numbered ships with its accession number and is listed as *serial pending*.
- **Accession number** — `NPSI-YYYYMMDD-X`. Assigned when a document enters the system, immutable, printed on the release. SB4 (`NPSI-20261003-B`), SB5 (`NPSI-20261003-C`), SB6 (`NPSI-20261002-A`), SB8 (`NPSI-20260920-B`, as printed on the author's release), TB2 (`NPSI-20261014`), SB9 (`NPSI-20261016`) and SB10 (`NPSI-20261027`), all printed without a same-day letter suffix, and Ledger №02 (`NPSI-20261001-A`) carry accession numbers only; their serials are pending the editor's ruling.

Numbers reserved and never released (WP6, WP8) stay on the register as *never issued*. The archive is ordered by publication date; the register by number; both are kept.

**Workflow:** after any change to a document's metadata, its folder, its text, or the current paper: `python3 tools/registry.py --all` (extract, render the three index pages, the home lists and `feed.xml`, refresh document breadcrumbs, rewrite the nav, write the Markdown editions, check). `tools/set_current_paper.py` runs the relevant parts itself.

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

In July 2026 the imprint adopted a **dark-first identity** at the editor's direction: the same four-colour brand, inverted. Document Cream became the ink; Pacific Navy became the paper. Nothing else changed — same wordmark geometry, same three typefaces, same bronze meridian, same chrome. Token *names* in `site.css` kept their light-era *roles* (`--navy` is still "primary ink", `--cream` is still "page background"); only the values flipped, so every page-scoped component inherits the theme untouched. **Print re-inverts to the light palette** inside `@media print` — the reference document still prints as paper. Figure SVGs, OG cards, and all raster icons were re-rendered in the dark identity. **Screen is dark only** (editor's decision, 14 October 2026): the site serves no light palette to devices that prefer light, so every reader meets the same identity as the share cards and PDFs; the `prefers-color-scheme: light` block added in July 2026 was removed and each page carries a single `theme-color` meta. Print remains the only inversion.

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

Three typefaces, **self-hosted** from `assets/fonts/` since 14 October 2026: the exact variable woff2 files Google Fonts serves, vendored by `tools/vendor-fonts.py` into `assets/css/fonts.css` (latin and latin-ext slices of the three Latin faces, plus only the Noto Serif KR slices covering Hangul set on the site, each with its original `unicode-range` so a slice downloads only when a page uses its glyphs). Every page links `/assets/css/fonts.css` once and preloads the serif roman and mono latin files; no page links Google, and the CSP allows fonts and styles from `'self'` only. Re-run the tool to add a face or weight. Do not add a fourth face without serious reason.

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
- **Square mark** (in `assets/img/favicon.svg` and the LinkedIn assets): for square/circle constraints — favicon, LinkedIn profile mark, future Slack/social where required. "NP" monogram in Pacific Navy with meridian above and mono volume marker below. On screen it is cream NP and bronze meridian on navy, drawn by `tools/render-icons.py` from the vendored Source Serif 4 Bold as outlined paths (an SVG favicon cannot load web fonts, so live text fell back to the reader's system serif). Two layouts of the same mark (October 2026): the *tab* layout, NP enlarged to read at 16px, for `favicon.svg`, `favicon-32.png`, `favicon.png` and the root `/favicon.ico` (16/32/48, which feed readers, chat unfurlers and favicon fetchers request); the *app* layout, with the original clear space, for `apple-touch-icon.png`, `icon-192.png` and `icon-512.png` (also the manifest's maskable icon and the JSON-LD `logo`). Pages link the icons with `?v=2` so returning browsers drop the old cached mark; bump it if the mark changes again.

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
      <a href="/papers/">Papers</a>
      <a href="/briefings/">Briefings</a>
      <a href="/ledger/">Ledger</a>
      <a href="/commentary/">Commentary</a>
      <a href="/about/">About</a>
    </nav>
    <div class="nav-volume">VOL. I  ·  EST. MMXXVI</div>
  </div>
</header>
```

The five-link nav (adopted October 2026 at the editor's direction, replacing a four-link nav whose first item pointed at the current paper only) is written on every page by `tools/registry.py --nav`; never hand-edit it. The active link follows the section: Papers on `/papers/` and every `wp*` page, Briefings on `/briefings/` and every `tb*`, `bn*`, `sb*` page, Ledger on `/ledger/` and `pl*`, Commentary and About on their own pages; home, engage, disclosure, colophon, register and the 404 have no active link. The masthead is sticky on scroll with a blur backdrop; its padding and the nav size are fluid tokens (`--pad-masthead`, `--fs-nav`), so it is 62px tall at 390px and one row; when a reader's large-text setting forces the five links onto two rows, the wrapped nav stays compact (no row gap, 1.3 leading) and the masthead holds near 100px.

### Document navigation (every document page)

Directly inside `<main>`, between `<!-- doc-nav -->` markers, every document carries a breadcrumb (NPSI › line › No. N) and previous/next links ordered by publication date within the line, each carrying number and title, plus the same trail as Schema.org `BreadcrumbList` JSON-LD (search engines show it in place of the bare URL). `tools/registry.py --doc-nav` writes and refreshes it; never hand-edit it.

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
        Document text: <a href="https://creativecommons.org/licenses/by/4.0/">CC-BY-4.0</a>, free to quote, share, translate and adapt, including in AI systems, with attribution. The imprint and wordmark are not licensed.<br>
        Companion record: <a href="https://www.macroview.live/ledger">MacroView daily calls, dated since 19 June 2026</a> (external, open data).
      </div>
    </div>
    <div class="colophon-right">
      VOL. I<br>
      EST. MMXXVI<br>
      <a href="https://github.com/cherishwins/npsi-site">GITHUB</a>  ·  <a href="https://www.linkedin.com/company/north-pacific-strategy-initiative/" rel="me">LINKEDIN</a>  ·  <a href="/ledger/">LEDGER</a>  ·  <a href="/disclosure/">DISCLOSURE</a>  ·  <a href="/colophon/">COLOPHON</a>
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
├── CLAUDE.md                        ← this file (house rules + document index)
├── README.md                        institutional landing for the GitHub repo
├── DEPLOYMENT.md                    deployment notes
├── index.html  404.html             home (current paper, the Ledger, compact archive and briefing lists); not-found page
├── registry.json  feed.xml          the public register of every published document, and its Atom feed (tools/registry.py)
├── papers/ briefings/ register/     index pages rendered from the registry — never hand-edit
├── about/ disclosure/ engage/ commentary/ colophon/ ledger/    institutional pages (ledger/ is the Ledger's issue index)
├── wp1/ … wp11/  tb1/ tb2/ bn1/ sb1/ … sb10/ pl1/ pl2/            one folder per document: index.html, its PDF, index.html.md (the Markdown edition, generated) and CLAUDE.md (canon)
├── llms.txt  llms-full.txt          machine-readable indexes
├── sitemap.xml  robots.txt  vercel.json  humans.txt  CITATION.cff  manifest.webmanifest  favicon.ico
├── .well-known/security.txt  .well-known/tdmrep.json  321437bffbf88535cb7beeaddd237764.txt (IndexNow key; keep)
├── assets/css/site.css              shared stylesheet, fully tokenized
├── assets/css/fonts.css  assets/fonts/   self-hosted @font-face rules and woff2 files (tools/vendor-fonts.py; OFL.txt alongside)
├── assets/img/                      wordmark (dark + light), favicons, share cards (SVG source + PNG), figures
├── tools/                           sitecheck.py · registry.py · fulltext.py · set_current_paper.py · indexnow.py · render-icons.py · pdf-metadata.py · vendor-fonts.py · archive-sources.py · render-og.sh · fonts/ (not deployed)
├── figures/                         working figure sources for papers in progress (not deployed)
└── .claude/skills/                  npsi-publish (publishing procedure) · npsi-korean-translation · fluid-scale
```

## Conventions for changes

### When adding a new page

1. **Copy `about/index.html` as the template.** It has the cleanest structure of the existing pages.
2. Update the `<title>`, meta description, OG tags (with `og:image:alt` and `twitter:image:alt`); keep the licence and feed links that follow the manifest link.
3. Run `python3 tools/registry.py --nav` to write the masthead nav (it sets the active link).
4. Use the existing CSS — do not add new tokens or new components without flagging.
5. Maintain the page footer verbatim.
6. Verify mobile rendering at 390px viewport (iPhone-class).

### When adding a new working paper

Follow the `npsi-publish` skill (`.claude/skills/npsi-publish/SKILL.md`): intake packet, pre-flight review, page build, sitewide updates, share card, gate. It carries the original twelve-step checklist verbatim; three of its steps are now scripts (`tools/set_current_paper.py`, `tools/render-og.sh`, `tools/sitecheck.py --fix-sitemap`).

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

- **`vercel.json`** — HTTP headers (CSP, HSTS, X-Frame-Options, Permissions-Policy, Referrer-Policy, X-Content-Type-Options, long-cache on immutable assets) plus URL canonicalisation: `trailingSlash: true` so `/wp11` redirects to `/wp11/` and the served URL matches `rel="canonical"`, and a 308 from `www.npsi.ca` to the apex so one hostname serves the imprint. Updating CSP requires also updating the `script-src` allowlist if a new third-party script is added. The Umami analytics domain (`cloud.umami.is`) is allowlisted; nothing else may run a script. Umami's script loads from `cloud.umami.is` but sends pageviews to `gateway.umami.is`, so `connect-src` names both; until 28 October 2026 it named only the first and every browser refused the send, so the dashboard holds no data before that date (Lighthouse's console-errors audit is how it surfaced). Fonts and stylesheets are `'self'` only (self-hosted fonts since 14 October 2026).
- **`sitemap.xml`** + **`robots.txt`** — discoverability plumbing for crawlers, Internet Archive, Google Scholar. `sitemap.xml` carries `<loc>`, `<lastmod>` and `<priority>` only; see the `npsi-publish` skill (checklist item 12) for how `lastmod` is derived; `python3 tools/sitecheck.py --fix-sitemap` applies it.
- **`humans.txt`** at site root — editorial/technical credits.
- **`llms.txt`** at site root — LLM-crawler index per the llms.txt convention: imprint summary, the use-and-citation statement, canonical URL and one-line abstract per paper, and a "Full text" list linking every Markdown edition (the gate fails a document missing from it). Update it whenever a paper or briefing is added or retitled.
- **`llms-full.txt`** at site root — the full-content companion (added July 2026): complete abstract, key findings, citation metadata, and PDF URL per document, sourced from each page's JSON-LD abstract and the per-document canonical-fact files (`<folder>/CLAUDE.md`). Update it in the same commit as `llms.txt` whenever a document is added, retitled, or superseded.
- **`robots.txt`** — allows all crawling and *explicitly* welcomes the named AI/LLM crawlers (GPTBot, ClaudeBot, Google-Extended, PerplexityBot, CCBot, et al.) and the search engines (Korea's Yeti and Daumoa among them), states its AI-use preferences in comments only (the machine-readable form is the HTTP headers; `Content-Usage`/`Content-Signal` lines inside the groups made Lighthouse report the file invalid, SEO 92), points machine readers at `llms.txt`, `llms-full.txt`, the Markdown editions, `registry.json` and `feed.xml`, and names two sitemaps: `sitemap.xml` and the Atom feed (Google and Bing read an Atom feed as a sitemap whose `<updated>` dates mark what changed). Search Console (property live since July 2026) reported on 22 October 2026 two pages indexed and 54 "Discovered – currently not indexed": a young site's crawl priority, not a technical fault (every page answers 200 to Googlebot in under a second, canonicals and sitemap agree). External links and Search Console's *Request indexing* are what move it. Maximal crawlability is deliberate imprint policy (CC-BY-4.0 text, citation-seeking); never add `Disallow` rules or `noindex` beyond the 404 page without flagging.
- **`.well-known/security.txt`** — RFC 9116 contact for security researchers. Bump the `Expires:` field annually.
- **`CITATION.cff`** at repo root — renders GitHub's "Cite this repository" widget for academic reuse.

### Machine readers (October 2026)

The imprint wants its text read, quoted, cited and used, by people and machines alike; every signal below says so in a vocabulary some reader understands. None of it changes a page's visible register.

- **Markdown editions** — `tools/fulltext.py` converts each document's `<main>` to `<folder>/index.html.md` (the llms.txt convention for a URL ending in a slash): front matter with title, identifier, version, dates, canonical URL, PDFs, licence and an exact `cite_as`, then the text, tables and sources, with figures as their `aria-label` descriptions. Derived, never hand-edited: `registry.py --all` writes them and the gate fails a stale one. Served as `text/markdown`, open CORS, `X-Robots-Tag: noindex, follow` (so search indexes keep the HTML page and the Markdown cannot compete with it as a duplicate). Each document's head links its edition with `rel="alternate" type="text/markdown"`.
- **`feed.xml`** — Atom feed of every document, newest first, rendered from the register by `registry.py --render` (with page, Markdown and PDF links and the JSON-LD abstract). A record of publication for feed readers, Naver and agents; not a content stream. Every page's head links it.
- **Licence signals** — every page's head carries `<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">`; the footer line reads "Document text: CC-BY-4.0, free to quote, share, translate and adapt, including in AI systems, with attribution"; JSON-LD carries `license` and `"isAccessibleForFree": true`; `/engage/` §4 states the machine terms; `llms.txt`, `llms-full.txt`, `robots.txt` and every Markdown edition open with the same use statement. HTTP headers on every response: `Content-Usage: train-ai=y, search=y` (IETF AI Preferences draft) and `tdm-reservation: 0`, with `/.well-known/tdmrep.json` (W3C TDMRep: no text-and-data-mining rights reserved). `robots.txt` restates them in comments, so the file stays valid RFC 9309 for every parser. These are preferences, not grants beyond CC-BY-4.0; the name and wordmark stay unlicensed everywhere.
- **Search snippets** — `X-Robots-Tag: index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1` on every response (large share images and full snippets in Google and Bing, and Discover eligibility); the 404 page's own `noindex` meta still wins.
- **Share cards** — every page carries `og:image:alt` and `twitter:image:alt` (the document's title, number and imprint), documents add `article:published_time`, `article:modified_time` where the JSON-LD has `dateModified`, and `article:section`. The gate fails a page without the alt text, licence link or feed link, and a document without its Markdown link or publication date.
- **IndexNow** — `.github/workflows/indexnow.yml` waits for Vercel's production deployment of each push to `main`, then submits the changed pages and PDFs (`tools/indexnow.py`) to api.indexnow.org, which shares them with Bing (and through it Copilot and ChatGPT search), Naver, Yandex, Seznam and Yep. The key is public by design and served at `/321437bffbf88535cb7beeaddd237764.txt`; never delete that file. Run the workflow by hand with *all* to resubmit every sitemap URL.
- **Entities** — one identity for the editor and one for the imprint, so search engines and AI systems do not confuse the author with the other Jesse James: `/about/` carries an `AboutPage` and a `Person` with `@id` `https://npsi.ca/about/#editor` (name, jobTitle Editor, url, worksFor the imprint, description from the About text); every document's JSON-LD `author` carries that `@id`, `url` and `jobTitle`, and its `publisher` the imprint's `@id` `https://npsi.ca/#organization` (the home page's `Organization`, whose `founder` points at the same Person). Add an ORCID or other profile to the Person's `sameAs` when the editor has one. The index pages (`/papers/`, `/briefings/`, `/register/`) carry a `CollectionPage` with an `ItemList` of their documents, rendered by `registry.py`. The About JSON-LD sits before the icon links on purpose: `registry.py` copies `/about/`'s head from the icon links on into the generated pages.
- **Section share cards** — `/papers/`, `/briefings/`, `/register/`, `/about/`, `/disclosure/`, `/engage/`, `/commentary/` and `/colophon/` each have their own card (`assets/img/<page>-og.svg` and `.png`, the document-card layout: classification line, title, italic line, two lines of description, no counts that could go stale), rendered with `tools/render-og.sh`; `registry.py` picks up the card for the pages it renders. The home page and the 404 keep `og-default.png`; `/ledger/` uses the current issue's card.
- **PDF metadata** — every release PDF carries Title, Author, Subject and Keywords in its document information and XMP (`tools/pdf-metadata.py --write` fills only empty fields or a tool's name, from the register and the page, and verifies every page's text is unchanged). Filled 28 October 2026 for thirteen PDFs, among them WP1's essay edition, whose author field read "python-docx". WP10 is skipped: it stays unaltered, metadata included. Run the tool after adding any PDF.
- **Brand logo** — `assets/img/npsi-logo-1080.png` (`tools/render-icons.py`), the square mark at 1080 px for profiles and directories that ask for a logo (Google Business Profile, ORCID, Zenodo). Permanent URL: https://npsi.ca/assets/img/npsi-logo-1080.png.
- **Caching** — fonts are `immutable` for a year; images (share cards, icons) cache for a day with a week of `stale-while-revalidate`, so a re-rendered card or mark reaches readers; machine files (`llms*.txt`, `registry.json`, `feed.xml`, `sitemap.xml`, `robots.txt`, `.well-known/*`, `*.md`) cache for an hour and allow any origin.

### When fixing or improving CSS

- Never introduce a new color outside the four-color palette.
- Never introduce a new typeface.
- Never add JavaScript dependencies, build tooling, or framework imports.
- Test changes in both desktop (1280px) and mobile (390px) viewports before considering done.
- **Use the fluid scale, not hard pixels.** Type and space are a continuous `clamp()` system in `site.css` (`--fs-*`, `--space-*`, fluid `--pad-x`); each clamp's max is the desktop identity and its min is the small-screen identity. The anchors are 360px and 1280px (the `fluid-scale` skill's `clamp.py` defaults), so generated tokens are pixel-identical at 1280px and 360px and interpolate between; 390px is the phone check width, not an anchor (`--fs-h1` is 28.5px there). Four older type tokens (`--fs-lede`, `--fs-h3`, `--fs-prose`, `--fs-card-title`) are hand-tuned and sit under 1px above their floors at 360px; regenerating them is a visible change, so it waits for the editor. Type clamps always carry a rem term; spacing and `--pad-x` are vw-only by design. Add new sizes as `clamp()` tokens in `:root`; do not hard-code a px size and do not add per-breakpoint font-size overrides — the `@media (max-width: 820px)` block is layout-only by design. Measure (line length) is set in `ch` via `--max-w`; keep it in the 66–75ch readability band. Print is A4 (`@page { size: A4 }`) — preserve the keep-together rules on `.pull/.wp-card/figure/.wp-meta-block`.

### When updating copy

- Read the relevant section of the brand specification (`/mnt/user-data/outputs/npsi-kit/10-NPSI-brand-specification.md` if available, or refer to the editorial-voice section above) before drafting.
- Match the existing register. The imprint speaks one way; new copy must speak that same way.
- For Korean-language content: bilingual audit table required (Korean left, English literal translation right); the `npsi-korean-translation` skill delivers it with any Korean going onto npsi.ca. No Western framing in Korean text.

## Deployment

The site deploys to **Vercel** as plain static files (headers, redirects and the `trailingSlash` rule in `vercel.json`); no build step. `DEPLOYMENT.md` covers DNS, email aliases, and pre-launch checks.

To preview locally:
```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Tools (repository only; never deployed)

- `python3 tools/sitecheck.py` — the gate. Run before every commit that touches a page; it must report 0 errors. `--external` probes outbound links; `--fix-sitemap` refreshes `<lastmod>` from git just before committing. It runs `registry.py --check` as its last step.
- `python3 tools/registry.py --all` — extract `registry.json` from the document pages, render `/papers/`, `/briefings/`, `/register/`, the home page lists and `feed.xml`, refresh every document's breadcrumb and previous/next links, write the nav on every page, write every document's Markdown edition, then check.
- `python3 tools/fulltext.py [--check]` — the Markdown editions alone (`registry.py --all` runs it).
- `python3 tools/indexnow.py --since <commit> | --all [--dry-run]` — announce changed URLs to IndexNow engines; the workflow runs it after each deploy.
- `python3 tools/render-icons.py` — redraw the square mark (favicon SVG, `/favicon.ico`, PNG icons, the 1080 px profile logo) from the vendored Source Serif 4 Bold; needs `pip install fonttools pillow`.
- `python3 tools/pdf-metadata.py [--write]` — fill missing Title, Author, Subject and Keywords in the release PDFs without touching a page; needs `pip install pikepdf` and `pdftotext`. The steps are also available singly (`--extract`, `--render`, `--doc-nav`, `--nav`, `--check`, `--list`).
- `python3 tools/set_current_paper.py N --title "…" --version v1.0 --month "Month YYYY"` — makes WP N current: every previous-paper banner, the demoted paper's banner, sitemap priorities, the registry's current paper, and the pages rendered from it. Update the home page's current card first.
- `python3 tools/archive-sources.py --check | --save | --report [--self]` — keeps every cited source in the Wayback Machine so a citation outlives its URL. `--check` looks up snapshots for all external hrefs on the site, `--save` asks Save Page Now to capture the ones without, `--self` adds the site's own pages from `sitemap.xml`; results go to `tools/archive-manifest.json` (a record, never deployed). No page is modified. `.github/workflows/archive-sources.yml` runs it weekly and commits the manifest; run `--save` from a network that can reach `web.archive.org`.
- `python3 tools/vendor-fonts.py` — refreshes `assets/fonts/*.woff2` and `assets/css/fonts.css` from Google Fonts (see *Typography*). Run it after adding a face or weight to its `FAMILIES`, or when new Korean text needs slices the site does not yet carry (the tool scans every page for Hangul).
- `tools/render-og.sh assets/img/<card>.svg` — renders a share card against the vendored brand faces in `tools/fonts/` (the bare `resvg-cli` call silently renders fallback fonts in a fresh container).

## Document index

Each document's canonical facts, file notes and open review items live in its folder's `CLAUDE.md` (`wp3/CLAUDE.md` and so on), which Claude Code loads automatically when it reads files in that folder. Open one before editing a document, its home card, its llms entries or its share card. The procedure for publishing, making a paper current, and applying errata is the `npsi-publish` skill (`.claude/skills/npsi-publish/SKILL.md`). Remaining review items across the archive are in the editor's private review docket: https://claude.ai/artifact/XL2ZeRwv1onScpBvpNkDzp

The same facts, machine-readable and gate-checked, are in `registry.json`; this table is the human summary.

| Doc | Folder | Title | Version · released | Release form |
|---|---|---|---|---|
| WP1 | `wp1/` | *The Bilateral Foundation* | v1.0.1 · May 2026, errata 14 Oct | reading view (technical specification, April 2026) + author PDF (essay edition, 15 May 2026, 17 pp.) |
| WP2 | `wp2/` | *A Canada–United States Energy and Compute Compact* | v1.0.1 · May 2026, errata 14 Oct | reading view; PDF printed from it (46 pp.) |
| WP3 | `wp3/` | *A Canada–Korea Pacific Defence-Industrial Corridor* | v1.0.2 · May 2026, rev. 29 Jul and 14 Oct | reading view (editor's note on the 6 July CPSP decision); PDF printed from it (32 pp.) |
| WP4 | `wp4/` | *The Addition Paradox* | v1.0.1 · 15 May 2026, errata 14 Oct | reading view; PDF printed from it (9 pp.) since 14 Oct — the author's longer PDF is in git history |
| WP5 | `wp5/` | *Sovereign Compute North* | v1.0.1 (page) · 27 May 2026, errata 14 Oct | PDF canonical (19 pp., v1.0) + full reading view with erratum note |
| WP7 | `wp7/` | *Dazzle 2.0* | v1.0.1 · 12 Jul 2026, errata 14 Oct | reading view; PDF printed from it (11 pp.) |
| WP9 | `wp9/` | *The Counterparty Problem* | v1.0.1 · 27 Jul 2026, errata 14 Oct | reading view; PDF printed from it (12 pp.) |
| WP10 | `wp10/` | *Fair Use for We, IP Theft for Thee* | v1.0 · 26 Jul 2026 · superseded by WP11 | PDF canonical (17 pp., unaltered); release page |
| WP11 | `wp11/` | *Rated AAA by the Issuer* | v1.0.1 (page) · 28 Jul 2026, errata 14 Oct · **current** | PDF canonical (18 pp., v1.0) + full reading view; Correction 2 withdrawn by erratum, Correction 1 under review |
| TB1 | `tb1/` | *The Verified Sky* | v1.0.1 · 11 Jun 2026, errata 14 Oct | reading view + author PDF (stands as issued) |
| TB2 | `tb2/` | *Running Silent* | v1.0.1 · dated 14 Oct 2026, published and corrected 17 Oct | reading view (set from the author's Markdown record) + PDFs, dark and cream print editions (23 pp. each), reissued at v1.0.1 from the author's corrected press plate. Accession `NPSI-20261014`; serial pending |
| BN1 | `bn1/` | *The Voter File* | v1.0.1 · 11 Jun 2026, errata 14 Oct | reading view + author PDF (stands as issued) |
| SB1 | `sb1/` | *Zero Secrets* | v1.0.1 · 11 Jun 2026, errata 14 Oct | reading view + author PDF (stands as issued) |
| SB2 | `sb2/` | *The Three Doors* | v1.0.1 · 2 Jul 2026, corrected 14 Oct (page; PDF v1.0 canonical) | PDF canonical (10 panels) + full reading view, reframed: one door where Canada counts as domestic, two that do not depend on it |
| SB3 | `sb3/` | *The Ledger With One Entry* | v1.0.1 (page) · 26 Jul 2026 | PDF canonical (39 pp.); release page; SVG share card since 14 Oct |
| SB4 | `sb4/` | *The Tollgate Markets* | v1.0.1 · 3 Oct 2026, corrected 4 Oct | PDF canonical (24 pp.) + full reading view (ported 14 Oct). Accession `NPSI-20261003-B`; serial pending |
| SB5 | `sb5/` | *One Day, Four Names* | v1.0.1 · 3 Oct 2026, corrected 4 Oct | PDF canonical (29 pp., dark; cream print edition) + full reading view (ported 14 Oct). Accession `NPSI-20261003-C`; serial pending |
| SB6 | `sb6/` | *The Walk-Away Price* | v1.0 · dated 2 Oct 2026, published 14 Oct | reading view (canonical); PDF printed from it (27 pp.). Accession `NPSI-20261002-A`; serial pending |
| SB8 | `sb8/` | *The Authored State* | v1.0 · dated 19 Sep 2026, published 14 Oct | reading view (canonical); PDF printed from it (43 pp.). Accession `NPSI-20260920-B`; serial pending. No. 7 reserved |
| SB9 | `sb9/` | *Settled in Cash* | v1.0 · dated 16 Oct 2026, published 17 Oct | reading view set from the author's HTML (v3) + PDF (11 pp.). Accession `NPSI-20261016`; serial pending. Signed, first person |
| SB10 | `sb10/` | *The 2027 Cliff* | v1.0 · dated 27 Oct 2026, published 28 Oct | reading view set from the author's HTML (v2), companion checklist as its final section; PDFs printed from the corrected plates (21 pp.; checklist 3 pp.). Accession `NPSI-20261027`; serial pending |
| PL1 | `pl1/` | *The Pacific Ledger* №01 | July 2026, closed 28 Jul; v1.0.1 corrected 14 Oct | reading view + author PDF (7 pp., stands as issued) |
| PL2 | `pl2/` | *The Pacific Ledger* №02 — *Pledged, Contingent, Operating* | October 2026, closed 1 Oct, published 14 Oct | reading view; PDF printed from it (10 pp.). Accession `NPSI-20261001-A`; serial pending |

## Series pieces in flight (not yet on the site)

- **An unnamed Nord Stream accountability piece** — five finished dark-identity figures exist (three courts: Warsaw/Karlsruhe/London; €16.9bn asset cost; MV AfD polling); no document or number yet.
- **NPSI-X dossier line** — *Follow the Money* (EU revenue, `NPSI-X-2607`, 23 July 2026) uses a separate "open-source investigative dossier" ID scheme (`NPSI-X-NNNN`) and is not part of the working-paper series; no site presence yet and none implied.

## Other NPSI projects in scope

- **Briefing Note No. 1** (`NPSI-BN-001`, Canadian voter files and the privacy asymmetry) — **integrated June 2026** as `bn1/index.html` with `bn1/briefing-note.pdf`; see `bn1/CLAUDE.md` for the canonical-fact list.
- **Briefing Note No. 2 — Confederation Mathematics** (`NPSI-BN-002`, forthcoming) — empirical constraints on provincial secession in 2026 (Quebec + Alberta), forensic two-part briefing-note format. Source material drafted, not yet integrated. If asked to integrate, create `bn2/index.html` modeled on `wp1/index.html` with briefing-note format. Cited in WP2 §10 as forthcoming.
- **Working Paper No. 3 — Pacific Defence-Industrial Corridor** (`NPSI-WP-003`, v1.0 published May 2026) — see `wp3/CLAUDE.md` for the canonical-fact list. Released ahead of the 23 May 2026 ROK Navy operational demonstration at CFB Esquimalt and the June 2026 CPSP final-contractor decision.
- **LinkedIn Company Page** assets exist in a sibling directory (`npsi-linkedin/`). Not part of this repo.

## What to ask before doing

When the request is ambiguous, ask Jesse rather than guess. Specifically:

- New domain name → confirm before find-and-replace (the kit was built for `npsi.ca`).
- New visual element → confirm it fits the brand spec.
- New content section → confirm the editorial register before drafting.
- New page in the navigation → confirm the addition (the five-link nav is intentional restraint; the register, disclosure and colophon live in the footer and the index pages, not the nav).

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
