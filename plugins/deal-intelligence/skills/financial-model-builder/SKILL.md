---
name: financial-model-builder
description: |
  **SaaS / Operating Model Financial Template Builder**: Reads a source Excel operating model (P&L, Balance Sheet) and generates a standardized 3-tab financial model with Input Page, Financial Model Template, and Output Tab.
  - MANDATORY TRIGGERS: "build financial model", "run the template", "create financial model template", "3-tab model", "generate financial model", "financial model from P&L"
  - Use this skill whenever a user uploads an Excel file containing a P&L or income statement and wants a structured financial model built from it
  - Also triggers for: "Input Page + FMT + Output Tab", "6+6 analysis", "go-forward analysis", "SaaS model template", "turn this P&L into a model", "build a model from this", "model this out", "create a financial template", "build the pattern template model"
---

# Financial Model Template Builder

## What This Skill Does

This skill takes a user's source Excel operating model (containing a P&L/Income Statement and
optionally a Balance Sheet) and builds a standardized 3-tab financial model on top of it:

1. **Input Page** — User-configurable parameters (company name, dates, units, subsegment names)
2. **Financial Model Template (FMT)** — Period-by-period IS/BS/CF model with formula-driven columns pulling from source data
3. **Output Tab** — Annual/6+6 summary with variances, margins, and YoY analysis

The skill is **adaptive**: it detects whether the source data is monthly, quarterly, or annual,
adapts the column structure and formulas accordingly, and handles any number of cost categories.

---

## Before You Start

**Read the full blueprint** before writing any code:

```
Read: {SKILL_DIR}/references/blueprint.md
```

To find `{SKILL_DIR}`: look at the path you used to read this SKILL.md — it ends in
`.../financial-model-builder/SKILL.md`. The `{SKILL_DIR}` is that directory.

The blueprint is the complete row-by-row specification for all 3 tabs, including every formula,
formatting rule, border pattern, number format, and cross-tab dependency. Read it in full before
writing any code — it contains critical details that are easy to get wrong.

Also read the xlsx skill reference before building:
```
Read: {SKILL_DIR}/../xlsx/SKILL.md
```

---

## Workflow

### Step 1: Gather Parameters from the User

Before building, collect these inputs (ask if not provided):

| Parameter | Example | Notes |
|---|---|---|
| Source P&L tab name | "P&L", "Income Statement" | Which tab has the P&L data |
| Last actuals period | "Dec 2024", "April 2025" | Last period with actual (not forecast) data |
| Forecast period | "2 years", "3 years" | How many years of forecast columns |
| Company name | "Acme Corp" | Used in titles and headers |
| Balance Sheet tab | "Balance Sheet", or "none" | Optional — skip BS/CF if not available |

---

### Step 2: Analyze the Source File

Write a Python script to scan the source file and detect:

**1. Periodicity** — are columns monthly, quarterly, or annual?
- Check the date/header row for patterns: "Jan-24" = monthly, "Q1 2024" = quarterly, "2024" = annual
- Monthly: date serials are first-of-month or end-of-month values
- Quarterly: labels contain "Q1", "Q2", etc.

**2. Column range** — where does data start/end? Which row has period headers?

**3. Row structure** — scan for key line items in column B/D:
- Revenue / Total Revenue
- COGS / Cost of Goods Sold
- Gross Profit
- All operating expense categories (find every one — don't assume standard 5)
- EBITDA / Operating Income
- Net Income
- All subsegments under each category

**4. Units** — actual dollars, thousands, or millions? Check revenue magnitude.

**5. Category detection** — group expense lines into logical categories. The reference template
uses S&M, R&D, G&A but adapt to whatever is in the source (e.g., "Direct Costs" / "Indirect
Costs", or 10+ individual departments).

---

### Step 3: Build the Input Page

Follow the blueprint (section "TAB 1: INPUT PAGE") exactly. Key rules:

- Tab color: `#4472C4`
- **Gridlines OFF** (`showGridLines = False`)
- Pre-fill user parameters (company name, dates, source sheet name)
- Pre-fill subsegment names from what you detected in Step 2
- User-input cells: blue font (`#0000FF`), thin blue top border
- Computed cells: black font, formulas (never hardcoded values)
- Section headers: gray fill (`#DDDDDD`), thin top+bottom borders

**Adaptive category slots:** The reference has 5 categories with 8 subsegment slots each
(Revenue, COGS, S&M, R&D, G&A). If the source has more/fewer categories:
- Add category sections as needed
- Each category gets up to 8 subsegment name slots
- Update the subsegment count formulas accordingly

---

### Step 4: Build the Financial Model Template

Follow the blueprint (section "TAB 2: FINANCIAL MODEL TEMPLATE") exactly. Critical rules:

- Tab color: `#548235`
- **Gridlines OFF**
- Frozen panes: 5 rows, 7 columns
- Hidden rows 1–4 contain date infrastructure
- White fill (`#FFFFFF`) on ALL data cells

**Column structure (adaptive):**
- Monthly source: one column per month from model start through forecast end
- Quarterly source: one column per quarter
- Row 1: first-of-period dates (for INDEX/MATCH against source)
- Row 3: end-of-period dates (for SUMIFS in Output Tab)

**Formula pattern for data cells:**
```excel
=IF($D{n}="","",IFERROR(INDEX('{Source}'!$C${start}:$BD${end},
  MATCH($D{n},'{Source}'!$B${start}:$B${end},0),
  MATCH(H$1,'{Source}'!$C$4:$BD$4,0))/$B$1,0))
```

This 2D INDEX/MATCH finds the subsegment by name in the source P&L, then finds the period
column by matching the date in row 1. Adapt match row/range based on Step 2 findings.

**Totals use SUM formulas** (not source references): `=SUM(H14:H21)` for Total Revenue, etc.

**Percentage rows:** `=IF(H$22=0,0,H34/H$22)` — always guard against division by zero.

**YoY %:** Start 4 periods in (quarterly) or 12 periods in (monthly):
`=IFERROR(H22/D22-1,"")`

---

### Step 5: Build the Output Tab

Follow the blueprint (section "TAB 3: OUTPUT TAB") exactly. Most formatting-intensive tab.

- Tab color: `#BF8F00`
- **Gridlines OFF**
- Hidden date rows (2–3), hidden separator columns, hidden subsegment detail rows

**Column layout** (always this structure regardless of source periodicity):

| Col | Content | Notes |
|---|---|---|
| E–H | Annual actuals (CY years) | |
| I | Spacer | Hidden |
| J–K | N-months actual vs. N-months prior year | 6+6 split |
| L–M | $ and % variance | |
| N | Spacer | Hidden |
| O–P | "To Go" months actual vs. prior year | |
| Q–R | $ and % variance | |
| S | Spacer | Hidden |
| T | LTM (last twelve months) | |
| U | Spacer | Hidden |
| V–X | Budget / Forecast years | |

**SUMIFS formula pattern** (ALL data cells):
```excel
=SUMIFS('Financial Model Template'!$H{row}:${lastcol}{row},
  'Financial Model Template'!$H$3:${lastcol}$3,">="&{col}$2,
  'Financial Model Template'!$H$3:${lastcol}$3,"<="&{col}$3)
```

**Row structure must include ALL segments** — not just summary totals. Every subsegment,
category total, gross profit, EBITDA line, and cash flow item needs data formulas.

**Variance columns:**
- $ Variance: `=K{n}-J{n}` (or P-O for "To Go")
- % Variance: `=IFERROR(IF(ABS(L{n}/J{n})>5,"n.m.",L{n}/J{n}),"")`
- YoY %: `=IFERROR(IF(ABS(V{n}/H{n}-1)>5,"n.m.",V{n}/H{n}-1),"")`
- Values >500% display as "n.m." (not meaningful)

---

### Step 6: Apply Formatting

Read the blueprint's formatting sections carefully. Most critical rules:

**Borders — full width:**
- FMT: All TB borders on total rows span column C through last data column
- Output Tab: TB borders on total rows span columns B through U (including spacer columns)
- Output Tab: Vertical borders on columns J (left thin), L (left hair), M (right thin),
  Q (left hair), R (right thin) — on EVERY row from 6 through last data row

**Revenue row special treatment (Output Tab):**
- TAN fill (`#E0DBD7`) on data columns only (B–H, J–M, O–R, T) — NOT on spacer columns

**Number formats:**

| Type | Format |
|---|---|
| Subsegment data | `_(#,##0.0_)_%;(#,##0.0)_%;_("–"_)_%;_(@_)_%` |
| Total dollar rows | `_([$]#,##0_)_%;([$]#,##0)_%;_("–"_)_%;_(@_)_%` |
| Percentage rows | `_(#,##0.0%_);(#,##0.0%);_("–"_)_%;_(@_)_%` |
| Output Tab dollars | `_(#,##0.0_)_%;(#,##0.0)_%;_("–"_)_%;_(@_)_%` |
| Output Tab percentages | `_(#,##0.0%_);(#,##0.0%);_("–"_)_%;_(@_)_%` |

---

### Step 7: Recalculate and Verify

After saving:

1. **Recalculate:**
```bash
python scripts/recalc.py output.xlsx 120
```

2. **Check for errors** in the 3 new tabs only (ignore pre-existing source tab errors)

3. **Spot-check values:** Compare 2–3 FMT cells against the source P&L to confirm formulas
   pull correctly

4. **Verify formatting:** Confirm gridlines off, borders on totals, fills correct

5. Fix any errors and recalculate again before delivery

---

### Step 8: Deliver

Save to outputs folder and provide a download link.

---

## Common Pitfalls

1. **Column offset errors:** When mapping FMT columns to source P&L columns, double-check
   the offset. The INDEX/MATCH with row 1 dates handles this — but verify with a spot check.

2. **Missing Output Tab formulas:** Every segment and subsegment needs SUMIFS data formulas —
   not just labels.

3. **Gridlines off = borders critical:** Any missing border creates a visible gap. Full-width
   borders on total rows and consistent vertical borders on the Output Tab are essential.

4. **Division by zero:** Always wrap percentage formulas in IF or IFERROR guards.

5. **`=-+` syntax:** LibreOffice doesn't support `=-+value`. Use `=-value` instead.

6. **Variance "n.m." handling:** When variance percentage exceeds 500% (|x| > 5), display
   "n.m." instead of the number.

7. **Adaptive categories:** If the source has more than 5 expense categories, add them —
   don't force data into S&M / R&D / G&A if that's not what the source uses.
