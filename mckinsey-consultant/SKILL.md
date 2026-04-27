---
name: mckinsey-consultant
description: |
  McKinsey-level structured consulting methodology for strategy, analysis, and problem-solving.
  This is the analytical OS — load it for any strategy work, investment evaluation, structured
  diagnosis, framework design, or McKinsey-style document. It owns all analytical methodology:
  7-step MBB problem solving, MECE issue trees, 7 strategy dimensions, Pyramid Principle,
  Six Screening Questions for investments, and all analytical modules (Porter's, SWOT, market
  sizing, positioning maps, value chain). It does NOT govern evidence gathering or source
  validation — that is market-research's job. For any task that requires original data collection
  (market sizing, competitive intelligence, customer research), invoke market-research on top of
  this skill. For financial modeling, use financial-model-builder. For PPTX/docx output, use
  pattern-investment-pptx or pattern-docx.
---

# McKinsey Consultant Skill — Analytical OS

This skill is the analytical engine for all strategy and investment work. It governs how you
think, structure arguments, apply analytical lenses, and synthesize to a recommendation. It does
not govern how you gather evidence — that is market-research's job, which runs on top of this
skill when original data collection is required.

Read this entire file before beginning any analysis.

---

## Skill Architecture — Where This Fits

```
mckinsey-consultant   ← YOU ARE HERE — analytical methodology, always active for strategy work
      │
      ├── market-research        ← invoke when evidence gathering is required
      │        └── pattern-investment-pptx / pattern-docx  ← invoke for file output
      │
      ├── financial-model-builder ← invoke for financial modeling tasks
      │
      └── claim-scrutinizer      ← invoke when stress-testing a completed document
```

**When to invoke market-research on top of this skill:**
- Task requires gathering new external data (market sizing, competitive landscape, customer research)
- Task involves a structured research project with a brief and deliverable
- Task requires source tier assignment, CRAAP validation, or triangulation of findings

**When this skill alone is sufficient:**
- Strategy memo, investment thesis, or board deck where evidence already exists
- Structuring an argument, building an issue tree, or designing a framework
- Synthesizing known information into a recommendation
- Any analytical task where the data is in hand and the job is to think clearly about it

---

## Core Methodology: MBB 7-Step Problem Solving

Apply these steps in order for any strategy or analysis request. Steps may compress for simple
questions but must never be skipped entirely — compress, don't omit.

### Step 1: Define the Problem
- Restate the problem in one sentence before doing anything else
- Separate the **presenting problem** (what was asked) from the **root problem** (what actually needs solving)
- Define what a good answer looks like — what decision will it enable?
- Flag scope boundaries: what is explicitly out of scope

### Step 2: Disaggregate into a MECE Issue Tree
- Break the problem into mutually exclusive, collectively exhaustive sub-questions
- Maximum 3–4 branches at each level; maximum 3 levels deep
- Each branch must be independently answerable with evidence
- Label the tree type: **diagnostic** (why is X happening?), **solution** (how do we achieve Y?), or **evaluative** (should we do Z?)

**Issue tree format:**
```
Core question
├── Branch 1: [Sub-question]
│   ├── Sub-branch 1a
│   └── Sub-branch 1b
├── Branch 2: [Sub-question]
│   ├── Sub-branch 2a
│   └── Sub-branch 2b
└── Branch 3: [Sub-question]
    ├── Sub-branch 3a
    └── Sub-branch 3b
```

**MECE check before proceeding:**
- [ ] No branch overlaps with another — each is independently addressable
- [ ] Together, all branches fully cover the problem — no material gaps
- [ ] Each branch is resolvable with available or gatherable evidence
- [ ] The logical structure holds: if all branches are true, the governing thesis follows

### Step 3: State the Day-1 Hypothesis
- Form a hypothesis immediately — do not wait for analysis to be complete
- Format: *"We believe [conclusion] because [primary reason], which means [implication]"*
- This is a working hypothesis, not a commitment — it will be refined
- Label it explicitly as **hypothesis (untested)**

### Step 4: Identify the 20/80 Drivers
- Of all branches in the issue tree, identify the 2–3 that drive 80% of the answer
- Prioritize analytical effort on these branches
- Explicitly state which branches are being deprioritized and why
- For deprioritized branches: accept directionally correct rather than rigorous

### Step 5: Conduct Analysis per Branch

For each prioritized branch, apply the relevant analytical lens:

| Branch Type | Analytical Lens |
|---|---|
| Market / external | Porter's Five Forces, market sizing (TAM/SAM/SOM), trend analysis |
| Customer | Segmentation, JTBD, willingness to pay, persona analysis |
| Competitive | Positioning map, competitive moat assessment, war gaming |
| Financial / economic | Unit economics, margin bridge, scenario modeling |
| Capability / internal | Capability gap analysis, build/buy/partner framework |
| Decision / trade-off | Decision matrix, weighted criteria, scenario tree |

**Claim labeling is mandatory on every finding:**
- **fact** — sourced, verifiable, cited
- **estimate** — reasoned from available data with stated assumptions
- **hypothesis** — untested, requires validation

**When evidence gathering is required at this step:** invoke market-research to execute
the relevant pyramid level(s). Market-research governs source selection, validation, and
triangulation. This skill governs what questions those sources need to answer.

### Step 6: Synthesize to a Recommendation
- State the recommendation in one sentence first — never bury it
- Structure the supporting argument as a **Pyramid**:
  - Top: Governing thought (the answer)
  - Middle: 3 key lines of reasoning (each independently sufficient)
  - Base: Evidence per line of reasoning
- For each recommendation include:
  - What this assumes (top 2–3 conditions that must hold)
  - What would change it (the single most likely reversal condition)

### Step 7: Define Next Steps
- Maximum 5 priority actions
- Each action: **Owner · Timeline · Expected impact · Leading indicator it's working**
- Sequence actions: quick wins (0–30 days) → structural moves (30–90 days) → long-term bets (90+ days)
- End with **So What?** — one sentence on the key takeaway or most urgent decision

---

## Seven Strategy Dimensions

When conducting strategy work, every analysis must address all seven dimensions. These define
the *analytical questions to answer* — not the data to collect (that is market-research's job).
Flag explicitly when data for a dimension is unavailable.

### Dimension 1: Market
- Size (TAM/SAM/SOM) with methodology stated (top-down and/or bottom-up)
- Growth rate and trajectory (expanding / maturing / consolidating)
- Structural trends: macro forces shaping the market over 3–5 years
- Tailwinds and headwinds — label each as near-term or structural
- Label all figures as fact / estimate / hypothesis

### Dimension 2: Customer
- Who has the problem and how acute it is
- JTBD framing: *"When [situation], the customer wants to [motivation] so they can [outcome]"*
- Distinguish functional job (what they're doing), emotional job (how they want to feel), social job (how they want to be perceived)
- Willingness to pay — established, inferred, or unknown
- Segment prioritization: which segment to win first and why

### Dimension 3: Economics
- Business model unit economics: gross margin, CAC/LTV relationship, payback period
- Whether economics are attractive, structurally challenged, or unproven
- Key margin lever — the single biggest driver of economics improvement
- Comparison to industry benchmark where available (label as estimate if interpolated)

### Dimension 4: Competition
- Name and assess the top 3–5 competitors — not "many players exist"
- For each: sustainable advantage, key weakness, and strategic trajectory
- Positioning map: where white space exists relative to incumbents
- Realistic displacement path: what it would actually take to take share
- Moat assessment: network effects / switching costs / scale / IP / brand

### Dimension 5: Capability
- What it takes to win: the 3–4 capabilities that are table stakes in this market
- Honest assessment of each: exists, can be built, must be acquired/partnered
- Capability gap — the single most important gap to close
- Build vs. buy vs. partner assessment for the critical gap

### Dimension 6: Trends & Disruption
- Macro forces: regulatory, technological, demographic, economic, environmental
- Timing: short-term (0–1yr), mid-term (1–3yr), long-term (3–5yr)
- Disruption risk: which trends could render current competitive positions obsolete
- "So what" for this business: what each trend means specifically, not generically

### Dimension 7: Risk
- Top 3 risks stated as specific testable questions, not generic categories
- For each: probability (1–5), impact (1–5), risk score, early warning indicator, mitigation
- Kill triggers: what single development would cause the strategy to be abandoned
- Scenario planning: base / upside / downside with revenue impact

---

## Structured Output Formats

### Format A: In-Chat Strategy Response
*Use for: conversational analysis, quick strategic questions, thinking through a problem*

```
**Hypothesis:** [One sentence — labeled fact/estimate/hypothesis]

**Issue tree:**
[MECE decomposition — 2–3 levels]

**Analysis by dimension:**
[One header per relevant dimension, 3–4 bullets each]
[Label each claim: fact / estimate / hypothesis]

**Recommendation:**
[One sentence answer first]
- Reason 1 [labeled]
- Reason 2 [labeled]
- Reason 3 [labeled]
- Assumes: [top 2 conditions]
- Would change if: [reversal condition]

**Next steps:**
| Action | Owner | Timeline | Impact |
|--------|-------|----------|--------|

**So What?** [One sentence]
```

### Format B: Situation-Complication-Resolution (SCR) Narrative
*Use for: executive briefings, board memos, investment theses, any document with a narrative arc*

```
**Situation:** [What is true and uncontested — shared starting point]
**Complication:** [What has changed or is at stake — the tension]
**Resolution:** [The answer — stated before supporting argument]

[Pyramid support structure]
[Evidence per pillar — labeled fact/estimate/hypothesis]
[Next steps]
```

### Format C: Decision Framework
*Use for: build/buy/partner, go/no-go, option selection, high-stakes decisions*

```
**Decision:** [Stated precisely]
**Criteria:** [MECE list, weighted]

| Option | Criterion 1 | Criterion 2 | Criterion 3 | Score | Verdict |
|--------|-------------|-------------|-------------|-------|---------|

**Recommendation:** [Winner with one-sentence rationale]
**Kill triggers:** [What would reverse this]
**Next steps:** [Owner · Timeline · Impact]
```

### Format D: McKinsey-Style Document or Deck
*Use for: when output is a Word doc or PPTX — defer to pattern-investment-pptx or pattern-docx
for file generation; this skill governs content structure only*

Storyline structure for any document or deck:
1. **Governing thought** — the single most important message (appears on cover / exec summary)
2. **3-part argument** — three mutually reinforcing lines of reasoning
3. **Evidence per argument** — data, analysis, examples (1 slide or section per point)
4. **Synthesis** — what the evidence means together, restating the governing thought
5. **Next steps** — owner, timeline, impact

Each slide or section title must be an **insight statement**, not a label:
- ❌ Label: "Revenue"
- ✅ Insight: "Revenue growth accelerating — 34% YoY driven by enterprise expansion"

---

## Analytical Modules

Apply the relevant module when the request warrants it. Each module is self-contained.

### Porter's Five Forces
Rate each force 1–10 and provide an overall industry attractiveness score.

| Force | Rating | Key Drivers | Implication |
|-------|--------|-------------|-------------|
| Supplier power | | | |
| Buyer power | | | |
| Competitive rivalry | | | |
| Threat of substitution | | | |
| Threat of new entry | | | |
| **Industry attractiveness** | **/10** | | |

### SWOT + Cross-Analysis
Strengths and weaknesses are internal and controllable. Opportunities and threats are external
and environmental. **Cross-analysis is mandatory** — SWOT without it is incomplete:
- **SO** (Strengths × Opportunities): how to exploit
- **ST** (Strengths × Threats): how to defend
- **WO** (Weaknesses × Opportunities): how to develop
- **WT** (Weaknesses × Threats): how to avoid

### Market Sizing
Always provide both methods and reconcile if they diverge significantly.
- **Top-down:** Global market → segment → addressable → serviceable
- **Bottom-up:** Unit economics × potential customers × penetration rate
- State all assumptions explicitly; label as fact / estimate / hypothesis
- Compare to 2+ analyst reports where available

### Competitive Positioning Map
- Two-axis map: choose axes that reveal the most meaningful trade-off in the market
- Plot top 5–10 competitors by estimated position
- Identify white space — where no incumbent is strongly positioned
- Assess defensibility: why hasn't someone already filled the white space?

### Value Chain Analysis
- Map the full value chain for the industry
- Identify where value is created vs. captured
- Assess which steps have high vs. low margins
- Identify where the subject company plays and where it could expand

---

## Investment Evaluation Mode

When the task involves **screening, evaluating, stress-testing, or building an IC memo for
an investment opportunity**, switch from the generic 7-step method to the Six Screening
Questions as the governing analytical structure.

```
Load: {SKILL_DIR}/references/investment-evaluation-framework.md
```

**How to apply the Six Questions:**
- The questions are gates, not a checklist — answer them in sequence. A weak answer to an
  earlier gate is not compensated by a strong answer to a later one.
- Sequence: Company quality → Sector timing → Investment attractiveness → Exit realization →
  Owner fit → Adversarial diligence
- Label every claim: **fact** (sourced) / **estimate** (reasoned) / **hypothesis** (untested)
- Surface red flags explicitly — do not soften or bury them
- End every IC-facing output with: walk-away conditions stated, single most important assumption
  named and labeled as assumption, and an honest post-mortem scenario

---

### Required IC Memo Structure — Five Mandatory Analytical Components

Every IC memo must include these five components in this order. Each is a gate — a memo
missing any of these is not IC-ready regardless of its prose quality.

#### 1. Gate Scoring Tables (Gate 1, Gate 2, Gate 3)

**Gate 1 — Why is this a good company?**
Score the company against all 12 canonical Gate 1 criteria from the investment-evaluation-framework.
Present as a table: Criterion | Verdict (PASS / CONDITIONAL / WATCH) | One-line evidence assessment.
Do not assert "the company is strong" — score each criterion explicitly.

**Gate 2 — Why is this a good sector today?**
Score the sector against all 12 canonical Gate 2 criteria. Present as a full 12-row scorecard
table with criterion number, criterion name, verdict (PASS / CONDITIONAL / WATCH), and
a 1–2 sentence assessment with evidence tags. The gate table summary cell points to this
scorecard; it does not repeat it.

CRITICAL: Gate 2 is a sector-only analysis. The following do NOT belong in Gate 2:
- Stock price drawdown or valuation discount → Gate 3
- Company-specific competitive position → Gate 1
- Adverse selection thesis or why the opportunity exists at this price → Gate 6

Test: could you make the same Gate 2 argument for a private company with no market price?
If not, the argument belongs in Gate 3.

**Gate 3 — Why is this a good investment?**
Score against all 9 canonical Gate 3 factors. Valuation entry point, drawdown, sentiment
mismatch, and adverse selection thesis belong HERE — not in Gate 2.

#### 2. Need-to-Believe (NTB) Registry

Position: immediately after the executive summary verdict paragraph, before the gate table.

The NTB registry is the bridge between the investment thesis (what we believe) and the
returns disaggregation table (what each belief is worth). Every IC memo requires it.

**The NTB registry is owned by the `ntb-diligence` skill.** This skill produces the registry
structure, evidence state classification, boundability narratives, and information gaps
table. If `ntb-diligence` has already run on this deal (typically as pre-IC diligence), the
registry it produced feeds directly into this IC memo's Section 1 without rework.

If `ntb-diligence` has not yet run, trigger it now before continuing with the IC memo:

```
Load: /mnt/skills/user/ntb-diligence/SKILL.md
```

The NTB registry produced by `ntb-diligence` becomes Section 1 of this memo. The
Information Gaps table produced there becomes part of Section 7 (Risk Analysis).

**Summary of NTB registry format (full spec in ntb-diligence):**
5 columns — Need-to-Believe | Key Findings & Workstreams | Evidence State | CY[exit year]E
EBITDA & MOIC Impact | Boundability. Minimum 4 NTBs, each governing a >5% MOIC driver.
GAP items in red bold. Diligence column intentionally excluded (lives in information gaps
table). Returns footnote required.

#### 3. Investment Thesis — Five-Point NTB-Structured Architecture

The investment thesis section must be restructured around the NTBs — not written as independent
analytical observations. Every NTB becomes a numbered thesis point.

**Format for each thesis point:**
```
[Number in navy bold] [NTB statement — one sentence] [NTB # — Evidence State / Boundability]

[Para 1: What the data shows — lead with confirmed facts, then conditional evidence]
[Para 2: What the uncertainty is — name the specific gap, quantify its impact]
[DATA GAP callout if applicable: exact data request in orange left-border paragraph]
[Para 3: Why it matters to the consolidated thesis — link to returns impact]
[Supporting table or data note if material evidence requires it]
```

This architecture makes the thesis immediately auditable: an IC member who disagrees with
the recommendation can identify exactly which NTB they dispute and why.

**What the five-point structure replaces:**
- Independent h2 sections for each product/segment without a governing NTB frame
- Flywheel narratives that don't connect to return quantification
- Risk sections disconnected from the return model

#### 4. Returns Disaggregation Table (section 3.3 of investment-evaluation-framework)

Every IC memo requires the structured returns disaggregation table with 7 columns:
Driver | Base Case Assumption | Upside Scenario + Mechanism | Downside Scenario + Mechanism |
CY[exit year]E EBITDA Impact Up/Down | MOIC Impact Up/Down | Resolving Diligence Item

The NTB table is the upstream document that populates the "Resolving Diligence Item" column.
Every NTB must map to at least one row in this table.

#### 5. Information Gaps Table

Ranked by priority (CRITICAL / HIGH / MEDIUM). Every GAP item in the NTB table must appear
here as a named priority with: specific data request, risk addressed, action and owner.
The NTB table references these by priority number — the information gaps table is the
single authoritative source for diligence prioritization.

---

**Trigger phrases that activate Investment Evaluation Mode:**
- "screen this deal / opportunity"
- "evaluate this investment / acquisition / target"
- "IC memo" / "investment committee"
- "investment thesis" / "stress-test the thesis"
- "why is this a good company"
- "ROIC analysis" / "return on invested capital"
- "deal screening" / "diligence scoping"
- "walk-away conditions"
- "need-to-believe" / "NTB"



## Quality Standards

Every output must pass all of the following before delivery:

**Structural integrity**
- [ ] Problem restated before analysis begins
- [ ] Issue tree is MECE — checked for overlaps and gaps
- [ ] Day-1 hypothesis stated, labeled as hypothesis
- [ ] 20/80 drivers identified and deprioritized branches explicitly noted
- [ ] Every claim labeled: fact / estimate / hypothesis

**Content standards**
- [ ] No generic observations — name names, state numbers
- [ ] No recommendations without owner, timeline, and expected impact
- [ ] Every analytical finding connects to the decision being made
- [ ] Missing data called out explicitly, never silently omitted
- [ ] All assumptions surfaced, not buried

**Executive readiness**
- [ ] Answer leads — never buried in analysis
- [ ] Max 3–4 bullets per cluster; sub-headers used if more content needed
- [ ] Numbers formatted: $2.3B not $2,300M; 34% not 0.34
- [ ] Every substantive response ends with So What?
- [ ] Decision-maker can act without asking a follow-up question

---

## References

All reference files live in this skill's /references folder. Market-research points here —
these files are not duplicated there.

**Investment evaluation (load for any investment or IC memo task):**
```
Read: {SKILL_DIR}/references/investment-evaluation-framework.md
```

**Extended MBB methodology (7-step deep-dive, MECE, Pyramid Principle, 80/20):**
```
Read: {SKILL_DIR}/references/MBB_METHODOLOGY.md
```

**Source validation — full CRAAP scoring rubric, triangulation matrix, confidence labeling:**
```
Read: {SKILL_DIR}/references/VALIDATION_FRAMEWORKS.md
```

**12-prompt research suite (market sizing, competitive landscape, personas, trends, SWOT,
pricing, GTM, journey mapping, financial modeling, risk, market entry, executive synthesis):**
```
Read: {SKILL_DIR}/references/prompts.md
```

**Source bibliography template (working tracker for documenting and scoring sources):**
```
Read: {SKILL_DIR}/references/source-bibliography.md
```

**Free data sources directory (Tier 1–3 sources by category — government agencies, academic
databases, SEC filings, industry associations, trade publications):**
```
Read: {SKILL_DIR}/references/FREE_SOURCES_GUIDE.md
```
