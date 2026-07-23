---
name: npsi-korean-translation
description: Translate EN ↔ KO for NPSI working papers and LinkedIn captions, and for reading Korean primary sources (Yonhap, KCNA, 조선중앙통신, Chosun, Hankyoreh, JoongAng, Korea Herald, 노동/로동신문). Enforces register (한다체 for papers, 합니다체 for LinkedIn, mirror-source for direct quotes), Sino-Korean academic vocabulary, ROK orthography default with DPRK forms preserved in quotes, canonical NPSI proper nouns (NPS, KIC, KOGAS, 도산안창호함, 에스콰이몰트), and Korean numbering (만/억/조). Trigger on 'translate to Korean', 'Korean version', 'in Korean', 'Korean caption', 'NPSI Korean', '한국어로', 'translate this article', or any Korean source handover. ALSO trigger automatically before publishing any NPSI output with Korean text — institutional readers detect translation tells instantly. Output is publishable target text only; translator notes only when real ambiguity warrants; back-translation gloss only on explicit QA request. NOT for JucheGang brand identity, Cherish/VI Care, Ibrahim Arabic, or Fit For Gov.
---

# NPSI Korean Translation

Reliable Korean ↔ English translation for NPSI working papers and LinkedIn captions. The goal is prose that a Korean institutional reader does not flag as translated.

## What "professional" means here

NPSI's Korean audience is not general. It includes National Pension Service (NPS) fund managers, Korea Investment Corporation (KIC) executives, Korea Investment PE partners, ROK Navy and intelligence officers, Korea Herald journalists, and the curated JucheGang LinkedIn page audience. They read Korean policy and finance writing daily. Their tolerance for translation tells is zero. A clumsy 가지다 calque or a wrong honorific choice signals immediately that the writer does not actually speak the language, which collapses the credibility the working paper was built to establish.

The bar is therefore not "comprehensible." The bar is "indistinguishable from native Korean institutional writing."

## Step 1: Pick the register

Korean speech and writing levels are not interchangeable. The wrong level reads as either condescending or unprofessional.

- **NPSI working paper body text → 한다체** (declarative formal, also called the *plain written* style). Sentence endings -다, -이다, -였다, -한다, -아니다. This is the register of *Chosun Ilbo* editorials, academic journals, and government white papers. Use throughout the body of any working paper.

- **NPSI working paper titles, abstracts, executive summaries → noun-final or 한다체**. Titles are usually noun phrases (e.g., "덧셈의 역설" not a sentence). Abstracts use 한다체.

- **NPSI LinkedIn captions, post intros, direct reader address → 합니다체** (deferential formal). Sentence endings -습니다, -합니다, -입니다, -였습니다. This is the register of business correspondence, formal speeches, and professional social media in Korean. It carries warmth and respect without familiarity. Korean LinkedIn does NOT use 한다체 because the reader feels addressed by it, and declarative-formal reads cold and journalistic in that context.

- **Direct quotes from Korean sources → mirror the source exactly**. If KCNA says 조선민주주의인민공화국, do not "translate" it to 북한. If a Yonhap dispatch uses 평양 정권, do not soften it to 북한 정부. Quote integrity outranks editorial consistency.

- **Mixed-register edge case**: when a working paper *contains* a long block-quoted Korean source, the body stays 한다체 and the quote stays in its native register. Use Korean quote marks 「」 or " " to mark the seam.

A note on familiar tempting wrong answers: 해요체 (polite informal, -요 endings) is wrong for both NPSI use cases. It reads as a personal blog or a service-industry interaction. 합쇼체 / -십시오 forms are wrong for written work because they are oratorical. Stay in 한다체 or 합니다체.

## Step 2: Translate

### English → Korean

1. **Read the entire English passage before translating any of it.** Korean sentence structure (SOV, drops subjects, marks topic) requires knowing where the sentence is going before its first word. Sentence-by-sentence translation produces calques. Paragraph-by-paragraph translation produces Korean.

2. **Identify proper nouns and institutions first.** Look them up in `references/glossary.md`. If a term is not in the glossary and the surface translation is non-obvious, flag it for verification rather than guessing. Korean readers will notice an institution name rendered three different ways across a paper.

3. **Choose Sino-Korean (한자어) vocabulary by default for institutional content.** Working papers in Korean lean heavily on 한자어 for precision: 협력 not 함께하기, 자본 not 돈, 인프라 not 기반시설 (both exist; 인프라 is the institutional finance term). Native Korean words (고유어) feel literary or casual and are wrong for working paper register. The exception is LinkedIn caption openings, where one native-Korean phrase can warm the opening line before the prose shifts back to 한자어.

4. **Drop English structural scaffolding.** Korean does not need most English subjects, articles, possessives, or relative-clause connectors. "The bond, which is co-issued by both governments, would finance" → 양국 정부가 공동발행하는 채권은 ~ 자금을 조달한다. Not "그 채권, 그것은 양국 정부에 의해 공동발행되는, 자금을 조달할 것이다." The second sentence is technically grammatical and immediately marks the writer as non-Korean.

5. **Use Korean numbering.** 만 (10,000), 억 (100,000,000), 조 (1,000,000,000,000). 6 trillion dollars → 6조 달러. 280 million barrels → 2억 8천만 배럴. 1,172 TWh → 1,172테라와트시. Do not write "60억" for 6 billion when you mean 6조 for 6 trillion — the unit shift is the most common high-stakes error.

6. **Gloss acronyms on first use, then use the acronym.** First use: 국민연금공단(NPS). After that: NPS. This matches Korean institutional convention exactly and serves both readers who know the acronym and readers cross-referencing in English.

7. **For LinkedIn captions specifically:**
   - Open with the strongest concrete claim, not setup.
   - 합니다체 throughout.
   - Line breaks every 1–2 sentences for mobile readability — Korean LinkedIn reads on phones, mostly.
   - Emoji-light. One trailing emoji is the institutional ceiling. Zero is also fine.
   - No hashtag spam. One or two relevant tags (#한미동맹 #한반도 #에너지안보) if any.
   - Do not translate Sutter-voice English idioms directly. Restate the *content* in Korean institutional voice. "The numbers don't lie" → 수치는 분명하다 or 숫자가 말해준다, not 숫자는 거짓말하지 않는다 (which is a calque tell).

### Korean → English

1. **Identify the source's posture before translating.** KCNA, *노동신문*, and *조선중앙통신* write from the DPRK state position. *Yonhap*, *Chosun*, *Hankyoreh*, *JoongAng*, *Korea Herald* carry distinct editorial postures within ROK media. The translation preserves the posture; it does not flatten it and does not editorialize against it.

2. **Translate what was actually said, not what an English audience expects to hear.** Do not sanitize DPRK rhetoric for Western readability. Do not soften ROK conservative framing into neutral-press voice. If 미제 appears in a DPRK quote, render "the U.S. imperialists" — not "the United States." If a ROK source uses 북한 도발, render "North Korean provocation" — do not translate it as "North Korean action."

3. **Watch for Sino-Korean compounds that have specific English-of-record translations** in policy and finance contexts. 자주국방 → "self-reliant national defense" (the technical term), not "independent military." 한반도 평화 프로세스 → "Korean Peninsula Peace Process" (capitalized; this is a proper noun for the 2018-era ROK policy framework). Consult `references/glossary.md` for the canonical list.

4. **Preserve DPRK orthographic markers when quoting**. *로동신문* not *노동신문*. *력사* not *역사*. *녀성* not *여성*. The orthographic difference signals to a careful reader which side of the DMZ the source comes from. Flattening this throws away information NPSI's audience can read.

5. **Korean drops subjects; English requires them.** Adding subjects is correct translation, not addition. But add the *correct* subject inferred from context, not a guess. When the subject is genuinely ambiguous in Korean, an English translator's note is appropriate (`[subject: speaker or government — ambiguous in original]`).

## Step 3: Verify before delivering

Run `references/qa-checklist.md` against the output. It catches the recurring failure modes (numbering unit errors, register drift, institution name inconsistency, calque tells, quote-integrity violations).

Two checks are non-negotiable before any EN → KO output is delivered:

- **Numbers**: every number, unit, and currency in the source appears correctly in the target. 만/억/조 conversions verified.
- **Proper nouns**: every named institution, place, person, and ship appears in its canonical Korean form per the glossary. If any are not in the glossary, flag them and ask Jesse to confirm before publication.

## Output format

Default: **publishable Korean (or English) only**, formatted to match the source's structure (headings remain headings, lists remain lists, paragraph breaks preserved).

Add a brief **Translator notes** block ONLY when:
- A deliberate terminology choice was made over a plausible alternative (e.g., chose 자주 over 독립 for "sovereign" because the source connoted self-determination, not separation).
- The source contained a genuine ambiguity that the target language forces a choice on (e.g., Korean subject-drop where English needs a subject, gendered pronouns in English that Korean does not mark).
- A proper noun was not in the glossary and was rendered on best inference.

Add an **English back-translation gloss** ONLY when Jesse explicitly asks for "QA," "gloss," "back-translate," "check," or similar. Format: paragraph-aligned, English under Korean.

Do not pad output with explanations Jesse did not request. Korean-only when Korean was asked for. English-only when English was asked for.

## Critical failure modes to avoid

**Calque tells** (English structure imported into Korean):
- ❌ 우리는 이 문제에 대해 논의를 가졌다  ✅ 우리는 이 문제를 논의했다
- ❌ 그것은 중요한 의미를 가진다  ✅ 이는 중요하다 (or context-specific restatement)
- ❌ 회의가 김 장관에 의해 개최되었다  ✅ 김 장관이 회의를 개최했다

**Numbering unit collapse**:
- ❌ "6 trillion" → 6,000십억 (literal "six thousand billion" — wrong unit base)  ✅ 6조
- ❌ "280 million barrels" → 280만 배럴 (off by 100×)  ✅ 2억 8천만 배럴

**Register drift mid-document**:
- A working paper that starts in 한다체 and slides into 합니다체 in the conclusion reads as if two people wrote it. Pick a register and hold it across the entire document.

**Slur-adjacent vocabulary**:
- Never produce: 북괴, 빨갱이, 종북, 남조선 괴뢰, 김씨일가 (in NPSI's own voice). Quoting a source that uses these is acceptable inside quote marks with attribution; using them in NPSI body text is not.
- Reunification term: 통일 (used by both sides, safe). Do not invent compounds like 흡수통일 in NPSI voice unless the source uses it.

**Sutter idiom direct translation**:
- Jesse's English voice has dry-American cadence ("the numbers don't lie," "let's call it what it is," "math is math"). Direct Korean translations of these are calque tells. Restate the *content* of the line in Korean institutional voice instead.

**Forced cultural equivalence**:
- Do not "Koreanize" English metaphors by reaching for a Korean idiom that carries different baggage. Plain restatement beats forced equivalence. Korean readers tolerate restated content; they do not tolerate mis-keyed cultural references.

## Reference files — when to consult

- **`references/glossary.md`** — Consult on EVERY EN→KO and KO→EN job before delivering. Contains canonical NPSI translations for institutions (NPS, KIC, KOGAS, Hanwha, NOC Libya), places (Esquimalt, Murzuq Basin, Fort McMurray, Prince Rupert), ships (도산안창호함), policy terms (sovereign bond, Pacific infrastructure facility), and working paper titles (WP01, WP02, WP03, WP04). Flag anything not in the glossary.

- **`references/style-guide.md`** — Consult when uncertain about register choice, orthographic conventions (ROK vs DPRK), numbering, punctuation, or how to handle mixed-language content. Contains the full register decision tree, ROK/DPRK orthographic differences, and side-by-side worked examples.

- **`references/qa-checklist.md`** — Run against every output before delivery. Eight-point checklist covering register consistency, numerical accuracy, proper noun consistency, calque detection, quote integrity, slur scan, formatting parity, and length sanity check.

## Working with related skills

- **Voice (Sutter, JPanda, Letters from the Earth)**: voice skills govern the English source. This skill governs the Korean target. The Korean target does not "preserve voice" mechanically — it produces the Korean institutional equivalent of the voice's *content*. Korean does not have a register that maps cleanly to Sutter's dry American sardonic register, so do not try to manufacture one.

- **Geopolitical briefing, scenario fork, briefing compression**: these govern English-side document architecture. When a deliverable will be bilingual or Korean-only, this skill runs after they do — on the finished English.

- **Red-team-read**: a Korean working paper should be red-teamed in Korean by a Korean reader before publication where possible. This skill cannot substitute for that. When primary-Korean review is not available, run red-team-read on the English source and flag in delivery that the Korean has not been native-reviewed.

- **JucheGang brand kit**: governs visual identity for 주체강 content. Does not govern translation choices. If a JucheGang post needs Korean translation, this skill produces the Korean; juchekang-brand-kit lays it out.

## When to refuse to translate

- When the source is not in front of you. Do not produce Korean from a paraphrase or a summary — request the source text.
- When proper nouns critical to the document are not in the glossary and cannot be verified. Flag and stop.
- When the source contains slurs (in any direction) that NPSI would not publish in its own voice. Ask Jesse for direction before producing target text.
