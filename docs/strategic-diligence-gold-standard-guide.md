# Pattern Strategic Diligence Gold Standard Guide

Use this guide when the goal is a standalone diligence package before a full IC
memo, or when the deal team needs the most thorough Need-to-Believe, risk, and
underwriting agenda.

## Decision Standard

Strategic diligence should answer:

> What must be true for this opportunity to work, what evidence do we have, what
> evidence is missing, and what finding would make us stop?

It is not a risk list. It is an evidence operating system for the deal.

## Minimum Deliverable Contract

| Requirement | Standard |
|---|---|
| Thesis | One-sentence investment or strategic hypothesis |
| NTB registry | 4-7 load-bearing beliefs with evidence state |
| Evidence states | Confirmed / supported / mixed / weak / missing |
| Diligence plan | Data requests and owners tied to each NTB |
| Stress tests | What breaks each NTB and what signal would show it |
| Kill triggers | Specific findings that change posture to pass or reprice |
| Correlation | Which NTBs fail together and create compound downside |
| Handoff | Mapping to IC memo sections and financial model assumptions |

## Canonical Diligence Architecture

1. Decision Context
2. Thesis and Investment Logic
3. Need-to-Believe Register
4. Evidence State Assessment
5. Diligence Plan and Data Requests
6. Stress Tests and Kill Triggers
7. Cross-NTB Correlation and Compound Risk
8. Financial Model / Underwriting Handoff
9. IC Memo Handoff
10. Open Questions and Next Actions

## Strategic Analysis Evidence Modules

When a diligence package includes market, competitive, pricing, product, or business-model
analysis, add the modules below before the IC memo handoff. The reference standard is
`Pattern_PAYG_Token_Pricing_Analysis_5.docx`.

| Module | What it answers | Required artifact | Handoff |
|---|---|---|---|
| Benchmark comparables | What market norms constrain the thesis? | Benchmark table with source type, price/term/model, implication | NTB evidence and model assumptions |
| Rule / policy constraints | What accounting, legal, regulatory, or platform rule changes the design? | Rule table with documented scope, interpretation, design implication | Risk section and open diligence |
| Design implications | What should be built, priced, monitored, or governed differently? | Numbered implication list with owner/action | Operating plan and IC recommendation |
| Pre-mortem | How does the strategy fail? | Failure mode registry and compound failure paths | Risk section and kill triggers |
| Boundability | Which risks are known, gettable, or structurally unknowable? | Boundability table: issue, what we know, what would sharpen it | Diligence plan and underwriting treatment |
| Bottom-up TAM / ICP build | Is the actionable buyer population large enough? | Assumption-driven buyer and spend model | Market NTB and revenue model |
| Moat / competitive durability | Which advantage persists and which decays? | Moat scorecard with replicability horizon and erosion vector | Competitive position and exit rationale |
| JTBD / willingness-to-pay | Why would buyers adopt and what can they pay? | Segment table with JTBD, pain, alternative cost, WTP signal | Pricing and revenue assumptions |
| Technology disruption | What could compress price, quality advantage, or supplier cost? | Disruption map with quantified signal and response | Downside case and monitoring plan |
| Unit economics | Does the model work at realistic adoption levels? | Scenario table with cost lines, breakeven, and contribution | Financial model handoff |

Every module must map to at least one NTB, failure mode, model assumption, or open
diligence item. If it maps to none, remove it from the package.

## Workflow

### 1. State The Thesis

Use a one-sentence hypothesis:

> This investment works if [asset quality] plus [market/sector timing] plus
> [value creation path] produce [return outcome] at [entry valuation].

### 2. Derive NTBs

Each NTB must be load-bearing and falsifiable.

| NTB | Why it matters | Evidence state | Current support | Data required | Kill trigger |
|---|---|---|---|---|---|

Evidence state definitions:

| State | Meaning |
|---|---|
| Confirmed | Direct evidence supports the belief |
| Supported | Multiple sources support, but not fully proven |
| Mixed | Evidence conflicts or depends on segment/time period |
| Weak | Mostly narrative, vendor, or management assertion |
| Missing | No evidence yet |

### 3. Build The Diligence Plan

Every data request must tie to a decision.

| Data request | NTB tested | Source owner | Format needed | Decision impact | Priority |
|---|---|---|---|---|---|

### 4. Stress Test The Thesis

For each NTB:

- What would make this belief false?
- What early signal would show deterioration?
- What financial model line item changes?
- What mitigation exists?
- Is the mitigation operationally credible?

### 5. Map To Underwriting

Turn qualitative diligence into model assumptions:

| Diligence finding | Model assumption affected | Base case | Downside case | Kill trigger |
|---|---|---|---|---|

### 6. Handoff To IC Memo

| Diligence output | IC memo section |
|---|---|
| NTB registry | Investment Thesis |
| Evidence state table | Executive Summary and Open Questions |
| Diligence plan | Open Diligence Items |
| Stress tests | Risks and Mitigants |
| Kill triggers | Recommendation / Decision Posture |
| Model handoff | Returns and Scenario Analysis |

## Quality Gates

- NTBs are not generic risks.
- Each NTB has a named evidence state.
- Each data request has decision impact.
- Kill triggers are specific and measurable.
- Stress tests include financial implications.
- Compound risks are identified, not treated independently.
- Handoff to IC memo and financial model is explicit.

## Anti-Patterns

- Turning the diligence plan into a data-room checklist.
- Treating all risks as equally important.
- Writing NTBs that cannot be disproven.
- Failing to connect diligence findings to model assumptions.
- Using management narrative as confirmed evidence.
- Missing cross-NTB correlation.

## Paste-Ready Prompt

```text
Create a full strategic diligence package for [Company].

Decision context: [screen / pre-LOI / IC prep].
Working thesis: [one sentence].
Known materials: [files/folder].
Output: [markdown or Pattern DOCX].

Use ntb-diligence in Full mode with mckinsey-consultant and
analytical-operating-system loaded. Build a 4-7 item NTB registry, assign
evidence states, create a diligence plan, stress-test every NTB, define kill
triggers, map compound risks, and hand off findings to IC memo sections and
financial model assumptions. When the thesis depends on market, competitive,
pricing, product-economics, regulatory, moat, or technology assumptions, add the
relevant strategic analysis evidence modules and map each module to an NTB, model
assumption, failure mode, or open diligence item. Run writing-style and
claim-scrutinizer before any formal DOCX output.
```
