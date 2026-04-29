# Reporting Views

Use this file when Output Mode 3 is requested — the user wants a board deck or operating review layout rather than a raw diagnostic workbook. Maps GTM metrics to standard reporting sections.

---

## Board deck GTM section

Standard slide order for a board-level GTM update. Each slide maps to a metric family.

### Slide 1 — ARR Summary
Key metrics:
- Beginning ARR → Net New ARR → Ending ARR (waterfall)
- Breakdown: New Logo ARR, Expansion ARR, Downsell, Logo Churn
- YoY growth rate
- Plan vs. actual ending ARR (attainment)

Data sources: Revenue & ARR inputs, Planning / Forecast inputs

### Slide 2 — Retention
Key metrics:
- NDR (quarterly annualized)
- GDR (quarterly annualized)
- Logo retention rate
- Expansion ARR by type (upsell vs. cross-sell)

Data sources: Retention inputs, Revenue & ARR inputs

### Slide 3 — Pipeline & Sales Funnel
Key metrics:
- Pipeline $ and pipeline coverage vs. target
- Weighted pipeline coverage
- Win rate and close rate
- Forecast as % of target

Data sources: Funnel & Pipeline inputs

### Slide 4 — Unit Economics
Key metrics:
- Simple CAC and time-adjusted CAC
- Gross margin (total, subscription, services)
- LTV / CAC
- Payback period (months)
- Net and gross magic number

Data sources: Efficiency & Economics inputs

### Slide 5 — Team Productivity
Key metrics:
- NNARR per S&M FTE
- Rep attainment and team quota attainment
- QCR headcount and attrition
- Ramp rate

Data sources: Team & Productivity inputs

---

## Quarterly operating review (internal)

More granular than board deck. Organized by GTM function.

### Section A — Revenue performance
- ARR funnel waterfall (actuals vs. plan)
- Net new ARR attainment
- ARR by segment, geo, or product (if segmentation data available)
- Revenue mix (subscription vs. services)
- YoY ARR growth vs. plan

### Section B — New business
- New logo ARR (actuals vs. plan)
- Gross new logo customers
- New logo average deal size
- Win rate and close rate by segment
- Pipeline coverage and conversion rates
- Source or attribution breakdown

### Section C — Retention & expansion
- NDR and GDR by segment
- Logo retention and churn
- Expansion ARR by type (upsell, cross-sell)
- Churn reasons breakdown (if available)
- Usage / health metrics (DAU rate, adoption rate, stickiness)
- NPS / CSAT / CES (if available)
- Time to implement vs. goal

### Section D — Unit economics & efficiency
- CAC (simple and time-adjusted)
- LTV, LTV/CAC, payback period
- Net and gross magic number
- Gross margin (total, subscription, services)
- S&M OpEx per FTE

### Section E — Team & capacity
- QCR headcount (beginning, adds, departures, ending)
- Quota allocated vs. attained
- Rep attainment distribution
- Team quota attainment
- Capacity per QCR
- Ramp rate for new hires

### Section F — Forecast & plan attainment
- Ending ARR attainment
- Net new bookings attainment
- YoY ARR growth attainment
- FCF attainment (if available)
- Quarter-over-quarter trend (last 4 quarters)

---

## Metric grouping by reporting audience

| Audience | Primary metrics | Secondary metrics |
|---|---|---|
| Board | NDR, net new ARR, ARR growth, gross margin, magic number | LTV/CAC, pipeline coverage, logo retention |
| Investors (pre-IPO) | NDR, GDR, ARR growth %, gross margin, CAC payback | Rule of 40, burn multiple (if applicable) |
| CEO / Operating review | All sections A–F above | Churn reasons, ramp rate, rep distribution |
| Sales leadership | Pipeline coverage, win rate, rep attainment, team quota attainment | Close rate, SQL to closed won, capacity per QCR |
| Finance / FP&A | Plan attainment (all), magic number, CAC, gross margin | S&M OpEx per FTE, FCF attainment |
| Customer Success | NDR, logo retention, NPS, adoption rate, time to implement | CSAT, CES, churn reasons |

---

## Period conventions by metric type

| Metric family | Standard reporting period | Annualization note |
|---|---|---|
| ARR funnel | Quarter (or month) | Flows are not annualized — report as-period |
| NDR / GDR | Quarterly, annualized | Multiply quarterly flows by 4 |
| Logo retention | Quarterly or annual | Annualize if reporting quarterly |
| Pipeline | Point-in-time snapshot | Coverage is as-of, not flow |
| CAC / LTV | Quarterly | Time-adjusted CAC uses prior quarter spend |
| S&M OpEx per FTE | Annualized | Multiply quarterly spend by 4 |
| NNARR per FTE | Annualized | Multiply quarterly NNARR by 4 |
| Quota attainment | Period-specific (quarter or year) | Not annualized |
| Fiscal maturity | Period vs. plan, same period | Attainment is ratio — no annualization needed |

---

## Common formatting standards

- ARR and dollar metrics: report in thousands ($K) or millions ($M) depending on company scale
- Rates and percentages: one decimal place (e.g., 108.3% NDR, 72.4% gross margin)
- Ratios: one decimal place (e.g., 3.4× LTV/CAC, 4.2× pipeline coverage)
- Headcount: whole numbers
- Attainment: one decimal place (e.g., 94.7% ending ARR attainment)
- Always show period label (e.g., Q1 2026, FY2025) next to each metric group
- Plan vs. actual: show both columns plus variance ($ and %)
