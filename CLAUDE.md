# CLAUDE.md

> This file is read by Claude Code at the start of every session in this repository. Keep it accurate. When the project's structure or conventions change, update this file in the same commit.

## What this repository is

The institutional website of the **North Pacific Strategy Initiative (NPSI)** — an independent research imprint publishing reference-grade working papers on Pacific sovereignty, bilateral financial architecture, and the defensive options available to middle powers in a period of dollar-system stress.

**Live at:** `npsi.ca` — registered for ten years through CIRA, the canonical domain. The `.ca` is strategic, not a fallback: CIRA verifies Canadian presence (blocks typosquatters by registry policy), the long registration signals permanence, and the domain matches the imprint's editorial seat in Victoria, BC. Defensive redirects from `npsi.org` and similar are optional, not required.
**Editor:** Jesse James (`editor@npsi.ca`). Standardized June 2026 (PR #24): all site-facing editorial correspondence — footers, JSON-LD, commentary mailtos, security.txt, humans.txt, CITATION.cff — uses the institutional alias `editor@npsi.ca`. The `commentary@npsi.ca` alias remains reserved for future activation. The personal address `jesse@fitforgov.com` no longer appears on the site.
**LinkedIn:** [`linkedin.com/company/north-pacific-strategy-initiative`](https://www.linkedin.com/company/north-pacific-strategy-initiative/) — the imprint's institutional social presence.
**Scope of the site:** 24 pages plus a 404 — home, nine working-paper views (No. 1 *The Bilateral Foundation*, No. 2, No. 3, No. 4 *The Addition Paradox*, No. 5 *Sovereign Compute North*, No. 7 *Dazzle 2.0*, No. 9 *The Counterparty Problem*, No. 10 *Fair Use for We, IP Theft for Thee*, No. 11 *Rated AAA by the Issuer*), one technical-briefing reading view (TB No. 1 *The Verified Sky*), one briefing-note reading view (BN No. 1 *The Voter File*), five special-briefing views (SB No. 1 *Zero Secrets*, SB No. 2 *The Three Doors*, SB No. 3 *The Ledger With One Entry*, SB No. 4 *The Tollgate Markets*, SB No. 5 *One Day, Four Names*), one Pacific Ledger issue (№01, July 2026) plus the `/ledger/` issue index, about, engage, commentary index, disclosure, colophon. Static HTML and CSS, no JavaScript framework.

**Working-paper titles (canonical):** WP1 = *The Bilateral Foundation* (retitled May 2026; was *A Canada–Korea Pacific Infrastructure Facility* — that phrase is now reserved for the CKPIF *instrument* in body prose, not the paper title). WP2 = *A Canada–United States Energy and Compute Compact*. WP3 = *A Canada–Korea Pacific Defence-Industrial Corridor*. WP4 = *The Addition Paradox*. WP5 = *Sovereign Compute North* (published 27 May 2026; `wp5/working-paper.pdf` is the canonical release, `wp5/index.html` carries the full reading view. Co-issued with Fit For Gov; companion to SB1). WP7 = *Dazzle 2.0* (first paper in the NPSI Counter-Autonomy series). WP9 = *The Counterparty Problem* (published 27 July 2026; `wp9/working-paper.pdf` generated from the reading view 29 July 2026). WP10 = *Fair Use for We, IP Theft for Thee* (Technical Series; published 26 July 2026; `wp10/working-paper.pdf` is the canonical release; **superseded by WP11** — remains available unaltered with a correction notice attached, per WP11's own commitment; never quietly edit WP10). WP11 = *Rated AAA by the Issuer* (Technical Series; published 28 July 2026; full reading view + `wp11/working-paper.pdf`, 18 pp.; supersedes WP10 with four itemised corrections at its §1). Numbering is the author's: WP6 and WP8 remain unreleased, so the archive carries intentional gaps at 6 and 8.

**Current paper: WP11** (published to the site 29 July 2026; WP9 held the slot for a few hours the same day before WP11 arrived). The "Working Paper" nav link sitewide points to **`/wp11/`**; WP9 and WP7 carry the standard previous-paper banner; WP10 carries a supersession notice instead. The archive runs WP9 (27 Jul) → WP10 (26 Jul) → WP7 (12 Jul) with day-level dates. Papers are ordered by publication date and nothing else.

**Disclosure regime (adopted 29 July 2026, editor's direction):** the imprint replaced its purity claims with a standing declaration of interests at **`/disclosure/`** — written in a securities-disclosure register: who writes and funds the imprint (one person), every outside interest touching published subject matter, and which papers each touches. Rules that follow from it:

- `/disclosure/` is linked from the **footer colophon sitewide** (GITHUB · LINKEDIN · LEDGER · DISCLOSURE · COLOPHON) and from `/about/` — **never from the four-link nav**.
- Papers touching a declared interest carry their own `aside.standard` note: WP5 (co-issuance with Fit For Gov, the editor's civic-technology practice), SB2 (no engagement sought), TB1 (written independently, no client; adjacent-interest note), SB5 (the Korean-reunification interest; the briefing's first-person voice). Keep these notes when editing those pages.
- `/about/` no longer claims "not affiliated with any commercial entity," "takes no position on questions internal to the Korean peninsula," or an unqualified content-cadence promise — those were replaced 29 July with disclosure-true language. Do not reintroduce purity claims the corpus contradicts.
- **The graduated-system rule:** the editor's separate Korean-reunification advocacy platform is *described but never named or linked* on npsi.ca — NPSI exists as a distinct register precisely so readers can encounter the analytical work first. Never name that platform on this site.
- Quality gates on `/about/` are scoped: Gates 1, 3, 4, 5 apply to every document; Gate 2's financial-architecture vocabulary applies to the architecture papers (1, 2, 3, 5), with the technical/open-source series held to their in-document evidence-grading disciplines.
- The public numbering note (gaps at 6 and 8, nothing withdrawn, git history as audit trail) lives on `/about/` and `/disclosure/`.
- Declared interests as first published: Fit For Gov; enterprise software / applied-intelligence work; Western operations for an international energy facilitation firm (never name the firm — deal-sensitive); Korean reunification advocacy (described, unnamed); Sagkeeng (Ojibway) ancestry as standpoint for WP1/WP2's Indigenous co-ownership provisions; external writing (Korea Pro commissioned essay, July 2026); AI drafting assistance (Claude), disclosed in-paper where material.

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
├── index.html  404.html             home (current paper, the Ledger, archive, briefings); not-found page
├── about/ disclosure/ engage/ commentary/ colophon/ ledger/    institutional pages (ledger/ is the Ledger's issue index)
├── wp1/ … wp11/  tb1/ bn1/ sb1/ … sb5/ pl1/                    one folder per document: index.html, its PDF, and CLAUDE.md (canon)
├── llms.txt  llms-full.txt          machine-readable indexes
├── sitemap.xml  robots.txt  vercel.json  humans.txt  CITATION.cff  manifest.webmanifest  .well-known/security.txt
├── assets/css/site.css              shared stylesheet, fully tokenized
├── assets/img/                      wordmark (dark + light), favicons, share cards (SVG source + PNG), figures
├── tools/                           sitecheck.py · set_current_paper.py · render-og.sh · fonts/ (not deployed)
├── figures/                         working figure sources for papers in progress (not deployed)
└── .claude/skills/                  npsi-publish (publishing procedure) · npsi-korean-translation · fluid-scale
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

- **`vercel.json`** — HTTP headers (CSP, HSTS, X-Frame-Options, Permissions-Policy, Referrer-Policy, X-Content-Type-Options, long-cache on immutable assets) plus URL canonicalisation: `trailingSlash: true` so `/wp11` redirects to `/wp11/` and the served URL matches `rel="canonical"`, and a 308 from `www.npsi.ca` to the apex so one hostname serves the imprint. Updating CSP requires also updating the `script-src` allowlist if a new third-party script is added. The Umami analytics domain (`cloud.umami.is`) is allowlisted; nothing else may run a script.
- **`sitemap.xml`** + **`robots.txt`** — discoverability plumbing for crawlers, Internet Archive, Google Scholar. `sitemap.xml` carries `<loc>`, `<lastmod>` and `<priority>` only; see the `npsi-publish` skill (checklist item 12) for how `lastmod` is derived; `python3 tools/sitecheck.py --fix-sitemap` applies it.
- **`humans.txt`** at site root — editorial/technical credits.
- **`llms.txt`** at site root — LLM-crawler index per the llms.txt convention: imprint summary, canonical URL and one-line abstract per paper. Update it whenever a paper or briefing is added or retitled.
- **`llms-full.txt`** at site root — the full-content companion (added July 2026): complete abstract, key findings, citation metadata, and PDF URL per document, sourced from each page's JSON-LD abstract and the per-document canonical-fact files (`<folder>/CLAUDE.md`). Update it in the same commit as `llms.txt` whenever a document is added, retitled, or superseded.
- **`robots.txt`** — allows all crawling and *explicitly* welcomes the named AI/LLM crawlers (GPTBot, ClaudeBot, Google-Extended, PerplexityBot, CCBot, et al.) with a comment header pointing machine readers at `llms.txt` / `llms-full.txt`. Maximal crawlability is deliberate imprint policy (CC-BY-4.0 text, citation-seeking); never add `Disallow` rules or `noindex` beyond the 404 page without flagging.
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

The site deploys to **Vercel** as plain static files (headers, redirects and the `trailingSlash` rule in `vercel.json`); no build step. `DEPLOYMENT.md` covers DNS, email aliases, and pre-launch checks.

To preview locally:
```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Tools (repository only; never deployed)

- `python3 tools/sitecheck.py` — the gate. Run before every commit that touches a page; it must report 0 errors. `--external` probes outbound links; `--fix-sitemap` refreshes `<lastmod>` from git just before committing.
- `python3 tools/set_current_paper.py N --title "…" --version v1.0 --month "Month YYYY"` — makes WP N current: nav link on every page, every previous-paper banner, the demoted paper's banner, sitemap priorities.
- `tools/render-og.sh assets/img/<card>.svg` — renders a share card against the vendored brand faces in `tools/fonts/` (the bare `resvg-cli` call silently renders fallback fonts in a fresh container).

## Document index

Each document's canonical facts, file notes and open review items live in its folder's `CLAUDE.md` (`wp3/CLAUDE.md` and so on), which Claude Code loads automatically when it reads files in that folder. Open one before editing a document, its home card, its llms entries or its share card. The procedure for publishing, making a paper current, and applying errata is the `npsi-publish` skill (`.claude/skills/npsi-publish/SKILL.md`). Remaining review items across the archive are in the editor's private review docket: https://claude.ai/artifact/XL2ZeRwv1onScpBvpNkDzp

| Doc | Folder | Title | Version · released | Release form |
|---|---|---|---|---|
| WP1 | `wp1/` | *The Bilateral Foundation* | v1.0 · May 2026 | reading view + author PDF |
| WP2 | `wp2/` | *A Canada–United States Energy and Compute Compact* | v1.0 · May 2026 | reading view; PDF printed from it (45 pp.) |
| WP3 | `wp3/` | *A Canada–Korea Pacific Defence-Industrial Corridor* | v1.0.1 · May 2026, rev. 29 Jul | reading view; PDF printed from it (30 pp.) |
| WP4 | `wp4/` | *The Addition Paradox* | v1.0 · 15 May 2026 | reading view + author PDF |
| WP5 | `wp5/` | *Sovereign Compute North* | v1.0 · 27 May 2026 | PDF canonical (19 pp.) + full reading view |
| WP7 | `wp7/` | *Dazzle 2.0* | v1.0 · 12 Jul 2026 | reading view; PDF printed from it |
| WP9 | `wp9/` | *The Counterparty Problem* | v1.0 · 27 Jul 2026 | reading view; PDF printed from it (12 pp.) |
| WP10 | `wp10/` | *Fair Use for We, IP Theft for Thee* | v1.0 · 26 Jul 2026 · superseded by WP11 | PDF canonical (17 pp., unaltered); release page |
| WP11 | `wp11/` | *Rated AAA by the Issuer* | v1.0 · 28 Jul 2026 · **current** | PDF canonical (18 pp.) + full reading view |
| TB1 | `tb1/` | *The Verified Sky* | v1.0 · 11 Jun 2026 | reading view + PDF |
| BN1 | `bn1/` | *The Voter File* | v1.0 · 11 Jun 2026 | reading view + PDF |
| SB1 | `sb1/` | *Zero Secrets* | v1.0 · 11 Jun 2026 | reading view + PDF |
| SB2 | `sb2/` | *The Three Doors* | v1.0 · 2 Jul 2026 | PDF canonical (10 panels) + full reading view |
| SB3 | `sb3/` | *The Ledger With One Entry* | v1.0 · 26 Jul 2026 | PDF canonical (39 pp.); release page |
| SB4 | `sb4/` | *The Tollgate Markets* | v1.0.1 · 3 Oct 2026, corrected 4 Oct | PDF canonical (24 pp.); release page |
| SB5 | `sb5/` | *One Day, Four Names* | v1.0.1 · 3 Oct 2026, corrected 4 Oct | PDF canonical (29 pp., dark; cream print edition); release page |
| PL1 | `pl1/` | *The Pacific Ledger* №01 | July 2026, closed 28 Jul | reading view + author PDF (7 pp.) |

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
