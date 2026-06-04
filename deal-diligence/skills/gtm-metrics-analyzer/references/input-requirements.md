# Input Requirements

Use this file to determine what the user must provide and what can be derived.

## Always identify three categories
For every request, separate fields into:
1. **Required user-provided inputs**
2. **Optional user-provided inputs that improve accuracy**
3. **Derived calculations**

Do not blur these categories.

## 1. Company and reporting context
These should almost always be provided:
- business model
- primary revenue metric: arr, mrr, carr, bookings, billings, or gaap revenue
- reporting cadence
- time period(s)
- segmentation scheme, if applicable

## 2. Revenue and ARR inputs
Common required inputs:
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

## 3. Customer and retention inputs
Common required inputs:
- beginning customer count
- ending customer count
- new logos
- churned customers
- cohort identifiers
- churn / lost reason fields
- user counts
- adoption / usage fields
- implementation timing
- survey outputs for nps, csat, ces

## 4. Funnel and pipeline inputs
Common required inputs:
- lead counts by stage
- opportunity counts by stage
- pipeline dollars
- weighted pipeline dollars or conversion probabilities
- opportunity create date
- opportunity close date
- sales target
- forecast
- source or attribution columns

## 5. Efficiency and economics inputs
Common required inputs:
- s&m opex
- gross profit
- total revenue
- subscription revenue
- services revenue
- gross margin percent if not derivable from revenue and gross profit
- gross new logo customer count
- arr per customer
- logo churn rate
- channel spend and channel-acquired logos if channel cac is requested

## 6. Team and productivity inputs
Common required inputs:
- average s&m ftes
- quota-carrying reps
- csms
- sdrs / bdrs
- sales managers
- quota allocated
- quota attained
- reps departed
- reps fully ramped
- reps hitting quota after ramp
- qcr retention rate if capacity is requested

## 7. Plan, forecast, and maturity inputs
Common required inputs:
- actuals
- plan / budget
- forecast
- guidance
- consensus, if relevant

## Common minimum data packs

### For ARR funnel analysis
Provide at minimum:
- beginning arr
- new logo arr
- expansion arr
- downsell
- logo churn arr

Derived:
- gross new arr
- churned arr
- net new arr
- ending arr

### For retention analysis
Provide at minimum:
- bop arr
- eop arr
- expansion arr
- churned arr
- beginning customer count
- ending customer count
- churned customers

Derived:
- ndr
- gdr
- logo retention
- logo churn

### For pipeline analysis
Provide at minimum:
- pipeline dollars
- sales target
- stage counts or stage conversion rates
- weighted pipeline or forecast probabilities

Derived:
- pipeline coverage
- weighted pipeline coverage
- win rate, if closed-won and closed-lost counts are available

### For CAC / LTV / payback
Provide at minimum:
- s&m opex
- gross new logo customers
- arr per customer
- gross margin
- logo churn rate

Derived:
- simple cac
- time-adjusted cac if prior-quarter spend is available
- ltv
- ltv/cac
- payback period

### For sales productivity
Provide at minimum:
- net new arr or gross new arr
- average s&m ftes
- qcr count
- quota allocated
- quota attained

Derived:
- nnarr per s&m fte
- sales productivity
- team quota attainment
- rep attainment

## Acceptable substitutions
- Use mrr only if it can be annualized cleanly and the user is comfortable with that substitution.
- Use carr when there is meaningful lag between signing and go-live.
- If the preferred methodology uses avg(bop and eop) and one side is missing, use the available balance and state that the result is simplified.

## If data is incomplete
When required inputs are missing:
1. list the missing uploaded tables or fields,
2. calculate only what can be derived exactly,
3. mark incomplete outputs as directional or unavailable,
4. never guess missing source data silently.
