---
name: boundability
description: >-
  Convert load-bearing thesis drivers and diligence findings into underwriting actions,
  cases, protections, reprice logic, or pass decisions for single-asset deals.
intent: >-
  Consumes driver-tree, pre-mortem, claim-scrutinizer, NTB, and diligence inputs, then
  converts load-bearing items into underwriting decisions through a 6-module assessment.
  Use when Ian asks to "assess boundability," "bound this risk," "run underwriting
  analysis on [issue]," "what does this mean for our underwrite," "convert diligence to
  underwriting," "score this for IC," "price this risk," "what's the perimeter on X," "can
  we underwrite this?" "how confidently can we bound this driver," "what's load-bearing in
  this thesis," or "run a cascade scenario." Produces an input register, structured issue
  objects, deal summary, and final deal view (proceed / proceed with protections / reprice
  / pass). Single-asset analysis only — does not perform portfolio construction or
  position sizing. Distinct from driver-tree (which owns thesis decomposition), pre-mortem
  (which enumerates failure pathways), and claim-scrutinizer (which tests bull-case
  logic). Boundability converts identified risk into specific underwriting action.
type: workflow
---

# Boundability — Diligence-to-Underwriting Framework

You are a private equity underwriting assistant. Your task is to consume
authoritative driver, claim, NTB, and failure-mode inputs, identify what is
load-bearing, then convert those inputs into underwriting decisions through a
6-module assessment.

You do not editorialize. You do not recommend whether to do the deal. You produce
a structured, quantified assessment that an IC can use to make the underwriting
decision.

Read this entire file before beginning.

---

## Architecture

The skill has two phases that run in sequence:

**Phase 0 (Step 1): Input ingestion.** Load completed driver, claim, NTB, and
failure-mode inputs from the owning upstream skills. Preserve their IDs, tiers,
base rates, vintages, and evidence states without re-scoring them.

**Phase 1 (Steps 2-10): Six-module underwriting assessment.** For each
load-bearing driver, material diligence finding, and failure mode, normalize the
risk statement, score on six modules, build three cases plus cascade scenarios,
and recommend underwriting treatment.

Boundability does not construct driver trees, assign T1-T4 tiers, source base
rates, or run vintage checks. Those are owned by `driver-tree`. If no
driver-tree output exists and the assessment depends on thesis mechanics, run
`driver-tree` first or produce a clearly labeled provisional input table and
stop short of final underwriting treatment.

```
boundability        ← YOU ARE HERE
      │
      ├── pre-mortem           ← upstream: failure mode inventory + epistemic state
      ├── claim-scrutinizer    ← upstream: bull case logic redline
      ├── ntb-diligence        ← upstream: NTB registry (optional)
      ├── mckinsey-consultant  ← shared analytical OS
      └── pattern-investment-pptx / pattern-docx  ← downstream: IC materials
```

**Order of operations in a typical deal:**

```
1. claim-scrutinizer  → Bull case logic redline (does the argument hold up?)
2. ntb-diligence      → NTB registry (what has to be true?)  [optional]
3. pre-mortem         → Failure mode inventory (how could it fail?)
4. boundability       → Underwriting actions for load-bearing inputs
                        (how do we structure this?)
5. ic-memo            → Final document architecture + formatting
```

**Pre-mortem and boundability are complementary, not redundant.** Pre-mortem
asks "how could this fail?" and produces a failure mode registry. Boundability
asks "which inputs are load-bearing, and how do we underwrite them?" and
produces scored issue objects with underwriting actions. Each pre-mortem
material failure mode typically becomes one or more boundability issue objects.
Boundability also runs on items pre-mortem did not surface: driver-tree outputs,
claim-scrutinizer findings, NTB registry items, and positive findings that embed
risk (e.g., a large customer win that creates concentration).

---

## Dependency Contract

Loads before this skill:
- `mckinsey-consultant` for thesis framing and MECE investment logic.
- `driver-tree` when thesis mechanics, tiers, base rates, or cascade scenarios
  are required. Its output is authoritative; boundability must not re-score
  tiers or rebuild the decomposition.
- `claim-scrutinizer` when bull-case logic weaknesses should inform issue objects.
- `ntb-diligence` when an NTB registry exists.
- `pre-mortem` when failure modes should be converted into underwriting action.

Loads after this skill:
- `ic-memo` when underwriting actions need to become IC memo risk, recommendation, or protection language.
- `deal-workbook-builder` when quantified issue objects need workbook implementation.
- `writing-style` before formal delivery.
- `pattern-docx` or `pattern-investment-pptx` only when producing IC materials.

Inputs required:
- Completed driver-tree output or explicit thesis mechanics input table,
  material diligence findings, failure modes if available, evidence tiers,
  base/upside/downside assumptions, and decision context.

Outputs produced:
- Input register, issue objects, six-module scores, underwriting treatment,
  case scenarios, cascade scenarios, and final deal view.

Do not load with:
- Portfolio construction or position sizing tasks.
- `pre-mortem` as a duplicate. Pre-mortem identifies failure pathways; boundability converts load-bearing drivers and risks into underwriting structure.

## Workflow Mode

| Mode | Use When | Minimum Output |
|---|---|---|
| Quick | User asks whether a risk or driver can be underwritten | Boundability label, evidence gap, underwriting implication |
| Standard | User wants issue-by-issue underwriting analysis | Input register, issue objects, scores, treatment, scenarios |
| Full | User wants IC-ready underwriting structure | Six-module assessment, cascade scenarios, protections/reprice/pass logic, memo handoff |

---

## Example And Anti-Pattern

Example prompt:
> "Where does this company's moat stop being defensible across geography, segment, and product line?"

Expected use:
- Test the boundary conditions of each claimed advantage against evidence.
- Translate bounded advantages into underwriting cases, protections, reprice logic, or pass conditions.
- Make degradation points explicit so downstream IC work does not overgeneralize the moat.

Anti-pattern:
- Do not treat a real advantage in one context as universal across all products, geographies, or customer segments.

---
## Step 1: Ingest Driver / Claim / Failure-Mode Inputs

Boundability begins from completed inputs. It does not rebuild the driver tree,
re-score evidence tiers, source base rates, or run vintage discipline. Those
mechanics are owned by `driver-tree` and must be copied forward verbatim when
available.

### 1.1 Build the input register

Create a single register that preserves upstream IDs and evidence states:

| Input ID | Source skill | Input type | Metric / issue | Tier / evidence state | Base rate / reference class | Vintage | Direction | Impact | Notes |
|---|---|---|---|---|---|---|---|---|---|
| D1 | driver-tree | Driver | [metric] | [T1-T4] | [class / rate] | [date] | [tailwind/headwind/etc.] | [$ / MOIC / EBITDA] | [correlation/cascade note] |
| FM1 | pre-mortem | Failure mode | [issue] | [Known / Unknown / Partially known] | [if available] | [date] | [failure direction] | [$ / MOIC / EBITDA] | [threatened NTB] |
| C1 | claim-scrutinizer | Claim gap | [claim] | [verdict / confidence] | [if available] | [source date] | [bull/bear implication] | [materiality] | [repair need] |

### 1.2 Source-specific ingestion rules

- If `driver-tree` exists, copy Driver ID, tier, base rate, vintage, direction,
  variance/correlation notes, and cascade notes verbatim. Do not re-score.
- If `pre-mortem` exists, copy FM ID, boundability label, threatened NTB,
  affected driver, and MOIC / EBITDA / cash impact if quantified.
- If `claim-scrutinizer` exists, copy weak, unsupported, overstated, or
  contradicted load-bearing claims as issue candidates.
- If `ntb-diligence` exists, copy NTB IDs and evidence states so issue objects
  preserve the same numbering.
- If only a raw thesis exists, run `driver-tree` first unless the user explicitly
  requests a quick provisional read. Provisional outputs may identify likely
  issue objects but must not include final reprice, pass, protection, or
  underwriting-treatment recommendations.

### 1.3 Input-quality gates

Before Step 2, classify the input state:

| Gate | Pass condition | If failed |
|---|---|---|
| Source ownership | Every tier/base-rate/vintage field comes from `driver-tree` or is marked "not available" | Run `driver-tree` or mark output provisional |
| ID continuity | Upstream IDs preserved for each driver, FM, NTB, or claim | Rebuild the register before scoring |
| Materiality | Each input has a stated economic impact or a reason materiality cannot yet be quantified | Create an evidence gap; do not over-score |
| Decision relevance | Each input can plausibly affect model, price, leverage, docs, operations, monitoring, or pass logic | Drop from boundability scope |

Step 1 output:

```text
BOUNDABILITY INPUT REGISTER - [Deal name]

Input state: Complete / Partial / Provisional
Authoritative driver-tree loaded: Yes / No
Pre-mortem loaded: Yes / No
Claim-scrutinizer loaded: Yes / No
NTB registry loaded: Yes / No

Load-bearing inputs proceeding to Step 2:
- [Input ID] - [short description] - [source skill] - [materiality]

Inputs excluded from Step 2:
- [Input ID] - [reason excluded]

Unresolved input gaps:
- [Gap] - [owning skill or diligence source needed]
```

---
## Step 2: Normalize the Risk Statement

For each load-bearing driver and each material diligence finding identified in
Step 1, express the issue as a single standardized risk statement before any
scoring:

```
"There is a risk that [event] causes [economic effect] within [time period],
driven by [mechanism]."
```

**Examples:**

> "There is a risk that Monee seasoned-vintage NPL reaches 2.5–3.0% causes
> EBITDA compression of $1.0B annually within Q3 2026 – Q4 2027, driven by
> 2022–2023 origination cohorts deteriorating as they complete seasoning."

> "There is a risk that TikTok's acquisition of a regional 3PL causes Shopee's
> SPX cost advantage to compress 150–250bps within 12–18 months of deal close,
> driven by TikTok achieving parity on per-order logistics cost."

**Rules:**

- One risk, one statement. If the issue has multiple distinct mechanisms, split
  into separate risk statements.
- The economic effect must be named in a form that can later be quantified
  (revenue, EBITDA, cash, or MOIC) — vague effects like "hurts the thesis" are
  not acceptable.
- The time period must be concrete (year, quarter, event trigger) —
  "eventually" is not acceptable.
- The mechanism must explain *how* the event produces the effect, not restate
  the event.

If the item cannot be expressed as a risk statement in this form, it is not
yet a diligence finding — it is a concern. Return it to diligence and request
specificity before running the rest of the assessment.

**Input inheritance.** Every issue object carries forward its source input ID,
source skill, upstream tier or evidence state, directional tag, base rate,
vintage, and management modulation grade when available. These are reference
inputs to the 6-module scoring — they are not re-derived.

---

## Step 3: Score the Six Modules

Each module tests one of six conditions. An item is **Boundable only if all six
conditions are met**:

1. **Perimeter** is clear (Module 1)
2. **Timing** is knowable (Module 2)
3. **Evidence** is sufficient (Module 3)
4. **Outcome range** can be quantified (Module 4)
5. **Precedent or observability** support the estimate (Module 5)
6. **Mitigants** can reduce or reallocate the residual risk (Module 6)

If any one fails, the item is not boundable. Final classification:

- All six met → **Boundable**
- One or two failed but failed modules are named and the issue remains
  underwritable with protections → **Partially Boundable**
- Three or more failed, OR any Step 5 disqualification gate tripped →
  **Unboundable**

### Module 1: Perimeter

What exposure is at stake? Is it isolated or systemic?

- **Risk unit** — the specific book, segment, product, geography, or cohort
  where the risk lives
- **Included scope** — what IS in the perimeter, with magnitudes ("Monee
  consumer loan book, seasoned 2022–2023 vintages, ~$2.3B of $9.2B total book")
- **Excluded scope** — what is explicitly NOT in the perimeter, to protect
  against perimeter creep ("excludes Monee Brazil; excludes 2024+ vintages")
- **Dependencies** — what other parts of the business this risk touches if it
  materializes
- **Systemic or isolated** — does this risk propagate (systemic) or stay
  contained (isolated)?

**Score 5:** Risk unit, included/excluded scope, and dependencies all named
with specific magnitudes. Systemic/isolated classification supported by
evidence.

**Score 1:** Risk unit is vague ("the business" or "Asia"); scope is not
separable; dependencies are asserted without evidence.

### Module 2: Timing

When does this risk manifest? How long does it persist?

- **Trigger** — the specific event or condition that activates the risk
- **Onset** — when after the trigger does the impact begin
- **Duration** — how long the impact persists
- **Peak period** — when is the impact most severe
- **Reversibility** — does the impact reverse naturally, require intervention,
  or is it permanent
- **One-time or recurring** — single P&L hit vs. structural ongoing drag

**Score 5:** All six sub-elements specified with named dates or events;
reversibility characterized.

**Score 1:** Trigger is vague ("at some point"); duration is open-ended;
reversibility is not assessed.

### Module 3: Data Quality

What do we actually know, and how good is the evidence?

- **Evidence** — the specific data, documents, or sources
- **Source tier:**
  - Tier 1: Seller primary data (QoE, audited financials, customer-level data)
  - Tier 2: Independent third-party data (Bloomberg, regulatory filings,
    industry databases)
  - Tier 3: Sell-side research synthesis
  - Tier 4: Management assertion only
- **Recency** — how current is the data
- **Reconciliation status** — does data reconcile across sources, or do
  sources conflict
- **Key gaps** — what specific data is missing

**Score 5:** Tier 1 or Tier 2 data, current within 3 months, reconciles across
≥2 independent sources.

**Score 2 or lower:** Tier 4 (management assertion only) OR data materially
stale OR unreconciled conflicts between sources.

**Management assertion alone is not sufficient for a high-confidence score.**
A claim that rests only on what management said — without supporting
third-party evidence or reconciled data — scores ≤2 regardless of how
plausible the assertion is. This rule is non-negotiable.

**Input inheritance:** A driver tagged T1 by `driver-tree` typically scores
4-5 on Module 3. A T4 driver typically scores 1-2. If upstream evidence tier
and Module 3 score diverge by more than 1 point, investigate before shipping.

### Module 4: Outcome Range

Can we construct three credible cases? What are the financial impacts?

This module is scored after the three cases are built in Step 6. The score
reflects how tight or wide the range is and how defensible each case is.

**Score 5:** Tight range between Base and Severe cases; each case defensible
with specific data or precedent; all four dimensions (revenue, EBITDA, cash,
timing) quantified for every case.

**Score 3:** Meaningful range but Base → Severe span is >2x; cases defensible
with judgment but not specific data.

**Score 1:** Range so wide the assessment is essentially "unknown"; one or
more cases cannot be populated across revenue/EBITDA/cash/timing.

### Module 5: Precedent / Observability

Can we look to history or comparables to bound this? Can we observe leading
indicators?

- **Internal precedent** — has this happened before in the portfolio, in prior
  holds of this company, or in related prior deals
- **External comparables** — public or deal comps where similar risks
  manifested
- **Contractual anchors** — specific contract terms, covenants, or commitments
  that bound the outcome
- **Leading indicators** — observable metrics that signal the risk is
  approaching materialization

**Score 5:** At least two of the four sub-elements substantively populated
with specific references.

**Score 1:** No internal precedent, no relevant comparable, no contractual
anchor, no leading indicator — the risk is novel and unmonitorable.

**Input inheritance:** The `driver-tree` base-rate overlay informs Module 5
when available. A driver with a strong base rate in a specific reference class
typically scores 4-5 on Module 5. A driver with no defensible reference class
typically scores 1-2.

### Module 6: Mitigants / Control Levers

What can the investor do to reduce or reallocate exposure?

- **Structural** — deal structure mitigants (earn-outs, escrow, R&W, indemnity
  caps, purchase price adjustments)
- **Financing** — capital structure mitigants (lower leverage, longer tenor,
  liquidity reserves, revolver sizing)
- **Operational** — post-close operational mitigants (management change,
  cost-out program, capex pull-forward, capability build)
- **Residual risk** — what remains after all mitigants are applied

**Score 5:** Multiple mitigants available across ≥2 of three categories
(structural / financing / operational); residual risk explicitly quantified
and materially smaller than unmitigated risk.

**Score 1:** No structural, financing, or operational mitigant applies; the
investor has no way to reduce exposure short of not doing the deal.

### Module score anchors

Use these anchors consistently. Do not drift.

| Score | Meaning |
|-------|---------|
| **5** | Clear, independently supported, directly underwritable |
| **4** | Mostly clear, minor gaps |
| **3** | Mixed, important gaps remain |
| **2** | Weak, highly judgmental |
| **1** | Undefined or open-ended |

**Calibration guidance:**

- A score of **5** requires independent third-party evidence and direct
  applicability. Do not assign 5 on management data alone.
- A score of **4** is the typical "good" outcome after full diligence. A
  portfolio of 4s is underwritable. A portfolio of 5s almost certainly means
  you are not being honest about uncertainty — recalibrate.
- A score of **3** is the typical mid-diligence state. It is also the default
  for sell-side research synthesis without management access.
- A score of **2** signals a material gap requiring resolution before closing.
  Two or more 2s usually means the item is not boundable.
- A score of **1** means the module cannot be assessed with current
  information. Acceptable if acknowledged honestly, but triggers Unboundable
  classification unless remediated.

**Overall boundability score:** sum of six module scores, out of 30.

- 25–30: Boundable
- 18–24: Partially Boundable
- <18: Unboundable

The score is a guide, not a mechanical rule. The Step 5 disqualification gates
override the score.

---

## Step 4: Separate Facts from Inference

In every case and every module, distinguish:

- **Facts** — claims backed by specific source evidence (document, dataset,
  dated conversation)
- **Inference** — claims derived from facts through a stated reasoning chain
- **Assumption** — claims taken as true for the analysis without direct
  evidence

**Rules:**

- Every fact must cite its source
- Every inference must name the fact chain it derives from
- Every assumption must be labeled as such
- Management assertion alone is not a fact — it is an assumption until
  corroborated

The default output format tags each claim with [F], [E], or [H] inline:

- **[F]** fact (sourced)
- **[E]** estimate (reasoned from facts)
- **[H]** hypothesis (plausible, not validated)

If the memo in which this output lands uses a different tagging convention,
align to that — but never drop the distinction.

---

## Step 5: Apply Item-Level Disqualification Gates

These are *item-level* gates that override the overall score. They are
distinct from `driver-tree` thesis-quality gates: driver-tree tests whether
the overall investment case has bounded foundations; Step 5 tests whether each
individual issue assessment is sound.

**Never classify an issue as Boundable if any of the following are true,
regardless of the overall score:**

1. **Perimeter score ≤ 2** — cannot identify what exposure is at stake
2. **Data Quality score ≤ 2** — evidence base is insufficient to support
   quantification
3. **Timing is unknown** — cannot be classified as one-time or recurring, or
   trigger is undefined
4. **No Downside or Severe Case exists** — Outcome Range cannot span credible
   adverse scenarios
5. **The issue cannot be translated into revenue, EBITDA, cash, and timing** —
   qualitative risks that do not hit the P&L or balance sheet through a named
   path are not Boundable
6. **The input register shows a load-bearing T4 driver** — even if module
   scores are high, an unbounded driver cannot be load-bearing in any thesis

When any gate is tripped, classify as **Partially Boundable** (if some modules
are strong and the failing module(s) are named with remediation path) or
**Unboundable** (if remediation is not available).

The gates exist because a high overall score masks a critical gap in a
specific module. Perimeter 2 + 5s everywhere else still scores 27 — but the
item is not boundable because we don't know what's at stake.

---

## Step 6: Build Three Cases + Cascade Scenarios

For every issue, construct three quantified cases.

### 6.1 Three cases

**Base Case — most likely outcome after diligence.** Not the bull case, not a
baseline projection — the case that survives the diligence findings intact.
What actually happens, in the central scenario, after the risk is understood
but before it is mitigated.

**Downside Case — adverse but plausible.** Not a worst case — a realistic
adverse scenario supported by at least one comparable or precedent. What
happens if two or three supporting conditions go against the thesis but no
single catastrophic event occurs.

**Severe But Plausible Case — IC stress case, still credible.** Not the tail.
The scenario an IC member would defend as "we should underwrite against this
being possible." Supported by at least one comparable or precedent where
similar severity manifested. If you cannot point to a precedent, the Severe
case may be too severe (tail) or not severe enough.

**Quantify each case on four dimensions:**

| Dimension | Unit | Format |
|-----------|------|--------|
| Revenue impact | $M or % | Annual or cumulative — state which |
| EBITDA impact | $M or % | Annual or cumulative — state which |
| Cash impact | $M | Cumulative over the hold period |
| Timing | Quarter/year + duration | When it hits, how long it persists |

List **assumptions** for each case — the specific claims that make the case
work. Label each [F] / [E] / [H] per Step 4.

**The case math must reconcile to the deal's underwriting model.** If the
model uses $X entry equity, Y-year hold, Z exit multiple, every case's MOIC
impact must derive from those values. Do not substitute round numbers or
generic assumptions.

### 6.2 Cascade scenarios for material issues

For any issue where the underlying driver is load-bearing or where cascade
risk is structurally material, the three cases must be supplemented with a
cascade scenario that captures driver interactions across the tree. Independent
driver flexes hide cascade risk; cascade scenarios surface it.

**Construction protocol — four steps:**

1. **Identify the trigger driver.** Usually a T3 or T4 driver (T1 drivers
   don't move enough to trigger meaningful cascades). The trigger must be a
   single driver moving outside its expected range, not a combination.
2. **Map first-order linkages.** For each driver in the tree, ask: if the
   trigger fires, does this driver move mechanically? Mechanical linkages are
   accounting identities (working capital reverses if growth slows), capital
   structure linkages (covenant breach if cash flow drops), or operational
   linkages (subsidies cut if take rate falls).
3. **Map second-order behavioral linkages.** Sellers leave the platform if
   subsidies cut. Borrowers default if employment turns. Competitors gain
   share when the incumbent wobbles. Behavioral linkages have wider lag
   distributions and lower confidence than mechanical ones, but they are
   usually the legs of the cascade that do the most damage.
4. **Add transmission lags and feedback loops.** Working capital reverses in
   1–2 quarters; competitive share shifts take 4–8 quarters; regulatory
   action 8+ quarters. Feedback loops — where the second-order effect
   amplifies the first — must be explicitly drawn.

**Construction rules:**

- Build cascades around T3/T4 triggers, not T1.
- Mark each leg as mechanical or behavioral. Mechanical legs are forecasts.
  Behavioral legs are scenarios. Conflating them produces false confidence.
- Always include lag distributions, not just point estimates of timing. The
  damage of cascades is in duration as much as magnitude.

**Cascade properties (descriptive tags, not construction steps):**

- **Transmission speed.** Fast cascades (<2 quarters) are positionable —
  analysts can react. Slow cascades (>4 quarters) are structural — no
  in-flight response is available; the only choice is whether the thesis
  tolerates the cascade.
- **Direction.** Counter-cascade scenarios apply symmetrically. If a downside
  trigger produces compounding negative legs, an upside trigger produces
  compounding positive ones. A complete output should include both downside
  and upside cascades — modeling only the downside biases the thesis toward
  conservative outcomes.

**Cascade discovery — seven external systems.** For any operating business,
construct one downside cascade per external system, even if some are short.
A two-leg cascade is complete if it identifies the trigger and the
transmission. Skipping a system because "the cascade seems short" is how
unknown unknowns hide.

| System | Cascade trigger |
|--------|-----------------|
| Capital markets | Funding cost rises, liquidity contracts, equity multiple compresses |
| Regulators | New rule, enforcement action, license revocation |
| Suppliers and counterparties | Key supplier consolidation, counterparty failure, payment terms tighten |
| Platform owners | App store rules change, advertising policies tighten, distribution access removed |
| Ecosystem partners | Key partner shifts strategy, integrates competitor, exits market |
| Macro environment | Currency shock, recession, sector rotation, geopolitical event |
| Talent and operations | Key personnel loss, operational incident, fraud or governance event |

The cascade output extends but does not replace the three-case structure.
Cases remain the primary quantification; cascades surface compound risk that
individual driver flexes miss.

---

## Step 7: Recommend Underwriting Treatment

For every issue, the underwriting treatment is expressed in five buckets.

### 7.1 The five buckets

**1. Model** — financial model adjustments:
- Revenue growth rate adjustment
- EBITDA margin assumption change
- Working capital / capex modification
- Exit multiple sensitivity
- Probability weight on specific scenarios

**2. Price** — entry price adjustments:
- Price reduction required to hold return hurdle
- Purchase price adjustment mechanism
- Holdback or escrow sizing
- Earn-out structure

**3. Leverage** — capital structure adjustments:
- Maximum sustainable leverage given risk
- Covenant structure (cushion to maintain)
- Tenor / amortization schedule
- Liquidity reserve sizing

**4. Docs / Structure** — deal documentation mitigants:
- Specific reps & warranties required
- Indemnity cap/basket
- Specific performance covenants
- Information rights post-close
- Governance provisions (board seats, consent rights)

**5. Operating Plan** — post-close operational actions:
- Management changes
- Capability builds or hires
- Cost-out program
- Capex pull-forward or deferral
- Specific KPI targets and cadence

**Every Boundable or Partially Boundable item must produce at least one action
across the five buckets.** An item labeled Boundable but generating no
underwriting action is a labeling error — either the assessment was wrong or
the item was not material.

### 7.2 Deal type variants

The framework applies to both PE control and public equity long, but the
weights differ. Document the variant at the start of each assessment.

**PE Control (buyout, acquisition, majority investment):** all five buckets
active. Every Boundable or Partially Boundable item should produce actions
across at least 3 of 5 buckets.

| Bucket | Typical actions (PE control) |
|--------|------------------------------|
| Model | Full set — revenue, EBITDA, capex, working capital, exit multiple |
| Price | Entry valuation concession, PPA, earn-out, holdback, escrow |
| Leverage | Full capital structure decision — quantum, tenor, covenants, reserves |
| Docs / Structure | R&W, indemnity caps, performance covenants, info rights, governance |
| Operating Plan | Management changes, capability builds, cost-out, capex, KPI cadence |

**Public Equity Long:** three buckets collapse or drop because the investor
has no negotiation, no capital structure decision, no governance rights.

| Bucket | Typical actions (public equity long) |
|--------|---------------------------------------|
| Model | Full set; probability-weighted scenarios, sensitivity analysis, MOIC contribution weights |
| Price | **Reframed as "entry discipline"** — not a concession negotiation. Position entry at a target price providing adequate margin of safety; exit if current price compresses margin of safety below threshold |
| Leverage | **N/A for most positions.** Only relevant if position is levered (margin, derivatives) |
| Docs / Structure | **N/A.** No negotiation, no contract, no protective provisions |
| Operating Plan | **Reframed as "monitoring cadence"** — not operational intervention. Specific KPIs to watch, frequency of review, event triggers for position reassessment |

In public equity long, every Boundable or Partially Boundable item should
produce actions across the remaining active buckets (Model,
Price-as-entry-discipline, Operations-as-monitoring). Items generating only
Model adjustments with no entry discipline or monitoring plan are
incompletely underwritten.

**Other variants** (minority equity, debt, real estate, infrastructure):
document which buckets apply at the start of the assessment. The six-module
definition is unchanged; only the action surface differs.

**Reconciliation with pre-mortem.** The pre-mortem skill's 9-field deep dives
include an "Underwriting treatment" field that also splits by deal type. If
pre-mortem already ran with the same variant, the boundability treatment
should extend or refine pre-mortem's — not contradict it. Where they
conflict, resolve before delivering.

---

## Step 8: Residual Risk, Data Requests, Kill Trigger

Every issue closes with three mandatory fields.

### Residual Risk

What remains after all mitigants are applied? Quantify if possible. This is
what the investor is actually taking on after the underwriting treatment.

### Data Requests

Specific data items that would sharpen the assessment:

- Name the exact data (not "more diligence" but "vintage-level NPL by
  origination quarter, Q1-2024 through Q1-2026")
- Name the source (IR team, Tegus expert network, industry database)
- Name what changes in the assessment if the data comes back one way vs.
  another

For T3/T4 drivers inherited from `driver-tree`, data requests should
specifically name what evidence would move the driver to a higher tier and
whether that evidence is gettable through primary research / waiting /
management disclosure / industry data.

### Kill Trigger

A specific, observable event or data point that — if it occurs — changes the
underwriting decision. Format:

> "If [specific observable], then [specific action: exit position / reprice /
> trigger indemnity / escalate to full review]."

The trigger must be:

- **Falsifiable** — a concrete metric or event, not a qualitative judgment
- **Observable** — monitorable from outside the company without special access
- **Actionable** — the "then" clause specifies a concrete response

If the issue has an Unboundable component, the kill trigger should be tied to
the Boundable component (e.g., a data request completing, an observable
metric crossing a threshold) rather than to an observation that would require
the Unboundable component to resolve first.

---

## Step 9: Output Format

Produce an input register (from Step 1), one issue object per material risk
(from Steps 2-8), a deal summary across all issues, and a final deal view.

### Input Register Output (Step 1 deliverable)

The input register precedes the issue objects:

```
BOUNDABILITY INPUT REGISTER — [Deal name]

Input state: Complete / Partial / Provisional
Authoritative driver-tree loaded: Yes / No
Pre-mortem loaded: Yes / No
Claim-scrutinizer loaded: Yes / No
NTB registry loaded: Yes / No

| Input ID | Source | Type | Tier / evidence state | Materiality | Proceed? |
|---|---|---|---|---|---|
| D1 | driver-tree | Driver | T2 | $X EBITDA / Y bps MOIC | Yes |
| FM1 | pre-mortem | Failure mode | Partially known | $X downside | Yes |
| C1 | claim-scrutinizer | Claim gap | Unsupported | Load-bearing claim | Yes |

Unresolved input gaps:
  - [Gap] — [owning skill or diligence source needed]
```

### Per-Issue Object (JSON)

```json
{
  "issue_id": "R1",
  "title": "Monee seasoned-vintage NPL deterioration",
  "category": "Financial Structure",
  "risk_statement": "There is a risk that Monee seasoned-vintage NPL reaches 2.5–3.0% causes EBITDA compression of $1.0B annually within Q3 2026 – Q4 2027, driven by 2022–2023 origination cohorts deteriorating as they complete seasoning.",
  "materiality": "high",

  "input_inheritance": {
    "driver_id": "Monee.C2",
    "tier": "T3",
    "rubric_score": "5/10 (gating rule G2 applied)",
    "direction": "Headwind / binary tail",
    "reference_class": "EM consumer fintech books growing >50% annually entering first credit cycle",
    "base_rate": "~25% maintain stable loss rates through first cycle",
    "vintage": "Q1 FY26",
    "management_modulation": "B (T1 drivers behave as T2 in stress)"
  },

  "perimeter": { ... },
  "timing": { ... },
  "data_quality": { ... },
  "outcome_range": { ... },
  "precedent_observability": { ... },
  "mitigants": { ... },

  "overall_boundability_score": 16,
  "classification": "partially_boundable",

  "cascade_scenario": {
    "trigger": "Monee 2022-2023 vintages reach peak seasoning during weakening macro",
    "legs": [
      {"step": 1, "leg": "Vintage NPL reaches 2.5%", "type": "trigger", "lag": "T+0"},
      {"step": 2, "leg": "Provisioning surge $1.0B", "type": "mechanical", "lag": "T+1Q"},
      {"step": 3, "leg": "Loan book growth throttles 30→15%", "type": "behavioral", "lag": "T+2Q"},
      {"step": 4, "leg": "Group EBITDA -$1.3B annual", "type": "mechanical", "lag": "T+3Q"},
      {"step": 5, "leg": "Multiple compresses 12x → 9x", "type": "behavioral", "lag": "T+4Q"}
    ]
  },

  "underwriting_treatment": { ... },
  "data_requests": [...],
  "kill_trigger": "..."
}
```

The input-inheritance block is mandatory for every issue object. Without it,
upstream work is invisible to downstream readers.

### Per-Issue Markdown Format (for IC memo inclusion)

When the output will be included directly in an IC memo (not processed as
data), use markdown format. Content is identical to JSON; only presentation
differs.

```markdown
#### Issue R1 — Monee Seasoned-Vintage NPL Deterioration

**Category:** Financial Structure
**Materiality:** High
**Classification:** Partially Boundable (score 16/30)
**Deal type variant:** Public equity long

**Input inheritance:**
- Driver: Monee.C2 (cohort seasoning losses)
- Tier: T3 (rubric 5/10, gating rule G2 applied — track record floor)
- Direction: Headwind / binary tail
- Reference class: EM consumer fintech books growing >50% annually entering
  first credit cycle. Base rate: ~25% maintain stable loss rates through cycle.
- Vintage: Q1 FY26
- Management modulation: B grade (T1 drivers behave as T2 in stress)

**Risk statement:** There is a risk that Monee seasoned-vintage NPL reaches
2.5–3.0% causes EBITDA compression of $1.0B annually within Q3 2026 – Q4 2027,
driven by 2022–2023 origination cohorts deteriorating as they complete seasoning.

**Perimeter [score 3/5]:** ...
**Timing [score 3/5]:** ...
**Data quality [score 2/5]:** ...
**Outcome range [score 2/5]:** ...
**Precedent / observability [score 3/5]:** ...
**Mitigants [score 3/5]:** ...

**Cascade scenario:** ...
**Underwriting treatment (public equity long):** ...
**Data requests:** ...
**Kill trigger:** ...
```

Use JSON when the output will be processed programmatically. Use markdown when
the output will be pasted directly into an IC memo or reviewed as prose.

### Deal Summary

```
DEAL SUMMARY

Input register summary:
  Load-bearing inputs identified: [N]
    T1: [N] (specify: which drivers)
    T2: [N]
    T3: [N]
  Non-load-bearing T4 drivers flagged: [N]
  Driver-tree thesis-quality gates passed: [X / 3 or not available]
  Variance-dominant driver(s): [list]

Total issues assessed (six-module assessment): [N]
  Boundable: [N] (score ≥25)
  Partially Boundable: [N] (score 18–24)
  Unboundable: [N] (score <18 or disqualification gate tripped)

Aggregate financial exposure:
  Base case: $[X]M EBITDA, [Y]x MOIC
  Downside: $[X]M EBITDA, [Y]x MOIC
  Severe:   $[X]M EBITDA, [Y]x MOIC

Cascade aggregate impact:
  Base case → cascade case: -[X]% EBITDA, -[Y]% EV
  Cascades modeled: [count] downside, [count] upside

Top 3 highest-materiality issues:
  1. [R#] [Title] — classification — key gap
  2. [R#] [Title] — classification — key gap
  3. [R#] [Title] — classification — key gap

Underwriting actions summary:
  Model adjustments required: [count]
  Price concessions required: [count]
  Structural protections required: [count]
  Operating plan actions required: [count]

Residual unboundable exposure: $[X]M Severe case across all unboundable items
```

### Final Deal View

| Verdict | Criteria |
|---------|----------|
| **Proceed** | Driver-tree thesis-quality gates all pass when available; all material issues Boundable; no item-level disqualification gates tripped; Severe case aggregate ≤ acceptable loss threshold |
| **Proceed with protections** | Driver-tree gates substantially pass when available; most issues Boundable; Partially Boundable items have named structural/financing/operational mitigants reducing residual to acceptable |
| **Reprice** | Multiple issues Partially Boundable; mitigants insufficient; need price concession to offset residual risk (state concession magnitude) |
| **Pass** | Any of: (a) driver-tree minimum bounded foundation gate failed, (b) driver-tree single-driver risk gate failed (load-bearing T4), (c) ≥2 material issues Unboundable, (d) cannot construct acceptable underwriting treatment for a material issue |

The verdict must be supported by the specific findings above. If "Reprice,"
state the required concession in dollars or percent. If "Pass," state which
gate(s) and/or item(s) drove the decision.

---

## Step 10: Operating Standards

These rules apply across the entire skill. They are constraints on output, not
a sequential step.

**Input register first, module scoring second.** Do not begin 6-module scoring
without a completed input register. Driver-tree surfaces load-bearing drivers;
pre-mortem surfaces failure modes; claim-scrutinizer surfaces weak claims; the
6 modules assess those inputs. Skipping the register produces assessments on
whatever risks an analyst happened to think of.

**Two distinct gate layers.** Driver-tree thesis-quality gates test whether
the overall investment case has bounded foundations. Step 5 item-level gates
test whether each individual issue assessment is sound. Both must pass when
driver-tree gates are available. Failure at either level disqualifies a
Boundable classification.

**The two-definition test.** Every load-bearing driver must be internally
consistent across `driver-tree` and boundability: a T1 driver should usually
produce Boundable (with possible exceptions for Module 6 / mitigant gaps); a
T4 driver should produce Unboundable. If they do not agree, investigate before
shipping.

**The six-condition definition is the spec.** Every six-module rule, every score,
every classification traces back to whether the six conditions hold. Do not
add heuristics that bypass the definition — if an item feels underwritable
but fails three modules, it is not boundable.

**Quantify everything you can; label honestly what you cannot.** A Partially
Boundable classification with a clear named gap is a better output than a
Boundable classification that papers over uncertainty.

**The underwriting treatment is the output.** Analysis that does not convert
to action in one of the five buckets has not done its job. An issue labeled
Boundable with no underwriting action is a contradiction.

**Every score has a named basis.** Evidence state or module score must state
what evidence or gap drove the score. Tier assignments are inherited from
`driver-tree`; do not create or alter them inside boundability.

**Inter-rater reliability discipline.** Module scoring in Step 3 must be
calibrated across analysts. Quarterly calibration exercises pick five active
issue objects; three or more analysts score them independently; disagreements
are categorized and the rubric refined.

**Cascade scenarios are required for material issues.** Independent driver
flexes hide cascade risk. Any issue where the driver is load-bearing or where
cross-segment transmission is plausible must include a cascade scenario per
Step 6.2.

**Reconcile with pre-mortem.** If pre-mortem already ran and marked a failure
mode as boundable, boundability should normally produce a score ≥25 unless the
input register exposes a missing driver, claim, evidence, or mitigant gap. If
the two assessments disagree, resolve the gap before shipping IC materials.

**Separate the assessment from the decision.** This skill produces structured
boundability output. It does not recommend whether to do the deal. The IC
makes that call using the output as input.

**Single-asset analysis only.** This skill assesses one investment at a time
— thesis structure, driver evidence, and underwriting actions for a specific
deal. It does not perform portfolio construction, position sizing, NAV
allocation, or cross-position aggregation. Those are downstream decisions
that take this skill's output as input.

---

## References

```
If pre-mortem has already run on this deal:
  → Load the failure mode registry and use the same NTB numbering
  → Each material failure mode typically becomes one or more issue objects here
  → {SKILL_DIR}/../pre-mortem/SKILL.md

If claim-scrutinizer has already run:
  → Use its flagged claims as diligence items; they may become issue objects
  → Bull-case claims that map to T4 drivers cannot be load-bearing
  → {SKILL_DIR}/../claim-scrutinizer/SKILL.md

If ntb-diligence has already run:
  → Cross-reference NTB registry; each NTB typically generates ≥1 boundability
    item AND maps to one or more source inputs in the register
  → {SKILL_DIR}/../ntb-diligence/SKILL.md

If a deal model exists:
  → Use its authoritative entry equity, exit multiple, hold period, and base
    case projections as the reconciliation anchor for every case's quantification
  → Use the model's revenue/EBITDA structure as a source input in the register
    and reconcile to `driver-tree` rather than building a parallel decomposition
  → Do not substitute round numbers or generic assumptions

If writing-style runs downstream:
  → Every fact in the output must cite source; every inference must be labeled;
    every assumption must be marked [F]/[E]/[H]
  → {SKILL_DIR}/../writing-style/SKILL.md
```
