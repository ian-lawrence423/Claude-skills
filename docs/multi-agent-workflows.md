# Multi-Agent Workflows

This document explains how the Claude Skills repo fits together operationally. It separates three different things that were previously mixed together: skills, plugins, and pipelines.

## Executive Answer

Use `deal-master` first for deal work. It should route into `new-deal-pipeline/orchestrator.md` for a full deal pack, `ic-memo-pipeline/orchestrator.md` for an IC memo-only process, or `market-research-pipeline/orchestrator.md` for standalone market research.

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
| "Run deal intelligence on this company" | `deal-master` | `new-deal-pipeline/orchestrator.md` | Market research, competitive assessment, IC memo, QA |
| "Write an IC memo" | `deal-master` or `ic-memo` | `ic-memo-pipeline/orchestrator.md` | 10-section IC memo, Pattern DOCX, QA |
| "Research this market" | `market-research` | `market-research-pipeline/orchestrator.md` | Standalone market research report |
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
  Yes -> Is the required output a full deal pack?
    Yes -> deal-master -> create shared/process-tracker.md -> new-deal-pipeline/orchestrator.md
    No -> Is the required output only an IC memo?
      Yes -> deal-master or ic-memo -> ic-memo-pipeline/orchestrator.md
      No -> Is the required output only market research?
        Yes -> market-research -> market-research-pipeline/orchestrator.md
        No -> invoke the narrow skill directly.
```

## Workflow Map

| Pipeline | Status | Role | Keep / Archive Decision |
|---|---|---|---|
| `new-deal-pipeline/` | Primary | Full deal-pack workflow. Creates one evidence spine for market research, competitive assessment, and IC memo. | Keep as primary route |
| `ic-memo-pipeline/` | Specialized | IC memo workflow when the memo is the main output and upstream research is already scoped. | Keep, but document as memo-only |
| `market-research-pipeline/` | Specialized | Standalone market research report workflow. | Keep, but do not use for IC memo production unless feeding a memo |
| Standalone research phase slice | Removed | Superseded by `plugins/deal-intelligence/` and root canonical skills. | Use `deal-intelligence` grouped plugin |
| `deal-diligence/` | Archive candidate | Standalone plugin slice for diligence. Overlaps with `plugins/deal-intelligence/`, but still exists for modular installs. | Keep only if you intentionally use modular diligence installs |
| Standalone output phase slice | Removed | Superseded by `plugins/deal-intelligence/` and root canonical skills. | Use `deal-intelligence` grouped plugin |

## Delete / Archive Recommendations

Confirmed-unused standalone slices have been removed after marketplace and workflow references
were redirected to `plugins/deal-intelligence/`. Current cleanup state:

| Candidate | Why It Looks Stale | Recommended Action |
|---|---|---|
| Standalone research phase slice | Superseded by packaged `deal-intelligence` bundle and unused by Ian | Removed |
| `deal-diligence/` | Standalone diligence slice overlaps with packaged `deal-intelligence` bundle | Keep for now unless Ian confirms it is unused |
| Standalone output phase slice | Superseded by packaged `deal-intelligence` bundle and unused by Ian | Removed |
| `analytical-operating-system.plugin` | Generated package artifact, not source | Move to `dist/` or regenerate on demand |
| `plugins/deal-intelligence.plugin` | Generated package artifact, not source | Move to `dist/` or regenerate on demand |
| `market-research-pipeline/remaining-agents.md` | Explicitly retained as historical source material in `market-research-pipeline/CLAUDE.md`; agents should not dispatch from it | Keep or move to `archive/notes/` only after updating `CLAUDE.md` |

## Mismatch To Resolve

`deal-workbook-builder` exists in `plugins/deal-intelligence/skills/` but not as a root canonical skill. Root `driver-tree` and `boundability` already reference it, and the docs generator includes it, so this is an active source-of-truth mismatch rather than a dead skill.

Choose one of two actions:

| Option | When To Choose It | Action |
|---|---|---|
| Promote | Preferred if the current references are intentional | Copy it to root as `deal-workbook-builder/`, then document it in the root README |
| Retire | Only if workbook building is no longer part of the system | Remove the plugin copy and update `driver-tree`, `boundability`, `docs/generate_claude_docs.py`, and package docs |

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
