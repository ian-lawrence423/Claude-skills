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
saas-revenue-growth-metrics    ──┐
saas-economics-efficiency-metrics─┤
financial-model-builder         ─┤──► gtm-metrics-analyzer ──► kpi-tree-builder (post-close)
driver-tree                     ─┤                          ──► ic-memo (supporting metrics section)
ntb-diligence                   ─┘
```

### When to use this skill vs. adjacent skills

| Task | Use |
|---|---|
| Quick metric definition or benchmark lookup | `finance-metrics-quickref` |
| SaaS revenue/retention metric definitions only | `saas-revenue-growth-metrics` |
| CAC/LTV/efficiency metric definitions only | `saas-economics-efficiency-metrics` |
| Full GTM diagnostic workbook from uploaded files | **this skill** |
| Causal driver decomposition with owner assignment | `kpi-tree-builder` |
| Investment Committee memo with GTM section | `ic-memo` (calls this skill for metrics) |
| 3-tab operating model from P&L | `financial-model-builder` |

### Integration with upstream skills
- **`financial-model-builder`**: Load first if a 3-tab model exists. Pull Revenue, Gross Profit, S&M OpEx directly from the Output Tab rather than asking for re-entry.
- **`driver-tree`**: If a driver tree has been built, import node values directly as input fields rather than entering them manually.
- **`ntb-diligence`**: NTB outputs (new logo ARR, cohort retention) feed directly into the ARR funnel and retention sections of this workbook.
- **`saas-revenue-growth-metrics`** / **`saas-economics-efficiency-metrics`**: Use these for metric definition disputes or benchmark context. This skill handles calculation; those skills handle interpretation.
- **`kpi-tree-builder`**: After GTM diagnostic is complete, hand off the derived metric outputs to `kpi-tree-builder` to assign owners, cadences, and thresholds for post-close tracking.
- **`ic-memo`**: The IC memo's GTM performance section pulls from this skill's Diagnostic_Output tab. Run gtm-metrics-analyzer first; reference the workbook in the memo.

---

## Input contract
This skill is designed for **uploaded tables and files**.

Preferred inputs:
- uploaded xlsx/csv exports
- board decks or operating review files with GTM data
- CRM / RevOps exports
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

The workbook is organized into four tabs:
- `README` = how to use the workbook
- `Input_Fields` = what the user must provide
- `Metric_Calcs` = all metrics, formulas, required inputs, and calculated values
- `Diagnostic_Output` = clean summary view for operators and investors

When completing work for the user, preserve this structure unless the uploaded workbook already has a better one.

### Step 5: produce diagnostic analysis in excel
Default output mode is **diagnostic analysis in excel**.

A good output should:
- show the load-bearing GTM metrics,
- distinguish raw uploaded inputs from derived calculations,
- highlight missing fields,
- surface the most important findings,
- keep the final workbook clean enough for operating review.

### Multi-period analysis
When the user provides data for multiple periods (e.g., Q1–Q4 or trailing 4 quarters):
- create one column per period in `Input_Fields` (add Period columns E, F, G… per period)
- add a Period row in `Metric_Calcs` header to show which period each calculation covers
- in `Diagnostic_Output`, add a sparkline column or period-over-period delta column
- flag metrics that require prior-period data (e.g., YoY ARR growth, time-adjusted CAC) — those require at least two periods

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
- beginning arr
- new logo arr
- expansion arr
- upsell arr
- cross-sell arr
- downsell
- logo churn arr
- ending arr
- bookings
- billings
- revenue
- deferred revenue

### Customer and retention inputs
- beginning customer count
- ending customer count
- new logos
- churned customers
- cohort table
- retention table
- churn / lost reasons
- product usage or health metrics

### Funnel and pipeline inputs
- lead counts by stage
- opportunity counts by stage
- pipeline dollars
- weighted pipeline dollars
- create date / close date
- conversion rates or stage history
- sales target
- forecast
- source / attribution columns

### Efficiency and economics inputs
- s&m opex
- gross profit
- subscription revenue
- services revenue
- gross margin
- new logo customer count
- arr per customer
- cac by channel if available

### Team and productivity inputs
- average s&m ftes
- quota-carrying reps
- csms
- sdrs / bdrs
- sales managers
- quota allocated
- quota attained
- rep ramp data
- rep attrition

### Plan and forecast inputs
- actuals
- plan / budget
- forecast
- guidance
- consensus, if relevant

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

### 2. Diagnostic analysis in excel
Default mode.
Output:
- populated workbook tabs
- concise findings
- missing inputs register
- derived metric table
- clean diagnostic output sheet

### 3. Reporting pack
Use when the user explicitly asks for a board or operating review layout.
Use `references/reporting-views.md` for board deck and operating review section layouts.

---

## Workbook behavior
When the bundled workbook is used:
- keep `Input_Fields` as the source-of-truth list of required inputs,
- keep `Metric_Calcs` as the full catalog of metrics and calculations,
- keep `Diagnostic_Output` focused on the most decision-useful metrics,
- do not hide assumptions,
- do not overwrite uploaded raw data tabs unless the user asks.

---

## Success standard
A good result should let the user answer:
- what data did i provide?
- what is still missing?
- which metrics were derived automatically?
- what formulas were used?
- what are the key GTM findings?
- which outputs are exact versus directional?
