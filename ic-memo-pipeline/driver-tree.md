# Phase 3b — Driver Tree Agent

Load immediately:
- `{SKILLS_PATH}/driver-tree/SKILL.md`
- `{SKILLS_PATH}/mckinsey-consultant/SKILL.md`

## Your Inputs
Read before starting:
- `{WORK_DIR}/intake.md`
- `{WORK_DIR}/ntb-registry.md` (if exists)
- `{WORK_DIR}/research/l4-market.md`
- `{WORK_DIR}/research/l3-customer.md`
- `{WORK_DIR}/research/l2-competitive.md`
- `{WORK_DIR}/research/moat-assessment.md`

## Your Job

Decompose the investment thesis into a MECE driver tree. This tree becomes the
structural backbone for Section 4 (Investment Thesis) and determines which
assumptions carry the most MOIC weight — informing both drafting and the
boundability verdicts in Pass 4c.

Run all 9 steps from driver-tree SKILL.md:
1. Construct the MECE driver tree (outcome → drivers → sub-drivers → atomic inputs)
2. Variance amplification — which nodes drive the most variance in the outcome?
3. Evidence tier assignment (T1–T4) per node
4. Gating — which nodes are necessary vs. sufficient?
5. Base-rate overlay — how often do companies achieve the claimed driver level?
6. Vintage discipline — does the evidence come from comparable vintages?
7. Segment tables — break top drivers by customer segment where relevant
8. Cascade scenarios — what happens to the outcome if the top 2 drivers fail?
9. Self-audit — check MECE, no circular logic, no double-counting

**If ntb-registry.md exists:** Map each NTB to a specific node in the driver
tree. NTBs should correspond to gating nodes (necessary conditions), not
sufficient conditions. Flag any NTB that doesn't map to a gating node —
it may not belong in the thesis pillar structure.

**Output feeds:**
- Section 4 (draft-sections.md SECTION_INDEX=4) — governs pillar construction
- Pass 4c (boundability) — load-bearing nodes become the boundability units

## Required Output — write to `{WORK_DIR}/research/driver-tree.md`

```markdown
# Driver Tree — [COMPANY]

## Governing outcome
[Investment return metric — e.g., 3× MOIC in 5 years]

## Driver tree
[COMPANY MOIC]
├── Driver 1: [name]
│   ├── Sub-driver 1a: [name] [T1/T2/T3/T4] [evidence]
│   └── Sub-driver 1b: [name] [T1/T2/T3/T4] [evidence]
├── Driver 2: [name]
│   ├── Sub-driver 2a: [name]
│   └── Sub-driver 2b: [name]
└── Driver 3: [name]

## Variance amplification
| Node | Variance contribution | Evidence tier | Gating? |
|------|----------------------|---------------|---------|

## Load-bearing nodes (top 3)
[Nodes whose failure alone materially impairs the investment case]

## NTB → driver tree mapping
| NTB | Mapped node | Gating? | Mismatch flag |
|-----|------------|---------|---------------|

## Cascade scenarios
**If Driver 1 fails:** [outcome impact]
**If Driver 1 + Driver 2 fail:** [outcome impact — must reconcile to s7 Bear case]

## Self-audit
- [ ] Tree is MECE — no overlap, no gaps
- [ ] No node is circular (outcome variable doesn't appear as its own driver)
- [ ] No double-counting between drivers
- [ ] All gating nodes have T1 or T2 evidence or are explicitly flagged as gaps
```
