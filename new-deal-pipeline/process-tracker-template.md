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
| Data room access status | none / requested / granted / partially_granted / complete |
| Data room opened date | TBD |
| Data room index path | TBD |
| Data room validation status | NOT_STARTED / IN_PROGRESS / PASS_WITH_GAPS / HALT |
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

Everything else runs through the full chain in two stages:

Pre-data-room: intake -> overnight market research -> competitive pre-fetch / landscape mapping -> deal-intelligence dispatch -> shared evidence spine -> market research DOCX -> competitive assessment DOCX -> outside-in NTB registry -> outside-in driver tree -> data-room request list.

Post-data-room: data-room intake and index -> company-specific source validation -> confirmed NTB registry and driver tree -> formula-linked deal workbook / model bridge -> GTM metrics diagnostic -> KPI tree -> boundability -> IC memo -> adversarial QA -> final DOCX/PPTX QA -> release.

## Data Room Separation Rule

The process tracker separates work by information state. Pre-data-room work maximizes outside-in evidence and creates the exact diligence asks. Post-data-room work validates or revises those hypotheses using company-specific materials.

| Stage | Information State | Allowed Outputs | Cannot Be Marked Complete Until |
|---|---|---|---|
| Pre-data-room | Public sources, banker materials, teasers, initial management materials, overnight research, competitive pre-fetch | Market report, competitive assessment, outside-in NTB registry, outside-in driver tree, data-room request list, open issues | Public/initial evidence is reconciled and every company-specific claim is tagged as GAP, MGMT, or provisional |
| Data-room gate | Access requested or granted | Data-room index, source inventory, validation plan | `shared/data-room-index.md` exists and source files have owner/date/type/source tags |
| Post-data-room | Full or partial data-room materials, source financial model, customer/KPI/CRM exports, contracts, QoE, management responses | Confirmed NTB registry, validated driver tree, deal workbook, GTM diagnostic, KPI tree, boundability, IC memo, final QA | Data-room evidence has been reconciled into registers and unresolved blockers are visible in `shared/open-issues.md` |

## Operating Model

The process tracker is the control plane. n8n workflows create intake, prefetch, dispatch, and automation evidence. Claude/Codex skills synthesize that evidence into diligence artifacts, run adversarial QA, and decide release posture. A deal is not complete because an n8n workflow finished; it is complete only when the tracker, required artifacts, and release gates all agree.

| Layer | Owns | Does Not Own | Tracker Test |
|---|---|---|---|
| n8n intake and queue | Email/material intake, Gold Standard Queue row state, output folders, dispatch packets | Final diligence judgment, IC memo quality, release status | Execution ID, queue row, output folder, and handoff JSON are recorded |
| Claude/Codex skills | Evidence synthesis, NTB registry, driver tree, formula-linked deal workbook, GTM metrics diagnostic, KPI tree, boundability, memo, DOCX/PPTX production, QA | Queue automation state or source-system truth | Artifacts exist, claims are tagged, model links reconcile, and gates pass |
| Human owner | Investment judgment, open data requests, final release decision | Hidden assumptions or untracked overrides | Decisions are logged with owner, due date, and rationale |

## n8n Workflow Registry

Use this table to decide which automation belongs in the deal run. Do not skip the completion evidence column.

| n8n Workflow | Live Status | Repo Path | Trigger / Input | Output / Handoff | Completion Evidence | Data-Room Stage / Downstream Use |
|---|---|---|---|---|---|---|
| M&A Deal Intake Automation | Available | `C:\Users\IanLawrence\github\n8n-workflows\m&a-deal-intake\workflow.json` | Daily Gmail scan for "Acquisition Opportunity" or "Project " subjects | Attachments saved to `Pattern Strategic M&A/{Project Name}/` | Materials folder exists; email labeled `n8n-processed`; source files added to `shared/materials-index.md` | Pre-data-room: starts Phase 0 inventory; does not validate the deal |
| Market Research Gold Standard Overnight | Available | `C:\Users\IanLawrence\github\n8n-workflows\market-research-gold-standard-overnight\workflow.json` | Schedule, manual trigger, or `/webhook/market-research-gold-standard/run` against one Gold Standard Queue row | Markdown pack plus `CompetitiveIntel` JSON in queue column L | Column K is `complete`; column L has valid JSON with `source`, `run_id`, `output_folder`, `module_files`, summaries, and sources; column M has Website | Pre-data-room: evidence prefetch and Phase 2 source input |
| Deal Intelligence Orchestrator | Available | `C:\Users\IanLawrence\github\n8n-workflows\deal-intelligence-orchestrator\workflow.json` | Manual or `/webhook/deal-intelligence/run` after overnight prefetch | WorkDir set, row marked `in_progress`, dispatch email/prompt created | Queue row updated in F:J; dispatch packet includes website, work dir, overnight output contract, and required deliverables | Pre-data-room: starts the Claude/Codex deal-master run; never marks the deal complete |
| Competitive Landscape Mapping | Available | `C:\Users\IanLawrence\github\n8n-workflows\competitive-landscape-mapping\master-orchestrator.json` | `/webhook/competitive-landscape/run` with company, `website_domain`, category, priority | 10-agent competitive row, scorecards, `competitive_landscape_template_row`, sheet write | `run_id`, sheet column written, recommendation, moat score, strategic fit score, M&A attractiveness score, review flag, source map | Pre-data-room: competitive evidence and optional market research payload input |
| Market Research Pipeline - Phase 2 | Deprecated as a deal mode; repair component only | `C:\Users\IanLawrence\github\n8n-workflows\market-research-pipeline\workflow.json` | `/webhook/market-research/run` with company and optional `competitive_landscape_template_row` | Four-module markdown research pack under `Pattern Strategic M&A/{Company}/research/` | `l4-market-context.md`, `l3-customer-insights.md`, `tam-sam-som.md`, `competitive-moat-assessment.md`, `driver-evidence-handoff.md`, summary file | Pre-data-room repair only: do not offer as a user-selected deal research mode |
| Thesis Validation - Phase 5 Pre-IC | Available as pre-IC check | `C:\Users\IanLawrence\github\n8n-workflows\thesis-validation\Thesis Validation - Phase 5 Pre-IC.json` | `/webhook/thesis-validation/run` with thesis and competitive template row | `claim-scrutinizer.md`, `red-team.md`, `pre-mortem.md` under `Pattern Strategic M&A/{Company}/thesis-validation/` | Three files exist and are referenced in open issues / QA notes | Pre-data-room challenge input; must not replace memo-level QA on the actual IC memo draft |
| IC Memo Pipeline | Spec exists; workflow export placeholder | `C:\Users\IanLawrence\github\n8n-workflows\ic-memo-pipeline\workflow.json` | Intended form/webhook fields for company, deal type, thesis, materials, NTB mode | Pattern-branded IC memo DOCX when workflow is implemented | Current `workflow.json` is a placeholder with no nodes; treat as not production-ready until exported and tested | Post-data-room only when implemented; current authority is Claude/Codex `ic-memo` skill path |

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

Use these tables as the operating checklist. A step is not complete because a file exists; it is complete only when the required gate passes and the status is updated here.

### Pre-Data-Room Step Tracker

Pre-data-room work is outside-in. Its job is to create the strongest possible public-evidence package, name every company-specific assumption, and convert unknowns into exact data-room requests.

| Step | Status | Workstream | Required Action | Required Input | Output / Evidence | Gate |
|---|---|---|---|---|---|---|
| PRE-0.1 | NOT_STARTED | Queue setup | Confirm Gold Standard Queue row exists and copy columns A:M into this tracker | Gold Standard Queue URL | Completed Queue Row Tracker | Company, thesis, website, work dir, and status are not blank |
| PRE-0.2 | NOT_STARTED | Materials intake | Inventory teaser, banker materials, public materials, and queue materials path | Materials folder, queue column E | `shared/materials-index.md` | Every source file has owner/date/type/source tag and data-room status |
| PRE-0.3 | NOT_STARTED | Overnight prefetch | Run or confirm Market Research Gold Standard Overnight | Queue row with thesis and website | Column K `complete`, column L CompetitiveIntel JSON, overnight output folder | JSON has `source`, `run_id`, `output_folder`, `module_files`, summaries, and sources |
| PRE-0.4 | NOT_STARTED | Competitive pre-fetch | Run or confirm competitive landscape / pre-fetch output | Company, website, category, known competitors | Sheet column or `competitive_landscape_template_row`, source map, scores | Scores have rationales and `review_required` is resolved or logged |
| PRE-0.5 | NOT_STARTED | Deal dispatch | Run Deal Intelligence Orchestrator | Queue row with K complete, L populated, M populated | `shared/dispatch-packet.md`; queue row marked `in_progress` | Dispatch packet names pre-data-room and post-data-room deliverables and does not mark complete |
| PRE-1.1 | NOT_STARTED | Evidence spine | Create shared work dir and copy quality contract | Work dir, template, quality contract | `shared/process-tracker.md`, `shared/quality-contract.md`, `shared/run-log.md` | Tracker names data-room stage, next action, and current phase owner |
| PRE-1.2 | NOT_STARTED | Evidence spine | Create deal brief and issue tree | Queue row, materials, dispatch packet | `shared/deal-brief.md` | Decision, thesis, scope, deliverables, and MECE issue tree are explicit |
| PRE-1.3 | NOT_STARTED | Evidence spine | Initialize source, evidence, belief, number, claim, and open-issue registers | Materials index, overnight outputs, competitive row | Required shared registers | No thesis-critical claim or recurring number is unregistered |
| PRE-2.1 | NOT_STARTED | Market report | Build overnight output index | CompetitiveIntel JSON, output folder | `shared/overnight-output-index.md` | Every expected overnight file is present or logged as GAP |
| PRE-2.2 | NOT_STARTED | Market report | Reconcile overnight claims into registers | Overnight markdown, source bibliography | `market-research/overnight-reconciliation.md` | Each accepted claim has tag, source, confidence, and downstream use |
| PRE-2.3 | NOT_STARTED | Market report | Define market boundary and sizing approach | Deal brief, overnight pack, materials | Market report draft section | In-scope, out-of-scope, substitutes, TAM/SAM/SOM method are explicit |
| PRE-2.4 | NOT_STARTED | Market report | Draft full market research report | Evidence spine, reconciled sources | `market-research/draft.md` | Market, customer, competition, economics, risk, and recommendation are covered |
| PRE-2.5 | NOT_STARTED | Market report | Run market report QA and register updates | Draft, shared registers | Updated source/evidence/number/open-issue registers | No unsupported market-size, growth, vendor, or management claim is used as proof |
| PRE-2.6 | NOT_STARTED | Market report | Produce Pattern DOCX | QA-cleared draft, Pattern DOCX rules | `market-research/final-output.docx` | `doc-quality-checker` passes or issues are logged |
| PRE-3.1 | NOT_STARTED | Competitive assessment | Confirm competitor universe | Competitive row, market report, sources | `competitive-assessment/source-map.md` | Direct competitors, substitutes, platforms, and non-consumption are named |
| PRE-3.2 | NOT_STARTED | Competitive assessment | Build moat and displacement analysis | Source map, market report | `competitive-assessment/competitive-assessment.md` | Moat mechanism, metric, durability, erosion vector, and displacement path are sourced |
| PRE-3.3 | NOT_STARTED | Competitive assessment | Produce competitive assessment DOCX | QA-cleared assessment | `competitive-assessment/final-output.docx` | Final document has sourced verdict and no unresolved review-required issue |
| PRE-4.1 | NOT_STARTED | Outside-in NTB registry | Build preliminary NTB registry and data-room request list | Market report, competitive assessment, source registers | `diligence/ntb-registry.md`, `diligence/data-room-request-list.md` | 4-7 NTBs map to evidence state, impact, kill trigger, and exact data-room request |
| PRE-4.2 | NOT_STARTED | Outside-in driver tree | Build preliminary driver tree | NTB registry, public comps, disclosed model assumptions if available | `diligence/driver-tree.md` | Thesis drivers are MECE, evidence-tiered, and marked provisional where data room evidence is required |
| PRE-5.1 | NOT_STARTED | Pre-IC challenge | Run optional thesis validation only after evidence spine exists | Competitive row, NTBs, open issues | `thesis-validation/*.md` | Outputs are treated as pre-data-room challenge inputs, not memo QA |
| PRE-5.2 | NOT_STARTED | Data-room gate | Confirm data-room access state and request missing materials | Preliminary NTBs, driver tree, open issues | `shared/data-room-access-log.md`, updated `shared/open-issues.md` | Post-data-room work has clear access status, requested files, owner, and decision impact |

### Post-Data-Room Step Tracker

Post-data-room work is validation and underwriting. It starts only when data-room access is granted or partially granted and `shared/data-room-index.md` exists. If access is not granted, keep these steps `BLOCKED` or `DEFERRED_WITH_BLOCKER`; do not mark them PASS from outside-in evidence.

| Step | Status | Workstream | Required Action | Required Input | Output / Evidence | Gate |
|---|---|---|---|---|---|---|
| POST-0.1 | NOT_STARTED | Data-room intake | Index all data-room files and management responses | Data-room export, source model, company uploads, request list | `shared/data-room-index.md`, updated `shared/materials-index.md` | Every file has owner/date/type/source tag, source tier, and mapped diligence request |
| POST-0.2 | NOT_STARTED | Source validation | Reconcile data-room evidence against outside-in claims | Data-room index, source/evidence/number registers | `diligence/data-room-validation.md`, updated registers | Each PRE-stage thesis-critical claim is confirmed, weakened, contradicted, or still GAP |
| POST-1.1 | NOT_STARTED | Confirmed NTB registry | Update NTBs with company-specific evidence | Data-room validation, preliminary NTB registry | Updated `diligence/ntb-registry.md` | Every NTB has confirmed evidence state, impact, kill trigger, and unresolved data request if any |
| POST-1.2 | NOT_STARTED | Validated driver tree | Update driver tree with model/data-room evidence | Confirmed NTBs, source model, KPI data, validation output | Updated `diligence/driver-tree.md` | Load-bearing drivers have evidence tiers, base-rate/vintage checks, and no hidden T4 base-case dependency |
| POST-2.1 | NOT_STARTED | Deal workbook / model bridge | Build or update formula-linked deal workbook | Source model, P&L, KPI data, NTB registry, driver tree | `diligence/deal-workbook.xlsx`, `diligence/workbook-quality-check.md` | Formula chain links to source model or documented inputs; no hardcoded model-chain cells; formula errors are zero |
| POST-2.2 | NOT_STARTED | GTM metrics diagnostic | Build GTM diagnostic workbook when sales-led or SaaS GTM data is available | CRM exports, ARR/MRR waterfall, pipeline, bookings, retention, S&M spend, headcount, driver tree, deal workbook | `diligence/gtm-metrics-diagnostic.xlsx`, `diligence/gtm-metrics-summary.md` | Inputs and derived metrics are separated; ARR funnel, retention, pipeline health, sales efficiency, and productivity are calculated or logged as missing |
| POST-2.3 | NOT_STARTED | KPI tree | Build KPI tree from driver tree, workbook, and GTM diagnostic | Driver tree, deal workbook, GTM diagnostic, source model, operating metrics, data-room files | `diligence/kpi-tree.md` | Every thesis-critical driver maps to KPI definition, formula, source, owner, cadence, and action threshold or a data-room request |
| POST-2.4 | NOT_STARTED | Boundability | Build boundability analysis | NTB registry, driver tree, deal workbook, GTM diagnostic, KPI tree, moat assessment, failure modes | `diligence/boundability.md` | Where the thesis holds, degrades, or breaks is explicit; underwriting treatment maps to model, price, leverage, docs/structure, or operating plan |
| POST-3.1 | NOT_STARTED | IC memo | Build memo outline around NTBs, drivers, GTM metrics, KPIs, and gates | Evidence spine, NTB registry, driver tree, deal workbook, GTM diagnostic, KPI tree, boundability | `ic-memo/draft/outline.md` | Memo architecture maps each thesis pillar to evidence, drivers, GTM metrics, KPIs, model impact, and risks |
| POST-3.2 | NOT_STARTED | IC memo | Draft IC memo sections | Market report, competitive assessment, NTB registry, driver tree, deal workbook, GTM diagnostic, KPI tree, boundability | `ic-memo/draft/*.md` | Claims retain source tags; gaps remain visible |
| POST-3.3 | NOT_STARTED | IC memo | Draft executive summary last | Completed section drafts, open issues | `ic-memo/draft/executive-summary.md` | Answer-first summary states recommendation, assumptions, and reversal conditions |
| POST-4.1 | NOT_STARTED | Adversarial QA | Run claim-scrutinizer on IC memo draft | Complete memo draft | `ic-memo/iteration/pass2-claim-scrutinizer.md` | Every material claim has verdict and disposition |
| POST-4.2 | NOT_STARTED | Adversarial QA | Run red-team on IC memo draft | Claim-scrutinized draft | `ic-memo/iteration/pass3-red-team.md` | KILL/WOUND/EXPOSE attacks are dispositioned |
| POST-4.3 | NOT_STARTED | Adversarial QA | Run pre-mortem and boundability on IC memo draft | Red-team output, driver tree | `ic-memo/iteration/pass4-pre-mortem.md`, `pass4c-boundability.md` | Failure modes, kill triggers, and bounded thesis zones are reflected in memo |
| POST-4.4 | NOT_STARTED | Adversarial QA | Reconcile claims and numbers across all outputs | Market report, competitive assessment, memo, registers | Updated `shared/claim-ledger.md`, `shared/number-register.md` | Zero conflicting thesis-critical claims or recurring numbers |
| POST-5.1 | NOT_STARTED | Production | Produce final Pattern IC memo DOCX | QA-cleared memo source | `ic-memo/final-output.docx` | Pattern DOCX standards and evidence tags preserved |
| POST-5.2 | NOT_STARTED | Production | Produce optional PPTX / exec summary if requested | Final memo, source registers | Optional PPTX / summary output | Same claims, numbers, and source posture as final memo |
| POST-5.3 | NOT_STARTED | Production | Run document quality checker | Final DOCX/PPTX outputs | `ic-memo/doc-quality-check.md` and related checks | Zero critical format, source, number, or artifact-language issues |
| POST-6.1 | NOT_STARTED | Release | Build deal-pack summary | All final outputs and registers | `deal-pack-summary.md` | Release posture is CLEAR_TO_RELEASE, RELEASE_WITH_GAPS, or HALT |
| POST-6.2 | NOT_STARTED | Release | Update queue release state | Deal-pack summary, open issues, final memo | Queue release note / status update | Queue Status changes to `complete` only after no HALT items remain |
| POST-6.3 | NOT_STARTED | Release | Final distribution check | Final docs, summary, queue state | Distribution-ready package | Every professional document has final path, QA pass, and owner sign-off |

## Professional Document Readiness Tracker

Use this table to see, at a glance, whether each deliverable is ready to distribute.

| Deliverable | Required? | Draft Complete | Evidence / Sources Complete | Number Reconciled | Adversarial QA Complete | Format QA Complete | Final Path | Release Status |
|---|---|---|---|---|---|---|---|---|
| Market research report | Yes | NOT_STARTED | NOT_STARTED | NOT_STARTED | N/A | NOT_STARTED | `market-research/final-output.docx` | NOT_STARTED |
| Competitive assessment | Yes | NOT_STARTED | NOT_STARTED | NOT_STARTED | N/A | NOT_STARTED | `competitive-assessment/final-output.docx` | NOT_STARTED |
| NTB registry | Yes | NOT_STARTED | NOT_STARTED | N/A | NOT_STARTED | N/A | `diligence/ntb-registry.md` | NOT_STARTED |
| Driver tree | Yes | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | N/A | `diligence/driver-tree.md` | NOT_STARTED |
| Deal workbook / model bridge | Yes when model or financial data is available | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | `diligence/deal-workbook.xlsx` | NOT_STARTED |
| GTM metrics diagnostic | Yes when GTM data is available | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | `diligence/gtm-metrics-diagnostic.xlsx` | NOT_STARTED |
| KPI tree | Yes; defer only when data is unavailable | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | N/A | `diligence/kpi-tree.md` | NOT_STARTED |
| Boundability assessment | Yes | NOT_STARTED | NOT_STARTED | N/A | NOT_STARTED | N/A | `diligence/boundability.md` | NOT_STARTED |
| IC memo | Yes | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | `ic-memo/final-output.docx` | NOT_STARTED |
| IC / deal deck | If requested | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | TBD | NOT_STARTED |
| Executive summary | If requested | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | TBD | NOT_STARTED |
| Deal-pack summary | Yes | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | N/A | `deal-pack-summary.md` | NOT_STARTED |

## n8n Run Register

Update this table for every automation run, including failed or partial runs.

| Stage | Workflow | Queue Row | n8n Execution ID / URL | Trigger | Started | Finished | Status | Output Folder / Sheet Column | Handoff File / JSON | Validation Result | Next Owner / Action |
|---|---|---:|---|---|---|---|---|---|---|---|---|
| PRE / POST / DR-GATE | TBD | TBD | TBD | TBD | TBD | TBD | NOT_STARTED | TBD | TBD | TBD | TBD |

## Master Phase Tracker

| Stage | Phase | Status | Required Plugin / Skill / Workflow | Required Inputs | Required Outputs | Integrity Gate | Owner / Next Action |
|---|---|---|---|---|---|---|---|
| Pre-data-room | -1. Framework load | NOT_STARTED | `deal-master`, `mckinsey-consultant`, `analytical-operating-system`, `new-deal-pipeline/quality-contract.md` | Company, deal type, materials path, work dir, intended workflow mode | `shared/process-tracker.md`, `shared/run-log.md`, copied `shared/quality-contract.md` | Frameworks loaded before any analysis; source strictness and data-room stage set | TBD |
| Pre-data-room | 0A. Intake and initial materials capture | NOT_STARTED | n8n `m&a-deal-intake`, `deal-master` | Deal email, teaser, banker materials, user-provided materials folder | `shared/materials-index.md`, raw materials path, intake notes | Every initial source file cataloged with owner/date/type/source and data-room status | TBD |
| Pre-data-room | 0B. Queue row and dispatch readiness | NOT_STARTED | Gold Standard Queue, `deal-intelligence-orchestrator/phase-contract.json` | Queue columns A:M, website, thesis, priority, work dir | Queue contract section completed, `shared/n8n-run-register.md` or tracker run register updated | Queue row is valid for the next automation; no blank thesis/website/CompetitiveIntel field is ignored | TBD |
| Pre-data-room | 0C. Overnight market research prefetch | NOT_STARTED | n8n `market-research-gold-standard-overnight` | Eligible Gold Standard Queue row, company, thesis, website, category/geography | `gold-standard-market-research/{run_id}/*.md`, `source-bibliography.md`, column K `complete`, column L `CompetitiveIntel` JSON | Overnight pack has `run_id`, `output_folder`, module files, summaries, and sources; partial failures are marked GAP | TBD |
| Pre-data-room | 0D. Competitive landscape automation | NOT_STARTED | n8n `competitive-landscape-mapping`, `competitive-moat-assessment` | Company, `website_domain`, category, priority, known competitors if available | Sheet column, `competitive_landscape_template_row`, recommendation, moat/fit/M&A scores, source map | Scores have rationales; `review_required` is resolved or carried to open issues; output is not treated as final diligence | TBD |
| Pre-data-room | 0E. Deal intelligence dispatch | NOT_STARTED | n8n `deal-intelligence-orchestrator`, `deal-master` | Queue row with PreFetchStatus `complete`, CompetitiveIntel JSON, Website, WorkDir | Queue F:J updated, row marked `in_progress`, dispatch email/prompt, output contract | Dispatch packet names pre-data-room and post-data-room outputs and does not mark the deal complete | TBD |
| Pre-data-room | 1. Shared evidence spine | NOT_STARTED | `analytical-operating-system`, `mckinsey-consultant`, `deal-master` | Materials index, dispatch packet, overnight outputs, competitive row, prior outputs | `shared/deal-brief.md`, `shared/source-bibliography.md`, `shared/evidence-register.md`, `shared/belief-register.md`, `shared/number-register.md`, `shared/open-issues.md` | No thesis-critical claim is untagged; all recurring numbers have source/date/scope; n8n sources are indexed | TBD |
| Pre-data-room | 2. Market research synthesis | NOT_STARTED | `market-research`, `tam-sam-som-calculator`; n8n `market-research-pipeline` only as repair component | Evidence spine, overnight markdown, source materials, competitive row if accepted | `market-research/final-output.docx`, updated registers, `market-research/overnight-reconciliation.md` | Overnight markdown is reconciled or superseded; final DOCX covers market, customer, competition, economics, risks, and gaps | TBD |
| Pre-data-room | 3. Competitive assessment | NOT_STARTED | `new-deal-pipeline/competitive-assessment.md`, `competitive-moat-assessment`, `boundability`, optional n8n landscape row | Market report, evidence spine, competitor sources, competitive landscape output | `competitive-assessment/competitive-assessment.md`, `competitive-assessment/source-map.md`, `competitive-assessment/open-issues.md`, optional `competitive-assessment/final-output.docx` | Competitor universe, moat mechanism, displacement path, durability, and verdict are sourced | TBD |
| Pre-data-room | 4A. Outside-in NTB registry and diligence request list | NOT_STARTED | `ntb-diligence`, `diligence-ddr` | Market report, competitive assessment, evidence registers, belief register, number register | `diligence/ntb-registry.md`, `diligence/data-room-request-list.md` | 4-7 NTBs; each maps to evidence state, decision impact, kill trigger, and exact data-room request | TBD |
| Pre-data-room | 4B. Outside-in driver tree | NOT_STARTED | `driver-tree` | NTB registry, market report, competitive assessment, public comps, provisional assumptions | `diligence/driver-tree.md` | Thesis decomposes into MECE causal drivers; provisional nodes and required company evidence are explicit | TBD |
| Pre-data-room | 5. Pre-IC thesis validation | NOT_STARTED | optional n8n `thesis-validation`, `claim-scrutinizer`, `red-team`, `pre-mortem` | Competitive row, thesis, NTB registry, open issues | `thesis-validation/claim-scrutinizer.md`, `red-team.md`, `pre-mortem.md`, updated open issues | Pre-IC attacks are logged as inputs only; memo-level QA must still run after the IC memo draft | TBD |
| Data-room gate | DR0. Access and source inventory | NOT_STARTED | `deal-master`, `diligence-ddr` | Data-room access, request list, management responses, full materials export | `shared/data-room-access-log.md`, `shared/data-room-index.md`, updated `shared/materials-index.md` | Post-data-room work cannot begin until data-room files are indexed or blocker is logged | TBD |
| Post-data-room | DR1. Data-room validation | NOT_STARTED | `analytical-operating-system`, `mckinsey-consultant` | Data-room index, outside-in registers, source model, management materials | `diligence/data-room-validation.md`, updated shared registers | Every PRE-stage thesis-critical claim is confirmed, weakened, contradicted, or still GAP | TBD |
| Post-data-room | DR2. Confirmed NTB registry and driver tree | NOT_STARTED | `ntb-diligence`, `driver-tree` | Data-room validation, source model, KPI exports, preliminary NTBs and driver tree | Updated `diligence/ntb-registry.md`, updated `diligence/driver-tree.md` | Load-bearing NTBs/drivers have company-specific evidence states and no hidden T4 base-case dependency | TBD |
| Post-data-room | DR3. Deal workbook / model bridge | NOT_STARTED | `financial-model-builder`, `deal-workbook-builder` | Source financial model, P&L, KPI exports, NTB registry, driver tree, data-room files | `diligence/deal-workbook.xlsx`, `diligence/workbook-quality-check.md` | Workbook is formula-linked to the source model or documented inputs; no hardcoded model-chain cells; formula errors and broken links are zero | TBD |
| Post-data-room | DR4. GTM metrics diagnostic | NOT_STARTED | `gtm-metrics-analyzer` | CRM exports, ARR/MRR waterfall, pipeline, bookings, retention, S&M spend, sales headcount, driver tree, deal workbook | `diligence/gtm-metrics-diagnostic.xlsx`, `diligence/gtm-metrics-summary.md` | User-provided inputs are separated from derived calculations; missing GTM inputs are explicit; workbook formulas resolve without errors | TBD |
| Post-data-room | DR5. KPI tree | NOT_STARTED | `kpi-tree-builder` | Driver tree, deal workbook, GTM diagnostic, operating metric exports, data-room files, open data requests | `diligence/kpi-tree.md` | Each thesis-critical driver maps to KPI definition, formula, source, owner, cadence, threshold, and action; unavailable data is logged as a blocker | TBD |
| Post-data-room | DR6. Boundability | NOT_STARTED | `boundability` | NTB registry, driver tree, deal workbook, GTM diagnostic, KPI tree, pre-mortem / failure modes, open issues | `diligence/boundability.md` | Underwriting actions map to model, price, leverage, docs/structure, and operating plan; driver-tree HALT cannot be overridden | TBD |
| Post-data-room | 6. IC memo draft | NOT_STARTED | `ic-memo`, `executive-summary-writer`, `writing-style`, current Claude/Codex path; n8n IC memo workflow is placeholder until rebuilt | Evidence spine, NTB registry, driver tree, deal workbook, GTM diagnostic, KPI tree, boundability, open issues | `ic-memo/draft/*.md`, updated claim ledger and number register | Memo uses only registered claims; GAPs remain visible; recurring numbers reconcile | TBD |
| Post-data-room | 7. Adversarial memo QA | NOT_STARTED | `claim-scrutinizer`, `red-team`, `pre-mortem`, `boundability` | IC memo draft, claim ledger, open issues, driver tree | `ic-memo/iteration/pass2-claim-scrutinizer.md`, `pass3-red-team.md`, `pass4-pre-mortem.md`, `pass4c-boundability.md` | Zero unaddressed KILL claims; every red/yellow issue has disposition and owner | TBD |
| Post-data-room | 8. Production and doc QA | NOT_STARTED | `pattern-docx`, `pattern-investment-pptx`, `doc-quality-checker` | QA-cleared memo/deck source, Pattern template, source footnotes | `ic-memo/final-output.docx`, optional PPTX, `ic-memo/doc-quality-check.md` | Zero critical format, source, number, or artifact-language issues | TBD |
| Post-data-room | 9. Cross-output release review | NOT_STARTED | `new-deal-pipeline/orchestrator.md`, `analytical-operating-system`, Gold Standard Queue | All deliverables, shared registers, n8n run register, QA passes | `deal-pack-summary.md`, final process tracker update, queue release note | Same market definition, competitor set, moat verdict, open issues, and key numbers across outputs; queue completion is justified | TBD |

## Required Artifact Checklist

| Artifact | Required? | Status | Notes |
|---|---|---|---|
| `shared/process-tracker.md` | Yes | NOT_STARTED | Created from this template |
| `shared/run-log.md` | Yes | NOT_STARTED | Chronological record of phase starts, completions, and decisions |
| `shared/n8n-run-register.md` | Yes if any n8n workflow is used | NOT_STARTED | Execution ID, queue row, output folder, status, and handoff for every automation run |
| `shared/queue-contract-check.md` | Yes if using Gold Standard Queue | NOT_STARTED | Snapshot of columns A:M, eligibility, blockers, and release status |
| `shared/dispatch-packet.md` | Yes after deal-intelligence dispatch | NOT_STARTED | Deal-master prompt, WorkDir, overnight output contract, required deliverables |
| `shared/data-room-access-log.md` | Yes once data room is requested | NOT_STARTED | Access status, request date, granted date, owner, and missing access blockers |
| `shared/data-room-index.md` | Yes before post-data-room work | NOT_STARTED | Every data-room file, folder, owner/date/type/source tag, mapped request, and evidence use |
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
| `diligence/data-room-request-list.md` | Yes before full data-room access | NOT_STARTED | Exact company-specific data asks mapped to NTBs, drivers, GTM metrics, model needs, and kill triggers |
| `diligence/data-room-validation.md` | Yes after data-room access | NOT_STARTED | Reconciles data-room evidence against pre-data-room claims and updates registers |
| `diligence/deal-workbook.xlsx` | Yes when source model or company financial data is available | NOT_STARTED | Formula-linked workbook with driver tree, KPI tree, NTB registry, and MOIC bridge |
| `diligence/workbook-quality-check.md` | Yes if deal workbook is built | NOT_STARTED | Formula integrity, source-link, broken-link, and hardcode check |
| `diligence/gtm-metrics-diagnostic.xlsx` | Yes when SaaS / sales-led GTM data is available | NOT_STARTED | ARR funnel, retention, pipeline health, sales efficiency, productivity, and missing-input register |
| `diligence/gtm-metrics-summary.md` | Yes if GTM diagnostic is built | NOT_STARTED | Key findings, missing inputs, derived metrics, and IC memo implications |
| `diligence/kpi-tree.md` | Yes; defer only with documented data blocker | NOT_STARTED | Maps drivers to measurable operating inputs, owners, cadences, thresholds, and actions |
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
| Data-room files not indexed | 0 | 0 before post-data-room work | NOT_STARTED |
| Data-room files not mapped to request / source use | 0 | 0 before final release | NOT_STARTED |
| Pre-data-room thesis-critical claims not re-tested against data-room evidence | 0 | 0 before IC memo draft | NOT_STARTED |
| Thesis-critical claims | 0 | All tagged | NOT_STARTED |
| Untagged thesis-critical claims | 0 | 0 | NOT_STARTED |
| `[GAP]` items affecting recommendation | 0 | 0 before CLEAR_TO_RELEASE | NOT_STARTED |
| Single-source dependencies | 0 | Explicitly disclosed | NOT_STARTED |
| Vendor or management claims used as proof | 0 | 0 | NOT_STARTED |
| Recurring numbers without source/date/scope | 0 | 0 | NOT_STARTED |
| Cross-output numeric conflicts | 0 | 0 | NOT_STARTED |
| Driver-tree load-bearing nodes without NTB mapping | 0 | 0 | NOT_STARTED |
| Driver-tree base-case nodes tagged T4 | 0 | 0 | NOT_STARTED |
| Deal workbook hardcoded model-chain cells | 0 | 0 | NOT_STARTED |
| Deal workbook formula errors or broken source links | 0 | 0 | NOT_STARTED |
| GTM diagnostic missing required fields without open-issue entry | 0 | 0 | NOT_STARTED |
| GTM diagnostic derived metrics without formula/source | 0 | 0 | NOT_STARTED |
| GTM diagnostic formula errors | 0 | 0 | NOT_STARTED |
| KPI tree nodes without formula/source/owner/cadence/action threshold | 0 | 0 | NOT_STARTED |
| Thesis-critical memo claims without NTB, driver, workbook, or KPI linkage | 0 | 0 | NOT_STARTED |
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
- [ ] Pre-data-room deliverables are complete or explicitly blocked before data-room work starts.
- [ ] `shared/data-room-index.md` exists before any post-data-room artifact is marked PASS.
- [ ] `diligence/data-room-validation.md` reconciles pre-data-room claims against company-specific evidence before the IC memo draft.
- [ ] Pre-IC thesis-validation outputs, if used, were rerun or re-tested against the actual IC memo draft.
- [ ] `diligence/driver-tree.md` exists and every load-bearing thesis claim maps to a causal driver.
- [ ] `diligence/deal-workbook.xlsx` exists if source financial data or a model is available; otherwise the blocker is logged in `shared/open-issues.md`.
- [ ] `diligence/workbook-quality-check.md` shows zero hardcoded model-chain cells, formula errors, and broken source links when a workbook is built.
- [ ] `diligence/gtm-metrics-diagnostic.xlsx` exists if SaaS / sales-led GTM data is available; otherwise missing GTM source tables are logged.
- [ ] GTM metrics used in the IC memo trace to uploaded inputs or derived formulas, not unsupported sales narratives.
- [ ] `diligence/kpi-tree.md` exists or is explicitly deferred with the missing data, owner, and decision impact logged.
- [ ] Every thesis-critical IC memo claim maps to at least one NTB, driver-tree node, data-room validation item, workbook assumption, GTM metric, or KPI-tree node.
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
