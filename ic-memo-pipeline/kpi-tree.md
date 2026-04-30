# Phase 8 — KPI Tree Agent (Post-Close Operating Architecture)

Load immediately:
- `{SKILLS_PATH}/kpi-tree-builder/SKILL.md`
- `{SKILLS_PATH}/driver-tree/SKILL.md`

## Activation

Only runs if `KPI_MODE=full`. If `KPI_MODE=skip`:
- Log: `[KPI TREE SKIPPED] KPI_MODE=skip — post-close operating architecture not produced`
- No output written

## Your Inputs
Read before starting:
- `{WORK_DIR}/intake.md`
- `{WORK_DIR}/research/driver-tree.md`
- `{WORK_DIR}/ntb-registry.md` (if exists)
- `{WORK_DIR}/draft/s7-financials.md` (Base Assumptions Table)
- `{WORK_DIR}/draft/s10-recommendation.md` (open items + underwriting actions)
- `{WORK_DIR}/iteration/pass4c-boundability.md` (boundability verdicts per NTB/node)

## Your Job

Convert the IC memo's investment thesis and NTB registry into a trackable post-close
operating architecture. This is not a summary of the IC memo — it is the operational
translation of the thesis into measurable drivers that a portfolio operations team can
track weekly and monthly after close.

**The governing logic:**
- Each load-bearing node in the driver tree becomes a KPI tree branch
- Each NTB (or driver node if no NTB registry) becomes a tracking metric cluster
- The Base Assumptions Table in s7-financials.md provides the targets
- Boundability underwriting actions from pass4c become the 100-day plan items

**Three outputs:**

### 1. KPI tree
Decompose: outcome → driver → sub-driver → atomic input

For each branch, apply kpi-tree-builder SKILL.md decomposition rules:
- Stop only when each input is directly measurable, owned by a function,
  observable at a reporting cadence, and usable in budget setting or tracking
- Do not stop at vague labels ("sales productivity", "retention") — decompose further
- Map each branch back to the corresponding NTB or driver tree node

### 2. Tracking pack
Define the reporting cadence for each metric:
- **Weekly:** leading indicators, pipeline metrics, NTB early warning signals
- **Monthly:** financial performance vs. plan, NTB status checkpoints
- **Quarterly:** IC thesis pillar progress, strategic milestones

For each metric in the weekly and monthly pack, state:
- Metric name and definition
- Target (from s7-financials Base Assumptions Table where applicable)
- Data source / owner
- Kill threshold (the value at which this metric triggers a thesis review)

Kill thresholds come from the pre-mortem failure modes in pass4-pre-mortem.md —
the leading indicators defined there map directly to the weekly tracking pack.

### 3. 100-day plan
From pass4c-boundability.md underwriting actions, convert each named action into
a concrete 100-day item:

| Day range | Action | Owner (function) | NTB/node it addresses | Success criterion |
|-----------|--------|-----------------|----------------------|-------------------|
| 0–30 | | | | |
| 31–60 | | | | |
| 61–100 | | | | |

## Required Output — write to `{WORK_DIR}/kpi-tree.md`

```markdown
# KPI Tree — Post-Close Operating Architecture
## [COMPANY]

## Governing outcome
[Investment return metric from driver-tree.md governing outcome]

## KPI tree
[COMPANY MOIC]
├── KPI Branch 1: [Driver 1 name — maps to driver tree Driver 1]
│   ├── [Sub-driver] → [atomic input: metric, owner, cadence]
│   └── [Sub-driver] → [atomic input: metric, owner, cadence]
├── KPI Branch 2: [Driver 2 name]
│   └── ...
└── KPI Branch 3: [Driver 3 name]
    └── ...

## NTB → KPI mapping
| NTB / Driver node | KPI branch | Primary metric | Kill threshold |
|-------------------|-----------|----------------|---------------|

## Tracking pack

### Weekly dashboard
| Metric | Definition | Target | Owner | Kill threshold |
|--------|-----------|--------|-------|---------------|

### Monthly review
| Metric | Definition | Target | Owner | Trigger for thesis review |
|--------|-----------|--------|-------|--------------------------|

### Quarterly IC check-in
| Thesis pillar | Milestone | Target date | Status flag |
|---------------|----------|-------------|------------|

## 100-day plan
| Day range | Action | Owner | NTB/node | Success criterion |
|-----------|--------|-------|----------|------------------|
| 0–30 | | | | |
| 31–60 | | | | |
| 61–100 | | | | |

## Status: COMPLETE
```
