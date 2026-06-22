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
| Gold Standard Queue URL | `https://docs.google.com/spreadsheets/d/159cKsL9YEWmIoo0BTt6NelobAmAm6qan-VyOagUJuJ4/edit?gid=0#gid=0` |
| Gold Standard Queue row | TBD |
| Queue sheet / range | `Gold Standard Queue!A2:M500` |
| Queue status / phase | TBD |
| Queue prefetch status | TBD |
| Queue Website field | TBD |
| Queue CompetitiveIntel JSON | missing / present / invalid / accepted |
| Overnight n8n run ID | TBD |
| Overnight output folder | TBD |
| Deal intelligence dispatch packet | TBD |
| n8n execution links | TBD |
| Workflow mode | full_deal_pack / resume_repair |
| Research mode | gold_standard_end_to_end |
| Resume / repair exception | none / resume_verified_outputs / repair_failed_phase |
| NTB mode | full |
| KPI mode | full / deferred_until_data_available |
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

## Single Research Mode Rule

There is one supported research path for deal work: `gold_standard_end_to_end`. Do not offer research-light, market-only, competitive-only, or skip-existing modes as deal research options. Existing n8n workflows are components of the one path, not alternative research modes.

Allowed exceptions:

| Exception | When Allowed | Required Proof |
|---|---|---|
| `resume_verified_outputs` | A prior full deal-pack artifact already exists and is current | Artifact path, source bibliography, evidence register, number register, and QA status are logged |
| `repair_failed_phase` | A prior automation or skill phase failed or produced partial output | Failed run ID, missing output, repair owner, and validation gate are logged |
| `deferred_until_data_available` for KPI/model work | Required company data or model is unavailable | Data request is added to `shared/open-issues.md` with owner and decision impact |

Everything else runs through the full chain: intake -> overnight market research -> competitive pre-fetch / landscape mapping -> deal-intelligence dispatch -> shared evidence spine -> market research DOCX -> competitive assessment DOCX -> NTB / driver tree / boundability -> IC memo -> adversarial QA -> final DOCX/PPTX QA -> release.

## Operating Model

The process tracker is the control plane. n8n workflows create intake, prefetch, dispatch, and automation evidence. Claude/Codex skills synthesize that evidence into diligence artifacts, run adversarial QA, and decide release posture. A deal is not complete because an n8n workflow finished; it is complete only when the tracker, required artifacts, and release gates all agree.

| Layer | Owns | Does Not Own | Tracker Test |
|---|---|---|---|
| n8n intake and queue | Email/material intake, Gold Standard Queue row state, output folders, dispatch packets | Final diligence judgment, IC memo quality, release status | Execution ID, queue row, output folder, and handoff JSON are recorded |
| Claude/Codex skills | Evidence synthesis, NTB registry, driver tree, boundability, memo, DOCX/PPTX production, QA | Queue automation state or source-system truth | Artifacts exist, claims are tagged, and gates pass |
| Human owner | Investment judgment, open data requests, final release decision | Hidden assumptions or untracked overrides | Decisions are logged with owner, due date, and rationale |

## n8n Workflow Registry

Use this table to decide which automation belongs in the deal run. Do not skip the completion evidence column.

| n8n Workflow | Live Status | Repo Path | Trigger / Input | Output / Handoff | Completion Evidence | Downstream Use |
|---|---|---|---|---|---|---|
| M&A Deal Intake Automation | Available | `C:\Users\IanLawrence\github\n8n-workflows\m&a-deal-intake\workflow.json` | Daily Gmail scan for "Acquisition Opportunity" or "Project " subjects | Attachments saved to `Pattern Strategic M&A/{Project Name}/` | Materials folder exists; email labeled `n8n-processed`; source files added to `shared/materials-index.md` | Starts Phase 0 inventory; does not validate the deal |
| Market Research Gold Standard Overnight | Available | `C:\Users\IanLawrence\github\n8n-workflows\market-research-gold-standard-overnight\workflow.json` | Schedule, manual trigger, or `/webhook/market-research-gold-standard/run` against one Gold Standard Queue row | Markdown pack plus `CompetitiveIntel` JSON in queue column L | Column K is `complete`; column L has valid JSON with `source`, `run_id`, `output_folder`, `module_files`, summaries, and sources; column M has Website | Phase 0 evidence prefetch and Phase 2 source input |
| Deal Intelligence Orchestrator | Available | `C:\Users\IanLawrence\github\n8n-workflows\deal-intelligence-orchestrator\workflow.json` | Manual or `/webhook/deal-intelligence/run` after overnight prefetch | WorkDir set, row marked `in_progress`, dispatch email/prompt created | Queue row updated in F:J; dispatch packet includes website, work dir, overnight output contract, and required deliverables | Starts the Claude/Codex deal-master run; never marks the deal complete |
| Competitive Landscape Mapping | Available | `C:\Users\IanLawrence\github\n8n-workflows\competitive-landscape-mapping\master-orchestrator.json` | `/webhook/competitive-landscape/run` with company, `website_domain`, category, priority | 10-agent competitive row, scorecards, `competitive_landscape_template_row`, sheet write | `run_id`, sheet column written, recommendation, moat score, strategic fit score, M&A attractiveness score, review flag, source map | Phase 3 competitive evidence and optional Phase 2 market research payload input |
| Market Research Pipeline - Phase 2 | Deprecated as a deal mode; repair component only | `C:\Users\IanLawrence\github\n8n-workflows\market-research-pipeline\workflow.json` | `/webhook/market-research/run` with company and optional `competitive_landscape_template_row` | Four-module markdown research pack under `Pattern Strategic M&A/{Company}/research/` | `l4-market-context.md`, `l3-customer-insights.md`, `tam-sam-som.md`, `competitive-moat-assessment.md`, `driver-evidence-handoff.md`, summary file | Do not offer as a user-selected deal research mode; use only to repair a failed or missing full-chain component |
| Thesis Validation - Phase 5 Pre-IC | Available as pre-IC check | `C:\Users\IanLawrence\github\n8n-workflows\thesis-validation\Thesis Validation - Phase 5 Pre-IC.json` | `/webhook/thesis-validation/run` with thesis and competitive template row | `claim-scrutinizer.md`, `red-team.md`, `pre-mortem.md` under `Pattern Strategic M&A/{Company}/thesis-validation/` | Three files exist and are referenced in open issues / QA notes | Pre-IC challenge input; must not replace memo-level QA on the actual IC memo draft |
| IC Memo Pipeline | Spec exists; workflow export placeholder | `C:\Users\IanLawrence\github\n8n-workflows\ic-memo-pipeline\workflow.json` | Intended form/webhook fields for company, deal type, thesis, materials, NTB mode | Pattern-branded IC memo DOCX when workflow is implemented | Current `workflow.json` is a placeholder with no nodes; treat as not production-ready until exported and tested | Use Claude/Codex `ic-memo` skill path as current authority |

## Gold Standard Queue Contract

The queue is the source of truth for automation state. The process tracker is the source of truth for diligence state. They must reconcile before release.

| Column | Field | Required For | Tracker Check |
|---|---|---|---|
| A | Company | All workflows | Matches Deal Metadata company |
| B | Deal Type | Dispatch and memo setup | Matches deal type |
| C | Thesis | Overnight and dispatch | Not blank or TBD before prefetch |
| D | Geography | Market boundary | Matches market scope |
| E | Materials Path | Inventory and dispatch | Exists or reason missing is logged |
| F | Work Dir | Dispatch and all artifacts | Matches this tracker location |
| G | Status | Automation state | `queued`, `research`, or `in_progress` before release; `complete` only after final release gate |
| H | Phase | Automation phase | Phase 0 for overnight; at least 1 after deal-intelligence dispatch |
| I | Priority | Queue ordering | Captured in run log |
| J | Notes | Dispatch context | Latest automation note copied into run log if material |
| K | Market Research Prefetch Status | Overnight handoff | `complete` before deal-intelligence dispatch unless explicitly forced |
| L | CompetitiveIntel JSON | Overnight handoff | Valid JSON with `source`, `run_id`, `output_folder`, `module_files`, summaries, and sources |
| M | Website | Overnight, competitive, and dispatch | Present and matches canonical company website |

Queue eligibility rules:

- Overnight prefetch can run when Company, Thesis, Status, Priority, and Website are present; Status is `queued`, `in_progress`, or `research`; Phase is less than 1 unless forced; column K is not already `complete` or `running...`.
- Deal intelligence dispatch can run when Status is `queued` or `in_progress`; Phase is at least 1, or Phase is 0 with PreFetchStatus `complete`; CompetitiveIntel is populated; Website and Thesis are populated.
- Completion cannot be set by dispatch. Queue Status becomes `complete` only after `deal-pack-summary.md` says `CLEAR_TO_RELEASE` or `RELEASE_WITH_GAPS`, `shared/open-issues.md` has no HALT items, the final IC memo exists, and cross-output QA has reconciled repeated claims and numbers.

## Gold Standard Queue Row Tracker

Copy the active queue row into this tracker before starting synthesis. Update it after every n8n or Claude/Codex phase that changes queue state.

| Queue Field | Current Value | Required State | Source / Check | Status |
|---|---|---|---|---|
| Row number | TBD | Known | Gold Standard Queue URL / row index | NOT_STARTED |
| Company | TBD | Matches Deal Metadata | Column A | NOT_STARTED |
| Deal Type | TBD | Matches Deal Metadata | Column B | NOT_STARTED |
| Thesis | TBD | Not blank or TBD | Column C; copied into `shared/deal-brief.md` | NOT_STARTED |
| Geography | TBD | Matches market boundary | Column D; reconciled to market report scope | NOT_STARTED |
| Materials Path | TBD | Exists or blocker logged | Column E; checked in `shared/materials-index.md` | NOT_STARTED |
| Work Dir | TBD | Matches this work dir | Column F; contains tracker and deliverables | NOT_STARTED |
| Status | TBD | `queued`, `research`, or `in_progress` until release | Column G; final `complete` only after release gate | NOT_STARTED |
| Phase | TBD | Phase 0 before prefetch; at least 1 after dispatch | Column H; matched to Master Phase Tracker | NOT_STARTED |
| Priority | TBD | Captured | Column I; copied into `shared/run-log.md` | NOT_STARTED |
| Notes | TBD | Latest material note copied | Column J; copied into `shared/run-log.md` if relevant | NOT_STARTED |
| PreFetchStatus | TBD | `complete` before dispatch | Column K | NOT_STARTED |
| CompetitiveIntel JSON | TBD | Valid JSON, archived, reconciled | Column L; copied or summarized in `shared/dispatch-packet.md` | NOT_STARTED |
| Website | TBD | Present and canonical | Column M; used for overnight and competitive research | NOT_STARTED |

## Detailed Step Tracker

Use this table as the operating checklist. A step is not complete because a file exists; it is complete only when the required gate passes and the status is updated here.

| Step | Status | Workstream | Required Action | Required Input | Output / Evidence | Gate |
|---|---|---|---|---|---|---|
| 0.1 | NOT_STARTED | Queue setup | Confirm Gold Standard Queue row exists and copy columns A:M into this tracker | Gold Standard Queue URL | Completed Queue Row Tracker | Company, thesis, website, work dir, and status are not blank |
| 0.2 | NOT_STARTED | Materials intake | Inventory raw files and queue materials path | Materials folder, queue column E | `shared/materials-index.md` | Every source file has owner/date/type/source tag |
| 0.3 | NOT_STARTED | Overnight prefetch | Run or confirm Market Research Gold Standard Overnight | Queue row with thesis and website | Column K `complete`, column L CompetitiveIntel JSON, overnight output folder | JSON has `source`, `run_id`, `output_folder`, `module_files`, summaries, and sources |
| 0.4 | NOT_STARTED | Competitive pre-fetch | Run or confirm competitive landscape / pre-fetch output | Company, website, category, known competitors | Sheet column or `competitive_landscape_template_row`, source map, scores | Scores have rationales and `review_required` is resolved or logged |
| 0.5 | NOT_STARTED | Deal dispatch | Run Deal Intelligence Orchestrator | Queue row with K complete, L populated, M populated | `shared/dispatch-packet.md`; queue row marked `in_progress` | Dispatch packet names all required deliverables and does not mark complete |
| 1.1 | NOT_STARTED | Evidence spine | Create shared work dir and copy quality contract | Work dir, template, quality contract | `shared/process-tracker.md`, `shared/quality-contract.md`, `shared/run-log.md` | Tracker names next action and current phase owner |
| 1.2 | NOT_STARTED | Evidence spine | Create deal brief and issue tree | Queue row, materials, dispatch packet | `shared/deal-brief.md` | Decision, thesis, scope, deliverables, and MECE issue tree are explicit |
| 1.3 | NOT_STARTED | Evidence spine | Initialize source, evidence, belief, number, claim, and open-issue registers | Materials index, overnight outputs, competitive row | Required shared registers | No thesis-critical claim or recurring number is unregistered |
| 2.1 | NOT_STARTED | Market report | Build overnight output index | CompetitiveIntel JSON, output folder | `shared/overnight-output-index.md` | Every expected overnight file is present or logged as GAP |
| 2.2 | NOT_STARTED | Market report | Reconcile overnight claims into registers | Overnight markdown, source bibliography | `market-research/overnight-reconciliation.md` | Each accepted claim has tag, source, confidence, and downstream use |
| 2.3 | NOT_STARTED | Market report | Define market boundary and sizing approach | Deal brief, overnight pack, materials | Market report draft section | In-scope, out-of-scope, substitutes, TAM/SAM/SOM method are explicit |
| 2.4 | NOT_STARTED | Market report | Draft full market research report | Evidence spine, reconciled sources | `market-research/draft.md` | Market, customer, competition, economics, risk, and recommendation are covered |
| 2.5 | NOT_STARTED | Market report | Run market report QA and register updates | Draft, shared registers | Updated source/evidence/number/open-issue registers | No unsupported market-size, growth, vendor, or management claim is used as proof |
| 2.6 | NOT_STARTED | Market report | Produce Pattern DOCX | QA-cleared draft, Pattern DOCX rules | `market-research/final-output.docx` | `doc-quality-checker` passes or issues are logged |
| 3.1 | NOT_STARTED | Competitive assessment | Confirm competitor universe | Competitive row, market report, sources | `competitive-assessment/source-map.md` | Direct competitors, substitutes, platforms, and non-consumption are named |
| 3.2 | NOT_STARTED | Competitive assessment | Build moat and displacement analysis | Source map, market report | `competitive-assessment/competitive-assessment.md` | Moat mechanism, metric, durability, erosion vector, and displacement path are sourced |
| 3.3 | NOT_STARTED | Competitive assessment | Produce competitive assessment DOCX | QA-cleared assessment | `competitive-assessment/final-output.docx` | Final document has sourced verdict and no unresolved review-required issue |
| 4.1 | NOT_STARTED | Diligence bridge | Build NTB registry | Market report, competitive assessment, source registers | `diligence/ntb-registry.md` | 4-7 NTBs map to evidence state, impact, kill trigger, and data request |
| 4.2 | NOT_STARTED | Diligence bridge | Build driver tree | NTB registry, model/data if available | `diligence/driver-tree.md` | Thesis drivers are MECE and mapped to evidence tiers |
| 4.3 | NOT_STARTED | Diligence bridge | Build boundability analysis | Driver tree, moat assessment, failure modes | `diligence/boundability.md` | Where the thesis holds, degrades, or breaks is explicit |
| 4.4 | NOT_STARTED | Diligence bridge | Build or update workbook/model if data is available | Model, P&L, KPI data, NTBs | Optional deal workbook/model outputs | Formula/source integrity passes; if unavailable, data request is logged |
| 5.1 | NOT_STARTED | Pre-IC challenge | Run optional thesis validation only after evidence spine exists | Competitive row, NTBs, open issues | `thesis-validation/*.md` | Outputs are treated as inputs, not memo QA |
| 6.1 | NOT_STARTED | IC memo | Build memo outline around NTBs and gates | Evidence spine, NTBs, driver tree, boundability | `ic-memo/draft/outline.md` | Memo architecture maps each thesis pillar to evidence and risks |
| 6.2 | NOT_STARTED | IC memo | Draft IC memo sections | Market report, competitive assessment, diligence bridge | `ic-memo/draft/*.md` | Claims retain source tags; gaps remain visible |
| 6.3 | NOT_STARTED | IC memo | Draft executive summary last | Completed section drafts, open issues | `ic-memo/draft/executive-summary.md` | Answer-first summary states recommendation, assumptions, and reversal conditions |
| 7.1 | NOT_STARTED | Adversarial QA | Run claim-scrutinizer on IC memo draft | Complete memo draft | `ic-memo/iteration/pass2-claim-scrutinizer.md` | Every material claim has verdict and disposition |
| 7.2 | NOT_STARTED | Adversarial QA | Run red-team on IC memo draft | Claim-scrutinized draft | `ic-memo/iteration/pass3-red-team.md` | KILL/WOUND/EXPOSE attacks are dispositioned |
| 7.3 | NOT_STARTED | Adversarial QA | Run pre-mortem and boundability on IC memo draft | Red-team output, driver tree | `ic-memo/iteration/pass4-pre-mortem.md`, `pass4c-boundability.md` | Failure modes, kill triggers, and bounded thesis zones are reflected in memo |
| 7.4 | NOT_STARTED | Adversarial QA | Reconcile claims and numbers across all outputs | Market report, competitive assessment, memo, registers | Updated `shared/claim-ledger.md`, `shared/number-register.md` | Zero conflicting thesis-critical claims or recurring numbers |
| 8.1 | NOT_STARTED | Production | Produce final Pattern IC memo DOCX | QA-cleared memo source | `ic-memo/final-output.docx` | Pattern DOCX standards and evidence tags preserved |
| 8.2 | NOT_STARTED | Production | Produce optional PPTX / exec summary if requested | Final memo, source registers | Optional PPTX / summary output | Same claims, numbers, and source posture as final memo |
| 8.3 | NOT_STARTED | Production | Run document quality checker | Final DOCX/PPTX outputs | `ic-memo/doc-quality-check.md` and related checks | Zero critical format, source, number, or artifact-language issues |
| 9.1 | NOT_STARTED | Release | Build deal-pack summary | All final outputs and registers | `deal-pack-summary.md` | Release posture is CLEAR_TO_RELEASE, RELEASE_WITH_GAPS, or HALT |
| 9.2 | NOT_STARTED | Release | Update queue release state | Deal-pack summary, open issues, final memo | Queue release note / status update | Queue Status changes to `complete` only after no HALT items remain |
| 9.3 | NOT_STARTED | Release | Final distribution check | Final docs, summary, queue state | Distribution-ready package | Every professional document has final path, QA pass, and owner sign-off |

## Professional Document Readiness Tracker

Use this table to see, at a glance, whether each deliverable is ready to distribute.

| Deliverable | Required? | Draft Complete | Evidence / Sources Complete | Number Reconciled | Adversarial QA Complete | Format QA Complete | Final Path | Release Status |
|---|---|---|---|---|---|---|---|---|
| Market research report | Yes | NOT_STARTED | NOT_STARTED | NOT_STARTED | N/A | NOT_STARTED | `market-research/final-output.docx` | NOT_STARTED |
| Competitive assessment | Yes | NOT_STARTED | NOT_STARTED | NOT_STARTED | N/A | NOT_STARTED | `competitive-assessment/final-output.docx` | NOT_STARTED |
| NTB registry | Yes | NOT_STARTED | NOT_STARTED | N/A | NOT_STARTED | N/A | `diligence/ntb-registry.md` | NOT_STARTED |
| Driver tree | Yes | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | N/A | `diligence/driver-tree.md` | NOT_STARTED |
| Boundability assessment | Yes | NOT_STARTED | NOT_STARTED | N/A | NOT_STARTED | N/A | `diligence/boundability.md` | NOT_STARTED |
| IC memo | Yes | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | `ic-memo/final-output.docx` | NOT_STARTED |
| IC / deal deck | If requested | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | TBD | NOT_STARTED |
| Executive summary | If requested | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | TBD | NOT_STARTED |
| Deal-pack summary | Yes | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | N/A | `deal-pack-summary.md` | NOT_STARTED |

## n8n Run Register

Update this table for every automation run, including failed or partial runs.

| Workflow | Queue Row | n8n Execution ID / URL | Trigger | Started | Finished | Status | Output Folder / Sheet Column | Handoff File / JSON | Validation Result | Next Owner / Action |
|---|---:|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | NOT_STARTED | TBD | TBD | TBD | TBD |

## Master Phase Tracker

| Phase | Status | Required Plugin / Skill / Workflow | Required Inputs | Required Outputs | Integrity Gate | Owner / Next Action |
|---|---|---|---|---|---|---|
| -1. Framework load | NOT_STARTED | `deal-master`, `mckinsey-consultant`, `analytical-operating-system`, `new-deal-pipeline/quality-contract.md` | Company, deal type, materials path, work dir, intended workflow mode | `shared/process-tracker.md`, `shared/run-log.md`, copied `shared/quality-contract.md` | Frameworks loaded before any analysis; source strictness set; process tracker owns status | TBD |
| 0A. Intake and materials capture | NOT_STARTED | n8n `m&a-deal-intake`, `deal-master` | Deal email or user-provided materials folder | `shared/materials-index.md`, raw materials path, intake notes | Every source file cataloged with owner/date/type; missing materials are explicit | TBD |
| 0B. Queue row and dispatch readiness | NOT_STARTED | Gold Standard Queue, `deal-intelligence-orchestrator/phase-contract.json` | Queue columns A:M, website, thesis, priority, work dir | Queue contract section completed, `shared/n8n-run-register.md` or tracker run register updated | Queue row is valid for the next automation; no blank thesis/website/CompetitiveIntel field is ignored | TBD |
| 0C. Overnight market research prefetch | NOT_STARTED | n8n `market-research-gold-standard-overnight` | Eligible Gold Standard Queue row, company, thesis, website, category/geography | `gold-standard-market-research/{run_id}/*.md`, `source-bibliography.md`, column K `complete`, column L `CompetitiveIntel` JSON | Overnight pack has `run_id`, `output_folder`, module files, summaries, and sources; partial failures are marked GAP | TBD |
| 0D. Competitive landscape automation | NOT_STARTED | n8n `competitive-landscape-mapping`, `competitive-moat-assessment` | Company, `website_domain`, category, priority, known competitors if available | Sheet column, `competitive_landscape_template_row`, recommendation, moat/fit/M&A scores, source map | Scores have rationales; `review_required` is resolved or carried to open issues; output is not treated as final diligence | TBD |
| 0E. Deal intelligence dispatch | NOT_STARTED | n8n `deal-intelligence-orchestrator`, `deal-master` | Queue row with PreFetchStatus `complete`, CompetitiveIntel JSON, Website, WorkDir | Queue F:J updated, row marked `in_progress`, dispatch email/prompt, output contract | Dispatch packet names required outputs and does not mark the deal complete | TBD |
| 1. Shared evidence spine | NOT_STARTED | `analytical-operating-system`, `mckinsey-consultant`, `deal-master` | Materials index, dispatch packet, overnight outputs, competitive row, prior outputs | `shared/deal-brief.md`, `shared/source-bibliography.md`, `shared/evidence-register.md`, `shared/belief-register.md`, `shared/number-register.md`, `shared/open-issues.md` | No thesis-critical claim is untagged; all recurring numbers have source/date/scope; n8n sources are indexed | TBD |
| 2. Market research synthesis | NOT_STARTED | `market-research`, `tam-sam-som-calculator`; n8n `market-research-pipeline` only as repair component | Evidence spine, overnight markdown, source materials, competitive row if accepted | `market-research/final-output.docx`, updated registers, `market-research/overnight-reconciliation.md` | Overnight markdown is reconciled or superseded; final DOCX covers market, customer, competition, economics, risks, and gaps | TBD |
| 3. Competitive assessment | NOT_STARTED | `new-deal-pipeline/competitive-assessment.md`, `competitive-moat-assessment`, `boundability`, optional n8n landscape row | Market report, evidence spine, competitor sources, competitive landscape output | `competitive-assessment/competitive-assessment.md`, `competitive-assessment/source-map.md`, `competitive-assessment/open-issues.md`, optional `competitive-assessment/final-output.docx` | Competitor universe, moat mechanism, displacement path, durability, and verdict are sourced | TBD |
| 4. Strategic diligence bridge | NOT_STARTED | `ntb-diligence`, `driver-tree`, `boundability`, optional `financial-model-builder`, `deal-workbook-builder`, `gtm-metrics-analyzer`, `kpi-tree-builder` | Market report, competitive assessment, evidence registers, model/data room files if available | `diligence/ntb-registry.md`, `diligence/driver-tree.md`, `diligence/boundability.md`, optional model/workbook outputs | Every NTB maps to evidence state, decision impact, kill trigger, driver-tree node, and model/data request | TBD |
| 5. Pre-IC thesis validation | NOT_STARTED | optional n8n `thesis-validation`, `claim-scrutinizer`, `red-team`, `pre-mortem` | Competitive row, thesis, NTB registry, open issues | `thesis-validation/claim-scrutinizer.md`, `red-team.md`, `pre-mortem.md`, updated open issues | Pre-IC attacks are logged as inputs only; memo-level QA must still run after the IC memo draft | TBD |
| 6. IC memo draft | NOT_STARTED | `ic-memo`, `executive-summary-writer`, `writing-style`, current Claude/Codex path; n8n IC memo workflow is placeholder until rebuilt | Evidence spine, NTB registry, driver tree, boundability, open issues | `ic-memo/draft/*.md`, updated claim ledger and number register | Memo uses only registered claims; GAPs remain visible; recurring numbers reconcile | TBD |
| 7. Adversarial memo QA | NOT_STARTED | `claim-scrutinizer`, `red-team`, `pre-mortem`, `boundability` | IC memo draft, claim ledger, open issues, driver tree | `ic-memo/iteration/pass2-claim-scrutinizer.md`, `pass3-red-team.md`, `pass4-pre-mortem.md`, `pass4c-boundability.md` | Zero unaddressed KILL claims; every red/yellow issue has disposition and owner | TBD |
| 8. Production and doc QA | NOT_STARTED | `pattern-docx`, `pattern-investment-pptx`, `doc-quality-checker` | QA-cleared memo/deck source, Pattern template, source footnotes | `ic-memo/final-output.docx`, optional PPTX, `ic-memo/doc-quality-check.md` | Zero critical format, source, number, or artifact-language issues | TBD |
| 9. Cross-output release review | NOT_STARTED | `new-deal-pipeline/orchestrator.md`, `analytical-operating-system`, Gold Standard Queue | All deliverables, shared registers, n8n run register, QA passes | `deal-pack-summary.md`, final process tracker update, queue release note | Same market definition, competitor set, moat verdict, open issues, and key numbers across outputs; queue completion is justified | TBD |

## Required Artifact Checklist

| Artifact | Required? | Status | Notes |
|---|---|---|---|
| `shared/process-tracker.md` | Yes | NOT_STARTED | Created from this template |
| `shared/run-log.md` | Yes | NOT_STARTED | Chronological record of phase starts, completions, and decisions |
| `shared/n8n-run-register.md` | Yes if any n8n workflow is used | NOT_STARTED | Execution ID, queue row, output folder, status, and handoff for every automation run |
| `shared/queue-contract-check.md` | Yes if using Gold Standard Queue | NOT_STARTED | Snapshot of columns A:M, eligibility, blockers, and release status |
| `shared/dispatch-packet.md` | Yes after deal-intelligence dispatch | NOT_STARTED | Deal-master prompt, WorkDir, overnight output contract, required deliverables |
| `shared/overnight-output-index.md` | Yes if overnight prefetch ran | NOT_STARTED | `run_id`, output folder, module file inventory, source bibliography path |
| `shared/materials-index.md` | Yes | NOT_STARTED | All source files, owners, dates, and source type |
| `shared/deal-brief.md` | Yes | NOT_STARTED | Decision, thesis, issue tree, deliverables |
| `shared/source-bibliography.md` | Yes | NOT_STARTED | Every source with date, scope, independence, and quality |
| `shared/evidence-register.md` | Yes | NOT_STARTED | Every material claim with F/E/H/VENDOR/MGMT/GAP tag |
| `shared/belief-register.md` | Yes | NOT_STARTED | 4-7 load-bearing beliefs, priors, updates, kill triggers |
| `shared/number-register.md` | Yes | NOT_STARTED | Every recurring number, definition, source, and location |
| `shared/claim-ledger.md` | Yes | NOT_STARTED | Claims reused across outputs and QA disposition |
| `shared/open-issues.md` | Yes | NOT_STARTED | All unresolved gaps with decision impact and owner |
| `market-research/overnight-reconciliation.md` | Yes if overnight prefetch ran | NOT_STARTED | Shows which overnight claims were accepted, superseded, or moved to GAP |
| `market-research/final-output.docx` | Yes | NOT_STARTED | Final synthesis; overnight markdown alone is not sufficient |
| `competitive-assessment/final-output.docx` | Yes | NOT_STARTED | Required unless `resume_verified_outputs` is logged with current QA |
| `competitive-assessment/source-map.md` | Yes | NOT_STARTED | Includes n8n competitive landscape sources if used |
| `diligence/ntb-registry.md` | Yes | NOT_STARTED | Required before IC memo for investment work |
| `diligence/driver-tree.md` | Yes for IC memo | NOT_STARTED | Maps thesis to causal drivers and evidence tiers |
| `diligence/boundability.md` | Yes for IC memo | NOT_STARTED | Tests where the thesis holds or breaks |
| `thesis-validation/claim-scrutinizer.md` | Optional pre-IC | NOT_STARTED | n8n pre-IC challenge output if used |
| `thesis-validation/red-team.md` | Optional pre-IC | NOT_STARTED | n8n pre-IC challenge output if used |
| `thesis-validation/pre-mortem.md` | Optional pre-IC | NOT_STARTED | n8n pre-IC challenge output if used |
| `ic-memo/draft/*.md` | Yes | NOT_STARTED | Draft before QA |
| `ic-memo/iteration/*.md` | Yes | NOT_STARTED | Claim, red-team, pre-mortem, boundability passes |
| `ic-memo/final-output.docx` | Yes | NOT_STARTED | Produced only after QA passes |
| `deal-pack-summary.md` | Yes | NOT_STARTED | Final cross-output release posture |

## Evidence Integrity Dashboard

| Measure | Current Count | Threshold | Status |
|---|---:|---:|---|
| n8n runs used as evidence without execution ID | 0 | 0 | NOT_STARTED |
| n8n runs missing output folder / sheet column | 0 | 0 | NOT_STARTED |
| Queue rows missing Website | 0 | 0 before overnight / dispatch | NOT_STARTED |
| Invalid or missing CompetitiveIntel JSON | 0 | 0 before dispatch | NOT_STARTED |
| Overnight module files missing from output index | 0 | 0 or explicit GAP | NOT_STARTED |
| Overnight claims accepted without source-register entry | 0 | 0 | NOT_STARTED |
| Competitive landscape fields with `review_required=true` unresolved | 0 | 0 before final release | NOT_STARTED |
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

## n8n Handoff Validation Log

Use this log before any n8n output is allowed to influence a final deliverable.

| Date | Workflow | Handoff Artifact | Accepted Scope | Rejected / Superseded Scope | Register Updates Made | Open Issues Added | Gate Result |
|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | NOT_STARTED |

## Open Decision Log

| Decision Needed | Why It Matters | Options | Recommendation | Owner | Due Date | Status |
|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | OPEN |

## Final Release Checklist

Do not mark the deal pack complete unless all checks are true:

- [ ] `shared/process-tracker.md` is current.
- [ ] Gold Standard Queue row, WorkDir, Website, Phase, and Status match this tracker.
- [ ] Every n8n run used as evidence has an execution ID, output folder or sheet column, and handoff artifact.
- [ ] `CompetitiveIntel` JSON from column L is valid, archived or copied into the work dir, and reconciled into registers.
- [ ] Overnight markdown was reconciled into `market-research/final-output.docx` or explicitly superseded.
- [ ] Pre-IC thesis-validation outputs, if used, were rerun or re-tested against the actual IC memo draft.
- [ ] Every requested deliverable exists.
- [ ] Every thesis-critical claim is tagged and sourced or marked GAP.
- [ ] Every recurring number ties to `shared/number-register.md`.
- [ ] Every GAP with decision impact appears in the memo risk/recommendation sections.
- [ ] Claim-scrutinizer, red-team, and pre-mortem have run on the memo draft, not just the pre-IC thesis.
- [ ] `doc-quality-checker` has run on final DOCX/PPTX outputs.
- [ ] `deal-pack-summary.md` states CLEAR_TO_RELEASE, RELEASE_WITH_GAPS, or HALT.
- [ ] Queue Status is changed to `complete` only after the release posture is CLEAR_TO_RELEASE or RELEASE_WITH_GAPS and no HALT items remain.

## So What?

This tracker is the source of truth for process integrity. n8n completion creates evidence and dispatch state; the deal process is complete only when the tracker, artifacts, registers, and release gates all reconcile.
