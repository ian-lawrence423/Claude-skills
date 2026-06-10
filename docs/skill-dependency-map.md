# Skill Dependency Map

Date: 2026-06-10
Branch: `main` after Work Package 1; updated on `codex/skill-dependency-contracts`

## Canonical Layer Model

| Layer | Skill(s) | Role |
|---|---|---|
| L0 Deal Orchestration | `deal-master` | Existing-work inventory, deal state assessment, phase routing, belief-register initialization |
| L1 Analytical Method | `mckinsey-consultant` | Problem framing, MECE, strategy dimensions, investment gates |
| L1b Evidence Control | `analytical-operating-system` | Evidence states, belief register, Bayesian updates, decision posture |
| L2 Research / Analysis | `market-research`, `competitive-moat-assessment`, `ntb-diligence`, `driver-tree`, `tam-sam-som-calculator`, `statistics-fundamentals`, `finance-metrics-quickref`, `gtm-metrics-analyzer`, `kpi-tree-builder` | Evidence gathering, diligence, causal analysis, metrics |
| L3 Quality | `writing-style`, `claim-scrutinizer`, `red-team`, `pre-mortem`, `boundability` | Prose review, claim testing, adversarial analysis, failure modes |
| L4 Production | `pattern-docx`, `pattern-investment-pptx`, `diligence-ddr`, `financial-model-builder`, `executive-briefing`, `executive-summary-writer`, `written-communication`, `giving-presentations` | Artifact generation and executive packaging |
| L4b QA | `doc-quality-checker`, `Deck_Check` | Final quality control |

## High-Centrality Skills

These skills have the most inbound references from other root skills and should be treated as system-critical:

| Skill | Incoming References | Interpretation |
|---|---:|---|
| `mckinsey-consultant` | 13 | Primary analytical method dependency |
| `claim-scrutinizer` | 12 | Core quality gate |
| `pattern-docx` | 12 | Core Word production dependency |
| `writing-style` | 9 | Core prose and attribution quality layer |
| `market-research` | 8 | Primary evidence-gathering workflow |
| `ntb-diligence` | 8 | Core investment diligence bridge |
| `pre-mortem` | 8 | Core adversarial investment quality pass |
| `pattern-investment-pptx` | 7 | Core deck production dependency |
| `boundability` | 6 | Core moat/NTB boundary stress test |
| `red-team` | 6 | Core adversarial review |

## Core Workflow Load Orders

### Market Research

1. `mckinsey-consultant`
2. `market-research`
3. `competitive-moat-assessment` when competitor durability matters
4. `writing-style`
5. `claim-scrutinizer`
6. `red-team`
7. `pattern-docx` or `pattern-investment-pptx`
8. `doc-quality-checker`

### Competitive Analysis / Landscape

1. `market-research`
2. `competitive-moat-assessment`
3. `competitive-landscape-deliverable` when the source is a competitive landscape sheet
4. `claim-scrutinizer` for IC-facing claims
5. `pattern-docx` / `pattern-investment-pptx` if producing a file
6. `doc-quality-checker`

### IC Memo / Investment Memo

1. `deal-master`
2. `mckinsey-consultant`
3. `analytical-operating-system`
4. `ic-memo` or `ic-memo-pipeline`
5. `market-research`
6. `ntb-diligence`
7. `driver-tree`
8. `writing-style`
9. `claim-scrutinizer`
10. `red-team`
11. `pre-mortem`
12. `boundability`
13. `pattern-docx`
14. `doc-quality-checker`

### Finance / GTM Diagnostics

1. `financial-model-builder`
2. `finance-metrics-quickref` as needed
3. `gtm-metrics-analyzer`
4. `kpi-tree-builder`
5. `driver-tree` if tying operating metrics to thesis or MOIC

## Packaging Map

| Packaging Shape | Current Examples | Risk |
|---|---|---|
| Root skill folders | All 33 root skills | Good for local source of truth, but not enough for plugin installs |
| Grouped plugin copy | `plugins/deal-intelligence/skills/*` | Must be synced from root copies before publication |
| Per-skill plugin folder | `deal-master`, `analytical-operating-system` | Dependencies may be absent when installed standalone |

## Drift Observed

| Item | Status | Action |
|---|---|---|
| `mckinsey-consultant` root vs `plugins/deal-intelligence` copy | Synced in Work Package 1 | Keep root-to-package sync before publishing grouped plugin |
| `deal-master` root vs packaged copy under `deal-master/skills` | In sync | Keep source-copy rule |
| `analytical-operating-system` root vs packaged copy under `analytical-operating-system/skills` | In sync | Keep source-copy rule |
| `deal-master` / `analytical-operating-system` root vs grouped plugin copies | Added and synced in Work Package 1 | Keep source-copy rule |
| `pattern-docx` root vs grouped plugin copy | Current root file is dirty | Resolve separately before judging package drift |

## Proposed Standard Dependency Block

Add this section to each high-priority skill. Work Package 2 has started with the core
strategy, research, memo, diligence, adversarial, and underwriting workflow stack; remaining
production-heavy skills should follow after the `pattern-docx` workflow update is handled
separately.

```markdown
## Dependency Contract

Loads before this skill:
- `[skill]` - [why]

Loads after this skill:
- `[skill]` - [handoff output]

Inputs required:
- [artifact / data / context]

Outputs produced:
- [artifact / table / decision / file]

Do not load with:
- `[skill]` when [condition]
```

## Proposed Workflow Mode Block

Add this section after the dependency contract for workflow skills:

```markdown
## Workflow Mode

| Mode | Use When | Minimum Output |
|---|---|---|
| Quick | [small request / directional answer] | [minimum useful handoff] |
| Standard | [normal reusable analysis] | [core deliverable / handoff] |
| Full | [IC-ready, board-ready, or file-producing workflow] | [full dependency chain and QA] |
```

Mode rules:
- Quick mode should not produce files unless explicitly requested.
- Standard mode should produce reusable handoff artifacts.
- Full mode should include evidence control, quality passes, and production QA when a branded file is requested.

## So What?

The system needs explicit dependency contracts. The skills already reference each other, but dependency intent is mostly buried in prose.
