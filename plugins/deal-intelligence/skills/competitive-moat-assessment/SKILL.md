---
name: competitive-moat-assessment
description: |
  Build a rigorous, evidence-based assessment of a company's competitive moat — the
  structural advantage that allows it to earn above-market returns sustainably. Use
  this skill whenever Ian asks to "assess the moat," "analyze competitive advantage,"
  "how defensible is this business," "what protects this company," "evaluate the moat,"
  "is this moat real," "rate the competitive position," or "what makes this business
  hard to displace." Also triggers for: "switching cost analysis," "network effect
  analysis," "competitive defensibility," "moat durability," "barrier to entry."

  This skill builds the affirmative case for a moat with the specific evidence standard
  required to survive adversarial IC scrutiny. It is distinct from:
  - Competitor profiling (market-research Level 2 — describes what competitors do)
  - Moat attack vectors (red-team-investment-attacks.md — challenges moat claims)
  - Moat type taxonomy (mckinsey-consultant Dimension 4 — lists moat categories)

  This skill owns the methodology for PROVING a moat is real, measuring its strength,
  assessing its durability, and producing an IC-ready moat verdict.
---

# Competitive Moat Assessment

You are building an evidence-based case for or against a competitive moat. Read this
entire file before beginning.

A moat assessment is not a description of what a company does well. It is a structured
proof that a specific structural advantage exists, is measurable, produces above-market
returns, and will persist for the investment horizon. The burden of proof is high —
every moat claim must survive the adversarial standard in `red-team-investment-attacks.md`.

---

## The Core Problem With Moat Claims

Most investment documents assert a moat without proving one. The most common failures:

**Narrative moats:** "Strong switching costs" stated without quantifying what switching
actually costs a customer in dollars, time, or organizational disruption.

**Feature moats:** "Best product in the market" — product advantages are not moats.
They are temporary leads that erode as competitors invest. A moat is a structural
feature of the business model, not a feature of the product.

**Scale moats without mechanism:** "Benefits from scale" stated without identifying
the specific cost category that declines non-linearly with volume.

**Network effects without feedback loops:** "Network effects" claimed for a product
where users don't interact — where adding user N+1 does not increase value for user N.

This skill exists to prevent these failures by requiring evidence at each step.

---

## Step 1: Classify the Moat Type

Before assessing strength or durability, identify the moat type. A company can have
multiple moats, but each must be assessed independently. Mixed or overlapping claims
produce weak analysis.

### The Five Moat Types

**Type 1 — Network Effects**
Definition: The value of the product to each user increases as more users join.
The feedback loop must be direct and measurable — not just "more users = more revenue."

Sub-types that matter in practice:
- *Direct network effect:* User A gets more value as User B joins (social networks,
  messaging platforms, marketplace liquidity)
- *Indirect network effect:* More users on one side attract more participants on the
  other side (two-sided marketplaces, app platforms)
- *Data network effect:* More users generate data that improves the product for all
  users (ML-based products — fraud detection, recommendation engines)

**Type 2 — Switching Costs**
Definition: A customer incurs meaningful cost — financial, operational, or psychological
— when moving from this product to a competitor.

Sub-types that matter:
- *Data lock-in:* Historical data, configurations, or integrations are non-portable
- *Process integration:* Product is embedded in operational workflows — replacement
  requires process redesign
- *Learning cost:* Significant time investment to retrain users on a competitor
- *Contractual:* Multi-year commitments with exit penalties
- *Risk cost:* Migration risk is high enough that buyers defer replacement indefinitely

**Type 3 — Scale Economies**
Definition: Unit costs decline as volume increases, creating a structural cost advantage
for the incumbent that entrants cannot replicate without first achieving scale.

Sub-types:
- *Fixed cost leverage:* High fixed cost base spread over growing volume
- *Purchasing power:* Scale-driven negotiating advantage with suppliers
- *Network density:* Geographic density reduces per-unit delivery or service cost
  (logistics, field service)

**Type 4 — Proprietary Assets (IP / Data / Brand)**
Definition: The company owns something valuable that competitors cannot replicate
regardless of how much capital they deploy.

Sub-types:
- *Patents and IP:* Legal protection that prevents direct replication
- *Proprietary data:* A dataset that cannot be recreated from scratch — it was built
  through years of transactions or user behavior
- *Regulatory licenses:* Permission to operate that is not available to new entrants
- *Brand:* Consistent price premium over generic alternatives, measured in willingness
  to pay

---

## Step 2: Establish Existence — Does the Moat Actually Exist?

For each claimed moat type, apply the existence test. A moat claim that fails the
existence test must be downgraded to a feature advantage or removed.

### Existence Test by Moat Type

**Network Effects — Existence Test:**
- Can you draw the feedback loop in one sentence? If not, the network effect is not
  established.
- Does value per user increase non-linearly with user count? Show the data.
- What happens to value when a user leaves? If the network is immune to defection,
  it is not a network effect.
- Has any competitor with fewer users demonstrated inferior outcomes on a measurable
  metric? Name the metric and the delta.

**Switching Costs — Existence Test:**
- What is the actual cost of switching, in dollars and time? Do not accept "significant"
  or "meaningful" — require a number or a named process step.
- Has any customer switched in the last 24 months? If yes, what did it cost them and
  how long did it take? That is the actual switching cost.
- Would a competitor offering a 30% price discount and free migration support cause
  a representative customer to switch? If yes, the switching cost is not structural —
  it is contractual or behavioral and will erode.
- Is the switching cost data-based (non-portable data), process-based (embedded
  workflow), or contract-based (exit penalty)? Data > process > contract for durability.

**Scale Economies — Existence Test:**
- Which specific cost line declines with volume? Name it.
- What is the cost per unit at current scale vs. at 2× scale? Show or estimate the curve.
- Has gross margin improved as revenue scaled? Flat margins despite volume growth
  suggests scale economies do not exist in this business model.
- What scale does an entrant need to reach cost parity? Is that achievable with
  available capital?

**Proprietary Assets — Existence Test:**
- For IP: Is the patent active, relevant, and broad enough to prevent workarounds?
  Name the specific claim and the infringement risk to competitors.
- For data: Can the dataset be recreated from scratch in 2–3 years by a competitor
  with sufficient capital? If yes, it is a head start, not a moat.
- For brand: Is there a measurable price premium? Name the premium and the comparison.
  "Strong brand" without a price premium is not a moat.

---

## Step 3: Measure Strength — How Wide Is the Moat?

After existence is established, rate moat strength on a 1–5 scale per dimension.

### Strength Rating Framework

| Rating | Label | Definition |
|--------|-------|------------|
| 5 | Dominant | Moat prevents meaningful competitive displacement for 5+ years under any realistic scenario |
| 4 | Strong | Moat requires sustained investment and favorable conditions to erode; displacement is costly and slow |
| 3 | Moderate | Moat provides 2–3 years of protection; a well-capitalized competitor could erode it |
| 2 | Weak | Moat provides 12–18 months of protection; a focused competitor with capital could displace |
| 1 | Nominal | Claim is directionally correct but structural advantage is insufficient to prevent displacement |

### Strength Evidence Requirements

For each moat type, specific evidence is required to support the rating:

**Network Effects Strength:**
- Churn rate differential: customers in dense networks vs. sparse networks
- Engagement metric trajectory: does engagement per user increase with network size?
- Evidence of network defensibility: did a competitor with better features fail to
  displace the incumbent because of network lock-in? Name the competitor and outcome.

**Switching Cost Strength:**
- Gross Revenue Retention (GRR): the direct measure of switching cost in aggregate.
  Below 85% GRR suggests switching costs are weak. Above 95% suggests they are strong.
- Win-back rate: do churned customers return? High win-back rates indicate switching
  costs make competitors unsatisfying even after migration.
- Average customer tenure: how long do customers stay? Normalize for company age.
- Migration failure rate: what % of customers who attempt to switch fail or return?

**Scale Economy Strength:**
- Gross margin trajectory over 3–5 years as a function of revenue
- Market share relative to nearest competitor — if scale matters, the leader should
  have structurally better margins
- Input cost advantage: what is the cost differential vs. a competitor at half the scale?

**Proprietary Asset Strength:**
- Price premium: what % above generic alternatives does the company command?
- Customer willingness to pay survey results if available; otherwise proxy with ASP trends
- Data asset freshness: is the proprietary dataset growing, stable, or decaying?

---

## Step 4: Assess Durability — Will the Moat Hold for the Investment Horizon?

A moat that exists today but will not exist at exit destroys the return thesis. This
step assesses moat durability specifically for the investment hold period (typically 4–6 years).

### Durability Framework

For each moat, identify the specific threat vector most likely to erode it during
the hold period:

**Network Effect Durability Threats:**
- *Multi-homing:* Can users participate in multiple networks simultaneously at low cost?
  If yes, the network effect is weaker than it appears — loyalty is behavioral, not structural.
- *Disruptive entrant:* Can a new entrant leapfrog the network by serving an underserved
  segment and then expanding? (Classic disruption pattern — name any analogues in this market.)
- *Platform disintermediation:* Can a platform (AWS, Salesforce, Google) replicate the
  network effect by bundling it into a larger ecosystem?

**Switching Cost Durability Threats:**
- *Migration tooling:* Is any competitor investing in migration support or data
  portability tools that would reduce the cost of switching?
- *Platform shift:* Does a major platform shift (cloud migration, AI layer, new OS)
  create a natural re-evaluation moment where switching costs reset to zero?
- *Regulatory:* Are there data portability regulations pending that would force the
  company to make switching easier?
- *Commoditization:* Is the product category commoditizing in a way that reduces
  the complexity — and thus switching cost — of the core product?

**Scale Economy Durability Threats:**
- *Technology shift:* Does a new technology (AI, cloud, automation) change the cost
  structure in a way that allows smaller players to reach cost parity without volume?
- *Vertical integration:* Can a large customer build the capability in-house at a cost
  below what the company charges?

**Proprietary Asset Durability Threats:**
- *IP:* Patent expiry, design-around risk, IPR challenges
- *Data:* New data sources that could substitute; synthetic data generation
- *Brand:* Category commoditization, new entrant with superior product at lower price

### Durability Rating

| Rating | Label | Definition |
|--------|-------|------------|
| High | Durable | Moat is structurally self-reinforcing — it compounds over the hold period |
| Medium | Stable | Moat holds for the hold period but requires active investment to maintain |
| Low | Eroding | Moat shows measurable erosion signals — monitor closely |
| Critical | At Risk | Moat is likely to be materially weaker at exit than entry |

---

## Step 5: Produce the Moat Verdict

After completing Steps 1–4, synthesize into a single moat verdict for IC use.

### Verdict Format

```
MOAT VERDICT: [Company Name]

Primary moat type: [Type 1–4]
Secondary moat (if applicable): [Type or None]

Existence: Established / Partially established / Not established
Strength: [1–5] — [Label]
Durability: High / Medium / Low / Critical

Overall verdict: [STRONG / MODERATE / WEAK / NOMINAL]

One-sentence summary:
"[Company] benefits from [specific moat type] driven by [specific mechanism],
evidenced by [specific metric], which [is / is not] self-reinforcing and
[will / is unlikely to] persist through the investment horizon."

Primary threat to moat:
[The single most likely erosion scenario, specific and named]

What would change the verdict:
[The specific observation or data point that, if true, would upgrade or
downgrade the rating by one level]
```

### Overall Verdict Calibration

**STRONG:** Moat exists (established), strength ≥4, durability High or Medium.
Returns above hurdle even in competitive scenarios.

**MODERATE:** Moat exists (established or partially), strength 3, durability Medium.
Returns adequate in base case; competitive erosion is the primary downside risk.

**WEAK:** Moat partially established or strength ≤2. Returns require above-base-rate
execution; competitive displacement is a realistic scenario in the hold period.

**NOMINAL:** Moat claim not established or durability Critical. No structural protection.
Returns depend on continued product and execution excellence — treat as a feature
advantage, not a moat.

---

## Step 6: Integration Points

### In an IC Memo (Section 5 and 6d)

The moat verdict produced in Step 5 feeds directly into:
- **Section 5** (Market & Competitive): summary competitive position with moat type
  and one-sentence verdict
- **Section 6d** (Business Quality — Competitive Moat): full Steps 1–5 analysis
  condensed to 0.5 page with the formatted moat verdict

### In a Market Research Report

The moat assessment integrates into the competitive landscape section at Level 2
(Competitor Profile Anatomy, Element 3 — Sustainable Advantage). Apply Steps 1–3
for each named competitor. Step 4 (durability) is assessed for the subject company
only, not for all competitors.

**In deep dive mode — produce the market-wide moat scorecard:**

When market-research is running in deep dive mode, competitive-moat-assessment
produces a scored matrix across all named companies in the market, not just the
subject company. This is Section 10 of the deep dive document structure.

**Moat scorecard format:**

Score each company 1–5 on each dimension. Total out of 25.
- ≥18: Structural moat — durable across the investment horizon
- 12–17: Conditional moat — depends on specific conditions holding
- <12: Transient advantage — feature lead, not structural protection

| Company | Data network | Switching cost | Platform lock-in | Scale economies | IP/Brand | Total | Verdict |
|---------|-------------|----------------|-----------------|-----------------|----------|-------|---------|
| [Name] | [1–5] | [1–5] | [1–5] | [1–5] | [1–5] | [/25] | Structural / Conditional / Transient |

**Scoring discipline:**
- Label every score [Fact], [Estimate], or [H] — most will be [Estimate]
- State the primary evidence for any score ≥4 — high scores without evidence are assertions
- Flag any company where scoring was impossible due to data scarcity (DATA GAP)
- Include a methodology note explaining the five dimensions and scoring criteria
- Reference market validation where available (e.g., Morningstar moat ratings for
  public companies provide an independent check on switching cost assessments)

### In a Red-Team Pass

After completing this assessment, load `red-team-investment-attacks.md` Section
"Attack Lens 1: Company Quality — Competitive Moat Attacks" and apply every attack
vector to the verdict produced in Step 5. A moat verdict that does not survive
adversarial review must be downgraded before it appears in an IC memo.

```
Read: /mnt/skills/user/red-team/references/red-team-investment-attacks.md
→ Section: Competitive Moat Attacks
```

---

## Claim Standards

All moat assessments are subject to writing-style claim discipline:

**Every moat claim must be labeled:** [F] fact / [E] estimate / [H] hypothesis

**Inductive chain requirement:** Any claim that the moat produces a specific outcome
(e.g., "switching costs drive NRR above 110%") must have a complete inductive chain:
outcome variable → proximate driver → gating constraint → observable condition.

**Absolute assertion prohibition:** Terms like "strong," "significant," "world-class,"
"best-in-class" applied to moat claims fail the absolute assertion test. Replace with
the specific metric, mechanism, or comparison.

**Exclusivity terms:** "Only," "solely," "exclusively" applied to competitive advantages
require that alternative mechanisms have been explicitly considered and ruled out.

```
Read: /mnt/skills/user/writing-style/SKILL.md → Steps 1–3
```

---

## Quality Gates

A moat assessment is IC-ready when all items pass:

**Existence**
- [ ] Moat type identified and named precisely (not "competitive advantages")
- [ ] Existence test applied and passed for each claimed moat type
- [ ] Any failed existence tests result in downgrade to feature advantage — not omission

**Strength**
- [ ] Strength rated 1–5 with specific evidence cited for the rating
- [ ] GRR cited for switching cost claims
- [ ] Margin trajectory cited for scale economy claims
- [ ] Price premium cited for brand/IP claims

**Durability**
- [ ] Primary durability threat named and assessed
- [ ] Hold-period specific — durability assessed for 4–6 year horizon, not indefinitely
- [ ] Regulatory and technology disruption threats explicitly addressed

**Verdict**
- [ ] One-sentence verdict states type, mechanism, evidence, and durability in one sentence
- [ ] Primary threat named
- [ ] What-would-change-the-verdict stated as a specific, observable condition
- [ ] Overall label (STRONG / MODERATE / WEAK / NOMINAL) justified by existence × strength × durability

**Claim integrity**
- [ ] All claims labeled F / E / H
- [ ] No absolute assertions (strong, significant, world-class) without specific metric
- [ ] Inductive chains complete for all causal moat claims
- [ ] Red-team moat attacks applied — verdict survives or is downgraded
