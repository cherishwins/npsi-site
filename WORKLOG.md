# Work log — registry and navigation rebuild

Branch: `claude/registry-and-navigation` · started 6 October 2026 · not deployed (listed in `.vercelignore`)

This file is the running record of one piece of work, written so Jesse and any later Claude session can see what was done, what was decided, and what is left. Updated at every step. When the branch merges, fold anything durable into `CLAUDE.md` and delete this file.

## Why

Jesse's brief, 6 October: the site is hard to navigate, nothing can be found, and serial numbers have been assigned by separate sessions without a register, producing collisions. Organise it the way a think tank would, or better.

Findings that drove the design (measured, not guessed):

- 17 documents published across 5 lines; the nav exposed exactly one, labelled "Working Paper" but pointing at the latest paper only.
- No index page for working papers (`/papers/` was a 404); the archive existed only as a home-page anchor roughly 10 phone-screens down a 21-screen page.
- The published site runs two identifier schemes: SB1 to SB3 carry `NPSI-SB-00N`; SB4 and SB5 carry `NPSI-20261003-B` and `-C`.
- Serial collisions off-site: WP5 and WP9 were each assigned to two different papers by different sessions.
- Sticky masthead at 390px measured 133px tall, 16% of the viewport, permanently.

## Design (approved by Jesse, 6 October)

1. **Two identifiers, not one.** An *accession number* is assigned by machine at intake, date-based, immutable (`NPSI-YYYYMMDD-X`). A *publication serial* (`NPSI-WP-NNN` and the other lines) is assigned by Jesse alone at publication, sequential, never reused. The date-style IDs already on SB4 and SB5 become accession numbers retroactively; no page's printed ID changes.
2. **One registry file**, `registry.json` at the site root, public, lists every published document with both identifiers, line, number, title, version, dates, status, and files. `tools/registry.py --check` fails the gate if any page disagrees with the registry.
3. **Navigation**: Papers · Briefings · Ledger · Commentary · About. Replaces the four-link nav; the "never add a fifth link" rule in `CLAUDE.md` is retired in the same commit on Jesse's instruction.
4. **New pages**: `/papers/` (working papers, by publication date, current first), `/briefings/` (technical briefings, briefing notes, special briefings), `/register/` (the number register: every serial ever assigned, by number, including WP6 and WP8 as never issued, and accession numbers awaiting serials).
5. **Document pages** gain a breadcrumb and previous/next links, ordered by publication date within the line, labels carrying number and title.
6. **Home page** trimmed to a front door: hero, current paper, latest Ledger, latest briefings, links to the indexes. `#archive` and `#briefings` anchors kept as short sections so external links survive.
7. **Masthead** compacted at phone widths.

Out of scope for this branch, deliberately: topic pages or filters (house rule against tag clouds), any change to document body text or printed IDs, the light-mode media query, and any public mention of unpublished work.

## Decisions needing Jesse's ratification (flagged in the PR)

- SB4 and SB5 are registered as Nos. 4 and 5 with accession numbers `NPSI-20261003-B` and `-C` and **serial pending**. No `NPSI-SB-004` or `-005` string is written anywhere; the Serial Rule says only Jesse assigns.
- The papers index and the previous/next chain follow publication date, per the existing house rule. By date the chain runs WP7 → WP10 → WP9 → WP11, so every link carries number and title.

## Status

| Step | State |
|---|---|
| Branch, pull 129 commits, read house rules and tools | done |
| `tools/registry.py` (extract, check, render, doc-nav, nav) and `registry.json` | done |
| CSS tokens for doc-nav, register table, compact masthead | done |
| `/papers/`, `/briefings/`, `/register/` pages | done |
| Nav swap across every deployed page (25 + 3 new) | done |
| Breadcrumb and previous/next on 17 document pages | done |
| Home page trim (18,093px → 6,761px at 390px) | done |
| Tooling: `set_current_paper.py`, `sitecheck.py` updated for the new nav and registry | done |
| `llms.txt`, `llms-full.txt`, `sitemap.xml`, 404 | done |
| `CLAUDE.md`, `README.md`, `npsi-publish` skill | done |
| Gate: sitecheck 0 errors; renders at 360/390/1280 in dark and light; no horizontal scroll; chains resolve | done |
| Commit, push, open PR | done, not merged |

## Measured results

| Measure | Before | After |
|---|---|---|
| Documents reachable from the nav | 1 | 17 (via Papers, Briefings, Ledger) |
| Sticky masthead at 390px | 133px, two nav rows | 65px, one row |
| Home page height at 390px | 18,093px | 6,761px |
| Index page for working papers | none (404) | `/papers/` |
| Register of identifiers | none | `/register/` + `registry.json` |
| Gate errors | 0 | 0 (one pre-existing warning on an inline px size on the home page) |

At 340px the nav wraps to two rows (96px masthead); that width is rarer than 360 and the wrap is clean.

## Left for Jesse

1. Review and merge the PR.
2. Rule on serials for SB4 and SB5 (currently accession `NPSI-20261003-B` / `-C`, serial pending). If they become `NPSI-SB-004` and `-005`, the printed IDs on the releases and pages change under the errata policy; the register will show both.
3. The private inventory of unpublished papers (about a dozen on disk, several as Claude artifacts, two serial collisions at WP5 and WP9) is in Claude's memory folder, not in this repo. Each needs a serial from Jesse before it can be published; the accession-number form covers anything unnumbered.
4. Docket item D3 still stands: this public repo carries internal files (`AUDIT.md`, `reviewfiles.zip`, `.agents/`, `skills-lock.json`). `WORKLOG.md` is in `.vercelignore` but is in the repo; delete it after merge.

## Log

- 06 Oct · Pulled main at 4352e19 (129 commits behind locally before this). Branched. Read `CLAUDE.md`, `npsi-publish` skill, `sitecheck.py`, `set_current_paper.py`. Dumped metadata from all 17 document pages: identifiers, issue numbers, dates, versions and PDFs are all present in Highwire and JSON-LD tags, so the registry can be extracted rather than typed.
- 06 Oct · Built `tools/registry.py`; extracted `registry.json` (17 documents, 0 mismatches on round-trip). Current-paper detection first grabbed WP10 via the "supersedes" link in the home card; fixed to read the card's Read button. Series parsing fixed for WP7 (Counter-Autonomy).
- 06 Oct · Rendered `/papers/`, `/briefings/`, `/register/`; breadcrumbs on 17 pages; nav on 25 pages. Masthead 133 → 66px at 390 through fluid tokens (`--pad-masthead`, `--fs-nav`).
- 06 Oct · Gate failures and fixes: (a) nav parser read past the register page's masthead into the body, bounded it to anchor tags; (b) WP2, WP3, WP9 never declared their PDFs as `rel=alternate`, so the registry now also accepts the line's conventional filename when the file exists; (c) the "every PDF linked from home" rule widened to the index pages, since the trimmed home no longer lists every file; (d) sitemap lastmod errors are the known pre-commit quirk and clear on commit.
- 06 Oct · Document-nav insertion was not idempotent (grew a blank line per run); fixed and verified with two consecutive runs producing no diff.
- 06 Oct · Commit 1: registry, nav, pages, tooling. Gate 0 errors after commit.
- 06 Oct · 360px test wrapped the nav; nav gap made fluid (`clamp(9px, …, 28px)`), nav size min lowered 13 → 12.5px. One row from 360 up.
- 06 Oct · Commit 2: house rules, README, publish skill, this log. Pushed; PR opened.
