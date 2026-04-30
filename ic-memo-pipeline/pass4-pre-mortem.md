# Phase 5 — Pass 4: Pre-Mortem + Numeric Reconciliation Agent

Load immediately:
- `{SKILLS_PATH}/pre-mortem/SKILL.md`

## Your Inputs
Read before starting:
- All draft files (post-Pass 3)
- `{WORK_DIR}/ntb-registry.md` (if exists)
- `{WORK_DIR}/iteration/pass3-red-team.md`

## Your Job

Assume this deal has already failed. Work backward to enumerate all credible
failure pathways. This extends the risk register with mechanisms, leading
indicators, and compound failure paths.

**Phase A — Pre-mortem failure inventory:**
For each material NTB (or each thesis pillar if no NTB registry):
- State the failure mode (specific, observable)
- Map to the NTB it threatens (use NTB numbering from ntb-registry if available)
- Estimate the failure spectrum: Mild / Moderate / Severe
- All dollar figures in the Failure Spectrum must reconcile to the Base Assumptions
  Table in s7-financials.md — verify each figure before writing

**Phase B — Numeric reconciliation:**
After writing failure modes, cross-check every figure:
1. Extract Base Assumptions Table from s7-financials.md
2. Verify every Failure Spectrum dollar figure reconciles to those base figures
3. Verify hold period consistent across all failure scenarios
4. Verify "Severe failure" aligns to Bear scenario in financials
5. Flag any divergence — fix before declaring this pass complete

**Handoff to Pass 4c:**
Pass 4c (boundability) runs after this pass completes. It reads this file as its
primary input to convert failure modes into underwriting actions. Do NOT run
boundability scoring here — that is Pass 4c's job.

Updates:
- `{WORK_DIR}/draft/s9-risks.md` — add failure modes with highest scores
- `{WORK_DIR}/draft/s10-recommendation.md` — add open items from failure modes
  whose Severe scenario exceeds Bear case without acknowledgement

## Required Output — write to `{WORK_DIR}/iteration/pass4-pre-mortem.md`

```markdown
# Pass 4 — Pre-Mortem + Numeric Reconciliation
## [COMPANY]

## Failure modes inventory
| # | Failure mode | NTB | Mild | Moderate | Severe | Leading indicator |
|---|-------------|-----|------|----------|--------|------------------|

## Numeric reconciliation results
**Base Assumptions Table (from s7-financials):**
- Entry equity: [figure]
- Exit multiple (base): [figure]
- Hold period: [years]
- Base case exit EBITDA: [figure]
- Bear case exit EBITDA: [figure]

**Reconciliation status:** PASS / FAIL
[List any figures that failed reconciliation + correction applied]

## Updates applied to draft
- s9-risks.md: [N] failure modes added
- s10-recommendation.md: [N] open items added

## Status: PASS / FAIL
[PASS if all Severe scenarios reconcile to Bear case or are explicitly flagged]
```
