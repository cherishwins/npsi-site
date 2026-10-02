---
name: npsi-publish
description: Publish a new NPSI document to npsi.ca (working paper, technical briefing, briefing note, special briefing, Pacific Ledger issue), make a paper current, or apply errata to a published document. Use whenever the editor hands over a paper, a manuscript or a PDF to add, publish, integrate, correct, or supersede. Covers the intake packet, the page build, every sitewide update, the share card, and the verification gate, with the least context spent.
---

# Publishing an NPSI document

The site carries fifteen documents and grows. The procedure below keeps each publication cheap: scripts do the sitewide edits, a gate does the checking, and no step requires reading a whole page. One document per session is the default; see **Batches** for more.

**Context rules for every step**
- Never read a full paper page to edit it. Locate with `grep -n`, read with `sed -n 'a,bp'`, change with exact-match replacements that assert their match count.
- Never hand-edit the nav link or previous-paper banners across pages: `tools/set_current_paper.py` does it.
- Never eyeball links or metadata: `python3 tools/sitecheck.py` checks them.
- A document's canonical facts live in its folder's `CLAUDE.md` and load when you open that folder. Read another document's canon only when the new one cites it.

## 0. The intake packet

Ask the editor for anything missing before building; a guessed date or number becomes an erratum later.

1. **The manuscript.** For a reading view, the source text (DOCX, Markdown or Google Docs export) is far better than a PDF, whose extraction loses structure. For a PDF-first release, the release PDF.
2. **The metadata block**, filled in:

```text
Line:            Working Paper | Technical Briefing | Briefing Note | Special Briefing | Pacific Ledger
Number:          12
Title:
Subtitle:
Series (if any): Technical Series | Counter-Autonomy | none
Version:         v1.0
Release date:    2026-10-15
Canonical form:  reading view (PDF printed from it) | PDF-first (page is a release page or a full reading view)
Abstract:        (120 words or fewer)
Key findings:    (3 to 5, one line each)
Keywords:
Companions:      (published documents it builds on)
Supersedes or corrects: (if any)
Declared interests it touches: (from /disclosure/; does it need an in-document note?)
AI-assistance note in the document? yes | no
Share-card stats: (three figures, each with a short label)
Becomes the current working paper? yes | no
Canonical facts: (5 to 15 bullets: the numbers, names and dates every later edit must keep)
```

3. **Figures**, as SVG in the four-colour palette, or the data to draw them.
4. **Sources**, inside the manuscript, with URLs.

## 1. Pre-flight review (before any page exists)

Spawn one review subagent on the manuscript with this brief; it costs little and catches what the October 2026 review found across the archive:
- every URL resolves and supports the claim it is attached to (fabricated or malformed URLs were found in WP3);
- arithmetic: sums, multiples ("sevenfold"), percentages, date spans ("five days" that were seven);
- superlatives and uniqueness claims ("only", "first", "largest", "unique") each carry a source or are softened;
- no "forthcoming" or "ahead of" pointing at a date already past, unless dated as the paper's vantage;
- house rules: no first person in body text, no exclamation marks, no bold for emphasis, no anti-American register;
- consistency with the canon of every companion it cites (`grep` their `CLAUDE.md` for the same entities).

Return findings to the editor before publishing; fix what the editor approves.

## 2. Build the page

- Classify: IDs are `NPSI-WP-NNN`, `NPSI-TB-NNN`, `NPSI-BN-NNN`, `NPSI-SB-NNN`, `NPSI-PL-NNN`, zero-padded; folder is `wp12/`, `tb2/`, `bn2/`, `sb4/`, `pl2/`. Versions follow `vM.m[.p]`.
- Copy the nearest page of the same line as the template (`wp11/` for a Technical Series paper with corrections apparatus, `wp9/` for a policy paper, `sb3/` for a PDF-first release page, `pl1/` for a Ledger issue). Keep the chrome trio verbatim: skip-link, masthead, footer.
- Head: title, description, canonical, og:* (og:image is the PNG, with its true width and height), Highwire `citation_*` tags, `rel="alternate"` for the PDF, and the JSON-LD block (checklist item 8 below).
- Release files go in the folder: `working-paper.pdf` (or the line's equivalent name) and any figures.
- A document touching a declared interest carries its `aside.standard` note; PDF-first pages say so in the metadata block.

## 3. Sitewide updates

1. **Current paper** (working papers only, and only if the packet says so):
   `python3 tools/set_current_paper.py 12 --title "Title" --version v1.0 --month "October 2026"`
   It moves the nav link on every page, rewrites every previous-paper banner, gives the demoted paper its banner, and sets sitemap priorities. Add a companion sentence to the new banner by hand if the demoted paper needs one.
2. **Home page** (`index.html`): the current card (title, subtitle, summary, Read · PDF · Submit Named Commentary); the demoted paper's card moves to the top of `#archive`; briefings and Ledger issues go in their own sections, newest first. Every card carries the same three buttons, the commentary button as `btn-mono`.
3. **Commentary** (`commentary/index.html`): a section for the new document, in home-page order.
4. **Indexes**: one line in `llms.txt`; a full entry (abstract, key findings, ID, version, URLs, PDF page count) in `llms-full.txt`.
5. **Sitemap**: add the page, then its PDF (reading views first; PDFs at priority 0.4; no `changefreq`).
6. **Canon**: create `wp12/CLAUDE.md` with the packet's canonical facts, and add one row to the document index in the root `CLAUDE.md`.

## 4. Share card

Hand-code `assets/img/wp12-og.svg` from `wp1-og.svg` or `wp4-og.svg` (1200×630, three stat blocks, no red, no flags), then:

`tools/render-og.sh assets/img/wp12-og.svg`

Open the PNG and look at it before committing: lines that run off the card and fallback fonts are the two failures seen in production.

## 5. Gate

```sh
python3 tools/sitecheck.py --fix-sitemap   # lastmod from git; uncommitted files get today
python3 tools/sitecheck.py                 # must report 0 errors
python3 tools/sitecheck.py --external      # new outbound links: 404/410 fail, bot-blocking 403s warn
```

Then render the new page at 390px and 1280px. In the cloud container, Playwright's Chromium sends loopback traffic through the egress proxy (every page answers 405), so serve with `python3 -m http.server 8766 --bind "$(hostname -I | awk '{print $1}')"` and pass that address in the proxy `bypass` list. Check that `document.documentElement.scrollWidth` does not exceed the viewport.

## Errata to a published document

The policy is on `/about/`: errata are patch versions (v1.0.1). For each corrected document: fix the text, bump the version everywhere it appears (doc-class line, meta block, meta description, JSON-LD, llms entries, home card, commentary subtitle), add one dated revision line to the meta block, and regenerate the PDF if it is printed from the reading view. A PDF-first document whose PDF is not reissued gets an on-page erratum note instead. WP10 is never edited; corrections to it live in WP11.

## Batches

For several documents at once, prepare in parallel and integrate once. One subagent per document builds its folder (page, figures, share card, folder `CLAUDE.md`) and touches no shared file. Then a single pass makes every sitewide update (home, commentary, llms files, sitemap, root index, current paper) and runs the gate. Shared files edited in parallel conflict; folders do not.

## Reference: the working-paper checklist (moved verbatim from CLAUDE.md, October 2026)

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
12. **Add `wp[N]/` and `wp[N]/working-paper.pdf` (if released) to `sitemap.xml`.** `lastmod` is the date the file last *changed*, not the date it was published — take it from `git log -1 --format=%cs -- <path>` so the field stays true after later edits. Reading views are listed before the PDF releases; give the new paper `<priority>0.9</priority>` and demote the previous current paper to `0.7`. PDFs sit at `0.4` so the crawler reaches the HTML first. Do **not** add `changefreq` — Google ignores it, and asserting a cadence contradicts the imprint's own position that the papers have none.

Since October 2026, item 3, item 4's banner text and item 12's priorities are done by `tools/set_current_paper.py`; item 7's render is `tools/render-og.sh` (the bare `resvg-cli` call renders fallback fonts in a fresh container); item 12's `lastmod` is `tools/sitecheck.py --fix-sitemap`.
