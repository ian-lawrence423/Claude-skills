# Phase 5 — Pass 4c: Boundability Agent

Load immediately:
- `{SKILLS_PATH}/boundability/SKILL.md`

## Your Inputs
Read before starting:
- `{WORK_DIR}/research/driver-tree.md`
- `{WORK_DIR}/ntb-registry.md` (if exists)
- `{WORK_DIR}/iteration/pass4-pre-mortem.md`
- `{WORK_DIR}/draft/s7-financials.md`
- `{WORK_DIR}/draft/s9-risks.md`
- `{WORK_DIR}/draft/s10-recommendation.md`

## Your Job

Convert the pre-mortem failure modes and driver tree load-bearing nodes into
specific underwriting actions. The unit of assessment is the NTB (if
ntb-registry.md exists) or the load-bearing driver node (from driver-tree.md).

**Six assessment modules per NTB / load-bearing node:**
1. Perimeter — is the risk well-defined and bounded?
2. Timing — can the risk be resolved before the investment decision?
3. Data Quality — is the evidence tier sufficient to assess it?
4. Outcome Range — how wide is the range of plausible outcomes?
5. Precedent / Observability — have comparable companies navigated this?
6. Mitigants — do specific deal terms, price, or operational actions reduce exposure?

**Scoring:**
- Each module: 0–5
- Total: 0–30
- Boundable ≥25 | Partially Boundable 15–24 | Unboundable <15

**Verdict terminology must match pre-mortem:**
An NTB classified Boundable here must have scored ≥25. If pre-mortem and
boundability disagree on classification for the same item, resolve before writing
the output — do not carry contradictions into the final document.

**Deal type adjustment:**
- PE buyout / acquisition: all five underwriting buckets active
  (model | price | leverage | docs | operations)
- Public equity long: Leverage and Docs collapse;
  Price → "entry discipline"; Operations → "monitoring cadence"

**Updates to draft files:**
- `s10-recommendation.md`: add boundability verdicts per NTB/node as a
  summary table; Unboundable items must appear in open items with named action
- `open-issues.md`: append any Unboundable items not already listed

## Required Output — write to `{WORK_DIR}/iteration/pass4c-boundability.md`

```markdown
# Pass 4c — Boundability
## [COMPANY]

## Boundability verdicts

| NTB / Node | P | T | D | O | Pr | M | Total | Classification |
|------------|---|---|---|---|----|---|-------|----------------|
| [NTB-1 name] | /5 | /5 | /5 | /5 | /5 | /5 | /30 | Boundable / Partial / Unboundable |

## Underwriting actions per NTB / node

### [NTB-1 name] — [Classification]
**Model:** [specific model adjustment, or N/A]
**Price:** [entry price discipline or entry multiple sensitivity]
**Leverage:** [leverage covenant or structure adjustment, or N/A for public equity]
**Docs:** [rep, warranty, earnout, or other doc protection, or N/A]
**Operations:** [100-day plan item or monitoring KPI]

[Repeat for each NTB / load-bearing node]

## Pre-mortem / boundability alignment check
[Flag any disagreements between pass4 classifications and pass4c verdicts — resolved before delivery]

## Updates applied
- s10-recommendation.md: boundability summary table added
- open-issues.md: [N] Unboundable items appended

## Status: PASS / FAIL
[PASS if all Unboundable items are in open-issues with named actions]
```
