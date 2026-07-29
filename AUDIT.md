# NPSI Editorial Integrity Remediation — Phase 1 Audit

**Branch:** `editorial-remediation` · **Prepared:** 29 July 2026 · **Method:** repository evidence only — every claim below carries a file:line or a git command whose output is reproducible. Nothing is asserted about the editor's interests, affiliations, or intentions beyond what the repository itself states.

**Terms of reference (as amended by the editor, 29 July 2026):** F-07 (India paper) struck. Remediation by labeling, not relocation — no published document moves or loses its URL. WP4 remains core corpus. Disclosure page linked footer-everywhere + `/about/` + doc-meta, not the primary nav. Quality gates resolved per-series by documenting existing practice. Numbering gaps resolved with a one-line archive note, not a withdrawal notice. Audit runs against all thirteen documents.

**Status note:** between the original audit (28 July) and this Phase 1, one finding was partially remediated. PR #37 (merged 29 July) rendered the missing WP2/WP3/WP9 PDFs from their canonical reading views, completed WP3 §1 (which had shipped as a structure-locked placeholder), and retired WP2's stale pre-publication-draft endmatter. The production-discipline gap behind F-09 is therefore narrower than at audit date; the About-page copy contradiction remains.

---

## 1. Corpus inventory — thirteen documents, all indexed

| # | ID | Series | Title | Released | Version | Reading view | PDF | Homepage index |
|---|----|--------|-------|----------|---------|--------------|-----|----------------|
| WP1 | NPSI-WP-001 | Working Papers | The Bilateral Foundation | May 2026 | v1.0 | `wp1/index.html` | `wp1/working-paper.pdf` | yes |
| WP2 | NPSI-WP-002 | Working Papers | A Canada–United States Energy and Compute Compact | May 2026 | v1.0 | `wp2/index.html` | `wp2/working-paper.pdf` (29 Jul) | yes |
| WP3 | NPSI-WP-003 | Working Papers | A Canada–Korea Pacific Defence-Industrial Corridor | May 2026 | v1.0.1 | `wp3/index.html` | `wp3/working-paper.pdf` (29 Jul) | yes |
| WP4 | NPSI-WP-004 | Working Papers | The Addition Paradox | 15 May 2026 | v1.0 | `wp4/index.html` | `wp4/working-paper.pdf` | yes |
| WP5 | NPSI-WP-005 | Working Papers | Sovereign Compute North | 27 May 2026 | v1.0 | `wp5/index.html` | `wp5/working-paper.pdf` (canonical) | yes |
| WP7 | NPSI-WP-007 | Counter-Autonomy | Dazzle 2.0 | 12 Jul 2026 | v1.0 | `wp7/index.html` | `wp7/working-paper.pdf` | yes |
| WP9 | NPSI-WP-009 | Working Papers | The Counterparty Problem | 27 Jul 2026 | v1.0 | `wp9/index.html` | `wp9/working-paper.pdf` (29 Jul) | yes |
| WP10 | NPSI-WP-010 | Technical Series | Fair Use for We, IP Theft for Thee | 26 Jul 2026 | v1.0 (superseded) | `wp10/index.html` | `wp10/working-paper.pdf` (canonical) | yes |
| WP11 | NPSI-WP-011 | Technical Series | Rated AAA by the Issuer | 28 Jul 2026 | v1.0 (current) | `wp11/index.html` | `wp11/working-paper.pdf` | yes |
| TB1 | NPSI-TB-001 | Technical Briefings | The Verified Sky | 11 Jun 2026 | v1.0 | `tb1/index.html` | `tb1/technical-briefing.pdf` | yes |
| BN1 | NPSI-BN-001 | Briefing Notes | The Voter File | 11 Jun 2026 | v1.0 | `bn1/index.html` | `bn1/briefing-note.pdf` | yes |
| SB1 | NPSI-SB-001 | Special Briefings | Zero Secrets | 11 Jun 2026 | v1.0 | `sb1/index.html` | `sb1/special-briefing.pdf` | yes |
| SB2 | NPSI-SB-002 | Special Briefings | The Three Doors | 2 Jul 2026 | v1.0 | `sb2/index.html` | `sb2/special-briefing.pdf` | yes |

Every published document appears on the homepage and in `sitemap.xml`, `llms.txt`, and `llms-full.txt`. There is no unlisted published document.

## 2. The numbering gaps (F-06) and the India question (F-07)

**WP6 and WP8 have never existed in this repository.** Evidence: `git log --all --oneline -- wp6 wp8 'wp6/*' 'wp8/*'` returns zero commits across all branches and all history. No file, no draft, no deletion. Nothing was withdrawn — the gaps are the author's numbering, already documented internally (`CLAUDE.md`) and in the machine index (`llms-full.txt`: "WP6 and WP8 are unreleased, so the archive carries intentional gaps at 6 and 8").

What is missing is the same sentence **on the human-facing archive**. Remediation (approved): a one-line note in the homepage archive section. Proposed wording, in register:

> *Numbering is the author's. Nos. 6 and 8 are unreleased; the archive carries the gaps rather than renumbering.*

**F-07 is struck** per the editor's amendment. Additionally confirmed from the repository side: no India-related paper exists in the repo or in any commit in history (`git log --all -i --grep='india'` returns only the WP5/SB2 publication commit, which matches "IndiaAI", a cited program name in SB1's comparison table).

## 3. Independence, affiliation, and neutrality claims — verbatim, with location

| Loc | Claim | Status against the record |
|---|---|---|
| `about/index.html:60` | "editorially independent and not affiliated with any government, institution, or commercial entity" | **Contradicted** — WP5 is "Co-issued with Fit For Gov" (`index.html:182`, `wp5/index.html:164`), a commercial entity. F-01. |
| `about/index.html:112` | Gate 5, "Independence check. No funding source, institutional partner, or commercial relationship has influenced the work." | **Contradicted** by the same co-issuance unless the relationship is disclosed and the gate rewritten to say *disclosed*, not *nonexistent*. F-01. |
| `about/index.html:123` | "NPSI takes no position on questions internal to the Korean peninsula" | **At risk** — F-02 as originally found; replacement wording gated on editor approval (Phase 2, item 9). |
| `about/index.html:140` | "An advocacy organisation… does not lobby, campaign, or endorse" | Survivable as conduct claim; adjacent to F-02's standpoint problem. |
| `about/index.html:141` | "A consultancy. NPSI does not accept paid engagements, sponsored research, or institutional funding tied to specific outcomes." | Survivable as stated; F-03 (SB2's lead-generation shape) and F-10 (TB1's "private Canadian operator" frame) require interest notes — facts gated on editor. |
| `about/index.html:142` | "A government affiliate." | No contradiction found. |
| `about/index.html:143` | "A commercial enterprise. The Initiative does not sell anything…" | No direct contradiction found on-site; F-01 pressure-tests it via the co-issuer. |
| `about/index.html:144` | "A personal platform. The author signs the work; the imprint hosts it." | **Asserted, not demonstrated** (F-11): one editor, one funder, one author; repository hosted on the editor's personal GitHub account (`github.com/cherishwins/npsi-site`, linked sitewide in the footer). Fix is candour, not deletion. |
| `about/index.html:145` | "A content stream… no mandatory cadence… published occasionally" | **Contradicted by the record** (F-09): thirteen documents in ~13 weeks (Apr 30 → Jul 28), three in the final four days. |
| `index.html:99` | "An Independent Research Imprint · Published Occasionally" | Same contradiction, on the homepage doc-class line. |
| `about/index.html:154–156` | "Funded by its editor… If at any point the Initiative accepts funding from any source other than its editor, that fact will be disclosed prominently" | The disclosure *mechanism* already promised here is the natural home of the F-01/F-02/F-12 remediation — the page commits to prominent disclosure; `/disclosure/` fulfils an existing promise rather than inventing a new organ. |
| `about/index.html:129` | "**Working Paper No. 1** is edited by Jesse James…" | **Stale** (F-08): thirteen documents; first-paper-era copy never updated. |

## 4. Cross-references to outside entities

**Fit For Gov** (the only outside co-issuer named anywhere):

- `index.html:182` — homepage WP5 card: "Co-issued with Fit For Gov."
- `wp5/index.html:164` — doc-meta: "Co-issue · Fit For Gov — municipal application layer"
- `wp5/index.html:439` — body: names Fit For Gov as "one such application-layer vendor — providing custom municipal websites, citizen portals, council systems, FOIP-release workflows and clerk-of-council tools — but the architecture is vendor-neutral."
- `llms.txt:17`, `llms-full.txt:146` — machine indexes carry the co-issuance.

Note for Phase 2 item 10: `wp5/index.html:439` is partial in-paper candour to build on — the page already names the vendor and its market. What no line on the site states is the vendor's relationship to the editor. The banner should close exactly that gap and no more.

Other external references (complete): GitHub (`cherishwins/npsi-site`, footer sitewide + About), LinkedIn company page (footer sitewide), Umami analytics (colophon; disclosed as cookieless), Google Fonts (colophon). Cited institutions and companies inside paper prose (Hanwha, Algoma, Microsoft, CoreWeave, etc.) are subjects of analysis, not affiliations. No other outside venture of the editor's is named anywhere on the site.

## 5. Quality gates versus the corpus (F-05)

The five gates at `about/index.html:107–113`, tested against all thirteen:

| Gate | Language can describe | Cannot describe |
|---|---|---|
| 1. Source verification | All thirteen | — |
| 2. Technical review ("financial-architecture, legal, and settlement components… specialist literature") | WP1, WP2, WP3, WP5, SB2 (finance/legal); partially SB1 (legal) | **WP4, WP7, WP9†, WP10, WP11, TB1, BN1** — no settlement or financial-architecture components exist in these papers |
| 3. Frame audit (counterparty-risk diversification, additive, defensive) | WP1–WP5, WP9, SB1, SB2 | **WP7, WP10, WP11, TB1, BN1** — the frame vocabulary is Pacific-financial; the technical papers run different disciplines |
| 4. Sequencing review | WP1, WP2, WP3, WP5, SB1, SB2 (recommendation-bearing papers) | WP4, WP9, WP10, WP11, BN1 (diagnostic papers with no sequenced programme) |
| 5. Independence check | All thirteen *as a check*; the wording is contradicted for WP5 (§3 above) | — |

† WP9 has financial content (EXIM, export credit) but no settlement/instrument architecture.

Same problem in Methodology: "Conventional instruments only," "live comparables" (`about/index.html:88`) and "Spread estimates" (`about/index.html:83`) are financial-series vocabulary presented as imprint-wide.

**The existing practice that solves this** (approved approach — document, don't invent): the technical papers already run their own visible, named gate sets —

- WP7: four-tier evidence discipline (Confirmed / Plausible / Speculation / Hype), hostile-read guardrails (§7)
- WP10/WP11: evidence grades (VERIFIED / CORROBORATED / ATTRIBUTED / UNDETERMINED), itemised published corrections, named falsifiers on every forecast branch
- TB1: verification-ledger architecture, benchmark-honesty rule (realistic vs headline performance), standing not-legal-advice caveat
- BN1: statutory chronology with primary citations, standing non-partisan caveat, labelled-fictional illustrative record

Phase 3 item 15 becomes: state on `/about/` that the financial gate set (gates 2–4 as written) applies to the Pacific/financial corpus, and describe the technical series' evidence-tier and correction apparatus as the technical gate set. Gates 1 and 5 remain imprint-wide (5 rewritten per F-01 to promise disclosure, not purity).

## 6. Cadence and production discipline (F-09, amended)

The record: 13 documents Apr 30 – Jul 28 (~13 weeks); May alone saw four working papers; 26–28 July saw three. Against "published occasionally" (`index.html:99`) and "no mandatory cadence… published occasionally" (`about/index.html:145`).

The deeper half of the finding — velocity outrunning production discipline — was evidenced by: WP2/WP3 having no PDFs eight weeks after publication, WP3 §1 shipping as a placeholder in a v1.0, WP2 carrying draft-era endmatter, and stale "(current)" labels in three companion lists. **All of those specific defects were remediated in PR #37 (29 July).** What remains is the copy: either the claim goes or the pace does. That is an editorial decision for Phase 2 item 8; the honest available wordings are (a) drop "occasionally" and describe the actual mode ("papers publish when ready; the record to date is front-loaded because the imprint launched with its foundational corpus"), or (b) keep the claim and let the record catch up to it. Wording gated on editor.

## 7. Findings register (amended status)

| Finding | Status | Evidence |
|---|---|---|
| F-01 Fit For Gov co-issuance vs independence claims | **Verified** | §3, §4 |
| F-02 Korea-position claim | **Verified** (line exists; standpoint facts are the editor's to state) | `about/index.html:123` |
| F-03 SB2 lead-generation shape | **Open** — gated on facts only the editor has | Phase 2 item 11 |
| F-04 Mandate vs corpus | **Verified, worse than audited** — current paper (WP11) is AI-governance; remediation by labeling + scope statement | §1 |
| F-05 Quality gates | **Verified**; per-series resolution approved | §5 |
| F-06 Numbering gaps | **Verified, benign** — never existed, nothing withdrawn; one-line archive note approved | §2 |
| F-07 India paper | **Struck** (editor's amendment; independently confirmed absent from repo and history) | §2 |
| F-08 About-page staleness | **Verified** | `about/index.html:129` |
| F-09 Cadence claim | **Verified**; production-discipline half remediated in PR #37; copy contradiction remains | §6 |
| F-10 TB1 "private Canadian operator" frame | **Open** — gated on facts only the editor has | Phase 2 item 11 |
| F-11 "Not a personal platform" | **Verified** as assertion-without-demonstration | §3 |
| F-12 Indigenous standpoint undisclosed | **Open** — disclosure content is the editor's to provide | Phase 2 item 7 |

## 8. What Phase 2 needs from the editor before any edit

Per the operating constraints, the following are required inputs, not things to be composed from inference:

1. **The interest list** for `/disclosure/` — every outside venture and interest touching published subject matter, and which papers each touches (item 7).
2. **The Fit For Gov facts** — what the co-issuance actually involved; the editor's relationship to the entity (items 7, 10).
3. **The Korea-position wording** — replacement for `about/index.html:123`; draft will be shown before commit (item 9).
4. **TB1 and SB2 facts** — whether either was written with any engagement in view, and whether any is sought (item 11).
5. **The Indigenous-standpoint wording** — ancestry as standpoint relevant to WP1/WP2's Indigenous co-ownership provisions (item 7).
6. **Cadence decision** — which honest wording replaces "published occasionally" (§6).

Everything else in Phases 2–3 (the What-we-are-not rewrite shape, per-series gates, archive gap note, F-08 fix, WP5 banner mechanics, footer/doc-meta disclosure links, index grouping labels) can be drafted from repository evidence and shown in the PR.

---

**Phase 1 ended here.** The editor approved the audit and supplied the §8 inputs; Phases 2–3 were executed 29 July 2026 (commit 98d077a, merged in PR #38): `/disclosure/` published, `/about/` rewritten disclosure-true, per-paper interest notes added (WP5 co-issuance, SB2, TB1), gates scoped per-series, gap note and editor-section staleness fixed.

## Phase 4 — Verification (run 29 July 2026, post-merge)

**Step 16 — re-read against the corpus.** One contradiction survived the Phase 2 rewrite: the homepage doc-class line "An Independent Research Imprint · Published Occasionally" (`index.html:99`) — the record is fourteen documents in thirteen weeks. Fixed in this commit ("· Victoria, British Columbia"). Sitewide sweep for every claim register in §3 returns nothing else: "not affiliated", "takes no position", "no commercial relationship", "published occasionally" — zero remaining instances.

**Step 17 — adversarial pass** (hostile reader, thirty minutes, target headline: "independent research imprint is a marketing arm for its editor's businesses"). Residual material and why each item is inert:

1. *The Fit For Gov co-issuance* — declared in three registers (WP5 note names editor ownership; /disclosure/ item 1; about lede). A conflict disclosed at this level of specificity supports the opposite headline.
2. *The Korea advocacy platform* — declared, register-separated, with the falsifiability standard stated. The graduated-system rule holds: described, never named, sitewide.
3. *The unnamed energy firm* — the one place a reader can push ("why unnamed?"). Defensible: the category, the touching papers (WP4, SB3), and the no-client-overlap statement are all declared; only the identity is withheld, and deal-sensitivity is a recognised reason.
4. *The public git history containing the pre-remediation purity claims* — usable as "they used to claim purity." Counter on the record: the correction was public, versioned, and self-initiated, consistent with the imprint's WP10/WP11 supersession discipline. The history is the audit trail, not the wound.
5. *One-person operation on a personal GitHub account* — stated plainly on /disclosure/ ("discipline of voice, not a claim of institutional scale"). Nothing left to reveal.

Nothing usable survives that the site has not already said about itself, with citations. Step 17 returns nothing.

**Step 18 — mechanical.** Every internal link and asset reference on all 21 pages resolves (automated check). The four-link nav is byte-identical across all pages. All 14 documents have PDFs matching their reading views (WP2/WP3/WP9 rendered from the canonical views 29 July, PR #37). Footer carries GITHUB · LINKEDIN · DISCLOSURE · COLOPHON on all 21 pages.

**The remediation is complete.**
