# Sea Ltd (NYSE: SE) — Worked Example

A fully populated driver tree and boundability output for Sea Ltd, current
through Q4 FY25 (reported March 2026). Use this example to see how the skill's
methodology applies in practice — particularly how Rule 5 correlations and
variance amplification show up, how the gating rules fire in a real case, and
how the cascade scenarios connect to the underlying tree.

This is a methodology illustration, not investment advice. The tier
assignments reflect a specific analyst's read of evidence at a specific point
in time. Any actual investment decision would require running the framework
fresh on current data, plus adversarial review and a separate pre-mortem pass
for out-of-tree structural risks.

---

## Cover information

- **Outcome modeled:** FY28 revenue and adjusted EBITDA
- **Decomposition basis:** Top-level segment sum (additive); within segments,
  multiplicative for revenue, additive for net result where credit costs apply
- **Time horizon:** FY26–FY28 (forecast period)
- **Vintage of analysis:** Q4 FY25 reported data (March 2026)

---

## Top-level decomposition

```
SE Revenue: $22.9B FY25 (+36.4% YoY)
├── Shopee:  $16.6B  (+33% YoY)  — 73% of revenue, ~70% of growth $
├── Monee:    $3.8B  (+60% YoY)  — 17% of revenue, ~22% of growth $
└── Garena:   $2.5B  (+37% YoY)  — 11% of revenue, ~9%  of growth $
```

Top-level structure is **additive** (segment sum). This matters because
high-variance segments (Garena binary risk, Monee dispersion) contribute to
total revenue variance only in proportion to their share. Garena variance
affects ~10% of total revenue, not 100% — which is why segment-level synthesis
matters more than headline group metrics.

| Business unit | Revenue tree | What matters |
|---------------|--------------|--------------|
| Shopee | GMV × take rate | Core valuation engine. GMV growth + take-rate expansion, profitability set by logistics and subsidy discipline. |
| Monee | Avg loan book × effective yield + fees − credit costs | Main swing unit. Book growth only matters if yield/fees hold while credit cost stays controlled. |
| Garena | Paying users × ABPU | Support unit. Cash helps, but retention is too binary to anchor base case. |

---

## Variance amplification analysis

| Tree level | Structure | Variance behavior | Implication |
|------------|-----------|-------------------|-------------|
| Top level (Shopee + Monee + Garena) | Additive | Variance is share-weighted; Garena variance contributes ~10% | Garena T4 binary risks are bounded in their effect on total revenue |
| Shopee (GMV × Take Rate) | Multiplicative | Highest-variance leg dominates: A4 (T3 GMV mix) > B2 (T1 take rate) | A4 dominates Shopee variance — the load-bearing risk driver is the messy one (geographic mix), not the clean one (ads) |
| Monee (Book × Yield − Losses) | Mixed | C-losses sit on a separate additive branch; high variance in C2/C3 directly hits net Monee result | Cohort seasoning + provisioning are more consequential than tier alone suggests |
| Garena (DAU × ABPU) | Multiplicative | Binary A1 (Free Fire DAU) dominates regardless of ABPU stability | Garena variance ≈ Free Fire variance; ABPU bounding doesn't reduce thesis risk |

**Key insight:** SE's tree contains both multiplicative and additive nodes.
Variance flows differently through each. The Shopee multiplicative node means
A4 (T3 TikTok mix) is the actual load-bearing driver for Shopee variance —
not B2 (T1 ad take rate) — even though B2 is the cleaner story. The thesis
"rests on Shopee ad monetization" is rhetorically appealing but mathematically
wrong: Shopee variance rests on geographic mix.

---

## Shopee — driver table

**FY25 baseline:** GMV $127B; 400M active buyers; 20M sellers. Revenue $16.6B
(+33% YoY). Adjusted EBITDA $881M (vs. $156M FY24) — nominal margin 0.7%.
Q4 FY25 EBITDA growth (+33%) lagged revenue growth (+36%); margins peaked at
0.9% Q1 FY25 then trended lower. FY26 guidance: GMV +25%, full-year adjusted
EBITDA at least flat in absolute dollars (i.e., explicit margin compression).

| Driver | Historical | Today | Underwritten path | Tier | Impact | Boundability |
|--------|-----------|-------|-------------------|------|--------|--------------|
| A1. Buyer count | ~295M (FY22) → ~400M (FY25) | 400M active buyers | Low-double-digit buyer growth; Brazil drives mix | T1 | High | Directly reported; range is tight |
| A2. Order frequency | Orders outgrew GMV consistently | Orders +30.5% YoY Q4 | Orders stay ahead of buyers; volume-led GMV | T2 | High | Trend visible; ceiling not |
| A3. AOV | Flat/down as mix skewed lower-ticket | Flat to slightly down | AOV stays soft; no major recovery needed | T2 | Medium | Starting point visible; recovery path less certain |
| A4. Geographic mix | Vietnam worsened while Brazil scaled | Vietnam GMV share fell 61% → 56% as TikTok reached ~41% | Core SEA holds better than Vietnam; Indonesia is the canary | **T3** | **Very High** | Main competitive variable; spillover not tightly bounded |
| B1. Commission | Step-up over time; Brazil reset Mar-26 | Brazil pricing reset implemented | Modest ongoing take-rate lift | T2 | Medium | Observable; seller pushback caps range |
| B2. Ad revenue | Accelerated sharply through FY24–25 | +70% YoY Q4; +80bps FY25 take-rate lift | Ad take rate keeps climbing from ~2% toward peer 4–6% | **T1** | **Very High** | Best-bounded positive driver; multiple analog companies |
| B3. VAS | Rebates normalized from elevated levels | Logistics rebates $180M → $121M YoY | Small positive take-rate tailwind | T2 | Medium | Direction measurable; impact smaller than ads |
| B4. Seller services | Proof in Malaysia; Brazil still early | MY FBS uplift disclosed; Brazil not yet | Some fulfillment monetization, not core to base case | T3 | Medium | Needs more market-specific proof |

**Reading the Shopee table.** B2 (ads) is the cleanest positive lever — T1
with multiple peer analogs (Amazon at ~6%, Mercado Libre at 2%+, Alibaba
historical paths) and current Shopee take rate ~2% with +80bps FY25 expansion.
A4 (geographic mix vs. TikTok) is the dominant unresolved risk — T3, with
Vietnam already showing what TikTok can take.

**Driver correlation flag (Rule 5):** A1, A2, and B2 share an upstream cause
through subsidy mechanics. Independent flexes overstate diversification. If
subsidy spend is cut (a likely response to TikTok pressure), buyer growth,
frequency, AND ad take-rate growth all soften together. A bear scenario must
move them as a cluster.

---

## Monee — driver table

**FY25 baseline:** Loan book $9.2B (+80% YoY). Revenue $3.8B (+60% YoY) on
~37M active credit users. Adjusted EBITDA $1.0B (+24.7%) — EBITDA growth
lagged revenue growth materially because credit-loss provisions rose 66.7%
YoY. Reported NPL90+ stable at 1.1%. Off-Shopee SPayLater: >300% YoY growth,
now >15% of portfolio (~30% in Malaysia). Funding: $2.7B of FY25 loans funded
directly from Sea balance sheet — a real constraint, not a hypothetical.

| Driver | Historical | Today | Underwritten path | Tier | Impact | Boundability |
|--------|-----------|-------|-------------------|------|--------|--------------|
| A1. Borrower count | Scaled rapidly through FY25 | +20M first-time borrowers; ~37M active credit users | Penetration rises from low base | T2 | High | Current penetration visible; ceiling not |
| A2. Avg loan size | Aggregate ticket increased | Aggregate up; cohort detail not disclosed | Modest ticket-size trade-up | T3 | Medium | Headline visible; cohort economics not |
| A3. Product mix | Broadened beyond BNPL | Mix disclosure limited | Mix shifts gradually toward higher-value products | T3 | High | Mix changes alter yield AND risk |
| B1. APR | Held within local caps | Bounded by regulatory caps | Yield stays healthy within caps | T2 | Medium | Public caps help bound the range |
| B2. Fee income | Present but poorly disclosed | Limited disclosure | Fees grow with scale; not core | T3 | Low | Not visible enough to underwrite tightly |
| B3. Off-Shopee origination | Strategically discussed; not yet quantified through FY24 | >15% of portfolio (~30% MY); +300% YoY in FY25 | Continues scaling toward 25–30% of book | **T2** | High | UPGRADED from T4: now disclosed; G3 triangulation gap remains |
| C1. Reported NPL90+ | Stayed low during rapid growth | 1.1%, stable | Reported losses stay optically controlled near term | T1 | High | Directly reported, but only point-in-time; G2 floor applies to the inference |
| C2. Cohort seasoning | No disclosed cohort history through full cycle | Seasoning risk not visible in disclosed cohorts | Losses rise modestly as book matures | **T3** | **Very High** | G2 gating: track record = 0; main make-or-break |
| C3. Provisioning trajectory | Credit-loss provisions rose with book | +66.7% YoY Q4 FY25 | Provisioning catches up to book growth; EBITDA margin compresses | T2 | Very High | Now visible; trajectory is the leading indicator for C2 |

**Reading the Monee table.** B3 has been upgraded from T4 to T2 since earlier
analysis — Sea now discloses off-Shopee SPayLater share, so the strategic
claim that was previously qualitative now has a specific number. C3
(provisioning trajectory) is a new explicit row — Q4 provisions rose 66.7%
YoY while reported NPL stayed at 1.1%, which is the canonical pattern of a
book outgrowing its loss recognition. C2 (cohort seasoning) remains the
dominant unbounded driver: the 1.1% NPL is mathematically suppressed by the
80% YoY denominator growth, and no SEA EM consumer fintech has been observed
through a full cycle since 2008–09.

**Structural quirk worth flagging:** Funding constraint is now material, not
hypothetical. Sea funded $2.7B of FY25 loans directly from its balance sheet.
If Shopee EBITDA does not generate enough cash to keep funding Monee growth,
Monee growth must decelerate or Sea must shrink its cash balance. This
linkage was implicit in earlier analyses; current disclosure makes it
explicit and creates a direct cascade pathway from Shopee margin pressure to
Monee loan-book growth.

---

## Garena — driver table

**FY25 baseline:** Bookings $2.9B (+37% YoY) — second consecutive year of
>30% Free Fire bookings growth. ~100M average DAU, ~65M paying active users.
ABPU improved from $0.88 to $1.06. Adjusted EBITDA $1.7B (+25.5%) on margin
expansion. Q4 FY25: bookings +23.8% YoY, but DAU and bookings declined
sequentially Q4 vs Q3 — a yellow flag for late-cycle franchise dynamics.

| Driver | Historical | Today | Underwritten path | Tier | Impact | Boundability |
|--------|-----------|-------|-------------------|------|--------|--------------|
| A1. Free Fire DAU | Large for years; recent late-period decline risk visible | ~100M avg DAU; Q4 FY25 QoQ decline | Game stays cash-generative through FY26; no credit beyond | **T4** | Medium | Current DAU visible; durability not forecastable |
| A2. New titles | No second major engine emerged | EA Sports FC Mobile launched Vietnam; no material disclosed contribution | Zero in base case | T4 | Low | Should not be underwritten ex ante |
| A3. Paying users | +15% FY25 | ~65M paying actives | Payer base stable to up | T2 | Medium | Reported and comparable to peers |
| B1. Spend per payer | ABPU $0.88 → $1.06 | $1.06 ABPU | ABPU holds near current level or edges up | T2 | Medium | Observable trend with reasonable bounds |
| B2. Collaborations | Episodic IP partnerships | Naruto, Squid Game collabs FY25 | Not needed in base case | T3 | Low | Event-driven; not recurring enough to credit heavily |

**Reading the Garena table.** Free Fire delivered two consecutive years of
>30% bookings growth, which is genuinely impressive for a 9-year-old F2P
title — but the Q4 sequential decline is the canonical pattern for
late-franchise softness. Treating A1 as binary T4 captures the correct shape:
either Free Fire continues with elevated retention (revenue continues), or
audience attention shifts (revenue collapses with deferred-revenue
write-downs that can produce negative reported revenue). The base rate for
F2P titles sustaining peak revenue 5+ years past launch is ~20%; the current
run is statistically lucky, not a model.

---

## Base-rate overlay

| Driver | Tier | Reference class | Base rate | Implied stance |
|--------|------|-----------------|-----------|----------------|
| Shopee B2 — Ad take rate scaling toward 5% | T1 | Marketplaces reaching mature ad monetization (Amazon, MercadoLibre, Alibaba historical paths) | ~70% of marketplaces with sustained GMV scale eventually reach 4–6% ad take rate | Tier and base rate aligned; high confidence |
| Monee — Loan book grows 60% with stable losses through cycle | T2 | EM consumer fintech books growing >50% annually entering first credit cycle | ~25% maintain stable loss rates through first cycle | Tier and base rate diverge sharply; thesis is betting on top-quartile outcome |
| Shopee A4 — Indonesia GMV share holds despite TikTok | T3 | Two-player marketplace dynamics where new entrant reaches 25%+ share within 3 years | ~40% of incumbents retain dominant share | Tier reflects evidence weakness; base rate mildly unfavorable |
| Garena — Free Fire revenue continues at current run rate through FY28 | T4 | F2P games with >5 years of peak revenue history sustaining revenue 3+ more years | ~20% sustain (most decline meaningfully) | Both tier and base rate adverse; thesis should price in zero contribution |

**Note on sourcing.** The base rates above are illustrative reference-class
benchmarks. A production version of this analysis would cite specific studies,
regulator data, or peer disclosure for each base rate. This is an open issue
in the worked example — see framework self-audit below.

---

## Vintage check

| Driver | Tier | Vintage | Decay risk | Re-validation action |
|--------|------|---------|------------|----------------------|
| Shopee B2 — Ad take rate trajectory | T1 | ~3 months (Q4 FY25) | Low | Standard quarterly refresh |
| Shopee A4 — Vietnam as leading indicator for Indonesia | T3 | ~12 months (2024–25 GMV share data) | High | Indonesia regulatory landscape changed materially in 2025; analog comparability degraded |
| Monee C1 — Reported NPL90+ at 1.1% | T1 | ~3 months (Q4 FY25) | Low for metric, high for inference | Metric is fresh; inference that it predicts future losses is itself stale (no SEA EM consumer fintech observed through full cycle since 2008–09) |
| Monee B3 — Off-Shopee origination share | T2 | ~3 months (Q4 FY25) | Low | Now disclosed; trajectory tracking trivial going forward |
| Garena A3 — Paying user conversion | T2 | ~3 months | Medium | F2P monetization patterns shifting industry-wide with regulatory pressure on loot boxes |
| Shopee B4 — FBS Brazil uplift | T3 | ~18 months (initial Malaysia ramp) | High | Approaching threshold; Brazil applicability requires fresh primary research |

The vintage discipline is most uncomfortable when applied to "obviously still
true" drivers. C1 reported NPL is fresh, but the inference it supports —
credit losses will remain at this level — depends on a relationship that has
never been observed through a stress event. Vintage analysis surfaces this
exact gap: a fresh metric supporting a stale inference is not the same as a
well-bounded driver.

---

## Downside cascade — TikTok competitive trigger

**Trigger:** Shopee GMV growth decelerates from 27% (FY25) to 12% (FY26) due
to TikTok displacement reaching ~32% share across Indonesia, Thailand, and
Philippines. This is the A4 driver moving to its T3 stress range.

| Step | Cascade leg | Mechanism | Lag | Type |
|------|-------------|-----------|-----|------|
| 1 | Shopee GMV slows to 12% | Trigger — TikTok share gain in three SEA markets | T+0 | Trigger |
| 2 | Ad take rate growth stalls at +30bps | Multiplicative GMV × take-rate effect; subsidy cuts reduce seller acquisition into the ad funnel | T+1Q to T+2Q | Mechanical |
| 3 | Working capital float reverses | Payables-funded float requires GMV growth to sustain; below ~15% GMV growth, the float reverses from tailwind to headwind | T+1Q to T+2Q | Mechanical |
| 4 | FCF conversion drops 151% → ~85% of EBITDA | WC reversal directly hits FCF; compounds with margin pressure as fixed costs do not flex | T+2Q | Mechanical |
| 5 | Monee funding capacity tightens | Monee growth substantially funded by Shopee FCF + Sea balance sheet. With FCF dropping, parent injection capacity falls — the $2.7B annual balance-sheet funding is not sustainable in this scenario | T+2Q to T+3Q | Mechanical |
| 6 | Monee loan book growth slows from 80% to 30% | Combination of capital constraint and credit-tightening response to early loss signals | T+3Q to T+4Q | Behavioral |
| 7 | Cohort seasoning losses surface | Existing book continues seasoning regardless of new origination volume. Denominator stops growing while numerator rises. NPL ratio surfaces honestly. | T+4Q to T+6Q | Mechanical |
| 8 | Monee EBITDA contracts 60–80% | Mechanical from steps 5+7: revenue growth slows while loss provisioning rises. Operating leverage works in reverse. | T+5Q to T+7Q | Mechanical |
| 9 | Multiple compresses 30–40% | Market reprices to lower growth + higher risk. Reflects in EV/EBITDA going from ~22x to ~14x on already-lower EBITDA base. | T+6Q to T+8Q | Behavioral |

---

## Upside cascade — Ad take-rate inflection

**Trigger:** Shopee ad take rate inflects to ~3% of GMV (from current ~2%) by
end FY26, ahead of guidance, on continued seller demand and AI-powered
shopping agent rollout. This is B2 moving from T1 base case to T1 upside.

| Step | Cascade leg | Mechanism | Lag | Type |
|------|-------------|-----------|-----|------|
| 1 | Ad take rate inflects to ~3% of GMV | Trigger — ad seller demand accelerates faster than current trajectory | T+0 | Trigger |
| 2 | Shopee EBITDA margin expands beyond 1% | High-margin ad revenue lifts segment margin | T+1Q | Mechanical |
| 3 | Subsidy budget expands | Higher ad-funded margin allows subsidy reinvestment without margin sacrifice | T+1Q to T+2Q | Behavioral |
| 4 | Buyer growth + order frequency accelerate | Subsidy-driven flywheel — Rule 5 correlation operates in the upside direction | T+2Q to T+3Q | Behavioral |
| 5 | FCF conversion stays above 150% | Working capital float stays favorable; FCF available for Monee | T+2Q | Mechanical |
| 6 | Monee funding capacity expands | Reduced parent-balance-sheet draw; more headroom for off-Shopee scaling | T+3Q to T+4Q | Mechanical |
| 7 | Multiple expands toward 28–30x | Market reprices on durability of margin expansion + Monee runway | T+4Q to T+6Q | Behavioral |

---

## Illustrative cascade quantification

| Metric | Base case (FY26) | Downside cascade | Upside cascade |
|--------|------------------|------------------|----------------|
| Shopee revenue | $22.0B | $18.5B (-16%) | $24.5B (+11%) |
| Shopee EBITDA | $1.5B | $0.8B (-47%) | $2.4B (+60%) |
| Monee revenue | $5.5B | $3.8B (-31%) | $6.5B (+18%) |
| Monee EBITDA | $1.4B | $0.4B (-71%) | $2.0B (+43%) |
| Garena EBITDA | $1.7B | $1.4B (-18%) | $1.8B (+6%) |
| **Total adjusted EBITDA** | **$4.6B** | **$2.6B (-43%)** | **$6.2B (+35%)** |
| EV/EBITDA multiple | ~22x | ~14x | ~28x |
| **Implied EV** | **~$100B** | **~$36B (-64%)** | **~$174B (+74%)** |

**The math is illustrative, not predictive.** A single trigger event running
through 8–9 cascade legs produces an enterprise-value impact roughly 2x the
impact of any single-driver stress test. The asymmetry is meaningful — the
downside (-64%) is larger than upside (+74%) only because the starting
multiple already reflects optimistic assumptions; if multiples were already
compressed, the asymmetry would invert. Both cascades are required reading.

---

## Carry-forward

| Driver | Tier | What would bound it | Gettable? |
|--------|------|---------------------|-----------|
| Shopee A4 — TikTok geographic mix in Indonesia | T3 | Quarterly GMV share data by SEA country (not just MAU); seller cross-listing rates; Indonesia GMV trajectory through FY26 | Partial — Momentum Works publishes parcel volume; full GMV by country requires waiting |
| Monee C2 — Cohort seasoning | T3 | NPL by origination cohort with vintage curves; product-mix-adjusted loss rates; comparable EM bank seasoning analogs | Yes — primary research with credit analysts and SE Asia consumer fintech operators |
| Monee A3 — Product mix | T3 | Disclosed split between BNPL / SME / cash-loan products with respective yield and NPL profile | Hard — Sea has not historically disclosed product-mix detail |
| Garena A1 — Free Fire DAU durability | T4 | Genuinely unforecastable. Right action: assume zero contribution from Free Fire in base case beyond FY26 | No — accept and price accordingly |
| Shopee B4 — FBS Brazil uplift | T3 | Brazil-specific FBS seller order uplift data; comparable Malaysia ramp curve | Partial — management may disclose; expert network calls with Brazil sellers can corroborate |

---

## Framework self-audit

Four explicit acknowledgments of framework limits in this worked example:

**1. Out-of-tree structural risks.** This analysis addresses analytical risk
(driver evidence quality and range). It does NOT address structural risks
that sit outside the driver tree: regulatory action in Indonesia (social
commerce rules) or Brazil (consumer credit caps), a Sea balance-sheet
funding crisis, Free Fire franchise crystallization triggering deferred-
revenue write-downs, or capital-market stress affecting all SEA EM operators.
A separate `pre-mortem` pass is required for any of these.

**2. Boundability is not probability.** Tiers describe how narrow the
plausible range is, not how likely the point estimate is. Shopee B2 (T1) at
the underwritten path "ad take rate keeps climbing from ~2% toward peer 4–6%"
can still land outside that range. Monee C2 (T3) at "losses rise modestly as
book matures" has a wide range, but can still land in the middle. The two
should not be conflated.

**3. Inter-rater calibration is untested.** Two analysts looking at the same
SE evidence could plausibly assign A4 (TikTok geographic mix) a T2 or a T4 —
the difference between sensitivity and unbounded is the entire thesis. The
gating rules + 5-dimension rubric reduce range of disagreement, but a
calibration exercise has not been run on this specific case.

**4. Base-rate sources are not cited.** The reference classes and base rates
in Section 5 are reasonable but not yet auditable. A production version
would cite specific studies, regulator data, or peer disclosure for each.
Open issue.

---

## Key insights from this worked example

For an analyst learning the methodology, three observations from SE are worth
internalizing:

**Variance amplification matters.** The cleanest driver in the SE tree (B2
ads, T1) is not the load-bearing driver for variance — A4 (TikTok mix, T3) is.
The thesis "rests on Shopee ad monetization" is rhetorically appealing but
mathematically wrong. The framework would catch this in any tree where
multiplicative nodes contain mixed-tier children.

**The leading-indicator fallacy is real.** The Vietnam GMV share data is
observable and tempts analysts to upgrade A4 to T2. But the question that
matters is whether Indonesia follows Vietnam — which is genuinely T4 because
the comparability is contested. Keep the tier where the actual decision-
relevant variable sits, not where the proxy data lives.

**Tier upgrades happen.** Monee B3 moved from T4 to T2 between the v6 and v7
analyses because Sea started disclosing off-Shopee SPayLater share. Drivers
are not static — vintage discipline (Section 6) catches stale tier
assignments going stale; disclosure-driven upgrades like B3 are the
opposite case where tiers improve as evidence becomes available.
