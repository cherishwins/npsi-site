---
title: "Running Silent"
subtitle: "What ambient signal mapping can and cannot find. A claim-by-claim technical assessment of “passive multi-domain over-the-horizon target fusion.”"
series: "Technical Briefings"
number: 2
identifier: "NPSI-20261014 (accession number; publication serial pending)"
version: "v1.0.1"
published: "2026-10-17"
status: published
author: "Jesse James"
publisher: "North Pacific Strategy Initiative"
canonical_url: "https://npsi.ca/tb2/"
pdf:
  - "https://npsi.ca/tb2/technical-briefing-print.pdf"
  - "https://npsi.ca/tb2/technical-briefing.pdf"
description: "What ambient signal mapping can and cannot find at sea: eighteen claims about passive over-the-horizon target fusion, graded against open physics."
license: "CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)"
cite_as: "James, J. (2026). Running Silent (NPSI Technical Briefing No. 2, NPSI-20261014, v1.0.1). North Pacific Strategy Initiative. https://npsi.ca/tb2/"
---

> Machine-readable full text of NPSI Technical Briefing No. 2, *Running Silent*, from the reading view at https://npsi.ca/tb2/. The reading view and the PDF are the editions of record; figures are given as their text descriptions. The text is licensed CC-BY-4.0: quote it, summarise it, translate it, share it and use it, including in AI systems and their answers, with attribution to the author and a link to https://npsi.ca/tb2/. The NPSI name and wordmark are not licensed. Register of every NPSI document: https://npsi.ca/registry.json · index for machine readers: https://npsi.ca/llms.txt

Technical Briefing No. 2 · v1.0.1 · Dated 14 October 2026, released and corrected 17 October · Unclassified — Open Source

# Running Silent

What ambient signal mapping can and cannot find. A claim-by-claim technical assessment of “passive multi-domain over-the-horizon target fusion.”

## Interest note.

This briefing assesses fusion software sold to defence customers, among it Palantir’s Gotham and its Gaia map application and the Maven Smart System. The editor works professionally as a systems architect in enterprise software, data systems and applied-intelligence platforms, and that interest is declared at [/disclosure/](https://npsi.ca/disclosure/). The briefing was researched and drafted with AI assistance (Claude); the author is responsible for every claim.

## Erratum, 17 October 2026 (v1.0.1).

Corrections from the source check, applied on the day of release. A hull is at most about a sixtieth of a VLF wavelength, not a thousandth, and the Rayleigh estimate is now given as a range, 75 to 115 dB. Seawater ends the VLF story within tens of metres rather than two, and a hull at 100 m sits nearly 490 dB down. Paolo and colleagues’ 21–30 per cent describes transport and energy vessel *activity*, not vessels. A preprint withdrawn by its author (SeaSpoofFinder, arXiv 2602.16257) is no longer cited. The Hensoldt quotation is restored to its source wording, and the 180-object figure is attributed to Diehl’s IRIS-T SLM integration rather than to a 2018 German Air Force demonstration. The Feinberg memo of 9 March 2026 directed Maven’s transition to a programme of record; it did not complete it. Gaia is quoted from the G-Cloud 14 definition without a phrase that belongs to another application, and that document is dated May 2024. An unconfirmed 2020 report of a strike on a moving target ship now sits beside the untested-chain judgment. Attributions are corrected for the Watts quotation, the skywave patent’s cited paper, the Asia Times magnetic-detection line, the fibre-sensing range and the IET paper’s year. Fig. 10 shows claim 12 on its own row, so it matches the four (d) grades on the cover. Two references to “requested” items, four sentences in the second person or the superlative, and one slogan-like line are restated. The sources now carry links. Both PDF editions were reissued from the corrected text; the first release is in the repository history.

- **Author:** Jesse James
- **Document ID:** `NPSI-20261014` — accession number, as printed on the release; second in this site’s Technical Briefing series; publication serial pending the editor’s ruling
- **Version:** `v1.0.1` · [change log](https://github.com/cherishwins/npsi-site/commits/main/tb2)
- **Series:** Technical Briefing — a companion line to the Working Papers, addressing the engineering substrate beneath the policy architecture
- **Issued:** Dated 14 October 2026; released 17 October 2026 · Victoria, British Columbia
- **Revised:** v1.0.1 · 17 October 2026 · errata from the source check, listed in the note above; sources linked; both PDF editions reissued
- **Canonical release:** This reading view, set from the author’s Markdown record. [technical-briefing.pdf](https://npsi.ca/tb2/technical-briefing.pdf) (23 pp., dark edition) and [technical-briefing-print.pdf](https://npsi.ca/tb2/technical-briefing-print.pdf) (23 pp., cream edition for print) carry the same corrected text, printed from the author’s press plate.
- **Status:** Unclassified · Open source. Every source is open and listed. Classified capability is neither claimed nor assessed.
- **Assistance:** Researched and drafted with AI assistance (Claude); the author is responsible for every claim. See [Disclosure](https://npsi.ca/disclosure/).
- **Cite as:** James, J. (2026). *Running Silent: What Ambient Signal Mapping Can and Cannot Find* (NPSI Technical Briefing No. 2, v1.0.1). https://npsi.ca/tb2/

18

claims graded against open-source physics and program evidence

4

claims that are physically or technically wrong as written

1.8 m

electromagnetic skin depth of seawater at 20 kHz, the number that ends the VLF story

## Bottom Line

### The direction is right. The physics is wrong.

A widely circulated AI-generated text claims that ambient radio, commercial transponder feeds and machine learning can be fused into a real-time global map of hidden submarines and carrier groups, with no decryption required. This briefing tested each assertion against open physics, peer-reviewed research and programme records.

**Finding.** Multi-sensor fusion is eroding concealment at sea. That much is true. But the three mechanisms the text relies on do not survive contact with the evidence. Submarines cannot be located by watching very low frequency (VLF) radio waves “warp” around their hulls; seawater extinguishes the field within tens of metres. Dark vessels cannot be found by subtracting declared traffic from a transponder feed; a ship that is not broadcasting is simply absent. And no published mechanism turns “micro-variance in background satellite signal strength” into a carrier track.

What actually works is narrower, more expensive and more active than the text implies: satellite radar matched against AIS, satellite geolocation of ships that still emit, seabed and towed acoustic arrays, skywave over-the-horizon radar cued to imaging satellites, and fusion software now used by more than a hundred thousand US personnel. None of it makes running silent obsolete. It makes running silent insufficient on its own.

#### How every claim was graded

(a) ESTABLISHED

Documented in open sources as fielded or routinely demonstrated.

(b) DEMONSTRATED

Shown in research or limited trials, not operational at scale.

(c) SPECULATIVE

No documented demonstration; possible in principle, unsupported in practice.

(d) WRONG

Contradicted by physics or by how the named systems actually work.

## Key Findings

### Eight judgments, with confidence stated

1. 01

   **The VLF submarine mechanism is wrong.** Seawater conducts. VLF fields fall by about 5 dB per metre of depth and a hull is at most about a sixtieth of a wavelength. Any scattered field sits hundreds of decibels below lightning noise. Submarines receive VLF; shore stations transmit it.

   HIGH
2. 02

   **Real non-acoustic submarine detection is short-range or experimental.** Magnetic anomaly detection works at hundreds of metres to low kilometres. Chinese magnetometer advances reported through the South China Morning Post are genuine laboratory and field-trial results, not wide-area search capabilities.

   MOD–HIGH
3. 03

   **Passive acoustics is the mature “passive” layer against submarines.** The US undersea surveillance system, SURTASS and TRAPS are real and funded. China’s “Underwater Great Wall” is partly deployed. Telecom cables now detect ships through distributed acoustic sensing in peer-reviewed trials.

   HIGH
4. 04

   **Dark-vessel analytics are mature, but the text’s logic is inverted.** Detection needs an independent sensor first. Warships are generally not required to broadcast AIS, and Russian AIS and GNSS spoofing is now routine enough that fourteen European states issued a joint warning in January 2026.

   HIGH
5. 05

   **Passive radar is real and range-limited.** Broadcast-illuminated systems track aircraft to a few hundred kilometres near transmitter-rich land. Starlink- and GNSS-illuminated passive radar reaches single-digit kilometres in the literature.

   HIGH
6. 06

   **The real over-the-horizon threat to carriers is active and dedicated.** Skywave radar cues coarsely at long range; imaging and electronic-intelligence satellites refine the fix. Western analysts still describe the full Chinese anti-ship missile chain as untested against a defended, manoeuvring carrier; a reported 2020 hit on a moving target ship remains unconfirmed.

   MOD–HIGH
7. 07

   **Fusion software is scaling fast; a real-time global “glass map” is not here.** The Maven Smart System ceiling is about $1.3 billion through 2029. It fuses existing intelligence feeds. Palantir’s “Gaia” is a map interface, not a detection engine.

   HIGH
8. 08

   **“Running silent is no longer a defense” is overstated.** Emission control plus dispersion and deception still impose large search costs. Both the US and its competitors keep investing in counter-surveillance, which is the behaviour of states that expect concealment to keep paying.

   MODERATE

## Scope and Method

### Two very different things share one phrase

“Over-the-horizon target fusion” names a genuine military capability and a largely fictional one. This briefing keeps them apart.

THE REAL ONE

Active radar plus satellites

High-frequency skywave radar and satellite cueing used to target ships beyond line of sight. Dedicated sensors, decades of engineering, known limits.

THE IMAGINED ONE

Ambient signals inverted by AI

Broadcast radio, satellite downlinks and commercial traffic behaviour supposedly revealing non-emitting assets anywhere on Earth. No sensor, no signal budget, no demonstration.

72–76%

of the world’s industrial fishing vessels are not publicly tracked, found by matching radar imagery to AIS

300 km

longest passive-radar air track claimed in a NATO trial, over land and coast, by the manufacturer

100,000+

US personnel on the Maven Smart System by September 2026, up from about 50,000 in January

#### Sources and their weight

Peer-reviewed literature (Nature, JASA, IEEE, IET, Sensors, arXiv), US government records (NRO releases, DARPA programme pages, Navy budget exhibits, Naval History and Heritage Command), Palantir’s own technical documentation, and established defence press (C4ISRNET, Defense News, Breaking Defense, DefenseScoop, The War Zone, SpaceNews). Chinese claims are attributed to their reporting outlet, usually the South China Morning Post summarising Chinese-language journals, and are treated as claims.

**Three honesty rules governed the write-up.** Classified capability is neither claimed nor assessed. Absence of open evidence is not evidence of absence, and it is also not evidence for the text. Where an item could not be traced to a primary document in this research cycle, the briefing says so rather than quoting a number it cannot stand behind.

The original text opens by congratulating its reader for having “independently architected” a classified programme. That flattery is set aside. The technical substance is judged on its merits, sentence by sentence, in the verification ledger at the end of this document.

## Chapter 1 · VLF physics and real non-acoustic detection

### Why seawater ends the VLF story

The claim: passive sensors watch VLF waves “warp or deflect around a massive metallic object under the water” and locate a submarine that never transmits. Grade (d), wrong, high confidence.

**Who transmits.** VLF, 3 to 30 kHz, is a one-way broadcast from very large shore stations to submarines, which receive it near the surface through towed wire or buoy antennas. The premise that submarines “use VLF to communicate” is true only in the receive direction.

**Wavelength against hull.** At the 10 to 30 kHz used for submarine broadcasts, wavelengths run 10 to 30 km. A Virginia-class hull is about 115 m long; an Ohio-class about 170 m. The hull is between about one sixtieth and one two-hundred-and-sixtieth of a wavelength, deep in the Rayleigh regime, where the scattered field scales as the cube of the electrical size, (ka)³: some 75 to 115 dB below the incident field across those hulls and frequencies, even with the hull floating in air.

Fig. 01

The ocean is a conducting mirror to VLF

Attenuation of a 20 kHz field with depth in seawater (4 S/m), decibels below the surface field

[Figure: Bar chart: a 20 kHz field in seawater loses about 5 dB at 1 m depth, 25 dB at 5 m, 49 dB at 10 m, 98 dB at 20 m, 245 dB at 50 m and 490 dB at 100 m. Skin depth about 1.8 m; loss about 4.9 dB per metre, each way.]

Computed: δ = 1/√(πfμσ) with f = 20 kHz, σ = 4 S/m. A hull at 100 m sits about 55 skin depths down.

**Skin depth.** Seawater conducts at about 4 S/m. The skin depth at 20 kHz is about 1.8 m, so the field loses about 4.9 dB per metre. A submarine at 100 m sits nearly 490 dB below the surface field, and any scattered energy suffers the same loss again coming back up. To VLF, the sea surface is a mirror.

**Noise floor.** VLF ambient noise is dominated by global lightning. The hypothesised signal sits hundreds of decibels below it, and no machine-learning integration recovers a signal that is absent at the sensor. VLF methods do locate conductive bodies, but on land, to tens of metres, with the sensor almost on top of the target.

### What non-acoustic detection actually looks like

| Method | Physical basis | Realistic status | Grade |
|---|---|---|---|
| Magnetic anomaly detection (MAD) | Hull’s induced and permanent magnetic field disturbing Earth’s field | Fielded on P-8, P-3 and helicopters; hundreds of metres to 1–2 km; localisation, not search | (a) |
| Underwater electric potential, ELF electromagnetics | Corrosion and cathodic-protection currents around the hull | Known signature, managed by degaussing; short-range, mostly mines and barriers | (a)/(b) |
| Radar imaging of wakes and internal waves | Surface expression of a moving submerged body | Research-grade for shallow, fast bodies; deep, slow submarines largely immune | (b)/(c) |
| Thermal scar, bioluminescence, chemical traces | Wake mixing and disturbance | Long studied, repeatedly hyped; no open evidence of wide-area use | (c) |
| Quantum and atomic magnetometers | Higher-sensitivity MAD | Real sensor progress; range still bounded by inverse-cube field decay | (b) |

#### Chinese claims, read against their own papers: headlines (c), papers (b)

MAGNETIC WAKE · NPU, Dec 2024

Wang Honglei’s team modelled the weak field from seawater ions moving through Earth’s field in a Kelvin wake. Real physics, model-only study. Asia Times, citing Sithiravel and colleagues (IEEE, 2020): MAD is “more suitable for short-range confirmation rather than long-range detection.” Phenomenon (b); capability (c). [Source: Journal of Harbin Engineering University, as reported by SCMP, 7 Feb 2025; Asia Times, Feb 2025]

DRONE-MOUNTED CPT MAGNETOMETER · Apr 2025

Wang Xuefeng’s group reports accuracy improving from 2.517 nT raw to 0.849 nT corrected, sensor on a 20 m tether beneath a rotor drone. A credible step toward cheaper, distributed MAD, not a range breakthrough. Grade (b). [Source: Chinese Journal of Scientific Instrument, as reported by SCMP and The Quantum Insider, Apr 2025]

HANDHELD MAGNETOMETER · USTC, Sep 2026

Peng Xinhua’s pencil-sized, 5 W device tracked a subway train beneath a city street. Miniaturisation, not ocean-scale detection. Grade (b). [Source: Acta Physica Sinica, 14 Sep 2026, as reported by SCMP, 25 Sep 2026]

## Chapter 2 · Passive acoustic networks

### The layer that is real, and the one the text left out

Seabed and towed hydrophone arrays are the mature passive sensor. Distributed acoustic sensing on telecom cables is the genuinely new one, and it does not appear in the original text at all.

**United States and allies.** The Cold War SOSUS seabed hydrophone system, now the Integrated Undersea Surveillance System, is the long-standing model of the “passive sea-floor chokepoint” network. SURTASS ships tow long passive and low-frequency active arrays. TRAPS, the Transformational Reliable Acoustic Path System, is a fixed passive node that exploits the deep-water reliable acoustic path from the seafloor. It began in DARPA’s Distributed Agile Submarine Hunting programme, with SAIC prototypes around 2013 and Leidos development from 2014. [Source: UPI, 28 Aug 2013; Military & Aerospace Electronics]

In June 2019 NAVWAR awarded Leidos a $72.8M sole-source follow-on for “up to forty-five” TRAPS units. The Department of Defense announcement said TRAPS “complements fixed surveillance systems and the surveillance towed array sensor system.” Navy budget exhibits show Congressional adds of $33.766M (FY2019) and $15M (FY2020) for additional units. [Source: NAVWAR solicitation N0003919R0022; Navy RDT&E budget exhibit, Integrated Surveillance System]

**DARPA Ocean of Things.** DARPA describes “thousands of low-cost, environmentally friendly, intelligent floats,” more than 3,000 deployed in Phase 2, with analytics that “automatically detect, track, and identify nearby vessels.” The 2018 solicitation set a ceiling of $500 per float in lots of 50,000, and the programme manager spoke of 50,000 floats covering a million square kilometres. Treat the latter as a planning figure, not a deployed one. Grade (b). [Source: DARPA programme page; BAA HR0011-18-S-0013]

**China.** China State Shipbuilding Corporation publicly proposed an “Underwater Great Wall” of submarine detectors in 2015–16. In January 2018 the Chinese Academy of Sciences disclosed two deep-sea acoustic sensors between Guam and the South China Sea, operating since 2016. Existence (a); effective coverage and integration with fleet operations (c), not knowable from open sources. [Source: SCMP, as reported by The War Zone, Jan 2018; National Maritime Foundation]

### Cables that listen

A 2026 study in the Journal of the Acoustical Society of America used a trenched telecom cable in Norway’s Trondheimsfjord to detect and localise ships automatically, including “an unidentified ship without active AIS recording.” Chinese researchers connected distributed acoustic sensing to a 69 km optoelectronic cable off Hainan for AI-enabled vessel detection, citing “potential for detecting dark ships.” Real-time sensing has been demonstrated on 148 to 171 km of fibre without inline amplification. [Source: JASA 159(5), 2026; ResearchGate 396960937; Waagaard et al., OSA Continuum 4(2), 2021, via arXiv 2509.11614]

Grade (b), moving toward (a) in coastal and littoral zones. Range from the cable is kilometres, and coverage follows cable routes, not the open ocean. The text’s “covert spy vessel dragging a sonar array” is broadly right about acoustics: surface survey and intelligence ships are mechanically noisy, run navigation radar and are large radar targets. Its “localised power signature” has no defined technical meaning.

Fig. 02

Detection reach by method, on a log scale

Order-of-magnitude range at which each sensor class plausibly detects its target, from open literature and manufacturer claims

[Figure: Log-scale range chart from 100 m to 10,000 km: VLF hull scatter has no signal at any range; magnetic anomaly detection reaches about 100 m to 2 km; cable acoustic sensing kilometres from the cable; Starlink and GNSS passive radar about 1 to 15 km; seabed arrays and TRAPS about 1 to 150 km; broadcast passive radar for aircraft about 10 to 300 km; skywave over-the-horizon radar about 1,000 to 3,000 km; imaging and ELINT satellites global by revisit.]

Bars show typical reach, not maximum stated. Satellite row is global by revisit, not by range. Sources: Ch. 1–5 of this briefing.

## Chapter 3 · AIS, ADS-B and dark-vessel analytics

### A ship that was never there cannot be subtracted

AIS and ADS-B are cooperative systems. They contain only what transmitters choose to broadcast. Removing declared traffic from a transponder feed leaves an empty set, not a map of ghosts. Grade as written: (d). Corrected version: (a).

Fig. 03

Where dark vessels actually come from

The text’s logic against the method that produces results

[Figure: Two equations. As written: AIS feed minus declared ships equals nothing, because non-broadcasters are absent. As practised: independent SAR, RF and optical detections minus matched AIS tracks equals dark vessels, 72 to 76 per cent of the industrial fishing fleet.]

Source: Paolo et al., Nature 625, Jan 2024 (Global Fishing Watch, Duke, UCSB, UW–Madison, SkyTruth).

**Radar matched to AIS.** Paolo and colleagues processed about two petabytes of Sentinel-1 imagery from 2017 to 2021 with deep learning and found that “72–76% of the world’s industrial fishing vessels are not publicly tracked,” along with 21–30% of transport and energy vessel activity. It is a peer-reviewed, global-scale public demonstration. It is coastal-weighted, and revisit latency is days, not seconds. Grade (a). [Source: Nature 625, 2024; PMC10764273]

**Radio geolocation from orbit.** HawkEye 360 geolocates “marine radar, VHF radio, satellite communications, and emergency beacons” and flags geolocations with no matching AIS as “DarkRF.” Published cases include the tanker Romina going dark after Suez in 2020 and a cargo ship’s week-long AIS gap off Syria in 2021, resolved through VHF to a call at Tartus. Unseenlabs offers comparable service. Grade (a). The limit is structural: a ship with radar and radios off defeats radio geolocation entirely. Only imagery, or acoustic sensing near a cable, catches it. [Source: HawkEye 360, Apr 2022; Via Satellite, Jan 2021]

### The feed is already poisoned

Any fusion architecture that trusts AIS inherits whatever deception is in it, and in 2026 that is a lot.

On 26 January 2026 Belgium, Denmark, Estonia, Finland, France, Germany, Latvia, Lithuania, the Netherlands, Norway, Poland, Sweden, the United Kingdom and Iceland published an open letter stating that “these disturbances, originating from the Russian Federation, degrade the safety of international shipping,” and warning that AIS falsification “severely hampers rescue operations.” [Source: joint open letter of fourteen European states, 26 Jan 2026]

The Royal Institute of Navigation’s report of 23 January 2026, drawing on more than 100 sector experts and 300 masters, records that “in 2025, at least two collisions and groundings were reported in mainstream media linked to GNSS interference in regions such as the Baltics, Straits of Hormuz and the Red Sea.” Windward reported that “more than 1,650 vessels experienced GPS and AIS interference across the Middle East Gulf on March 7 [2026], up 55% from a week ago.” [Source: RIN, Impacts of GNSS Interference on Maritime Safety, 23 Jan 2026; Windward, Mar 2026]

#### Aviation

Military transports, tankers and surveillance aircraft often fly with Mode S and ADS-B on in peacetime for airspace deconfliction. Unfiltered aggregators such as ADS-B Exchange, and multilateration of Mode S returns, let open-source communities follow them. Combat and stealth aircraft on operations turn transponders off. The Hensoldt “F-35 tracking” episode of 2018 involved aircraft reportedly flying with radar reflectors and ADS-B on.

(a) ESTABLISHED

Open-source tracking of cooperative military aircraft through their own transponders.

(d) WRONG

Finding non-cooperative stealth aircraft by subtracting declared ADS-B traffic from the feed.

## Chapter 4 · Passive radar and signals of opportunity

### Borrowed light reaches kilometres, not oceans

Passive coherent location correlates a broadcast transmitter’s direct signal against its echoes to get bistatic range and Doppler. It is mature for aircraft near transmitter-rich land, and small-scale for everything else.

| System or study | Illuminator | Reported performance | Grade |
|---|---|---|---|
| Hensoldt TwInvis | FM, DAB, DVB-T | “The achieved ranges over the Baltic Sea coast were up to 300km” in a NATO STO campaign; “more than 180 objects up to a range of 250 km” in its IRIS-T SLM integration, according to Diehl. Manufacturer and partner figures. [Hensoldt, Oct 2019; Defense News, Aug 2023] | (a) |
| Hensoldt F-35 claim, ILA 2018 | FM, DVB | Two F-35s tracked for 150 km; aircraft reportedly carried reflectors and ADS-B. Unverified. [C4ISRNET, 30 Sep 2019; Association of Old Crows] | (b) |
| ERA VERA-NG, Czechia | none: emitter location | To 400 km, 500 tracks, 50 MHz–18 GHz. Requires the target to emit. Irrelevant to a silent target. [ERA data sheet] | (a) |
| China DWL002, YLC-20 | none: emitter location | 400 km against fighters, 600 km against AEW&C, per CETC; CETC staff conceded detection depends on the stealth fighter’s own radar or jammer being active. [CASI/BluePath, Mar 2025] | (a)/(c) |
| China YLC-29 | FM broadcast | Marketed as anti-stealth; no range published. [Global Times, 2017] | (b) |
| Silentium Defence, Australia | FM | Small drones at 3–7 km, aircraft to 20 km; MAVERICK units delivered to Lockheed Martin Australia for AIR6500, 2024. [National Defense, 2023; Lockheed Martin Australia] | (a)/(b) |
| Starlink passive radar, Birmingham 2019 | Starlink Ku-band | About 10 km for a 10 m² air target with coherent integration; 2 km worst case. Theoretical. [EasyChair preprint 900] | (b) |
| LEO broadband passive radar | Starlink, OneWeb | 1 m² target to about 1.9 km at Pd 0.9, Pfa 10⁻⁴ with a 39 dBi antenna. [IET Radar, Sonar & Navigation, 2024] | (b) |
| GNSS passive radar for ships | GNSS | 27 dBm² ship detected to about 5 km with 40 s dwell. [Sensors 20(3), 2020] | (b) |
| Chinese Starlink forward-scatter test | Starlink | Detected a DJI Phantom 4 drone off Guangdong; no range reported. [SCMP, Sep 2024] | (b) |

### The “micro-variance” mechanism does not exist in the literature

A carrier does reflect satellite signals; that is the basis of GNSS- and Starlink-illuminated passive radar. Exploiting it requires a coherent bistatic receiver near the target, with ranges of a few kilometres, because satellite signals at the surface are weak and high signal-to-noise comes only with narrow beams or long integration. No published study shows a carrier group modulating received satellite signal strength over an ocean block in a way detectable by distributed receivers. Grade (c) bordering on (d), moderate to high confidence. Over the open Pacific there are no FM or television towers to borrow.

GNSS REFLECTOMETRY

Built for wind, not warships

TechDemoSat-1 (July 2014) and NASA’s eight-satellite CYGNSS constellation (2016) measure ocean winds, sea state and soil moisture. Ship detection from them is research-grade, limited to large targets in specific geometries, with kilometre-scale footprints. Grade (b). [Source: Geophysical Research Letters, 2015; TDS-1 backscatter studies]

WI-FI SENSING

The near-field analogue, and its limit

Channel-state sensing detects people through walls at metres. It illustrates the principle, that targets perturb ambient radio, and the constraint: the target must be close to both transmitter and receiver. Grade (a) at room scale; irrelevant at ocean scale.

**Reading the table.** Every operational row is an air-surveillance system near a coast or a land mass with broadcast transmitters, or an emitter-location system that needs the target to talk. The space-illuminated rows are peer-reviewed and honest about their numbers, and those numbers are kilometres. A hostile analyst should ask of any passive-radar claim: what illuminator, what bistatic geometry, what integration time, what false-alarm rate. The original text answers none of the four.

## Chapter 5 · Skywave radar and space-based persistence

### What over-the-horizon targeting really is

Skywave radar bounces high-frequency energy off the ionosphere to illuminate targets 1,000 to 3,000 km away. It is active, it is coarse, and it is the real first link in the chain the text imagines.

Australia’s JORN, the US Navy’s AN/FPS-71 ROTHR, Russia’s Konteyner and Chinese systems all work this way. Ship detection is far harder than aircraft detection: ships move slowly, and their echoes sit inside powerful sea clutter in Doppler. A US patent citing Frazer, Heitmann and Abramovich (2014) notes that skywave ship detection “is significantly more challenging than the equivalent task for aircraft.” Resolution cells run from kilometres to tens of kilometres, and ionospheric registration error dominates position uncertainty. Skywave radar can say a large surface group is roughly there. It cannot target it alone. Grade (a). [Source: US Patent 11,953,580; Naval Applications of HF OTH Radar, ResearchGate]

Fig. 04

The real anti-ship kill chain, and where it is untested

Open-source description of the Chinese DF-21D / DF-26 targeting sequence

[Figure: Kill-chain diagram: skywave over-the-horizon radar gives a coarse cue at 1,000 to 3,000 km; Yaogan ELINT and SAR satellites refine the fix; aircraft and UAVs confirm identity and position; DF-21D (about 1,500 km) or DF-26 launch; the terminal seeker must find a moving ship. Each link can be broken; no open source documents an end-to-end test against a defended, manoeuvring carrier.]

Source: Air Force Magazine, Dec 2013 (Barry Watts); DF-21 and DF-26 open literature; China-Arms, Jun 2026.

Barry Watts of CSBA judged in 2013, as quoted in Air Force Magazine, that “the Chinese have yet to conduct an end-to-end test of it against a moving target at sea,” and no open source has since documented one against a defended carrier. A reported August 2020 strike on a moving target ship in the South China Sea, attributed by the South China Morning Post to a source close to the PLA, has not been confirmed. This chain is the real-world version of “over-the-horizon target fusion.” It is built from dedicated active and imaging sensors. [Source: Air Force Magazine (Otto Kreisher), Dec 2013, quoting Watts, The Evolution of Precision Strike, CSBA, 2013; SCMP, 14 Nov 2020]

### Persistence from orbit is what actually erodes concealment

14

launches of the NRO’s multi-phenomenology proliferated architecture by NROL-179, 19 June 2026

hundreds

of NRO satellites on orbit, by the agency’s own statement, with launches continuing through 2029

21

Tranche 1 Transport Layer satellites deployed by Northrop Grumman for the SDA on 10 October 2026

**National Reconnaissance Office.** NROL-179 was “the fourteenth overall launch of the NRO’s multi-phenomenology proliferated architecture.” The NRO states it has “hundreds of NRO satellites on orbit,” that the architecture includes electro-optical, radar and relay satellites with support to ground moving target indication, and that it is “exceeding expectations.” Existence (a); performance (c), classified. [Source: NRO Release 5-26; NRO proliferated architecture press kit, Jan 2026; NRO news, Space Symposium, Apr 2026; Spaceflight Now, May 2026]

Fig. 05

Fourteen proliferated-architecture launches in twenty-five months

NRO proliferated architecture missions by calendar year, May 2024 to 19 June 2026

[Figure: Bar chart of NRO proliferated-architecture launches: six in 2024 from May, five in 2025, three in 2026 to 19 June, NROL-179 the fourteenth overall.]

Sources: NRO Release 5-26 (NROL-179, “fourteenth overall launch”); NRO mission releases NROL-146 through NROL-48, 2024–25; ExecutiveGov, NROL-172.

**Space Development Agency.** The Proliferated Warfighter Space Architecture’s Tracking Layer is aimed at missiles, not ships. Golden Dome and Space Force commercial-imagery budget lines were not traced to primary documents and are not quoted. [Source: Northrop Grumman, 10 Oct 2026]

**Interpretation.** Revisit over priority areas is moving from hours toward minutes. This, not ambient physics, shortens the time a surface fleet can stay unlocated: wide-area radar, optical and electronic-intelligence imaging, with fusion behind it. China’s Yaogan constellation plays the same role on the other side.

## Chapter 6 · Pattern of life, anomaly detection and fusion software

### Palantir Gaia is a map, not a sensor

The text names “Palantir Gaia” as the platform built to execute ambient signal mapping. Gaia exists. It is the geospatial command-and-control application inside Palantir Gotham. Grade for the text’s description: (d).

Palantir’s own documentation describes Gaia as Gotham’s map application: users load “Gaia maps,” add Foundry ontology data and create objects by drawing on the map. Its UK G-Cloud 14 service definition calls Gaia “a collaborative geospatial command and control application” that integrates data from across Gotham into a map-based picture. It organises fused data; it does not detect submarines. Palantir is, accurately, a central fusion vendor to the US military. [Source: Palantir Foundry and Gotham documentation; UK Digital Marketplace G-Cloud 14 service definition, May 2024]

Fig. 06

Fusion at scale: Maven Smart System, 2024 to 2026

Contract ceiling in US dollars and reported active users

[Figure: Bar chart: Maven Smart System contract ceiling of $480 million in May 2024, raised to $1.3 billion in May 2025 through 2029; active users of more than 20,000 in May 2025, about 50,000 in January 2026 and more than 100,000 in September 2026.]

Sources: SpaceNews, May 2025; Breaking Defense, May 2025 (Vice Adm. Frank Whitworth); DefenseScoop, 15 Apr 2026 and 22 Sep 2026 (James Mazol at DefenseTalks).

James Mazol, deputy under secretary of defense for research and engineering, at DefenseTalks on 22 September 2026: “In January of this year, we had about 50,000 people using Maven. Then [Operation] Epic Fury kicks off, and now we’re up to over 100,000.” A memo of 9 March 2026 from Deputy Secretary of Defense Steve Feinberg directed that Maven become a programme of record by the end of the fiscal year, with its administration moving from NGA to the Chief Digital and AI Office; NATO bought its own instance in March 2025. Fusion at scale is (a). It ingests radar, optical, signals and video detections. It does not replace them. [Source: DefenseScoop, 22 Sep 2026; DefenseScoop, 15 Apr 2026]

### Three reasons the carrier inference fails

The text’s trigger: three merchants altering course by two degrees without a weather reason, plus a satellite-signal “micro-variance,” means a carrier group under emission control. Grade (c), high confidence.

1 · NO CAUSAL LINK

Merchant ships do not know where a silent carrier is and have no reason to deviate for it. Exercise areas are visible through their declared NAVAREA closures, not through inference.

2 · BASE RATES

Thousands of ships make small course changes daily for weather routing, traffic separation and commercial instruction. Even a 99%-specific detector flags many false carriers for every true one.

3 · ADVERSARIAL DATA

AIS is spoofed at state scale (Chapter 3). The “signal variance” input does not exist (Chapter 4). A model trained on both learns the deception and the noise.

Fig. 07

The base-rate problem, drawn to scale

A detector with 99% specificity scanning 5,000 ships in one ocean region, one true carrier group present

[Figure: One bronze mark for the single true carrier group beside fifty teal marks for false alarms: a 99 per cent specific detector scanning 5,000 ships flags 50 ordinary merchants on every pass.]

Illustrative arithmetic: 1% of 5,000 non-carrier ships = 50 false alarms per sweep. Sensitivity assumed perfect; a real detector does worse.

Anomaly detection is mature for cooperative traffic: AIS gaps, loitering, rendezvous, spoofing jumps. Anduril Lattice, Project Linchpin, CJADC2, Project Overmatch and DARPA’s Mosaic Warfare are real programmes for networking sensors to shooters; their budget lines were not traced to primary documents, so none are quoted.

**Where the “glass map” actually stands.** A near-real-time map of cooperative or emitting traffic, with periodic radar checks of priority areas, is roughly today’s reality. A real-time global map of non-emitting assets is a decade and several sensor generations away, if achievable at all.

## Chapter 7 · Emission control and counter-detection

### How long a carrier stays hidden, on the record

Emission control is not invisibility. A carrier is a 330 m steel ship visible to radar and optical satellites in clear weather. What EMCON, dispersion and deception degrade is identification and targeting-quality tracking, which is what a long-range missile needs.

Fig. 08

Measured concealment in exercises and trials

Time a carrier force remained unlocated or survived, as recorded in official and participant accounts

[Figure: Bar chart of time a carrier force stayed unlocated or survived: Haystack trials, under 2 hours before and 8 to 15 hours with emission control and dispersion; NORPAC 1982 Midway group, 4 days under strict EMCON by a participant account; UPTIDE series, about 5.5 days on average against cruise-missile submarines.]

Sources: Naval War College Review, 2011, “Hiding in Plain Sight”; NavWeaps, “How to Hide a Task Force”; Naval History and Heritage Command, Enterprise (CVAN-65) 1981–85.

**NORPAC 1982.** The Navy’s official history records that Enterprise “proved the subject of extensive Soviet air, surface, and subsurface surveillance,” including “unprecedented use of Backfire bombers.” A participant’s account says the Midway group, under strict EMCON and dispersion, flew mirror-image strikes for four days without detection while Soviet regiments raided the openly operating Enterprise. The participant account is not independently confirmed in detail. [Source: NHHC, Enterprise VIII; NavWeaps]

**Earlier trials.** The Haystack experiments raised simulated carrier survival in a nuclear exchange from under two hours to eight to fifteen hours, and the UPTIDE series averaged about five and a half days against cruise-missile submarines. Diesel-electric boats have repeatedly penetrated carrier screens in exercises; the often-cited 2005 Gotland encounter with Ronald Reagan was not traced to a primary source here. [Source: Naval War College Review, 2011]

“Running silent is no longer a defense” is therefore (c): overstated, moderate confidence. The defensible statement is that running silent alone is increasingly insufficient against a peer with proliferated space surveillance.

## Chapter 8 · Cognitive electronic warfare and decoys

### Phantom fleets are a programme, not a thought experiment

The text closes by offering to explore “cognitive EW generating realistic electronic background noise” against passive mapping. Against the text’s fictional sensors the question is moot. Against real passive sensing it is an active research line. Grade (b).

DARPA BLADE AND ARC

Where cognitive EW began

BLADE (from 2010, against communications) and ARC (from 2012, against adaptive radars) sense an unknown emitter, learn its behaviour and synthesise countermeasures in real time. BLADE flew with Lockheed Martin and Raytheon; ARC performers included BAE Systems, Leidos and Exelis. DARPA’s 2016 testimony cited transitions to the F-18, F-35, Next Generation Jammer and the Army’s multi-function EW programme. Grade (a). [Source: DARPA SASC testimony, 1 Apr 2016; Defense News, Aug 2016]

NAVY NEMESIS

Netted emulation against many sensors at once

First visible in FY2014 budget documents as a “System of Systems able to coordinate distributed EW resources against many adversary surveillance and targeting sensors simultaneously,” and reported as a means of projecting phantom fleets across radar, electronic-support and acoustic sensors. Long-endurance decoys and Nulka’s combat use are the visible pieces. Programme (a); full capability (c), classified. [Source: The War Zone; Navy FY2014 budget exhibits]

Chinese doctrine, described in Western analysis as “system destruction warfare,” treats sensor networks and kill chains as the primary target, with counter-space as a central tool. Primary PLA texts were not obtained in this cycle; this summary reflects standard Western analysis, grade (b), moderate confidence. The Russian spoofing campaign in Chapter 3 is a crude state-level example of synthetic signatures at scale.

**The inference that matters.** Both the United States and its competitors keep spending on deception, decoys and counter-surveillance. A decoy programme is worth funding only against sensors that can be fooled. The investment pattern is itself evidence that concealment still pays.

## Chapter 9 · Assessment

### Each layer, sorted into what is mature and what is fiction

Fig. 09

The maturity matrix

The text’s three layers against the open record

[Figure: Matrix of the text's three layers. Layer 1, passive RF and acoustic: mature components are seabed and towed arrays, cable sensing, radio geolocation of emitters and broadcast passive radar for aircraft; fictional components are VLF hull-scattering detection and a localised power signature. Layer 2, AIS and ADS-B: mature is radar, RF and optical detections matched against AIS and open-source tracking of cooperative aircraft; fictional is subtracting AIS to find ghosts and finding stealth aircraft by ADS-B subtraction. Layer 3, machine-learning pattern of life: mature is cooperative-traffic anomaly detection and fusion platforms at 100,000-plus users; fictional is carrier inference from satellite micro-variance and two-degree deviations.]

Teal: established or demonstrated in open sources. Bronze outline: no documented mechanism, or contradicted by physics.

#### The limits that bind every layer

Revisit and latency: hours to days for radar imagery over most of the ocean. Coverage: acoustic networks follow chokepoints and cable routes, not the open sea. False alarms: base rates punish any anomaly detector working on the whole merchant fleet. Adversarial contamination: spoofing and decoys are already in the data. And seawater, which blocks every electromagnetic method beyond tens of metres.

#### Figures this briefing stands behind

Maven Smart System ceiling about $1.3B through 2029. TRAPS follow-on $72.8M (2019) plus Congressional adds of $33.766M (FY2019) and $15M (FY2020). Comprehensive FY2025 to FY2027 lines for the other programmes were not verified and are not asserted.

## Verification Ledger

### Every sentence, graded

1. 01

   **A capability called “Passive Multi-Domain OTH Target Fusion,” “Ambient Signal Mapping” or “Passive Global Surveillance.”** Not a recognised programme or doctrinal term. OTH targeting is real and active-radar based.

   (c)
2. 02

   **Physics, metadata and ML can render a real-time global map of hidden assets.** Fusion is real; global real-time coverage of non-emitters is undemonstrated. Maven, NRO; Paolo et al. latency.

   (c)
3. 03

   **Submarines use VLF to communicate while submerged.** They receive shore-transmitted VLF near the surface; they do not transmit it. Qualified.

   (a)
4. 04

   **Passive sensors map a submarine via VLF “warping” around its hull.** Skin depth about 1.8 m at 20 kHz; hull far smaller than wavelength; scattered field far below lightning noise. Chapter 1.

   (d)
5. 05

   **AI locates the submarine from “environmental displacement of the background wave.”** No signal reaches the sensor; machine learning cannot recover absent information.

   (d)
6. 06

   **A spy vessel towing an array cannot hide its engine acoustics.** Surface ships are noisy; detected by arrays and cable DAS. IUSS; JASA 2026.

   (a)
7. 07

   **Nor its “localised power signature.”** Undefined term; no documented sensor.

   (c)
8. 08

   **Sea-floor passive sonar at chokepoints tracks these deviations.** SOSUS/IUSS, TRAPS, Chinese seabed sensors. Leidos/NAVWAR 2019; The War Zone 2018.

   (a)
9. 09

   **The system pulls live global AIS and ADS-B.** Commercial feeds are widely available. Spire, HawkEye 360, ADS-B Exchange.

   (a)
10. 10

    **Filtering out declared traffic leaves “ghost signatures.”** Non-broadcasters are absent from AIS; detection needs radar, RF or optical first. Paolo et al., Nature 2024.

    (d)
11. 11

    **Corrected: radar and RF detections unmatched to AIS reveal dark vessels.** 72–76% of industrial fishing vessels not publicly tracked. Paolo et al. 2024; HawkEye 360 DarkRF.

    (a)
12. 12

    **Micro-variance in background satellite signal strength over a region reveals a hidden group.** No documented mechanism; satellite-illuminated passive radar reaches kilometres. IET RSN 2023; Birmingham 2019.

    (c)/(d)
13. 13

    **Merchants deviating 2° without a weather reason signal an EMCON carrier.** No causal mechanism; base-rate false alarms; spoofed AIS. RIN; fourteen-state letter; Chapter 6.

    (c)
14. 14

    **AI infers the carrier group and renders a high-probability estimate.** Real carrier targeting uses OTH radar plus satellites and is still judged untested at sea. Air Force Magazine 2013.

    (c)
15. 15

    **Palantir Gaia is built to execute this.** Gaia is Gotham’s geospatial command-and-control map; it displays data, it does not sense. Palantir docs; UK G-Cloud 14.

    (d)
16. 16

    **Western SIGINT clouds are built to execute this.** Fusion clouds exist (Maven); no evidence of the described mechanisms. DefenseScoop 2025–26.

    (c)
17. 17

    **“Running silent is no longer a defense.”** Overstated; EMCON still raises search costs; both sides fund deception. Naval War College Review 2011; NHHC; NEMESIS.

    (c)
18. 18

    **Cognitive EW generating realistic background noise is deployed against passive mapping.** Cognitive EW and multi-sensor deception are real; framing against fictional sensors is moot. DARPA BLADE/ARC; NEMESIS.

    (b)

Fig. 10

Where the eighteen claims land

Count of claims by evidence grade

[Figure: Bar chart of the eighteen claims by grade: five established, one demonstrated, seven speculative, five wrong including one graded (c)/(d).]

Claim 12 is graded (c)/(d) and shown on its own row. The five established claims include one qualified (03) and the briefing’s corrected restatement of claim 10 (11).

## Conclusions and Implications

### Four judgments and three things to do about them

1. KJ-1

   **The text’s three most specific mechanisms are wrong or unsupported.** VLF hull scattering, AIS subtraction and satellite-signal micro-variance. Its general thesis, that fusion is eroding concealment, is directionally correct.

   HIGH
2. KJ-2

   **Surface-fleet concealment is being eroded by proliferated space imaging and electronic intelligence, commercial radio geolocation, and fusion software at scale.** Not by passive “ambient” physics.

   HIGH
3. KJ-3

   **Submarines remain far harder to find than surface ships.** The credible threats are expanding acoustic networks in chokepoints and littoral bastions, plus incremental magnetic-detection gains. Regional and short-range, not global.

   MODERATE
4. KJ-4

   **Deception and emission control retain significant value.** They matter most against long-range kill chains that need targeting-quality tracks rather than mere detection.

   MODERATE

FOR ANALYSTS

Demand a stated signal, a signal-to-noise ratio at the sensor, a range and a false-alarm rate. The VLF claim fails the first test. AI cannot create a signal that physics removes before it reaches the sensor.

FOR NAVAL PLANNERS

Assume persistent surface detection in priority theatres within this decade. Invest in identification and targeting denial: decoys, signature emulation, dispersion, electronic attack on radar and space sensors. Not in invisibility.

FOR POLICY

AIS and GNSS integrity is now a security problem. The European response to Russian spoofing shows that cooperative maritime data cannot be treated as ground truth in any fusion architecture.

#### Caveats

Classified capability (undersea surveillance performance, NRO sensor specifics, Chinese seabed coverage) cannot be assessed from open sources; this briefing grades only what is publicly evidenced. Several items were not traced to primary documents in this cycle: FY2025 to FY2027 budget lines for Overmatch, Linchpin, Golden Dome and commercial imagery; Japanese, British and Norwegian arrays; the 2005 Gotland encounter; primary PLA doctrinal texts. Passive-radar figures are mostly manufacturer or partner claims. Chinese research is often reachable only through SCMP summaries, whose headlines overstate the papers beneath them.

## Sources

### Open sources consulted

Grouped by chapter. Chained citations are declared as such in the text.

CH. 1 · PHYSICS AND MAGNETICS

[SCMP, “China can detect US Seawolf-class submarine with magnetic wake tracking,” 7 Feb 2025](https://www.scmp.com/news/china/science/article/3297575/china-can-detect-us-seawolf-class-submarine-magnetic-wake-tracking-study) · [Asia Times, “China’s magnetic tech can detect US stealth subs,” Feb 2025](https://asiatimes.com/2025/02/chinas-magnetic-tech-can-detect-us-stealth-subs-study/) · [The Quantum Insider, drone-mounted quantum sensor, 27 Apr 2025](https://thequantuminsider.com/2025/04/27/china-tests-drone-mounted-quantum-sensor-that-could-reshape-submarine-detection/) · [SCMP, handheld submarine detector, 25 Sep 2026](https://www.scmp.com/news/china/science/article/3367965/china-tested-handheld-submarine-detector-it-tracked-subway-train-underground)

CH. 2 · ACOUSTICS

UPI, SAIC deep ocean acoustic sensors, 28 Aug 2013 · NAVWAR solicitation N0003919R0022 (GovTribe) · Military & Aerospace Electronics, TRAPS prototypes · Naval Technology, Leidos TRAPS · Navy RDT&E exhibit, Integrated Surveillance System · [DARPA, Ocean of Things](https://www.darpa.mil/research/research-spotlights/ocean-of-things) · [The War Zone, Jan 2018](https://www.twz.com/17903/china-reveals-it-has-two-underwater-listening-devices-within-range-of-guam) · National Maritime Foundation, Undersea Great Wall · Maritime Executive · [JASA 159(5), 2026](https://pubs.aip.org/asa/jasa/article/159/5/4702/3392990/Tracking-ships-with-submarine-cables-Unsupervised) · ResearchGate 396960937 · [Waagaard et al., OSA Continuum 4(2), 2021](https://doi.org/10.1364/OSAC.408761) · [arXiv 2509.11614](https://arxiv.org/abs/2509.11614)

CH. 3 · DARK VESSELS AND SPOOFING

[Paolo et al., Nature 625, Jan 2024 (PMC10764273)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10764273/) · Global Fishing Watch press release · HawkEye 360 Maritime Association, Apr 2022 (SatNews) · Via Satellite, 28 Jan 2021 · Geospatial World, dark ships · [Joint open letter of fourteen European states, 26 Jan 2026](https://kliimaministeerium.ee/sites/default/files/documents/2026-01/Open%20Letter%20by%20the%20Coastal%20States%20of%20the%20Baltic%20Sea%20and%20the%20North%20Sea%20with%20Iceland%20on%20the%20Growing%20Risks%20to%20Maritime%20Safety%20%20to%20the%20International%20_.pdf) · [Royal Institute of Navigation, 23 Jan 2026](https://rin.org.uk/page/RIN_Maritime_Report) · [Windward, Mar 2026](https://windward.ai/blog/gps-jamming-surges-in-the-middle-east-gulf-1650-ships-hit/)

CH. 4 · PASSIVE RADAR

[Hensoldt, NATO measurement campaign, 29 Oct 2019](https://www.hensoldt.net/news/hensoldts-passive-radar-in-nato-measurement-campaign/) · [Defense News, 10 Aug 2023](https://www.defensenews.com/global/europe/2023/08/10/hensoldt-unveils-a-deployable-package-of-its-twinvis-passive-radar/) · [C4ISRNET, 30 Sep 2019](https://www.c4isrnet.com/intel-geoint/sensors/2019/09/30/stealthy-no-more-a-german-radar-vendor-says-it-tracked-the-f-35-jet-in-2018-from-a-pony-farm/) · Association of Old Crows · ERA VERA-NG data sheet · [CASI/BluePath Labs, China’s Air Defense Radar Industrial Base, Mar 2025](https://www.airuniversity.af.edu/Portals/10/CASI/documents/Research/Infrastructure/2025-03-10%20Air%20Defense%20Radars.pdf) · Global Times, 20 Jul 2017 · National Defense, 28 Mar 2023 · Lockheed Martin Australia, AIR6500 · [EasyChair preprint 900](https://easychair.org/publications/preprint/Z8Mw) · [IET Radar, Sonar & Navigation, rsn2.12446](https://doi.org/10.1049/rsn2.12446) · [Sensors 20(3):599, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7037432/) · Geophysical Research Letters, 2015GL064204

CH. 5 · OTH RADAR AND SPACE

[US Patent 11,953,580](https://patents.google.com/patent/US11953580) · “Naval Applications of HF Over-the-Horizon Radar” (ResearchGate) · [Air Force Magazine (Otto Kreisher), 1 Dec 2013](https://www.airandspaceforces.com/article/1213china/) · [SCMP, DF-21D and DF-26B test report, 14 Nov 2020](https://www.scmp.com/news/china/military/article/3109809/chinas-aircraft-carrier-killer-missiles-successfully-hit-target) · China-Arms, Jun 2026 · [NRO Release 5-26](https://www.nro.gov/news-media-featured-stories/news-media-press-releases/Archived-Press-Releases/Press-Release-Article/Article/4520427/nro-launches-fourteenth-proliferated-architecture-mission-with-nrol-179/) · NRO proliferated architecture press kit, 7 Jan 2026 · [NRO news, Space Symposium, Apr 2026](https://www.nro.gov/news-media-featured-stories/news-media-archive/News-Article/Article/4457615/nros-proliferated-architecture-exceeding-expectations-pddnro-tells-space-sympos/) · Spaceflight Now, 11 May 2026 · [ExecutiveGov, NROL-172 and NROL-179](https://www.executivegov.com/articles/national-reconnaissance-office-nrol172-launch) · Northrop Grumman, 10 Oct 2026

CH. 6–8 · FUSION, EMCON, EW

Palantir Foundry and Gotham documentation (Gaia) · [UK Digital Marketplace, G-Cloud 14 Gotham service definition, May 2024](https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/92736/801146272055049-service-definition-document-2024-05-02-1537.pdf) · SpaceNews, Maven expansion · [Breaking Defense, May 2025](https://breakingdefense.com/2025/05/ai-unchained-ngas-maven-tool-significantly-decreasing-time-to-targeting-agency-chief-says/) · DefenseScoop, [15 Apr 2026](https://defensescoop.com/2026/04/15/palantir-maven-smart-system-pentagon-program-transition-feinberg/) and [22 Sep 2026](https://defensescoop.com/2026/09/22/maven-smart-system-ai-james-mazol-cameron-stanley-defensetalks/) · [NHHC, Enterprise (CVAN-65) 1981–85](https://www.history.navy.mil/research/histories/ship-histories/danfs/e/enterprise-cvan-65-viii-1981-1985.html) · NavWeaps, “How to Hide a Task Force” · [Naval War College Review, “Hiding in Plain Sight,” 2011](https://digital-commons.usnwc.edu/nwc-review/vol64/iss2/6) · DARPA SASC testimony, 1 Apr 2016 · Defense News, 29 Aug 2016 · Military & Aerospace Electronics, AI in EW · [The War Zone, NEMESIS](https://www.twz.com/29505/the-navys-secretive-nemesis-electronic-warfare-capability-will-change-naval-combat-forever); Nulka

End of Technical Briefing No. 2

None of it makes running silent obsolete. It makes running silent insufficient on its own.

— Bottom Line
