# Skill System Assessment

Date: 2026-06-10
Branch: `codex/skill-overview-assessment`

## BLUF

The skill library has strong analytical content, but the system is now constrained by orchestration hygiene rather than methodology depth. Work Package 1 now stabilizes the highest-risk source-of-truth and packaging issues; the next constraint is explicit dependency contracts and metadata cleanup.

## Decision

Decide which skills should be kept as-is, tightened, merged, split, deprecated, or repackaged.

## Core Hypothesis

The core skills are effective when manually invoked by someone who understands the library, but weaker when used as an autonomous system because dependencies, packaged copies, and trigger metadata are not consistently governed.

## Evidence Summary

| Finding | Evidence | Implication |
|---|---|---|
| README was directionally useful but not fully authoritative | `deal-master` was a root skill but was not in the README skill index; this branch adds it as the L0 deal orchestration entry point | Users now have a clearer default starting point for full deal workflows |
| Root and plugin copies can drift | `mckinsey-consultant` root copy differed from `plugins/deal-intelligence/skills/mckinsey-consultant/SKILL.md`; this branch syncs the grouped plugin copy | Packaged plugin users now get the same analytical ownership rules as root-skill users |
| Metadata is not validator-ready | `skill-authoring-workflow` requires description <= 200 chars; most major skills exceed that | Skill discovery and upload surfaces may truncate or reject descriptions |
| Dependencies are implicit in prose | High-dependency skills name other skills, but most do not expose a formal dependency block | Agents can load skills in the wrong order |
| Quality stack is strong but heavy | `writing-style`, `claim-scrutinizer`, `red-team`, `pre-mortem`, and `doc-quality-checker` create a good control system | Workflows need explicit "lite vs full" gates to avoid over-processing small tasks |

## Skill Quality Snapshot

| Skill / Workflow | Current Effectiveness | Main Strength | Main Gap | Recommendation |
|---|---:|---|---|---|
| `mckinsey-consultant` | High | Strong method owner: issue trees, 7 dimensions, investment gates | Root/grouped-plugin drift has been fixed; formal dependency block still needed | Keep root-to-package sync rule and add formal dependency block |
| `analytical-operating-system` | Medium-High | Clear evidence-control role after recent narrowing | Grouped plugin package now exists; description remains long for stated standard | Shorten metadata and add dependency contract |
| `market-research` | High | Full workflow from brief to QA; strong architecture | Very large; trigger description too long; overlaps with `mckinsey-consultant` and `claim-scrutinizer` in source rules | Keep, but add mode selector and dependency block |
| `competitive-moat-assessment` | High | Strong, specific methodology with existence/strength/durability tests | It sits between research, claim scrutiny, and IC memo but lacks explicit handoff contract | Add input/output contract |
| `ic-memo` / `ic-memo-pipeline` | Medium-High | Clear 10-section structure and quality-pass flow | Complexity split across standalone skill and pipeline agents; dependency load rules differ by entry point | Make `deal-master` the preferred entry and document standalone usage |
| `ntb-diligence` | High | Strong checkpointing and evidence inventory logic | Heavy process; requires clearer "when to skip" rule | Add lite/full mode and reusable NTB output schema |
| `driver-tree` | Medium-High | Deep causal decomposition and scenario discipline | Dense and easy to overuse; depends on downstream boundability/pre-mortem assumptions | Add invocation guardrails and shorter examples |
| `claim-scrutinizer` | High | Strong adversarial claim testing and gap resolution | Can duplicate source validation from `market-research` and prose standards from `writing-style` | Clarify it starts after a draft or claim set exists |
| `writing-style` | High | Excellent final-output prose and attribution discipline | Auto-run rule can be over-applied to interim analysis | Keep auto-run only for formal outputs |
| `pattern-docx` | High but fragile | Detailed Pattern Word production workflow | Current root file is dirty; root/plugin consistency cannot be judged cleanly | Resolve separately before packaging work |
| `pattern-investment-pptx` | Medium-High | Detailed deck design system | Very long and production-specific; could be split into reference files | Keep as production skill, move long specs to references later |
| `doc-quality-checker` | High | Useful post-production QA gate | Mostly manual unless paired with render/verifier tooling | Add concrete smoke-test commands where possible |
| `financial-model-builder` | Medium | Important foundational finance skill | README labels it L4 production, but finance group says it is foundational for finance work | Reclassify as finance foundation, not pure production |
| `gtm-metrics-analyzer` / `kpi-tree-builder` | Medium-High | Strong analytics use cases | Downstream of model/NTB/driver-tree but dependency order is implicit | Add input requirements and dependency blocks |

## Priority Findings

### P0 - Source-of-Truth and Packaging

Applied in this branch:

1. Synced `mckinsey-consultant` root content into the grouped `deal-intelligence` plugin copy.
2. Added `deal-master` to README and CHEATSHEET as the L0 orchestration entry point.
3. Added YAML frontmatter to `deal-master` and synced its packaged copies.
4. Added `analytical-operating-system` and `deal-master` to the grouped `deal-intelligence` plugin skills.
5. Added source-of-truth policy language to README and the grouped plugin README.
6. Tightened the `deal-master` marketplace description so it sits below the metadata ceiling.

### P1 - Dependency Hygiene

1. Skills describe dependencies in prose instead of a consistent machine-readable block.
2. The library has at least three deployment shapes: root skills, grouped `deal-intelligence` plugin copies, and per-skill plugin packages.
3. The current README does not state which packaging path is canonical for each skill.

### P2 - Trigger and Metadata Quality

1. Many frontmatter descriptions exceed the stated 200-character standard.
2. Several major skills use descriptions as mini-briefs rather than trigger text.
3. Some skills should expose quick/full modes to avoid using full diligence machinery for small requests.

### P3 - Content Simplification

1. Several skills are strong but too large for fast, reliable invocation.
2. Long production specs should move into `references/` when they are not needed for every run.
3. Examples should be shorter and more task-specific.

## Recommended Sequence

1. Finish verification for the Work Package 1 sync.
2. Add a standard metadata/dependency block to every system-critical skill.
3. Shorten frontmatter descriptions to validator-friendly trigger language.
4. Add workflow mode rules: quick, standard, full.
5. Only then rewrite or split individual large skills.

## So What?

The library does not need a conceptual rebuild. Work Package 1 handles the highest-risk source-of-truth cleanup; the next value-creating move is explicit dependency contracts, compliant metadata, and clearer mode selection.
