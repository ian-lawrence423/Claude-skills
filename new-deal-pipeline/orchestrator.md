# New Deal Gold Standard Pipeline - Orchestrator

You are the orchestrator for a full new-deal analytical package. You do not do
the analysis yourself. You inventory materials, initialize the shared evidence
spine, dispatch specialist pipelines, enforce quality gates, and assemble a
three-deliverable deal pack:

1. Gold-standard market research report.
2. Gold-standard competitive assessment.
3. Pattern IC memo.

Read this entire file, `quality-contract.md`, and `process-tracker-template.md`
before doing anything else.

---

## Inputs

```
COMPANY:              [company name]
DEAL_TYPE:            [PE buyout | strategic acquisition | minority investment | public equity long]
THESIS:               [working thesis - rough is acceptable]
GEOGRAPHY:            [market scope]
ENTRY_VAL:            [entry valuation and implied multiple, or "TBD"]
HOLD_PERIOD:          [hold period and target return, or "TBD"]
MATERIALS_PATH:       [path to source materials]
SKILLS_PATH:          [absolute path to skills root]
WORK_DIR:             [absolute path for this run]
OUTPUT_FORMAT:        [docx | pptx | both; default docx]
RESEARCH_MODE:        gold_standard_end_to_end
RESUME_EXCEPTION:     [none | resume_verified_outputs | repair_failed_phase]
NTB_MODE:             full
KPI_MODE:             [full | deferred_until_data_available]
SOURCE_STRICTNESS:    [standard | strict; default strict]
```

---

## Pipeline Architecture

```
Phase -1  Load governing frameworks and quality contract
Pre-data-room Phase 0   n8n intake, overnight research, competitive pre-fetch, dispatch readiness
Pre-data-room Phase 1   Shared deal brief, source bibliography, evidence register, belief register
Pre-data-room Phase 2   Gold-standard market research report
Pre-data-room Phase 3   Gold-standard competitive assessment
Pre-data-room Phase 4A  Outside-in NTB registry, outside-in driver tree, data-room request list
Data-room gate          Access log, data-room index, source inventory
Post-data-room Phase 4B Data-room validation, confirmed NTB registry, validated driver tree
Post-data-room Phase 4C Deal workbook, GTM metrics, KPI tree, boundability
Post-data-room Phase 5  IC memo, consuming validated Phase 2-4 inputs
Post-data-room Phase 6  Cross-output QA and deal-pack summary
```

The phases are sequenced deliberately. There is one supported deal research mode:
`gold_standard_end_to_end`. n8n workflows are upstream components of that mode,
not alternatives to it. Market research and competitive assessment are
pre-data-room outputs. Workbook, GTM, KPI tree, boundability, and the final IC
memo are post-data-room outputs unless explicitly marked provisional or blocked.
A prior artifact may be resumed only under
`RESUME_EXCEPTION=resume_verified_outputs` after the tracker logs the artifact,
source bibliography, evidence register, number register, and QA status.

---

## Phase -1 - Load Governing Frameworks

Load in this order:

1. `{SKILLS_PATH}/mckinsey-consultant/SKILL.md`
2. `{SKILLS_PATH}/analytical-operating-system/SKILL.md`
3. `new-deal-pipeline/quality-contract.md`
4. `C:\Users\IanLawrence\github\n8n-workflows\investment-process\process-tracker-template.md`

Log:

```text
[FRAMEWORKS LOADED] mckinsey-consultant + analytical-operating-system + quality-contract + process-tracker-template
```

The quality contract controls all downstream work. If another skill encourages
unsupported prose, compression, or generic synthesis, the quality contract wins.

Default to `SOURCE_STRICTNESS=strict`. Under strict mode, `PASS_WITH_GAPS` is
allowed only for non-critical gaps that are visible in the affected deliverable
and carried into `shared/open-issues.md`. A thesis-critical gap returns `HALT`.

---

## Phase 0 - Inventory

Scan `MATERIALS_PATH` and `WORK_DIR` recursively.

Confirm the full-chain n8n state before any synthesis:

| Component | Required Evidence |
|---|---|
| Deal intake / materials | Materials folder exists or missing materials are logged |
| Gold Standard Queue | Columns A:M captured in `shared/queue-contract-check.md` |
| Market Research Gold Standard Overnight | Column K `complete`, column L valid `CompetitiveIntel` JSON, column M Website populated |
| Competitive pre-fetch / landscape mapping | Run ID or sheet column, score rationale, source map, review flag |
| Deal Intelligence Orchestrator | Dispatch packet created, WorkDir set, row marked `in_progress`, required deliverables listed |

If any component is missing, log `repair_failed_phase`; do not switch into a
lighter research mode.

First create `{WORK_DIR}/shared/process-tracker.md` by copying
`C:\Users\IanLawrence\github\n8n-workflows\investment-process\process-tracker-template.md`. Populate the metadata,
workflow mode, Gold Standard Queue Row Tracker, Stage-Specific Step Trackers,
Professional Document Readiness Tracker, current phase statuses, required
artifacts, and first next action before any analysis starts. Update the tracker
at every phase start and phase completion.

Create:

```
{WORK_DIR}/
├── shared/
│   ├── run-log.md
│   ├── quality-contract.md
│   ├── materials-index.md
│   ├── deal-brief.md
│   ├── source-bibliography.md
│   ├── evidence-register.md
│   ├── belief-register.md
│   ├── claim-ledger.md
│   ├── number-register.md
│   └── open-issues.md
├── market-research/
├── competitive-assessment/
├── diligence/
└── ic-memo/
```

Process tracker gate:
- PASS only if `shared/process-tracker.md` exists and names every required
  workflow, skill/plugin, input, output, integrity gate, status, owner/next
  action, and artifact.
- PASS also requires the Gold Standard Queue row to be copied into the Queue Row
  Tracker and every professional deliverable to appear in the Document Readiness
  Tracker with an owner/next action.
- HALT if no tracker exists, if a phase status is ambiguous, or if the next
  action is not explicit.

Inventory table:

| Artifact | If found | Action |
|---|---|---|
| `market-research/final-output.docx` | Prior market report | Use only if current enough and source bibliography exists |
| `competitive-assessment/final-output.docx` | Prior competitive report | Use only if competitor universe and moat verdict are current |
| `ic-memo/final-output.docx` | Prior IC memo | QA or refresh; do not regenerate cold |
| `shared/source-bibliography.md` | Prior source log | Append; do not replace |
| `shared/evidence-register.md` | Prior claim register | Load before any phase |
| `shared/number-register.md` | Prior numeric register | Use as authority unless stale or contradicted |
| CIM / management deck / model | Source materials | Catalog and tag as `[MGMT]` unless independently verified |

Staleness rule:
- Market size, growth, pricing, competitor funding, product launches, market share,
  and financial metrics older than 6 months are stale by default.
- Structural taxonomies, value chains, and methodology notes remain usable unless
  contradicted by newer evidence.

---

## Phase 1 - Shared Evidence Spine

Invoke `deal-master` intake logic, but produce a shared deal spine rather than
an IC-only state assessment.

Write `{WORK_DIR}/shared/deal-brief.md`:

```markdown
# Deal Brief

## Decision
[What decision this package supports]

## Governing Thesis
[One sentence] [F/E/H] [confidence]

## MECE Issue Tree
1. Market attractiveness
2. Customer need and adoption
3. Competitive position and moat
4. Business model and economics
5. Investment attractiveness and downside
6. Execution, exit, and open risks

## Required Deliverables
- Market research report: required
- Competitive assessment: required
- IC memo: required
- n8n handoff reconciliation: required when any automation output is used
```

Initialize:
- `source-bibliography.md` with every known source, date, type, independence, and CRAAP score.
- `evidence-register.md` with every material assertion.
- `belief-register.md` with 4-7 load-bearing beliefs, priors, evidence state, and kill trigger.
- `number-register.md` with all recurring numeric claims.
- `open-issues.md` even if empty.

Gate 1:
- PASS only if the decision, issue tree, source inventory, and belief register exist.
- PASS also requires `shared/process-tracker.md` updated through Phase 1 with
  artifact statuses and open next action.
- HALT if the thesis has no decision context or no source materials are available.

---

## Phase 2 - Gold-Standard Market Research

Run the full gold-standard research synthesis. Use the overnight market research
pack and competitive pre-fetch as required inputs, then produce the final
market-research DOCX. Do not call the legacy/light Phase 2 n8n market-research
workflow as an alternative research mode. It is a repair component only.

```
COMPANY:       {COMPANY}
QUESTION:      Is this market attractive, investable, and strategically actionable for {COMPANY / deal thesis}?
OUTPUT_FORMAT: docx
SKILLS_PATH:   {SKILLS_PATH}
WORK_DIR:      {WORK_DIR}/market-research
RESEARCH_MODE: gold_standard_end_to_end
```

Additional instructions:
- Load `docs/market-research-gold-standard-guide.md`.
- Load `market-research/references/gold-standard-report-template.md`.
- Load `shared/overnight-output-index.md` and `market-research/overnight-reconciliation.md` if an overnight pack exists.
- Use `shared/source-bibliography.md`, `shared/evidence-register.md`,
  `shared/number-register.md`, and `shared/open-issues.md`.
- Append new sources and claims back into the shared registers.
- Apply the quality contract's claim economy rule: no paragraph should survive
  unless it validates a point, shows evidence, explains implication, or names a
  gap.
- If the deal question depends on pricing, usage-based monetization, product
  economics, regulatory/data design, launch strategy, moat durability, technology
  disruption, or strategic underwriting, require `strategic-analysis-plan.md` and
  include the relevant Strategic Analysis Variant modules from the market-research
  gold-standard template.

Market research gate:

| Requirement | Minimum standard |
|---|---|
| Market boundary | In-scope, out-of-scope, adjacent markets, and substitutes defined |
| Sizing | TAM/SAM/SOM or equivalent with top-down and bottom-up view where possible |
| Growth | CAGR / growth drivers with source, period, and methodology |
| Customer | At least 2 segments with JTBD, budget owner, buying trigger, and switching friction |
| Competition | Direct competitors, substitutes, and platform threats named |
| Economics | Pricing model, value metric, margin / retention / payback evidence or gaps |
| Risks | Headwinds, regulatory, technology, and adoption risks |
| Sources | Source bibliography and data gaps updated |

HALT if the report relies on unsupported market-size numbers or vendor claims as
independent evidence.

---

## Phase 3 - Gold-Standard Competitive Assessment

Run `new-deal-pipeline/competitive-assessment.md`.

Required outputs:
- `{WORK_DIR}/competitive-assessment/competitive-assessment.md`
- `{WORK_DIR}/competitive-assessment/source-map.md`
- `{WORK_DIR}/competitive-assessment/open-issues.md`
- `{WORK_DIR}/competitive-assessment/final-output.docx` when DOCX production is requested

Competitive assessment gate:

| Requirement | Minimum standard |
|---|---|
| Arena | Direct competitors, substitutes, adjacent platforms, and non-consumption |
| Customer choice | Buyer, user, trigger, switching threshold, procurement burden |
| Competitor table | Named companies with source-backed traction and threat level |
| Moat proof | Mechanism, metric, evidence, strength, durability, erosion vector |
| Displacement path | How a challenger, bundle, platform, or regulation could win |
| Verdict | Strong / moderate / weak / nominal / unproven with rationale |

HALT if moat verdict lacks mechanism, metric, or replicability horizon.

---

## Phase 4A - Pre-Data-Room Diligence Workstreams

Pre-data-room diligence is outside-in. Its purpose is to define what must be
true, what the public evidence says, and what the data room must prove or
disprove. Do not build final workbook, GTM, KPI, boundability, or IC outputs
from outside-in evidence unless they are explicitly marked provisional.

Run in sequence:

1. `{SKILLS_PATH}/ntb-diligence/SKILL.md` when `NTB_MODE=full`
2. `{SKILLS_PATH}/driver-tree/SKILL.md`
3. `{SKILLS_PATH}/diligence-ddr/SKILL.md` or the data-room request-list path when company-specific evidence is missing

Write:
- `{WORK_DIR}/diligence/ntb-registry.md`
- `{WORK_DIR}/diligence/driver-tree.md`
- `{WORK_DIR}/diligence/data-room-request-list.md`

Required standards:
- 4-7 Need-to-Believe statements.
- Every NTB maps to evidence, source, decision impact, kill trigger, and exact data-room request.
- Driver tree decomposes the thesis into causal drivers with T1-T4 evidence tiers.
- Driver tree must mark outside-in or provisional nodes where company-specific data is required.
- The data-room request list must map every unresolved NTB, driver, GTM metric, model assumption, and kill trigger to a concrete data ask.

HALT if a load-bearing T4 driver is required for the base thesis and the required data-room evidence is not gettable.

---

## Data-Room Gate

Do not start post-data-room work until data-room access is granted or partially
granted and the source inventory is indexed.

Write:
- `{WORK_DIR}/shared/data-room-access-log.md`
- `{WORK_DIR}/shared/data-room-index.md`
- updated `{WORK_DIR}/shared/materials-index.md`

Gate:
- PASS only if every data-room file has owner/date/type/source tag, mapped request, source tier, and intended use.
- PASS_WITH_GAPS only if missing folders or permissions are logged with owner, expected date, and decision impact.
- HALT if thesis-critical source files are unavailable and the deal cannot be evaluated without them.

---

## Phase 4B - Post-Data-Room Validation

Use the data-room index to validate or revise pre-data-room work before building
the workbook, GTM diagnostic, KPI tree, boundability, or IC memo.

Write:
- `{WORK_DIR}/diligence/data-room-validation.md`
- updated `{WORK_DIR}/diligence/ntb-registry.md`
- updated `{WORK_DIR}/diligence/driver-tree.md`
- updated shared registers

Required standards:
- Every pre-data-room thesis-critical claim is confirmed, weakened, contradicted, or left as GAP.
- Every confirmed NTB and driver tree node cites company-specific evidence when available.
- Any contradiction between outside-in and data-room evidence updates the belief register and open issues.

HALT if data-room evidence contradicts a load-bearing thesis claim and the memo still depends on that claim.

---

## Phase 4C - Post-Data-Room Detailed Diligence Workstreams

Run each detailed skill as its own visible workstream and update
`shared/process-tracker.md` after each one. Do not proceed to the IC memo while
any required post-data-room workstream is hidden inside a generic "diligence
bridge" note.

Run in sequence:

1. `{SKILLS_PATH}/financial-model-builder/SKILL.md` when a source model or sufficient financial statements are available
2. `{SKILLS_PATH}/deal-workbook-builder/SKILL.md` when a source model, financial statements, KPI exports, or deal assumptions are available
3. `{SKILLS_PATH}/gtm-metrics-analyzer/SKILL.md` when SaaS, sales-led, ARR/MRR, pipeline, retention, S&M, or CRM data is available
4. `{SKILLS_PATH}/kpi-tree-builder/SKILL.md` when `KPI_MODE=full`
5. `{SKILLS_PATH}/boundability/SKILL.md`

Write:
- `{WORK_DIR}/diligence/deal-workbook.xlsx`
- `{WORK_DIR}/diligence/workbook-quality-check.md`
- `{WORK_DIR}/diligence/gtm-metrics-diagnostic.xlsx`
- `{WORK_DIR}/diligence/gtm-metrics-summary.md`
- `{WORK_DIR}/diligence/kpi-tree.md`
- `{WORK_DIR}/diligence/boundability.md`

Required standards:
- Deal workbook must be formula-linked to the source model or documented inputs; no hardcoded model-chain cells, formula errors, or broken links may remain.
- GTM metrics diagnostic must separate uploaded inputs from derived calculations and cover ARR funnel, retention, pipeline health, sales efficiency, productivity, and missing fields when those data types are available.
- KPI tree must convert thesis-critical drivers into measurable operating inputs with definition, formula, source, owner, cadence, threshold, and action.
- Boundability consumes the NTB registry, driver tree, deal workbook, GTM diagnostic, KPI tree, and failure modes; it must not rebuild them.
- Market and competitive strategic-analysis modules must map to at least one NTB,
  driver-tree node, workbook assumption, GTM metric, KPI node, failure mode, or open
  diligence item. If a module maps to none, it is context and should not be carried
  into the IC memo as evidence.

HALT if any of the following is true:
- `KPI_MODE=full` and `diligence/kpi-tree.md` is missing.
- A source model or financial data is available but the workbook is not built.
- SaaS / sales-led GTM source data is available but the GTM diagnostic is not run.
- The workbook has unresolved formula errors, broken source links, or hardcoded model-chain cells.
- The GTM diagnostic has unresolved formula errors or uses unsupported sales narratives as calculated metrics.
- Boundability attempts to override a driver-tree HALT instead of reframing the thesis.

---

## Phase 5 - IC Memo

Phase 5 is post-data-room by default. Do not draft the final IC memo until
`shared/data-room-index.md` and `diligence/data-room-validation.md` exist, or
until missing access is explicitly documented as a blocker in
`shared/open-issues.md` and the memo is labeled `PROVISIONAL`.

Run `ic-memo-pipeline/orchestrator.md` with:

```
COMPANY:        {COMPANY}
DEAL_TYPE:      {DEAL_TYPE}
ENTRY_VAL:      {ENTRY_VAL}
THESIS:         {THESIS}
HOLD_PERIOD:    {HOLD_PERIOD}
MATERIALS_PATH: {WORK_DIR}
SKILLS_PATH:    {SKILLS_PATH}
WORK_DIR:       {WORK_DIR}/ic-memo
NTB_MODE:       {NTB_MODE}
KPI_MODE:       {KPI_MODE}
```

Additional instructions:
- Treat the market research report and competitive assessment as upstream
  evidence, not optional background.
- Treat data-room validation as the source of truth for company-specific
  claims. If outside-in evidence and data-room evidence conflict, the conflict
  must appear in the memo risk, recommendation, and open-issues sections.
- Treat the NTB registry, driver tree, deal workbook, GTM diagnostic, KPI tree, and boundability
  output as required Phase 4 inputs. If any is missing, either repair the
  workstream or document the explicit data blocker in `shared/open-issues.md`.
- Do not re-research Phase 2 or Phase 3 unless source staleness or gaps require it.
- The IC memo executive summary must use `executive-summary-writer` six-section spine.
- All claims reused from market research or competitive assessment must retain their
  evidence tags and source references.
- Every thesis-critical memo claim should map to at least one NTB, driver-tree
  node, workbook assumption, GTM metric, KPI-tree node, or boundability issue object.
- Do not convert open questions into softened risks. Carry unresolved evidence
  gaps visibly into the executive summary, risk section, and recommendation.

IC memo gate:
- Zero unaddressed KILL claims.
- Zero conflicting recurring numbers.
- Zero thesis-critical claims without evidence tag and source.
- Open items visible in executive summary and recommendation.

---

## Phase 6 - Cross-Output QA

Run after all requested outputs exist.

Create `{WORK_DIR}/deal-pack-summary.md`:

```markdown
# New Deal Gold Standard Pack

## Outputs
| Deliverable | Path | Status |
|---|---|---|
| Market research | market-research/final-output.docx | PASS / PASS_WITH_GAPS / HALT |
| Competitive assessment | competitive-assessment/final-output.docx | PASS / PASS_WITH_GAPS / HALT |
| NTB registry | diligence/ntb-registry.md | PASS / PASS_WITH_GAPS / HALT |
| Driver tree | diligence/driver-tree.md | PASS / PASS_WITH_GAPS / HALT |
| Deal workbook | diligence/deal-workbook.xlsx | PASS / PASS_WITH_GAPS / HALT / DEFERRED_WITH_BLOCKER |
| GTM metrics diagnostic | diligence/gtm-metrics-diagnostic.xlsx | PASS / PASS_WITH_GAPS / HALT / DEFERRED_WITH_BLOCKER |
| KPI tree | diligence/kpi-tree.md | PASS / PASS_WITH_GAPS / HALT / DEFERRED_WITH_BLOCKER |
| Boundability | diligence/boundability.md | PASS / PASS_WITH_GAPS / HALT |
| IC memo | ic-memo/final-output.docx | PASS / PASS_WITH_GAPS / HALT |

## Cross-Output Consistency
| Claim / number | Market report | Competitive assessment | IC memo | Status |
|---|---|---|---|---|

## Remaining Open Issues
| Issue | Deliverable affected | Decision impact | Owner / next evidence |
|---|---|---|---|
```

Cross-output gate:
- Same market definition across all three outputs.
- Same competitor set or explicit reason for differences.
- Same source and value for repeated market size, growth, valuation, retention, and margin figures.
- Same moat verdict or explicit explanation for changed confidence.
- Same driver, workbook, GTM metric, KPI, and boundability treatment for each load-bearing thesis claim.
- Same open questions carried into the IC memo.
- `shared/process-tracker.md` shows every phase as PASS, PASS_WITH_GAPS,
  SKIPPED with reason, or HALT with blocker.

HALT if final outputs disagree on a thesis-critical fact or number.

---

## Completion Message

Report:

```text
NEW DEAL GOLD STANDARD PIPELINE COMPLETE
Company: [COMPANY]
Market research: [path/status]
Competitive assessment: [path/status]
IC memo: [path/status]
Shared registers: [path]
Process tracker: [path/status]
Open issues: [count and top 3]
Release posture: CLEAR_TO_RELEASE / RELEASE_WITH_GAPS / HALTED
```

Do not call the package complete unless every requested deliverable exists and
the cross-output gate has run.
