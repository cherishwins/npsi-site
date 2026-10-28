---
title: "The Voter File"
subtitle: "What every federal political party holds on every Canadian voter — and the statute that, as of March 2026, removes that file from provincial and territorial privacy law and leaves voters no right of access or correction, retroactive to the year 2000."
series: "Briefing Notes"
number: 1
identifier: "NPSI-BN-001"
version: "v1.0.1"
published: "2026-06-11"
status: published
author: "Jesse James"
publisher: "North Pacific Strategy Initiative"
canonical_url: "https://npsi.ca/bn1/"
pdf:
  - "https://npsi.ca/bn1/briefing-note.pdf"
description: "What Canadian federal parties hold on every voter, the five-layer file, and the 2026 statute that removes it from provincial privacy law."
license: "CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)"
cite_as: "James, J. (2026). The Voter File (NPSI Briefing Note No. 1, NPSI-BN-001, v1.0.1). North Pacific Strategy Initiative. https://npsi.ca/bn1/"
---

> Machine-readable full text of NPSI Briefing Note No. 1, *The Voter File*, from the reading view at https://npsi.ca/bn1/. The reading view and the PDF are the editions of record; figures are given as their text descriptions. The text is licensed CC-BY-4.0: quote it, summarise it, translate it, share it and use it, including in AI systems and their answers, with attribution to the author and a link to https://npsi.ca/bn1/. The NPSI name and wordmark are not licensed. Register of every NPSI document: https://npsi.ca/registry.json · index for machine readers: https://npsi.ca/llms.txt

Briefing Note No. 1 · v1.0.1 · June 2026 · For Discussion v1.0.1 · OCTOBER 2026

# The Voter File

What every federal political party holds on every Canadian voter — and the statute that, as of March 2026, removes that file from provincial and territorial privacy law and leaves voters no right of access or correction, retroactive to the year 2000.

## Erratum, 14 October 2026 (v1.0.1).

Corrections to the text of 11 June 2026, found in review. The subtitle said Bill C-4 placed the voter file “beyond every privacy law in the country”; the note’s own account of the Canada Elections Act regime that remains contradicts that, and the line now says what the statute does: it removes the file from provincial and territorial privacy law and leaves voters no right of access or correction. In the citations, *Liberal Party of Canada v. The Complainants* carries its neutral citation (2024 BCSC 814), Bill C-4 its chapter (S.C. 2026, c. 2), and an untitled “(eds.)” credit is replaced by two titled works. Three register fixes: “moved in the opposite direction”; emphasis on “retroactive” set in italic rather than bold; “across party lines” for a U.S. idiom. The series index is dated to the release and includes Working Paper No. 5. The PDF of 11 June stands as issued with these corrections attached.

- **Author:** Jesse James
- **Document ID:** `NPSI-BN-001`
- **Version:** `v1.0.1` · [change log](https://github.com/cherishwins/npsi-site/commits/main/bn1/index.html)
- **Series:** Briefing Note — the imprint's short-form line: a single mechanism, documented end to end, in under twenty minutes of reading
- **Released:** 11 June 2026 · Victoria, British Columbia
- **Revised:** v1.0.1 · 14 October 2026 · errata: the headline claim about Bill C-4 restated to what the statute does; the neutral citation and chapter number supplied; an untitled credit replaced; three register fixes; the series index dated to release. The PDF of 11 June stands as issued.
- **Status:** Unclassified · For public distribution. Editorially controlled. Public version-controlled review open.
- **Cite as:** James, J. (2026). *The Voter File* (NPSI Briefing Note No. 1, v1.0.1). https://npsi.ca/bn1/

Every major Canadian federal political party maintains a database with a record on substantially every voter in the country. The record is assembled in five layers: the Elections Canada list of electors as the statutory spine; the party's own canvassing observations; appended public records; appended commercial data; and modelled scores predicting how the voter will behave. No layer requires the voter's consent. No layer grants the voter a right of access or correction. This briefing note documents the file — layer by layer, with a worked illustrative record — and then documents the law that governs it.

The law is the second finding, and it is recent. In March 2026, Part 4 of Bill C-4 — an omnibus affordability bill — received royal assent, replacing the privacy regime for federal political parties in the Canada Elections Act and *explicitly excluding* them from provincial and territorial privacy law, retroactive to the year 2000.^[1] The provision was drafted while British Columbia's courts were considering whether that province's privacy law reached federal parties; it was designed to settle the question by statute before the courts could.^[2] The Senate proposed a three-year sunset clause; the House rejected it; every party in the Commons supported the final bill except the Green Party.^[3] The file described in Part I of this note is now, by Parliament's own hand, the least-regulated large personal database in Canada.

## § I · The File: Five Layers

The voter file is not a list. It is a relational database in which a statutory spine is progressively enriched until the record can predict the voter's behaviour. The layers below are documented across party privacy policies, vendor marketing, parliamentary testimony, and the academic literature on Canadian data-driven campaigning.^[4]

*Table 1 · The five layers of a Canadian federal voter file*

| Layer | Contents | Source and legal basis |
|---|---|---|
| **1 · Statutory spine** | Name, address, unique elector identifier; updated lists during writ periods including who has voted (bingo sheets) | List of electors supplied to parties by Elections Canada under the Canada Elections Act; no voter consent involved or required |
| **2 · Canvassing layer** | Door-knock and phone observations: stated support, lawn sign, issues raised, demeanour, languages spoken, accessibility notes, donation and volunteering history | Collected by the party's own volunteers and staff; logged in party CRM tools at the door |
| **3 · Public-records layer** | Property registry data, political donation disclosures, professional licensure, corporate registries, court records where digitized | Appended from public registries; "public" at the record level, profiling-grade in aggregate |
| **4 · Commercial layer** | Geodemographic segment codes (e.g., postal-code lifestyle clusters), appended consumer attributes, social-platform custom-audience matching, and — at the aggressive end of practice — mobile location-derived audience data | Purchased or licensed from commercial data brokers and platforms; collected from consumers under commercial terms, repurposed for politics |
| **5 · Modelled scores** | Support score, turnout propensity, persuadability, issue-salience scores, volunteer and donation propensity — typically expressed 0–100 per voter | Computed by the party or its vendors from layers 1–4; the scores, not the raw data, drive who gets contacted and about what |

What the layered structure produces is best seen in a single record. The record below is *illustrative and fictional* — no real person — but every field type in it is documented practice.

Illustrative Record · Elector № [REDACTED] Fictional · Field types documented

Spine**F., 52** · single-family dwelling, suburban riding, BC · on list since 1998 · voted in 7 of last 8 federal elections

Canvass2021: "leaning, healthcare top issue" · 2025: refused at door, sign for rival party noted · spouse identified as supporter

PublicProperty assessed mid-six-figures, owned 14 yrs · $400 donation to a rival party, 2019 · registered professional designation

CommercialGeodemographic cluster: "established suburban families" · appended attributes: charitable donor, news-radio listener · matched to platform custom audience

ModelledSupport 31/100 · Turnout 88/100 · Persuadability 64/100 · Issue salience: healthcare 0.81, affordability 0.77

Consent obtained: none requiredRight of access: none exists

Two properties of this record deserve emphasis. First, the high-turnout, mid-persuadability profile makes this fictional voter a priority contact — the file exists precisely to find her. Second, she cannot see it. There is no statutory right for a Canadian to access, correct, or delete their record in a federal party's database. That is not an oversight in the law. As of March 2026, it is the law's design.

## § II · The Asymmetry: How the File Escaped Every Statute

A grocery chain holding one tenth of this data on its loyalty-card members would owe those members access, correction, breach notification, and a complaints regime under PIPEDA. The voter file owes its subjects nothing, and the path by which that came to be is short enough to state in four steps.

### Step one: PIPEDA never applied

The federal private-sector privacy statute governs the collection of personal information in the course of *commercial activity*. Federal political parties are not engaged in commercial activity when they profile voters, and so fall outside the Act — a position confirmed by the federal privacy regime's own administrators over many years.^[5] The Privacy Act, governing federal institutions, does not reach parties either. Parties occupy a gap between the two pillars of federal privacy law.

### Step two: Bill C-76 installed a placebo

The Elections Modernization Act of 2018 required parties to *publish a privacy policy* as a condition of registration. It did not regulate what the policy must permit or forbid, created no audit power over the policy's substance, and granted voters no rights against the party. A party complies by describing its practices, whatever they are.^[6]

### Step three: British Columbia found the gap — and the courts agreed enough to frighten

Three BC complainants asked whether the province's Personal Information Protection Act applied to federal parties operating in BC. In Order P22-02 (2022), the BC Information and Privacy Commissioner's delegate held that it did, and the BC Supreme Court upheld that conclusion on judicial review in 2024 — the first crack in the asymmetry: one province's law, with real access and consent rights, reaching the federal voter file. The parties appealed.^[7]

### Step four: Parliament closed the gap from the inside — March 2026

While the BC appeal was pending, the government introduced Bill C-4, the *Making Life More Affordable for Canadians Act*. Part 4 of that affordability bill replaced the federal parties' privacy regime in the Canada Elections Act with one declared to be national, uniform, exclusive, and complete — and to exclude provincial and territorial privacy law from applying to federal parties at all, *retroactive to the year 2000*.^[8] The substantive content of the new federal regime is, in essence, Step Two again: parties must have policies; the policies are not audited; voters gain no access, correction, or deletion rights. The Chief Electoral Officer told the Senate committee he was not consulted on the provisions and characterized the bill as not enhancing privacy protection; protections from an earlier bill (C-65) that had included prohibitions on selling voter data died with the 2025 dissolution and were not carried into C-4.^[9] The Senate, after expert study, proposed a three-year sunset clause that would have returned the question to Parliament; the House rejected the amendment, and the bill received royal assent in March 2026 with every party in the Commons in support except the Green Party.^[10]

The file is the least-regulated large personal database in Canada — not by oversight, but by a recorded vote of the people the file elects. *— §II, The Asymmetry*

The structural point matters more than the partisan one, and this note makes no partisan claim: the immunity was supported across party lines, because every large party owns a file. That is precisely the asymmetry. Privacy law in Canada is written by the only data controllers it exempts. The European Union moved in the opposite direction in the same period, bringing political messaging under a dedicated transparency-and-targeting regulation layered on top of its general privacy law.^[11] Canada now anchors the permissive end of the democratic spectrum.

### What a real regime would contain

The elements are not exotic; most appeared in the lapsed Bill C-65 or exist in provincial law: a voter's right to access and correct their record; consent or a defined lawful basis for appending commercial data; a prohibition on selling or maliciously disclosing voter data; breach notification; and independent audit — by the Privacy Commissioner or the Chief Electoral Officer, either of whom currently has none.^[12] The C-4 regime's authors noted it does not preclude stronger future legislation. The sunset clause the Senate proposed would have guaranteed Parliament revisited the question by 2029; its rejection means the question returns only if voters put it there.

#### Standing caveat

This note is a structural survey, not legal advice, and names no party as better or worse than another: the practices in § I are industry-standard across the major parties, and the statute in § II passed with all-party support save one. The illustrative record contains no real person's data. Statutory references current to 11 June 2026.

## § III · Sources and Notes

1. Bill C-4, *Making Life More Affordable for Canadians Act*, S.C. 2026, c. 2, 45th Parliament, 1st Session, Part 4 (amendments to the Canada Elections Act); Library of Parliament Legislative Summary 45-1-C4: the new regime is intended to be national, uniform, exclusive and complete, and excludes federal political parties from the application of provincial or territorial privacy laws. Royal assent 12 March 2026. Retroactive application to the year 2000 as reported in parliamentary study and press coverage (see notes 3 and 8).
2. On Part 4 as a response to the British Columbia litigation: S. Bannerman (McMaster University), public analysis, September 2025 — Part 4 explicitly states that provincial and territorial privacy laws do not apply to federal political parties, in apparent response to the BC ruling finding that they did.
3. Canada's National Observer, 13 March 2026: royal assent; Senate three-year sunset amendment rejected by the House; Green Party the sole party opposing the privacy provisions.
4. On the structure of Canadian voter files and data-driven campaigning generally: C. J. Bennett & R. M. Bayley, *Canadian Federal Political Parties and Personal Privacy Protection: A Comparative Analysis* (Office of the Privacy Commissioner of Canada, March 2012); S. Bannerman, J. Kalinina, E. Dubois & N. Goodman, “Privacy and Canadian Political Parties: The Effects of the Data-Driven Campaign on Elector Engagement,” *Canadian Journal of Political Science* (2022); and the Canadian political-data literature, 2018–2026; party privacy policies as published under the Canada Elections Act; vendor documentation for Canadian campaign CRM platforms and geodemographic segmentation products.
5. PIPEDA, S.C. 2000, c. 5, s. 4 (application limited to commercial activity); Office of the Privacy Commissioner of Canada findings and guidance on the non-application of PIPEDA to federal political parties, including the joint OPC–Elections Canada position, 2019–2021.
6. Bill C-76, *Elections Modernization Act*, S.C. 2018, c. 31 (privacy-policy publication requirement as a condition of party registration; no substantive standards, audit power, or individual rights).
7. BC Office of the Information and Privacy Commissioner, Order P22-02 (2022); *Liberal Party of Canada v. The Complainants*, 2024 BCSC 814 (PIPA capable of applying to federal parties operating in BC); appeal pending at the time of Bill C-4's introduction.
8. Library of Parliament Legislative Summary 45-1-C4, Part 4; Senate Standing Committee on Legal and Constitutional Affairs, Report No. 4 (45-1), February 2026.
9. Testimony of S. Perrault, Chief Electoral Officer, and C. Simard, Commissioner of Canada Elections, before the Senate committee, February 2026, as reported by The Globe and Mail (not consulted; provisions vague and difficult to oversee; bill does not enhance privacy protection). Senate LCJC Report No. 4: protections from former Bill C-65 — including prohibitions on selling or maliciously disclosing personal information — died on the Order Paper at the 2025 dissolution and were not incorporated into Part 4.
10. Canada's National Observer, 13 March 2026; Canadian Civil Liberties Association, open letters and legislative briefs on Bill C-4 Part 4, June 2025 – March 2026 (retroactive immunity; absence of access and correction rights).
11. Regulation (EU) 2024/900 on the transparency and targeting of political advertising, applicable from late 2025, layered on the GDPR's general regime.
12. Former Bill C-65, *Electoral Participation Act* (44th Parliament; died on the Order Paper, 2025): privacy elements as catalogued in Senate LCJC Report No. 4 (45-1). Privy Council Office witnesses before the same committee: Part 4 does not preclude further legislation specifying more comprehensive privacy standards.

## Series Index at Release, 11 June 2026

The documents the imprint had published when this note was released. The current archive is at [Papers](https://npsi.ca/papers/) and [Briefings](https://npsi.ca/briefings/).

WP-01

[The Bilateral Foundation](https://npsi.ca/wp1/) — A thirty-year Canada–Korea sovereign bond. *(published May 2026)*

WP-02

[A Canada–United States Energy and Compute Compact.](https://npsi.ca/wp2/) *(published May 2026)*

WP-03

[A Canada–Korea Pacific Defence-Industrial Corridor.](https://npsi.ca/wp3/) *(published May 2026)*

WP-04

[The Addition Paradox](https://npsi.ca/wp4/) — An energy thesis for Canada. *(published May 2026)*

WP-05

[Sovereign Compute North](https://npsi.ca/wp5/) — An energy-for-memory swap, signed under Canadian law. *(published 27 May 2026)*

TB-01

[The Verified Sky](https://npsi.ca/tb1/) — Sensing, certainty, and the law of automated airspace awareness. *(published June 2026)*

BN-01

The Voter File — The five-layer record and the statute that immunized it. *(this note)*

SB-01

[Zero Secrets](https://npsi.ca/sb1/) — Canada's data and AI sovereignty crisis. *(published June 2026)*

End of Briefing Note No. 1

Privacy law in Canada is written by the only data controllers it exempts.

— § II, The Asymmetry
