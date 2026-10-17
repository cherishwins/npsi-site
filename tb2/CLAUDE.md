# Technical Briefing No. 2 — canonical facts

> Loaded automatically when Claude Code reads files in `tb2/`. Every edit to this document, its register entry, its llms entries and its share card must stay consistent with what follows.

## Files

```
├── tb2/
│   ├── index.html                     Technical Briefing No. 2 — *Running Silent* — full reading view
│   ├── technical-briefing.pdf         PDF, dark edition (23 pp.), v1.0.1, printed from the author's corrected press plate
│   └── technical-briefing-print.pdf   PDF, cream print edition (23 pp.), same text (the plate with data-register="light")
```

## Release

- Title: *Running Silent: What Ambient Signal Mapping Can and Cannot Find*. Short title on the site: *Running Silent*.
- Identifier: accession number `NPSI-20261014`, printed on the release without a same-day letter suffix; kept as printed (accession numbers are immutable and the register tool accepts the bare form). **No publication serial**: the register shows it as serial pending until the editor rules. Never mint `NPSI-TB-002`.
- Number: second in the site's Technical Briefing line (folder `tb2/`), after TB1 *The Verified Sky*.
- Dated 14 October 2026 (the author's date); published to the site 17 October 2026 (`citation_publication_date`, JSON-LD `datePublished`; `dateCreated` carries 14 October). **v1.0.1, 17 October 2026**: errata from the pre-publication source check, applied the day of release at the editor's direction ("fix everything"); the erratum note on the page lists them; JSON-LD `dateModified` is 17 October.
- Canonical form: the author's note on the source reads "Markdown is the record; the PDF is the copy." The reading view is ported from the author's web press plate, whose text matched the Markdown record word for word at v1.0. At v1.0.1 the corrections were applied once, to the plate (`corrections.py` and `edition.py` in the session scratchpad; the diff is in git), and both the page body and the two PDFs were regenerated from it, so page and PDFs carry the same text. The ten figures are the plate's inline SVGs on the site tokens (`.lbl` → `--navy`, `.sub` → `--ink-soft`, `.base` → `--teal`, `.hl` → `--bronze`, `.ontl` → `--cream`); on phones each scrolls sideways in `.tb2-fig-scroll`. Page-scoped components are `tb2-` prefixed.
- PDF reissue (v1.0.1): the byline reads "Jesse James · Editor · editor@npsi.ca" (the personal LinkedIn and "Founding Editor" are gone); the closing line reads "Unclassified. Researched and drafted with AI assistance (Claude); the author is responsible for every claim. Interests declared at npsi.ca/disclosure/." (replacing "Independent research. No funding conflicts. Analysis first, advocacy never."). Fig. 1's maximum height is 140px so Chapter 1 keeps to one A4 page; printing the original plate with Playwright gives 24 pages with a three-line orphan, the corrected plate 23. The v1.0 PDFs are in git history.
- Interest note: the editor's enterprise-software and applied-intelligence work (the interest TB1 declares), plus the AI-assistance statement. `/disclosure/` lists TB2 under that interest and among the documents that state AI assistance in-document.

## Canonical facts (as corrected at v1.0.1)

- Subject: a claim-by-claim assessment of a widely circulated AI-generated text claiming "passive multi-domain over-the-horizon target fusion". The text under review is not identified by author, date or platform; that is an open item.
- Grading scale: (a) established, (b) demonstrated, (c) speculative, (d) wrong. Eighteen ledger entries: five (a) (claim 03 qualified; entry 11 is the briefing's corrected restatement of claim 10), one (b), seven (c), one (c)/(d) (claim 12), four (d). The cover's "4 wrong as written" and Fig. 10 now agree: claim 12 has its own row.
- Eight key findings (01–08), four key judgments (KJ-1 to KJ-4), three recommendations.
- Physics: seawater about 4 S/m; skin depth about 1.8 m at 20 kHz; about 4.9 dB per metre; a hull at 100 m sits about 55 skin depths and nearly 490 dB below the surface field. VLF broadcasts at 10–30 kHz, wavelengths 10–30 km; Virginia-class about 115 m, Ohio-class about 170 m; the hull is between about 1/60 and 1/260 of a wavelength; Rayleigh scattering on the (ka)³ estimate puts the scattered field some 75 to 115 dB below the incident field. Seawater ends the VLF story within tens of metres (submarines receive VLF at shallow depth).
- Dark vessels: Paolo et al., *Nature* 625 (2024): 72–76% of industrial fishing vessels not publicly tracked; 21–30% of transport and energy vessel **activity** missing from public tracking.
- Spoofing: fourteen states' open letter, 26 January 2026; RIN report dated **23 January 2026** (the report's own date; the review's "26 January" is the announcement and was not applied); Windward, 1,650+ vessels on 7 March 2026. SeaSpoofFinder (arXiv 2602.16257) was withdrawn by its author and is not cited.
- Fibre sensing: 148 km in standard fibre and 171 km in low-loss fibre without inline amplification (Waagaard et al., *OSA Continuum* 4(2), 2021) — the review's doubt about 148 km was wrong.
- Passive radar: Hensoldt, "The achieved ranges over the Baltic Sea coast were up to 300km" (NATO measurement campaign, 29 Oct 2019); "more than 180 objects up to a range of 250 km" is Diehl's figure for TwInvis in IRIS-T SLM (Defense News, 10 Aug 2023), not a 2018 German Air Force demonstration.
- Kill chain: Watts (CSBA, *The Evolution of Precision Strike*, 2013, quoted by Otto Kreisher in Air Force Magazine, 1 Dec 2013): "the Chinese have yet to conduct an end-to-end test…"; an August 2020 strike on a moving target ship reported by SCMP (14 Nov 2020) from a PLA-linked source is unconfirmed. Skywave patent US 11,953,580 (University of Birmingham, 9 Apr 2024) cites Frazer, Heitmann and Abramovich (2014).
- Space: NROL-179 (19 June 2026) the fourteenth proliferated-architecture launch (six in 2024 from May, five in 2025, three in 2026); "exceeding expectations" is from NRO news, Space Symposium, April 2026; 21 SDA Tranche 1 Transport Layer satellites deployed by Northrop Grumman on 10 October 2026.
- Fusion: Maven Smart System ceiling about $1.3 billion through 2029 ($480M IDIQ May 2024, raised by $795M May 2025); users about 50,000 in January 2026 and more than 100,000 by September 2026 (James Mazol, DefenseScoop, 22 September 2026). Deputy Secretary Steve Feinberg's memo of 9 March 2026 **directed** a transition to programme of record by fiscal year-end, administration moving from NGA to the CDAO. Gaia, per Palantir's G-Cloud 14 service definition (2 May 2024): "a collaborative geospatial command and control application"; it is a map, not a sensor.
- Concealment record: Haystack, carrier survival from under 2 hours to 8–15 hours; NORPAC 1982 Midway group four days undetected (participant account, not independently confirmed); UPTIDE average about 5.5 days.
- Base-rate figure: a 99%-specific detector scanning 5,000 ships flags 50 false carriers per sweep (illustrative).
- Register: no first or second person; no unsourced superlatives; Chinese research attributed to its reporting outlet and treated as claims; classified capability neither claimed nor assessed.

## Open review items

Not verified in the October 2026 source check (absence of a result is not an error): TRAPS "up to forty-five" units and the FY2019/FY2020 Congressional adds (only the $72.8M award verified); the DoD "complements…" wording; UPTIDE's 5.5 days; NHHC's NORPAC quotations (a contemporary press report describes simulated attacks on both Enterprise and Midway); the Hainan "dark ships" quote; China-Arms (June 2026); CASI's DWL002 ranges; Silentium's ranges; VERA-NG specifications; YLC-29; NEMESIS in FY2014 exhibits; DARPA's April 2016 testimony; the 2021 HawkEye Tartus case; the 50,000-float planning figure. The editor's private review docket: <https://claude.ai/artifact/XL2ZeRwv1onScpBvpNkDzp>.
