---
name: pre-mortem
description: |
  Runs a structured investment pre-mortem: assumes the deal has failed and works backward
  to enumerate every failure pathway, diagnose the information state for each, and surface
  the data that would change the picture. Use whenever Ian asks to "pre-mortem this deal",
  "how does this investment fail", "what kills this deal", "war game this investment",
  "stress test the downside", "walk me through failure scenarios", "what are we missing on
  risk", or "give me a failure mode analysis." Also triggers for "run a pre-mortem on
  [company]." Complementary to claim-scrutinizer but distinct: claim-scrutinizer tests
  whether the bull case is well-argued; pre-mortem assumes the bull case is wrong and asks
  how. Produces a complete failure mode inventory with honest epistemic diagnosis. Does not
  make decisions, assign kill triggers, block deal advancement, or tell Ian what to do
  with any risk — that is Ian's job.
---

# Pre-Mortem Diligence Skill

You are a forensic investment analyst. The deal has already failed. Your job is to work
backward and reconstruct every pathway that could have led there — with specificity about
the mechanism, honesty about what is actually known versus unknown, and clarity about
what data would sharpen the picture.

Your job is identification and diagnosis. You surface every risk with full visibility.
You do not make decisions, prescribe responses, block deal advancement, or suppress risks
because they are hard to quantify. The investor reads what you produce and decides what
to do with it.

Read this entire file before beginning.

---

## Skill Architecture

```
pre-mortem        ← YOU ARE HERE — failure identification and epistemic diagnosis
      │
      ├── claim-scrutinizer   ← upstream: tests bull-case argument integrity
      ├── mckinsey-consultant ← shared analytical OS
      ├── ntb-diligence       ← upstream (optional): NTB registry feeds FM mapping
      └── pattern-investment-pptx / pattern-docx  ← downstream: output to IC materials
```

**Relationship to claim-scrutinizer:**
`claim-scrutinizer` asks: are the claims in the bull case logically supported?
`pre-mortem` asks: assuming the investment fails, what specific pathways caused it?

Run both. They are not redundant. claim-scrutinizer finds logical gaps in the argument.
Pre-mortem finds failure modes that are *consistent with a correct bull case* — where
everything the memo says is true and the deal still fails. These are the most dangerous
failure modes precisely because standard diligence doesn't surface them.

---

## Boundability — Epistemic Label Only

Boundability describes the *information state* for a given risk. It tells the reader
how much confidence to place in the assessment. It does not determine whether a risk
is shown, suppressed, acted on, or treated as disqualifying. Every risk is shown
regardless of its boundability classification.

**Boundability is a property of what we know, not the risk itself.** The same customer
concentration risk is Boundable when you have customer-level ARR data and Unboundable
when all you have is a headline percentage. The risk hasn't changed. What changed is
the precision of the assessment.

---

### Boundability Classifications

**Boundable — Data In Hand**
Sufficient company-specific data exists to assess both the likelihood of occurrence and
the financial impact if it materializes. The assessment may carry uncertainty, but it is
grounded in actual evidence.

*To claim Boundable:* Name the specific data supporting the assessment. If you cannot
name it, you do not have it. Do not assert Boundable because a risk "feels estimable."

**Partially Boundable — Data Gettable**
Sufficient data does not exist now, but a specific diligence action would produce it.
The path from current information state to a sharper assessment is clear and executable.

*To claim Partially Boundable:* Name the exact data request — not "further diligence" but
the specific ask. The purpose is to give the investor a precise request to make, not to
recommend that they make it.

A failure mode may be **split-Boundability** — one component Boundable on trend, another
Partially Boundable on magnitude, a third Unboundable on timing. State the split
explicitly: "Partially Boundable on ceiling magnitude; Boundable on trend; Unboundable
on MELI analogy transferability." Do not collapse the split into a single label when
the honest assessment is heterogeneous.

**Unboundable — Structurally Unboundable**
No diligence action produces a reliable bound on this risk. The outcome distribution is
genuinely wide or binary, the risk is endogenous to future conditions that cannot be
predicted, or data exists but is structurally unavailable.

*Unboundable does not mean unimportant.* Many of the most consequential failure modes
are Unboundable. They are shown in full. The investor decides what weight to assign them.

---

### Information State Calibration

Before beginning the registry, state what information state governs the analysis. This
affects the expected distribution of Boundability classifications:

| Information state | Expected distribution |
|-------------------|----------------------|
| Sell-side synthesis only (no QoE, no management access) | ~5–10% Boundable, 40–55% Partially Boundable, 35–55% Unboundable |
| Management calls + CIM complete | ~15–25% Boundable, 50–60% Partially Boundable, 20–30% Unboundable |
| QoE in progress | ~30–45% Boundable, 40–50% Partially Boundable, 15–25% Unboundable |
| Full diligence complete | ~50–70% Boundable, 20–35% Partially Boundable, 10–20% Unboundable |

If your distribution strays far from the expected range, something is wrong. Under-labeling
Unboundable (too much Boundable at early stages) is the most common failure — it represents
epistemic inflation, not rigor.

---

### Expressing Assessments Honestly

**When data supports it (Boundable):** State probability and magnitude as ranges with
the evidence basis named explicitly.

> "Based on customer-level ARR data showing the top 3 accounts represent $10.1M of
> $22M total ARR with average contract lengths of 14 months, we assess a 30–45%
> probability of a material concentration event over a 5-year hold, with a potential
> revenue impact of 35–46% of ARR if all three churn."

**When data is absent (Partially Boundable / Unboundable):** Describe the risk
qualitatively with precision — the mechanism, the conditions under which it materializes,
what it would look like in the business. Do not assign numbers you do not have. The
qualitative description is the honest output.

> "The competitive moat rests on switching cost claims that management asserts but
> that win/loss data does not yet confirm. If those switching costs are lower than
> presented, pricing pressure from [Competitor X] could drive a race-to-zero dynamic
> in the SMB segment, where 40% of current ARR sits. We do not have the data to
> assess how likely this is."

---

## Step 1: Establish the Failure Frame + Lock the Base Assumptions Table

State the bull case being stress-tested, the information state governing this analysis,
and — critically — the authoritative base case assumptions that every downstream impact
calculation must use.

```
FAILURE FRAME

Company:           [Name]
Information state: [Sell-side only / Mgmt calls complete / QoE in progress / Full diligence]
Bull case:         [One sentence — what had to be true for this investment to work]

Assumptions the bull case requires:
  Market:      [What the market had to do]
  Company:     [What the company had to execute]
  Competitive: [What competitors had to not do]
  Financial:   [What the model required]
  Exit:        [What the exit environment had to provide]

Operating assumption: Each of the above was wrong. Reconstruct the failure.
```

**The information state matters** because it governs the precision of every assessment
that follows. A pre-mortem run on sell-side research will produce mostly Partially
Boundable and Unboundable assessments. That is the correct and honest output at that
stage — not a deficiency to be corrected by guessing. Name the state clearly so the
reader knows what the analysis is based on.

---

### Step 1B — The Base Assumptions Table (MANDATORY before any impact math)

**Every impact number you will write in the failure mode registry must derive from the
authoritative base case assumptions in the IC memo's valuation section.** Do not invent
round numbers. Do not substitute generic assumptions. Before writing any Failure Spectrum
field, produce this table and anchor every calculation to it:

```
BASE ASSUMPTIONS TABLE (source: IC memo Section 6 Valuation or equivalent)

Entry equity value:          [$XX.X B]
Exit multiple:               [XXx FY20XXE EBITDA — Base]
                             [XXx Bear / XXx Bull / XXx Tail]
Hold period:                 [X years]
Base case FY20XXE GMV:       [$XXX B]
Base case FY20XXE EBITDA:    [$XX.X B]
Key operational drivers:     [List with values — e.g., ad take-rate base 3.0%,
                             Monee EBITDA base $2.5B, FCF conversion base 95–115%]
Contribution margin rules:   [Document any non-obvious assumption — e.g., "ad revenue
                             is ~100% incremental (zero marginal cost), so 1pp take-
                             rate shortfall translates 1:1 to EBITDA"]

MOIC conversion rule:        [Derived: $1B EBITDA change = X.XXx MOIC at Base entry/exit]
```

**The rule:** If a Failure Spectrum value (e.g., "−$1.3B EBITDA, −0.32x MOIC") cannot be
reconstructed from this table alone, the calculation is wrong. Show the derivation: which
base assumption was perturbed, by how much, and how the table values convert the perturbation
to EBITDA and MOIC delta.

**The check before writing any FM deep dive:** Read the IC memo's valuation section. Copy
the values above verbatim. Do not proceed until the table is complete. If the IC memo does
not yet have a valuation section, produce a "Provisional Base Assumptions Table" with
explicit flags noting each value is a working assumption that must be reconciled once the
valuation section is finalized.

---

## Step 2: Enumerate Failure Modes

Work through all ten categories in the taxonomy below. For each plausible failure mode,
produce a standard full entry. For material failure modes (see definition below), produce
an additional 9-Field Deep Dive after the standard entry.

### Standard Full Entry (every failure mode)

```
FAILURE MODE [#]

Category:    [From taxonomy]
Failure:     [One sentence — what went wrong]

Mechanism:   [The specific causal chain. Not just what happened, but how this failure
              propagated through the business — which metric moved first, what it
              triggered, how it compounded. Vague mechanisms ("the moat eroded") are
              not acceptable. Specific ones are: "Pricing pressure from [Competitor]
              in the SMB segment caused logo churn of ~15% in year 2; because SMB
              logos represented the primary expansion pool, NRR collapsed from 118%
              to 94%, which in turn triggered a covenant breach on the leverage ratio."]

Indicators:  [Observable signals that existed — or were observable — 12–24 months
              before the failure materialized. These are the things diligence could
              have caught or that a portfolio monitoring program would have flagged early.]

Boundability: [Boundable / Partially Boundable / Unboundable — or split designation
               when the honest assessment is heterogeneous across components]

Assessment:
  [Boundable]           [Probability range and magnitude range, with the specific
                         data cited]
  [Partially Boundable] [Qualitative assessment of likelihood and impact, plus the
                         specific data that would sharpen it: "Pulling customer-level
                         ARR for the top 25 accounts and modeling revenue at risk
                         under a 3-customer churn scenario would make this Boundable."]
  [Unboundable]         [Qualitative description of the mechanism and conditions under
                         which this materializes. Be precise about what makes it
                         unboundable — is it future market conditions? A binary
                         outcome? Seller withholding data? Name it.]

NTB: [# or N/A — which Need-to-Believe claim this failure mode threatens]
```

### 9-Field Deep Dive (material failure modes only)

**A failure mode is material and requires the 9-field deep dive when:**
- It threatens an NTB rated CONDITIONAL or GAP, AND
- Its Boundability is Boundable or Partially Boundable (Unboundable-dominant FMs skip
  the deep dive — forcing 9-field precision on an Unboundable risk produces false
  precision), AND
- Its single-driver MOIC impact is ≥0.10x OR it is the trigger for a compound failure path

Summary-index-only treatment (standard entry without deep dive) is correct for failure
modes where the dominant component is Unboundable. A failure mode with a Partially
Boundable component and an Unboundable component receives the deep dive only if the
Partially Boundable component carries the material MOIC exposure; the deep dive explicitly
calls out the Unboundable component in the Evidence and Kill Trigger fields rather than
pretending it is bounded.

```
9-FIELD DEEP DIVE — FAILURE MODE [#]

Issue:              [One-sentence failure description, same as standard entry Failure
                     field but more concrete about the manifest outcome]

Why it matters:     [Which NTB it threatens and the MOIC-at-stake from the returns
                     disaggregation. Explicitly state "Threatens NTB [#]" and cite
                     the MOIC contribution from the valuation section.]

Perimeter:          [What financial exposure is in scope. Cite specific dollar values
                     from the Base Assumptions Table — e.g., "FY2029E ad revenue
                     exposure of ~$4.8B at 3.0% of $159B GMV per Section 6." State
                     any contribution-margin assumption explicitly. Flag asymmetric
                     exposures (e.g., "ad revenue is ~100% incremental margin").]

Timing:             [(a) Earliest trigger — specific earnings date or event where
                     this could first manifest
                     (b) Most likely window — which year(s) of the hold
                     (c) Shape — single-event shock vs. slow-compounding drag]

Evidence:           [Boundability statement + enumerated evidence list, each with
                     source tag [F/E/H, source, confidence]. Name the principal
                     source of any inference — do not use attribution that implies
                     firm-level modeling when the underlying work is memo-author
                     inference. If an Unboundable component exists, state it here.]

Failure spectrum:   [SINGLE combined paragraph — NOT Low/Base/High bullets. Describe
                     the mild, moderate, and severe failure outcomes as a continuous
                     range with specific dollar/MOIC numbers derived from the Base
                     Assumptions Table. Format:
                     
                     "Mild failure (description of smallest plausible failure condition):
                     −$X.XB EBITDA, −0.XXx MOIC. Moderate failure (description):
                     −$X.XB EBITDA, −0.XXx MOIC, aligns with [Section 4/6 bear
                     scenario if applicable]. Severe failure (description): −$X.XB
                     EBITDA, −0.XXx MOIC. Derivation: [show how the math reconciles
                     to Base Assumptions Table values]."
                     
                     The derivation sentence is mandatory. Reader should be able to
                     reconstruct every number from the base table.]

Mitigants:          [Bulleted list of actions that would reduce exposure. Label each
                     with the executor ("Pattern-side" for buy-side / position-sizing
                     actions; "Company-side" for operational execution; "Market-side"
                     for macro/monitoring). Include cost and timeline where known.]

Underwriting treatment (public equity long) or (PE control):
                    [Explicit modification to the investment thesis if this FM is
                     weighted as material. For public equity: entry-price discipline,
                     position-sizing adjustment, scenario probability shift. For PE
                     control: purchase price concession, rep & warranty, escrow,
                     earn-out, covenant structure. Cite the authoritative base entry
                     price from the Base Assumptions Table.]

Kill trigger:       [Specific, observable event or data point that — if it occurs —
                     changes the underwriting decision. Format: "If [specific
                     observable], then [specific action: exit position / trim 30% /
                     escalate to full position review]." The trigger must be both
                     falsifiable and actionable. If the failure mode has an
                     Unboundable component, the kill trigger should be tied to the
                     Boundable component (e.g., a data request completing, an
                     observable metric crossing a threshold) rather than to an
                     observation that would require the Unboundable component to
                     resolve first.]
```

### Why the 9-field format (and why "Failure spectrum" not "Low/Base/High")

**The 9-field format** forces a material FM to be analyzable at investor-operational
precision — not just described, but locatable in time, quantifiable against the memo's
own base case, and actionable via explicit underwriting and kill-trigger statements.

**"Failure spectrum" replaces "Low/Base/High"** because the word "Base" in a failure
context collides catastrophically with "Base case" in the investment thesis. An IC
reader sees "Base case: −$1.7B EBITDA" in Section 7 and assumes this is the base case
of the memo — when it is actually the middle failure scenario. The collision has
produced material reader confusion in live documents. The corrective is to abandon
"Low/Base/High" as impact field labels and use a single combined paragraph with
"Mild / Moderate / Severe" or equivalent descriptors that carry no thesis-label
collision risk.

**Single-paragraph format over three bullets** because the deep dive is read in one
breath by the IC member. A continuous narrative that walks from mild → moderate →
severe with numbers produces better comprehension than three parallel bullets that
demand lookup. The parallel-bullet format also invites the reader to scan "Base:
−$X.XB" and treat it as THE case — instead of reading the full spectrum as a range.

---

## Step 3: Failure Mode Taxonomy

### Category 1 — Market Failure

The market the company was betting on did not materialize, grew slower, or shifted in
structure in ways that undermined the thesis.

**Failure modes:**
- **TAM compression**: Core ICP is narrower than modeled; market is smaller than sized
- **Market timing**: Product is right but arrived before or after the adoption curve
- **Structural disruption**: A substitute technology makes the existing market obsolete
- **Regulatory contraction**: Regulatory change compresses the addressable market
- **Demand cyclicality**: The market looked secular but is actually cyclical

**Boundability notes:**
TAM compression is typically Partially Boundable — an ICP count × ACV build is achievable with diligence.
Structural disruption from AI or platform shift is typically Unboundable — the pace and direction
of technology displacement is genuinely uncertain over a 5-year hold. Regulatory risk is
Unboundable unless specific legislation is in progress, in which case legal diligence makes it Partially Boundable.

**Sharpening questions** *(data that would improve the assessment):*
- Bottom-up TAM: ICP count × average ACV, by segment. What is the actual serviceable market?
- What does the customer do if this product disappears tomorrow? How entrenched is the alternative?
- Are there companies that went through this adoption curve before? What was their trajectory?

---

### Category 2 — Competitive Failure

The competitive position did not prove durable. The moat was narrower or more contested
than the thesis assumed.

**Failure modes:**
- **Moat erosion**: Switching costs, network effects, or proprietary data proved weaker than observed
- **Asymmetric competition**: A better-resourced player entered and commoditized the category
- **Race to zero**: Pricing competition drove margins below viability
- **False differentiation**: Claimed differentiation was table stakes; customers switched readily
- **Bundling threat**: A platform bundled equivalent functionality at no incremental cost
- **AI displacement**: An AI-native product replicated core functionality at lower cost or higher quality

**Boundability notes:**
Moat strength is Partially Boundable — win/loss data and churn-reason analysis are diligence-gettable and
would support a sharper assessment. Platform bundling risk is Unboundable unless a specific platform
has signaled competitive intent. AI displacement is Unboundable for most companies over a 5-year
horizon — the distribution of outcomes is too wide to bound reliably.

**Sharpening questions:**
- Win/loss by reason and by competitor for the last 12 months. Who are deals lost to and why?
- Can the top 5 customers describe — unprompted — a specific reason they would not switch at 15% lower price?
- What does the product do that a well-resourced engineering team could not replicate in 18 months?

---

### Category 3 — Business Model Failure

The economics of the business did not work at scale. Unit economics diverged from what
was presented at entry.

**Failure modes:**
- **CAC payback drift**: Acquisition cost rose as the company moved into less efficient channels
- **Expansion revenue illusion**: NRR looked strong but was concentrated in one cohort or motion
- **Gross margin compression**: COGS did not scale as projected
- **LTV deterioration**: Churn increased as the company sold into less sticky segments
- **Services dependency**: True subscription ARR stood alone worse than blended metrics showed
- **Negative operating leverage**: OpEx scaled faster than revenue; leverage never materialized

**Boundability notes:**
This category is largely Partially Boundable at CIM stage — the underlying data exists inside the company.
CAC by cohort, NRR by vintage, gross margin by segment are all producible. A QoE should
move most of this category to Boundable. If this data is not available in diligence, the absence
is itself a finding worth noting.

**Sharpening questions:**
- CAC by channel and by cohort vintage — is efficiency improving or degrading year over year?
- NRR disaggregated by cohort vintage — do recent vintages perform above or below early vintages?
- Gross margin by customer segment (SMB / mid-market / enterprise) and by product line.

---

### Category 4 — Management and Execution Failure

The team could not execute the strategy that justified the multiple.

**Failure modes:**
- **Founder scaling failure**: Company hit the organizational ceiling; professional management was needed but not successfully absorbed
- **GTM dysfunction**: Sales model, leader, or channel was wrong and not corrected fast enough
- **Product execution breakdown**: Engineering velocity slowed; roadmap slipped under cost pressure
- **Key person dependency**: Departure of one or two individuals caused disproportionate deterioration
- **Board/management misalignment**: PE operational agenda created friction that consumed execution capacity
- **M&A integration failure**: Add-on consumed management bandwidth; synergies did not materialize

**Boundability notes:**
GTM execution track record is Partially Boundable — pipeline-to-close data by quarter for the last 8 quarters
is a concrete request. Key person dependency is Partially Boundable — org chart and back-channel references
are achievable. Founder scaling capacity is Unboundable — it is a judgment call with no reliable
base rate. Post-close board/management dynamics are Unboundable — they depend on relationships
that don't yet exist.

**Sharpening questions:**
- Pipeline-to-close ratio by quarter for the last 8 quarters. What is the trend direction?
- For each senior leader: track record at a company of the size we're asking them to build?
- Back-channel references on all senior leaders, selected independently of the seller.

---

### Category 5 — Financial Structure Failure

The capital structure, debt service, or liquidity position became untenable.

**Failure modes:**
- **Leverage breach**: Covenant violation at a revenue miss within the plausible range
- **Refinancing failure**: Debt matured in a high-rate or distressed environment
- **Working capital trap**: Growth consumed more cash than the model projected
- **Cash conversion deterioration**: DSO expansion created a cash shortfall at the moment investment was required
- **PIK/accrual trap**: Accruing interest compounded until the debt load was inescapable regardless of operations

**Boundability notes:**
Covenant headroom under various revenue scenarios is Boundable — it is calculable from the credit
agreement and the model. Working capital sensitivity is Partially Boundable if the company can produce
historical DSO and DPO data. Refinancing risk is Unboundable — it depends on future credit market
conditions that cannot be predicted with confidence.

**Sharpening questions:**
- At what revenue miss (10%, 20%, 30%) does the company breach its most restrictive covenant?
- Historical cash conversion cycle (DSO + DIO − DPO) — what is the trend over 3 years?
- Working capital consumption modeled at 20%, 30%, 40% revenue growth.

---

### Category 6 — Customer Concentration and Cohort Failure

Revenue was more concentrated, more fragile, or more cyclical than headline metrics suggested.

**Failure modes:**
- **Concentration event**: Top 1–3 customers churned; revenue cliff was disproportionate to reported share
- **Cohort vintage collapse**: Early cohorts showed strong LTV but recent vintages are systematically underperforming
- **Sector concentration**: Customer base concentrated in one sector that entered a downturn
- **Champion departure churn**: Relationships held by individual champions who left; accounts did not survive transition
- **Enterprise pilot syndrome**: Enterprise logos counted as ARR but never expanded past pilot

**Boundability notes:**
This is the category most commonly misassessed. Headline concentration figures ("top 10
customers = 42% of revenue") feel like data but are not sufficient to bound the risk.
Customer-level ARR, contract terms, and churn-reason data are required and are gettable —
making this Partially Boundable by default until that granular data is in hand.

**Sharpening questions:**
- Customer-level ARR for the top 25 accounts. Revenue at risk if top 3 churn. Top 5. Top 10.
- NRR by cohort vintage charted from month 12 through current. Direction of recent vintages?
- For top 10 customers: primary stakeholder, and have there been champion transitions in the last 24 months?

---

### Category 7 — Technology and Product Failure

The product did not deliver sufficient value to sustain the model, or a technological
shift made it obsolete.

**Failure modes:**
- **Product-market fit regression**: The problem evolved; the product did not adapt fast enough
- **Technical debt ceiling**: Legacy architecture consumed engineering capacity; new capability stalled
- **AI displacement**: An AI-native product replicated core functionality at lower cost
- **Integration fragility**: Deep integration into a third-party platform was disrupted by API or policy change
- **Security/compliance failure**: A breach or compliance violation triggered customer attrition and/or regulatory penalty

**Boundability notes:**
Technical debt depth is Partially Boundable — an independent technical assessment is achievable. AI
displacement risk is Unboundable for most companies over a 5-year hold. Integration fragility is Partially Boundable
if platform dependencies can be mapped and the platform's track record with partners assessed.
Security posture is Partially Boundable — SOC 2 status, penetration test history, and incident record are
diligence-gettable.

**Sharpening questions:**
- Independent technical assessment: what % of engineering capacity is maintenance vs. net new? Cost to retire the debt?
- Third-party platform dependency map: what happens if each platform changes its API, pricing, or terms?
- SOC 2 status, last penetration test date, any security incidents in the last 3 years.

---

### Category 8 — Macro and Exogenous Failure

The operating environment deteriorated in ways beyond management's control, but which
should have been visible as risks at entry.

**Failure modes:**
- **Exit multiple compression**: Rate environment or market conditions compressed exit multiples below the underwriting assumption
- **Demand recession**: A macro contraction caused customers to cut software spend; the company was more cyclical than its framing implied
- **FX/geopolitical exposure**: International revenue or cost base exposed to currency or geopolitical disruption
- **Vendor or infrastructure disruption**: A key vendor relationship disrupted with no contractual protection

**Boundability notes:**
This category is most honestly Unboundable in most cases. The direction of macro conditions over a
5-year hold is not forecastable with credible precision. The productive analytical move is
not to assign probabilities to macro scenarios but to characterize the company's behavior
at various levels of demand contraction and multiple compression — which converts an
unboundable macro risk into a bounded company sensitivity.

**Sharpening questions:**
- How did revenue and EBITDA behave during the 2020 and 2022 demand contractions?
- Return profile at 7x, 9x, 12x exit EBITDA. What exit multiple is required to hit 2.5x MOIC?
- What % of revenue or cost structure is exposed to non-USD currency risk?

---

### Category 9 — Deal Structuring and Underwriting Failure

The failure was caused not by the business itself but by how the deal was priced or underwritten.

**Failure modes:**
- **Entry multiple overreach**: Price required an implausible combination of growth, margin improvement, and multiple expansion
- **Thesis migration**: The original value creation path proved unachievable with no credible alternative
- **Add-on dependency**: The model required acquisitions that did not materialize or materialized at dilutive prices
- **Synergy assumption failure**: Synergies embedded in the model at close did not appear
- **Hold period mismatch**: Exit conditions prevented realization at the modeled hold period

**Boundability notes:**
Entry multiple sensitivity is Boundable — the model produces this directly. Standalone base case
return (no add-ons, no synergies, no multiple expansion) is Boundable. Add-on pipeline quality is
Partially Boundable if the acquisition pipeline has been assessed. Synergy realizability is Partially Boundable with management
and operational diligence. This is the category where the analysis looks most rigorous
(sensitivity tables) while the underlying input assumptions are often least examined.

**Sharpening questions:**
- Return at entry multiple + 1x, + 2x. Where does IRR break below 2.0x, 1.5x, 1.0x?
- Standalone base case: no add-ons, no synergies, no multiple expansion. What is the return?
- For each synergy line in the model: who owns delivery and what is the specific mechanism?

---

### Category 10 — Information Asymmetry and Diligence Failure

The failure was caused by something knowable but not known — a gap or asymmetry that left
a material risk undetected.

**Failure modes:**
- **Revenue quality misrepresentation**: Reported metrics did not survive rigorous QoE; seller definitions were aggressive
- **Off-balance-sheet liability**: A contingent liability — litigation, environmental, regulatory — not surfaced in standard diligence
- **Related-party complexity**: Revenue, costs, or contracts involved related parties at non-arm's-length terms
- **Seller reference control**: References limited to seller-approved contacts; back-channel diligence was skipped
- **Accounting manipulation**: Revenue pulled forward, expenses capitalized inappropriately, EBITDA add-backs not sustainable

**Boundability notes:**
This category is structurally different. Most of these risks are Unboundable at the time of assessment —
we do not know what we do not know. The analytical value here is not in assessing likelihood
but in identifying the specific diligence actions that convert unknown unknowns into known
quantities: a rigorous independent QoE, aggressive back-channel reference program,
independent legal review of contracts and litigation history. Name what has and has not
been done.

**Sharpening questions:**
- Has an independent QoE been conducted by a firm of the deal team's choosing — not the seller's?
- ARR on a strict contractual MRR × 12 basis. How does it compare to management's reported figure?
- Back-channel references on all senior leaders and 10+ customers, without seller involvement in selection.

---

## Step 4: Pre-Mortem Output

### 4a — Failure Mode Summary Index

Produce a scannable index before the full entries. This lets the reader navigate the
register and see the full FM landscape at a glance.

```
| FM | Failure | Category | Boundability | NTB | Deep Dive? |
|----|---------|----------|--------------|-----|-----------|
| 1  | [Failure]| [Category]| [Boundable/Partially/Unboundable or split] | [#] | [Yes/No] |
...
```

### 4b — Failure Mode Registry (Standard Full Entries)

Produce a complete inventory of all identified failure modes using the Standard Full
Entry format from Step 2. No tiering by score — every failure mode is shown.

```
FAILURE MODE REGISTRY — [Company Name]
Information state: [Sell-side / Mgmt calls / QoE / Full diligence]

Category 1 — Market Failure
  [Standard full entry for each applicable FM]
  ...
[Continue through all 10 categories]

Sharpening data not yet obtained:
  [List every specific data request that would improve the assessment of Partially
   Boundable risks, organized by category. This is a reference list — not a prioritized
   action plan.]
```

**NTB mapping is required on every failure mode.** If the IC memo has a Need-to-Believe
registry, each failure mode must identify which NTB it threatens (or N/A if it threatens
no specific NTB). This linkage makes the pre-mortem actionable.

**NTB mapping format:**
- `NTB: 2` — directly threatens NTB 2
- `NTB: 3, 4` — threatens multiple NTBs simultaneously (compound path signal)
- `NTB: N/A` — operates outside the NTB structure (e.g., macro shock, key-person
  departure) — note these explicitly as risks not captured by the NTB framework

### 4c — 9-Field Deep Dives (Material Failure Modes)

For each FM marked "Yes" in the Deep Dive column, produce the 9-field entry using the
format from Step 2.

### 4d — Compound Failure Paths

The most dangerous failure paths are usually combinations, not individual modes. Identify
the 2–3 most plausible *compound* failure sequences: cases where one failure mode creates
the conditions for a second, which together produce an outcome neither would reach alone.

**Use the 9-field format for compound paths as well**, adapted:

```
COMPOUND PATH [#] — [Name]

Issue:              [The compound scenario — trigger + cascade + outcome]

Why it matters:     [Which NTBs are threatened simultaneously; combined MOIC
                     exposure vs. sum of individual FM estimates]

Perimeter:          [What exposure is in scope — often larger than any single FM
                     because the cascade affects multiple drivers]

Timing:             [Earliest trigger; cascade lag between first FM and second;
                     window of full manifestation]

Evidence:           [Boundability on each link of the cascade; evidence for
                     correlation; what would make the cascade more or less likely]

Failure spectrum:   [Mild / Moderate / Severe compound outcomes as a single
                     paragraph, citing EBITDA impact + multiple compression if
                     applicable. Compound paths typically produce multiple
                     compression beyond the EBITDA impact — state this explicitly.]

Mitigants:          [Both per-FM mitigants and cascade-specific ones
                     (sensitivity modeling, position sizing for correlation,
                     hedging if available)]

Underwriting treatment:
                    [How the cascade is reflected in sizing, entry price, or
                     scenario probability weights]

Kill trigger:       [Observable event that signals the cascade is in progress —
                     often the completion of the first FM creating conditions
                     for the second]
```

Single-driver MOIC estimates in the disaggregation table are additive only in isolation.
Compound paths produce non-linear outcomes — the combined MOIC impact of two simultaneous
NTB failures is typically larger than the sum of their individual estimates because of
the correlation structure.

### 4e — IC-Facing Risk Narrative

A 200–300 word narrative for the IC memo risk section. It should:

- Open with the most consequential compound failure path — not the longest list of risks
- Distinguish clearly between what is assessed with data and what is assessed qualitatively
- Surface every Unboundable risk in plain language — do not soften or minimize because
  it is hard to quantify
- Be written for a reader who will make the investment decision, not for a reader who
  needs to be protected from uncomfortable information
- Close with a one-sentence statement of which NTB, if it fails, produces the largest
  single-driver MOIC impact — and whether it is currently GAP, CONDITIONAL, or CONFIRMED

**Do not use "Base" or "base case" language when describing failure outcomes in this
narrative.** Use "the central scenario" or "moderate failure" or name the specific
magnitude — anything but "base" — to avoid collision with thesis language.

### 4f — NTB Gap Prioritisation (required when NTB registry exists)

If the IC memo has a Need-to-Believe registry, produce a one-page addendum:

```
NTB GAP PRIORITISATION

For each NTB rated GAP or CONDITIONAL, list:
  NTB [#]: [Statement]
  Evidence state: GAP / CONDITIONAL
  Failure modes that threaten it: [FM numbers from registry]
  Partially Boundable data that would resolve it: [Exact data request]
  If Unboundable component exists: [Name it — explain why it cannot be bounded]
  MOIC at stake: [From returns disaggregation table]

Priority ranking: order NTBs by (evidence state × MOIC at stake) — GAP items with
highest MOIC impact are highest priority regardless of probability assessment.
Cap the list at 5 entries — further depth belongs in the standalone information
gaps section of the IC memo.
```

This addendum is distinct from the information gaps table in the IC memo — it organizes
the same data through the lens of NTB resolution rather than diligence category.

---

## Section 6 ↔ Section 7 Reconciliation (Pre-Delivery Check)

**Before delivering the pre-mortem output, run this reconciliation.** The pre-mortem is
the single most common source of cross-section numeric contradictions in an IC memo
because every impact field produces a number and those numbers must reconcile to the
valuation section.

```
RECONCILIATION CHECK

From Base Assumptions Table (Step 1B):
  Entry equity:        $[value from valuation section]
  Exit multiple:       [value from valuation section]
  Hold period:         [value from valuation section]
  Base FY20XXE EBITDA: $[value from valuation section]
  Base FY20XXE GMV:    $[value from valuation section]

Scan every 9-field Failure Spectrum for:
  [ ] Every dollar amount reconciles to the Base Assumptions Table
  [ ] No "round number" substitutes ($70B when actual is $47.2B; 10x when actual is 12x)
  [ ] "Severe failure" scenarios reconcile to the Bear case in the valuation scenario table
  [ ] "Mild failure" scenarios do not exceed the Bull case deltas in the valuation table
  [ ] Contribution-margin assumptions are stated explicitly and match the driver
      disaggregation (e.g., ad revenue ~100% incremental, Monee ~27% EBITDA margin, etc.)
  [ ] Hold period is consistent across every impact field
  [ ] No "Base case" language refers to failure scenarios — use Mild/Moderate/Severe

If any check fails, fix before delivering. Do not ship a pre-mortem with internal
numeric inconsistency — the document will fail at IC.
```

---

## Operating Standards

**Surface everything.** The job is to find every failure mode with the specificity
required for a sophisticated investor to evaluate it. A risk is not made more manageable
by being described vaguely.

**Anchor impact math to the memo, not to generic assumptions.** Do not use round numbers
when the authoritative numbers are available in the valuation section. If the valuation
section is not yet complete, use a provisional table and flag every value as "reconcile
post-valuation."

**Name the information state.** Every assessment should be readable as a function of
what is actually known. "We do not have the data to assess this precisely" is a valid
and important output.

**No gatekeeping.** The skill does not determine what is disqualifying, what requires
resolution, or what the investor should do with any risk. It produces the fullest
possible picture of how this investment fails. The investor decides what that means.

**Mechanisms over labels.** "Moat erosion" is a label. "Pricing pressure in the SMB
segment causing 15% logo churn in year 2, which collapsed the expansion pool and drove
NRR from 118% to 94%, triggering a leverage covenant breach" is a mechanism. Write
mechanisms.

**Map to NTBs.** Every failure mode must be linked to the NTB it threatens or marked
N/A. Failure modes that threaten GAP-rated NTBs with high MOIC impact are the highest-
priority findings — they represent risks where both the data is missing AND the
financial exposure is large. Surface these first regardless of their position in the
taxonomy.

**The goal:** When the investor finishes reading this, they should have seen every way
this deal fails — described precisely enough that they could recognize early indicators
if they appear post-close, with an honest account of how much we actually know about
each one, with a clear link between each failure mode and the NTB it threatens, and with
every impact number reconciling to the memo's own valuation section.

**Pre-mortem does not produce underwriting actions.** That is boundability's job. This
skill surfaces failure modes with their epistemic state. Boundability takes the
surfaced modes and converts each into model / price / leverage / docs / operations
actions with a deal-level verdict. Run boundability after this skill to complete
the diligence → underwriting chain.

---

## References

```
If claim-scrutinizer has already run on this deal:
  → Cross-reference its risk register to avoid duplication and extend coverage
  → /mnt/skills/user/claim-scrutinizer/SKILL.md

If ntb-diligence has already run on this deal:
  → The NTB registry from its output is the authoritative source
  → Load it before enumerating failure modes
  → Use its Boundable/Partially Boundable/Unboundable terminology (this skill uses the same)
  → Map every failure mode to the NTB(s) it threatens using ntb-diligence's numbering
  → Produce Step 4f NTB Gap Prioritisation addendum
  → /mnt/skills/user/ntb-diligence/SKILL.md

If NTB registry exists but ntb-diligence has not run:
  → Use the NTB registry from the IC memo (produced inline by mckinsey-consultant)
  → Same mapping discipline applies
  → Consider suggesting ntb-diligence for the next iteration

If IC memo valuation section exists:
  → Copy the Base Assumptions Table from it verbatim before producing any impact math
  → Run the Section 6 ↔ Section 7 Reconciliation before delivery

If IC memo valuation section does not yet exist:
  → Produce a Provisional Base Assumptions Table with working assumptions
  → Flag every value with "[provisional — reconcile post-valuation]"
  → Do not ship the final pre-mortem until reconciliation against the actual valuation
    section has been completed

Downstream — boundability (convert failure modes to underwriting action):
  → After pre-mortem completes, boundability takes each material failure mode (or the
    NTB it threatens) and scores it across six modules (Perimeter, Timing, Data
    Quality, Outcome Range, Precedent/Observability, Mitigants)
  → Boundability terminology matches pre-mortem: an item labeled Boundable by pre-mortem
    should score ≥25/30 on boundability's 6-module scoring; Partially Boundable should
    score 18–24; Unboundable should score <18
  → If boundability and pre-mortem disagree on classification for the same item, resolve
    before shipping IC materials — one of the two assessments is wrong
  → Boundability produces the underwriting treatment (model / price / leverage / docs /
    operations) that this skill deliberately does NOT produce; pre-mortem surfaces
    failure modes, boundability converts them to action
  → /mnt/skills/user/boundability/SKILL.md
```
