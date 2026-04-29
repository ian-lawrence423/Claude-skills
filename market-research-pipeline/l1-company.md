# L1 — Company / Client Position Agent

Load immediately:
- `{SKILLS_PATH}/market-research/SKILL.md`  → Section: Level 1
- `{SKILLS_PATH}/mckinsey-consultant/SKILL.md` → Section: SWOT + Cross-Analysis

## Your Inputs
```
BRIEF:      {WORK_DIR}/brief.md
L4_OUTPUT:  {WORK_DIR}/research/l4-market.md
L3_OUTPUT:  {WORK_DIR}/research/l3-customer.md
L2_OUTPUT:  {WORK_DIR}/research/l2-competitive.md
```

## Depth Requirements

- Capability assessment: three-state taxonomy only — exists / can build / must acquire
- SWOT cross-analysis is mandatory. A SWOT without SO/ST/WO/WT is incomplete.
- Every gap requires a stated build/buy/partner disposition with rationale.
- Gap analysis must cross-reference the competitive landscape from L2.

## Output — write to `{WORK_DIR}/research/l1-company.md`

```markdown
# L1 — Company Position — [COMPANY]

## Current strategy and business model
[Specific, evidenced — not boilerplate]

## Capability assessment
[Table: capability / state (exists/can build/must acquire) / evidence / gap severity]

## SWOT
[Strengths / Weaknesses / Opportunities / Threats]

## Cross-analysis (mandatory)
- SO (exploit): [how strengths capture opportunities]
- ST (defend): [how strengths counter threats]
- WO (develop): [how to address weaknesses to capture opportunities]
- WT (avoid): [how to minimize exposure where weak + threatened]

## Build / buy / partner disposition
[For each critical gap: recommended path + rationale + evidence]
```
