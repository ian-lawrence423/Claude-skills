---
name: mckinsey-consultant
description: >-
  Use when a complex problem — strategy, diagnosis, or a decision — needs disciplined
  structure, not an ad hoc answer. Builds MECE issue trees and Pyramid Principle
  recommendations.
intent: >-
  McKinsey-level structured thinking for any non-trivial problem. This is the analytical
  OS — load it whenever a question benefits from disciplined reasoning rather than an ad
  hoc answer: strategy work, structured diagnosis, framework design, decision-making, or
  a McKinsey-style document. It owns the general method: 7-step MBB problem solving, MECE
  issue trees, 7 strategy dimensions, Pyramid Principle, and all analytical modules
  (Porter's, SWOT, market sizing, positioning maps, value chain). Investment evaluation is
  one application of this method, not its purpose — when a task specifically requires
  screening or stress-testing an investment, pair this skill with the Six Screening
  Questions (see Investment Lens below). It does NOT govern evidence gathering or source
  validation — that is market-research's job. For any task that requires original data
  collection (market sizing, competitive intelligence, customer research), invoke
  market-research on top of this skill. For financial modeling, use
  financial-model-builder. For PPTX/docx output, use pattern-investment-pptx or
  pattern-docx. In deal workflows, pair this skill with analytical-operating-system for
  persistent belief registers, Bayesian updates, kill triggers, and decision posture
  tracking.
type: workflow
---

# McKinsey Consultant Skill — Analytical OS

This skill is the analytical engine for structured thinking — a way of reasoning through any
complex problem, not a strategy or investment specific tool. It governs how you think, structure
arguments, apply analytical lenses, and synthesize to a recommendation. It does not govern how
you gather evidence — that is market-research's job, which runs on top of this skill when
original data collection is required.

Read this entire file before beginning any analysis.

---

## Ownership & Routing

```
mckinsey-consultant   ← analytical method: problem definition, MECE trees, 7 dimensions,
                         Pyramid Principle, analytical modules, investment screening questions
      │
      ├── market-research             ← new evidence gathering, source validation, triangulation
      ├── analytical-operating-system ← belief registers, Bayesian updates, kill triggers, decision posture
      ├── financial-model-builder     ← operating models and return cases
      ├── competitive-moat-assessment ← moat type, depth, durability, erosion risk (Dimension 4 specifics)
      └── pattern-docx / pattern-investment-pptx / ic-memo ← file and document output
```

This skill alone is sufficient whenever evidence is already in hand and the job is to
structure and reason — a memo, thesis, or deck built from known facts. Invoke
`market-research` when new external evidence must be gathered or validated. Invoke
`analytical-operating-system` when assertions must be tracked over time — deal-master,
IC memo, or diligence workflows where evidence state and decision posture need to be
auditable. Do not duplicate either skill's artifacts here.

---

## Dependency Contract

Loads before this skill:
- None required for standalone strategy work.
- `deal-master` may load before this skill in full deal workflows to inventory existing work and route the phase.

Loads after this skill:
- `analytical-operating-system` for deal workflows that need belief registers, evidence states, or decision posture.
- `market-research` when new external evidence, source validation, or citation tracking is required.
- `financial-model-builder` when the answer depends on an operating model or return case.
- `writing-style` before any formal deliverable leaves draft state.
- `claim-scrutinizer`, `red-team`, or `pre-mortem` after a draft thesis, memo, or recommendation exists.
- `pattern-docx` or `pattern-investment-pptx` only when producing a file.

Inputs required:
- Decision to be made, scope boundaries, known facts, existing evidence, and output format.

Outputs produced:
- Problem statement, MECE issue tree, Day-1 hypothesis, 20/80 analysis plan, analytical lens selection, and recommendation structure.

Do not use this skill alone when:
- The task requires original research, evidence triangulation, belief-register tracking, financial model construction, or branded file production.

## Workflow Mode

| Mode | Use When | Minimum Output |
|---|---|---|
| Quick | User needs structure, an issue tree, or a rapid recommendation from known facts | BLUF, issue tree, 2-3 key drivers, next step |
| Standard | User needs a strategy or investment analysis using existing evidence | Problem definition, MECE tree, hypothesis, evidence by branch, recommendation |
| Full | User needs an IC-grade or board-ready workflow | This skill plus evidence control, research, quality review, and production skills as needed |

A request to "skip the framework," "just give me the bottom line," or a tight deadline is a
request to compress, not a license to omit. Quick mode's minimum output above already includes
an issue tree and a hypothesis — shrink them to 2–3 branches and one sentence, don't drop them.
The label doesn't have to be the bold word "Hypothesis:" or "Issue tree:" — a clean header, a
"Bottom line:" sentence that states a falsifiable claim, or a short list of named candidate
causes all satisfy this if the content is actually there. The tell is content, not string
matching: is there one stated, falsifiable claim about the cause (not just a description of the
symptom), and are there 2–3 distinct, named candidate drivers (not one vague paragraph)? If
either is missing, the structure was dropped regardless of formatting; if both are present in
substance, it doesn't matter what the section is called.

---

## Example And Anti-Pattern

Example prompt:
> "Our enterprise churn rate jumped this quarter — help me figure out why and what to do about it."

Expected use:
- Define the decision, Day-1 hypothesis, MECE issue tree, binding driver, and recommendation logic.
- Use known evidence only; invoke `market-research` if new source collection is required.
- Hand off to `analytical-operating-system` when belief registers or decision posture are required.

A second valid example, same method:
> "Structure the investment case for Company X using this existing CIM and management deck."

The method does not change between the two — only the analytical lenses applied (see Seven
Strategy Dimensions and Investment Lens below) and, if the output is an IC memo, the document
architecture (owned by `ic-memo`).

Anti-pattern:
- Do not use this skill to gather new sources, maintain evidence registers, build financial models, or generate branded files.
- Do not force every problem through an investment-screening frame — the Six Screening Questions
  are a lens for investment decisions specifically, not the default structure for all analysis.

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
- **Horizontally consistent**: siblings at each level sit at the same altitude of detail/
  importance — don't mix a market-sizing question with an implementation-timeline question at
  the same level
- **Vertically logical**: each child branch answers a question the parent branch raises; if it
  doesn't, it belongs elsewhere in the tree or not in it
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
- [ ] Concise — the tree is no bigger than it needs to be; cut branches that don't change the answer
- [ ] No branch overlaps with another — each is independently addressable
- [ ] Together, all branches fully cover the problem — no material gaps
- [ ] Each branch is resolvable with available or gatherable evidence
- [ ] The logical structure holds: if all branches are true, the governing thesis follows
- [ ] Each grouping is typed as **inductive** (parallel items sharing a category, jointly
      implying the point above) or **deductive** (a chain where each step follows from the one
      before)
- [ ] No branch has more than ~6 inductive items or ~4 chained deductive steps — past that,
      split and regroup rather than listing more

### Step 3: State Hypotheses
- A hypothesis is a testable initial answer derived directly from the question it answers —
  not a final answer, and it must be falsifiable
- State the overarching Day-1 hypothesis for the whole problem immediately — do not wait for
  analysis to be complete. Format: *"We believe [conclusion] because [primary reason], which
  means [implication]"* — label it explicitly as **hypothesis (untested)**
- Give each major branch of the issue tree its own branch-level hypothesis — the initial answer
  to that branch's question — so each branch has something concrete to test, not just a topic
  to research
- If a hypothesis isn't yet visible for the overarching question or a branch, build bottom-up
  instead: list the points you're already confident of, find what they share in common, and let
  the conclusion emerge from that commonality
- Hypotheses are working beliefs, not commitments — revise or reject them as findings come in
  (see Step 5)

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

Every hypothesis is supported by **arguments** — each argument must be individually necessary
to support the hypothesis, and the full set of arguments must be collectively sufficient to
prove it. An argument that's merely "related" but not necessary doesn't belong.

**Findings** are the yes/no-style statements derived from data that test a hypothesis — they
should fully test the hypothesis, fully support whatever conclusion follows, and be accurate
enough to be convincing on their own.

**Claim labeling is mandatory on every finding — tag each one inline, immediately after
stating it, with `[fact]`, `[estimate]`, or `[hypothesis]`:**
- **fact** — sourced, verifiable, cited
- **estimate** — reasoned from available data with stated assumptions
- **hypothesis** — untested, requires validation

Use this skill to decide which claims matter and how they fit the issue tree; route
persistent claim tracking to `analytical-operating-system` and new evidence gathering to
`market-research` (see Ownership & Routing above).

### Step 6: Synthesize to a Recommendation
- For each branch, draw a **conclusion**: a diagnostic statement that unites that branch's
  findings, checks them against the branch hypothesis, and revises or confirms it. A conclusion
  can come from the hypothesis holding up, or directly from findings that overturn it.
- State the overarching recommendation in one sentence first — never bury it
- Structure the supporting argument as a **Pyramid** (Minto): Top = governing thought (the
  answer); Middle = 3 key lines of reasoning, one per binding conclusion; Base = evidence
- **Vertical test:** every point below a line must answer a why/how question the line above
  raises; the supporting points are individually necessary and collectively sufficient to
  prove it
- **Horizontal test:** the lines supporting one point are typed as **inductive** (parallel
  reasons sharing a category) or **deductive** (a chain, breakable at its weakest link) — check
  for no misfits, no overlaps, no gaps, and correct order. Same cap as the issue tree: regroup
  past ~6 inductive lines or ~4 chained deductive steps
- For each recommendation include:
  - What this assumes (top 2–3 conditions that must hold)
  - What would change it (the single most likely reversal condition)

### Step 7: Define Next Steps
- Maximum 5 priority actions
- Each action: **Owner · Horizon · Expected impact · Leading indicator it's working**
- **Horizon is a category, not an invented date:** quick win / structural move / long-term bet,
  judged from the nature of the action (e.g. "verify a claim before deciding" is inherently a
  quick win; "build multi-year relationships" is inherently a long-term bet). Do not state a
  specific duration — "2–3 weeks," "next quarter," a day count — unless the user gave it or it's
  a known fact. A specific-sounding timeline you don't have a basis for is not more rigorous than
  a horizon category, it's fabricated precision — the same failure as an unlabeled [estimate]
  presented as [fact]. If no real basis exists for even the horizon, say so rather than guessing.
- End with **So What?** — one sentence on the key takeaway or most urgent decision
- Before delivering, re-read the Quality Standards checklist below and confirm every item
  yourself — this is a required step, not a suggestion; do not assume a hook will catch a miss

---

## Seven Strategy Dimensions

Apply all seven only to market/competitive/positioning-level strategy questions — not to a
narrow root-cause diagnostic or single-metric investigation (e.g. "why did this number move,"
a build/buy call), **and not to a narrow competitive or capability sub-question inside a larger
deal or strategy context** (e.g. "is this target's moat durable," "can we close this capability
gap") — those need only the specific dimension(s) the question is actually about (Competition
and/or Capability, typically), not all seven. In both cases the 7-step method above is
sufficient on its own; running the full seven dimensions on a question that only touches one or
two of them pads the answer with dimensions the question never asked about. When conducting
strategy work, every analysis must address all seven dimensions: **Market** (size, growth,
trends), **Customer** (JTBD, willingness to pay), **Economics** (unit economics, margin
levers), **Competition** (named competitors, moat, displacement path — invoke
`competitive-moat-assessment` for moat type/depth/durability/erosion specifically, rather than
improvising that framework here), **Capability**
(table-stakes gaps, build/buy/partner), **Trends & Disruption** (macro forces by timing
horizon), **Risk** (top 3 as testable questions, kill triggers). These define the *analytical
questions to answer* — not the data to collect (that is market-research's job). Flag explicitly
when data for a dimension is unavailable.

```
Load: {SKILL_DIR}/references/strategy-dimensions-and-formats.md
```
for the full required sub-elements per dimension.

---

## Structured Output Formats

| Format | Use for |
|---|---|
| **A — In-Chat Strategy Response** | Conversational analysis, quick strategic questions |
| **B — SCQA Narrative** | Executive briefings, board memos, investment theses, or any longer answer where the reader doesn't already share your context — default opening in those cases |
| **C — Decision Framework** | Build/buy/partner, go/no-go, option selection, high-stakes decisions |
| **D — McKinsey-Style Document or Deck** | Output is a Word doc or PPTX — defer to `pattern-investment-pptx`/`pattern-docx` for file generation; this skill governs content structure only |

Every format leads with the answer, labels claims fact/estimate/hypothesis, and ends with
Owner · Horizon · Impact next steps — horizon is quick win/structural/long-term, not an invented
date (see Step 7). For Format D, every slide/section title is an insight
statement ("Revenue growth accelerating — 34% YoY"), not a label ("Revenue").

```
Load: {SKILL_DIR}/references/strategy-dimensions-and-formats.md
```
for the full template of each format.

---

## Analytical Modules (Optional)

Named frameworks (Porter's, SWOT, market sizing, positioning map, value chain, advantage
durability, substrate disintermediation) for when a specific branch calls for one. They are not
the core method — the issue tree → hypothesis → argument → finding → conclusion → Pyramid chain
above is sufficient on its own for most problems. Reach for a module only when a branch
specifically warrants it; don't default into naming a framework just because one exists.

```
Load: {SKILL_DIR}/references/analytical-modules.md
```

---

## Investment Lens (Optional)

The 7-step method and Seven Strategy Dimensions above are sufficient for most problems,
investment included. Reach for this lens only when the task specifically requires
**screening, evaluating, stress-testing, or building an IC memo for an investment
opportunity** — triggered by phrases like "screen this deal," "IC memo," "investment
thesis," "ROIC analysis," "walk-away conditions," or "need-to-believe." Do not route a
general strategy or business question through this lens by default.

When it does apply, swap the Six Screening Questions in for the generic 7-step method as
the governing structure — they are gates, not a checklist (a weak answer to an earlier
gate is not compensated by a strong answer to a later one):

Company quality → Sector timing → Investment attractiveness → Exit realization →
Owner fit → Adversarial diligence

```
Load: {SKILL_DIR}/references/investment-evaluation-framework.md
```

Label every claim fact / estimate / hypothesis, surface red flags rather than softening
them, and end every IC-facing output with walk-away conditions, the single most important
assumption (labeled as such), and an honest post-mortem scenario.

Document architecture — section order, NTB registry placement, gate scorecards, returns
disaggregation, information gaps — is owned by `ic-memo`; invoke it for document
structure rather than re-deriving IC memo formatting here. `ntb-diligence` is the
authoritative source for the NTB registry itself.

---

## Common Mistakes

- **Dropping the issue tree or Day-1 hypothesis under time pressure.** "Skip the framework,"
  "just give me the bottom line," or a tight deadline means compress, not omit — see Workflow
  Mode above. This is the single most common failure, and it survives even when the response
  looks reasonable: a flat "here's what's likely driving it" bullet list of symptoms, with no
  falsifiable claim about the cause and no distinct named candidate drivers, reads like analysis
  but isn't the structure — regardless of whether a section happens to be labeled "Hypothesis"
  or "Issue tree." Check content, not labels.
- **Satisfying the keyword instead of the requirement.** Using the word "hypothesis" or
  "estimate" somewhere in the response is not the same as stating a labeled Day-1 hypothesis or
  tagging every claim inline. The requirement is the structure, not the word appearing once.
- **Treating a hypothesis as a conclusion once stated.** A Day-1 hypothesis is a starting point to
  revise or reject as findings come in (Step 3) — restating it unchanged at the end without
  checking it against the evidence is not synthesis, it's a shortcut.
- **Naming a framework for its own sake.** Reaching for Porter's, SWOT, or a named module when
  the issue tree → hypothesis → finding chain already answers the question — see Analytical
  Modules.
- **Forcing every question through the investment-screening lens.** The Six Screening Questions
  are for investment decisions specifically, not the default structure for all analysis — see
  Investment Lens.

---

## Quality Standards

Self-apply this checklist before every response — it is the primary check, required by Step 7
above, not a passive reference. Two hooks configured in `.claude/settings.json` (a PostToolUse
reminder right after this skill loads, and a Stop-time keyword check for hypothesis labels,
claim tags, and a closing "So What?") reinforce this in environments where they're active, but
hook support cannot be assumed — treat them as a bonus tripwire if present, never as the
mechanism this checklist actually depends on. Even where hooks are active, they only catch
outright omissions mechanically; they do not verify the other items below — that judgment is
yours either way.

Every output must pass all of the following before delivery:

**Structural integrity**
- [ ] Problem restated before analysis begins
- [ ] Issue tree is MECE — checked for overlaps and gaps
- [ ] Day-1 hypothesis stated, labeled as hypothesis
- [ ] 20/80 drivers identified and deprioritized branches explicitly noted
- [ ] Every claim tagged inline: [fact] / [estimate] / [hypothesis]
- [ ] Each issue-tree branch has its own testable hypothesis, revised or rejected as findings
      come in — not treated as a fixed commitment
- [ ] Every argument under a hypothesis is individually necessary; the full set is collectively
      sufficient to prove it
- [ ] Findings test the hypothesis explicitly (confirm / weaken / reject) before a conclusion is
      drawn
- [ ] Horizontal groupings typed inductive or deductive, with no misfits, overlaps, or gaps

**Content standards**
- [ ] No generic observations — name names, state numbers
- [ ] No recommendations without owner, horizon, and expected impact
- [ ] No fabricated timeline — a horizon category (quick win / structural / long-term), not an
      invented date or duration, unless the user supplied it or it's a known fact
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

**Seven Strategy Dimensions (full per-dimension checklist) and Structured Output Formats
(full templates for A–D):**
```
Read: {SKILL_DIR}/references/strategy-dimensions-and-formats.md
```

**Extended methodology deep-dive (MECE, Pyramid Principle, Hypothesis Chain, 80/20):**
```
Read: {SKILL_DIR}/references/MBB_METHODOLOGY.md
```

**Analytical modules (Porter's, SWOT, market sizing, positioning map, value chain, advantage
durability, substrate disintermediation — optional lenses, not the core method):**
```
Read: {SKILL_DIR}/references/analytical-modules.md
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
