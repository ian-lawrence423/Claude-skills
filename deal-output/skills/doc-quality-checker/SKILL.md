---
name: doc-quality-checker
description: |
  Runs a comprehensive quality and formatting check on Pattern Word documents (.docx) and
  Pattern investment PPTX decks after they are created. Checks brand formatting, content
  quality, structural logic, table integrity, header/footer, page numbers, and narrative flow.
  AUTO-RUNS after any pattern-docx or pattern-investment-pptx output is produced — do not
  wait to be asked. Also triggers when Ian says "check this", "QA this", "review this doc",
  "proof this", "quality check", "run a check on this", "does this look right", or "is this
  ready". Always produces a severity-rated inline issue list with exact locations. Never
  auto-fixes — list issues only and let Ian decide what to fix.
---

# Pattern Document Quality Checker

You are running a post-production quality audit on a Pattern document. Your job is to catch
every formatting deviation, content error, structural problem, and brand violation before the
document reaches an external audience. Read this entire file before beginning any check.

This skill auto-runs after any output from pattern-docx or pattern-investment-pptx. It can
also be invoked manually on any existing Pattern document.

---

## Step 1: Identify Document Type and Load Brand Spec

Before running any checks, identify what you are auditing:

**Type A — Pattern Word Document (.docx)**
Load the brand spec:
```
Read: /mnt/skills/user/pattern-docx/SKILL.md
```
Focus sections: Step 3 (Brand Constants), Step 4 (Paragraph Types), Step 6 (Table Styles),
Step 9 (Critical Rules).

**Type B — Pattern Investment PPTX Deck**
Load the brand spec:
```
Read: /mnt/skills/user/pattern-investment-pptx/SKILL.md
```
Focus sections: Step 3 (Brand Constants), slide dimension rules, no-fly zone margins,
font rules, chart and table specs.

If auditing both in one session, load both specs before proceeding.

---

## Step 2: Severity Classification

Every issue found is assigned one of three severity levels. This determines how urgently it
must be resolved before the document is used externally.

| Severity | Label | Meaning |
|----------|-------|---------|
| **Critical** | 🔴 CRITICAL | Brand violation, factual error, broken reference, or missing required element. Document should not be sent until resolved. |
| **Warning** | 🟡 WARNING | Formatting inconsistency, weak content, or structural issue that degrades quality but doesn't break the document. |
| **Minor** | 🔵 MINOR | Polish item — small spacing issue, word choice, or style deviation that is noticeable up close but doesn't affect readability. |

---

## Step 3: Word Document Checks (Type A)

Run all five check categories in order. Report every issue with its exact location:
paragraph number, section name, or table identifier.

### Check Category 1 — Brand Formatting

Cross-reference every text element against the brand constants in pattern-docx SKILL.md Step 3.

**Fonts:**
- [ ] All body text uses `Wix Madefor Display` — flag any Arial, Calibri, Times, or system font
- [ ] All H1 headings use `Wix Madefor Display SemiBold` — flag if using regular weight or bold:true
- [ ] All H2 headings use `Wix Madefor Display SemiBold` — flag if bold:true is set instead
- [ ] Table headers use `Wix Madefor Display SemiBold` — flag regular weight in header rows
- [ ] No other fonts present anywhere in the document

**Colors:**
- [ ] H1 text color = `4280F4` — flag any deviation
- [ ] H2 text color = `3A00FD` — flag any deviation
- [ ] Body text color = `000000` — flag colored body text that isn't a deliberate callout
- [ ] Body Note color = `0F4761` — flag if Body Note paragraphs use a different color
- [ ] Table header fill = `0F4761` — flag any other fill color in header rows
- [ ] Alternating row fill = `F2F2F2` / `FFFFFF` — flag inconsistent alternation
- [ ] Red callout color = `C00000` — flag approximate reds
- [ ] Orange callout color = `C55A11` — flag approximate oranges
- [ ] Green callout color = `375623` — flag approximate greens

**Spacing and margins:**
- [ ] Page margins = 720 DXA (0.5 inch) all sides — flag if default 1-inch margins present
- [ ] H1 spacing: before=160, after=100 — flag deviations
- [ ] H2 spacing: before=200, after=80 — flag deviations
- [ ] Body spacing: after=80 — flag deviations
- [ ] Body Bold Lead spacing: after=120 — flag deviations

### Check Category 2 — Structural Logic

- [ ] First H1 has `pageBreakBefore: false` — flag if first section starts on page 2
- [ ] All subsequent H1s have `pageBreakBefore: true` — flag any H1 that doesn't start a new page
- [ ] H1 has bottom border rule (color BBBBBB, single, size 4) — flag missing rules
- [ ] H2s appear only within H1 sections — flag any H2 that precedes the first H1
- [ ] No heading levels skipped (H3 should not appear without H2 above it)
- [ ] Cover page has title block, subtitle, and metadata line — flag missing elements
- [ ] Sections follow a logical order consistent with document purpose
- [ ] No orphaned headings (H1 or H2 with no body content beneath them)

**Page numbers:**
- [ ] Page numbers are present in the footer
- [ ] Page numbers are sequential — flag any break in sequence
- [ ] Page 1 (cover) numbering — confirm whether cover is numbered or excluded, flag if inconsistent with intent
- [ ] If an agenda or table of contents is present: verify every referenced page number matches the actual page where that section begins — flag any mismatch

**Agenda / Table of Contents (if present):**
- [ ] Every section listed in the agenda exists in the document
- [ ] Every section in the document is listed in the agenda (no unlisted sections)
- [ ] Page numbers in the agenda match actual section start pages exactly — this is a 🔴 CRITICAL check
- [ ] Agenda formatting matches body style (no rogue fonts or colors)

### Check Category 3 — Header and Footer

- [ ] Header is present on all pages (or all non-cover pages if cover is excluded)
- [ ] Header contains the Pattern logo — flag if missing or broken image reference
- [ ] Header contains the gradient rule line — flag if absent (common Phase 2 failure)
- [ ] Header contains the document title text — flag if blank or placeholder text remains
- [ ] Footer is present on all pages
- [ ] Footer contains the Pattern icon mark (left side) — flag if missing
- [ ] Footer page number appears right-aligned — flag if left-aligned or centered
- [ ] Footer format: `[page number] | Page` — flag any deviation
- [ ] Footer top border rule present (color D9D9D9) — flag if missing
- [ ] No placeholder text remaining in header or footer (`[Document Title]`, `[Date]`, etc.)

### Check Category 4 — Table Integrity

For every table in the document:

- [ ] Table width = 10800 DXA — flag any table that doesn't span full content width
- [ ] Column widths sum to exactly 10800 DXA — flag any discrepancy
- [ ] Header row fill = `0F4761` with white (`FFFFFF`) SemiBold text
- [ ] Data rows alternate `FFFFFF` / `F2F2F2` — flag broken alternation pattern
- [ ] Highlighted/totals rows use `D9E2F3` fill with SemiBold text
- [ ] All cells have border: single, size 4, color `DDDDDD`
- [ ] Cell margins: top=80, bottom=80, left=120, right=120
- [ ] No merged cells that break the column width rule
- [ ] ShadingType.CLEAR used — flag any SOLID shading (renders as black)
- [ ] No empty header cells — flag tables where a column has no header label

### Check Category 5 — Content Quality

- [ ] No placeholder text anywhere (`[Insert X]`, `TBD`, `[Date]`, `[Company Name]`)
- [ ] No lorem ipsum or filler text
- [ ] Grammar and spelling — flag obvious errors (do not flag stylistic choices)
- [ ] Numbers formatted consistently: `$2.3B` not `$2,300M`; `34%` not `0.34`
- [ ] Dates formatted consistently throughout (pick one: `March 2026` or `Mar 2026` or `3/2026`)
- [ ] No sentence ends without punctuation (except headings — headings intentionally unpunctuated)
- [ ] No mid-sentence capitalization errors
- [ ] Callout/verdict colors used correctly: red = risk, orange = conditional, green = pass
  — flag if a green callout describes a risk or a red callout describes a positive finding
- [ ] Every section has a lead paragraph — flag any H1 section that jumps straight to H2 or bullets
- [ ] Body Note paragraphs (navy, SemiBold) used only for genuinely important callouts — flag overuse

**Draft artifact language check — 🔴 CRITICAL for any IC-distribution document:**

These patterns indicate internal analytical scaffolding that was not cleaned before
distribution. Each is a CRITICAL issue — they signal to an external reader that the
document is a working draft, not a final deliverable.

- [ ] Cover subtitle contains changelog text — e.g., `v[N] adds: [list]` or
  `v[N] incorporates: [list]` → should be distribution metadata only:
  `[Month Year] · [Team name] · CONFIDENTIAL · For IC Distribution`
- [ ] Cover or header contains version suffix — e.g., `MEMORANDUM — v4`, `Memo v5` →
  strip to `INVESTMENT COMMITTEE MEMORANDUM` for distribution
- [ ] Bottom footnote is a changelog rather than source citation — should name data
  sources, date ranges, BRL/USD sensitivity where applicable, and legal disclaimer
- [ ] Section headers contain version annotations — e.g., `(NEW v4)`, `— v4 (15 Failure Modes)`,
  `(updated from v3)` → remove entirely; the section title stands alone
- [ ] Body text contains `Pre-mortem addition:` or `Pre-mortem addition —` prefix →
  rewrite as substantive label describing what the finding is
- [ ] Body text contains `Pre-mortem update:`, `Pre-mortem note:`, or `[Analysis pass] adds`
  → remove prefix; integrate substance into analytical paragraph
- [ ] Failure mode codes in body text — e.g., `FM1`, `FM2, v4 NEW`, `(FM9, v4 NEW)` →
  use the named finding directly: "Silent Credit Cliff" not "FM1"
- [ ] Compound path headers contain version tags — e.g., `Compound Path 1 (NEW v4)`,
  `Compound Path 3 (updated from v3)` → remove version suffix

**The distribution-readiness test:** Read the cover, every section header, and every
sentence that begins a paragraph. If any phrase would prompt an IC member to ask
"what is v4?" or "what pre-mortem?" without context, that phrase has failed.

---

**Internal number consistency check — 🔴 CRITICAL for any deal memo:**

An IC memo fails instantly when the same metric appears with different values in
different sections. The pre-mortem skill's Section 6 ↔ Section 7 Reconciliation should
have caught these before delivery, but this check is the final backstop.

- [ ] Entry valuation / market cap — identical value used everywhere it appears
  (Executive Summary, Investment Thesis, Valuation, Risk Analysis). Flag any variance.
- [ ] Exit multiple assumption — identical value used everywhere (Valuation, Scenario
  table, Risk Analysis impact math, Recommendation). Flag any variance.
- [ ] Hold period — stated consistently as X years across every impact calculation
  and return analysis. Flag any inconsistency (e.g., "3-year hold" in one section
  and "5-year hold" in another).
- [ ] Key FY projections — base case FY exit GMV, EBITDA, and revenue. Flag any
  metric where Section 6 states $X and a different section uses $Y for the same
  FY and same metric.
- [ ] Contribution margin / conversion assumptions — if the Valuation or Returns
  Disaggregation stipulates "ad revenue is ~100% incremental margin" (or similar),
  every downstream impact calculation in Risk Analysis must apply the same rule.
  Flag any section that uses a different margin assumption without explicit
  reconciliation.
- [ ] Current-period vs. future-period metric confusion — for every metric that
  appears with a specific value, verify the period label is present and consistent
  (e.g., "$127B FY2025 GMV" not just "$127B GMV" when the same document also
  references "$159B FY2029E GMV").
- [ ] "Base case" language not used ambiguously — flag any use of "Base" or "Base
  case" that could refer to both the thesis base case and a failure scenario's
  middle-severity case. The pre-mortem skill requires Mild/Moderate/Severe or
  "Failure spectrum" language to avoid this collision; flag any surviving
  Low/Base/High labeling in Risk Analysis impact fields.

**The internal-consistency test:** For every numeric claim that appears more than
once in the document, verify: (a) same value, (b) same units, (c) same period label
(FY2025 vs. FY2029E), (d) same basis (gross vs. net, platform vs. group). Flag
every variance at 🔴 CRITICAL.

## Step 4: Investment PPTX Checks (Type B)

Run all five check categories in order. Report every issue with its exact slide number and
element (e.g., "Slide 4, chart title" or "Slide 7, table row 3").

### Check Category 1 — Brand Formatting

Cross-reference against pattern-investment-pptx SKILL.md Step 3.

**Slide dimensions:**
- [ ] All slides = 10" × 5.625" (widescreen) — flag any non-standard dimensions
- [ ] No slide uses a different aspect ratio

**Fonts:**
- [ ] All text uses `Wix Madefor Display` or `Wix Madefor Display SemiBold`
- [ ] No Arial, Calibri, or system font substitution anywhere
- [ ] Slide titles use correct weight per brand spec — flag deviations
- [ ] Body/data text uses correct size per brand spec — flag oversized or undersized text

**Colors:**
- [ ] All content slides use white (`FFFFFF`) background — flag any colored content slide background
- [ ] Title slide uses brand spec background — flag deviation
- [ ] Brand blue (`3A55FF`) used for accents and highlights only — flag overuse
- [ ] Bright blue (`009BFF`) used for charts and secondary accents — flag misuse
- [ ] No off-brand colors introduced (gradients, shadows, custom hex values not in brand spec)
- [ ] Dark text on light backgrounds only — flag any low-contrast text

### Check Category 2 — Slide Structure

**No-fly zones:**
- [ ] No content element bleeds into slide margins (minimum 0.25" from all edges)
- [ ] Title area is clear of body content overlap
- [ ] Footer/logo zone is clear of body content

**Layout integrity:**
- [ ] Every slide has a title — flag any untitled slide (except intentional divider slides)
- [ ] No overlapping text boxes
- [ ] No clipped or partially visible content elements
- [ ] Images and charts are within slide boundaries — flag any element extending beyond slide edge
- [ ] Consistent vertical alignment of recurring elements across slides (titles at same Y position)

### Check Category 3 — Content Quality

- [ ] No placeholder text (`[Insert X]`, `[Source]`, `[Date]`, `Click to add text`)
- [ ] Numbers formatted consistently: `$2.3B`, `34%`, `2.4×` — flag mixing of formats
- [ ] All percentages use consistent decimal places (e.g., all to one decimal or all whole numbers)
- [ ] No spelling errors in any visible text element
- [ ] Footnote / source lines present on all slides with data claims — flag unsourced data slides
- [ ] Source lines use consistent format and font size throughout
- [ ] No sentence-case violations in slide titles (should be sentence case, not Title Case or ALL CAPS
  unless brand spec specifies otherwise)
- [ ] All numbers in the deck are internally consistent — flag where the same metric appears
  with different values on different slides (e.g., revenue figure cited as $42M on slide 3
  and $44M on slide 7)

### Check Category 4 — Chart and Table Integrity

**Charts:**
- [ ] Every chart has a title
- [ ] Every chart has a source line in the footnote — flag unsourced charts (🔴 CRITICAL in investment context)
- [ ] Axis labels present and legible
- [ ] Legend present if multiple data series
- [ ] Y-axis starts at zero for bar charts unless deviation is deliberate and labeled
- [ ] Data labels present where values are not readable from axis alone
- [ ] Chart colors use brand palette only — flag any off-brand chart colors

**Tables:**
- [ ] Header row clearly distinguished (fill, font weight, or both)
- [ ] No merged cells that obscure data relationships
- [ ] Column widths proportional to content — no truncated text
- [ ] Alternating row shading if table has more than 4 data rows
- [ ] Every table has a title or is preceded by a clear slide section heading
- [ ] Numbers right-aligned in numeric columns — flag center or left-aligned numbers

### Check Category 5 — Narrative Flow

- [ ] Every slide title is an insight statement, not a label
  - ❌ Label: `"Competitive Landscape"`
  - ✅ Insight: `"Market consolidating around two players — white space in mid-market"`
  - Flag every label title as 🟡 WARNING
- [ ] Slide titles tell a coherent story when read in sequence — flag any title that
  contradicts or repeats the finding of the previous slide
- [ ] Executive summary / opening slide states the governing conclusion — flag if it only
  previews topics without stating a point of view
- [ ] Recommendations slide (if present) has specific, actionable items with owners and
  timelines — flag vague recommendations ("consider investing in X")
- [ ] Appendix slides clearly labeled as appendix — flag unlabeled backup slides
- [ ] No dead-end slides (slide with no logical connection to the preceding or following slide)

---

## Step 5: Produce the Issue Report

Output a single inline issue list immediately after completing all checks. Do not produce
a separate document — the report lives in chat.

### Report Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUALITY CHECK REPORT — [Document name]
[Document type] · Checked [date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUMMARY
🔴 Critical:  [X] issues
🟡 Warning:   [X] issues
🔵 Minor:     [X] issues
Total:        [X] issues

[If zero issues across all categories:]
✅ No issues found. Document meets Pattern quality standards.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ISSUES BY CATEGORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[CATEGORY NAME]
──────────────
🔴 [Location] — [Specific issue description]
   Fix: [Exact corrective action]

🟡 [Location] — [Specific issue description]
   Fix: [Exact corrective action]

🔵 [Location] — [Specific issue description]
   Fix: [Exact corrective action]

[Repeat for each category that has issues. Skip categories with zero issues.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MOST URGENT FIX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[The single most important issue to resolve before this document is used externally.
One sentence. Direct.]
```

### Location format standards

Use these exact location formats — never vague references:

| Document type | Location format |
|--------------|----------------|
| Word — body text | `Section "[H1 name]", paragraph [N]` |
| Word — heading | `H1/H2 heading: "[heading text]"` |
| Word — table | `Table [N] (under "[section name]"), row [N], column "[header name]"` |
| Word — header | `Page header` |
| Word — footer | `Page footer` |
| Word — agenda | `Agenda, row [N]: "[item name]"` |
| PPTX — slide title | `Slide [N] title` |
| PPTX — body text | `Slide [N], text box [N], line [N]` |
| PPTX — chart | `Slide [N], chart: "[chart title]"` |
| PPTX — table | `Slide [N], table row [N], column "[header name]"` |
| PPTX — footnote | `Slide [N], footnote` |

---

## Step 6: Post-Check Behaviour

After delivering the issue report:

- **Do not auto-fix anything.** Ian decides what to fix and when.
- **Do not ask follow-up questions** unless Ian responds with a specific question.
- **If zero issues found:** state this clearly and confirm the document meets Pattern
  quality standards. Do not hunt for minor issues to fill the report.
- **If Ian asks to fix a specific issue:** execute that fix precisely, then re-run the
  relevant check category only (not the full check) and confirm the fix resolved the issue.

---

## Quality Standards for This Skill

The check itself must meet these standards:

- [ ] Brand spec loaded from pattern-docx or pattern-investment-pptx before any check runs
- [ ] Every check category completed — no categories skipped silently
- [ ] Every issue has an exact location (no "somewhere in the document")
- [ ] Every issue has an exact fix (no "review and update as needed")
- [ ] Agenda page number check completed if agenda is present — this is always 🔴 CRITICAL
- [ ] Internal number consistency check completed for PPTX decks
- [ ] Zero-issue result stated explicitly if document is clean — not just an empty list
- [ ] Most urgent fix identified and stated at end of every report that has issues

---

## Integration Notes

This skill defers to the brand specs in:
- `pattern-docx` SKILL.md — for all Word document brand rules
- `pattern-investment-pptx` SKILL.md — for all PPTX brand rules

If either skill has been updated with new rules since this skill was last installed,
those updated rules take precedence over anything hardcoded here. Always load the
source skill spec before running checks — never rely on memory of brand rules.
