# Phase 5 — Pass 4: Pre-Mortem Agent

Load immediately:
- `{SKILLS_PATH}/pre-mortem/SKILL.md`
- `{SKILLS_PATH}/boundability/SKILL.md`

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

**Phase B — Numeric reconciliation (Pass 4b):**
After writing failure modes, cross-check every figure:
1. Extract Base Assumptions Table from s7-financials.md
2. Verify every Failure Spectrum dollar figure reconciles to those base figures
3. Verify hold period consistent across all failure scenarios
4. Verify "Severe failure" aligns to Bear scenario in financials
5. Flag any divergence — fix before declaring this pass complete

**Phase C — Boundability verdict (Pass 4c):**
For each NTB (or major diligence item): assign a boundability classification:
- Boundable (≥25/30 on six modules)
- Partially Boundable
- Unboundable

Updates:
- `{WORK_DIR}/draft/s9-risks.md` — add failure modes with highest scores
- `{WORK_DIR}/draft/s10-recommendation.md` — add open items from unbounded NTBs

## Required Output — write to `{WORK_DIR}/iteration/pass4-pre-mortem.md`

```markdown
# Pass 4 — Pre-Mortem + Numeric Reconciliation + Boundability
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

## Boundability verdicts
| NTB | Classification | Score | Key binding action |
|-----|---------------|-------|--------------------|

## Updates applied to draft
- s9-risks.md: [N] failure modes added
- s10-recommendation.md: [N] open items added

## Status: PASS / FAIL
```
