---
name: gtm-metrics-analyzer
description: calculate, interpret, and package b2b saas go-to-market metrics into a diagnostic excel workbook using the bundled metric catalog, formulas, and input requirements. use when a user uploads gtm tables, exports, board files, forecasts, or operating spreadsheets and wants a clean excel-based diagnostic analysis of growth drivers, arr funnel, pipeline, retention, efficiency, productivity, or forecast metrics. ask for missing uploaded inputs, distinguish provided values from derived calculations, and populate the bundled workbook tabs for inputs, metric calculations, and diagnostic output.
---

Build a stand-alone GTM diagnostic workbook from uploaded tables and files.

## What this skill does
Use this skill when the user wants an Excel-based diagnostic analysis of GTM performance from uploaded source files.

The skill should:
1. identify which GTM metrics are relevant,
2. determine what the user must provide,
3. separate provided inputs from derived calculations,
4. calculate metrics using the bundled formulas,
5. populate or mirror the structure of the bundled workbook template,
6. produce a clean diagnostic output tab in the same workbook.

This skill is built primarily for B2B SaaS companies with some sales-led motion.

> **Excel version note:** Metric formulas use XLOOKUP, which requires Excel 365 or Excel 2019+. Earlier versions will show `#NAME?` errors in Metric_Calcs and Diagnostic_Output. If the user is on an older version, replace XLOOKUP with INDEX/MATCH equivalents.

---

## Skill architecture

```
financial-model-builder  ──┐
driver-tree              ──┤──► gtm-metrics-analyzer ──► kpi-tree-builder (post-close)
ntb-diligence            ──┘                          ──► ic-memo (supporting metrics section)
```

### When to use this skill vs. adjacent skills

| Task | Use |
|---|---|
| Quick metric definition or benchmark lookup | `finance-metrics-quickref` |
| Full GTM diagnostic workbook from uploaded files | **this skill** |
| Causal driver decomposition with owner assignment | `kpi-tree-builder` |
| Investment Committee memo with GTM section | `ic-memo` (calls this skill for metrics) |
| 3-tab operating model from P&L | `financial-model-builder` |

### Integration with upstream skills
- **`financial-model-builder`**: Load first if a 3-tab model exists. Pull Revenue, Gross Profit, S&M OpEx directly from the Output Tab rather than asking for re-entry.
- **`driver-tree`**: If a driver tree has been built, import node values directly as input fields rather than entering them manually.
- **`ntb-diligence`**: NTB outputs (new logo ARR, cohort retention) feed directly into the ARR funnel and retention sections of this workbook.
- **`finance-metrics-quickref`**: Use for quick metric definition lookups or benchmark checks. This skill handles calculation from uploaded data; `finance-metrics-quickref` handles definition and quick-reference.
- **`kpi-tree-builder`**: After GTM diagnostic is complete, hand off the derived metric outputs to `kpi-tree-builder` to assign owners, cadences, and thresholds for post-close tracking.
- **`ic-memo`**: The IC memo's GTM performance section pulls from this skill's Diagnostic_Output tab. Run gtm-metrics-analyzer first; reference the workbook in the memo.

---

## Input contract
This skill is designed for **uploaded tables and files**.

Preferred inputs:
- uploaded xlsx/csv exports
- board decks or operating review files with GTM data
- CRM / RevOps exports (HubSpot deal exports, pipeline snapshots)
- ARR funnel tables
- pipeline tables
- cohort retention tables
- S&M spend and headcount tables

If the user asks for calculations without enough uploaded data, do not guess silently.
Instead:
1. use `references/input-requirements.md` to identify the missing fields,
2. ask the user to upload the missing source tables or files,
3. state which metrics can still be derived with current data,
4. clearly label any assumption, simplification, or substitution.

---

## Default workflow

### Step 1: classify the request
Map the request into one or more metric families using `references/metric-catalog.md`:
- growth drivers
- sales funnel
- retention
- efficiency & economics
- team & productivity
- fiscal maturity
- deal cycle & pipeline health (see section below)

### Step 2: identify required uploads
Before calculating, check the uploaded files against `references/input-requirements.md`.

Always separate:
- **required user-provided inputs**
- **derived calculations**

If data is incomplete, tell the user exactly which uploaded tables or columns are still needed.

### Step 3: calculate metrics
Use `references/formulas.md` as the human-readable source of truth for all metric formulas and methodology.

Rules:
- prefer the ICONIQ preferred methodology when marked,
- match the metric period exactly: monthly, quarterly, annualized quarterly, annual, or LTM,
- do not mix logo and dollar metrics,
- do not collapse gross and net metrics into one figure,
- if a substitute metric is used because the preferred input is unavailable, say so explicitly.

### Step 4: structure the workbook
Use the bundled asset workbook:
- `assets/gtm_metrics_template.xlsx`

To regenerate the template from source, run:
- `assets/build_template.py` (requires Python + openpyxl)

The bundled workbook is organized into four tabs:
- `README` = how to use the workbook, tab order, requirements, and metric family index
- `Input_Fields` = user-provided values entered directly into column F (User Value); one row per input field, organized by section
- `Metric_Calcs` = 48 derived metrics; column G (Calculated Value) auto-populates via XLOOKUP from Input_Fields
- `Diagnostic_Output` = 20-metric summary view; values pulled from Metric_Calcs via XLOOKUP

The `Metric_Calcs` tab columns are:
| Col | Content |
|-----|---------|
| A | Metric Family |
| B | Metric Key (XLOOKUP lookup key — do not modify) |
| C | Metric Name |
| D | Type (Derived) |
| E | Formula / Logic |
| F | Required Inputs |
| G | Calculated Value (formula; auto-populates when Input_Fields is populated) |
| H | Comments |

When completing work for the user, populate Input_Fields column F with values from uploaded source files, then review Metric_Calcs column G and Diagnostic_Output for the derived results. Preserve this structure unless the uploaded workbook already has a better one.

> **For multi-period time-series analysis** (when the user provides monthly data across multiple fiscal years), see the advanced multi-period architecture section below.

### Step 5: produce diagnostic analysis in excel
Default output mode is **diagnostic analysis in excel**.

A good output should:
- show the load-bearing GTM metrics,
- distinguish raw uploaded inputs from derived calculations,
- highlight missing fields,
- surface the most important findings,
- keep the final workbook clean enough for operating review.

---

## Advanced: multi-period workbook architecture

Use this section when the user provides monthly time-series data across multiple fiscal years and wants a full multi-period build instead of the single-period bundled template.

In a multi-period build, add a fifth tab — `Raw_Monthly_Data` — as the source-of-truth layer before `Input_Fields`. The formula chain becomes:

```
Raw_Monthly_Data   ← source of truth for all monthly time-series data
      ↓
Input_Fields       ← annual aggregates, rates, and context; formula-driven from Raw_Monthly_Data
      ↓
Metric_Calcs       ← all metric calculations; formula-driven from Input_Fields
      ↓
Diagnostic_Output  ← summary and findings; formula-driven from Metric_Calcs
```

**Nothing flows backward — each layer only reads from the layer above it.**

**Never hardcode a value in Metric_Calcs or Diagnostic_Output that could be a formula referencing Input_Fields or Raw_Monthly_Data.** The only hardcoded (blue) values permitted are context fields (e.g., business model, reporting cadence, benchmark references, source notes) and all cells in Raw_Monthly_Data.

### Raw_Monthly_Data tab: layout rules

#### Column layout
- Column B: Metric label
- Column C: Unit (€K, %, count, days, etc.)
- Column D onward: one column per month, chronological (e.g., D=Jan-24, E=Feb-24, … O=Dec-24, P=Jan-25, … AA=Dec-25 for a 24-month layout)
- Final column: Comment (source notes and caveats)

Use named groups of 12 columns per fiscal year. For FY2024+FY2025: cols D–O = FY2024, cols P–AA = FY2025.

#### Row layout
Organize rows into logical sections separated by blank rows. Suggested structure:
1. MRR Waterfall (BOP MRR, New Logo MRR, Expansion MRR, Gross New MRR, Downsell MRR, Logo Churn MRR, Gross Churn MRR, Net New MRR, EOP MRR)
2. Logo Counts (New Logo Count)
3. Retention Rates (GRR Logo, GRR Total, NRR)
4. Efficiency Metrics (S&M Expense, CAC, Gross Margin %, LTV:CAC)
5. HubSpot Pipeline Data (monthly closed-won counts and MRR by deal type)
6. Any additional monthly data

#### Atomic cell rule
**One value per cell. Never combine two values in one cell.**

Wrong: `"21 deals, €115K MRR"` in a single cell
Right: separate rows — one for deal count, one for MRR

#### Null handling
Months where data is not yet available should be left blank (None / empty), not zero.
- Zero means the metric was actually zero that month.
- Empty/None means the metric is not yet reported.

### Input_Fields tab: formula rules for multi-period builds

When Input_Fields is formula-driven from Raw_Monthly_Data (multi-period build), use these patterns:

**Flow metrics** (accumulate): use SUM
```excel
=SUM('Raw_Monthly_Data'!D7:O7)     # FY2024 New Logo MRR
=SUM('Raw_Monthly_Data'!P7:AA7)    # FY2025 New Logo MRR
```

**Rate / percentage metrics** (average): use AVERAGEIF to skip null months
```excel
=AVERAGEIF('Raw_Monthly_Data'!D27:O27,"<>")    # FY2024 Gross Margin avg
```
Do not use AVERAGE() for rate metrics — it counts blank months as zero, which distorts partially-available periods.

**Stock metrics** (point-in-time): reference a specific month cell
```excel
='Raw_Monthly_Data'!D6      # Jan-24 BOP MRR (start of FY2024)
```

**Metrics with intermittent nulls**: use IFERROR to default null months to zero
```excel
=IFERROR('Raw_Monthly_Data'!P10, 0) + 'Raw_Monthly_Data'!P11
```

#### Cross-sheet formula syntax — critical gotcha
The sheet reference must wrap the range, not the function:

**Wrong:** `='Raw_Monthly_Data'!SUM(D7:O7)` — invalid Excel; produces `#NAME?`
**Right:** `=SUM('Raw_Monthly_Data'!D7:O7)` — the function wraps the full sheet-prefixed range

This applies to all functions: SUM, AVERAGE, AVERAGEIF, MIN, MAX, COUNT, etc.

### Metric_Calcs tab: multi-period column layout

For a multi-period build, expand Metric_Calcs to one column per fiscal year:

| Col | Content |
|-----|---------|
| B | Metric label |
| C | FY2024 value (formula from Input_Fields) |
| D | FY2025 value (formula from Input_Fields) |
| E | Unit |
| F | Delta (=D−C) |
| G | Delta % (=IF(C<>0,(D−C)/ABS(C),"—")) |
| H | Benchmark |
| I | Notes / methodology |
| J | Source |
| K | Commentary |

#### Magic number quarterly formulas in multi-period builds
Magic numbers require prior-quarter S&M in the denominator. The correct syntax:
```excel
# Net Magic Number Q1 2025 = (Q1 Net New MRR × 4) / Q4 2024 S&M
=IF(SUM('Raw_Monthly_Data'!M24:O24)<>0, SUM('Raw_Monthly_Data'!P13:R13)*4 / SUM('Raw_Monthly_Data'!M24:O24), "—")
```
Note: the SUM function wraps the full `'Sheet'!range` reference. Do not split it.

### Color coding standards (multi-period builds)
- **Blue text**: hardcoded inputs — values entered manually, not derived
- **Black text**: formula-derived values
- **Green text**: cross-sheet formula links
- **Red text**: external file links

Apply consistently. A reviewer should be able to identify at a glance which cells are assumptions vs. calculations.

---

## Deal cycle analysis: methodology

Deal cycle is a first-class GTM metric for sales-led SaaS. It must be calculated from CRM data, not estimated.

### Calculation
- **Deal cycle (days)** = `closeDate − createDate` in calendar days, per individual closed-won deal record
- Each deal type (New Contract, Renewal, PoC) is measured independently
- PoC and the subsequent Full Contract are **separate deal records** with **separate cycle clocks**. The time from PoC close to New Contract createDate (the "conversion gap") is not captured by this method.

### Methodology rules
1. Exclude same-day closes (createDate = closeDate) — these are data entry artefacts, not real deal cycles
2. Exclude negative cycles (closeDate < createDate) — backdated close dates
3. Report both **average** and **median** — the average is sensitive to long-tail enterprise deals; the median reflects the typical experience
4. Report **P25 and P75** alongside median — the interquartile range signals predictability. A narrow band (e.g., renewal: P25=37d, P75=78d) means the sales cycle is consistent; a wide band (e.g., new contract: P25=34d, P75=194d) means high variability and poor forecastability

### Outlier detection
Use the **1.5×IQR Tukey fence** applied **per deal type**, not across all deal types combined:
```python
Q1 = 25th percentile of deal cycle days for that type
Q3 = 75th percentile
IQR = Q3 - Q1
lower fence = Q1 - 1.5 × IQR
upper fence = Q3 + 1.5 × IQR
# Any deal outside [lower, upper] is flagged as an outlier
```

Applying one fence across all types masks genuine patterns: a 200-day new contract cycle is within-range for New Contracts but an extreme outlier for Renewals.

### Interpretation guidance
- If avg >> median for a deal type, a small number of long-tail deals (complex procurement, enterprise, agency intermediary) are distorting the average. Report median as the primary figure.
- Deal size (MRR) typically has near-zero correlation with deal cycle length (Pearson r ≈ 0). Deal type and complexity are stronger predictors.
- The fastest closers tend to be warm relationships or geographies with direct commercial relationships (no procurement layer). The slowest tend to involve agency intermediaries, multi-stakeholder procurement, or first-time enterprise relationships.

### What to calculate and report
| Metric | Note |
|--------|------|
| Avg deal cycle — All types | Include with caveat if outliers are present |
| Median deal cycle — All types | Primary figure |
| Avg deal cycle — New Contract | |
| Median deal cycle — New Contract | |
| Avg deal cycle — Renewal | |
| Median deal cycle — Renewal | |
| Avg deal cycle — PoC | Flag if n < 10 (thin sample) |
| Median deal cycle — PoC | |
| P25 / P75 per type | Signal predictability |
| Contract length — by type | endDate − startDate; typically 12 months for renewals, 3 months for PoCs |

---

## Pipeline health: stage age methodology

Open pipeline stage age measures how long currently-open deals have been sitting in the pipeline, as a proxy for velocity and stall risk.

### Calculation
- **Stage age (days)** = `today − deal.createDate` per open deal
- Group by current pipeline stage
- Report median and average per stage

### Limitation
This uses `createDate` as a proxy for stage entry date. The exact stage entry date (when a deal moved into its current stage) is not surfaced by most CRM APIs. If stage history is available via webhooks or audit log, use that instead — it is more accurate.

### Interpretation
- Deals in "Verbally agreed" sitting >90 days are a priority risk signal — verbally agreed deals should convert to signed within 30–60 days; if they don't, the verbal agreement is soft
- Deals in "Product negotiations" or "Commercial negotiations" sitting >180 days indicate a blocked funnel; investigate deal-by-deal
- "Offer" stage deals often include overages/upsells which have naturally longer ages — consider segmenting offer-stage deals by type (new, renewal, overage) before drawing conclusions

---

## HubSpot field coverage guide

When pulling data from HubSpot via MCP:

### Available via search API (all deals, bulk)
`createDate`, `updateDate`, `closeDate`, `name`, `stage`, `pipeline`, `type`, `totalDealValueInCurrency`, `monthlyRecurringRevenueEur`, `paymentPeriodicity`, `currency`, `startDate`, `endDate`, `earlyTerminationDate`, `region`, `hubspotUrl`

### Available via deal detail API (per deal, requires individual pulls)
`companyName`, `ownerName`, `csmName`, `billingInfo.country`, `billingInfo.paymentTerms`, `legalInfo.rhEntity`, `legalInfo.terminationClause`, `meddic.*`, `contacts[].numberOfTimesContacted`, `contacts[].lastContacted`, `purchasedServices[].contractedService`, `purchasedServices[].spendLimitInCurrency`, `purchasedServices[].finalPriceInEur`

### High-value derived fields (compute from available data)
- **Deal cycle days**: `closeDate − createDate`
- **Contract length (months)**: `(endDate − startDate) / 30.44`
- **Channel mix**: count distinct `purchasedServices[].contractedService` values per deal (requires detail pull)
- **Pipeline stage age**: `today − createDate` per open deal

### Fields not available via API
- Stage entry date (when a deal moved into its current stage) — requires audit log / webhook
- Quota per rep — stored separately
- Individual rep activity metrics (calls, emails) — requires activity API

---

## Multi-period and monthly analysis

When the user provides data for multiple periods:

### Annual comparison (FY-to-FY)
- One column per fiscal year in Input_Fields (C=FY2024, D=FY2025)
- Delta column (=D-C) and Delta% column in Metric_Calcs
- FY aggregates derived from monthly data via SUM / AVERAGEIF formulas referencing Raw_Monthly_Data

### Monthly time-series (preferred for SaaS diagnostics)
- Maintain a Raw_Monthly_Data tab with 12 columns per fiscal year
- Use the formula chain: Raw_Monthly_Data → Input_Fields → Metric_Calcs
- Flag months with no data as blank (not zero)
- For charts and sparklines in Diagnostic_Output, reference Raw_Monthly_Data directly (avoids double-aggregation)

### Quarterly aggregation from monthly
- Q1 = SUM of months 1–3 in a fiscal year (or AVERAGEIF for rate metrics)
- Magic numbers and efficiency ratios use prior-quarter denominators — track quarterly ranges explicitly
- Example: Net Magic Number Q1 2025 = Net New ARR Q1 2025 × 4 / S&M Expense Q4 2024

---

## Workbook construction with Python/openpyxl

When building the workbook programmatically (recommended for repeatability):

### General rules
- Use openpyxl for all formula and formatting work
- Use pandas only for data extraction and transformation; write back to Excel via openpyxl
- After writing any formula-containing workbook, open it in Excel and manually verify that all formula cells in Metric_Calcs column G and Diagnostic_Output column B resolve to values rather than errors
- Check for `#REF!`, `#NAME?`, `#DIV/0!`, `#VALUE!` before delivering; fix at the source formula, not by overriding with values

### Common formula errors to prevent
| Error | Cause | Fix |
|-------|-------|-----|
| `#NAME?` | Sheet reference before function: `='Sheet'!SUM(A1:A5)` | Reverse: `=SUM('Sheet'!A1:A5)` |
| `#VALUE!` | String in a cell starting with `=` being interpreted as a formula | Never start comment strings with `=`; rephrase as `"Gross New = New Logo + Expansion"` |
| `#REF!` | Cell reference points to a deleted or out-of-bounds cell | Verify all row/column indices before saving |
| `#DIV/0!` | Denominator is zero or blank | Wrap with `IF(denominator<>0, formula, "—")` |

### Row indexing pattern
Track row numbers as named variables during programmatic construction, not as magic numbers:
```python
RD_BOP = 6   # BOP MRR row in Raw_Monthly_Data
RD_NL  = 7   # New Logo MRR row
# etc.
# Use these to build cross-sheet formulas:
f"=SUM('Raw_Monthly_Data'!D{RD_NL}:O{RD_NL})"   # FY2024 New Logo MRR
```

---

## Prompt the user for what must be provided
When the uploaded files are insufficient, prompt the user with this structure:

### Company and reporting context
- business model
- primary revenue metric: arr, mrr, carr, bookings, billings, gaap revenue, or another metric
- reporting cadence
- time periods to analyze
- segmentation scheme, if any

### Revenue and arr inputs
- beginning arr / mrr
- new logo arr / mrr
- expansion arr / mrr
- downsell
- logo churn arr / mrr
- ending arr / mrr
- bookings, billings, revenue (if different from ARR/MRR)
- deferred revenue

### Customer and retention inputs
- beginning customer count
- ending customer count
- new logos
- churned customers
- cohort table
- churn / lost reasons

### Funnel and pipeline inputs
- lead counts by stage
- opportunity counts by stage
- pipeline dollars (total and weighted)
- create date / close date (for deal cycle calculation)
- win rate
- source / attribution
- sales target and forecast

### Efficiency and economics inputs
- s&m opex (monthly preferred)
- gross profit / gross margin %
- new logo customer count
- arr per customer
- cac by channel if available

### Team and productivity inputs
- average s&m ftes
- quota-carrying reps
- csms
- sdrs / bdrs
- quota allocated and attained

### Plan and forecast inputs
- actuals
- plan / budget
- forecast
- guidance

---

## Output modes

### 1. Metric calculation
Use for a specific metric request.
Output:
- metric
- formula used
- inputs provided
- derived result
- note on missing inputs if any

### 2. Diagnostic analysis in excel (default)
Output:
- populated workbook tabs (README, Input_Fields, Metric_Calcs, Diagnostic_Output)
- concise findings summary
- missing inputs register
- derived metric table
- clean diagnostic output sheet

### 3. Deal cycle detail export
When the user wants a per-deal breakdown (rather than summary stats):
- produce a separate Excel file with one row per closed-won deal
- columns: deal name, type, region, create date, close date, cycle days, MRR, ARR, outlier flag (1.5×IQR per type), IQR fence, notes
- include a summary stats table by deal type at the bottom
- apply auto-filter and freeze panes for usability
- color-code outlier rows (red = outside IQR fence, yellow = same-day artefact)

### 4. Reporting pack
Use when the user explicitly asks for a board or operating review layout.
Use `references/reporting-views.md` for board deck and operating review section layouts.

---

## Workbook behavior
When the bundled workbook is used:
- keep `Input_Fields` as the data-entry layer — populate column F only; do not add formulas to columns A–E
- keep `Metric_Calcs` as the full metric calculation catalog; column G auto-populates from Input_Fields
- keep `Diagnostic_Output` focused on the most decision-useful metrics
- do not hide assumptions
- do not overwrite uploaded raw data tabs unless the user asks
- do not put two values in one cell; one metric per row per cell
- if the user provides monthly time-series data, add a `Raw_Monthly_Data` tab before Input_Fields and follow the multi-period architecture described above

---

## Interaction with kpi-tree-builder

`kpi-tree-builder` is the structural companion to this skill.

Use `gtm-metrics-analyzer` to:
- calculate metrics
- identify missing inputs
- separate user inputs from derived calculations
- populate workbook tabs
- diagnose metric movement

Use `kpi-tree-builder` to:
- organize those metrics into a causal operating tree
- decide which metrics belong under each branch
- define weekly / monthly / quarterly tracking architecture

This skill can support a KPI tree by supplying the metrics used in its nodes, but it should not replace the structural decomposition performed by `kpi-tree-builder`.

---

## Success standard
A good result should let the user answer:
- what data did i provide?
- what is still missing?
- which metrics were derived automatically?
- what formulas were used?
- what are the key GTM findings?
- which outputs are exact versus directional?
- what are the outliers in the deal cycle data and why?
- what does the open pipeline look like on a stage-age basis?
