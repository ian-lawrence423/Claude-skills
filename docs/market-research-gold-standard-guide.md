# Pattern Market Research Gold Standard Guide

Use this guide when the goal is a full, standalone market research report that can
support an IC memo, board discussion, strategic investment decision, or CEO-level
market entry decision.

## Decision Standard

The best market research document is not the longest document. It is the document
that lets a senior decision-maker answer five questions with evidence:

1. What exactly is the market, and what is outside the boundary?
2. Why does the market matter now?
3. Who buys, who pays, and what workflow pain drives willingness to pay?
4. Which competitors or substitutes control the profit pool today?
5. What should Pattern, an operator, or an investor underwrite differently after reading it?

## Minimum Deliverable Contract

A full report must include all of the following:

| Requirement | Standard |
|---|---|
| Decision purpose | State the decision the report supports before analysis begins |
| Scope control | Define in-scope, out-of-scope, adjacent, and excluded markets |
| Evidence discipline | Label claims as fact, estimate, hypothesis, vendor claim, or Pattern analytic |
| Market sizing | Reconcile multiple market frames and show arithmetic |
| Buyer analysis | Segment by buying behavior, budget owner, JTBD, and switching friction |
| Competition | Include direct competitors, substitutes, and platform-native alternatives |
| Economics | Explain pricing, gross margin, retention, payback, or proxy economics |
| Technology/regulation | Separate durable forces from narrative tailwinds |
| Moat | Classify advantage durability and replicability horizon |
| Implications | Convert research into underwriting, operating, or strategic actions |

## Canonical Report Architecture

Use this structure for the most thorough standalone report:

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
12. Appendix: methodology, arithmetic checks, source labels, and open questions

Do not organize the report as raw research notes. Use the research pyramid to
investigate. Use the report architecture to communicate.

## Workflow

### 1. Define The Decision

Start with one decision statement:

> We are deciding whether [company/operator/investor] should [enter, invest,
> acquire, partner, prioritize, avoid] [market/category] over [time horizon].

Then state the working hypothesis and the two or three ways it could be wrong.

### 2. Build The Research Brief

Before collecting evidence, complete the research brief:

| Brief field | What to define |
|---|---|
| Decision | The business decision the work supports |
| Hypothesis | The current answer before research |
| Issue tree | MECE branches that would prove or disprove the hypothesis |
| Source plan | Tier 1, Tier 2, and fallback sources for each branch |
| Kill criteria | Findings that would materially change the answer |
| Output format | DOCX, PPTX, IC memo input, or research brief only |

### 3. Collect Evidence By Pyramid Level

Use the pyramid as the research operating model:

| Level | Question | Evidence to collect |
|---|---|---|
| L4 - Market | How large, fast-growing, and structurally attractive is the market? | Size, growth, segmentation, tailwinds, constraints |
| L3 - Customer | Who has the pain, who pays, and what triggers purchase? | Buyer archetypes, JTBD, procurement motion, switching costs |
| L2 - Competitive | Who wins today, who substitutes, and where is profit captured? | Competitor map, value chain, substitutes, pricing, moat |
| L1 - Position | What should the target, investor, or operator do? | Strategic implications, underwriting actions, open questions |

### 4. Build Decision Artifacts

Every major section needs at least one artifact. A section with only prose is not
done.

| Section | Required artifact |
|---|---|
| Cover | KPI strip with 4-6 framing metrics |
| Context and scope | Scope table or value-chain map |
| Executive Summary | Two-page six-section summary |
| Market Sizing | Frame comparison and source/scope tables |
| Customer Segmentation | Buyer archetype and JTBD table |
| Competitive Landscape | Competitor map and substitute workflow table |
| Pricing and Economics | Pricing archetype and economics benchmark table |
| Technology Trends | Trend signal and disruption map |
| Regulatory/Risk | Regulation/risk table with "do not over-claim" column |
| Moat | Moat scorecard with replicability horizon |
| Strategic Implications | Underwriting/action table |
| Appendix | Source labels and arithmetic checks |

### 5. Check Market Sizing Arithmetic

Market sizing fails when scope and math drift. Apply these checks:

- Separate reference markets, analytic slices, and upside scenarios.
- Do not sum overlapping markets unless overlap is removed.
- Tie every CAGR to start value, end value, and number of years.
- Label Pattern-built estimates separately from third-party market figures.
- Treat vendor or commissioned studies as directional unless independently triangulated.

Core formula:

```
CAGR = (End value / Start value) ^ (1 / Years) - 1
```

### 6. Label Evidence

Use these labels throughout the report and in the appendix:

| Label | Use for | Confidence treatment |
|---|---|---|
| Fact | Official, primary, or directly sourced evidence | Strongest support |
| Estimate | Reasoned calculation from credible inputs | Use with assumptions visible |
| Hypothesis | Plausible but not yet proven interpretation | State confirming evidence needed |
| Vendor claim | Vendor, PR, or commissioned customer claim | Directional only |
| Pattern analytic | Internal model, bridge, or scenario | Keep separate from consensus |

### 7. Write The Executive Summary Last

Use the six-section spine:

1. Company Overview
2. Product Offering
3. Market Dynamic
4. Business Model
5. Thesis: What You Need To Believe
6. Open Questions

The executive summary should not recap every section. It should state the answer,
the evidence base, the belief requirements, and the unresolved diligence agenda.

### 8. Run Quality Passes

Before producing the final DOCX, run:

1. `writing-style` for prose quality, claim tagging, and data-gap language.
2. `claim-scrutinizer` for claim integrity, source strength, and derivative math.
3. `red-team` for the strongest opposing case.
4. `pattern-docx` for the final Pattern-branded Word output.
5. `doc-quality-checker` after the file exists.

## Section Quality Gates

The report is not release-ready until these checks pass:

- Every headline is an insight, not a topic label.
- Every table has a "what this proves" interpretation.
- Every market size states scope, source type, year, and arithmetic.
- Every vendor claim is labeled as vendor or commissioned evidence.
- Every competitive claim names the competitor or substitute.
- Every moat claim states why it is structural, conditional, transient, or unproven.
- Every regulatory claim states jurisdiction, timing, scope, and implication.
- Every strategic implication changes an action, underwriting assumption, or diligence question.

## Anti-Patterns

Avoid these failure modes:

- A single TAM number with no scope reconciliation.
- A competitor list with no substitute logic.
- "Large and growing" language without growth mechanism.
- Vendor ROI claims presented as independent evidence.
- Market maps that do not explain buyer choice.
- Moat claims with no replicability horizon.
- Strategic implications that summarize rather than recommend.

## Paste-Ready Prompt

```text
Run a full standalone market research report on [market/company/category].

Decision to support: [enter/invest/acquire/partner/prioritize/avoid].
Geography: [scope].
Time horizon: [time horizon].
Output: Pattern-branded DOCX.

Use market-research in Full mode. Load mckinsey-consultant first, then complete
the research brief. Use the gold-standard report architecture: cover/KPI strip,
scope, executive summary, market sizing, customer segmentation, competitive
landscape, pricing/economics, technology trends, regulatory/risk, moat analysis,
strategic implications, and appendix. Label claims as fact, estimate, hypothesis,
vendor claim, or Pattern analytic. Show market-sizing arithmetic and include
decision-grade artifacts in every major section. Run writing-style,
claim-scrutinizer, red-team, pattern-docx, and doc-quality-checker before final
delivery.
```
