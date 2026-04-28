---
name: driver-tree
description: |
  Decomposes investment theses into MECE driver trees, assigns evidence tiers
  (T1–T4) to each leaf node, and surfaces what a thesis is actually built on.
  Use when Ian asks to "build a driver tree," "decompose this thesis," "score
  the drivers," "map the revenue tree," "what's load-bearing in this thesis,"
  "tier the drivers," "run a base-rate overlay," "check the vintage on this
  evidence," "run a cascade scenario," "what's the variance-dominant driver,"
  or "do a structural assessment of [company]." Single-asset methodology only.
  Produces a driver tree with tiers and directionality, segment driver tables
  with historical/today/path/tier/impact/boundability columns, base-rate overlay
  for load-bearing drivers, vintage check on supporting evidence, variance
  amplification analysis, downside and upside cascade scenarios, and a
  framework self-audit. Output is a methodology document — does not produce
  underwriting actions, deal verdicts, or position sizing. Distinct from
  boundability (which converts driver work into underwriting structure),
  pre-mortem (which enumerates failure pathways), and claim-scrutinizer
  (which tests bull-case logic). Driver-tree is the structural decomposition
  step that those other skills build on.
---

# Driver Tree — Single-Asset Methodology

You decompose a thesis into a MECE driver tree, assign evidence tiers to every
leaf node, and surface what the thesis is actually built on. You produce a
methodology document — not a deal verdict, not underwriting actions, not
position sizing.

You do not editorialize. You produce a structured assessment that another
analyst, an IC, or a downstream skill (boundability, pre-mortem) can use as
input.

Read this entire file before beginning.

---

## Architecture

The skill runs in a fixed sequence. Each step produces an output that feeds
the next:

```
1. Construct driver tree            (Section 1)
2. Apply variance amplification     (Section 2)
3. Assign tiers via 5-dim rubric    (Section 3)
4. Apply gating rules               (Section 4)
5. Apply base-rate overlay          (Section 5)
6. Apply vintage discipline         (Section 6)
7. Build segment driver tables      (Section 7)
8. Build cascade scenarios          (Section 8)
9. Carry-forward + self-audit       (Section 9)
```

The skill produces five deliverables: the driver tree itself, segment driver
tables, a base-rate overlay table, a vintage check table, and downside +
upside cascade scenarios. It does NOT produce underwriting actions, deal
verdicts, or position sizing — that is `boundability`'s job, downstream.

---

## Where this skill sits

```
driver-tree         ← YOU ARE HERE — structural decomposition + tier assignment
      │
      ├── pre-mortem           ← parallel: failure mode inventory (out-of-tree risks)
      ├── claim-scrutinizer    ← parallel: bull-case logic redline
      ├── boundability         ← downstream: converts driver work to underwriting
      ├── mckinsey-consultant  ← shared analytical OS
      └── pattern-docx         ← downstream: methodology doc output
```

The skill is **single-asset analysis only**. It does not perform portfolio
construction, position sizing, or cross-position aggregation. It also does not
assess structural risks that sit outside the driver tree (regulatory action,
capital-market shocks, platform-policy changes, macro tail events) — those
require a separate `pre-mortem` pass. This is by design and is documented in
the framework self-audit (Section 9).

---

## Step 1 — Construct the driver tree

A driver tree decomposes an outcome (revenue, EBITDA, IRR, market share) into
the underlying levers that mechanically produce it. The point is not the
picture. The point is to force specificity about which lever is doing the
work.

### Five construction rules

**Rule 1: Decompose by mechanical identity, not by narrative.** Every parent
node should equal the sum or product of its children by construction. If you
cannot write the math that connects parent to children, the decomposition is
wrong. "Growth comes from new markets and existing markets" is a narrative —
"Revenue = Σ(country GMV × take rate)" is a tree.

**Rule 2: Decompose to the level where evidence exists.** Bottom out at the
level where you can find data. Decomposing AOV further into "category mix ×
price-per-SKU × discount rate" is only useful if you have those three data
points. Otherwise the deeper levels are imaginary precision.

**Rule 3: Choose the right top-level split.** For multi-segment businesses,
split by reporting segment first — different segments have different drivers
and competitive dynamics. For single-segment businesses, split by volume × price
or, for subscription businesses, ARR = (customers × price × retention).

**Rule 4: Tag each driver with directionality.** Six possible tags: tailwind,
headwind, contested, cyclical, binary, optionality.

- **Binary** is reserved for bimodal distributions — drivers that either work
  or break (long-running F2P game franchises, regulatory licensing).
- **Optionality** is reserved for asymmetric distributions where downside is
  bounded by management discipline while upside is open-ended.

If every driver in the tree is a tailwind, you have built a sales pitch, not
an analysis.

**Rule 5: Flag driver correlations explicitly.** A tree is technically MECE in
a static accounting snapshot but causally not MECE if drivers share a common
upstream cause. When two leaf nodes share an upstream cause (subsidy spend,
marketing budget, ecosystem flywheel), mark them as correlated. Scenario flexes
must move correlated drivers in the same direction.

### Construction discipline

The tree must include:
- The outcome being modeled (specific quantity, e.g., "FY28 revenue")
- The decomposition basis (the math: A × B, A + B, etc.)
- Every leaf node tagged for directionality
- Correlation flags between leaf nodes that share upstream causes
- Time horizon for the forecast period

The tree must NOT include:
- Drivers without a mechanical connection to a parent
- Decomposition deeper than the level where evidence exists
- Untagged leaf nodes
- Implicit correlations that aren't drawn

---

## Step 2 — Apply the variance amplification rule

Multiplicative trees behave differently from additive trees. In multiplicative
trees, the variance of the parent is dominated by the highest-variance child —
which changes which driver actually matters for thesis risk.

For a multiplicative tree where Parent = X × Y × Z, the coefficient of
variation of the parent (σ/μ) approximately equals the square root of the sum
of squared CVs of the children. If X has CV 0.10 (T1), Y has CV 0.15 (T2), and
Z has CV 0.50 (T3), the parent's CV ≈ 0.53 — completely dominated by Z. The T1
and T2 children effectively don't matter for parent variance.

For additive trees where Parent = A + B + C with shares of 60/30/10, the
parent CV is approximately the share-weighted CV of the children. A
high-variance 10%-share child contributes only 10% to parent variance.

### Practical implication

In multiplicative nodes, the load-bearing driver is the highest-variance
child, not the child with the cleanest story. The thesis "rests on driver X"
is rhetorically appealing only if X is genuinely the variance-dominant driver.
Often it is not.

After constructing the tree, label each parent node as additive or
multiplicative and identify the variance-dominant child for each
multiplicative node. This identification is part of the deliverable — it is
not optional commentary.

### Decomposition strategy guidance

When the analyst has equivalent decomposition choices (Customers × ARPU vs.
Segment 1 + Segment 2 + Segment 3), prefer the decomposition that places the
highest-variance driver in an additive position. Multiplicative position lets
a single high-variance driver dominate. Additive position bounds its effect to
its share.

**Caveat:** the right decomposition is the one that matches the mechanical
structure of the business. Choosing decompositions to minimize apparent
variance is decomposition-shopping — the same epistemic error as cherry-picking
analogs. The variance amplification rule is a diagnostic, not a license to
restructure trees for narrative convenience.

---

## Step 3 — Assign tiers via the 5-dimension rubric

Score each leaf node against five evidence dimensions on a 0–2 scale:

| Dimension | Score = 0 | Score = 1 | Score = 2 |
|-----------|-----------|-----------|-----------|
| **Source count** | No external source; management assertion only | One independent external source | Three or more independent external sources |
| **Source quality** | Qualitative claim, expert opinion, or vendor data with conflict of interest | One rigorous source (audited, peer-reviewed, primary research with sample size) | Multiple rigorous sources OR mechanical/contractual constraint |
| **Triangulation** | Sources do not agree, or only one source exists | Sources directionally agree but ranges differ by >2x | Sources triangulate to within 25% of each other |
| **Analog comparability** | No analog, or analog in structurally different market | Analog with material differences | Multiple analogs in comparable markets |
| **Track record** | Driver never observed in the company or comparable companies | <2 years or <2 cycles | Multiple market cycles in this company or close peers |

### Score-to-tier mapping

| Total (0–10) | Tier | Treatment in thesis |
|--------------|------|---------------------|
| 8–10 | **T1 Bounded** | Load-bearing acceptable. Range typically ±5–10%. |
| 5–7 | **T2 Partially bounded** | Supports thesis; should not be single point of failure. Range ±10–25%. |
| 2–4 | **T3 Loosely bounded** | Sensitivity, not base case. Range ±25–50%. |
| 0–1 | **T4 Unbounded** | Cannot be load-bearing. Range >±50% or bimodal. |

### Two-analyst test

If two analysts looking at the same evidence assign different tiers, the
rubric is not falsifiable enough. The dimensions above are calibrated so each
score is a yes-or-no question, not a judgment call. When in doubt about a
score, document the specific evidence considered and the ambiguity — this
makes the disagreement diagnosable.

---

## Step 4 — Apply gating rules

Some rubric dimensions are gating, not additive. If a gating dimension scores
zero, no amount of strength elsewhere produces a high tier:

| Rule | Effect | Rationale |
|------|--------|-----------|
| **G1 Source-quality floor** | If source quality = 0, max tier is T3 | No rigorous source means the entire driver rests on assertion |
| **G2 Track-record floor** | If track record = 0 AND outcome depends on relationship persistence (cyclical, behavioral, regulatory), max tier is T3 | A relationship never observed under stress cannot be tagged T1 regardless of point-in-time evidence |
| **G3 Triangulation floor** | If triangulation = 0, max tier is T2 | A single source cannot triangulate; bounded only as well as that source |
| **G4 Analog floor** | If structurally novel AND analog comparability = 0, max tier is T3 | Novel situations cannot be bounded by historical evidence alone |

The gating rules exist because the additive rubric can produce false confidence
when a structural weakness exists. A driver with three T1-quality sources but
no track record under stress is not the same as a driver with full evidence
across all dimensions.

When a gating rule fires, document which rule fired and why. The final tier
should be stated as "T3 (G2 applied)" or similar — not just "T3."

---

## Step 5 — Apply base-rate overlay for load-bearing drivers

Tier assignment is about evidence quality for a specific driver. Investment
outcomes are also shaped by base rates — the historical frequency of outcomes
in the relevant reference class. A T1 driver in a 20% base-rate reference
class is a thesis betting the company is in the top quintile, which must be
argued explicitly.

### Discipline rules

**Rule 1: Every load-bearing driver carries a reference class and base rate.**
A load-bearing driver is any T1 or T2 driver in the primary value-creation
logic. The reference class must be specific enough to be meaningful — "EM
fintech" is too broad; "EM consumer credit books growing >50% annually
entering first credit cycle" is the actual reference class.

**Rule 2: When tier and base rate diverge, the divergence is the analytical
insight.** A T1 driver with a 20% base rate is a thesis betting the company is
in the top quintile of its reference class. This is a defensible position but
must be argued explicitly, not assumed.

**Rule 3: Base rates must be sourced.** Acceptable sources: academic studies
of comparable cohorts, industry consortium data, regulator-published outcome
statistics, structured analog company analyses. "My sense is that about 30% of
these work" is not a base rate — it is expert judgment that should be tagged
[H] hypothesis.

### Output format

Produce a base-rate overlay table with one row per load-bearing driver:

| Driver | Tier | Reference class | Base rate | Implied stance |
|--------|------|-----------------|-----------|----------------|

The "implied stance" column should state whether tier and base rate are
aligned (high confidence), diverge (thesis is betting on outlier outcome), or
contested.

---

## Step 6 — Apply vintage discipline

Each driver carries a vintage — the date of the most recent supporting
evidence. Evidence decays. A driver that was T1 in 2023 may be T3 in 2026 if
the underlying market structure has shifted, even without new contradicting
evidence arriving.

### Vintage thresholds

| Vintage age | Required action |
|-------------|-----------------|
| <24 months | Standard refresh; quarterly review sufficient |
| 24–36 months | Explicit re-validation required (see below) |
| >36 months | Tier auto-reduces by one level until re-validated |

Fast-changing markets carry shorter lives: 18 months for fintech regulation,
12 months for consumer behavior in markets undergoing platform transitions,
24 months for stable operating businesses.

### Re-validation discipline

Re-validation is not the same as re-confirmation. Re-validating a tier
requires actively seeking disconfirming evidence ("is there evidence that the
relationship that produced this tier no longer holds?"), not just confirming
that the old evidence still exists.

The most uncomfortable application is to "obviously still true" drivers — a
fresh metric supporting a stale inference is not the same as a well-bounded
driver. A reported NPL ratio that is fresh but supports an inference about
through-cycle losses is itself stale if the relationship has never been
observed through a stress event.

### Output format

Produce a vintage check table:

| Driver | Tier | Vintage | Decay risk | Re-validation action |
|--------|------|---------|------------|----------------------|

---

## Step 7 — Build segment driver tables

For each top-level segment, build a complete driver table using this format:

| Driver | Historical | Today | Underwritten path | Tier | Impact | Boundability |
|--------|-----------|-------|-------------------|------|--------|--------------|

Each column has a specific purpose:

- **Driver:** specific leaf node, with parent identifier (e.g., "A1. Buyer count")
- **Historical:** the prior trajectory; what it was doing 2–3 years back
- **Today:** the current metric, with date or quarter stamp
- **Underwritten path:** the assumption about where it goes — should be
  expressed as a claim, not a forecast
- **Tier:** T1 / T2 / T3 / T4 with rubric score and any gating rule applied
- **Impact:** Very High / High / Medium / Low — relative valuation impact
- **Boundability:** one-sentence rationale for the tier — why this score, what
  evidence supports or limits it

After the table, write a "reading the table" paragraph that pulls out:
- The cleanest positive driver (typically the highest-tier tailwind)
- The dominant unresolved risk (typically the lowest-tier headwind)
- Any Rule 5 driver correlations that affect scenario flexing

If the segment has structural quirks worth flagging (funding constraints,
binary-tail risks, cross-segment dependencies), include a single note
paragraph after the reading paragraph.

---

## Step 8 — Build cascade scenarios

Independent driver flexes hide cascade risk. A cascade scenario captures
driver interactions across the tree — the case where one driver moving
outside its expected range mechanically and behaviorally moves others.
Cascades are where most thesis failures actually live, because that is where
independence assumptions break.

### Construction protocol

1. **Identify the trigger driver.** Usually a T3 or T4 driver — T1 drivers
   don't move enough to start a cascade. The trigger must be a single driver
   moving outside its expected range, not a combination.
2. **Map first-order mechanical linkages.** For each driver in the tree, ask:
   if the trigger fires, does this move mechanically? Mechanical linkages are
   accounting identities (working capital reverses if growth slows), capital
   structure linkages (covenant breach if cash flow drops), or operational
   linkages (subsidies cut if take rate falls).
3. **Map second-order behavioral linkages.** Sellers leave the platform if
   subsidies cut. Borrowers default if employment turns. Competitors gain
   share when the incumbent wobbles. Behavioral linkages have wider lag
   distributions and lower confidence than mechanical ones, but they usually
   do the most damage.
4. **Add transmission lags and feedback loops.** Working capital reverses in
   1–2 quarters; competitive shifts take 4–8 quarters; regulatory action 8+
   quarters. Feedback loops — where the second-order effect amplifies the
   first — must be explicitly drawn.

### Required: both downside AND upside cascades

Counter-cascades apply symmetrically. If a downside trigger produces
compounding negative legs, an upside trigger produces compounding positive
ones. Modeling only the downside biases the thesis toward conservative
outcomes — a complete output requires both.

### Cascade discipline rules

- Build cascades around T3/T4 triggers, not T1 triggers
- Mark each leg as mechanical or behavioral. Mechanical legs are forecasts;
  behavioral legs are scenarios. Conflating them produces false confidence.
- Always include lag distributions, not just point estimates of timing. The
  damage of cascades is in duration as much as magnitude.

### Output format

For each cascade (downside and upside), produce:

1. **Trigger statement** — single sentence naming the trigger driver and the
   specific stress range it moves to
2. **Cascade map** as a table:

| Step | Cascade leg | Mechanism | Lag | Type |
|------|-------------|-----------|-----|------|

Type column values: trigger / mechanical / behavioral.

3. **Optional illustrative quantification** — if the cascade is being used to
   inform IC discussion, show base / cascade-case impact on revenue, EBITDA,
   and EV. Label as "illustrative" — these are scenario impacts, not model
   outputs.

---

## Step 9 — Carry-forward + framework self-audit

The driver tree is not the end of the analysis. It is a structured input for
adversarial review and downstream skills (boundability, pre-mortem). This
step produces two outputs.

### Carry-forward — what would resolve the unbounded drivers

The point of identifying T3 and T4 drivers is not to abandon analysis. It is
to specify what evidence would move the driver to a higher tier — and decide
whether that evidence is gettable.

| Driver | Tier | What would bound it | Gettable? |
|--------|------|---------------------|-----------|

The "Gettable?" column should be: Yes (primary research), Partial (some data
available, full data requires waiting), Hard (company has not historically
disclosed), No (genuinely unforecastable — accept and price accordingly).

### Framework self-audit

Every driver-tree analysis must close with an explicit acknowledgment of the
framework's limits. State in plain language:

1. **Out-of-tree structural risks.** The framework addresses analytical risk
   (how confidently can a driver's range be narrowed using evidence?) but does
   not address structural risk (catastrophic outcomes that sit outside the
   driver tree entirely). Regulatory action, capital-market shocks, platform-
   policy changes, and macro events sit outside the tree. A separate
   pre-mortem pass is required.

2. **Boundability is not probability.** Tiers describe how narrow the
   plausible range is, not how likely the point estimate is. A T1 driver with
   a 10% range can still land outside that range. A T4 driver with a 100%
   range can still land at the center.

3. **Inter-rater calibration is untested.** The two-analyst test is
   aspirational unless the rubric has been empirically calibrated across
   analysts on a calibration set. Note explicitly whether calibration has
   been done.

4. **The framework is gameable.** An analyst can pass thesis-quality gates by
   identifying a genuinely T1 driver and placing it in "primary
   value-creation logic" while the actual thesis depends on T3 and T4
   drivers in subsidiary roles. Adversarial review (claim-scrutinizer,
   red-team) is required, not optional.

---

## Output format

The skill produces a single methodology document with these sections in
order:

1. **Cover page** — outcome modeled, decomposition basis, time horizon
2. **Driver tree** — full tree with directionality tags and correlation flags
3. **Variance amplification** — additive vs. multiplicative classification per
   parent node; variance-dominant child for each multiplicative node
4. **Per-segment driver tables** — one table per segment with the seven
   columns (driver / historical / today / path / tier / impact / boundability)
5. **Base-rate overlay** — load-bearing drivers with reference classes and
   base rates
6. **Vintage check** — drivers with vintage age and decay risk
7. **Downside cascade** — trigger, leg map, optional quantification
8. **Upside cascade** — trigger, leg map, optional quantification
9. **Carry-forward** — what would resolve unbounded drivers
10. **Framework self-audit** — explicit acknowledgment of framework limits

The document should be 15–25 pages depending on segment count and tree depth.
Use Pattern docx formatting (`pattern-docx` skill) when delivering as a Word
document. Use markdown when output is feeding into another skill or being
reviewed in chat.

### Mandatory reconciliations

The output must reconcile across sections:

- Tier assignments in the driver tables must match the rubric scores in the
  base-rate overlay and vintage check
- Variance-dominant drivers identified in Section 3 must reappear in the
  cascade triggers (the variance-dominant driver is usually the right cascade
  trigger)
- Correlation flags from Rule 5 must be respected in cascade construction —
  correlated drivers move together, not independently

If the reconciliations don't hold, fix the underlying analysis before
delivering.

---

## Operating standards

These rules apply across every output:

**Single-asset analysis only.** This skill assesses one investment at a
time. It does not perform portfolio construction, position sizing, NAV
allocation, or cross-position aggregation. Those are downstream decisions
that take this skill's output as input.

**Methodology output, not deal verdict.** This skill produces a structured
analysis. It does not recommend whether to proceed, reprice, or pass on a
deal. Those verdicts come from `boundability` (which uses driver-tree as
input) or from the IC.

**Every score has a named basis.** Tier, rubric dimension, base rate, or
vintage — do not assign without stating what evidence drove the score. Tier
assignments specifically must carry the rubric breakdown (0–10 across five
dimensions) and any gating rules applied.

**Quantify what you can; label honestly what you cannot.** A T3 driver
clearly tagged is more useful than a T2 driver with concealed weak evidence.

**Adversarial review is required, not optional.** This skill produces
structural decomposition. The decomposition is one input among several.
Always run claim-scrutinizer and red-team passes on the output before
treating it as analytical ground truth.

**Reconcile with adjacent skills.** If pre-mortem has already run and labeled
a failure mode boundable, the corresponding driver in this tree should be T1
or T2. If claim-scrutinizer has flagged a bull-case claim as weakly supported,
the corresponding driver should not be tagged T1.

---

## References

```
If pre-mortem has already run on this deal:
  → Failure modes that are tree-mappable should appear as T3/T4 drivers in
    the tree
  → Out-of-tree structural risks remain pre-mortem's territory
  → /mnt/skills/user/pre-mortem/SKILL.md

If claim-scrutinizer has already run:
  → Bull-case claims that map to T4 drivers cannot be load-bearing in the
    underwritten path
  → Drivers tagged T1 in this tree should correspond to claim-scrutinizer
    "supported" verdicts
  → /mnt/skills/user/claim-scrutinizer/SKILL.md

If a deal model exists:
  → Use the model's revenue/EBITDA structure as the starting point for the
    driver tree (do not build a parallel decomposition that contradicts the
    model)
  → Use authoritative entry equity, exit multiple, hold period, and base
    case projections for any cascade quantification

If the analysis will hand off to boundability:
  → Driver tree + tier assignments become Step 1 of boundability
  → Load-bearing T1/T2 drivers and material T3/T4 risks proceed to
    boundability's Layer 2 6-module assessment
  → /mnt/skills/user/boundability/SKILL.md

Worked example:
  → A complete worked example using Sea Ltd (NYSE: SE) is available in
    references/sea_ltd_worked_example.md. Load when the analyst wants to see
    a fully populated tree-and-tables output, especially for understanding
    how Rule 5 correlations and variance amplification show up in practice.
```
