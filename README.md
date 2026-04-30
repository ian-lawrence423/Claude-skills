# Claude Skills Library

Pattern's modular skill architecture for Claude. Each skill is a folder containing a `SKILL.md` file that instructs Claude on methodology, output format, and quality standards for a specific domain. Skills are loaded on-demand — Claude reads the relevant `SKILL.md` before executing any task in its domain.

**28 skills across 8 groups and 4 functional layers, plus 2 multi-agent pipelines.** Every formal output runs through at least two layers — usually three or four. Layers are not optional — skipping a layer produces a draft, not a deliverable.

> **Source of truth:** This README reflects the folders in [`ian-lawrence423/Claude-skills`](https://github.com/ian-lawrence423/Claude-skills). Update this file whenever skills are added or removed from the repo.

---

## 1. How Skills Fit Together

The skill library has four functional layers. The mandatory sequence for any formal output:

1. **Analytical OS** → frames the problem, governs methodology, structures NTB registry (investment work)
2. **Research/Analysis** → gathers evidence, builds NTB-ready findings, confirms Gate 2 scorecard
3. **writing-style** → runs on all prose before any document code is written
4. **claim-scrutinizer** → redlines every material claim, checks IC memo structure (investment work)
5. **red-team** → adversarial pass on load-bearing pillars
6. **pre-mortem** → failure mode inventory with NTB mapping (IC/investment work)
7. **Document production** → generates the file using canonical template
8. **doc-quality-checker** → auto-runs after file delivery

> **Critical:** Never trigger a document production skill without running the quality layer first. A file produced without `writing-style` and `claim-scrutinizer` will fail the `doc-quality-checker` pass and require a full rebuild.

| Layer | Skills | What It Owns | When It Runs |
|---|---|---|---|
| **1 — Analytical OS** | `mckinsey-consultant` | Problem structuring, MECE trees, frameworks, claim labeling (F/E/H), Six Screening Questions | Always active for strategy or investment work |
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

All 30 skills organized by group. Invoke the most specific skill first; fall back to broader skills if needed.

### Strategy & Problem Solving

| Skill | Layer | What It Does | Triggers |
|---|---|---|---|
| `mckinsey-consultant` | L1 — Analytical OS | Problem structuring, MECE trees, 7 strategy dimensions, Pyramid Principle, Six Screening Questions — analytical OS for all strategy/investment work | Issue trees, MECE frameworks, structured diagnosis, storyline design |
| `market-research` | L2 — Research | Full research workflow: intake → brief → pyramid (L4→L1) → deep dives → draft → iteration loop. Integrates `mckinsey-consultant`, `writing-style`, `claim-scrutinizer`, `competitive-moat-assessment` | "conduct market research", "competitive landscape", "full analysis", "size a market" |
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
| `ic-memo` | L2 — Research | IC memo architecture: 10-section structure, three-gate structure (company quality → sector timing → investment attractiveness), kill criteria, scenario analysis, Pattern-branded DOCX output | "IC memo", "investment committee memo", "write up this deal", "deal memo" |
| `ntb-diligence` | L2 — Research | Standalone 4-phase NTB diligence, 2 checkpoints, MOIC sum tolerance ±15%. Evaluates whether growth is driven by genuine new customers vs. base recycling | "NTB diligence", "new-to-brand analysis", "customer acquisition quality", "cohort analysis" |
| `diligence-ddr` | L4 — Production | Generates or customizes Due Diligence Request Lists for PE buyout / M&A sell-side. Tailored by sector and business model | "DDR", "due diligence request list", "data room requests", "diligence checklist" |
| `finance-metrics-quickref` | L2 — Research | Quick-reference lookup for financial metric definitions, formulas, and benchmarks. Covers SaaS, PE, and general corporate finance | "what's the formula for", "define [metric]", "what's a good benchmark for" |
| `gtm-metrics-analyzer` | L2 — Research | Full GTM diagnostic workbook from uploaded source files. Calculates 48 derived metrics across 6 families (ARR funnel, pipeline, retention, efficiency, productivity, fiscal maturity). Produces 4-tab Excel output with inputs, formulas, and diagnostic summary | "build a GTM workbook", "analyze these GTM metrics", "calculate NDR from this data", "diagnostic on this ARR table", "board prep metrics" |

### Executive Leadership

| Skill | Layer | What It Does | Triggers |
|---|---|---|---|
| `executive-briefing` | L4 — Production | Executive-ready briefing documents: memos, one-pagers, board notes, C-suite briefings. Enforces BLUF structure and decision-oriented formatting | "memo", "board note", "one-pager", "C-suite briefing", "executive summary" |
| `executive-summary-writer` | L2 — Research | Compresses completed analysis into publication-ready executive summary. Four format variants: one-page memo, deck slide, briefing paragraph, multi-section | "write an executive summary", "summarize for leadership", "condense this" |
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

Pipelines are multi-agent workflows composed of skills. They live in their own folders at the repo root alongside the skill folders. Unlike skills, pipelines are not loaded as a single `SKILL.md` — they are orchestrated by an `orchestrator.md` file that dispatches specialist agents in sequence.

| Pipeline | Folder | What It Produces | Mode Flags |
|----------|--------|-----------------|-----------|
| `ic-memo-pipeline` | `ic-memo-pipeline/` | Full 10-section IC memo: intake → market research → NTB diligence → driver tree → section drafts → 5 iteration passes → Pattern DOCX → QA | `NTB_MODE`: full/skip · `KPI_MODE`: full/skip |
| `market-research-pipeline` | `market-research-pipeline/` | Standalone market research report: brief → L4→L3→L2 → themes → draft → iteration passes → Pattern DOCX | — |

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

## 6. Adding a New Skill

Follow this checklist to add a new skill without breaking conventions:

1. Create a folder: `[skill-name]/` (kebab-case)
2. Write `SKILL.md` — invoke `skill-authoring-workflow` for structure and standards
3. Add the skill to `agents.md` Skill Directory under the appropriate group
4. Add an entry to this README under the correct group table
5. Commit and push — this README is the source of truth for what is deployed

---

## 6. Related Files

| File | Location | Purpose |
|---|---|---|
| `agents.md` | Repo root / OneDrive sync | Always-on operating layer — default mode, work-mode templates, full skill directory, file output rules |
| `README.md` | Repo root | Source of truth for deployed skills — skill index, invocation guide, architecture overview |
| `CHEATSHEET.md` | Repo root | Quick-reference: task→skill map, layer sequence, pipeline phase map, brand constants |
| `Claude_Skills_CheatSheet.docx` | `docs/` / OneDrive | Legacy quick-reference card (see CHEATSHEET.md for current version) |
| `Claude_Skill_Library_External (Finance).docx` | `docs/` / OneDrive | Deep reference for PE/investment workflow: skill architecture, inventory, IC memo sequential prompts |
| `Claude_Skills_README.docx` | `docs/` | Pattern-branded Word version of this README |
| `MBB_METHODOLOGY.md` | `mckinsey-consultant/references/` | Full MBB 7-step methodology reference |
| `VALIDATION_FRAMEWORKS.md` | `mckinsey-consultant/references/` | Source validation, CRAAP scoring, triangulation standards |
