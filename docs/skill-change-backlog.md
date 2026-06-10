# Skill Change Backlog

Date: 2026-06-10
Branch: `codex/skill-content-refinement` after Work Packages 1-3 were merged

## P0 - Applied in Work Package 1

| Item | Why It Matters | Applied Change | Files |
|---|---|---|---|
| Sync `mckinsey-consultant` package copy | Root analytical method differed from grouped plugin copy | Copied root `mckinsey-consultant` content into `plugins/deal-intelligence/skills/mckinsey-consultant` and queued hash verification | `mckinsey-consultant/`, `plugins/deal-intelligence/skills/mckinsey-consultant/` |
| Add `deal-master` to README | README omitted the main entry-point skill | Added L0 orchestration row and skill index entry; updated CHEATSHEET sequence | `README.md`, `CHEATSHEET.md` |
| Add frontmatter to `deal-master` | It was a root skill without `name` / `description` metadata | Added concise frontmatter and synced standalone plus grouped packaged copies | `deal-master/SKILL.md`, `deal-master/skills/deal-master/SKILL.md`, `plugins/deal-intelligence/skills/deal-master/SKILL.md` |
| Decide canonical packaging model | Root, grouped plugin, and standalone plugin structures coexist | Added source-of-truth policy: root skill folders are canonical authoring source; package copies are synced for publication; tightened marketplace discovery copy | `README.md`, `plugins/deal-intelligence/README.md`, `.claude-plugin/marketplace.json` |

## P1 - Make Dependencies Explicit

| Item | Why It Matters | Proposed Change | Files |
|---|---|---|---|
| Add dependency contract section to system-critical skills | Agents need load order and handoff outputs | Add standard dependency block | `mckinsey-consultant`, `market-research`, `ic-memo`, `ntb-diligence`, `claim-scrutinizer`, `writing-style`, `pattern-docx` |
| Add quick / standard / full modes | Avoid over-processing simple tasks | Define mode gates and skip rules | `market-research`, `ic-memo`, `ntb-diligence`, `driver-tree`, `claim-scrutinizer` |
| Clarify auto-run rules | Prevent quality skills from running on interim scratch work | Make auto-run conditions explicit and bounded | `writing-style`, `doc-quality-checker`, `README.md` |
| Create workflow tests | Validate load order and handoffs | Add scenario prompts and expected skill chain | `docs/` or `tests/` |

## P2 - Metadata and Trigger Hygiene

| Item | Why It Matters | Proposed Change | Files |
|---|---|---|---|
| Shorten descriptions over 200 chars | Repo standard requires descriptions <= 200 chars | Applied concise discovery summaries and moved prior trigger prose to `intent` | Root skill set plus matching packaged copies |
| Normalize frontmatter fields | Metadata is inconsistent across skills | Standardized `name`, `description`, `intent`, and `type` on root skills and synced package copies | Root skill set plus matching packaged copies |
| Fix folder/name mismatch | Folder `Deck_Check` has frontmatter name `ib-check-deck`; `Deck_Refresh` has `deck-refresh` | Kept frontmatter `name` as canonical invocation name; folder names remain legacy packaging paths | `Deck_Check`, `Deck_Refresh` |

## P3 - Content Quality Improvements

| Item | Why It Matters | Proposed Change | Files |
|---|---|---|---|
| Split long production specs into references | Long skills are harder to load and reason over | Move detailed XML/PPTX specs into references | `pattern-docx`, `pattern-investment-pptx` |
| Add one good example per skill | Current skills often have method but not concrete examples | Add compact input/output example | Core 15 skills first |
| Add anti-pattern per skill | Skill-authoring standard calls for one anti-pattern | Add a short "do not use this when..." block | Core 15 skills first |
| Improve README architecture | Current README is useful but not enough for governance | Add orchestration, packaging, and source-of-truth sections | `README.md` |

## Suggested Work Packages

### Work Package 1 - Governance Stabilization

Scope:
- P0 fixes
- Packaging source-of-truth policy
- README/CHEATSHEET corrections

Exit criteria:
- No packaged-copy drift for synced system-critical skills
- `deal-master` is discoverable and metadata-compliant
- README accurately describes deployment shapes

Status: implemented and merged in Work Package 1.

### Work Package 2 - Dependency Contracts

Scope:
- Add dependency blocks to the top 10 central skills
- Add quick / standard / full mode gates
- Add handoff output schemas

Exit criteria:
- A user can trace market research, competitive analysis, IC memo, and GTM diagnostic workflows without reading every skill file

Status: implemented and merged in Work Package 2. Dependency contracts and mode gates were added to the core strategy, research, memo, diligence, adversarial, and underwriting workflow skills: `mckinsey-consultant`, `market-research`, `ic-memo`, `ntb-diligence`, `driver-tree`, `claim-scrutinizer`, `writing-style`, `red-team`, `pre-mortem`, and `boundability`. The separate Pattern DOCX workflow update was also merged.

### Work Package 3 - Metadata Cleanup

Scope:
- Shorten frontmatter descriptions
- Move long explanations to `intent`
- Normalize naming

Exit criteria:
- All skills satisfy the stated metadata standard

Status: implemented on `codex/skill-metadata-cleanup`. Root skill frontmatter now uses concise `description` values, preserves fuller trigger/context text in `intent`, and includes `type: workflow`. Matching packaged copies were synced from root sources.

### Work Package 4 - Content Refinement

Scope:
- Improve examples and anti-patterns
- Split oversized production specs into reference files
- Add smoke-test prompts

Exit criteria:
- High-priority skills are easier to invoke and less likely to overlap

Status: first slice implemented on `codex/skill-content-refinement`. Added compact examples and anti-pattern boundaries to the core deal workflow stack, then added matching content-refinement smoke tests in `docs/skill-workflow-tests.md`. Splitting the large DOCX/PPTX production specs remains deferred to a separate branch because those files encode exact generation behavior and should be migrated with dedicated render/QA verification.

## So What?

Governance is now the active workstream. With Work Package 1 applied, the next highest-return changes are dependency contracts, mode gates, and metadata normalization.
