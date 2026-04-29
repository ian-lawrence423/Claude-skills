# Example Output: New Customer SaaS Revenue Tree

Use this as the default formatting and depth template for KPI tree outputs.

---

## A. Top-line summary

**Target metric:** CY2026 New Customer SaaS Revenue, $M
**Business model:** B2B SaaS — quota-carrying field sales (US + Non-US), PoC-led motion, annual contracts
**Decomposition logic:** (US New ARR Bookings + Non-US New ARR Bookings) × CY Realization % + PoC-to-Paid Revenue
**Biggest branches:** New Customer ARR Bookings (capacity × attainment) drives ~85% of the outcome; realization timing and PoC conversion are the two adjustment factors that determine how much of booked ARR lands in-year
**Key takeaway:** The plan has two structurally distinct risks — a capacity risk (are there enough ramped reps to hit quota?) and a timing risk (does enough of the booked ARR realize within CY2026?). These compound: a late-loaded booking schedule combined with long implementation lag can create a gap even if bookings hit plan.
**Key underwriting implication:** Ramp adjustment is the most frequently misstated assumption in early-stage SaaS models. A plan that counts a rep hired in Q3 at full quota capacity overstates in-year ARR by 50–70% for that cohort. Confirm rep hire dates and ramp curves before accepting the capacity build.

---

## B. KPI tree

```
CY2026 Revenue
│
└── New Customer SaaS
    │
    ├── New Customer ARR Bookings
    │   ├── US New ARR
    │   │   ├── In-Year Quota
    │   │   │   ├── # of Quota-Carrying Reps
    │   │   │   ├── Run-Rate Quota per Rep
    │   │   │   ├── % of Quota Applicable for CY
    │   │   │   └── Ramp Adjustment
    │   │   └── Quota Attainment
    │   │
    │   └── Non-US New ARR
    │       ├── In-Year Quota
    │       │   ├── # of Quota-Carrying Reps
    │       │   ├── Run-Rate Quota per Rep
    │       │   ├── % of Quota Applicable for CY
    │       │   └── Ramp Adjustment
    │       └── Quota Attainment
    │
    ├── Realization in CY2026
    │   ├── Booking Timing
    │   ├── Implementation Lag
    │   └── Billing Start Timing
    │
    ├── PoC-to-Paid Conversion
    │   ├── % PoCs Converting
    │   ├── Conversion Timing
    │   ├── PoC Pricing vs List
    │   └── PoC Discount %
    │
    └── New Customer SaaS Revenue
        [= (US New ARR + Non-US New ARR) × Realization % + PoC-to-Paid Revenue]
```

---

## C. Driver dictionary

| Node | Parent | Definition | Formula | Unit | Owner | Cadence | Signal | Controllability | Variance lens | Evidence |
|------|--------|------------|---------|------|-------|---------|--------|----------------|--------------|----------|
| New Customer SaaS Revenue | CY2026 Revenue | Recognized revenue from new customers in CY2026 | ARR Bookings × Realization % + PoC-to-Paid Revenue | $M | Finance | Monthly | Lagging | Low | — | Historical |
| New Customer ARR Bookings | New Customer SaaS | Total ARR contracted from new logos in CY2026 | US New ARR + Non-US New ARR | $M | Sales | Monthly | Coincident | High | Volume / conversion | Historical + mgmt est |
| US New ARR | New Customer ARR Bookings | ARR booked from US-based new customers | In-Year Quota × Quota Attainment | $M | US Sales | Monthly | Coincident | High | Volume / conversion | Historical |
| In-Year Quota (US) | US New ARR | Total quota capacity available from US reps in CY2026 | # Reps × Run-Rate Quota × % Applicable × Ramp Adjustment | $M | Sales Ops | Monthly | Leading | High | Productivity | Mgmt estimate |
| # of Quota-Carrying Reps (US) | In-Year Quota (US) | Count of US reps with assigned quota at any point in CY2026 | Headcount by hire date | Count | Sales Ops / HR | Monthly | Leading | High | Volume | Historical + plan |
| Run-Rate Quota per Rep (US) | In-Year Quota (US) | Annual quota assigned to a fully ramped US rep | Quota schedule by segment/tier | $K | Sales leadership | Quarterly | Leading | High | Price / rate | Historical |
| % of Quota Applicable for CY (US) | In-Year Quota (US) | Fraction of annual quota that counts toward CY2026 based on hire timing | Months active in CY ÷ 12 | % | Sales Ops | Monthly | Leading | Medium | Timing | Mgmt estimate |
| Ramp Adjustment (US) | In-Year Quota (US) | Discount to quota capacity for reps not yet at full productivity | Ramp curve applied by cohort hire month | % of full quota | Sales Ops | Monthly | Leading | Medium | Productivity | Historical ramp curves |
| Quota Attainment (US) | US New ARR | Actual ARR booked as % of in-year quota | Booked ARR ÷ In-Year Quota | % | US Sales | Monthly | Coincident | Medium | Conversion | Historical |
| Non-US New ARR | New Customer ARR Bookings | ARR booked from non-US new customers | In-Year Quota × Quota Attainment | $M | International Sales | Monthly | Coincident | High | Volume / conversion | Historical |
| In-Year Quota (Non-US) | Non-US New ARR | Total quota capacity from non-US reps in CY2026 | # Reps × Run-Rate Quota × % Applicable × Ramp Adjustment | $M | Sales Ops | Monthly | Leading | High | Productivity | Mgmt estimate |
| # of Quota-Carrying Reps (Non-US) | In-Year Quota (Non-US) | Count of non-US reps with assigned quota | Headcount by hire date | Count | Sales Ops / HR | Monthly | Leading | High | Volume | Historical + plan |
| Run-Rate Quota per Rep (Non-US) | In-Year Quota (Non-US) | Annual quota for a fully ramped non-US rep | Quota schedule by region/tier | $K | Sales leadership | Quarterly | Leading | High | Price / rate | Historical |
| % of Quota Applicable for CY (Non-US) | In-Year Quota (Non-US) | Fraction of annual quota applicable to CY2026 | Months active in CY ÷ 12 | % | Sales Ops | Monthly | Leading | Medium | Timing | Mgmt estimate |
| Ramp Adjustment (Non-US) | In-Year Quota (Non-US) | Productivity discount for reps not yet fully ramped | Ramp curve by cohort | % of full quota | Sales Ops | Monthly | Leading | Medium | Productivity | Historical ramp curves |
| Quota Attainment (Non-US) | Non-US New ARR | Actual ARR booked as % of in-year quota | Booked ARR ÷ In-Year Quota | % | International Sales | Monthly | Coincident | Medium | Conversion | Historical |
| Realization in CY2026 | New Customer SaaS | % of booked ARR that converts to recognized revenue within CY2026 | In-year recognized revenue ÷ total ARR booked | % | Finance / Implementation | Monthly | Coincident | Medium | Timing | Historical |
| Booking Timing | Realization in CY2026 | Distribution of bookings across quarters — back-loaded bookings reduce in-year realization | % of ARR booked by quarter | % | Sales Ops | Monthly | Leading | Medium | Timing | Historical + plan |
| Implementation Lag | Realization in CY2026 | Average days from contract signature to billing start | Avg days sign-to-live | Days | Implementation | Weekly | Leading | Medium | Timing | Historical |
| Billing Start Timing | Realization in CY2026 | Days from go-live to first invoice issued | Avg days live-to-billed | Days | Finance / Ops | Monthly | Coincident | High | Timing | Historical |
| PoC-to-Paid Conversion | New Customer SaaS | Revenue contribution from PoCs converting to paid contracts in CY2026 | # PoCs × Conversion % × Avg PoC ACV × Realization % | $M | Sales / CS | Monthly | Coincident | Medium | Conversion | Mgmt estimate |
| % PoCs Converting | PoC-to-Paid Conversion | Share of active PoCs that convert to paid in CY2026 | Converted PoCs ÷ total PoCs in period | % | Sales / CS | Monthly | Coincident | Medium | Conversion | Historical |
| Conversion Timing | PoC-to-Paid Conversion | Average days from PoC start to paid contract signature | Avg days PoC-to-signed | Days | Sales | Weekly | Leading | Medium | Timing | Historical |
| PoC Pricing vs List | PoC-to-Paid Conversion | ACV of converted PoC contracts relative to list price | Converted ACV ÷ list price | % of list | Sales | Monthly | Coincident | Medium | Price / rate | Historical |
| PoC Discount % | PoC-to-Paid Conversion | Discount applied at PoC conversion relative to standard new logo pricing | (List − Converted ACV) ÷ List | % | Sales / Finance | Monthly | Coincident | Medium | Price / rate | Historical |

---

## D. Diligence view

**Explicit assumptions in the plan:**
- US rep headcount grows from X to Y by Q2 (hire dates assumed in plan) — labeled management estimate
- Ramp curve assumes 50% productivity in months 1–3, 75% in months 4–6, 100% thereafter — labeled management estimate; requires confirmation against historical actuals
- Quota attainment of 80% applied uniformly across US and Non-US — labeled management estimate
- PoC conversion rate of X% assumed based on CY2025 cohort — labeled diligence hypothesis if prior cohort data is limited

**Hidden assumptions inferred from the model:**
- % of Quota Applicable for CY is implicitly set at 100% for all current reps — does not account for any mid-year attrition or role changes
- Realization % assumes current implementation capacity scales with bookings — does not model implementation team headcount
- Non-US quota per rep is assumed equal to US in dollar terms — does not adjust for purchasing power, deal size, or sales cycle differences by region
- PoC pricing vs list is assumed to hold at current levels — no adjustment for competitive pressure or customer mix shift

**Unsupported assumptions:**
- Ramp curve applied to Non-US reps mirrors US curve — Non-US markets typically have longer ramp periods due to sales cycle length and territory build; confirm with historical Non-US cohort data
- PoC discount % held flat — if PoC pipeline is growing, discounting pressure typically increases as sales team uses PoC as a deal acceleration tool

**Branches requiring confirmatory diligence:**
- Ramp adjustment: obtain hire dates and historical ramp-to-quota curves for the last 3 rep cohorts (US and Non-US separately); verify whether plan ramp curve is achievable
- Quota attainment: obtain rep-level attainment data for trailing 8 quarters; identify whether 80% is structural or reflects a strong period
- PoC conversion: obtain PoC-to-paid conversion data by cohort for trailing 4 quarters; confirm whether conversion timing assumption is consistent with actuals

**Branches to track post-close:**
- Weekly: active PoC count, PoC conversion rate (rolling), implementation backlog, rep headcount vs. plan
- Monthly: ARR booked vs. quota by region, quota attainment by cohort, realization % vs. plan, PoC discount % trend

---

## E. Tracking pack

### Weekly (early-warning only)
| KPI | Threshold | Owner | Action if breached |
|-----|-----------|-------|-------------------|
| Implementation backlog (days) | > plan lag by 10+ days | Implementation | Capacity review; assess Q4 revenue realization risk |
| Active PoC count | < plan by > 15% | Sales / CS | Pipeline review — identify whether PoC sourcing or extension rate is the gap |
| Rep headcount vs. plan | Any hire > 30 days behind plan | Sales Ops / HR | Escalate; model impact on in-year quota capacity |
| PoC conversion rate (rolling 4-week) | < trailing 12-month average | Sales | Deal review — identify whether pricing, timing, or product is the driver |

### Monthly
| KPI | Owner | Diagnosis if off plan |
|-----|-------|----------------------|
| US New ARR booked vs. quota | US Sales | Split into capacity miss (quota shortfall) vs. attainment miss (rep productivity); diagnose separately |
| Non-US New ARR booked vs. quota | International Sales | Same split; additionally check whether miss is concentrated in one region or broad-based |
| Realization % actual vs. plan | Finance | Break into booking timing (front- vs. back-loaded quarter) vs. implementation lag vs. billing delay |
| PoC-to-paid revenue | Sales / CS | Break into conversion rate vs. ACV vs. timing; identify if discount pressure is increasing |
| Quota attainment by cohort | Sales Ops | Separate ramping reps from fully ramped reps — attainment miss in ramping cohort is timing; miss in fully ramped cohort is structural |

### Quarterly
| Theme | What to assess |
|-------|---------------|
| Ramp curve actuals vs. assumptions | Are new rep cohorts hitting productivity milestones on schedule? Revise forward capacity model if not. |
| US vs. Non-US quota productivity | Is Non-US quota per rep tracking to plan? If not, identify whether it's a market, territory, or rep quality issue. |
| PoC pipeline quality | Are PoCs converting at higher or lower ACV than new logo direct sales? Is PoC motion accretive or dilutive to ASP? |
| Booking timing distribution | Is the quarter back-loaded? A consistently back-loaded pattern structurally reduces in-year realization and creates a recurring Q1 gap. |

---

## Bad output patterns to avoid

### Too high level
```text
Revenue
├─ New Business
├─ Existing Business
└─ Other
```
Not actionable. These branches have no formulas, no owners, and cannot be tracked.

### Mirrors a spreadsheet rather than the business
```text
Revenue
├─ Rev Build Tab
├─ Assumption Block
├─ Waterfall Adj
└─ Plug
```
Label nodes using business language, not model tab names.

### Mixed economic concepts in one node
```text
Revenue
├─ Sales Productivity / Churn / Pricing
```
Each economic effect has a different owner, driver, and fix. Never collapse them.

### Stops too early on GTM nodes
```text
New Customer Revenue
└─ Sales Execution
```
"Sales Execution" is not a KPI. Decompose it into Capacity → Quota → Attainment → Conversion → Deal Size.
