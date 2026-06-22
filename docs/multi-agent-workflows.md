# Multi-Agent Workflows

This document explains how the Claude Skills repo fits together operationally. It separates three different things that were previously mixed together: skills, plugins, and pipelines.

## Executive Answer

Use `deal-master` first for all deal work. For a new deal, it routes into `new-deal-pipeline/orchestrator.md` with one research mode: `gold_standard_end_to_end`. The n8n workflows are components of that route, not separate research options.

The repo should not be cleaned by deleting anything that looks unused. First classify each folder as one of five types:

| Type | What It Means | Safe Action |
|---|---|---|
| Canonical root skill | Source skill folder with `SKILL.md` at repo root | Keep; edit here first |
| Packaged plugin copy | Skill copy under `plugins/deal-intelligence/skills/` | Keep if plugin is published; sync from root |
| Pipeline | Folder with `orchestrator.md` and agent prompts | Keep if it still maps to an active route |
| Generated artifact | `.plugin`, `.docx`, dist/package output | Regenerate or move to `dist/`; do not treat as source |
| Archive candidate | Old plugin slice or backlog file superseded by current route | Archive after install references are checked |

## Canonical Operating Order

| User Need | First Skill | Workflow | Output |
|---|---|---|---|
| "Run deal intelligence on this company" | `deal-master` | `new-deal-pipeline/orchestrator.md` | Full gold-standard chain split by information state: pre-data-room outside-in work, data-room gate, post-data-room validation, workbook/GTM/KPI/boundability, IC memo, QA |
| "Write an IC memo" | `deal-master` | `ic-memo-pipeline/orchestrator.md` only if upstream research is verified/current | 10-section IC memo, Pattern DOCX, QA |
| "Research this market" for a deal | `deal-master` | `new-deal-pipeline/orchestrator.md` | Full deal research path, not standalone/light research |
| "Research this market" outside a deal | `market-research` | `market-research-pipeline/orchestrator.md` only as non-deal/legacy route | Standalone market research report |
| "Build a model/workbook" | `financial-model-builder`, then narrow finance skill | No pipeline unless part of deal pack | Excel model or workbook |
| "Make the final Word/PPT artifact" | `writing-style`, then output skill | No pipeline unless upstream analysis is incomplete | Pattern DOCX/PPTX plus QA |

## How The Three Layers Fit

### 1. Skills

Skills are the atomic capabilities. A root folder with `SKILL.md` is the canonical authoring copy. Examples: `market-research/`, `ic-memo/`, `pattern-docx/`.

Rule: update the root skill first, then sync packaged copies.

### 2. Plugins

Plugins bundle skills for installation. The main bundled plugin is `plugins/deal-intelligence/`, which packages 25 deal-related skills. It is not the canonical authoring layer for most skills.

Rule: treat `plugins/deal-intelligence/skills/` as a distribution copy unless a skill exists only inside the plugin.

### 3. Pipelines

Pipelines sequence multiple skills and specialist prompt files. They are not skills and should not be installed as skills.

Rule: a pipeline is an operator workflow, not a source skill.

## Pipeline Decision Tree

```text
Is this deal-related?
  No -> invoke the most specific root skill.
  Yes -> deal-master -> create shared/process-tracker.md -> new-deal-pipeline/orchestrator.md
         with RESEARCH_MODE=gold_standard_end_to_end.
         Only use ic-memo-pipeline when verified/current upstream research already exists.
         Do not use standalone market-research-pipeline as a deal shortcut.
```

## Workflow Map

| Pipeline | Status | Role | Keep / Archive Decision |
|---|---|---|---|
| `new-deal-pipeline/` | Primary | Full deal-pack workflow. Creates one evidence spine, splits pre-data-room outside-in work from post-data-room validation, and gates workbook/GTM/KPI/boundability/IC memo on data-room evidence. | Keep as the only deal research route |
| `ic-memo-pipeline/` | Specialized | IC memo workflow when the memo is the main output and upstream research is already scoped. | Keep, but document as memo-only |
| `market-research-pipeline/` | Legacy / repair | Standalone market research report workflow. | Keep for non-deal research or failed-component repair; do not present as a deal research mode |
| Standalone research phase slice | Removed | Superseded by `plugins/deal-intelligence/` and root canonical skills. | Use `deal-intelligence` grouped plugin |
| Standalone diligence phase slice | Removed | Superseded by `plugins/deal-intelligence/` and root canonical skills. | Use `deal-intelligence` grouped plugin |
| Standalone output phase slice | Removed | Superseded by `plugins/deal-intelligence/` and root canonical skills. | Use `deal-intelligence` grouped plugin |

## Delete / Archive Recommendations

Confirmed-unused standalone slices have been removed after marketplace and workflow references
were redirected to `plugins/deal-intelligence/`. Current cleanup state:

| Candidate | Why It Looks Stale | Recommended Action |
|---|---|---|
| Standalone research phase slice | Superseded by packaged `deal-intelligence` bundle and unused by Ian | Removed |
| Standalone diligence phase slice | Superseded by packaged `deal-intelligence` bundle and unused by Ian | Removed |
| Standalone output phase slice | Superseded by packaged `deal-intelligence` bundle and unused by Ian | Removed |
| `analytical-operating-system.plugin` | Generated package artifact, not source | Move to `dist/` or regenerate on demand |
| `plugins/deal-intelligence.plugin` | Generated package artifact, not source | Move to `dist/` or regenerate on demand |
| `market-research-pipeline/remaining-agents.md` | Explicitly retained as historical source material in `market-research-pipeline/CLAUDE.md`; agents should not dispatch from it | Keep or move to `archive/notes/` only after updating `CLAUDE.md` |

## Resolved Source-Of-Truth Mismatch

`deal-workbook-builder` is now promoted to a root canonical skill and remains synced
into `plugins/deal-intelligence/skills/`. Root `driver-tree`, root `boundability`, and
the docs generator can reference it without relying on a plugin-only source.

## Quality Gates

| Gate | Required Before Moving On |
|---|---|
| Process tracker gate | `shared/process-tracker.md` exists, names every workflow/skill/doc, and has phase statuses plus next action |
| Intake gate | Company, deal context, output target, current evidence, and open questions are known |
| Evidence gate | Claims are tagged fact / estimate / hypothesis and unsupported claims are marked `GAP` |
| Arithmetic gate | Model, market sizing, and bridge math tie out or exceptions are explicit |
| Draft gate | `writing-style` runs before final document production |
| Adversarial gate | `claim-scrutinizer`, `red-team`, and `pre-mortem` run for IC-facing work |
| File gate | `pattern-docx` or `pattern-investment-pptx` produces the file, then `doc-quality-checker` runs |

## So What?

The order is: canonical skill first, process tracker second, deal plugin/workflow execution third. Use pipelines to orchestrate work, not as source files. Archive old standalone plugin slices only after confirming nothing installs or invokes them.
