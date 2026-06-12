# Pass 4b — Numeric Reconciliation Agent

Load immediately:
- `{SKILLS_PATH}/mckinsey-consultant/SKILL.md`
- `{SKILLS_PATH}/ic-memo/SKILL.md` -> Numeric consistency and financial section standards

## Your Inputs

```
WORK_DIR:    [working directory]
SKILLS_PATH: [path to skills]
```

Read before starting:
- `{WORK_DIR}/draft/s2-exec-summary.md`
- `{WORK_DIR}/draft/s3-overview.md`
- `{WORK_DIR}/draft/s4-thesis.md`
- `{WORK_DIR}/draft/s5-market-competitive.md`
- `{WORK_DIR}/draft/s6-business-quality.md`
- `{WORK_DIR}/draft/s7-financials.md`
- `{WORK_DIR}/draft/s8-deal-structure.md` if present
- `{WORK_DIR}/draft/s9-risks.md`
- `{WORK_DIR}/draft/s10-recommendation.md`
- `{WORK_DIR}/iteration/pass4-pre-mortem.md`
- `{WORK_DIR}/source-bibliography.md`

## Purpose

Reconcile every number, date, percentage, multiple, valuation figure, market-size
figure, source citation, and scenario assumption across the IC memo draft. This
pass is mechanical and evidence-first. Do not improve prose unless the wording
creates a numeric inconsistency.

## Required Checks

1. **Base Assumptions Table anchor**
   - Identify the authoritative Base Assumptions Table in `s7-financials.md`.
   - Extract entry equity, exit multiple, hold period, base exit EBITDA / revenue,
     bear case exit EBITDA / revenue, leverage, and target return.
   - Every scenario or MOIC reference elsewhere must reconcile to this table.

2. **Cross-section number map**
   - Build a table of every numeric claim by section.
   - Group repeated figures and flag conflicting values.
   - Include units, period, source, and whether the figure is fact, estimate, or hypothesis.

3. **Formula and arithmetic check**
   - Recalculate percentages, growth rates, multiples, contribution shares, and return bridges.
   - Show the arithmetic for each correction.
   - If inputs are missing, mark `DATA GAP` rather than inventing a value.

4. **Source consistency**
   - Confirm every fact-number has a named source in `source-bibliography.md`.
   - Mark vendor / management figures as such. Vendor or management figures cannot be
     treated as independent proof unless triangulated.

5. **Scenario consistency**
   - Base, downside, bear, severe, and pre-mortem cases must use compatible starting points.
   - If pre-mortem severe impact exceeds the memo bear case, flag the mismatch and require
     the risk section to acknowledge it.

## Output

Write to `{WORK_DIR}/iteration/pass4b-numeric-reconciliation.md`.

Required format:

```markdown
# Numeric Reconciliation

## Status
PASS 4B STATUS: CLEAR_TO_ADVANCE | BLOCKING_ISSUES_FOUND

## Base Assumptions Table Extract
| Metric | Value | Period | Source | Evidence State |
|---|---:|---|---|---|

## Cross-Section Numeric Register
| Figure | Sections Used | Values Found | Authoritative Value | Source | Action |
|---|---|---|---|---|---|

## Corrections Made
| Section | Original | Corrected | Arithmetic / Reason |
|---|---|---|---|

## Open Numeric Issues
| Issue | Why It Matters | Data Needed | Blocks IC? |
|---|---|---|---|
```

## Blocking Conditions

Do not advance if any of these remain unresolved:
- Same metric appears with conflicting values across sections.
- MOIC / IRR / valuation bridge does not reconcile to `s7-financials.md`.
- A thesis-critical number lacks source, period, or unit.
- A formulaic claim has no displayed arithmetic.
- A vendor / management-only number is used as independent proof.

