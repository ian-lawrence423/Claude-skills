# Claude Skills Library

Pattern's modular skill architecture for Claude. Each skill is a folder containing a `SKILL.md` file that instructs Claude on methodology, output format, and quality standards for a specific domain. Skills are loaded on-demand — Claude reads the relevant `SKILL.md` before executing any task in its domain.

**35 skills across 8 groups, one orchestration entry point, 5 functional layers, 3 multi-agent pipelines, and 8 generated reference documents.** Every formal output runs through at least two layers — usually three or four. Layers are not optional — skipping a layer produces a draft, not a deliverable.

> **Source of truth:** Root skill folders in this repo are the canonical authoring source. Packaged copies under grouped plugin folders must be synced from root before publishing. Update this README whenever skills are added, removed, repackaged, or promoted as workflow entry points.

> **Current inventory note:** The current repo has 35 canonical root skills, 25 packaged deal-intelligence skills, 3 multi-agent pipeline folders, and 8 generated reference documents. The top summary should be treated as stale if these counts diverge.

> **Reference docs:** Generated Word reference files in `docs/` are rebuilt from this repo with `docs/generate_claude_docs.py`. Do not hand-edit the DOCX files without also updating the Markdown/source generator.

---

## Start Here: Canonical Order

This repo has three different surfaces. They are not interchangeable:

| Surface | What It Is | Use It For | Source-of-Truth Rule |
|---|---|---|---|
| Root skill folders, for example `market-research/` | Canonical authoring copy for individual skills | Editing skill behavior and local skill loading | Edit here first |
| `plugins/deal-intelligence/skills/` | Packaged grouped plugin copy | Installing/running the full deal-intelligence bundle | Sync from root before publishing |
| Pipeline folders, for example `new-deal-pipeline/` | Multi-agent workflow instructions | Running a sequenced workflow across multiple skills | Orchestrators consume skills; they are not skills themselves |

If you are unsure what to run, use this order:

1. New deal or company research for a deal: `deal-master` -> `new-deal-pipeline/orchestrator.md` with `RESEARCH_MODE=gold_standard_end_to_end`.
2. IC memo only: use only when upstream research is already verified and current.
3. Non-deal market research only: `market-research`; do not use it as a shortcut for deal diligence.
4. Single artifact or analysis task: invoke the most specific root skill directly.
5. File output: run quality first, then `pattern-docx` or `pattern-investment-pptx`, then `doc-quality-checker`.

For every new deal, create `{WORK_DIR}/shared/process-tracker.md` from
`new-deal-pipeline/process-tracker-template.md` before research, diligence, or
memo drafting. The tracker is the control tower for phase order, required
skills/plugins, required docs, integrity gates, and next action.

Deletion rule: do not delete a folder just because it is not the primary route. First classify it as canonical skill, packaged copy, pipeline, generated artifact, or archive candidate.

For the full workflow map, stale-flow recommendations, and delete/archive candidates, see `docs/multi-agent-workflows.md`.

---

## 1. How Skills Fit Together

The skill library has one orchestration entry point and five functional layers. For deal workflows, start with `deal-master`; for standalone tasks, invoke the most specific skill directly.

0. **Deal Orchestration** → `deal-master` inventories existing work and routes to the right phase
1. **Analytical Method** → `mckinsey-consultant` frames the problem and governs methodology
2. **Evidence Control** → `analytical-operating-system` maintains evidence states, belief registers, Bayesian updates, and decision posture
3. **Research/Analysis** → gathers evidence, builds NTB-ready findings, confirms Gate 2 scorecard
4. **writing-style** → runs on all prose before any document code is written
5. **claim-scrutinizer** → redlines every material claim, checks IC memo structure (investment work)
6. **red-team** → adversarial pass on load-bearing pillars
7. **pre-mortem** → failure mode inventory with NTB mapping (IC/investment work)
8. **Document production** → generates the file using canonical template
9. **doc-quality-checker** → auto-runs after file delivery

> **Critical:** Never trigger a document production skill without running the quality layer first. A file produced without `writing-style` and `claim-scrutinizer` will fail the `doc-quality-checker` pass and require a full rebuild.

> **Full deal-pack quality contract:** When the task is a new deal requiring market research, competitive assessment, and an IC memo, route through `deal-master` -> `new-deal-pipeline/orchestrator.md`. The pipeline applies `new-deal-pipeline/quality-contract.md`: thoroughness over speed, source-tagged claims, explicit arithmetic, MECE issue trees, no unsupported hyperbole, and visible `GAP` handling instead of plausible filler.

> **Process tracker standard:** Every full deal run must maintain `shared/process-tracker.md` from `new-deal-pipeline/process-tracker-template.md`. If the tracker is stale, the deal process is stale.

> **Repeatable deal prompt:** For checkpointed execution, use `docs/new-deal-gold-standard-prompt-sequence.md`. It is the operator prompt sequence for complete market research, competitive assessment, IC memo, and cross-output QA.

> **Source footnote standard:** Pattern DOCX outputs use true Word footnotes for thesis-critical sourcing: body `w:footnoteReference` runs mapped to `word/footnotes.xml`. Source notes start with `[F · H]`-style tags where type = fact / estimate / hypothesis and confidence = high / medium / low.

| Layer | Skills | What It Owns | When It Runs |
|---|---|---|---|
| **0 — Deal Orchestration** | `deal-master` | Existing-work inventory, deal state assessment, phase routing, belief-register initialization | Default entry point for full deal workflows |
| **1 — Analytical Method** | `mckinsey-consultant` | Problem structuring, MECE trees, frameworks, Pyramid Principle, Six Screening Questions | Always active for strategy or investment work |
| **1b — Evidence Control** | `analytical-operating-system` | Evidence-state tagging, belief registers, Bayesian updates, kill triggers, decision posture | Deal-master, IC memo, diligence, and investment thesis workflows |
| **2 — Research** | `market-research`, `ntb-diligence`, `ic-memo`, `competitive-moat-assessment`, `executive-summary-writer`, `driver-tree`, `tam-sam-som-calculator`, `statistics-fundamentals`, `finance-metrics-quickref`, `gtm-metrics-analyzer` | Evidence gathering, research workflow, deliverable architecture, metrics analysis | When research or a specific deliverable type is needed |
| **3 — Quality** | `writing-style` ⚙️, `claim-scrutinizer`, `red-team`, `pre-mortem`, `boundability` | Prose standards, claim testing, adversarial stress-testing, failure mode enumeration | During drafting (`writing-style`) and after draft (all others) |
| **4 — Production** | `pattern-docx`, `pattern-investment-pptx`, `diligence-ddr`, `financial-model-builder`, `executive-briefing`, `written-communication`, `giving-presentations` | Branded file output in correct format with header/footer/logo | Final step — after analytical and quality layers complete |
| **4b — QA** | `doc-quality-checker` ⚙️ | Brand compliance, formatting, internal consistency, draft artifact language check | Auto-runs after every Layer 4 file output |

---

## 2. Auto-Running Skills

These two skills execute on every relevant output **without being explicitly invoked**:

| Skill | Auto-Runs When... |
|---|---|
| `writing-style` | Any final or near-final formal output — memos, reports, investment theses, PPTX narrative text |
| `doc-quality-checker` | After any `pattern-docx` or `pattern-investment-pptx` file is produced |

All other skills are invoked by name when the task matches their trigger criteria.

---

## 3. Complete Skill Index

All 35 root skills organized by group. Invoke the most specific skill first; fall back to broader skills if needed.

### Strategy & Problem Solving

| Skill | Layer | What It Does | Triggers |
|---|---|---|---|
| `deal-master` | L0 — Deal Orchestration | Single entry point for deal intelligence: inventories existing work, loads core frameworks, initializes the belief register, and routes to the next phase | "run deal intelligence", "start this deal", "resume this IC memo", "where are we in diligence" |
| `mckinsey-consultant` | L1 — Analytical Method | Problem structuring, MECE trees, 7 strategy dimensions, Pyramid Principle, Six Screening Questions — canonical analytical method for strategy/investment work | Issue trees, MECE frameworks, structured diagnosis, storyline design |
| `analytical-operating-system` | L1b — Evidence Control | Evidence-state tagging, belief-register initialization, Bayesian updates, kill triggers, and PROCEED / REPRICE / PASS / RESOLVE FIRST decision posture | Deal-master, IC memo, diligence, investment thesis, active deal update |
| `market-research` | L2 — Research | Full research workflow: intake → brief → pyramid (L4→L1) → gold-standard report architecture → iteration loop. Full-mode standalone reports use `docs/market-research-gold-standard-guide.md` plus `market-research/references/gold-standard-report-template.md` | "conduct market research", "competitive landscape", "full analysis", "size a market" |
| `competitive-moat-assessment` | L2 — Research | 5-step moat evidence methodology: classify → existence test → strength rating → durability → verdict. Mandatory at L2b in all market research | "assess the moat", "how defensible is X", "moat depth", "durability of advantage" |
| `pre-mortem` | L3 — Quality | Assumes deal/project failed and works backward to enumerate every failure pathway. Maps failure modes to NTBs. Distinct from `claim-scrutinizer` — assumes the bull case is wrong | "pre-mortem this", "how does this fail", "war game", "stress test downside" |
| `red-team` | L3 — Quality | Adversarial review — constructs the strongest opposing case with evidence. 6-gate attack lenses. Produces a structured rebuttal, not a general critique | "red team this", "make the bear case", "argue against this", "steelman the opposition" |
| `claim-scrutinizer` | L3 — Quality | Seven-part claim test, assumption audit, derivative integrity. For investment docs: Six Screening Questions as lens + IC memo structure check (NTB registry, Gate 2 scorecard) | "scrutinize", "redline", "pressure-test", "poke holes in this", "is this IC-ready" |
| `boundability` | L3 — Quality | Tests geographic, segment, and product boundaries of a competitive advantage — where it holds vs. degrades. 6-module scoring, 5 disqualification gates | "where does the moat hold", "test the limits of this advantage", "boundary conditions" |
| `driver-tree` | L2 — Research | Decomposes investment thesis into causal driver tree — revenue, cost, capital, and competitive dynamics. Maps drivers to NTBs and MOIC outcomes | "build a driver tree", "decompose this thesis", "what drives MOIC here" |
| `tam-sam-som-calculator` | L2 — Research | Market sizing — TAM/SAM/SOM with bottoms-up and tops-down approaches, labeled assumptions (fact/estimate/hypothesis), and sensitivity analysis | "size the market", "TAM/SAM/SOM", "how big is this market", "market sizing" |
| `statistics-fundamentals` | L2 — Research | Applied statistics for investment and business analysis: regression interpretation, confidence intervals, A/B test validity, correlation vs. causation, common statistical errors | "is this statistically significant", "interpret this regression", "confidence interval" |

### Finance & Investment

> ⚠️ **Foundational rule:** Always load `financial-model-builder` first before invoking any other skill in this group. All downstream finance work builds on the canonical 3-tab model structure.

| Skill | Layer | What It Does | Triggers |
|---|---|---|---|
| `financial-model-builder` | L4 — Production | Builds canonical 3-tab operating model (Input Page, Financial Model Template, Output Tab) from source P&L/BS. 6+6 analysis (actuals + forecast). **Read first — foundational** | "build financial model", "3-tab model", "6+6 analysis", "turn this P&L into a model" |
| `deal-workbook-builder` | L4 — Production | Builds the formula-linked PE/M&A deal workbook: driver tree, KPI tree, NTB registry, and MOIC bridge chained to a source financial model | "build the deal workbook", "rebuild the driver tree", "link the NTB registry to the model", "fix the MOIC bridge" |
| `ic-memo` | L2 — Research | IC memo architecture: 10-section structure, three-gate structure (company quality → sector timing → investment attractiveness), kill criteria, scenario analysis, Pattern-branded DOCX output | "IC memo", "investment committee memo", "write up this deal", "deal memo" |
| `ntb-diligence` | L2 — Research | Standalone 4-phase NTB diligence, 2 checkpoints, MOIC sum tolerance ±15%. Evaluates whether growth is driven by genuine new customers vs. base recycling | "NTB diligence", "new-to-brand analysis", "customer acquisition quality", "cohort analysis" |
| `diligence-ddr` | L4 — Production | Generates or customizes Due Diligence Request Lists for PE buyout / M&A sell-side. Tailored by sector and business model | "DDR", "due diligence request list", "data room requests", "diligence checklist" |
| `finance-metrics-quickref` | L2 — Research | Quick-reference lookup for financial metric definitions, formulas, and benchmarks. Covers SaaS, PE, and general corporate finance | "what's the formula for", "define [metric]", "what's a good benchmark for" |
| `gtm-metrics-analyzer` | L2 — Research | Full GTM diagnostic workbook from uploaded source files. Calculates 48 derived metrics across 6 families (ARR funnel, pipeline, retention, efficiency, productivity, fiscal maturity). Produces 4-tab Excel output with inputs, formulas, and diagnostic summary | "build a GTM workbook", "analyze these GTM metrics", "calculate NDR from this data", "diagnostic on this ARR table", "board prep metrics" |

### Executive Leadership

| Skill | Layer | What It Does | Triggers |
|---|---|---|---|
| `executive-briefing` | L4 — Production | Executive-ready briefing documents: memos, one-pagers, board notes, C-suite briefings. Enforces BLUF structure and decision-oriented formatting | "memo", "board note", "one-pager", "C-suite briefing", "executive summary" |
| `executive-summary-writer` | L2 — Research | Writes two-page executive summaries using the canonical Company Overview, Product Offering, Market Dynamic, Business Model, Thesis, and Open Questions spine | "write an executive summary", "summarize for leadership", "draft the two-page summary" |
| `managing-up` | Interpersonal | Frameworks for executive relationship management, influencing leadership without authority, and navigating organizational dynamics | "how do I handle this with my boss", "managing up", "influencing leadership" |

### Communication & Deliverables

> **Brand rules:**
> - `pattern-investment-pptx`: **Wix Madefor Display** font, primary blue `#4285F4`, navy `#002060`
> - `pattern-docx`: **Wix Madefor Display** font, section headers `#4280F4`, subheaders `#3A00FD`, table headers `#0F4761`
> - The `pattern-docx` header contains the Pattern logo and gradient line — injected via Python patch, not docx-js

| Skill | Layer | What It Does | Triggers |
|---|---|---|---|
| `pattern-docx` | L4 — Production | Pattern-branded Word documents. Two-phase build: docx-js body + Python XML patch for header/footer/logo | Any Pattern memo, report, analysis, IC memo as Word doc |
| `pattern-investment-pptx` | L4 — Production | Institutional-grade investment decks: IC, PE, acquirer materials. 10×5.625" format | Investment deck, investor presentation, due diligence deck, M&A deck |
| `written-communication` | L4 — Production | Emails, memos, strategy documents, and announcements. Covers tone calibration, audience framing, structure, and edit passes | "write an email", "draft a memo", "help me communicate this", "write an announcement" |
| `giving-presentations` | L4 — Production | Talk track prep, slide deck narrative design, and presentation delivery coaching | "help me prep for this presentation", "talk track", "what's the narrative for this deck" |
| `competitive-landscape-deliverable` | L4 — Production | Converts a competitive landscape, market mapping, or M&A target spreadsheet into a board-ready Executive Deliverable. Preserves rating + key evidence (fidelity over brevity), verdict-led layout, Pattern brand styling. Handles Pattern n8n pipeline output (`Rating — McKinsey rationale`) | "make an executive view of this landscape", "build deliverable from competitor sheet", "summarize this competitive grid", "executive deliverable for [companies]" |
| `Deck_Refresh` | L4 — Production | Swaps numbers across an existing deck without rebuilding it. 4-phase: get data → find every instance (text, tables, chart axes, footnotes) → approval gate → execute. Never reformats; flags derived numbers (growth rates, share %) that may be stale. | "update the deck with Q4 numbers", "refresh the comps", "roll this forward", "change all the $485M to $512M" |
| `Deck_Check` | L4b — QA | IB-grade deck QC across 4 dimensions: number consistency (runs `extract_numbers.py` to normalize units and flag cross-slide mismatches), data-narrative alignment, language polish against IB standards, visual/formatting. Outputs Critical / Important / Minor findings. Read-only — no edits. | "check my numbers", "reconcile figures across slides", "is this client-ready", "proof this deck", "what am I missing before I send this out" |
| `writing-style` | L3 — Quality ⚙️ | 5-step prose self-review. Runs on **all** formal outputs before document production. Enforces claim tagging, inductive chain check, data gap flagging, prose standards | Auto-runs — do not invoke manually |
| `doc-quality-checker` | L4b — QA ⚙️ | Brand compliance QA gate. Auto-runs after every `pattern-docx` or `pattern-investment-pptx` output. Checks formatting, structural logic, table integrity, narrative flow | Auto-runs after Layer 4 production output |

### AI & Technology

| Skill | Layer | What It Does | Triggers |
|---|---|---|---|
| `vibe-coding` | L7 — AI | AI-assisted rapid prototyping — building functional tools, scripts, and apps without deep technical skills. Optimized for speed-to-working-artifact | "build this quickly", "prototype", "just make it work", "vibe code this" |
| `kpi-tree-builder` | L2 — Research | Decomposes a budget, forecast, or operating target into causal drivers and atomic inputs. Two modes: diligence (audit management budget credibility) and post-close (define tracking cadence with owners). Produces KPI tree + driver dictionary + tracking pack | "build a KPI tree", "break down this budget", "what should we track post-close", "audit this plan", "define operating metrics" |

### Meta / Workflow

| Skill | Layer | What It Does | Triggers |
|---|---|---|---|
| `skill-authoring-workflow` | L8 — Meta | Standards and process for creating or updating a skill without breaking conventions. Covers `SKILL.md` structure, trigger language, integration rules, quality checks | "create a new skill", "update this skill", "how should I structure this skill" |

---

## 4. Skill Invocation Priority

When multiple skills could apply, use this tie-breaking order:

| # | Rule | How to Apply |
|---|---|---|
| 1 | **Most specific first** | Prefer a narrow skill (e.g., `gtm-metrics-analyzer`) over a broad one (e.g., `mckinsey-consultant`) when the narrow one directly addresses the task |
| 2 | **Pattern-branded first** | For any output file, prefer `pattern-investment-pptx` over generic `pptx`; `pattern-docx` over generic Word |
| 3 | **Consulting OS default** | If no skill fits, apply the Default Mode 8-step framework from `agents.md` directly |

---

## 5. Pipelines

**Primary order:**

| Need | Start Here | Use This Pipeline | Do Not Use |
|---|---|---|---|
| Full deal package from research through IC memo | `deal-master` | `new-deal-pipeline/orchestrator.md` | Standalone/light research workflows; all deal research uses the full gold-standard chain |
| IC memo only, with verified current research already in hand | `deal-master` | `ic-memo-pipeline/orchestrator.md` | Any path that treats unverified n8n markdown as final research |
| Non-deal market research report only | `market-research` | `market-research-pipeline/orchestrator.md` only as a legacy/repair reference | Using standalone market research as a shortcut for a deal pack |

If two routes could work, use the broader route only when it produces an output you actually need.

Pipelines are multi-agent workflows composed of skills. They live in their own folders at the repo root alongside the skill folders. Unlike skills, pipelines are not loaded as a single `SKILL.md` — they are orchestrated by an `orchestrator.md` file that dispatches specialist agents in sequence.

| Pipeline | Folder | What It Produces | Mode Flags |
|----------|--------|-----------------|-----------|
| `new-deal-pipeline` | `new-deal-pipeline/` | Full new-deal pack: pre-data-room n8n intake/prefetch/dispatch -> shared evidence spine -> market research -> competitive assessment -> outside-in NTB / driver tree / data-room request list -> data-room gate -> post-data-room validation -> workbook/model bridge -> GTM metrics -> KPI tree -> boundability -> IC memo -> cross-output QA | `RESEARCH_MODE=gold_standard_end_to_end`; `RESUME_EXCEPTION`: none/resume_verified_outputs/repair_failed_phase; `SOURCE_STRICTNESS`: standard/strict |
| `ic-memo-pipeline` | `ic-memo-pipeline/` | Full 10-section IC memo: intake → market research → NTB diligence → driver tree → section drafts → 5 iteration passes → Pattern DOCX → QA | `NTB_MODE`: full/skip · `KPI_MODE`: full/skip |
| `market-research-pipeline` | `market-research-pipeline/` | Legacy standalone/repair research path. Not a deal research mode. | Use only outside deal workflows or to repair a failed full-chain component |

**new-deal-pipeline files:**

| File | Phase | Role |
|------|-------|------|
| `orchestrator.md` | all | Routes the full deal pack and enforces cross-output consistency |
| `quality-contract.md` | all | Mandatory source, MECE, arithmetic, anti-hyperbole, and claim-economy gate |
| `process-tracker-template.md` | all | Mandatory phase tracker for workflows, skills/plugins, docs, gates, blockers, and next actions |
| `competitive-assessment.md` | 3 | Standalone competitive assessment agent with moat proof and displacement paths |

**ic-memo-pipeline agent files:**

| File | Phase | Role |
|------|-------|------|
| `orchestrator.md` | — | Main orchestrator |
| `intake.md` | 1 | Structured intake + Six Screening Questions |
| `l4-market.md` | 2 | Market sizing + PESTLE + trends |
| `l3-customer.md` | 2 | Customer segments + JTBD + decision journey |
| `l2-competitive.md` | 2 | Competitor profiles + Porter's Five Forces + white space |
| `moat-assessment.md` | 2 | Competitive moat verdict per competitor |
| `ntb-diligence.md` | 3 | NTB registry + diligence plan (NTB_MODE=full) |
| `driver-tree.md` | 3b | MECE driver tree — NTB→node mapping, cascade scenarios |
| `draft-sections.md` | 4 | All 10 IC memo sections (SECTION_INDEX param) |
| `pass1-writing-style.md` | 5 | Claim tagging, inductive chains, artifact removal |
| `pass2-claim-scrutinizer.md` | 5 | Seven-part claim test |
| `pass3-red-team.md` | 5 | Adversarial attack pass |
| `pass4-pre-mortem.md` | 5 | Pre-mortem failure inventory + numeric reconciliation |
| `pass4c-boundability.md` | 5 | Boundability verdicts + underwriting actions |
| `output-docx.md` | 6 | pattern-docx body gen + template transplant |
| `kpi-tree.md` | 8 | Post-close KPI tree + 100-day plan (KPI_MODE=full) |

---

## 6. Gold-Standard Deliverable Guides

Use these one-off reference documents when the goal is the most thorough version of a major strategic deliverable.

| Guide | Source | DOCX |
|---|---|---|
| Market Research Gold Standard | `docs/market-research-gold-standard-guide.md` | `docs/Market_Research_Gold_Standard_Guide.docx` |
| IC Memo Gold Standard | `docs/ic-memo-gold-standard-guide.md` | `docs/IC_Memo_Gold_Standard_Guide.docx` |
| Competitive Assessment Gold Standard | `docs/competitive-assessment-gold-standard-guide.md` | `docs/Competitive_Assessment_Gold_Standard_Guide.docx` |
| Executive Summary Gold Standard | `docs/executive-summary-gold-standard-guide.md` | `docs/Executive_Summary_Gold_Standard_Guide.docx` |
| Strategic Diligence Gold Standard | `docs/strategic-diligence-gold-standard-guide.md` | `docs/Strategic_Diligence_Gold_Standard_Guide.docx` |

---

## 7. Adding a New Skill

Follow this checklist to add a new skill without breaking conventions:

1. Create a folder: `[skill-name]/` (kebab-case)
2. Write `SKILL.md` — invoke `skill-authoring-workflow` for structure and standards
3. Add the skill to `agents.md` Skill Directory under the appropriate group
4. Add an entry to this README under the correct group table
5. Commit and push — this README is the source of truth for what is deployed

---

## 8. Related Files

| File | Location | Purpose |
|---|---|---|
| `multi-agent-workflows.md` | `docs/` | Operator map for the three pipeline folders, when to use each, and stale-flow/archive candidates |
| `agents.md` | Repo root / OneDrive sync | Always-on operating layer — default mode, work-mode templates, full skill directory, file output rules |
| `README.md` | Repo root | Source of truth for deployed skills — skill index, invocation guide, architecture overview |
| `CHEATSHEET.md` | Repo root | Quick-reference: task→skill map, layer sequence, pipeline phase map, brand constants |
| `new-deal-pipeline/quality-contract.md` | Repo root | Mandatory evidence, MECE, arithmetic, anti-hyperbole, and claim-economy gate for full deal packs |
| `new-deal-pipeline/process-tracker-template.md` | Repo root | Copy to `shared/process-tracker.md` for every new deal before analysis starts |
| `docs/new-deal-gold-standard-prompt-sequence.md` | `docs/` | Repeatable prompt sequence for full market research, competitive assessment, IC memo, and cross-output QA |
| `pattern-docx/references/production-spec.md` | Repo root | Pattern DOCX implementation spec, including true Word footnotes and source-tag format |
| `Claude_Skills_README.docx` | `docs/` | Generated Pattern-branded Word version of this README |
| `Claude_Skills_CheatSheet_v2.docx` | `docs/` / OneDrive | Generated quick-reference card for common tasks, mandatory layers, pairings, and brand constants |
| `Claude_Skill_Library_External (Finance)_v6.docx` | `docs/` / OneDrive | Generated finance/investment reference: skill architecture, inventory, IC memo workflow, finance handoff rules |
| `Market_Research_Gold_Standard_Guide.docx` | `docs/` | Generated standalone guide for creating the most thorough market research report |
| `IC_Memo_Gold_Standard_Guide.docx` | `docs/` | Generated standalone guide for a full Pattern IC memo |
| `Competitive_Assessment_Gold_Standard_Guide.docx` | `docs/` | Generated standalone guide for competitive assessment and moat analysis |
| `Executive_Summary_Gold_Standard_Guide.docx` | `docs/` | Generated standalone guide for two-page executive summaries |
| `Strategic_Diligence_Gold_Standard_Guide.docx` | `docs/` | Generated standalone guide for NTB diligence and underwriting handoff |
| `market-research-gold-standard-guide.md` | `docs/` | Markdown source for the standalone market research guide |
| `ic-memo-gold-standard-guide.md` | `docs/` | Markdown source for the IC memo guide |
| `competitive-assessment-gold-standard-guide.md` | `docs/` | Markdown source for the competitive assessment guide |
| `executive-summary-gold-standard-guide.md` | `docs/` | Markdown source for the executive summary guide |
| `strategic-diligence-gold-standard-guide.md` | `docs/` | Markdown source for the strategic diligence guide |
| `generate_claude_docs.py` | `docs/` | Rebuilds the README, cheat sheet, finance library, and market research Word references |
| `MBB_METHODOLOGY.md` | `mckinsey-consultant/references/` | Full MBB 7-step methodology reference |
| `VALIDATION_FRAMEWORKS.md` | `mckinsey-consultant/references/` | Source validation, CRAAP scoring, triangulation standards |
