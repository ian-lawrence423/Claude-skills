# Claude Skills Library

Pattern's modular skill architecture for Claude. Each skill is a folder containing a `SKILL.md` file that instructs Claude on methodology, output format, and quality standards for a specific domain. Skills are loaded on-demand — Claude reads the relevant `SKILL.md` before executing any task in its domain.

> **Source of truth:** This README reflects the folders in [`ian-lawrence423/Claude-skills`](https://github.com/ian-lawrence423/Claude-skills). Update this file whenever skills are added or removed from the repo.

---

## How Skills Work

Skills encode hard-won constraints that Claude's training alone doesn't guarantee: brand specs, analytical methodology, quality gates, and output formatting rules. Claude reads the skill before writing any code, producing any file, or running any analysis.

**Auto-running skills** execute on every relevant output without being explicitly invoked:

| Skill | Auto-runs when... |
|---|---|
| `writing-style` | Any final/near-final formal output — memos, reports, investment theses, PPTX narrative text |
| `doc-quality-checker` | After any `pattern-docx` or `pattern-investment-pptx` file is produced |

All other skills are invoked by name when the task matches their trigger criteria.

---

## Full Skill Index (A–Z)

All 28 skills currently in the repo, alphabetically.

---

### `boundability`
Defines and tests the boundaries of a business's competitive advantage — where the moat holds, where it degrades, and what would cause it to collapse. Useful for investment diligence and competitive positioning work.

**Triggers:** "where does the moat hold", "test the boundaries of this advantage", "how defensible is this"

---

### `claim-scrutinizer`
Adversarial MECE redline of investment memos, IC decks, and strategy documents. Produces structured **KILL / WOUND / EXPOSE** verdicts with CRAAP scoring, derivative integrity checks, and logic tree analysis. For IC memos, applies the Six Screening Questions as the primary analytical lens. Always produces a redline output — never a general summary.

**Triggers:** "redline", "scrutinize", "pressure-test", "poke holes in this", "is this IC-ready", "check the logic", "fact-check this deck"

---

### `competitive-moat-assessment`
Structured assessment of a company's competitive moat: moat type classification (network effects, switching costs, cost advantages, intangibles, efficient scale), depth, durability, and erosion risk. Goes deeper than a generic competitive analysis — focuses specifically on advantage sustainability.

**Triggers:** "assess the moat", "how defensible is X", "competitive advantage analysis", "moat depth", "durability of advantage"

---

### `diligence-ddr`
Generates or customizes a Due Diligence Request List (DDR) for PE buyout or M&A sell-side transactions. Full DDR generation from scratch given a company description, and targeted customization to a specific business model, sector, and deal context.

**Triggers:** "DDR", "due diligence request list", "data room requests", "diligence checklist", "I need a DDR for [company]"

---

### `doc-quality-checker`
⚙️ **Auto-runs after `pattern-docx` or `pattern-investment-pptx` output.**

QA pass on Pattern Word docs and Pattern investment PPTX decks. Checks brand formatting, content quality, structural logic, table integrity, header/footer, page numbers, and narrative flow. Always produces a severity-rated inline issue list with exact locations. Never auto-fixes.

**Manual triggers:** "check this", "QA this", "proof this", "is this ready"

---

### `executive-briefing`
Produces executive-ready briefing documents: memos, one-pagers, board notes, and C-suite briefings. Enforces BLUF structure, three-level hierarchy max, and decision-oriented formatting.

**Triggers:** "memo", "board note", "one-pager", "C-suite briefing", "executive summary", "briefing doc"

---

### `executive-summary-writer`
Writes tight, decision-ready executive summaries from longer documents or analyses. Enforces strict length discipline and inductive structure — conclusion first, evidence second.

**Triggers:** "write an executive summary", "summarize this for leadership", "condense this into an exec summary"

---

### `finance-metrics-quickref`
Quick-reference lookup for financial metric definitions, formulas, and benchmarks. Covers SaaS, PE, and general corporate finance metrics.

**Triggers:** "what's the formula for", "define [metric]", "what's a good benchmark for", "how do I calculate"

---

### `financial-model-builder`
⚠️ **Read first before any other finance skill.**

Builds the canonical 3-tab operating model (Input Page, Financial Model Template, Output Tab) from a source P&L/Balance Sheet. All downstream finance skills assume this structure exists.

**Triggers:** "build financial model", "3-tab model", "6+6 analysis", "go-forward analysis", "turn this P&L into a model", "model this out", "build the pattern template model"

---

### `giving-presentations`
Talk track prep, slide deck narrative design, and presentation delivery coaching. Covers structuring a compelling narrative, anticipating audience questions, and landing key messages under time pressure.

**Triggers:** "help me prep for this presentation", "talk track", "how do I pitch this", "what's the narrative for this deck", "presentation coaching"

---

### `having-difficult-conversations`
Framework for navigating high-stakes interpersonal conversations: hard feedback, performance discussions, co-ownership framing for sensitive issues, and escalations. Produces talk tracks, not just advice.

**Triggers:** "how do I say this to them", "help me prepare for a hard conversation", "feedback delivery", "performance conversation", "how do I raise this with [person]"

---

### `ic-memo`
Produces Pattern-standard IC (Investment Committee) memos. Enforces the three-gate structure (company quality → sector timing → investment attractiveness), kill criteria, scenario analysis, and Pattern-branded DOCX output.

**Triggers:** "IC memo", "investment committee memo", "write up this deal", "IC write-up", "deal memo"

---

### `managing-up`
Frameworks for executive relationship management, influencing leadership without authority, and navigating organizational dynamics. Covers how to frame issues, build credibility, and drive decisions upward.

**Triggers:** "how do I handle this with my boss", "managing up", "executive relationship", "influencing leadership", "navigating org politics"

---

### `market-research`
Full market research project workflow — from brief through final deliverable. Hypothesis-driven methodology: research brief → pyramid analysis (Market → Customer → Competitive → Company) → source bibliography → report architecture → final DOCX or PPTX.

Integrates `mckinsey-consultant` (analytical method), `writing-style` (prose discipline), `claim-scrutinizer` (logic redline).

**Triggers:** "conduct market research", "build a research brief", "run a market analysis", "size a market", "competitive landscape", "full analysis"

---

### `mckinsey-consultant`
**The analytical OS. Load for any strategy, investment evaluation, or structured diagnosis.**

Governs all analytical methodology: McKinsey 7-step problem solving, MECE issue trees, Six Screening Questions for investments, Pyramid Principle, and all analytical modules (Porter's, SWOT, market sizing, positioning maps, value chain). Does not govern evidence gathering — that is `market-research`'s job. For financial modeling, use `financial-model-builder`. For file output, use `pattern-investment-pptx` or `pattern-docx`.

**Triggers:** issue trees, structured diagnosis, MECE frameworks, storyline design, McKinsey-style PPT, any strategy or PE/finance work mode

---

### `ntb-diligence`
New-to-brand (NTB) diligence framework — evaluates customer acquisition quality, new cohort behavior, and whether stated growth is driven by genuine new customer expansion vs. base recycling. Specific to e-commerce and marketplace businesses.

**Triggers:** "NTB diligence", "new-to-brand analysis", "customer acquisition quality", "cohort analysis", "is this growth real"

---

### `pattern-docx`
**Pattern-branded Word document generator.**

Encodes Pattern's exact typography (Wix Madefor Display), brand colors, header/footer with logo, section structure, table styles, and paragraph formatting. Two-phase build: docx-js body + Python patch for header/footer/logo injection.

**Brand spec:**
- Font: Wix Madefor Display
- Section headers: `#4280F4` | Subheaders: `#3A00FD` | Table headers: `#0F4761` | Body: `#000000`
- Header: Pattern logo + gradient line (Python-injected)

**Triggers:** any Pattern memo, report, analysis, IC memo, market research output as Word doc

---

### `pattern-investment-pptx`
**Pattern-branded investment-grade PowerPoint generator. Ian's primary deck skill.**

Encodes Pattern's full visual system: Wix Madefor Display font, 10×5.625" format, strict no-bold rule, financial tables, market sizing slides, EBITDA bridges, thesis sections.

**Brand spec:**
- Font: Wix Madefor Display | Slide: 10 × 5.625 inches
- Primary blue: `#4285F4` | Navy: `#002060` | Highlight row: `#D9E2F3`

**Triggers:** investment deck, investor presentation, due diligence deck, M&A deck, board deck, deal materials

---

### `pre-mortem`
Investment failure analysis. Assumes the deal has already failed and works backward to enumerate every failure pathway, diagnose the information state for each, and surface the data that would change the picture.

Distinct from `claim-scrutinizer`: scrutinizer tests whether the bull case is well-argued; pre-mortem assumes it is wrong.

**Triggers:** "pre-mortem this deal", "how does this fail", "what kills this deal", "war game this investment", "stress test the downside", "failure mode analysis"

---

### `red-team`
Adversarial review of investment theses, strategy documents, and market analyses. Actively constructs the strongest opposing case — not a list of risks, but a coherent counter-narrative with evidence. Produces a structured rebuttal, not a general critique.

**Triggers:** "red team this", "make the bear case", "argue against this", "what's the counter-thesis", "steelman the opposition"

---

### `saas-economics-efficiency-metrics`
CAC, LTV, payback period, Rule of 40, burn multiple, and capital efficiency ratios. Benchmarking against SaaS peers included.

**Triggers:** CAC/LTV analysis, payback period, Rule of 40, efficiency metrics, burn analysis

---

### `saas-revenue-growth-metrics`
Revenue, retention, NRR/GRR, ARR growth, churn, expansion, and logo retention. Covers metric definitions, calculation methodology, and benchmark ranges by stage and sector.

**Triggers:** NRR, GRR, ARR, churn, expansion revenue, retention analysis, revenue quality

---

### `skill-authoring-workflow`
Standards and process for creating or updating a skill without breaking existing conventions. Covers `SKILL.md` structure, trigger language, integration rules with adjacent skills, and quality checks before committing.

**Triggers:** "create a new skill", "update this skill", "I want to add a skill for", "how should I structure this skill"

---

### `statistics-fundamentals`
Applied statistics for investment and business analysis: regression interpretation, confidence intervals, sample size, A/B test validity, correlation vs. causation, and common statistical errors in business contexts.

**Triggers:** "is this statistically significant", "interpret this regression", "how do I size this test", "what's the confidence interval", "is this correlation meaningful"

---

### `tam-sam-som-calculator`
Market sizing — TAM/SAM/SOM with explicit assumptions, bottoms-up and tops-down approaches, and sensitivity analysis. Produces labeled estimates (fact / estimate / hypothesis) with stated methodology.

**Triggers:** "size the market", "TAM/SAM/SOM", "how big is this market", "market sizing"

---

### `vibe-coding`
AI-assisted rapid prototyping — building functional tools, scripts, and apps without deep technical skills. Optimized for speed-to-working-artifact over engineering purity.

**Triggers:** "build this quickly", "prototype", "just make it work", "I don't need it to be perfect", "vibe code this"

---

### `writing-style`
⚙️ **Auto-runs on all formal outputs.**

Governs prose quality, claim standards, and epistemic discipline via an explicit self-review pass after drafting. Enforces five-step review, inductive chain reasoning standard, and absolute/exclusivity term discipline. Runs alongside `mckinsey-consultant`, `market-research`, `diligence-ddr`, `pattern-docx`, and `pattern-investment-pptx`. Does not run on conversational responses or interim work.

---

### `written-communication`
Emails, memos, strategy documents, and announcements. Covers tone calibration, audience framing, structure, and edit passes for clarity and concision.

**Triggers:** "write an email", "draft a memo", "help me communicate this", "write an announcement", "message to leadership"

---

## Skill Invocation Priority

When multiple skills could apply:

1. **Most specific first** — prefer a narrow skill (e.g., `saas-revenue-growth-metrics`) over a broad one (e.g., `mckinsey-consultant`) when the narrow one directly addresses the task
2. **Pattern-branded first** — for any output file, prefer `pattern-investment-pptx` over generic PPTX; `pattern-docx` over generic Word
3. **Consulting OS default** — if no skill fits, apply the `agents.md` Default Mode 8-step framework directly

---

## Adding a New Skill

1. Create a folder: `[skill-name]/` (kebab-case)
2. Write `SKILL.md` — follow `skill-authoring-workflow` for structure and standards
3. Add the skill to `agents.md` Skill Directory under the appropriate group
4. Add an entry to this README in alphabetical order using the format above
5. Commit and push — this README is the source of truth for what's deployed

---

## Related Files

| File | Location | Purpose |
|---|---|---|
| `agents.md` | repo root / OneDrive | Always-on operating layer — default mode, work-mode templates, skill directory, file output rules |
| `MBB_METHODOLOGY.md` | `mckinsey-consultant/references/` | Full MBB 7-step methodology reference |
| `VALIDATION_FRAMEWORKS.md` | `mckinsey-consultant/references/` | Source validation, CRAAP scoring, triangulation standards |
