# Red-Team Investment Attack Lenses

Load this file when red-teaming any Type A investment document (IC memo, deal memo,
investment thesis, CIM analysis). This file provides the specific attack lenses,
historical base rates, and adversarial question sets for each of the Six Screening
Questions. It does not replace the red-team SKILL.md methodology — it augments it
with investment-specific attack surfaces.

Read in conjunction with:
- red-team SKILL.md (Steps 1–7: full adversarial methodology)
- investment-evaluation-framework.md (Six Screening Questions as the attack surface map)

The Six Screening Questions ARE the logic tree for investment documents. Map every
attack vector to the gate it targets. Gate 1 and Gate 3 failures are typically
load-bearing kills. Gate 5 and Gate 6 failures are typically wounds or exposes.

---

## Attack Lens 1: Company Quality (Gate 1)

### Competitive Moat Attacks

**Attack: The moat is narrative, not structural**
Most investment memos assert a competitive advantage without proving the mechanism.
Attack surface: claim names a category ("switching costs") without demonstrating the
actual switching cost in dollars, time, or organizational disruption.
Base rate: In PE-backed software, ~60% of companies that claim switching cost moats
show meaningful churn when a well-funded competitor offers a migration path.
Attack type: `ASSUMPTION-KILL`
Defeat condition: Author must produce named customer evidence that customers have
been offered a competitive alternative and declined, with stated reason.

**Attack: Network effects are asserted but one-sided**
A network effect claim must show that value increases non-linearly with users.
Attack surface: "network effects" claimed for a business where value is delivered
to each user independently (e.g., a SaaS tool where users don't interact).
Attack type: `CIRCULAR`
Defeat condition: Author must demonstrate the feedback loop — how does user N+1
increase value for user N?

**Attack: Scale advantages are theoretical, not demonstrated**
Attack surface: Gross margins have not expanded as revenue grew, which contradicts
the claimed scale economy.
Attack type: `FACT-REVERSAL`
Defeat condition: Author must explain the margin trajectory and identify the specific
cost category that will inflect at stated scale.

### Customer Quality Attacks

**Attack: NRR headline masks cohort deterioration**
Attack surface: Aggregate NRR looks healthy but the most recent 2–3 cohorts have
materially lower retention than older cohorts — indicating product-market fit is
weakening or initial customers were atypical.
Base rate: In SaaS, cohort NRR declining >10 points from early to recent cohorts
is a leading indicator of competitive or product-fit erosion in ~70% of cases.
Attack type: `CHERRY-PICKED`
Defeat condition: Author must show cohort-level retention data, not just aggregate.

**Attack: Customer concentration creates binary revenue risk**
Attack surface: Top 3 customers represent >40% of revenue. Loss of any single
customer would materially impair the base case return.
Attack type: `OMISSION`
Defeat condition: Author must show contract terms (length, renewal rights, termination
clauses) and any known customer health signals for top accounts.

**Attack: Logo retention overstates health because downsells are excluded**
Attack surface: GRR is reported as strong, but if measured on logo count rather than
dollar retention, it obscures customers who renewed at lower contract values.
Attack type: `CHERRY-PICKED`
Defeat condition: Author must confirm GRR is measured on dollar value, not logo count,
and provide the dollar-weighted figure.

### Management Quality Attacks

**Attack: Track record is titles, not outcomes**
Attack surface: Management bio lists roles at notable companies but does not state
what they built, what P&L they owned, or what outcomes they produced.
Base rate: ~40% of executives who cite prior blue-chip affiliation without outcome
specifics were not in operational roles during the value-creation period.
Attack type: `NEEDS EVIDENCE`
Defeat condition: Author must name the specific business unit, the revenue or EBITDA
under management, and the outcome during that executive's tenure.

**Attack: Founding team has never operated at exit scale**
Attack surface: Company projects scaling to $X in revenue, but no management team
member has operated a business at that scale before.
Attack type: `BASE-RATE`
Defeat condition: Author must identify the specific hire or operating partner plan
that closes the capability gap before it becomes a constraint.

---

## Attack Lens 2: Sector Timing (Gate 2)

### Market Size Attacks

**Attack: TAM is top-down and self-serving**
Attack surface: Market size figure comes from a single analyst report (often
commissioned by or favorable to the industry) without bottom-up verification.
The figure has not been stress-tested against bottom-up unit economics.
Base rate: Top-down market size figures from industry reports overstate achievable
market by a median of 30–50% when compared to bottom-up calculations.
Attack type: `SELECTION-BIAS`
Defeat condition: Author must provide a bottom-up sizing and reconcile the divergence.

**Attack: Market growth rate is cyclical, not structural**
Attack surface: The CAGR cited was generated during an anomalous period (COVID
tailwinds, interest rate suppression, stimulus-driven demand) that has since reversed.
Attack type: `TIMING`
Defeat condition: Author must strip the cyclical component and show the underlying
structural growth rate.

**Attack: SAM is inflated by including segments the company cannot serve**
Attack surface: The SAM includes enterprise, mid-market, and SMB segments, but the
company's product, pricing, and GTM are only viable in one segment.
Attack type: `STRUCTURAL`
Defeat condition: Author must define SAM using only segments where the company has
demonstrated ability to win and retain customers.

### Competitive Dynamic Attacks

**Attack: The market is consolidating and the company will be squeezed**
Attack surface: Two or more well-capitalized platforms are expanding into the company's
core segment. Historical pattern in this category suggests smaller players get
displaced or forced to sell at distressed multiples within 3–5 years of consolidation.
Attack type: `BASE-RATE`
Defeat condition: Author must demonstrate a specific defensive position that makes
the company immune to platform encroachment, or reframe the exit thesis as a
consolidation target (which changes the return model).

**Attack: The competitive moat is eroding because the category is commoditizing**
Attack surface: Average selling prices in the category have declined >15% over the
last 3 years. This is inconsistent with the claimed pricing power.
Attack type: `FACT-REVERSAL`
Defeat condition: Author must explain why this company's pricing has or will diverge
from category trend, with specific mechanism.

---

## Attack Lens 3: Investment Attractiveness (Gate 3)

### Valuation Attacks

**Attack: Entry multiple assumes a re-rating that has not been earned**
Attack surface: The company is being acquired at a multiple above current public
comps for similar-quality businesses. The thesis implicitly requires further multiple
expansion at exit — a double re-rating assumption.
Base rate: Deals that require multiple expansion to achieve target returns fail to
meet base case in ~55% of PE transactions over a 10-year period (Cambridge Associates).
Attack type: `PROJECTION UNSUPPORTED`
Defeat condition: Author must show either (a) the entry multiple is justified by
a specific differentiator not reflected in public comps, or (b) the return is
acceptable at flat or compressed exit multiples.

**Attack: The comp set is cherry-picked to justify the entry price**
Attack surface: The comparable companies cited trade at premium multiples because
they have superior growth rates, margins, or market positions. The subject company
does not share the characteristics that justify those multiples.
Attack type: `CHERRY-PICKED`
Defeat condition: Author must include the full relevant comp set, not just the
favorable subset, and explain any multiple premium with specific factors.

### Return Model Attacks

**Attack: Base case requires above-historical revenue growth**
Attack surface: The projected revenue CAGR over the hold period exceeds the company's
historical growth rate and exceeds the median growth rate for comparable businesses
at similar scale.
Base rate: PE-backed companies in this revenue range and sector achieve median CAGR
of X% over 5-year holds (cite specific benchmark). The model requires Y% — a
[Z]-point premium to base rate with no stated mechanism.
Attack type: `BELOW BASE RATE`
Defeat condition: Author must identify the specific operational change that produces
above-base-rate growth, show evidence it is already underway, and cite a comparable
situation where a similar intervention produced the stated outcome.

**Attack: EBITDA expansion assumes margin improvement that contradicts cost structure**
Attack surface: The model shows EBITDA margin expanding X points over the hold period,
but the company is still investing heavily in sales and product. Operating leverage
claims are inconsistent with the stated go-to-market and R&D investment plan.
Attack type: `LOGIC-INVERSION`
Defeat condition: Author must reconcile the investment plan with the margin expansion
trajectory — specifically, at what revenue level does operating leverage produce
the stated margin improvement, and what evidence from comparable companies supports
that inflection point.

**Attack: Downside case is not a real downside**
Attack surface: The "downside" scenario still produces a positive return above the
fund's hurdle rate. A real downside case should model a scenario that tests the
investment's floor, not a modest miss.
Attack type: `CIRCULAR`
Defeat condition: Author must model a scenario where (a) revenue growth is 50% of
base case, (b) no margin expansion occurs, and (c) exit multiple compresses 2 turns.
State the IRR and MOIC under those conditions.

---

## Attack Lens 4: Exit Realization (Gate 4)

### Exit Path Attacks

**Attack: The strategic buyer universe is narrower than claimed**
Attack surface: The memo identifies 8–10 potential strategic acquirers, but most
have no demonstrated acquisition history in this category, are capital-constrained,
or have made public statements de-prioritizing M&A.
Attack type: `SELECTION-BIAS`
Defeat condition: Author must narrow to acquirers who have (a) acquired in this
category in the last 5 years, (b) have stated strategic interest, and (c) have
balance sheet capacity at the assumed exit price.

**Attack: Sponsor-to-sponsor exit requires a buyer willing to pay the same or higher multiple**
Attack surface: At the assumed exit date, the company will be larger but not
structurally different. A financial buyer will apply the same valuation methodology
as the current sponsor. Multiple expansion between sponsor transactions is rare
unless the company has crossed a quality threshold (e.g., $100M ARR, Rule of 40).
Base rate: Sponsor-to-sponsor exits in PE show median multiple expansion of <0.5x
EV/EBITDA between entry and exit for companies that have not crossed a recognized
quality threshold.
Attack type: `BASE-RATE`
Defeat condition: Author must identify the specific quality threshold the company
will cross during the hold period that justifies a higher exit multiple from
a financial buyer.

**Attack: IPO exit is speculative given market conditions and company profile**
Attack surface: The IPO exit path requires public market conditions favorable to
this sector, a company scale typically required for successful IPO (>$100M ARR,
growth >30%), and a multiple that requires public investors to pay a premium to
current private market comps. All three conditions are uncertain.
Attack type: `PROJECTION UNSUPPORTED`
Defeat condition: Author must either (a) remove IPO as a primary exit scenario or
(b) show that the company will clearly meet IPO-readiness thresholds within the
hold period under base case assumptions.

---

## Attack Lens 5: Owner Fit (Gate 5)

### Value-Add Attacks

**Attack: The claimed value-add is generic and not differentiated**
Attack surface: Claimed value-add ("operational expertise," "network," "go-to-market
support") is the same claim made by every sponsor in every deal. There is no
specific mechanism, named resource, or proven playbook that distinguishes this
sponsor's contribution.
Attack type: `CIRCULAR`
Defeat condition: Author must name the specific operating partner, the specific
playbook, and a named portfolio company where an identical intervention produced
a stated outcome.

**Attack: This sponsor has no proven track record in this sector**
Attack surface: The investment is in a sector where the sponsor has not previously
operated or exited a company. The learning curve cost is borne by this investment.
Attack type: `OMISSION`
Defeat condition: Author must acknowledge the sector learning curve and identify
the specific advisors, operating partners, or co-investors who bring sector-specific
knowledge.

---

## Attack Lens 6: Adversarial Diligence (Gate 6)

### Structural Risk Attacks

**Attack: The technology is more replicable than the moat claim suggests**
Attack surface: The core product functionality can be replicated by a well-funded
competitor within 12–18 months. The claimed switching cost is process-based, not
data or network-based — making it vulnerable to a competitor willing to absorb
migration friction for customers.
Attack type: `COMPETITIVE-RESPONSE`
Defeat condition: Author must demonstrate that the switching cost survives a
competitor that offers to absorb all migration costs and provides a 12-month
free trial. If it does not, the moat is weaker than claimed.

**Attack: Regulatory exposure has not been stress-tested**
Attack surface: The business model has regulatory exposure that has not been
addressed in the memo. Named regulatory risks (cite specific relevant regulations)
could materially impair the business model or require expensive compliance
investment that is not in the cost model.
Attack type: `REGULATORY`
Defeat condition: Author must obtain a legal opinion on the specific regulatory
exposure and model the cost of compliance or business model adaptation.

**Attack: The data room has not been independently verified**
Attack surface: Key financial and operational metrics are sourced from
management-provided materials without independent verification. Revenue figures,
churn rates, and customer counts have not been confirmed through customer reference
calls, bank statement review, or third-party data validation.
Attack type: `INCENTIVE`
Defeat condition: Author must identify which metrics have been independently
verified, by what method, and which remain management-represented only.

### Bear Case Construction

When writing the bear case for a Type A document, structure it around the
two or three gate failures that most directly collapse the return model. The
bear case is not a list of risks — it is a coherent argument that the investment
fails, structured as follows:

**Bear case structure:**
1. **Central counter-thesis** — one sentence stating why the investment fails
2. **Primary kill** — the gate failure that most directly destroys the return
3. **Compounding factor** — the second gate failure that accelerates the damage
4. **Realistic outcome** — what actually happens to the investment given the above
5. **Verdict** — direct statement of what the return looks like under the bear case

The bear case must be internally consistent. It cannot claim both that the market
is too small AND that it will attract too many competitors — pick the more
credible attack and build the coherent argument around it.

---

## Base Rate Reference Table

Use these benchmarks when assessing whether investment assumptions require
above-historical performance. Always cite the source when using in a redline.

| Metric | Median (PE-backed, comparable stage) | Top quartile | Source basis |
|--------|--------------------------------------|--------------|--------------|
| Revenue CAGR (5yr hold, $10–50M ARR SaaS) | 18–22% | 35%+ | Cambridge Associates, Bain PE Report |
| Gross margin (SaaS) | 68–72% | 78%+ | OpenView SaaS Benchmarks |
| NRR (SaaS, mid-market) | 105–110% | 120%+ | KeyBanc SaaS Survey |
| GRR (SaaS, mid-market) | 88–92% | 95%+ | KeyBanc SaaS Survey |
| EBITDA margin at exit (SaaS) | 18–24% | 30%+ | Comparable public comps |
| CAC payback (SaaS, SMB) | 12–18 months | <12 months | OpenView |
| CAC payback (SaaS, enterprise) | 18–30 months | <18 months | OpenView |
| Hold period to exit | 4.5–5.5 years | — | Bain Global PE Report |
| Entry-to-exit multiple expansion | 0.3–0.8x EV/EBITDA | — | Sponsor-to-sponsor comps |

**Note:** Always verify these benchmarks against current data before citing in a
redline. Market conditions shift benchmarks materially. These figures represent
approximate historical medians and should be updated with a web search for the
most recent published survey.

---

## Kill Criteria Template for Investment Documents

State these in Gate 6 of every investment redline. They are binary — not risks,
not sensitivities. Each is a specific finding that, if confirmed, produces a no-vote.

```
KILL CRITERION [N]
Condition: [The specific finding — stated as a binary, observable fact]
Currently: Known / Unknown / Partially known
Evidence required: [The specific data, document, or reference call that resolves this]
Responsible party: [Who obtains this before close]
Deadline: [When this must be resolved]
```

Examples of correctly stated kill criteria:
- "NRR for the most recent two cohorts is below 95%"
- "The top customer (>15% of revenue) has a termination-for-convenience clause
  exercisable within 90 days"
- "The claimed patent protection does not cover the core product workflow as
  implemented — confirmed by independent IP counsel"
- "Management equity vesting accelerates on change of control, creating a
  misalignment with the sponsor's operating plan"

Examples of incorrectly stated kill criteria (these are risks, not kills):
- "Customer concentration is high" — this is a risk level, not a binary condition
- "Market growth slows" — this is a scenario, not a kill criterion
- "Competition increases" — too vague to be actionable

---

## Quick-Reference: Highest-Frequency Investment Attacks

These attacks appear in the majority of IC documents and should be checked first:

| # | Attack | What to look for |
|---|--------|-----------------|
| 1 | TAM top-down construction | "Total market is $X billion" with no bottom-up check |
| 2 | Hockey stick projection | Year 3+ growth materially above historical trend |
| 3 | Asserted moat without evidence | "Strong network effects" with no cohort or churn data |
| 4 | Exit multiple assumption | Bull case relies on re-rating without comparables |
| 5 | Management halo transfer | Prior success cited without verifying it was the same team / context |
| 6 | Margin expansion assumption | EBITDA improvement assumed without named mechanism |
| 7 | Omitted competitive entrants | Competitive analysis frozen at point-in-time, ignores announced entrants |
| 8 | Revenue quality conflation | ARR / MRR used interchangeably with bookings or billings |
| 9 | Churn understatement | Logo churn and dollar churn reported separately; use the worse number |
| 10 | Regulatory omission | Adjacent regulatory risk (payments, data, labor) unexamined |
