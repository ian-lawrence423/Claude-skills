---
name: pattern-investment-pptx
description: >-
  Create Pattern-branded investment decks for IC, diligence, M&A, PE, board, and investor
  materials using the institutional deck system.
intent: >-
  Generate professional, on-brand investment-grade PowerPoint decks for Pattern. Use this
  skill whenever Ian asks to create an investment deck, investor presentation, due
  diligence deck, M&A deck, deal deck, board deck, pitch to investors, or any financial or
  strategic presentation intended for external investors, PE firms, or acquirers. This
  skill encodes the exact visual system, fonts, colors, layout patterns, chart rules,
  table rules, editorial standards, and slide types from Pattern's investment deck
  template — including financial tables, market sizing, unit economics, EBITDA bridges,
  and thesis sections. Always use this skill instead of the generic pptx or pattern-pptx
  skills for any investment or deal materials.
type: workflow
---

# Pattern Investment Deck Generator

You are generating a professional, data-dense investment presentation for Pattern. Every slide
must feel analytical, credible, and institutional — not marketing. Read this entire file before
writing any code.

---

## Example And Anti-Pattern

Example prompt:
> "Build a Pattern investment deck from this approved IC memo and operating model."

Expected use:
- Use Pattern investment deck assets, slide rules, table rules, chart rules, and editorial standards.
- Build data-dense investor slides from hardened content, not raw brainstorming notes.
- Run slide QA before delivery and then `doc-quality-checker` on the output.

Anti-pattern:
- Do not create a generic marketing deck, improvise colors/fonts, or start slide production before the narrative and numbers are hardened.

---
## Step 1: Read the Technical Reference First

Before writing any code, read the full pptxgenjs reference for API usage, pitfalls, and best
practices:

```
Read: {SKILL_DIR}/../pptx/pptxgenjs.md
```

To find `{SKILL_DIR}`: look at the path you used to read this SKILL.md — it ends in
`.../pattern-investment-pptx/SKILL.md`. The `{SKILL_DIR}` is that directory.

---

## Step 2: Locate Logo Assets

```
{SKILL_DIR}/assets/pattern_footer_logo.svg   — Full wordmark, gradient (light slides)
{SKILL_DIR}/assets/pattern_logo_white.svg    — Full wordmark, white (title slide only)
{SKILL_DIR}/assets/pattern_icon_mark.svg     — Icon mark only (title slide corner)
```

Logo appears on the **title slide only**. Content slides do not include a logo — maximize
data space.

---

## Step 3: Read Deck Production Reference Before Generating

Read the implementation reference before writing code:

```
Read: {SKILL_DIR}/references/deck-production-spec.md
```

This reference owns the detailed Pattern investment deck production specs:
- Brand constants and color methodology
- Slide grid, recurring elements, and layout templates
- Bullet hierarchy and text fitting rules
- Chart, table, and layout-selection rules

Use the reference as the implementation source of truth. Keep this file focused on routing,
asset loading, narrative sequence, writing-style review, QA, and professionalism gates.

---

## Step 4: Recommended Slide Sequence

1. **Title slide** (Dark) — project name, date, confidentiality note
2. **Executive summary** — company background, value proposition, financial summary
3. **Business overview** — company profile, financials table, product/service overview
4. **Market** (multi-slide) — TAM/sizing, market structure, growth drivers
5. **Product / Platform** (multi-slide) — product detail, component breakdown, competitive positioning
6. **Customer / Revenue** (multi-slide) — segmentation, cohort data, NRR/GRR, retention
7. **Financials** (multi-slide) — P&L, revenue bridge, EBITDA bridge, unit economics
8. **Growth / Outlook** — forward projections, path to profitability
9. **Appendix** — supporting data, supplemental tables

**No thesis divider slides.** Content flows continuously. Each slide title must be an
insight statement, not a label.
- ✓ "Multi-module adoption accelerating — single-module merchants down to 61% of base"
- ✗ "Module Adoption"

**Pacing:** One key message per slide. Align chart axes and sizes when multiple charts
appear on the same slide. Financial tables: add a "Key Insights" callout column when space allows.

---

## Step 5: Writing-Style Self-Review — Run Before Generating Code

After planning slide content (Step 4) and before writing any pptxgenjs code, draft
all slide text in plain text and run the writing-style self-review pass on all
narrative and body content.

**When this applies:** Executive summary slide, thesis slides, narrative body text,
callout boxes, recommendation slides, and any text block longer than a short label.

**When this does NOT apply:** Pure data labels, chart axis titles, table cell values,
source lines, and slide numbers.

**How to invoke:**
1. Draft all slide text content in plain text — do not write pptxgenjs code yet
2. Load and run the writing-style skill self-review (Steps 1–5) on all prose content
3. Apply all flags before generating code — fixing prose after it is in pptxgenjs
   code requires rewriting the code
4. The writing-style pre-delivery checklist must pass before code is written

**Specific PPTX focus areas for writing-style:**
- Every slide title is an insight statement (not a label) — this is both a writing-style
  and brand standard. writing-style Step 2 (absolute assertion test) catches titles
  that are labels masquerading as insights.
- Executive summary slide bullets pass the inductive chain test — each bullet states
  a conclusion with its evidence, not just a topic
- Callout boxes pass the specificity test — numbers, not adjectives

**Reference:**
```
Read: /mnt/skills/user/writing-style/SKILL.md
```

---

## Step 6: Editorial Standards

### Case
- **Title slide title:** Title Case (skip articles/prepositions/conjunctions under 5 letters)
- **All other slide text:** Sentence case — titles, headings, bullets, labels

### Punctuation
- No closed punctuation on bullets (no periods, commas, or colons at end)
- Running/paragraph text: closed punctuation
- Bullets: short phrases, not full sentences
- En dash (–): ranges and routes, no spaces (100–150, 10:00–11:00, Frankfurt–New York)
- Em dash (—): parenthetical phrases, no spaces (50% off—today only)
- Ellipses: only for omitted quoted material; never to trail off a thought or title
- No space before or after a slash (and/or, 1920/21, 5 ft/s)
- Thousands separator: comma (8,000 not 8000)
- Double quotes for quotations; periods/commas inside; single quotes for quote-within-quote

### Numbers
- Under 10: spell out unless preceded by a unit symbol ($9 = fine; "nine companies" not "9 companies")
- Fractions: spell out in text (one-half); decimal in tables (0.5)
- T/B/M/K: no space between number and abbreviation (42K, 17.4M, $2.3B, 1.1T)
- Never use "000" as a unit for thousands
- Comma as thousands separator; decimal form in tables

### Units of Measure
- Always lowercase (kg, km, lb — not Kg, LB)
- Space between number and unit (15 kg, 9.84 m, 100 rpm)
- No periods in unit abbreviations (kg not kg., rpm not r.p.m.)
- No "s" pluralization (kg not kgs, lb not lbs)
- In charts/tables: unit in parentheses after heading (Revenue ($M), Population (K))

### Dates
- Write out in full in running text; no numeric-only dates (not "4/5/07")
- US format: October 23, 2025
- Tables/charts: three-letter abbreviations (Jan, Feb, Mar…)
- Cardinal numbers: October 19 (not October 19th)

### Abbreviations
- No punctuation needed for most (US, UK, GDP, EBITDA, GMV, NRR)
- Always punctuate: e.g., i.e., p.a., vs., etc., et al., avg., ca., excl., incl., esp.
- Spell out "versus" in prose; "vs." in tables/charts only

### Vernacular
- Don't capitalize or italicize anglicized foreign words (ad hoc, per se, vice versa, bona fide)
- Don't capitalize common nouns: seasons, directions, generic government/org terms
- Capitalize ranks/titles alongside a name; lowercase when referring to office alone

### Typesetting
- Avoid widows (last line alone at top of column) and orphans (first line alone at bottom)
- Fix with soft return before the previous word, or trim content

---

## Step 7: QA — Do Not Skip

### Content check
```bash
python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum|placeholder|tbd"
```

### Visual check
```bash
python /mnt/skills/public/pptx/scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

**Inspect every slide for:**
- [ ] Text overflow or cutoff at edges
- [ ] Blue rule present below title on every content slide at y=0.656
- [ ] Icon mark present top-right on every content slide
- [ ] Footnote zone present on every slide that has a source or note
- [ ] Slide number present on every slide
- [ ] No logo on content slides (title slide only)
- [ ] Column alignment consistent across multi-column layouts
- [ ] Chart colors from defined palette (not default Office colors)
- [ ] Table headers use `tableHeaderDark` fill with white text and `F.semibold`
- [ ] No `bold: true` anywhere — all bold text uses `fontFace: F.semibold`
- [ ] Slide titles are 14pt `F.semibold`
- [ ] Body level-1 bullets are 10pt brandBlue; level-2/3 are 9pt black
- [ ] Bullet characters: level-1 = • Arial, level-2 = ‒ Wix Madefor Display, level-3 = • Arial
- [ ] No periods at end of bullet points
- [ ] All content slide titles in sentence case; title slide in Title Case
- [ ] Every slide title reads as an insight, not a label
- [ ] No thesis divider slides in the deck
- [ ] Slide dimensions are 10" × 5.625"

Fix all issues before declaring done.

---

## Step 8: Professionalism Review — Do Not Skip

This step runs **after** the mechanical QA in Step 7. Render every slide to image, then evaluate each one through the lens of an MBB (McKinsey / Bain / BCG) consultant preparing materials for a sophisticated client. The brand guide is the floor, not the ceiling. The goal is a deck that would pass without comment in a senior partner review.

### No-fly zones — hard margins nothing may enter

Authoritative values confirmed from source presentation settings:

```
Top edge:      y < 0.94"   (content starts at y=0.94")
Bottom edge:   y > 5.185"  (content ends at y=5.185"; footnote zone below this is exempt)
Left edge:     x < 0.40"
Right edge:    x > 9.72"   (10.0 - 0.28")
```

**Exempt from no-fly zone** (by design, outside content area):
- Slide title: y=0.174" — above top margin, exempt
- Blue rule: y=0.656" — above top margin, exempt
- Icon mark: x=9.478" — in right margin, exempt
- Footnote zone: y=5.276" — below bottom margin, exempt
- Slide number: y=5.276" — below bottom margin, exempt

If any content text box, chart, table, or shape bleeds into these margins, reposition or resize before proceeding.

### Slide-by-slide professionalism checks

For each rendered slide image, ask all of the following:

**Density & fit**
- [ ] Does all content fit comfortably within the no-fly zone with visible breathing room? If content is cramped, reduce font size (minimum: 8pt body, 7pt captions), tighten paragraph spacing, or split onto a second slide — never sacrifice margins
- [ ] Is there obvious dead space on a slide that could be filled with a supporting visual, callout, or data point? Dead space signals incomplete thinking
- [ ] Is text size consistent within a content zone? Mixed sizes within the same column or section suggest inconsistency — standardize

**Typography & readability**
- [ ] Are slide titles insight statements or labels? A label ("Revenue") is unacceptable — rewrite as an insight ("Revenue growth accelerating — 34% YoY in CY2027")
- [ ] Is every title in sentence case? Check the first letter of every word after the first
- [ ] Do bullet level-1 lines open with the key claim, not a qualifier? ("Revenue grew 40%" not "In terms of revenue, growth was 40%")
- [ ] Are bullets parallel in structure within a section? Mixed verb tenses or inconsistent phrasing signal unpolished writing — align them
- [ ] Are there any bullet points that could be tightened by 30%+ without losing meaning? If so, tighten them. Consultants write lean
- [ ] Is any single bullet more than two lines long? If so, split or trim — three-line bullets signal a layout problem, not a writing one
- [ ] Are numbers formatted correctly? ($2.3B not $2,300M; 42K not 42,000; 97% NRR not 0.97 NRR)

**Visual hierarchy & layout**
- [ ] Is there one unambiguous "most important thing" on the slide? If a reader's eye lands in three places, the hierarchy is broken — use size, color, and position to fix it
- [ ] Is brandBlue used sparingly enough to retain signal value? More than one or two brandBlue elements per content zone dilutes emphasis
- [ ] Are all column headings aligned with their column content? Misalignment of any element — even by a few pixels — reads as sloppy
- [ ] Do all charts have a source line in the footnote? Unsourced data is a credibility risk in investment contexts
- [ ] Are chart axes labeled with units? An unlabeled axis is never acceptable

**Tables**
- [ ] Does the table have more rows or columns than can be read at a glance? If yes: remove non-essential columns, move detail to appendix, or use a summary table + footnote
- [ ] Are totals/subtotals visually distinct from body rows (SemiBold or shading)?
- [ ] Are negative values shown in alertRed? Are positive variances shown in tealPrimary? Consistent encoding of valence is a professional standard

**Consistency across the deck**
- [ ] Are all slide titles the same font size (14pt) and positioned at the same y-coordinate (y=0.174)?
- [ ] Are all blue rules at y=0.656, full width?
- [ ] Are all slide numbers in the same position, same font, same color?
- [ ] Are all content areas starting at y=0.801?
- [ ] Does the visual language feel consistent — same chart style, same table style, same callout style throughout?

### Font-size adaptation rules

The brand guide specifies sizes optimized for typical content density. When slides are unusually dense, **scale down proportionally** rather than letting content overflow:

| Situation | Adjustment |
|---|---|
| Body text overflows content area | Reduce to 9pt (lvl-1) / 8pt (lvl-2/3); tighten paraSpaceBef to 2pt |
| Table has 15+ rows | Reduce tableBody to 7pt; tableHeader stays 9pt |
| Table has 6+ columns | Reduce all table text to 7pt; abbreviate headers aggressively |
| 3+ columns of text | Reduce body to 9pt/8pt; remove third-level bullets |
| Chart axis labels overlap | Reduce to 6pt; rotate x-axis labels 45° only as last resort |

**Minimum readable sizes:** 7pt body text, 6pt captions. Never go below these.

### The partnership-ready test

Before marking the deck complete, answer these four questions as if you are the Pattern partner who will hand it to a PE firm tomorrow:

1. **Would a senior partner approve this without edits?** If not — identify specifically what they would mark up and fix it.
2. **Does every slide earn its place?** A slide that could be removed without weakening the narrative should be removed or merged.
3. **Is the data story legible in under 10 seconds per slide?** If the key point requires reading three bullet levels to find, restructure.
4. **Would this pass a print-quality review?** Render at high resolution. Blurry icons, misaligned elements, or clipped text disqualify the deck.

If any answer is "no," fix it before outputting the final file.

---

## Common Pitfalls

- **Color is a signal, not decoration** — keep Pattern palette constants unchanged, but apply color with restraint: gray/neutral base, one `brandBlue` highlight, semantic teal/red only for valence. Do not color-code blocks of text, fill textboxes to organize content, or use multiple accents when whitespace, alignment, or de-emphasis would create the hierarchy more cleanly.
- **`margin` is table-level only — never per-cell** — passing `margin` inside individual cell `options` objects is silently ignored and corrupts layout. Always set margin at the `addTable(rows, { margin: [...] })` level only:
  ```javascript
  // ❌ WRONG — margin in cell options is silently ignored
  { text: "Cell", options: { fill: ..., margin: [2, 4, 2, 5] } }
  // ✅ CORRECT — margin at table level applies to all cells
  slide.addTable(rows, { x, y, w, colW, rowH, margin: [2, 5, 2, 5] });
  ```
- **Section header rows: do NOT use `colspan`** — pptxgenjs colspan causes the entire row fill to bleed across the whole table. Instead, create 6 explicit cells per section row, all with the same fill color:
  ```javascript
  // ❌ WRONG — colspan breaks adjacent column fills
  [{ text: "Section", options: { colspan: 6, fill: { color: "1C3461" } } }, empty(), ...]
  // ✅ CORRECT — 6 explicit cells with matching fill
  const sec = (label) => [
    { text: label, options: { fill: { color: "1C3461" }, align: "left", ... } },
    { text: "",    options: { fill: { color: "1C3461" }, border: [{ pt:0 },...] } },
    { text: "",    options: { fill: { color: "1C3461" }, border: [{ pt:0 },...] } },
    { text: "",    options: { fill: { color: "1C3461" }, border: [{ pt:0 },...] } },
    { text: "",    options: { fill: { color: "1C3461" }, border: [{ pt:0 },...] } },
    { text: "",    options: { fill: { color: "1C3461" }, border: [{ pt:0 },...] } },
  ];
  ```
- **Never use `LAYOUT_WIDE`** — deck is 10"×5.625", must use `pres.defineLayout({ name:'CUSTOM_10x5625', width:10, height:5.625 })`
- **Never use `bold: true`** — all bold uses `fontFace: F.semibold` ("Wix Madefor Display SemiBold")
- **Never use `#` with hex colors** — causes file corruption in pptxgenjs
- **Never use 8-char hex for opacity** — use the `opacity:` property
- **Always `margin: 0`** on text boxes when aligning with shapes
- **Never reuse option objects** across multiple `addShape/addText` calls
- **Dark slide** uses `090A0F` not pure `000000`
- **No accent underlines under headings** — use whitespace
- **No thesis divider slides**
- **No logo on content slides** — icon mark only (top-right, every slide)
- **Set chart colors explicitly** — never rely on Office default series colors
- **Slide title is 14pt** — not 9pt. These decks are printed/PDF, not projected
- **Blue rule is full-width** (x=0, w=10.0) at y=0.656, not a partial rule at y=0.52
- **Content area starts at y=0.801**, not y=0.65
- **doc-quality-checker is mandatory after every output** — after presenting the final
  .pptx file, always run the doc-quality-checker skill immediately. Do not wait to be
  asked. State "Running quality check..." and produce the full issue report before
  ending the response. If zero issues are found, state that explicitly.

---

## Full Brand Reference

For complete edge cases, see:
```
Read: {SKILL_DIR}/references/brand-guide.md
```
