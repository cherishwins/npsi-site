# NPSI Korean Translation — QA Checklist

Run this checklist against every translation before delivery. It catches the recurring high-stakes failure modes. Use it for both EN → KO and KO → EN unless a check is direction-specific.

If a check fails, fix and re-run the full checklist — fixes sometimes introduce new errors elsewhere.

---

## 1. Register consistency

- [ ] Single register held across the entire document.
- [ ] Working paper body → 한다체 throughout, no drift into 합니다체.
- [ ] LinkedIn caption → 합니다체 throughout, no drift into 한다체 or 해요체.
- [ ] Direct quotes from Korean sources mirror the source's register, not the document's.
- [ ] Titles and headings are noun phrases or 한다체 — not 합니다체 sentences.

**Quick test:** Read the last sentence of each section. They should all end in the same register marker (-다 family for 한다체, -습니다/-합니다 family for 합니다체).

---

## 2. Numerical accuracy

- [ ] Every number in the source appears in the target.
- [ ] Unit conversions correct: 만 / 억 / 조 placement verified for any number above 9,999.
- [ ] Currency units correct (USD ≠ KRW ≠ CAD; place after numeral with no space).
- [ ] Energy units correct (TWh = 테라와트시; GWh = 기가와트시).
- [ ] Date formats correct: Korean uses YYYY년 MM월 DD일 form.
- [ ] Percentage values correct and sign-aligned (% symbol travels).
- [ ] Range notation uses tilde ~ in Korean, not hyphen.

**High-stakes check:** Trillion vs billion. 6조 ≠ 6,000십억. The most common high-impact error.

---

## 3. Proper noun consistency

- [ ] Every named institution appears in its canonical glossary form on first reference.
- [ ] Acronym glossed on first reference, bare acronym thereafter — and the bare acronym matches.
- [ ] The same institution is rendered the same way every time it appears (check for variant spellings like 국민연금공단 vs 국민연금 vs NPS in the same document).
- [ ] Place names rendered consistently (Esquimalt does not appear as 에스콰이몰트 in one paragraph and 이스콰이몰트 in another).
- [ ] Person names use the person's preferred romanization (ROK officials → revised romanization; DPRK officials → McCune-Reischauer or DPRK-preferred form).
- [ ] Ship names match Korean naval convention (도산안창호함 spacing matches across the document).

**Verification:** Any **[VERIFY]** tag from the glossary should be confirmed by primary source before publication, OR flagged in the delivery note.

---

## 4. Calque tells

Scan for the patterns that mark text as translated. (Direction: EN → KO mostly.)

- [ ] No 가지다 + noun calques (회의를 가지다, 의미를 가지다).
- [ ] No English-style passive constructions (~에 의해 + 되다).
- [ ] No floating English pronouns rendered as 그것 / 그 / 그녀 where Korean would drop the subject.
- [ ] No "그리고" between every clause (Korean prefers connective verb endings or comma-listing).
- [ ] No literal idiom translation (숫자는 거짓말하지 않는다 etc.).
- [ ] Sentences read aloud with Korean rhythm — no thumps or hesitations from imported English structure.

**Quick test:** Pick three sentences at random. Read them aloud. If any sound like they were written by someone whose first language was English, rewrite.

---

## 5. Quote integrity

- [ ] Direct quotes from Korean sources are exact reproductions.
- [ ] DPRK orthography preserved in DPRK quotes (로동신문 not 노동신문, 력사 not 역사).
- [ ] ROK source quotes preserve the source's terminology even when NPSI would phrase it differently.
- [ ] No "translation by paraphrase" inside quote marks. Either it's an exact quote or it's NPSI's restatement (in which case remove the quote marks).
- [ ] When a Korean quote contains a slur or politically loaded term, the slur is preserved inside the quote with attribution intact — but never imported into NPSI body voice.

---

## 6. Slur and politically loaded vocabulary scan

- [ ] No 북괴, 빨갱이, 종북, 남조선 괴뢰, 미제 (in NPSI body voice — these may appear only inside attributed quotes).
- [ ] No 김씨 왕조 / 김씨일가 in NPSI body voice.
- [ ] Reunification term: 통일 used (safe). 흡수통일 used only if source uses it.
- [ ] No "Sea of Japan" / "일본해" — East Sea / 동해 is the only acceptable NPSI form.
- [ ] No inadvertent Cold War-era English-side terminology in KO → EN translation ("Red Korea," "Communist North," etc.) unless quoting a historical source.

---

## 7. Formatting parity

- [ ] Paragraph breaks match the source.
- [ ] Heading levels match the source (H1 → H1, H2 → H2 etc.).
- [ ] Lists remain lists.
- [ ] Tables retain their structure; column headers translated; row data translated; numbers verified inside table cells.
- [ ] Footnote and citation markers preserved at the right anchor points.
- [ ] Bold/italic emphasis preserved where it carried meaning in the source.

---

## 8. Length sanity check

- [ ] Korean target length is within ~20% of English source length (character count vs character count, not word count).
- [ ] Target significantly longer than source (>30%) usually indicates padding or calques — investigate.
- [ ] Target significantly shorter than source (>30%) usually indicates omission or compression — investigate.

**Note:** Well-translated Korean is typically slightly shorter than its English source because Korean drops subjects and articles. A target that comes in 5–15% shorter is healthy. A target that comes in longer than the source is usually carrying calque weight.

---

## 9. Final read-through

- [ ] Read the entire target language version once, top to bottom, as a Korean (or English) reader would. Not as a checker.
- [ ] If anything trips you on read, fix it. The institutional reader will trip on the same thing.
- [ ] If the document contains a strong claim (a number, a comparison, a recommendation), confirm the claim survives translation intact. Strength can dilute through restatement.

---

## Delivery note template

When delivering a translated document, include this short note (if useful):

> **Translation note**
> Source: [filename or section]
> Direction: EN → KO (or KO → EN)
> Register: 한다체 working paper / 합니다체 LinkedIn / mixed
> Glossary terms used: [list any [VERIFY] items used so Jesse can confirm]
> Open items: [any ambiguity in source, any term flagged for verification, any decision Jesse should review]

If nothing in the document required a choice worth flagging, deliver clean target text with no note. Do not pad delivery with translator-process commentary Jesse did not ask for.
