# GTM Metric Formulas

Human-readable formula reference for all 48 derived metrics in the workbook. Used by SKILL.md Step 3 as the calculation source of truth. For the Excel formula implementations (XLOOKUP-based), see `assets/build_template.py`.

---

## Methodology notes

- **Quarterly annualization**: multiply a single-quarter flow by 4 to annualize. Used for NDR, GDR, S&M OpEx per FTE, and NNARR per FTE.
- **Average balance**: use avg(BOP, EOP) as the denominator for NDR, GDR, logo retention, and logo churn. If only one side is available, use it and flag as simplified.
- **Time-adjusted CAC**: uses prior-quarter S&M OpEx against current-quarter new logos. This is the preferred methodology; simple CAC (same-period) is the fallback.
- **Logo churn rate**: annualized. If provided directly, use it; if not, derive from churned customers / avg customers (annualize if quarterly).
- **Gross margin**: prefer derived (gross profit / revenue) over direct input to ensure consistency with reported financials.

---

## 1. Growth Drivers

| Metric | Formula | Required Inputs | Notes |
|---|---|---|---|
| Gross New ARR | New Logo ARR + Expansion ARR | new_logo_arr, expansion_arr | Top of the ARR funnel |
| Churned ARR | Downsell ARR + Logo Churn ARR | downsell_arr, logo_churn_arr | Gross churn; do not net against expansion |
| Net New ARR | Gross New ARR − Churned ARR | All four ARR flow inputs | Core growth metric |
| Ending ARR (Calculated) | Beginning ARR + Net New ARR | beginning_arr + all four flows | Cross-check against reported ending ARR |
| ARR Growth YoY % | (EOP ARR / EOP ARR prior year − 1) × 100 | Requires prior-year EOP ARR | Directional only if prior-year data unavailable |
| % Gross New ARR from New Logo | New Logo ARR / Gross New ARR | new_logo_arr, expansion_arr | Acquisition vs. expansion mix |
| % Gross New ARR from Expansion | Expansion ARR / Gross New ARR | new_logo_arr, expansion_arr | Complement to new logo mix; both must sum to 100% |

---

## 2. Sales Funnel

| Metric | Formula | Required Inputs | Notes |
|---|---|---|---|
| Pipeline Coverage | Pipeline $ / Sales Target | pipeline_dollars, sales_target | Unweighted; benchmark 3–5× for mature SaaS |
| Weighted Pipeline Coverage | Weighted Pipeline $ / Sales Target | weighted_pipeline_dollars, sales_target | Preferred over unweighted; benchmark 1.5–2.5× |
| Win Rate | Closed Won / (Closed Won + Closed Lost) | closed_won_opportunities, closed_lost_opportunities | Stage-based; use same-cohort won/lost |
| Close Rate | Closed Won (same period) / Opportunities Created (same period) | closed_won_same_period, opportunities_created | Period-matched; complementary to win rate |
| SQL to Closed Won | Closed Won SQLs / SQL Count | closed_won_sql, sql_count | Full funnel conversion |
| Forecast as % of Sales Target | Forecast $ / Sales Target | forecast_dollars, sales_target | Below 0.85× signals coverage risk |

---

## 3. Retention

| Metric | Formula | Required Inputs | Notes |
|---|---|---|---|
| Quarterly Annualized NDR | 1 + ((Qtr Expansion ARR − Qtr Churned ARR) × 4) / avg(BOQ ARR, EOQ ARR) | beginning_arr, ending_arr, expansion_arr, downsell_arr, logo_churn_arr | ICONIQ preferred methodology; annualizes quarterly flows |
| Quarterly Annualized GDR | 1 − (Qtr Gross Churned ARR × 4) / avg(BOQ ARR, EOQ ARR) | beginning_arr, ending_arr, downsell_arr, logo_churn_arr | GDR excludes expansion; capped at 100% |
| Logo Retention | 1 − Churned Customers / avg(BOP Customers, EOP Customers) | bop_customers, eop_customers, churned_customers | Dollar and logo retention should be tracked separately |
| Logo Churn | Churned Customers / avg(BOP Customers, EOP Customers) | bop_customers, eop_customers, churned_customers | Complement to logo retention |
| DAU Rate (Active User Rate) | DAU / Total Users | dau, total_users | Engagement signal |
| MAU Rate | MAU / Total Users | mau, total_users | Breadth of engagement |
| Adoption Rate | Feature Active Users / Total Users | feature_active_users, total_users | Feature-specific penetration |
| Stickiness Rate | DAU / MAU | dau, mau | Depth vs. breadth; benchmark 20–40%+ for sticky products |
| Time to Implement vs Goal | Actual Implementation Days / Expected Implementation Days | actual_implementation_days, expected_implementation_days | >1.0 = behind schedule |
| NPS | Promoter % − Detractor % | promoter_pct, detractor_pct | Range −100 to +100; benchmark 30–50+ for SaaS |
| CSAT | Satisfied Responses / Total Responses | satisfied_responses, total_responses | Usually >80% target |

---

## 4. Efficiency & Economics

| Metric | Formula | Required Inputs | Notes |
|---|---|---|---|
| Gross Margin | Gross Profit / Total Revenue | gross_profit, total_revenue | Derive rather than accept direct input where possible |
| Subscription Gross Margin | Subscription Gross Profit / Subscription Revenue | subscription_gross_profit, subscription_revenue | Blended margin can mask structural services drag |
| Services Gross Margin | Services Gross Profit / Services Revenue | services_gross_profit, services_revenue | Often below 20%; flag if negative |
| Net Magic Number | Quarter Net New ARR / Prior Quarter S&M OpEx | net_new_arr (derived), prior_qtr_sm_opex | Preferred: lagged S&M spend. Benchmark >0.75 |
| Gross Magic Number | Quarter Gross New ARR / Prior Quarter S&M OpEx | gross_new_arr (derived), prior_qtr_sm_opex | Ignores churn; use alongside net magic number |
| Simple CAC | S&M OpEx / Gross New Logo Customers | sm_opex, gross_new_logo_customers | Same-period; directional fallback if prior-period not available |
| Time-Adjusted CAC | Prior Quarter S&M OpEx / Current Quarter Gross New Logo Customers | prior_qtr_sm_opex, gross_new_logo_customers | Preferred; accounts for sales cycle lag |
| Simple LTV | (ARR per Customer × Gross Margin) / Logo Churn Rate | avg_arr_per_customer, gross_margin, logo_churn_rate | Annualized churn rate; use derived logo_churn if not provided |
| LTV / CAC | Simple LTV / Time-Adjusted CAC (or Simple CAC) | All LTV and CAC inputs | Benchmark >3× for capital-efficient SaaS |
| Payback Period | CAC / (ARR per Customer × Gross Margin) | avg_arr_per_customer, gross_margin, cac | In years; benchmark 1–2 years for capital-efficient SaaS |

---

## 5. Team & Productivity

| Metric | Formula | Required Inputs | Notes |
|---|---|---|---|
| S&M OpEx per S&M FTE | (Quarter S&M OpEx × 4) / Average S&M FTEs | sm_opex, avg_sm_ftes | Annualized quarterly spend |
| AE per CSM | Quota-Carrying Reps / CSMs | qcr_count, csm_count | Ratio; benchmark 4–8× depends on segment |
| AE per Sales Manager | Quota-Carrying Reps / Sales Managers | qcr_count, sales_manager_count | Ratio; benchmark 6–10× |
| AE per SDR | Quota-Carrying Reps / SDRs | qcr_count, sdr_count | Ratio; benchmark 2–4× |
| Employee Attrition | QCRs Departed / Average QCRs in Period | qcr_departed, qcr_count | Annualize if reporting quarterly |
| NNARR per S&M FTE | (Net New ARR × 4) / Average S&M FTEs | net_new_arr (derived), avg_sm_ftes | Annualized; primary FTE productivity metric |
| Sales Capacity | Allocated Quota × Quota Attainment % × QCR Retention Rate | quota_allocated, quota_attained, qcr_retention_rate | Forward-looking capacity model |
| Capacity per QCR | Sales Capacity / QCR Count | All capacity inputs, qcr_count | Per-rep expected output |
| Net Productivity | Net New ARR / Average QCRs | net_new_arr (derived), qcr_count | Per-rep net output; account for ramp |
| Team Quota Attainment | QCRs attaining 100%+ / Total QCRs | qcrs_attaining_100, qcr_count | Distribution metric; >60% attainment is benchmark |
| Rep Attainment | Quota Attained / Quota Allocated | quota_attained, quota_allocated | Team-level aggregate; distinguish from team quota attainment |
| Ramp Rate | Reps hitting quota in first fully ramped period / Reps in first fully ramped period | reps_hit_quota_first_full_ramp, reps_first_full_ramp_period | Only count the first full ramp period |

---

## 6. Fiscal Maturity

| Metric | Formula | Required Inputs | Notes |
|---|---|---|---|
| Net New Bookings Attainment | Actual Net New ARR / Plan Net New Bookings | net_new_arr (derived), plan_net_new_bookings | ARR used as bookings proxy if bookings not available |
| Gross New Bookings Attainment | Gross New ARR / Plan Gross New Bookings | gross_new_arr (derived), plan_gross_new_bookings | |
| Ending ARR Attainment | Actual Ending ARR / Plan Ending ARR | ending_arr (or calculated), plan_ending_arr | Use calculated ending ARR if reported not available |
| YoY ARR Growth Attainment | Actual YoY ARR Growth % / Plan YoY ARR Growth % | actual_yoy_arr_growth_pct, plan_yoy_arr_growth_pct | Requires both actual and plan growth rates |
| Free Cash Flow Attainment | Actual FCF / Plan FCF | actual_fcf, plan_fcf | Sign-aware: negative FCF attainment = worse than plan |
| Beat Against Revenue Guidance | (Actual Revenue / Revenue Guidance) − 1 | revenue, revenue_guidance | Public company context; positive = beat |
| Beat Against Revenue Consensus | (Actual Revenue / Consensus Estimate) − 1 | revenue, consensus_estimate | Public company context only |

---

## Benchmark reference

| Metric | Seed / Early | Series B | Growth (>$50M ARR) | Public |
|---|---|---|---|---|
| NDR | >90% | >100% | >110% | >120% |
| GDR | >80% | >85% | >90% | >90% |
| Logo retention | >80% | >85% | >90% | >90% |
| Gross margin | >60% | >65% | >70% | >70–80% |
| Net magic number | >0.5 | >0.75 | >1.0 | >1.0 |
| CAC payback | <24 mo | <18 mo | <12–18 mo | <12 mo |
| LTV/CAC | >2× | >3× | >3–5× | >5× |
| Pipeline coverage | 3–5× | 3–5× | 3–5× | 3–5× |
| Rep attainment | — | >50% | >60% | >65% |
| Team quota attainment | — | >50% | >60% | >65% |

> Benchmarks are directional ranges based on ICONIQ and industry norms. Stage, business model, and segment affect materially. Flag comparisons as estimates.
