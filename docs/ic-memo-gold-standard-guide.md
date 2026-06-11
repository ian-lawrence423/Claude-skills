# Pattern IC Memo Gold Standard Guide

Use this guide when the goal is a full Investment Committee memo for a PE
buyout, acquisition, minority investment, or strategic investment.

## Decision Standard

A great IC memo does not describe a deal. It forces a decision. It must tell the
committee whether to proceed, reprice, resolve first, or pass, and it must make
the case in a way that survives hostile questions.

The memo must answer three gates:

1. Why is this a good company?
2. Why is this a good sector to invest in today?
3. Why is this a good investment at this price and structure?

If any gate cannot be answered with evidence, the memo should say so explicitly.

## Minimum Deliverable Contract

| Requirement | Standard |
|---|---|
| Recommendation | Clear PROCEED / REPRICE / RESOLVE FIRST / PASS posture |
| Gate structure | Company quality, sector timing, investment attractiveness |
| NTBs | 4-7 load-bearing Need-to-Believe statements tied to evidence |
| Returns | IRR/MOIC bridge split into EBITDA growth, margin, multiple, leverage/cash |
| Evidence | Claims tagged as fact, estimate, hypothesis, or gap |
| Risks | Specific risks with leading indicators, mitigants, and kill criteria |
| Open items | Diligence agenda tied to decision impact |
| Executive summary | Two-page summary written last, not first |

## Canonical 10-Section Memo

1. Investment Recommendation
2. Executive Summary
3. Company Overview
4. Investment Thesis / Need-to-Believe Register
5. Market and Sector Timing
6. Customer, Product, and Competitive Position
7. Financial Profile and Value Creation Plan
8. Valuation, Returns, and Scenario Analysis
9. Risks, Mitigants, and Failure Modes
10. Open Diligence Items and IC Decision

## Workflow

### 1. Define The IC Decision

Start with one sentence:

> We recommend [PROCEED / REPRICE / RESOLVE FIRST / PASS] because [primary
> reason], subject to [one or two gating diligence items].

Then state what would change the recommendation.

### 2. Build The Evidence Base

Before drafting, assemble:

| Evidence area | Minimum input |
|---|---|
| Company | Business description, scale, ownership, management, historical performance |
| Market | Size, growth, cycle timing, tailwinds/headwinds, competitive structure |
| Customer | Segments, buying criteria, retention, concentration, pain, willingness to pay |
| Product | Offering, workflow role, differentiation, implementation, switching friction |
| Financial | Revenue, gross margin, EBITDA, cash flow, model, working capital, capex |
| Deal | Entry valuation, structure, leverage, hold period, exit assumptions |
| Diligence | NTBs, open questions, management claims, third-party evidence |

### 3. Derive The NTB Register

Every thesis should compress into 4-7 Need-to-Believe statements. Each NTB must
be:

- Load-bearing: if false, the recommendation changes.
- Testable: evidence can confirm or reject it.
- Economic: tied to revenue, margin, multiple, risk, or strategic value.
- Owned: tied to a diligence owner or required source.

Required NTB table:

| NTB | Current evidence | Evidence state | Decision impact | Confirming data | Kill trigger |
|---|---|---|---|---|---|

### 4. Write The Investment Thesis

The thesis should not be a list of positives. It should be the belief chain that
connects asset quality to returns.

Use this form:

> We should invest because [company quality] is positioned to benefit from
> [sector timing], and at [entry valuation] we can generate [return path] if
> [NTBs] prove true.

### 5. Build The Returns Bridge

Separate value creation into explicit components:

| Return component | Question |
|---|---|
| EBITDA growth | What revenue and margin drivers create earnings growth? |
| Margin improvement | What operational levers expand EBITDA margin? |
| Multiple expansion/contraction | What exit multiple is justified and why? |
| Leverage paydown / cash generation | How much value comes from deleveraging or cash flow? |

Do not use one blended upside case. The committee needs to see what drives value.

### 6. Build Scenarios

Create base, upside, and downside cases with coherent narratives, not arbitrary
haircuts.

| Scenario | Narrative | Revenue | Margin | Exit multiple | MOIC/IRR | Why it happens |
|---|---|---|---|---|---|---|

The downside case should be the strongest case not to do the deal.

### 7. Run The Quality Stack

Before final DOCX production:

1. Run `writing-style` on the full draft.
2. Run `claim-scrutinizer` on every material claim.
3. Run `red-team` to build the bear case.
4. Run `pre-mortem` to identify failure pathways.
5. Run `boundability` on load-bearing moat or NTB claims.
6. Produce via `pattern-docx`.
7. Run `doc-quality-checker`.

## Section Quality Gates

- Recommendation appears before supporting detail.
- Each gate has evidence, not narrative assertion.
- Every NTB has a decision impact and kill trigger.
- Market section explains why now, not just why the market is attractive.
- Competitive section includes substitutes and displacement path.
- Financial section ties operating drivers to returns.
- Risk section includes leading indicators, not generic mitigants.
- Open questions are decision-relevant, not a diligence laundry list.
- Executive summary is written last using the six-section summary spine.

## Anti-Patterns

- Starting with document production before claim hardening.
- Writing a CIM summary instead of an investor recommendation.
- Making every diligence question an NTB.
- Treating downside as a softer base case.
- Hiding kill criteria in generic risk language.
- Using market research as narrative support without underwriting implications.

## Paste-Ready Prompt

```text
Write the full Pattern IC memo for [Company].

Decision context: [first look / pre-LOI / final IC].
Deal type: [buyout / acquisition / minority / strategic investment].
Entry valuation and structure: [details].
Hold period: [years].
Working thesis: [one sentence].
Materials: [folder/files].

Use the full IC memo workflow. Load mckinsey-consultant and the investment
evaluation framework first, then analytical-operating-system. Build the evidence
base, derive 4-7 NTBs, use the 10-section memo architecture, include Gate 1/2/3
logic, returns bridge, scenario analysis, risks, kill criteria, and open
diligence items. Write the executive summary last. Run writing-style,
claim-scrutinizer, red-team, pre-mortem, boundability where relevant,
pattern-docx, and doc-quality-checker before delivery.
```
