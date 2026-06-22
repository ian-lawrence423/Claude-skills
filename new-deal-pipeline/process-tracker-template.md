# New Deal Process Tracker Template

Use this tracker for every new deal before drafting any narrative output. It is the control tower for workflow order, evidence integrity, and completion status.

Copy this file to:

```text
{WORK_DIR}/shared/process-tracker.md
```

Update it at the start and end of every phase. A phase is not complete until its required artifacts exist, its gate is passed, and the next action is explicit.

## Deal Metadata

| Field | Value |
|---|---|
| Company | TBD |
| Deal type | TBD |
| Decision this work supports | TBD |
| Geography / market boundary | TBD |
| Entry valuation / multiple | TBD |
| Hold period / return target | TBD |
| Materials path | TBD |
| Work dir | TBD |
| Workflow mode | full_deal_pack / ic_memo_only / resume |
| Market mode | full / skip_existing / skip |
| Competitive mode | full / skip_existing / skip |
| IC mode | full / skip_existing / skip |
| NTB mode | full / skip |
| KPI mode | full / skip |
| Source strictness | strict / standard |
| Current release posture | NOT_STARTED / IN_PROGRESS / PASS_WITH_GAPS / HALT / CLEAR_TO_RELEASE |

## Status Rules

| Status | Meaning |
|---|---|
| NOT_STARTED | Phase has not begun |
| IN_PROGRESS | Phase is actively being worked |
| BLOCKED | Phase is waiting on a source, model, user decision, or missing input |
| SKIPPED | Phase was intentionally skipped with a documented reason |
| PASS | Phase gate passed with required artifacts complete |
| PASS_WITH_GAPS | Phase can proceed, but gaps are visible in `shared/open-issues.md` |
| HALT | Phase cannot proceed without resolving a thesis-critical gap |

## Master Phase Tracker

| Phase | Status | Required Plugin / Skill / Workflow | Required Inputs | Required Outputs | Integrity Gate | Owner / Next Action |
|---|---|---|---|---|---|---|
| -1. Framework load | NOT_STARTED | `deal-master`, `mckinsey-consultant`, `analytical-operating-system`, `new-deal-pipeline/quality-contract.md` | Company, deal type, materials path, work dir | `shared/process-tracker.md`, `shared/run-log.md`, copied `shared/quality-contract.md` | Frameworks loaded before any analysis; source strictness set | TBD |
| 0. Inventory and state assessment | NOT_STARTED | `deal-master` | Materials folder, overnight outputs, prior work dir | `shared/materials-index.md`, updated process tracker, state A/B/B2/C/D/E | Every source file cataloged; prior outputs classified as usable/stale/missing | TBD |
| 1. Shared evidence spine | NOT_STARTED | `analytical-operating-system`, `mckinsey-consultant` | Materials index, thesis, prior outputs | `shared/deal-brief.md`, `shared/source-bibliography.md`, `shared/evidence-register.md`, `shared/belief-register.md`, `shared/number-register.md`, `shared/open-issues.md` | No thesis-critical claim is untagged; all numbers have source/date/scope | TBD |
| 2. Market research / overnight handoff | NOT_STARTED | `deal-intelligence`, `market-research-pipeline/orchestrator.md`, `market-research`, `tam-sam-som-calculator` | Evidence spine, overnight market files or source materials | `market-research/final-output.docx` or accepted overnight pack, updated source/evidence/number registers | Market boundary, sizing, growth, customer, competition, economics, risk, and sources complete or marked GAP | TBD |
| 3. Competitive assessment | NOT_STARTED | `deal-intelligence`, `new-deal-pipeline/competitive-assessment.md`, `competitive-moat-assessment`, `boundability` | Evidence spine, competitor sources, market report | `competitive-assessment/competitive-assessment.md`, `competitive-assessment/source-map.md`, `competitive-assessment/open-issues.md`, optional `competitive-assessment/final-output.docx` | Competitor universe, moat mechanism, displacement path, and verdict are sourced | TBD |
| 4. Strategic diligence bridge | NOT_STARTED | `deal-intelligence`, `ntb-diligence`, `driver-tree`, `boundability`, optional `financial-model-builder`, `deal-workbook-builder`, `gtm-metrics-analyzer`, `kpi-tree-builder` | Market report, competitive assessment, evidence registers, model/data room files if available | `diligence/ntb-registry.md`, `diligence/driver-tree.md`, `diligence/boundability.md`, optional model/workbook outputs | Every NTB maps to evidence state, decision impact, kill trigger, and driver-tree node | TBD |
| 5. IC memo draft | NOT_STARTED | `deal-intelligence`, `ic-memo-pipeline/orchestrator.md`, `ic-memo`, `executive-summary-writer`, `writing-style` | Evidence spine, NTB registry, driver tree, boundability, open issues | `ic-memo/draft/*.md`, updated claim ledger and number register | Memo uses only registered claims; GAPs remain visible; recurring numbers reconcile | TBD |
| 6. Adversarial QA | NOT_STARTED | `deal-intelligence`, `claim-scrutinizer`, `red-team`, `pre-mortem`, `boundability` | IC memo draft, claim ledger, open issues, driver tree | `ic-memo/iteration/pass2-claim-scrutinizer.md`, `pass3-red-team.md`, `pass4-pre-mortem.md`, `pass4c-boundability.md` | Zero unaddressed KILL claims; every red/yellow issue has disposition | TBD |
| 7. Production and doc QA | NOT_STARTED | `deal-intelligence`, `pattern-docx`, `pattern-investment-pptx`, `doc-quality-checker` | QA-cleared memo/deck source, Pattern template, source footnotes | `ic-memo/final-output.docx`, optional PPTX, `ic-memo/doc-quality-check.md` | Zero critical format, source, number, or artifact-language issues | TBD |
| 8. Cross-output release review | NOT_STARTED | `new-deal-pipeline/orchestrator.md`, `analytical-operating-system` | All deliverables, shared registers, QA passes | `deal-pack-summary.md`, final process tracker update | Same market definition, competitor set, moat verdict, open issues, and key numbers across outputs | TBD |

## Required Artifact Checklist

| Artifact | Required? | Status | Notes |
|---|---|---|---|
| `shared/process-tracker.md` | Yes | NOT_STARTED | Created from this template |
| `shared/run-log.md` | Yes | NOT_STARTED | Chronological record of phase starts, completions, and decisions |
| `shared/materials-index.md` | Yes | NOT_STARTED | All source files, owners, dates, and source type |
| `shared/deal-brief.md` | Yes | NOT_STARTED | Decision, thesis, issue tree, deliverables |
| `shared/source-bibliography.md` | Yes | NOT_STARTED | Every source with date, scope, independence, and quality |
| `shared/evidence-register.md` | Yes | NOT_STARTED | Every material claim with F/E/H/VENDOR/MGMT/GAP tag |
| `shared/belief-register.md` | Yes | NOT_STARTED | 4-7 load-bearing beliefs, priors, updates, kill triggers |
| `shared/number-register.md` | Yes | NOT_STARTED | Every recurring number, definition, source, and location |
| `shared/claim-ledger.md` | Yes | NOT_STARTED | Claims reused across outputs and QA disposition |
| `shared/open-issues.md` | Yes | NOT_STARTED | All unresolved gaps with decision impact and owner |
| `market-research/final-output.docx` | If market mode is full | NOT_STARTED | Or accepted overnight pack with register updates |
| `competitive-assessment/final-output.docx` | If competitive mode is full | NOT_STARTED | Or accepted existing assessment with register updates |
| `diligence/ntb-registry.md` | If NTB mode is full | NOT_STARTED | Required before IC memo for investment work |
| `diligence/driver-tree.md` | Yes for IC memo | NOT_STARTED | Maps thesis to causal drivers and evidence tiers |
| `diligence/boundability.md` | Yes for IC memo | NOT_STARTED | Tests where the thesis holds or breaks |
| `ic-memo/draft/*.md` | If IC mode is full | NOT_STARTED | Draft before QA |
| `ic-memo/iteration/*.md` | If IC mode is full | NOT_STARTED | Claim, red-team, pre-mortem, boundability passes |
| `ic-memo/final-output.docx` | If IC mode is full | NOT_STARTED | Produced only after QA passes |
| `deal-pack-summary.md` | Yes | NOT_STARTED | Final cross-output release posture |

## Evidence Integrity Dashboard

| Measure | Current Count | Threshold | Status |
|---|---:|---:|---|
| Thesis-critical claims | 0 | All tagged | NOT_STARTED |
| Untagged thesis-critical claims | 0 | 0 | NOT_STARTED |
| `[GAP]` items affecting recommendation | 0 | 0 before CLEAR_TO_RELEASE | NOT_STARTED |
| Single-source dependencies | 0 | Explicitly disclosed | NOT_STARTED |
| Vendor or management claims used as proof | 0 | 0 | NOT_STARTED |
| Recurring numbers without source/date/scope | 0 | 0 | NOT_STARTED |
| Cross-output numeric conflicts | 0 | 0 | NOT_STARTED |
| KILL claims unresolved | 0 | 0 | NOT_STARTED |

## Phase Completion Log

| Date | Phase | Status Change | Files Created / Updated | Key Evidence Updates | Open Issues Added | Next Action |
|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Open Decision Log

| Decision Needed | Why It Matters | Options | Recommendation | Owner | Due Date | Status |
|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | OPEN |

## Final Release Checklist

Do not mark the deal pack complete unless all checks are true:

- [ ] `shared/process-tracker.md` is current.
- [ ] Every requested deliverable exists.
- [ ] Every thesis-critical claim is tagged and sourced or marked GAP.
- [ ] Every recurring number ties to `shared/number-register.md`.
- [ ] Every GAP with decision impact appears in the memo risk/recommendation sections.
- [ ] Claim-scrutinizer, red-team, and pre-mortem have run on the memo draft, not just the pre-IC thesis.
- [ ] `doc-quality-checker` has run on final DOCX/PPTX outputs.
- [ ] `deal-pack-summary.md` states CLEAR_TO_RELEASE, RELEASE_WITH_GAPS, or HALT.

## So What?

This tracker is the source of truth for process integrity. If the tracker is stale, the deal process is stale.
