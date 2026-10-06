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
| `tools/registry.py` (extract, check) and `registry.json` | in progress |
| CSS tokens for doc-nav, register table, compact masthead | pending |
| `/papers/`, `/briefings/`, `/register/` pages | pending |
| Nav swap across every deployed page | pending |
| Breadcrumb and previous/next on 17 document pages | pending |
| Home page trim | pending |
| Tooling: `set_current_paper.py`, `sitecheck.py` updated for the new nav | pending |
| `llms.txt`, `llms-full.txt`, `sitemap.xml` | pending |
| `CLAUDE.md`, `README.md`, `npsi-publish` skill | pending |
| Gate: sitecheck 0 errors, 390px and 1280px renders, no horizontal scroll | pending |
| Commit, push, open PR (not merged) | pending |

## Log

- 06 Oct · Pulled main at 4352e19 (129 commits behind locally before this). Branched. Read `CLAUDE.md`, `npsi-publish` skill, `sitecheck.py`, `set_current_paper.py`. Dumped metadata from all 17 document pages: identifiers, issue numbers, dates, versions and PDFs are all present in Highwire and JSON-LD tags, so the registry can be extracted rather than typed.
