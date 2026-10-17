# Special Briefing No. 9 — canonical facts

> Loaded automatically when Claude Code reads files in `sb9/`. Every edit to this document, its register entry, its llms entries and its share card must stay consistent with what follows.

## Files

```
├── sb9/
│   ├── index.html               Special Briefing No. 9 — *Settled in Cash* — full reading view
│   └── special-briefing.pdf     11 pp., A4, dark; printed (Chromium, CSS page size) from the author's HTML with the pre-publication corrections applied
```

## Release

- Title: *Settled in Cash*. Subtitle (the author's cover stand): "The AI build was priced like a futures contract. A data centre only settles one way: physical delivery of power." Lede: "Gold, crude, the October credit scare and the money loop, checked against the record."
- Identifier: accession number `NPSI-20261016`, printed on the release without a same-day letter suffix. **No publication serial**: the register shows *serial pending* until the editor rules. Never mint `NPSI-SB-009`.
- Number: ninth in the site's Special Briefing line (folder `sb9/`). **No. 7 stays reserved** for the document named in `sb8/CLAUDE.md`; this briefing does not take it.
- Version v1.0 on the site. The author's file was labelled v3 (drafting iterations before release); the site's first published version is v1.0.
- Dated 16 October 2026 (cover, running feet); published to the site 17 October 2026 (`citation_publication_date`, JSON-LD `datePublished`; `dateCreated` carries 16 October).
- Canonical form: the PDF and the reading view carry the same text. Both come from the author's HTML press plate with the pre-publication corrections applied once (`corrections.py` in the session scratchpad; the diff is in git); the PDF is printed from the corrected plate, the page built from it. The author's uncorrected PDF of 16 October is not published. The corrections are listed at the foot of the page ("Corrections before release"), and the version stays v1.0, as SB6 and SB8 did. The six figures are the plate's inline SVGs moved onto the site tokens (bone → `--ink-soft`, cream → `--navy`, teal #5E8C9A → `--teal`, bronze → `--bronze`, plate navy → `--paper`; labels on teal circles in Fig. 05 → `--cream`), with the plate's unquoted `Source Sans 3` font name quoted (unquoted, it is invalid CSS and fell back to the serif) and Fig. 01's canvas extended so its date labels are not clipped. Page-scoped components are `sb9-` prefixed; figures scroll sideways on phones.
- Register: a **signed briefing in the author's first-person voice**, declared in the interest note ("my screen", "What I am watching", signed "J.J. · Victoria, British Columbia"). Analysis is marked "[my view]" and kept in its own sentence; the house rule against first person in working-paper body text does not apply to this signed register (precedent: SB5, SB6, SB8). Not investment advice (stated in the closing note).
- Declared interests: the energy-facilitation interest (described, never named), the adjacent applied-intelligence interest, the first-person voice and AI assistance, in the page's "Declared interests." aside and the meta block's Assistance row. `/disclosure/` lists SB9 under items 2 (adjacent) and 3.
- The author's closing pointed to *Aedificare* Edition 08, *Waiting for the Tie-In* (aedificare.art), "I mapped it, piece by piece". On 17 October aedificare.art listed seven editions and no Edition 08, so the pointer and its source were removed before release. If the edition is published, the pointer can return, and *Aedificare*, the editor's own publication, must then be declared on `/disclosure/`.

## Canonical facts

- S&P 500 closed 15 October 2026 at 7,744, 0.96% below its 6 October record (high 7,819 in Fig. 01); Nasdaq Composite 3.21% below its 6 October high (26,713 against 27,600).
- September CPI (released 14 October): 3.7% headline (3.6% forecast), 2.6% core (2.5% forecast). Fed target range 3.75–4.00% after the September meeting.
- 10-year Treasury about 5.34–5.36% intraday on 1 and 7 October, highest since 2002; closing peak 5.31% on 5 October; 5.19% on 14 October. High-yield spread 2.60 → 3.25 points since late August.
- KOSPI −7.57% on 15 October (SK hynix −11%, Samsung −9.5%). CoreWeave shares −15%+ on 14 October; its 9% notes due 1 Feb 2031 at 80.75 on 15 October (19.25 points below par), yield near 15.3%; 2032 notes near 78, just over 16%; five-year default insurance past 1,000 bp, which Reuters said implies nearly a 63% five-year default risk (at 40% recovery 1,000 bp gives about 57%, so the figure stays attributed). Oracle five-year CDS 288 bp, up from 260 (not called a record).
- Claims against delivery (Fig. 03): COMEX open interest about 41.5 million oz against 15.1 million registered, about 2.7×; Sightline 16 GW slated for 2026 against about 5 GW under construction (3.2×); Texas about 474 GW of large loads seeking to connect as of June against a 91 GW record peak (22 July) (5.2×); Dominion about 54 GW of data-centre capacity contracted (32 GW of it early-stage engineering letters) against a 4.8 GW data-centre billing peak (11.3×, "11×" in the findings). The ratios are rough magnitudes, not like-for-like measures.
- Gold: $35 peg on 15 August 1971; $289 carried forward by CPI; $1,192 by M2 (M2 grew 34.05× from $685.5 billion to $23.34 trillion); market $4,147 on 15 October 2026, 26% below the $5,608 record of 29 January 2026, 3 to 4% below its level a month earlier, up about 1% on 15 October.
- Federal debt $40.33 trillion on 14 October, $32.48 trillion held by the public; marketable $31.83 trillion (notes 51%, bills 22%, bonds 17%). Fed Treasury holdings $4.57 trillion. Runoff ended 1 December 2025; reserve management purchases from 12 December, about $40 billion a month at first. The Fed buys in the open market and does not buy new debt from the Treasury; at auctions it only rolls over its own maturing holdings as non-competitive add-ons. Treasury buybacks up to $38 billion (liquidity) and $25 billion (cash management), August–October round. 26 primary dealers (MUFG added January 2026). The $37T→$38T trillion took 71 days (2025); faster only in 2020 and early 2022; the last two took 147 and 154 days; the circulating "51 days" has no source.
- Exposure: top ten stocks about 38% of the S&P 500; index funds about 54% of US long-term mutual fund and ETF assets and 65% of domestic equity fund assets (ICI). Bank of America: the largest hyperscalers' combined free cash flow from $180 billion (2025) to −$64 billion (2026) and −$186 billion (2028).
- Verification ledger: 15 claims from the circulating summary, each with a verdict (Confirmed, Partly, Not supported, Wrong, No source, Opinion, Unverifiable, Understated, Not this month).
- Watch list: Fed decision and hyperscaler Q3 results (late October); China's export-control suspensions expire 10 and 27 November; ERCOT's Batch Zero eligibility report, covering about 194 GW, 10 December.

## Open review items

The pre-publication fact-check of 17 October 2026 and the editor's rulings on it belong in the editor's private review docket: <https://claude.ai/artifact/XL2ZeRwv1onScpBvpNkDzp>.
