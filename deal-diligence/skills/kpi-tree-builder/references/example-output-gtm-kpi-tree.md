# Example Output — GTM KPI Tree (B2B SaaS)

Use this example when building a KPI tree for a B2B SaaS or GTM-driven business. It shows how to decompose Ending ARR into full-funnel GTM drivers and map them to an operating cadence.

---

## Example
### CY2026 Ending ARR Operating Tree

```text
CY2026 Ending ARR
├─ Beginning ARR (stock)
│
├─ Gross New ARR (acquisition branch)
│  ├─ New Logo ARR
│  │  ├─ Sales Capacity
│  │  │  ├─ Quota-Carrying Rep Count
│  │  │  ├─ Quota per Rep
│  │  │  ├─ Quota Attainment %
│  │  │  └─ QCR Retention Rate
│  │  ├─ Pipeline
│  │  │  ├─ Pipeline $
│  │  │  ├─ Pipeline Coverage
│  │  │  ├─ Weighted Pipeline Coverage
│  │  │  └─ Win Rate
│  │  ├─ Funnel
│  │  │  ├─ SQL Count
│  │  │  ├─ Close Rate
│  │  │  └─ Average Deal Size / ACV
│  │  └─ Timing
│  │     ├─ Booking Timing
│  │     └─ Implementation Lag
│  └─ Expansion ARR
│     ├─ Upsell ARR
│     │  ├─ Upsell Rate
│     │  └─ Eligible Base ARR
│     └─ Cross-sell ARR
│        ├─ Cross-sell Incidence
│        └─ Eligible Customer Count
│
├─ Churned ARR (retention branch)
│  ├─ Downsell ARR
│  │  ├─ Downsell Rate
│  │  └─ Downgraded Customer Count
│  └─ Logo Churn ARR
│     ├─ Logo Churn Rate
│     ├─ Churn by Reason (Budget / Competition / Product / Fit)
│     └─ Retention Drivers
│        ├─ Net Dollar Retention (NDR)
│        ├─ Gross Dollar Retention (GDR)
│        ├─ Logo Retention
│        ├─ Adoption Rate
│        ├─ Time to Implement vs Goal
│        └─ NPS / CSAT
│
└─ Net New ARR
   └─ Ending ARR (Calculated)
```

---

## GTM Efficiency Branch (diagnostic overlay)

These metrics are not structural branches of the ARR tree but are required for diagnosing whether the acquisition and retention engines are working. Include them in the driver dictionary and tracking pack.

```text
GTM Efficiency
├─ Economics
│  ├─ Gross Margin
│  ├─ Net Magic Number
│  ├─ Gross Magic Number
│  ├─ CAC (Simple)
│  ├─ Time-Adjusted CAC
│  ├─ LTV
│  ├─ LTV / CAC
│  └─ Payback Period (months)
└─ Team Productivity
   ├─ S&M OpEx per S&M FTE
   ├─ NNARR per S&M FTE
   ├─ Net Productivity (NNARR / QCR)
   ├─ Rep Attainment
   ├─ Team Quota Attainment
   └─ Ramp Rate
```

---

## Why this structure works

- **Separates stock and flow**: Beginning ARR (stock) → Gross New ARR + Churned ARR → Net New ARR → Ending ARR
- **Separates acquisition from retention**: Gross New ARR and Churned ARR are distinct branches with different owners and drivers
- **Separates gross and net retention**: Downsell and Logo Churn are broken out; NDR and GDR are computed metrics that overlay the structural tree
- **Decomposes vague nodes**: "Sales productivity" becomes Capacity → Quota → Attainment → Retention
- **Separates bookings from realization**: Implementation Lag is isolated so timing effects are visible
- **Keeps GTM efficiency separate**: Magic Number, CAC, LTV are diagnostic — they explain how efficiently Gross New ARR is being generated, not the outcome itself

---

## Selected driver dictionary entries

| Node | Type | Owner | Cadence | Signal | Variance Lens |
|---|---|---|---|---|---|
| Ending ARR | Output | Finance | Monthly | Lagging | All |
| Gross New ARR | Driver | Sales | Monthly | Lagging | Volume / conversion |
| Pipeline Coverage | Atomic input | RevOps | Weekly | Leading | Volume |
| Win Rate | Atomic input | Sales | Weekly | Leading | Conversion |
| Average Deal Size / ACV | Atomic input | Sales | Monthly | Coincident | Price / rate |
| Quota Attainment % | Atomic input | Sales | Monthly | Coincident | Productivity |
| QCR Retention Rate | Atomic input | Sales | Monthly | Leading | Productivity |
| Logo Churn Rate | Atomic input | Customer Success | Monthly | Lagging | Retention |
| Net Dollar Retention | Derived | Customer Success | Monthly | Lagging | Retention |
| Adoption Rate | Atomic input | Customer Success | Weekly | Leading | Retention |
| Net Magic Number | Derived | Finance | Quarterly | Lagging | Efficiency |
| LTV / CAC | Derived | Finance | Quarterly | Lagging | Efficiency |
| Payback Period | Derived | Finance | Quarterly | Lagging | Efficiency |

---

## Tracking pack (GTM operating cadence)

### Weekly
- Pipeline Coverage (vs. 3× threshold)
- Weighted Pipeline Coverage
- Win Rate (rolling 4-week)
- Adoption Rate on at-risk accounts
- At-risk account flags (churn signal)
- Implementation backlog vs. target

### Monthly
- Gross New ARR vs. plan
- New Logo ARR and Expansion ARR split
- Churned ARR (Downsell + Logo Churn)
- Net New ARR vs. plan
- Ending ARR (calculated) vs. plan
- NDR and GDR
- Logo Churn Rate by cohort
- Quota Attainment % by team
- Pipeline Coverage (beginning-of-month snapshot)

### Quarterly
- Net Magic Number
- LTV / CAC and Payback Period trends
- Cohort NDR by join quarter
- Ramp Rate for new hires
- Churn reasons (Pareto by ARR)
- Segment and product mix shifts
- Forecast vs. plan attainment (Fiscal Maturity section)

---

## Common mistakes to avoid in GTM trees

**Stopping at "Retention"**
Not enough. Decompose into Logo Churn, Downsell, Expansion, NDR, GDR, and the health signals that predict them.

**Collapsing new logo and expansion into one branch**
They have different owners (Sales vs. CSM/AM), different drivers, and different economics. Keep them separate.

**Putting CAC or Magic Number as a structural ARR branch**
These are efficiency diagnostics, not causal contributors to Ending ARR. Place them in the efficiency overlay, not the main tree.

**Treating quota attainment as the full productivity story**
Attainment × Quota × Reps = Capacity. If attainment is fine but quota is wrong, or rep count is below plan, the capacity calculation is still broken. Show all three.
