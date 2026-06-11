# Gold-Standard Market Research Report Template

Use this reference for every Full-mode market research report unless Ian explicitly
asks for a lighter output or a different structure.

Source standard: `Commerce_Market_Research_v9.docx` from the Pattern research
artifact library. Treat that document as the benchmark for depth, structure,
artifact density, and Pattern DOCX presentation.

## Purpose

The gold-standard report is a decision document, not a research dump. It must let
a CEO, investor, or strategy lead understand:

1. What market is being analyzed and why it matters now
2. How the market is sized without scope or arithmetic leakage
3. Who buys, why they buy, and how buying behavior differs by segment
4. How the competitive structure works, including substitutes
5. How vendors monetize and whether the economics are attractive
6. Which technology, regulatory, and market forces change the category
7. Which companies have structural vs. transient advantages
8. What the strategic implications are for Pattern, an operator, or an investor

## Canonical Report Architecture

Use this top-level structure for Full-mode DOCX reports:

1. Cover and KPI strip
2. Context and scope definition
3. Executive Summary
4. Market Sizing
5. Customer Segmentation and Buying Behavior
6. Competitive Landscape
7. Pricing Models and Unit Economics
8. Technology Trends and Disruption Vectors
9. Regulatory Environment and External Risk
10. Competitive Moat Analysis
11. Strategic Implications and Key Takeaways
12. Appendix: arithmetic corrections, methodology, source labels

Do not organize the report as a raw L4/L3/L2/L1 pyramid. Use the pyramid to
research. Use the architecture above to communicate.

## Required Analytical Artifacts

Every major section must include at least one decision-grade artifact. A section
that contains only prose is incomplete.

| Section | Required artifact | What it must prove |
|---|---|---|
| Cover | KPI strip | The 4-6 numbers that frame the category before the reader starts |
| Context and scope | Value-chain map or scope table | What is in scope, out of scope, and adjacent |
| Executive Summary | Two-page six-section summary | Company/category, product, market, business model, thesis, open questions |
| Market Sizing | Frame comparison table and source/scope table | Which market definition is usable and which is only directional |
| Customer Segmentation | Buyer archetype table and JTBD map | Who buys, who uses, who pays, budget owner, buying motion, pain points |
| Competitive Landscape | Competitor map and substitute workflow table | Where rivalry is direct, where substitutes matter, and where white space exists |
| Pricing and Unit Economics | Pricing archetype table and benchmark table | How value is captured and whether category economics are attractive |
| Technology Trends | Quantified signal table and disruption map | What compounds, what erodes, and over what time horizon |
| Regulatory/Risk | Regulation/risk table with "do not over-claim" column | Which external forces are real, scoped, and decision-relevant |
| Moat Analysis | Moat framework and scorecard | Which advantages are structural, conditional, or transient |
| Strategic Implications | IC/operator underwriting table | What a decision-maker should actually underwrite or do differently |
| Appendix | Arithmetic corrections and source labels | How figures tie, what changed, and how evidence should be interpreted |

## Market Sizing Rules

Market sizing is where poor research most often fails. Apply these rules:

1. Separate reference markets, analytic slices, and upside scenarios.
2. Do not sum overlapping markets unless the overlap is explicitly removed.
3. Every CAGR must tie mathematically to its start year, end year, and endpoint.
4. If a figure is a Pattern internal construction, label it as such.
5. If a vendor or commissioned report supplies the figure, label the source type.
6. Use ranges when sources diverge and explain why the divergence exists.
7. Keep agentic, AI, or other emerging upside separate from the base market unless
   there is independent sizing support.

Required market sizing artifacts:
- Frame comparison table: `Frame | 2025 | Forecast | CAGR | Interpretation`
- Source/scope table: `Source / Scope | Size | Forecast | CAGR | Notes`
- Sub-segment table when relevant: `Stage | Sub-segment | Size | CAGR | Growth driver`
- Geographic table when geography changes the thesis
- Arithmetic corrections appendix if any prior number, CAGR, or total changed

## Evidence Labeling Rules

Every substantive claim must be labelable by source type:

| Label | Use for | Treatment |
|---|---|---|
| Official / primary | Filings, regulator publications, official company disclosures, government or association data | Strongest evidence; cite directly |
| Independent research | Analyst reports, industry benchmarks, reputable third-party research | Use for market structure and benchmarks; check methodology |
| Vendor / commissioned | Vendor marketing, PR, commissioned TEI studies, self-reported customer value | Directional only; do not treat as independent proof |
| Pattern analytic | Internal calculations, scenario models, bridges, estimates | Label separately; do not mix with consensus figures |
| Hypothesis | Plausible but unproven interpretation | State what evidence would confirm or reject it |

Source labels belong in the appendix and should be referenced inline where they
matter to claim strength.

## Section Standards

### Context and Scope

Must define the category boundary before sizing or competitor claims begin.

Required elements:
- Value-chain or workflow map
- In-scope stages and out-of-scope adjacencies
- Data sensitivity or system-criticality tiering when the market touches customer,
  transaction, payment, operational, or regulated data

### Market Sizing

Must show why the selected market frame is valid. It is not enough to cite one TAM.

Required elements:
- Evidence and framing guardrails before any big number
- At least two source/scope views when available
- Explanation of what is included, excluded, and overlapping
- Arithmetic integrity check for every CAGR and total

### Customer Segmentation and Buying Behavior

Must segment by buying behavior, budget, workflow need, and implementation motion,
not by generic vertical unless vertical genuinely drives the buying process.

Required elements:
- Buyer archetype table
- Budget/ACV range where available
- Buyer, user, and economic decision-maker
- Jobs-to-be-done by segment
- Switching friction and procurement pattern

### Competitive Landscape

Must include direct competitors and substitute workflows. Buyers compare outcomes,
not vendor taxonomies.

Required elements:
- Competitor tiers by segment or workflow
- Named competitors, not generic categories
- Substitute paths and platform-native threats
- Porter's Five Forces when rivalry/substitution/supplier power changes the answer
- White-space and displacement path

### Pricing Models and Unit Economics

Must explain how value turns into revenue and margin.

Required elements:
- Pricing archetypes
- Where pricing scales with customer value vs. vendor cost
- Retention, payback, gross margin, or proxy benchmarks
- Where the category is under- or over-monetized

### Technology Trends and Disruption

Must separate durable compounding advantages from features likely to erode.

Required elements:
- Quantified trend signals with source tags
- Time horizon: now, 1-2 years, 3-5 years
- Disruption map: durable layer, at-risk layer, disruptive force
- Specific implications for vendors or operators

### Regulatory Environment and External Risk

Must distinguish real regulatory scope from broad narrative tailwinds.

Required elements:
- Regulation/risk name
- Jurisdiction and effective timing
- Documented scope
- Specific implication
- "Do not over-claim" column

### Competitive Moat Analysis

Must classify advantage durability, not just describe strong competitors.

Required elements:
- Moat type definitions
- Replicability horizon
- Binding limits on each moat
- Company scorecard
- Verdict: structural, conditional, transient, or unproven

### Strategic Implications and Key Takeaways

Must answer what the analysis changes for a decision-maker.

Required elements:
- 5-7 findings maximum
- Each finding written as a conclusion
- Evidence and implication for each finding
- "What an IC/operator should underwrite" table
- Competitive positioning summary for key players when companies are named

## Quality Gates

The report is not ready until all gates pass:

- [ ] Full-mode report uses the canonical architecture or documents why not
- [ ] Every major section has at least one decision-grade artifact
- [ ] Every section headline is an insight, not a topic label
- [ ] Every table has an interpretation in prose before or after it
- [ ] Market sizing separates reference markets, analytic cuts, and upside scenarios
- [ ] Every CAGR and market total ties arithmetically
- [ ] Vendor and commissioned claims are labeled separately from independent evidence
- [ ] Pattern estimates are labeled and not blended into consensus figures
- [ ] Competitive analysis includes substitutes and platform-native threats
- [ ] Moat analysis classifies durability and replicability horizon
- [ ] Regulatory claims include scope and a "do not over-claim" guardrail
- [ ] Strategic implications state what a CEO, investor, or operator should do differently
- [ ] Appendix includes source labels and any arithmetic corrections

## Anti-Patterns

Avoid these failure modes:

- A beautiful report with no tables or decision artifacts
- A single TAM number with no scope reconciliation
- Market sizing that sums overlapping categories
- Vendor claims presented as independent evidence
- Competitor lists with no substitution logic
- "Large and growing" language without growth mechanism
- Moat claims without replicability horizon
- Regulatory tailwinds generalized beyond documented scope
- Strategic implications that summarize findings but do not change a decision
