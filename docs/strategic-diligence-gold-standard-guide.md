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
financial model assumptions. Run writing-style and claim-scrutinizer before any
formal DOCX output.
```
