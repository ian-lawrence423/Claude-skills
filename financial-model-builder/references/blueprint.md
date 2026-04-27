# SaaS Financial Model Builder — Blueprint

> ⚠️ **THIS IS THE AUTHORITATIVE SPEC** — Every formula, label column, row number, color, border, font size, column width, and number format below is extracted directly from `Financial Template (Claude).xlsx`. Do not substitute, approximate, or simplify. Reproduce exactly.

## PURPOSE
This file is a company-agnostic blueprint for building an M&A analysis toolkit. Given any company's raw Income Statement and Balance Sheet data, Claude reads this spec to produce three interconnected tabs:
1. **Input Page** — Auto-populated configuration layer that maps the target company's chart of accounts into the standard template structure
2. **Financial Model Template** — Monthly IS/BS/CF model with date-driven columns
3. **Output Tab** — Annual/6+6 summary for investment memos, pulling from the Financial Model Template

## WORKFLOW: How Claude Uses This File
1. User provides raw IS + BS data (uploaded file or pasted into a sheet)
2. Claude reads the source data and identifies: company name, currency, date range, fiscal year, revenue streams, cost categories, and OpEx groupings
3. Claude populates the Input Page by mapping source line items into the standard category structure
4. Claude builds/refreshes the Financial Model Template and Output Tab from that configuration
5. All three tabs stay dynamically linked — changing the Input Page updates everything downstream

## DESIGN PRINCIPLES
- **Company-agnostic**: No hardcoded company names or line items. All company-specific data is entered in blue input cells.
- **Dynamic IS categories**: The Income Statement section supports any OpEx breakdown (not just S&M/R&D/G&A). Claude infers the right categories from the source data.
- **8-slot maximum per category**: Each IS category has up to 8 subsegment slots. Unused slots stay blank.
- **Standardized BS/CF**: Balance Sheet and Cash Flow use a fixed template structure regardless of company.

## PREREQUISITES
Before building these tabs, the workbook must contain a **source data sheet** (default: "P&L") with:
- Monthly columns starting at column H, with dates in a header row (row 4 in the template's P&L)
- Row labels in column B or D matching the subsegment names defined on the Input Page
- Income Statement line items organized by category (Revenue, COGS, OpEx subcategories)

---

## TAB 1: INPUT PAGE

### Tab Properties
- **Tab color:** `#4472C4`
- **Gridlines:** OFF (`showGridLines = False`)
- **Frozen panes:** None

### Column Widths (exact)

| Column | Width (chars) |
|--------|--------------|
| A | 2.78 |
| B | 32.44 |
| C | 2.78 |
| D | 30.55 |
| E | 18.55 |
| F | 41.66 |

### Row Heights
- Row 2: **17.4 pt**
- All other rows: default

### Font Rules (complete)

| Element | Font | Size | Bold | Italic | Color |
|---------|------|------|------|--------|-------|
| Title B2 | Arial | 14pt | Yes | No | `#FFFFFF` (white) |
| Subtitle B3 | Arial | 9pt | No | Yes | `#808080` (gray) |
| Section headers (B5, B12, B23, B36, B92) | Arial | 10pt | Yes | No | `#000000` |
| Subsegment category headers (B40, B50, B60, B70, B80) | Arial | 10pt | Yes | No | `#FFFFFF` (white — on blue fill) |
| Row label cells (B7–B38 labels, B93–B97) | Arial | 10pt | No | No | `#000000` |
| Bold input labels (B7, B17, B20, B38) | Arial | 10pt | Yes | No | `#000000` |
| Blue input cells — bold (D7, D17, D20, D38) | Arial | 10pt | Yes | No | `#0000FF` |
| Blue input cells — regular (D8, D9, D15, D18) | Arial | 10pt | No | No | `#0000FF` |
| Computed cells (D10, D14, D16, D21, D25–D31, D33, D93–D97) | Arial | 10pt | No | No | `#000000` |
| Row number cells (B41–B88) | Arial | 9pt | No | No | `#808080` |
| E-column helper text (E15, E17, E20, E21) | Arial | 9pt | No | Yes | `#000000` |
| F-column guidance notes | Arial | 9pt | No | Yes | `#808080` |

### Fill Colors (exact)

| Fill | Hex | Applied To |
|------|-----|-----------|
| Black | `#000000` | Row 2 full band (B2:F2) — title bar |
| Light gray | `#DDDDDD` | Section header rows: B5:F5, B12:F12, B23:F23, B36:F36, B92:F92 |
| Blue | `#4472C4` | Subsegment category rows: B40:F40, B50:F50, B60:F60, B70:F70, B80:F80 |
| None | — | All other cells |

### Borders (exact)

| Style | Color | Applied To |
|-------|-------|-----------|
| `thin` top + bottom | `#000000` | Section header bands: B:F of rows 5, 12, 23, 36, 92 |
| `thin` bottom | `#000000` | Subsegment category rows B:F (rows 40, 50, 60, 70, 80) |
| `thin` bottom | `#0000FF` (blue) | User input cells: D8, D9, D15, D17, D18 |
| `thin` bottom | `#000000` | First subsegment slot in each group: D41, D51, D61, D71, D81 |
| `thin` bottom | `#000000` | Computed result cells: D10, D21, D27, D31, D33, D38 |
| `dotted` top | `#B0B0B0` (light gray) | Subsequent subsegment slots: D42–D47, D52–D57, D62–D67, D72–D77, D82–D87 |
| `dotted` top + bottom | `#B0B0B0` | Last slot in each group: D48, D58, D68, D78, D88 |

### Alignment

| Location | Horizontal |
|----------|-----------|
| B column (labels) | left (default) |
| D column (values) | left (default) |
| B41–B88 (row numbers) | center |
| D93–D97 (subsegment counts) | center |
| F column (hints) | left (default) |

### Number Formats (exact)

| Format String | Applied To |
|---------------|-----------|
| `#,##0` | D10 (Units Divisor) |
| `mm/dd/yyyy` | D14, D16, D17, D20, D27, D29, D30, D31 (all date cells) |
| `0` | D15 (FY Start Month), D18 (Forecast Period), D21 (Months Actual), D26 (Current FY) |

---

### Layout (Row-by-Row)

#### Rows 2–3: Title
- **B2:** "Model Input Page" — Arial 14pt bold white, black fill (#000000), row height 17.4pt
- **B3:** "All blue cells are user inputs — update these to drive the Financial Model and 6+6 Summary" — Arial 9pt italic gray (#808080)

#### Rows 5–10: Company Information
- **B5:F5:** "Company Information" — section header (gray #DDDDDD fill, thin top+bottom borders, Arial 10pt bold black)
- **B7:** "Company Name" → **D7:** user input (blue bold, thin black bottom border). **F7:** `"← Enter company name"`
- **B8:** "Currency" → **D8:** user input (blue, thin blue bottom border). **F8:** `"← e.g., USD, EUR, CZK"`
- **B9:** "Units Display" → **D9:** user input (blue, thin blue bottom border). **F9:** `"← Thousands, Millions, or Actual"`
- **B10:** "Units Divisor" → **D10:** `=IF(D9="Thousands",1000,IF(D9="Millions",1000000,1))` — black text, thin black bottom border, format `#,##0`. **F10:** `"← Auto-calculated from Units Display"`

#### Rows 12–21: Dates & Periods
- **B12:F12:** "Dates & Periods" — section header
- **B14:** "Today's Date" → **D14:** `=TODAY()` — format `mm/dd/yyyy`
- **B15:** "Fiscal Year Start Month" → **D15:** user input (blue, thin blue bottom border). Format `0`. **E15:** `=TEXT(DATE(2025,D15,1),"MMMM")`
- **B16:** "Model Start Date" → **D16:** `=DATE(YEAR(D17)-4,D15,1)` — **4 years before last actuals FY start**, to cover all Output Tab historical columns (E, F, G, H). Format `mm/dd/yyyy`.
- **B17:** "Last Date of Actuals" → **D17:** user input (blue bold, thin blue bottom border). Format `mm/dd/yyyy`. **E17:** `=TEXT(D17,"MMMM YYYY")`
- **B18:** "Forecast Period (Years)" → **D18:** user input (blue, thin blue bottom border). Format `0`. Example: 3
- **B20:** "6+6 Split Month" → **D20:** user input (blue bold). **E20:** `=TEXT(D20,"MMMM YYYY")`
- **B21:** "Months Actual (6+6)" → **D21:** `=DATEDIF(DATE(YEAR(D20),D15,1),D20,"M")+1` — thin black bottom border, format `0`. **E21:** `=D21&" + "&(12-D21)&" Split"`

#### Rows 23–33: Derived / Computed Values
- **B23:F23:** "Derived / Computed Values" — section header
- **B25:** "Units Label" → **D25:** `="$ "&D9`
- **B26:** "Current Fiscal Year" → **D26:** `=IF(MONTH(D14)>=D15,YEAR(D14),YEAR(D14)-1)` — format `0`
- **B27:** "Last Complete FY End" → **D27:** `=EOMONTH(DATE(D26,D15,1),-1)` — thin black bottom border, format `mm/dd/yyyy`
- **B29:** "6+6 Actual Start" → **D29:** `=IF(MONTH(D20)>=D15,DATE(YEAR(D20),D15,1),DATE(YEAR(D20)-1,D15,1))` — format `mm/dd/yyyy`
- **B30:** "6+6 Forecast Start" → **D30:** `=D20+1` — format `mm/dd/yyyy`
- **B31:** "6+6 Forecast End" → **D31:** `=EOMONTH(D27,12)` — one full year after Last Complete FY End; used by Output Tab P3 as the current-year "To Go" end date. Thin black bottom border, format `mm/dd/yyyy`.
- **B33:** "Analysis Title" → **D33:** `=D7&" - CY'"&D26&" Go-Forward Analysis"` — thin black bottom border. **F33:** `"← Auto-generated title for Output Tab"`

#### Rows 36–88: Income Statement Line Items (DYNAMIC CATEGORIES)
- **B36:F36:** "Income Statement Line Items" — section header
- **B37:** "Type subsegment names below. Leave blank rows empty. These drive the Financial Model structure." — Arial 9pt italic gray
- **B38:** "Source Sheet" → **D38:** user input (blue bold, thin black bottom border). Example: "P&L"

##### Subsegment Category Blocks
Each category follows this **10-row pattern**:
- **Header row (B40, B50, B60, B70, B80):** Category name in white bold Arial 10pt on `#4472C4` fill, thin black bottom border on full B:F band
- **Number column (B41–B48, etc.):** "1"–"8" in Arial 9pt gray, center-aligned
- **Input column D:** First slot has thin black bottom border; subsequent slots have dotted gray (`#B0B0B0`) top border; last slot has dotted gray top+bottom borders
- **F41 guidance note:** "← Must match row label in source sheet" — Arial 9pt italic gray

**Revenue Subsegments (rows 40–48):**
- B40: "Revenue Subsegments" (white on blue); D41–D48: user input names

**COGS Subsegments (rows 50–58):**
- B50: "COGS Subsegments" (white on blue); D51–D58: user input names

**OpEx Category Blocks (rows 60–88) — DYNAMIC:**
The default template shows 3 OpEx categories. Claude replaces generic placeholders with categories inferred from the source data (e.g., "S&M Subsegments", "R&D Subsegments", "G&A Subsegments").
- **B60:** Category 1 header; D61–D68: user input names
- **B70:** Category 2 header; D71–D78: user input names
- **B80:** Category 3 header; D81–D88: user input names

**When source data has more or fewer OpEx categories:** Add or remove 10-row category blocks. The 10-row-per-block pattern ensures predictable row offsets throughout FMT and Output Tab.

#### Rows 90–97: Subsegment Counts
- **B92:F92:** "Subsegment Counts (auto)" — section header (gray fill, thin borders)
- **B93:** "Revenue" → **D93:** `=COUNTA(D41:D48)` — center-aligned
- **B94:** "COGS" → **D94:** `=COUNTA(D51:D58)` — center-aligned
- **B95:** (Cat 1 label) → **D95:** `=COUNTA(D61:D68)` — center-aligned
- **B96:** (Cat 2 label) → **D96:** `=COUNTA(D71:D78)` — center-aligned
- **B97:** (Cat 3 label) → **D97:** `=COUNTA(D81:D88)` — center-aligned

### Input Page Cell Reference Map

| Cell | Contents | Used By |
|------|----------|---------|
| D10 | Units Divisor | FMT B1 |
| D15 | FY Start Month | Date generation |
| D16 | Model Start Date | FMT column generation |
| D17 | Last Date of Actuals | FMT Actual/Forecast flag |
| D18 | Forecast Period (Years) | FMT column end |
| D20 | 6+6 Split Month | Output Tab K3, date ranges |
| D25 | Units Label | Output Tab B6 |
| D26 | Current Fiscal Year | Output Tab columns |
| D27 | Last Complete FY End | Output Tab H3 |
| D29 | 6+6 Actual Start | not directly referenced by Output Tab — H2/J2 derived via EOMONTH |
| D30 | 6+6 Forecast Start | Output Tab P2 |
| D31 | 6+6 Forecast End (= EOMONTH(D27,12)) | Output Tab P3 |
| D33 | Analysis Title | Output Tab B5 |
| D38 | Source Sheet name | FMT data pull |
| D41–D48 | Revenue subsegment names | FMT D14–D21 + Output Tab D9–D16 |
| D51–D58 | COGS subsegment names | FMT D26–D33 + Output Tab D20–D27 |
| D61–D68 | OpEx Cat 1 subsegment names | FMT D41–D48 + Output Tab D34–D41 |
| D71–D78 | OpEx Cat 2 subsegment names | FMT D52–D59 + Output Tab D45–D52 |
| D81–D88 | OpEx Cat 3 subsegment names | FMT D63–D70 + Output Tab D56–D63 |

---

## TAB 2: FINANCIAL MODEL TEMPLATE

### Tab Properties
- **Tab color:** `#548235`
- **Gridlines:** OFF (`showGridLines = False`)
- **Frozen panes:** `H92` (freeze_panes = 'H92') — freezes columns A–G and rows 1–91

### Column Widths (exact)

| Column | Width (chars) | Notes |
|--------|--------------|-------|
| A | 1.78 | narrow spacer |
| B–E | default | label/indent area |
| F | 26.78 | wide label column (structural section headers only — blank in data rows) |
| G | 1.78 | **hidden** (spacer between labels and data) |
| H | 11.78 | first monthly data column |
| I onward | 11.78 | all monthly data columns |

### Hidden Rows and Columns
- **Hidden rows:** 1–4 (date infrastructure / helper rows)
- **Hidden column:** G (spacer between label area and data)

### Font Rules
- **Universal:** Arial 9pt throughout
- **Aptos Narrow 11pt:** Column D subsegment name cells (D14–D21, D26–D33, D41–D48, D52–D59, D63–D70) — visually distinguishes subsegment names from structural labels
- Bold: section title (row 7), section headers (rows 12, 112, 175), all total/subtotal rows
- Italic: all % of Revenue rows, all YoY % rows, assumption rows
- All text black (`#000000`)

### Fill Colors
- **White** (`#FFFFFF`): Row 7 title band and all data rows H onward (apply explicitly)
- No color-coding of actuals vs. forecast columns — both are white

### Borders (exact)

| Style | Sides | Applied To |
|-------|-------|-----------|
| `thin` | bottom | Row 7 (A–G): "Financial Model" section title |
| `thin` | bottom | Row 12 (B–H): "Income Statement" section header |
| `thin` | bottom | Row 98: "Assumptions" header |
| `thin` | top + bottom | **Major total rows:** 22 (Total Revenue), 34 (COGS), 37 (Gross Profit), 74 (Total OpEx), 78 (EBIT), 86 (EBITDA), 94 (EBT), 124 (Total Assets), 134 (Total Liabilities), 138 (Total Liab & Equity) |
| `thin` | top only | **Subtotal rows:** 49 (Cat 1 total), 60 (Cat 2 total), 71 (Cat 3 total), 84 (D&A total), 92 (Other), 120 (Total Current Assets), 130 (Total Current Liabilities), 141 (NWC header), 145, 151, 153, 172, 184 (FCF), 189 (Total Financing CF), 191 (Net Change in Cash) |

Borders on total rows span **full width** from column C through the last data column.

### Alignment
- Data columns H onward: `horizontal: right`
- Date header rows 1–2, 9: `horizontal: right`
- Label columns C, D, E: left (default)

### Number Formats (exact)

| Format String | Applied To |
|---------------|-----------|
| `mm-dd-yy` | Row 1 hidden (month start dates) |
| `mmm-yy` | Row 2 visible date headers |
| `m/d/yyyy;@` | Row 3 hidden (EOMONTH date serials for SUMIFS matching) |
| `_(#,##0.0_)_%;(#,##0.0)_%;_("–"_)_%;_(@_)_%` | All subsegment detail rows (14–21, 26–33, 41–48, 52–59, 63–70, 82–83, 90–91) |
| `_([$]#,##0_)_%;([$]#,##0)_%;_("-"_)_%;_(@_)_%` | All total / subtotal dollar rows |
| `_(#,##0.0%_);(#,##0.0%);_("–"_)_%;_(@_)_%` | All % of Revenue rows and YoY % rows |

---

### Label Column Structure

> Labels are distributed across columns A–E by indent level:
> - **Column A:** Major title ("Financial Model" — row 7)
> - **Column B:** Top-level section headers ("Income Statement", "Balance Sheet Statement", "Cash Flow Statement")
> - **Column C:** Structural totals ("Total Revenue", "COGS", "Gross Profit", "Total Operating Expense", "EBIT", "EBITDA", "EBT", "Total Assets", "Total Liabilities", "Total Liab & Equity", "Net working Capital")
> - **Column D:** Subsegment name links (IF formulas from Input Page) AND OpEx category total labels (e.g., "Sales & Marketing", "R&D", "G&A") AND BS/CF line item labels
> - **Column E:** Indented annotation rows ("% Total Revenue", "YoY %", "(--) Taxes", etc.) and indented BS items ("Cash", "Investment Account", etc.)

### Row Structure

#### Hidden Infrastructure (Rows 1–4)
- **Row 1 (hidden):** B1 = `='Input Page'!D10` (units divisor). H1 = first month start date serial. I1 = `=H2+1`, J1 = `=I2+1`, etc. — each column's row 1 holds the **start date** of that month (used by INDEX/MATCH to match source date headers)
- **Row 2 (hidden):** H2 = `=EOMONTH(H1,0)`, I2 = `=EOMONTH(I1,0)`, etc. — EOMONTH date serials, format `mmm-yy`
- **Row 3 (hidden):** B3 = "DatePeriod". H3 = same EOMONTH serials as row 2, format `m/d/yyyy;@` (used by SUMIFS in Output Tab)
- **Row 4:** spare / blank

#### Header Band (Rows 7–9, white fill)
- **Row 7:** A7 = "Financial Model" — bold, white fill, thin bottom border
- **Row 8:** blank spacer (white fill)
- **Row 9:** H9 onward = month-end date labels (format `mmm-yy`, bold, right-aligned, white fill)

#### Income Statement (Rows 12–96)
- **Row 12:** B12 = "Income Statement" — bold, thin bottom border

**Revenue Subsegments (rows 14–21, up to 8 slots):**
- D14: `=IF('Input Page'!D41="","",'Input Page'!D41)` — Aptos Narrow 11pt
- D15–D21: same pattern linking to Input Page D42–D48
- **H14 onward (actuals):**
  ```
  =IF($D14="","",IFERROR(INDEX('{Source}'!$C${start}:$BD${end},
    MATCH($D14,'{Source}'!$B${start}:$B${end},0),
    MATCH(H$1,'{Source}'!$C$4:$BD$4,0))/$B$1,0))
  ```
  - `H$1` = month start date (row 1) — matches source sheet date header row (adjust `$C$4` to actual source date row)
  - `$B$1` = units divisor; adjust source sheet name and row ranges to match actual source data
- Row height: 14.4pt; format: `_(#,##0.0_)_%;(#,##0.0)_%;_("–"_)_%;_(@_)_%`

**Row 22: Total Revenue**
- C22: "Total Revenue" — bold; H22: `=SUM(H14:H21)`; border: thin top + bottom; format: accounting

**Row 23: YoY %**
- E23: "YoY %" — italic; H23 (starts 12 columns in): `=IFERROR(H22/D22-1,"")` ; row height: 11.4pt

**Rows 24–25:** spacer (4.95pt each)

**COGS Subsegments (rows 26–33, up to 8 slots):**
- D26–D33: same link pattern → Input Page D51–D58 — Aptos Narrow 11pt
- Data formula: same INDEX/MATCH pattern — adjust row range to COGS rows in source

**Row 34: COGS**
- C34: "COGS" — bold; H34: `=SUM(H26:H33)`; border: thin top + bottom; format: accounting

**Row 35: % Total Revenue** — E35; italic, 11.4pt; `=H34/H$22`

**Row 36:** spacer 4.95pt

**Row 37: Gross Profit**
- C37: "Gross Profit" — bold; H37: `=H22-H34`; border: thin top + bottom; format: accounting

**Row 38: % Total Revenue** — E38; italic; `=H37/H$22`

**Rows 39–40:** spacers

**OpEx Category 1 Subsegments (rows 41–48):**
- D41–D48: link pattern → Input Page D61–D68 — Aptos Narrow 11pt
- Data formula: same INDEX/MATCH pattern — adjust row range to Category 1 rows in source

**Row 49: Category 1 Total (e.g., "Sales & Marketing")**
- D49: hardcoded category total label (NOT pulled from Input Page) — bold
- H49: `=SUM(H41:H48)`; border: thin top; format: accounting

**Row 50: % Total Revenue** — E50; italic; `=H49/H$22`; row height 11.4pt

**Row 51:** spacer 4.95pt

**OpEx Category 2 Subsegments (rows 52–59):**
- D52–D59: link pattern → Input Page D71–D78 — Aptos Narrow 11pt

**Row 60: Category 2 Total (e.g., "R&D")**
- D60: hardcoded category total label — bold; H60: `=SUM(H52:H59)`; border: thin top

**Row 61: % Total Revenue** — E61; italic; `=H60/H$22`

**Row 62:** spacer 4.95pt

**OpEx Category 3 Subsegments (rows 63–70):**
- D63–D70: link pattern → Input Page D81–D88 — Aptos Narrow 11pt

**Row 71: Category 3 Total (e.g., "G&A")**
- D71: hardcoded category total label — bold; H71: `=SUM(H63:H70)`; border: thin top

**Row 72: % Total Revenue** — E72; italic; `=H71/H$22`

**Row 73:** spacer

**Row 74: Total Operating Expense**
- C74: "Total Operating Expense" — bold
- **H74: `=H71+H60+H49`** — **OpEx categories only; COGS is NOT included here**
- Border: thin top + bottom

**Row 75: % Total Revenue** — E75; italic; `=H74/H$22`
**Row 76: YoY %** — E76; italic

**Row 77:** spacer

**Row 78: EBIT**
- C78: "EBIT" — bold
- **H78: `=H37-H74`** — **Gross Profit minus Total Operating Expense** (not Revenue minus everything)
- Border: thin top + bottom

**Row 79: % Total Revenue** — E79; italic; `=H78/H$22`
**Row 80: YoY %** — E80; italic

**Row 81:** spacer

**Row 82:** D82 = "Depreciation" — detail; format `_(#,##0.0_)_%;(#,##0.0)_%;_("–"_)_%;_(@_)_%`
**Row 83:** D83 = "Amortization" — detail; format `_(#,##0.0_)_%;(#,##0.0)_%;_("–"_)_%;_(@_)_%`
**Row 84:** D84 = "Depreciation & Amortization" — bold, thin top border; H84: `=H82+H83`

**Row 85:** spacer

**Row 86: EBITDA**
- C86: "EBITDA" — bold; H86: `=H84+H78`; border: thin top + bottom

**Row 87: % Total Revenue** — E87; italic; `=H86/H$22`
**Row 88: YoY %** — E88; italic

**Row 89:** spacer

**Row 90:** D90 = "Other Income" — detail
**Row 91:** D91 = "Other Expense" — detail
**Row 92:** D92 = "Other (Income)/Expense" — thin top border; H92: `=SUM(H90:H91)`

**Row 93:** spacer

**Row 94: EBT**
- C94: "EBT" — bold; H94: `=H78-H92`; border: thin top + bottom

**Row 95: % Total Revenue** — italic
**Row 96: YoY %** — italic

#### Assumptions Section (Rows 98–107)
- Row 98: C98 = "Assumptions" — bold, thin bottom border
- Row 99: D99 = "% of Revenue" — italic
- Rows 101–107: COGS%, Category 1%, Category 2%, Category 3%, Total OpEx%, EBIT%, EBITDA% — each `=IF(H22=0,0,H{total}/H22)`; italic

#### Balance Sheet (Rows 112+)
- Row 112: B112 = "Balance Sheet Statement" — bold, thin top+bottom border

**Assets:**
- E115 = "Cash"; H115 = `='Balance Sheet'!I12/$B$1`
- E116 = "Investment Account"; H116 = `='Balance Sheet'!I14/$B$1`
- D117 = "Cash & Equivalent" — bold, thin top border; H117 = `=SUM(H115:H116)`
- D118 = "Accounts receivable"; H118 = `='Balance Sheet'!I25/$B$1`
- D119 = "Pre-paid & other current"; H119 = `='Balance Sheet'!I42/$B$1`
- D120 = "Total Current Assets" — bold, thin top border; H120 = `=SUM(H117:H119)`
- D122 = "PP&E, Net"; H122 = `='Balance Sheet'!I58/$B$1`
- D123 = "Other LT Assets"; H123 = `='Balance Sheet'!I67/$B$1`
- **C124 = "Total Assets"** — bold, thin top+bottom border; **H124 = `=H122+H120+H123`**

**Liabilities:**
- D126 = "Accounts Payable"; H126 = `='Balance Sheet'!I74/$B$1+'Balance Sheet'!I77/$B$1`
- D127 = "Accrued Payables"; H127 = `='Balance Sheet'!I99/$B$1`
- D128 = "Accrued Expenses"; H128 = `='Balance Sheet'!I116/$B$1`
- D129 = "Deferred Revenue"; H129 = `='Balance Sheet'!I107/$B$1`
- **D130 = "Total Current Liabilities"** — bold, thin top+bottom border; H130 = `=SUM(H126:H129)`
- D132 = "Lease Liability"; H132 = `='Balance Sheet'!I121/$B$1`
- D133 = "Convertible Note"; H133 = `='Balance Sheet'!I123/$B$1`
- C134 = "Total Liabilities" — bold, thin top+bottom border; H134 = `=H130+SUM(H132:H133)`

**Equity:**
- D136 = "Capital Contribution"; H136 = `='Balance Sheet'!I155/$B$1`
- D137 = "Retained"; H137 = `='Balance Sheet'!I156/$B$1+'Balance Sheet'!I158/$B$1`
- C138 = "Total Liab & Equity" — bold, thin top+bottom border; H138 = `=H134+SUM(H136:H137)`
- D139 = "check?" — balance check; H139 = `=+H124-H138` (should be 0)

#### Working Capital Analysis (Rows 141–153)
- Row 141: C141 = "Net working Capital" — bold, thin bottom border
- Row 142: spacer 4.95pt
- D143 = "Accounts receivable"; H143 = `=H118`
- D144 = "Pre-paid & other current"; H144 = `=H119`
- D145 = "Current Assets (ex. Cash)" — subtotal, thin top border; H145 = `=SUM(H143:H144)`
- Row 146: spacer
- D147 = "Accounts Payable"; H147 = `=H126`
- D148 = "Accrued Payables"; H148 = `=H127`
- D149 = "Accrued Expenses"; H149 = `=H128`
- D150 = "Deferred Revenue"; H150 = `=H129`
- D151 = "Current Liabilities" — subtotal, thin top border; H151 = `=SUM(H147:H150)`
- Row 152: spacer
- D153 = "Net Working Capital" — bold, thin top+bottom border; H153 = `=H145-H151`
  - **Note:** G153 = prior-period NWC (column G = one month back), used by CF: `=-(H153-G153)`

#### PP&E Section (Rows 155–157)
- Row 155: spacer
- D156 = "PP&E" — bold; H156 = `=H122`. **G156 = prior period PP&E** (used by CF Capex)
- E157 = "% of Revenue" — italic; H157 = `=H156/H22`

#### Other Long-Term Assets/Liabilities (Rows 160–172)
- D160 = "Other Long-Term Assets" (underlined)
- E161 = "Total Assets"; H161 = `=H124`
- E162 = "(--) Current Assets"; H162 = `=H120`
- E163 = "(--) PP&E"; H163 = `=H122`
- E164 = "Other Long-Term Assets"; H164 = `=H161-H162-H163`. **G164 = prior period value**
- D166 = "Other Long-Term Liabilities" (underlined)
- E167 = "Total Liabilities"; H167 = `=H134`
- E168 = "(--) Current Liabilities"; H168 = `=H130`
- E169 = "(--) Convertible Note / Debt"; H169 = `=H133`
- E170 = "Other Long-Term Liabilities"; H170 = `=H167-H168-H169`. **G170 = prior period value**
- E172 = "Long Term Assets, Net" — bold, thin top border; H172 = `=H164-H170`

#### Cash Flow Statement (Rows 175–194)
- Row 175: B175 = "Cash Flow Statement" — bold, thin top+bottom border
- Rows 176–177: spacers
- D178 = "EBITDA"; H178 = `=H86`
- E179 = "(--) Taxes"; H179 = `=0`
- E180 = "(--) Interest Expense, net"; H180 = `=-H92`
- E181 = "(--) Change in Working Capital"; H181 = `=-(H153-G153)` (negative of NWC delta)
- E182 = "(--) Capex"; H182 = `=-(H156-G156)` (negative of PP&E delta)
- E183 = "(--) Other LT Assets, Net"; H183 = `=-((H164-H170)-(G164-G170))`
- D184 = "Free Cash Flow" — bold, thin top+bottom border; H184 = `=SUM(H178:H183)`
- Rows 185–186: spacers
- E187 = "Debt raise, net"; H187 = `=H133-G133`
- E188 = "Equity raise, net"; H188 = `=H136-G136`
- E189 = "Total Financing Cash Flow" — bold, thin top border; H189 = `=SUM(H187:H188)`
- Row 190: spacer
- D191 = "Net Change in Cash" — bold, thin top+bottom border; H191 = `=H184+H189`
- Row 192: spacer
- D193 = "Beginning Cash"; H193 = `=G117` (prior period Cash & Equivalent)
- D194 = "Ending Cash"; H194 = `=H193+H191`

---

## TAB 3: OUTPUT TAB

### Tab Properties
- **Tab color:** `#BF8F00`
- **Gridlines:** OFF (`showGridLines = False`)
- **Frozen panes:** None

### Column Widths (exact)

| Column | Width (chars) | Hidden? |
|--------|--------------|---------|
| A | 1.89 | No |
| B | 1.78 | No |
| C | 3.33 | No |
| D | 21.33 | No (label column) |
| E | 13.89 | No |
| F | 13.89 | No |
| G | 13.89 | No |
| H | 13.89 | No |
| I | 0.89 | **Yes** (spacer) |
| J | 13.89 | No |
| K | 13.89 | No |
| L | 13.89 | No |
| M | 13.89 | No |
| N | 0.89 | **Yes** (spacer) |
| O | 13.89 | No |
| P | 13.89 | No |
| Q | 13.89 | No |
| R | 13.89 | No |
| S | 0.89 | **Yes** (spacer) |
| T | 13.89 | No |
| U | 0.89 | **Yes** (spacer) |
| V | 13.89 | No |
| W | 13.89 | No |
| X | 13.89 | No |
| Y | 0.89 | **Yes** (spacer) |
| Z | 13.89 | No |

**Hidden columns: I, N, S, U, Y** — set width 0.89 AND hidden=True.

### Row Heights (exact)

| Row | Height (pt) |
|-----|------------|
| Row 7 (period labels) | 17.4 |
| Row 33 (section spacer) | 4.95 |
| Row 44 (section spacer) | 4.95 |
| Row 55 (section spacer) | 4.95 |
| Row 75 (CF header) | 15.0 |
| All other rows | default |

### Font Rules (complete)

| Element | Font | Size | Bold | Italic | Underline | Color |
|---------|------|------|------|--------|-----------|-------|
| Title row 5 | Arial | 9pt | Yes | No | No | `#FFFFFF` |
| Column group headers row 6 | Arial | 9pt | Yes | No | No | `#000000` |
| Period label headers row 7 | Arial | 9pt | Yes | No | `singleAccounting` | `#000000` |
| Units label B6 | Arial | 9pt | No | Yes | No | `#000000` |
| All total rows (17, 28, 31, 42, 53, 64, 67, 71, 77, 83) | Arial | 9pt | Yes | No | No | `#000000` |
| All % rows (29, 32, 43, 54, 65, 68, 72, 84) | Arial | 9pt | No | Yes | No | `#000000` |
| All subsegment label rows | Arial | 9pt | No | No | No | `#000000` |
| YoY % rows (18, 69, 73) | Arial | 9pt | No | Yes | No | `#000000` |

**Row 7 underline = `singleAccounting`** (apply via openpyxl `Font(underline='singleAccounting')`).

### Fill Colors (exact)

| Fill | Hex | Applied To |
|------|-----|-----------|
| Gray | `#DDDDDD` | Rows 2 and 3 (date bands, full width) |
| Black | `#000000` | Row 5 full band B5:Z5 (title bar) |
| Gray | `#DDDDDD` | Row 6 full band (column group headers) |
| Tan | `#E0DBD7` | Row 17 ONLY (Revenue total) — ALL data columns E–X including variance cols, but NOT spacer cols I/N/S/U/Y |
| None | — | All other rows |

### Borders (exact — critical)

**Continuous vertical borders** from row 6 (or 7) through last data row (row 84):

| Style | Side | Column | Rows |
|-------|------|--------|------|
| `thin` | left | J | 6–84 |
| `hair` | left | L | 7–84 |
| `thin` | right | M | 6–84 |
| `thin` | left | O | 6–84 |
| `hair` | left | Q | 7–84 |
| `thin` | right | R | 6–84 |

**Horizontal borders on total/section rows:**

| Style | Sides | Rows |
|-------|-------|------|
| `thin` | top + bottom | 17 (Revenue), 31 (Gross Profit), 67 (Total OpEx), 71 (EBITDA) |
| `thin` | top only | 28 (COGS), 42 (OpEx Cat 1 total), 53 (OpEx Cat 2 total), 64 (OpEx Cat 3 total) |
| `thin` | bottom only | 82 (Capex), 83 (FCF) |

Horizontal borders on total rows span **all non-spacer columns** (B through Z, skipping I/N/S/U/Y).

### Alignment (exact)

| Location | Horizontal |
|----------|-----------|
| D column (row labels) | left |
| E6–H6 "Actuals" group header | center |
| T6 "LTM", V6 "Budget", Z6 "YoY % / bps" | center |
| J6, W6 (6+6 labels) | centerContinuous |
| Row 7 period labels | right |
| All data cells (E–Z, rows 9–84) | right |

### Number Formats (exact)

| Format String | Applied To |
|---------------|-----------|
| `_(#,##0.0_)_%;(#,##0.0)_%;_("–"_)_%;_(@_)_%` | ALL dollar value cells (E through X data columns) |
| `_(#,##0.0%_);(#,##0.0%);_("–"_)_%;_(@_)_%` | % Var columns (M, R), % of Revenue rows, YoY % rows, column Z |

---

### Column Layout (Date Infrastructure)

> **Column H = CY-1 (last full FY).** H3 = `='Input Page'!D27` (Last Complete FY End). H2 = `=EOMONTH(H3,-12)+1` (derived — start of the same FY). This means H always covers the last fully-closed fiscal year. Columns E, F, G are 3 prior complete fiscal years before H. The 6+6 section has **J = prior year N-months** (J2=H2, J3=EOMONTH(K3,-12)) and **K = current year N-months** (K2=H3+1, K3=D20). "To Go" has **O = prior year M-months** (O2=J3+1, O3=H3) and **P = current year M-months** (P2=D30, P3=D31). V = Budget FY (H3+1 through EOMONTH(H3,12)).

**Row 2 (date start serials, gray fill #DDDDDD):**
- E2: `=EOMONTH(E3,-12)+1`
- F2: `=EOMONTH(F3,-12)+1`
- G2: `=EOMONTH(G3,-12)+1`
- H2: `=EOMONTH(H3,-12)+1` — **start of last complete FY** (derived from H3)
- J2: `=H2` — prior-year 6+6 period starts at same point as H
- K2: `=H3+1` — current-year 6+6 period starts the day after last complete FY end
- O2: `=J3+1` — prior-year "To Go" starts day after prior-year split month
- P2: `='Input Page'!D30` — current-year "To Go" start (= D20+1)
- T2: `=EOMONTH(T3,-12)+1`
- V2: `=EOMONTH(V3,-12)+1`
- W2: `=V3+1`
- X2: `=W3+1`

**Row 3 (date end serials, gray fill #DDDDDD):**
- H3: `='Input Page'!D27` — **Last Complete FY End**
- E3: `=F2-1`, F3: `=G2-1`, G3: `=H2-1`
- J3: `=EOMONTH(K3,-12)` — prior-year N-months end (same calendar month as K3, one year prior)
- K3: `='Input Page'!D20` — current-year N-months end (the 6+6 split month)
- O3: `=H3` — prior-year "To Go" end (= Last Complete FY End = same end as H)
- P3: `='Input Page'!D31` — current-year "To Go" end (= 6+6 Forecast End = EOMONTH(D27,12))
- T3: `=K3`
- V3: `=EOMONTH(H3,12)` — Budget year end
- W3: `=EOMONTH(W2,11)`, X3: `=EOMONTH(X2,11)`

### Column Purpose Summary

| Col | Label | Period | Row 2 (start) | Row 3 (end) |
|-----|-------|--------|--------------|------------|
| E | CY oldest | Complete FY, 3 years before H | `=EOMONTH(E3,-12)+1` | `=F2-1` |
| F | CY-3 | Complete FY, 2 years before H | `=EOMONTH(F3,-12)+1` | `=G2-1` |
| G | CY-2 | Complete FY, 1 year before H | `=EOMONTH(G3,-12)+1` | `=H2-1` |
| H | CY-1 (last full FY) | Last fully-closed fiscal year | `=EOMONTH(H3,-12)+1` | `='Input Page'!D27` |
| J | N Months Actual (6+6) | Prior-year N months (same calendar span as K, one year earlier) | `=H2` | `=EOMONTH(K3,-12)` |
| K | N Months Actual +1yr | Current-year N months (Jan thru split month) | `=H3+1` | `='Input Page'!D20` |
| L | $ Var (K–J) | Current minus prior (positive = improvement) | | |
| M | % Var | | | |
| O | M Months To Go | Prior-year "To Go" (same calendar span as P, one year earlier) | `=J3+1` | `=H3` |
| P | M Months To Go +1yr | Current-year "To Go" ([split+1]–FY end) | `='Input Page'!D30` | `='Input Page'!D31` |
| Q | $ Var (P–O) | Current minus prior | | |
| R | % Var | | | |
| T | LTM | LTM end = K3 | `=EOMONTH(T3,-12)+1` | `=K3` |
| V | Budget (current/next FY) | 12 months starting the day after H3 | `=EOMONTH(V3,-12)+1` | `=EOMONTH(H3,12)` |
| W | Forecast Year 1 | 12 months starting W2 | `=V3+1` | `=EOMONTH(W2,11)` |
| X | Forecast Year 2 | 12 months starting X2 | `=W3+1` | `=EOMONTH(X2,11)` |
| Z | YoY % (V vs H) | Budget vs Last Full FY | | |

---

### Row Structure (Rows 5–84)

**Row 5: Title bar**
- B5: `='Input Page'!D33` — Arial 9pt bold white on black (#000000) fill, spans B5:Z5

**Row 6: Column group headers** (gray #DDDDDD fill)
- E6–H6: "Actuals" (centered)
- J6: `=DATEDIF(J$2,J$3,"M")+1&" Months Actual thru "&TEXT(J$3,"MMMM")` (centerContinuous — prior-year actual period label)
- K6: `=DATEDIF(K$2,K$3,"M")+1&" Months Actual thru "&TEXT(K$3,"MMMM")` (centerContinuous — current-year actual period label)
- O6: `=DATEDIF(O$2,O$3,"M")+1&" Months "&CHAR(34)&"To Go"&CHAR(34)` (prior-year to-go label)
- P6: `=DATEDIF(P$2,P$3,"M")+1&" Months "&CHAR(34)&"To Go"&CHAR(34)` (current-year to-go label)
- T6: "LTM" (center); V6: "Budget" (center); W6: "Forecast" (centerContinuous); Z6: "YoY % / bps" (center)
- B6: `='Input Page'!D25` (units label, italic)

**Row 7: Period labels** (Arial 9pt bold singleAccounting underline, right-aligned, row height 17.4pt)
- E7: `="CY"&YEAR(E$3)`, F7, G7, H7: same pattern (`="CY"&YEAR({col}$3)`)
- J7: `=DATEDIF(J$2,J$3,"M")+1&"M'"&YEAR(J$3)` (prior-year N-months label)
- K7: `=DATEDIF(K$2,K$3,"M")+1&"M'"&YEAR(K$3)` (current-year N-months label)
- L7: "$ Var.", M7: "% Var."
- O7: `=DATEDIF(O$2,O$3,"M")+1&"M'"&YEAR(O$3)` (prior-year to-go label)
- P7: `=DATEDIF(P$2,P$3,"M")+1&"M'"&YEAR(P$3)` (current-year to-go label)
- Q7: "$ Var.", R7: "% Var."
- T7: `="LTM "&TEXT(T3,"MMM 'YY")`; V7: `="CY"&YEAR(V$3)`; W7: `="CY"&YEAR(W$3)`; X7: `="CY"&YEAR(X$3)`
- Z7: `=RIGHT(H7,2)&"-'"&RIGHT(V7,2)` (dynamic YoY label, e.g., "25-'26")

**Row 8:** blank spacer (vertical borders applied per border rules)

---

#### Revenue Section (Rows 9–18)

**Rows 9–16:** Revenue subsegment rows (8 slots)
- D9: `=IF('Input Page'!D41="","",'Input Page'!D41)` through D16 → Input Page D48
- Mapping: D9→FMT row 14, D10→15, D11→16, D12→17, D13→18, D14→19, D15→20, D16→21
- **Data formula (col E):** `=IF($D9="","",SUMIFS('Financial Model Template'!$H14:$BC14,'Financial Model Template'!$H$3:$BC$3,">="&E$2,'Financial Model Template'!$H$3:$BC$3,"<="&E$3))`

**Row 17: Revenue total** — bold, thin top+bottom border, **tan fill `#E0DBD7`** on all non-spacer data cols
- B17: "Revenue"
- E17: `=SUMIFS('Financial Model Template'!$H22:$BC22,'Financial Model Template'!$H$3:$BC$3,">="&E$2,'Financial Model Template'!$H$3:$BC$3,"<="&E$3)`

**Row 18: YoY %** — italic; D18: "YoY %"; F18 onward: `=IFERROR(IF(ABS(F17/E17-1)>5,"n.m.",F17/E17-1),"")`

**Row 19:** spacer

---

#### COGS Section (Rows 20–29)

**Rows 20–27:** COGS subsegment rows (D20→FMT 26, ..., D27→FMT 33)

**Row 28: COGS** — bold, thin top border; C28: "COGS"; `=SUMIFS('Financial Model Template'!$H34:$BC34,...)`

**Row 29: % Total Revenue** — italic; `=IFERROR(E28/E17,"")`; format `0.0%`

**Row 30:** spacer

---

#### Gross Profit (Rows 31–32)

**Row 31: Gross Profit** — bold, thin top+bottom border; B31: "Gross Profit"; E31: `=E17-E28`

**Row 32: % of Net Revenue** — italic; `=IFERROR(E31/E17,"")`; format `0.0%`

**Row 33:** spacer 4.95pt

---

#### OpEx Category 1 Section (Rows 34–43)

**Rows 34–41:** Category 1 subsegment rows (D34→FMT 41, ..., D41→FMT 48)
- `=IF($D34="","",SUMIFS('Financial Model Template'!$H41:$BC41,...))`

**Row 42: Category 1 Total** — bold, thin top border
- B42: category label (e.g., "Sales & Marketing"); `=SUMIFS('Financial Model Template'!$H49:$BC49,...)`

**Row 43: % Total Revenue** — italic; `=IFERROR(E42/E17,"")`

**Row 44:** spacer 4.95pt

---

#### OpEx Category 2 Section (Rows 45–54)

**Rows 45–52:** Category 2 subsegment rows (D45→FMT 52, ..., D52→FMT 59)

**Row 53: Category 2 Total** — bold, thin top border; B53: category label; `=SUMIFS('Financial Model Template'!$H60:$BC60,...)`

**Row 54: % Total Revenue** — italic

**Row 55:** spacer 4.95pt

---

#### OpEx Category 3 Section (Rows 56–65)

**Rows 56–63:** Category 3 subsegment rows (D56→FMT 63, ..., D63→FMT 70)

**Row 64: Category 3 Total** — bold, thin top border; B64: category label; `=SUMIFS('Financial Model Template'!$H71:$BC71,...)`

**Row 65: % Total Revenue** — italic

**Row 66:** spacer

---

#### Total OpEx (Rows 67–69)

**Row 67: Total Operating Expense** — bold, thin top+bottom border
- B67: "Total Operating Expense"; `=SUMIFS('Financial Model Template'!$H74:$BC74,...)`

**Row 68: % of Net Revenue** — italic; `=IFERROR(E67/E17,"")`
**Row 69: YoY %** — italic; D69: "YoY %"

**Row 70:** spacer

---

#### EBITDA (Rows 71–73)

**Row 71: EBITDA** — bold, thin top+bottom border
- B71: "EBITDA"; `=SUMIFS('Financial Model Template'!$H86:$BC86,...)`

**Row 72: % of Net Revenue** — italic; `=IFERROR(E71/E17,"")`
**Row 73: YoY %** — italic

**Row 74:** spacer

---

#### Cash Flow Summary (Rows 75–84)

**Row 75:** B75 = "Cash Flow Summary" — bold, thin bottom border, row height 15.0pt

**Row 76:** blank

**Row 77: Reported EBITDA** — bold; C77: "Reported EBITDA"; E77: `=E71` (direct reference)

**Row 78:** D78 = "(-) Other Expense / (income)"; `=SUMIFS('Financial Model Template'!$H92:$BC92,...)`

**Row 79:** D79 = "(-) Taxes" — blank/zero

**Row 80:** D80 = "(-) Δ in NWC"; `=SUMIFS('Financial Model Template'!$H182:$BC182,...)`

**Row 81:** D81 = "(-) Other LT Assets, Net"; `=SUMIFS('Financial Model Template'!$H184:$BC184,...)`

**Row 82:** D82 = "(-) Capex" — thin bottom border; `=SUMIFS('Financial Model Template'!$H183:$BC183,...)`

**Row 83: Reported Free Cash Flow** — bold, thin bottom border; B83: "Reported Free Cash Flow"; E83: `=SUM(E77:E82)`

**Row 84: % of Reported EBITDA** — italic; D84: "% of Reported EBITDA"; `=IF(E77=0,0,E83/E77)`

---

### SUMIFS Formula Pattern (all data cells)

```excel
=SUMIFS('Financial Model Template'!$H{row}:$BC{row},
  'Financial Model Template'!$H$3:$BC$3,">="&{col}$2,
  'Financial Model Template'!$H$3:$BC$3,"<="&{col}$3)
```

- **Range always `$H:$BC`** — 48 monthly columns from FMT. Extend to the last populated FMT data column if model period exceeds 48 months.
- Subsegment guard: `=IF($D{n}="","",SUMIFS(...))`

### Variance Column Formulas

**$ Variance (columns L, Q):**
- Subsegment rows (IS): `=IF($D{n}="","",K{n}-J{n})` (or `P{n}-O{n}` for "To Go"). Uses `$D` guard.
- Total rows: `=K{n}-J{n}`; % rows (bps): `=K{n}-J{n}`
- **Cash Flow rows (78–82):** `=IF($B{n}="","",K{n}-J{n})` — uses `$B` column check (not `$D`)

**% Variance (columns M, R):**
- `=IFERROR(IF(ABS(L{n}/J{n})>5,"n.m.",L{n}/J{n}),"")`
- Values exceeding 500% display as "n.m."

**YoY % / bps (column Z):**
- $ rows: `=IFERROR(IF(ABS(V{n}/H{n}-1)>5,"n.m.",V{n}/H{n}-1),"")`
- % rows (margins): `=V{n}-H{n}` (bps change)

---

## CROSS-TAB DEPENDENCIES

### Input Page → Financial Model Template
- B1 (units divisor) ← `='Input Page'!D10`
- D14–D21 ← Input Page D41–D48; D26–D33 ← D51–D58; D41–D48 ← D61–D68; D52–D59 ← D71–D78; D63–D70 ← D81–D88
- Date column generation ← Input Page D16 (Model Start), D17 (Last Actuals), D18 (Forecast Period)

### Input Page → Output Tab
- B5 (title) ← `='Input Page'!D33`; B6 (units label) ← `='Input Page'!D25`
- Date ranges ← Input Page D27 (H3), D20 (K3), D30 (P2), D31 (P3). H2/J2/O2 derived via EOMONTH — no direct D29 link from Output Tab.
- Subsegment names ← Input Page D41–D88

### Financial Model Template → Output Tab
- ALL numeric data via SUMIFS on FMT columns **H through BC** (row 3 = EOMONTH date serials)
- Row mapping: Revenue subs → FMT 14–21 | Total Revenue → FMT 22 | COGS subs → FMT 26–33 | COGS → FMT 34 | Cat 1 subs → FMT 41–48 | Cat 1 total → FMT 49 | Cat 2 subs → FMT 52–59 | Cat 2 total → FMT 60 | Cat 3 subs → FMT 63–70 | Cat 3 total → FMT 71 | Total OpEx → FMT 74 | EBITDA → FMT 86 | Other Inc/Exp → FMT 92 | **Output row 80 (NWC) → FMT 182** | **Output row 81 (Other LT) → FMT 184** | **Output row 82 (Capex) → FMT 183**

---

## RECONSTRUCTION STEPS

### Step 0: Read the Source Data
1. Read the uploaded IS and BS data
2. Identify: company name, currency, FY start month, date range, last actuals date
3. Categorize IS line items: Revenue, COGS, OpEx — **infer from source, do NOT assume S&M/R&D/G&A**
4. Map BS line items into the standard BS categories

### Step 1: Build the Input Page
1. Create tab "Input Page", set tab color `#4472C4`, gridlines OFF; set column widths per spec
2. Build all sections with formulas
3. **Key: D16 = `=DATE(YEAR(D17)-4,D15,1)` (4 years back — covers all Output Tab historical columns E/F/G/H); D31 = `=EOMONTH(D27,12)` (6+6 Forecast End = one full year after Last Complete FY End)**
4. Create IS category blocks (10-row-per-block), populate subsegment names, create Counts section
5. Apply all formatting per spec

### Step 2: Build the Financial Model Template
1. Create tab "Financial Model Template", tab color `#548235`, gridlines OFF
2. freeze_panes = 'H92'; hide column G; hide rows 1–4; set column widths per spec
3. Generate monthly date columns in rows 1–3 from Model Start through forecast end
4. Build IS block structure with subsegment name links and INDEX/MATCH data formulas
5. **Key: Total OpEx (row 74) = `=H71+H60+H49`; EBIT (row 78) = `=H37-H74`**
6. Build BS: **Total Assets at C124 = `=H122+H120+H123`; Total Current Liabilities at D130**
7. Build Working Capital, PP&E, Other LT, CF sections with delta formulas
8. Apply all number formats, borders, Aptos Narrow 11pt on subsegment D cells

### Step 3: Build the Output Tab
1. Create tab "Output Tab", tab color `#BF8F00`, gridlines OFF
2. Set hidden columns (I, N, S, U, Y); set column widths per spec
3. Build date rows 2–3: **H3 = `='Input Page'!D27`; H2 = `=EOMONTH(H3,-12)+1`; J2 = `=H2`; J3 = `=EOMONTH(K3,-12)`; K2 = `=H3+1`; K3 = `='Input Page'!D20`; O2 = `=J3+1`; O3 = `=H3`; P2 = `='Input Page'!D30`; P3 = `='Input Page'!D31`; T3 = `=K3`; V3 = `=EOMONTH(H3,12)`; W3 = `=EOMONTH(W2,11)`; X3 = `=EOMONTH(X2,11)`**
4. Build row 5 (title), row 6 (headers), row 7 (singleAccounting underline period labels)
5. Build all IS sections with SUMIFS range `$H:$BC`; build variance columns; build CF Summary
6. Apply: tan fill row 17, continuous vertical borders, horizontal borders on totals

---

## PARAMETERIZATION NOTES
1. Claude reads source data → infers categories → populates Input Page → builds FMT → builds Output Tab
2. If OpEx categories differ from default 3, adjust all three tabs accordingly
3. BS/CF structure stays fixed — map source BS items into standard categories
4. Handle different FY, currency, or units via Input Page config
