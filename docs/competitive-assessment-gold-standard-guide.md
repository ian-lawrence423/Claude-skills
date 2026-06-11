# Pattern Competitive Assessment Gold Standard Guide

Use this guide when the goal is a board-ready competitive assessment, moat
review, competitor deep dive, or market-positioning analysis.

## Decision Standard

A strong competitive assessment answers one question:

> What position can this company defend, against whom, for how long, and why?

The deliverable must distinguish current advantage from durable moat. Product
lead, better execution, and brand momentum can matter, but they are not moats
unless they create measurable resistance to displacement.

## Minimum Deliverable Contract

| Requirement | Standard |
|---|---|
| Category boundary | Define direct competitors, substitutes, and adjacent platforms |
| Customer choice | Explain how buyers choose and what triggers switching |
| Competitor map | Segment competitors by workflow, buyer, price, and strategic position |
| Moat proof | Classify moat type and prove existence with evidence |
| Durability | State replicability horizon and erosion vectors |
| Displacement path | Explain how a challenger could win share |
| Verdict | STRONG / MODERATE / WEAK / NOMINAL / UNPROVEN with rationale |
| Implication | State what the company or investor should do differently |

## Canonical Assessment Architecture

1. Executive Verdict
2. Category Boundary and Competitive Arena
3. Customer Choice and Buying Criteria
4. Competitor Landscape and Segmentation
5. Substitute Workflows and Platform Threats
6. Moat Type Classification
7. Moat Evidence and Strength Score
8. Durability, Erosion Risk, and Replicability Horizon
9. Displacement Paths and Strategic Response
10. Implications for Investment, Product, GTM, or M&A
11. Appendix: competitor profiles, evidence labels, source notes

## Moat Types

Assess each moat independently. Do not blend claims.

| Moat type | What must be proven |
|---|---|
| Network effects | Value per user rises as more users or counterparties join |
| Switching costs | Customer faces measurable time, cost, risk, or disruption to leave |
| Scale economies | Specific cost line declines structurally with volume or density |
| Proprietary assets | Data, IP, licenses, brand, or relationships cannot be replicated quickly |
| Efficient scale | Market is too small or local for rational duplicate infrastructure |

## Workflow

### 1. Define The Arena

Do not start with a competitor list. Start with the job being solved and the
buyer’s alternatives.

| Boundary | Questions |
|---|---|
| Direct competitors | Who sells the same workflow to the same buyer? |
| Substitutes | What manual, internal, bundled, or platform-native workflow solves the same job? |
| Adjacent platforms | Which larger systems could absorb the workflow? |
| Non-consumption | When does the customer choose to do nothing? |

### 2. Map Customer Choice

The assessment must explain buying behavior:

- Buyer, user, economic decision-maker, and blocker.
- Trigger event that creates urgency.
- Switching threshold and migration risk.
- Price/value metric.
- Procurement path and implementation burden.

### 3. Build The Competitive Map

Required table:

| Competitor | Segment | Buyer | Core workflow | Pricing model | Advantage | Weakness | Threat level |
|---|---|---|---|---|---|---|---|

Use named companies. Avoid generic categories unless the market is too early to
name clear players.

### 4. Prove Or Disprove The Moat

For every claimed moat, ask:

1. What is the mechanism?
2. What evidence proves the mechanism exists?
3. What metric shows the mechanism creates economic advantage?
4. What would a competitor need to replicate it?
5. How long would replication take?
6. What could erode it?

Required moat table:

| Moat claim | Type | Evidence | Strength 1-5 | Replicability horizon | Erosion vector | Verdict |
|---|---|---|---|---|---|---|

### 5. Test Durability

Durability must match the investment or strategy horizon.

| Horizon | Question |
|---|---|
| 0-12 months | Is the advantage real today? |
| 1-3 years | Can a well-funded competitor copy or route around it? |
| 3-5 years | Does the advantage compound or decay? |
| Exit horizon | Will the buyer universe still value the moat? |

### 6. Identify Displacement Paths

Every moat assessment needs the bear case:

- Low-end disruption.
- Enterprise bundle.
- Platform-native feature absorption.
- Better pricing model.
- Data portability or integration standard.
- Regulatory change.
- Channel shift.

## Quality Gates

- The assessment names competitors and substitutes.
- Every moat claim has a mechanism and metric.
- Switching costs are quantified in dollars, time, workflow risk, or contract friction.
- Network effects include a feedback loop, not just user growth.
- Scale claims name the cost line that improves with scale.
- Proprietary data claims explain whether a competitor could recreate the dataset.
- Verdict states durability and erosion vector.
- Strategic implication is action-oriented.

## Anti-Patterns

- Calling product quality a moat without structural evidence.
- Listing competitors without explaining buyer choice.
- Ignoring substitutes because they are not vendors.
- Claiming network effects where users do not create value for each other.
- Treating current lead as durable advantage.
- Giving a moat verdict without a replicability horizon.

## Paste-Ready Prompt

```text
Create a full competitive assessment for [company/category].

Decision to support: [investment / M&A / product strategy / market entry].
Geography: [scope].
Time horizon: [time horizon].
Known competitors: [list if available].

Use market-research for competitor evidence and competitive-moat-assessment for
the moat proof. Include direct competitors, substitutes, platform threats,
customer buying criteria, competitor map, moat type classification, evidence
scorecard, durability and erosion risk, displacement paths, and strategic
implications. Label facts, estimates, hypotheses, vendor claims, and gaps. Run
writing-style and claim-scrutinizer before final DOCX output.
```
