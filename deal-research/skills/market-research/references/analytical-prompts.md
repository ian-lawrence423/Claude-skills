# Analytical Prompts — Market Research Reference

Structured analytical question sets for each pyramid level. Load the relevant section
when executing that pyramid level. These are research questions — they define what
evidence is required. They are not output templates.

All findings produced using these prompts must meet the claim standards in writing-style
and the source standards in market-research SKILL.md. Label every claim F / E / H.
Apply inline citation format to every figure as you go.

---

## Market Sizing & Trends
*Load for: Level 4 — Market & Segment Analysis*

### Market Sizing

**Top-down questions:**
- What is the global or regional market for this category? State the analyst source,
  base year, and methodology — not just the figure.
- What is the serviceable addressable market (SAM)? What criteria segment the TAM to SAM
  (geography, customer type, product scope)?
- What is the realistic obtainable market (SOM) given current competitive position?
  State the penetration assumption and its basis.

**Bottom-up questions:**
- How many potential buyers exist in the target segment? Source this — do not estimate
  without a named basis.
- What is the average revenue per customer (ACV or AUV)? State source and whether this
  is observed or inferred from comparable companies.
- Multiply: potential buyers × ACV = bottom-up TAM. Compare to top-down figure.
  If divergence exceeds 25%, reconcile explicitly — which assumption drives the gap?

**Growth rate questions:**
- What is the reported CAGR for this market? State the source, base year, forecast year,
  and stated methodology. A growth figure without these is not usable.
- What specific drivers are cited as producing this growth rate? List them individually.
- What macro conditions would cause growth to come in below the stated rate? This
  is a required counterpoint — do not omit.

### Structural Trends

For each trend identified, answer all four questions before including it:
1. What specific evidence establishes this as a real trend vs. a narrative?
2. What is the mechanism — why is this trend occurring?
3. What is the timing — near-term (0–1yr), mid-term (1–3yr), long-term (3–5yr)?
4. What does this trend mean specifically for the subject company or market? Generic
   "so whats" (e.g., "this creates opportunity") do not pass — be specific.

**Macro forces to assess (PESTLE):**
- Political / regulatory: policy changes, compliance requirements, enforcement trends
- Economic: macro conditions affecting buyer budgets, pricing power, cost structures
- Social / demographic: behavioral shifts, generational patterns, urbanization
- Technological: infrastructure changes, platform shifts, AI/automation impact
- Legal: IP, liability, data privacy, sector-specific regulation
- Environmental: supply chain exposure, ESG-driven purchasing behavior

**Segment map:**
- What distinct segments exist within this market?
- How is each segment sized (revenue, units, customer count)?
- Which segment is growing fastest and why?
- Which segment has the best unit economics for a new entrant?

---

## Customer Insights
*Load for: Level 3 — Customer Insights*

### Segmentation

- What are the 3–5 meaningful customer segments in this market?
- What observable criteria distinguish each segment (company size, use case, buying
  process, budget authority, technical sophistication)?
- How large is each segment as a share of the total addressable market?
- Which segment is the highest-priority entry point and why?

For each segment, build a profile using this structure:
```
Segment name:
Observable distinguishing criterion:
Problem acuity (how painful is the problem, and how is that evidenced):
JTBD: "When [situation], this customer needs to [motivation] so they can [outcome]"
Primary pain points (specific, observable, evidenced — not generic):
Decision process (who decides, who influences, what triggers search):
Willingness to pay (stated, inferred from comp, or unknown — label which):
Key barrier to purchase (categorize: awareness / switching cost / budget /
  technical / organizational):
```

### Pain Points and Needs

- What are the top 3 functional pain points per segment? Each must be specific and
  evidenced — not a category label.
- What are the emotional and social dimensions of the problem (how do customers feel
  about having this problem; what does solving it signal)?
- What workarounds do customers currently use? What does the workaround cost them
  in time, money, or risk?
- What would a customer have to give up to switch to a new solution? This is the
  switching cost — quantify where possible.

### Decision Journey

- What triggers active search for a solution?
- What information sources do buyers consult during evaluation?
- What criteria determine the shortlist?
- What criteria determine the final decision?
- Who has veto power in the buying process?
- What causes deals to stall or fail after initial interest?

---

## Competitive Landscape
*Load for: Level 2 — Competitive Landscape*

### Competitor Identification

- Who are the top 3–7 direct competitors? Rank by estimated market share, revenue,
  or customer count — whichever has the strongest evidence basis.
- Who are the indirect competitors — companies solving the same problem differently,
  or adjacent players who could enter?
- What is the competitive intensity? Apply Porter's competitive rivalry assessment:
  number of players, growth rate of the market, switching costs, differentiation,
  exit barriers.

### Competitor Profiles

For each named competitor, complete all six elements of the Competitor Profile Anatomy
defined in market-research SKILL.md. Questions that drive each element:

**Element 1 — Core product and GTM:**
What does this company actually sell and to whom? How do they acquire customers?
What is their primary sales motion (direct, channel, PLG, enterprise)?

**Element 2 — Customer base:**
What segments do they serve? How many customers? What is their ARR or revenue
if public or reported? If not available, say so explicitly.

**Element 3 — Sustainable advantage:**
What structural feature of their business makes them hard to displace?
Which of these applies: network effect / switching cost / scale economies /
proprietary IP / brand? Name the specific mechanism, not a generic descriptor.

**Element 4 — Key weakness:**
What is the most exploitable gap in their position? Look for: geographic limits,
product gaps, customer segment gaps, technical debt, pricing structure vulnerabilities,
channel conflicts, leadership/execution signals.

**Element 5 — Strategic trajectory:**
What signals indicate where they are moving? Check: last 3 product announcements,
last 3 acquisitions or partnerships, job posting patterns (what roles are they hiring),
public executive statements on strategy, analyst day materials if public.

**Element 6 — Competitive verdict:**
Given their position, what does this competitor mean for the subject company?
Are they a displacement target, a partnership candidate, a moat-builder, or
a trajectory threat?

### Positioning Map

- What are the two axes that best reveal the market's structural trade-offs?
  (Not "price vs. quality" — that's generic. Find axes specific to this market's
  actual dynamics: e.g., "breadth of integration × deployment speed" or
  "enterprise depth × SMB accessibility")
- Where does each competitor sit on those axes?
- Where is white space — positions that no incumbent occupies?
- Why hasn't the white space been filled? Is it a capability gap, a willingness gap,
  or a market timing issue?

### Porter's Five Forces — Mandatory for Every Market Analyzed

Run a full Porter's Five Forces analysis for every distinct market or stage in scope.
If the research covers multiple markets (e.g., Stage 4, 5, and 6 separately), produce
a separate Porter's analysis per market — do not aggregate into one.

**Rate each force 1–10 and produce an overall industry attractiveness score.**

| Force | Questions to answer |
|-------|-------------------|
| **Supplier power** | Who are the key suppliers (infrastructure, data, distribution)? Do they have alternatives? What leverage do they hold? |
| **Buyer power** | How much negotiating power do customers have? Is the market fragmented or concentrated on the buy side? What are switching costs from the buyer's perspective? |
| **Competitive rivalry** | How many players? How differentiated? What is the growth rate of the market (slow growth = more rivalry)? Are there exit barriers? |
| **Threat of substitution** | What substitute workflows exist? Does a buyer solve this problem without buying a dedicated product? What is the cost of the substitute? |
| **Threat of new entry** | What does it cost to enter? What incumbency advantages exist (data, network, distribution)? How long does it take a new entrant to reach competitive parity? |

**Required output for each force:**
- Rating (1–10, where 10 = maximum threat to incumbent profitability)
- 2–3 sentences of specific evidence for the rating
- Structural implication: what does this force mean for pricing power, margin sustainability, and competitive durability?

**Overall attractiveness verdict:**
- Score: [weighted average or qualitative assessment]
- One sentence: is this an attractive market to be in as an incumbent? As a new entrant?
- The single force most likely to change over the next 3–5 years and in what direction

**Do not produce generic Porter's analysis.** Every force must name specific companies,
specific data points, or specific structural features of this market. "Competitive rivalry
is high because there are many players" is not an analytical finding — name the players,
estimate their relative positions, and explain what drives rivalry in this specific context.

---

## Company Position & Strategy
*Load for: Level 1 — Company / Client Position*

### Capability Assessment

For each capability required to win in this market, assess:
```
Capability: [name]
Required to win: Yes / Table stakes / Differentiator
Current state: Exists / Partial / Absent
Path: Can build (timeline + cost) / Must acquire / Must partner
Gap severity: High (blocks go-to-market) / Medium (limits scale) / Low (affects efficiency)
```

What is the single most important capability gap to close? What is the realistic path?

### Strategic Position

- What is the company's current positioning relative to the competitive map?
- What segments are they winning today and why?
- What segments are they losing today and why?
- What is the gap between current position and the white space identified at Level 2?

### SWOT + Cross-Analysis

**Strengths:** Internal advantages that are specific and evidenced — not generic.
**Weaknesses:** Internal limitations stated honestly — not softened.
**Opportunities:** External conditions the company can exploit — tied to Level 4 trends.
**Threats:** External forces that could damage the position — tied to Level 2 competitive
  trajectory and Level 4 structural trends.

**Mandatory cross-analysis:**
- **SO (Strengths × Opportunities):** How do existing strengths enable exploitation
  of specific opportunities?
- **ST (Strengths × Threats):** How do existing strengths defend against specific threats?
- **WO (Weaknesses × Opportunities):** Which weaknesses must be closed to capture
  specific opportunities?
- **WT (Weaknesses × Threats):** Which weakness-threat combinations represent the
  highest existential risk?

### Build / Buy / Partner

For each critical capability gap:
- **Build:** What does internal development require in time, capital, and talent?
  What is the realistic timeline to competitive parity?
- **Buy:** Are there acquirable companies that close this gap? At what cost range?
  What integration risks apply?
- **Partner:** Are there partnership structures that provide access without ownership?
  What are the dependency risks?

Recommend a disposition for each gap with explicit rationale.

---

## Financial & Unit Economics
*Load for: Level 3 (customer economics) and Level 4 (market economics)*

### Unit Economics

- Customer Acquisition Cost (CAC) by channel — state source or derivation method
- Lifetime Value (LTV) — state assumptions: average contract value, retention rate,
  gross margin. Label each assumption F / E / H.
- LTV:CAC ratio and payback period — compare to sector benchmark
- Gross margin per customer/unit — compare to sector benchmark
- Contribution margin — gross margin minus variable costs per unit

For any unit economics figure that is estimated:
- State the estimation method explicitly
- State the key assumption that most affects the figure
- State what a 10% change in that assumption does to the output

### Market Economics

- What are the structural margin dynamics in this market?
  (Is value captured at the platform layer, the data layer, the service layer?)
- Where do incumbents make money vs. where do they subsidize?
- What does the margin structure imply about competitive sustainability?

---

## Risk Assessment
*Load for: Level 4 (macro/market risks) and Level 1 (execution risks)*

For each risk identified, complete this assessment:

```
Risk: [specific description — not a category]
Category: Market / Competitive / Regulatory / Operational / Financial / Reputational
Probability: 1 (unlikely) → 5 (very likely)
Magnitude: 1 (negligible) → 5 (thesis-killing)
Risk score: P × M
Early warning indicator: [specific observable signal that this risk is materializing]
Mitigation: [specific action that reduces probability or magnitude]
```

**Scenario planning — three required scenarios:**

*Base case:* Most likely outcome given current trajectory and evidence.
State the key assumptions that produce this scenario.

*Upside case:* What goes right beyond the base case. What specific conditions must hold?
Do not inflate — the upside case must be achievable, not aspirational.

*Downside case:* What goes wrong. Which risks materialize? What is the impact on the
governing thesis? State the conditions under which this scenario becomes reality.

---

## Pricing Models & Unit Economics
*Load for: deep dive mode, or when pricing transition is thesis-critical*

This section goes beyond the unit economics covered in Financial & Unit Economics.
It maps the pricing architecture of the market — how vendors charge, what billing
unit they use, and what that signals about value capture theory and competitive dynamics.

### Pricing Architecture Mapping

For each major pricing model present in the market:
- **Model name:** (flat SaaS / usage-based / per-transaction / take-rate / per-resolution / hybrid)
- **Vendors using it:** name them
- **Billing unit:** what is the atomic unit of pricing (seat, shipment, transaction, resolution, GMV %)
- **Price range:** where available — vendor-published or estimated from public sources
- **What this model signals:** which theory of value capture does this encode? (volume = more valuable → usage-based; switching cost = sticky = flat SaaS; outcome = per-resolution)

### Pricing Transition Dynamics

- Is the market migrating from one model to another? In which direction?
- What is driving the transition? (buyer pressure, competitive dynamics, AI enabling outcome-based billing)
- Who benefits from the current model? Who benefits from the emerging model?
- What does a pricing transition do to gross margins for incumbents vs. new entrants?

### Unit Economics Benchmarks

Compare the market's unit economics to SaaS sector medians. Flag where this market
outperforms or underperforms and explain the structural reason.

| Metric | SaaS median | This market | Direction | Structural reason |
|--------|-------------|-------------|-----------|-------------------|
| Gross margin | 68–72% | [estimate] | Higher / Lower / At par | |
| NRR | 105–110% | [estimate] | | |
| GRR | 88–92% | [estimate] | | |
| CAC payback | 12–18 months | [estimate] | | |

Label all estimates [Estimate] with stated methodology. Flag any metric where
no reliable public data exists as DATA GAP.

---

## Regulatory Environment
*Load for: deep dive mode, or when regulatory forces are structurally material to the thesis*

Regulation is frequently the most underpriced structural force in market research —
analyst reports rarely quantify its impact and most market sizing sources exclude it.
This section treats regulation as a value creation or destruction event, not a risk list.

### Regulatory Mapping

For each material regulation in scope:
- **Regulation name and jurisdiction**
- **Core requirement:** what does it actually mandate? (be specific — not "data privacy" but "right to erasure within 30 days")
- **Effective date or expected timeline**
- **Which vendors are affected:** and in what direction (compliance burden = moat for incumbents / barrier for new entrants / tailwind for compliance-as-a-feature vendors)
- **Market sizing implication:** does this regulation expand the TAM, compress margins, or create a new sub-segment?
- **Do not over-claim:** state what is confirmed in the regulation text vs. what is market speculation about enforcement or interpretation

### Regulatory Thesis Questions

- Which vendors are best positioned to become the compliance layer for their buyers?
- Does regulatory complexity create a moat for incumbents or an opening for purpose-built compliance vendors?
- What is the realistic enforcement timeline — and does the market's current pricing reflect the compliance cost?

---

## Technology Trends & Disruption Vectors
*Load for: deep dive mode, or when platform shift or category disruption is a primary theme*

This section separates technology trends (things happening) from disruption vectors
(things that could structurally alter competitive positions). The distinction matters:
a trend that doesn't threaten or create a moat is context, not a finding.

### Trend Identification and Quantification

For each significant technology trend:
- **Trend name**
- **Quantified signal:** a specific, cited data point that confirms this is real and not speculative (adoption rate, investment volume, production deployments, latency improvement, cost reduction)
- **Horizon:** near-term (0–1yr already underway), mid-term (1–3yr), long-term (3–5yr speculative)
- **Impact on each market stage in scope:** specific, not generic

### Disruption Vector Analysis

A disruption vector is a technology development that, if it reaches mainstream adoption,
would materially alter competitive positions — not just improve them.

For each disruption vector:
- **What is being disrupted:** the specific workflow, revenue stream, or moat that is threatened
- **The mechanism:** how does this technology route around or devalue the existing approach?
- **Who compounds vs. who erodes:** name specific companies in each category
- **The timing uncertainty:** what has to be true for this to materialize at scale? What is the gating constraint?
- **Evidence it is already happening:** cite production deployments, named customers, or measurable adoption — not roadmap announcements

### Structural Disruption Map

Produce a table:

| Capability layer | Durable (3–5yr horizon) | At risk of disruption | The disruptive force |
|-----------------|------------------------|-----------------------|---------------------|
| [Layer 1] | | | |
| [Layer 2] | | | |

Every cell must be specific — name the companies, name the technology, state the mechanism.
A disruption map with generic entries is not an analytical finding.

---

## Open Questions & Priority Diligence Areas
*Load for: all deep dive mode reports — this section is mandatory in deep dive mode*

This section is what separates a deep dive document from a summary. Its purpose is
to surface what the research does not know — the open questions, data gaps, and
diligence areas that matter most for the governing decision.

This section does three things:

### 1. What the Research Surfaced That Requires Validation

List every significant finding that is currently labeled [Estimate] or [H] and is
thesis-critical. For each:
- **The finding:** state it precisely
- **Why it matters:** what decision does it affect?
- **What would validate it:** specific data source, expert type, or primary research method
- **Priority:** High (changes the conclusion if wrong) / Medium / Low

### 2. Data That Was Unavailable

List every DATA GAP that was flagged during research. For each:
- **The gap:** what specifically could not be found
- **Where it would likely be found:** named source, named expert profile, named data provider
- **Impact if the gap is wrong:** best case / worst case for the thesis

### 3. Questions the Research Raised That It Could Not Answer

The most valuable part of a deep dive is often what it makes you realize you don't
know. List 5–10 specific questions that emerged during research that the available
evidence cannot resolve. These are not limitations — they are the diligence agenda.

Format each as a direct question, followed by why it matters:

> "Does [Company X]'s cross-retailer data network include return fraud signals, or
> only tracking and resolution data? If fraud signals are excluded, the network
> effect moat rating drops from 4 to 2 because fraud detection is where the
> data density advantage is most defensible."

Questions should be specific enough that someone knows exactly who to call or
what to request in a data room to answer them.

---

## Executive Synthesis
*Load for: Executive Summary and Strategic Implications sections*

The executive synthesis is not a summary of what the document contains. It is the
governing argument: the conclusion first, then the three strongest lines of evidence
that earn it, then the implications for the decision at hand.

**Structure:**

1. **Governing thesis** (1 sentence): What is the central finding of this research?
   This is the answer to the research question stated in the brief.

2. **Three supporting arguments** (1 paragraph each):
   Each argument is one of the themes from Phase 3. State the structural observation,
   cite the strongest evidence that supports it, and draw the implication.

3. **Strategic implications** (bullet per implication):
   What does this research mean for the specific decision stated in the brief?
   Each implication must be actionable: owner / timeline / expected outcome.

4. **Priority actions** (max 5, sequenced):
   - 0–30 days: quick wins and immediate validations
   - 30–90 days: structural moves requiring resource allocation
   - 90+ days: long-term bets contingent on earlier actions

5. **Key assumption to monitor**:
   The single assumption that, if proven wrong, most changes the strategic implications.
   State what would falsify it and what the monitoring mechanism is.
