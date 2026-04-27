---
name: market-research
description: |
  Execute professional-grade market research projects using a structured, hypothesis-driven
  methodology. Use this skill whenever Ian asks to conduct market research, build a research
  brief, run a market analysis, size a market, profile competitors, or produce a research
  deliverable for any deal, product, or strategic initiative. Trigger even for partial requests
  like "help me build a brief for X", "what's the market look like for Y", "I need a research
  plan", "run diligence on this market", or "put together a research framework." This skill
  governs the full research workflow — from brief creation through pyramid analysis, theme
  development, report architecture, and the mandatory iteration loop — to final DOCX or PPTX
  output. Integrates with mckinsey-consultant (analytical methodology), writing-style (prose
  and claim discipline), claim-scrutinizer (logic redline), red-team (adversarial pass), and
  pattern-docx / pattern-investment-pptx (file output). Does not duplicate logic owned by
  those skills.
---

# Market Research Skill

You are executing a structured, MBB-quality market research project. Read this entire file
before beginning any work.

This skill governs: research workflow sequencing, output architecture, section anatomy,
theme development, iteration protocol, depth standards, source strategy, and citation format.

It does NOT govern: analytical methodology (mckinsey-consultant), prose and claim standards
(writing-style), logic redlining (claim-scrutinizer), adversarial stress-testing (red-team),
or file formatting (pattern-docx / pattern-investment-pptx). Defer to those skills for
their respective responsibilities. Do not duplicate their logic here.

---

## Skill Architecture

```
market-research        ← workflow, architecture, iteration sequencing
      │
      ├── mckinsey-consultant     ← MECE, pyramid principle, 7 strategy dimensions,
      │                              claim labeling (F/E/H), analytical modules
      │
      ├── competitive-moat-assessment ← invoked at Level 2: uses competitor profiles
      │                                  as inputs; produces moat verdict per competitor
      │
      ├── writing-style           ← runs after every draft section:
      │                              inductive chain test, absolute assertion test,
      │                              epistemic language, data gap flagging, prose standards
      │
      ├── claim-scrutinizer       ← Pass 2 of iteration loop:
      │                              7-part test, assumption audit, derivative integrity,
      │                              base rate checks, CRAAP-scored evidence
      │
      ├── red-team                ← Pass 3 of iteration loop:
      │                              attack vectors, kill scenarios, bear case, scorecard
      │
      ├── doc-quality-checker     ← QA gate after Phase 6 output:
      │                              brand compliance, narrative flow, internal consistency
      │
      └── pattern-docx            ← final DOCX output
          pattern-investment-pptx ← final PPTX output

Consumed by (downstream):
      ├── ntb-diligence           ← when producing NTB diligence, this skill's Phase 3
      │                              NTB-ready findings feed its Phase 3 evidence inventory
      │
      └── ic-memo                 ← when producing an IC memo, this skill runs in
                                     IC Memo Mode (see Phase 1 IC Memo Mode section)
```

---

## Execution Flow — Full Overview

```
Phase 1 │ BRIEF
        │ Define decision, MECE hypothesis tree, source strategy, success criteria
        │
Phase 2 │ PYRAMID RESEARCH  (bottom-up: L4 → L3 → L2 → L1)
        │ Gather and validate evidence by pyramid level
        │ Apply inline citation format to every claim as you go
        │ Flag data gaps immediately — do not paper over thin evidence
        │
Phase 3 │ THEME DEVELOPMENT  ← most critical phase, do not skip
        │ Synthesize pyramid evidence into 4–6 governing structural themes
        │ Themes are the report spine — not pyramid levels, not data summaries
        │
Phase 4 │ DRAFT
        │ Build document using Report Architecture below
        │ Organize by themes, never by pyramid levels
        │ Apply Section Anatomy to every theme section
        │ Apply Competitor Profile Anatomy to every named competitor
        │
Phase 5 │ ITERATION LOOP  (three sequential passes — none optional)
        │ Pass 1: writing-style self-review
        │ Pass 2: claim-scrutinizer redline
        │ Pass 3: red-team adversarial pass
        │ Harden after each pass before advancing to the next
        │ Pre-mortem is NOT part of market-research — see Phase 5 note
        │
Phase 6 │ OUTPUT
        │ pattern-docx (long-form report) or pattern-investment-pptx (deck)
        │
Phase 7 │ QA GATE
        │ doc-quality-checker runs on the produced file
        │ Checks brand compliance, formatting, structural logic, narrative flow
        │ Zero CRITICAL issues required before release
```

**Sequencing is mandatory.** Theme development must complete before drafting. Each
iteration pass must complete and be hardened before the next pass begins. Do not compress
or skip phases to save time — the iteration loop is what separates a draft from a
publishable document. doc-quality-checker runs AFTER file output because it checks
brand compliance (fonts, colors, spacing) that only exists once the .docx or .pptx
is produced.

---

## Phase 1: Brief Creation

Load and complete the canonical template:
```
Read: {SKILL_DIR}/references/research-brief.md
```

**Domain Template Auto-Load — check before building the brief:**

Before constructing the hypothesis tree, scan the research topic against the domain template
trigger lists below. If a match is found, load the template immediately — it pre-loads
confirmed data, known gaps, NTB evidence inventories, and open questions that would otherwise
require re-gathering.

```
IC memo domain templates (investment memo context):
  Path: /mnt/skills/user/ic-memo/references/domain-templates/

  sea-ltd-sea-brazil.md
  Triggers: Sea Limited, NYSE: SE, Shopee, Monee, SPayLater, SPX Express, Garena,
            SEA e-commerce investment, TikTok Shop SEA, MercadoLibre Brazil vs Shopee,
            MELI vs Sea, SEA platform investment thesis, Sea Ltd IC memo

Market research domain templates (sector research context):
  Path: /mnt/skills/user/market-research/references/domain-templates/

  marketplace-operator-sea-brazil.md
  Triggers: Shopee market research, SEA e-commerce market, Southeast Asia marketplace,
            Brazil e-commerce market, SPX logistics, TikTok Shop competitive analysis

  commerce-infrastructure.md
  Triggers: Digital commerce, post-purchase, OMS, returns management, checkout, PPX,
            Narvar, Loop, Redo, Manhattan Associates, AfterShip, Gorgias, Kibo, parcelLab,
            Stripe, Adyen, Stage 4/5/6

  narvar-ppx-competitive-intelligence.md
  Triggers: Narvar, post-purchase investment thesis, PPX competitive landscape,
            returns software, Loop Returns, Redo, parcelLab, IRIS, NAVI, Shield,
            Happy Returns, AfterShip returns
```

**When a domain template loads:**
- Treat all data marked [F] in the template as confirmed context — do not re-gather
- Treat all GAP items in the template as priority research actions for Phase 2
- For IC memo templates: pre-populate the NTB evidence inventory from the template's NTB registry
- State in the brief: "Domain template loaded: [filename]. [N] confirmed data points pre-loaded.
  [N] open questions carried forward. Research focuses on resolving gaps and updating stale data."
- **Staleness check:** Look at the template's footer for a "Template version" or
  "Last updated" line. If the template is dated more than one quarter before the
  current research date, treat time-sensitive data categories (market share, GMV,
  pricing, competitive moves, financial figures) as [E] and add them to the Phase 2
  research agenda for verification. Structural data (taxonomies, value chains,
  methodologies) can be treated as [F] regardless of template age. If no version
  footer exists, treat all quantitative data as [E] and verify.

Required inputs: project name, company/market, core business question, decision deadline.

**How to complete the brief:**
1. Sharpen the research question against SMART criteria — reject vague framing.
   "Understand the market" is not a research question. "Is this market large enough and
   structurally attractive enough to justify a $X investment?" is.
2. Build the MECE hypothesis tree (defer to mckinsey-consultant for MECE logic)
3. Assign source tiers per Source Strategy below
4. State success criteria as measurable outcomes, not activity completions

**Brief quality gates — all must pass before proceeding:**
- [ ] Research question is tied to a specific decision
- [ ] Hypothesis tree is MECE — branches tested for overlap and exhaustiveness
- [ ] Each hypothesis has a stated evidence need and named source strategy
- [ ] Success criteria are measurable and scoped to the decision deadline
- [ ] Domain template checked — if loaded, pre-loaded data and open questions noted in brief

---

## IC Memo Mode — When Invoked by ic-memo

When `ic-memo` invokes this skill as part of the IC memo workflow, market-research
runs in a constrained mode. Three differences from standalone execution:

**1. No intake protocol**
The ic-memo intake has already captured: company, market, deal context, key questions,
and known data challenges. Do NOT run Phase 1 brief creation or ask intake questions.
Pass the ic-memo intake directly into Phase 2.

**2. Scoped pyramid — L4, L3, L2 only**
- Execute Level 4 (Market) → Level 3 (Customer) → Level 2 (Competitive)
- SKIP Level 1 (Company / Client Position) — ic-memo handles this directly via its own
  intake materials, CIM, and management presentation. Level 1 inside the IC memo
  workflow would duplicate work.
- competitive-moat-assessment runs immediately after Level 2 completes, using the
  competitor profiles as inputs — before Phase 3 theme development.

**3. No standalone deliverable**
Do NOT produce a standalone report or deck. Output is a structured evidence summary
organized by pyramid level with inline citations, which feeds directly into ic-memo
memo sections:
- L4 findings → Section 5 (Market & Competitive)
- L3 findings → Section 6 (Business Quality) customer subsection
- L2 findings → Section 5 (Competitive Position) and competitive-moat-assessment inputs

**4. Theme count stays 4–6**
Theme count is the same in IC memo mode as standalone (4–6 themes minimum to maximum).
Themes align to the IC memo's investment thesis pillars where possible but are not
constrained to the pillar count.

**5. Phase 5 iteration loop runs — but belongs to ic-memo's iteration loop**
Writing-style / claim-scrutinizer / red-team passes run on market-research output as
part of ic-memo's iteration loop, not as a separate sequence. Do NOT run them twice.

**6. No Phase 6 or Phase 7 on standalone basis**
Phase 6 output and Phase 7 QA gate are owned by ic-memo in this mode — ic-memo
produces the final .docx with its own doc-quality-checker pass on the memo file.

**Trigger:** This mode activates automatically when this skill is invoked from within
ic-memo's workflow. If the user runs market-research directly (even on a deal topic),
standalone mode applies.

---

## Phase 2: Pyramid Research

**Numbering orientation:** In this skill, Level 4 is the broadest research scope (market
context) and Level 1 is the most specific synthesis (company position). "Bottom-up"
means starting at L4 (broad evidence base) and synthesizing upward to L1 (company-specific
implications). Some pyramid conventions invert this numbering — this skill uses the
"base = broadest" convention. Execute the pyramid in the L4 → L3 → L2 → L1 sequence
regardless of what convention a reader is used to.

Execute bottom-up: Level 4 → Level 3 → Level 2 → Level 1. Each level builds on the prior.
These levels are analytical inputs. They are never the output structure.

Apply the **inline citation format** to every claim as you research — not after drafting:
```
[Source name, Year] [Confidence: H/M/L]
```
Full CRAAP scores go in source-bibliography.md. Inline tags keep claims traceable during
drafting and iteration passes.

Flag data gaps immediately using this format when web search returns thin, conflicting,
or unverifiable data on any thesis-critical claim:
```
DATA GAP: [Claim] — [one source only / sources conflict / no third-party validation].
Warrants: [specific follow-on action] before treating as confirmed.
```
Do not paper over gaps with qualified language. The gap is material information.

---

### Level 4: Market & Segment Analysis

**Questions to answer:**
- TAM / SAM / SOM — both top-down and bottom-up methods required
- CAGR with source base year and stated methodology — not just the figure
- Structural trends shaping the market over 3–5 years
- Segment map with individual sizing

**Depth standard:**
- Both sizing methods required. If they diverge by more than 25%, reconcile explicitly
- Growth rate must state the source's methodology and base year — a figure alone fails
- Segment sizing must be bottom-up verified — top-down alone is insufficient
- Trend analysis must name specific drivers with evidence, not category labels
- Every quantitative claim: 2–3 independent Tier 1–2 sources minimum

**Analytical prompt set:** Load for this level:
```
Read: {SKILL_DIR}/references/analytical-prompts.md → Section: Market Sizing & Trends
```

**Source priority:** Government data, public company filings, Tier 1 analyst reports
(Gartner, IDC, Forrester), academic research.

---

### Level 3: Customer Insights

**Questions to answer:**
- Who has the problem and how acute is it?
- What are the 3–5 distinct customer segments?
- JTBD for each segment: *"When [situation], the customer needs to [motivation] so they
  can [outcome]"*
- Primary pain points and barriers per segment
- Decision-making process and key purchase triggers

**Depth standard:**
- Each segment profile requires a specific observable behavior or pain point that
  distinguishes it from other segments. Generic descriptions fail.
  ❌ "Enterprise buyers prioritize reliability"
  ✅ "Enterprise buyers require SLA-backed uptime guarantees because outages trigger
     contract penalties — evidenced by [Source, Year]"
- Barrier analysis must categorize barriers (awareness / switching cost / budget /
  technical / organizational) and rate severity — not just list them
- JTBD framing required for each segment — not optional

**Analytical prompt set:**
```
Read: {SKILL_DIR}/references/analytical-prompts.md → Section: Customer Insights
```

**Source priority:** Consumer surveys (Pew, Nielsen), industry association research,
academic behavioral studies, trade press with named methodology.

---

### Level 2: Competitive Landscape

**Questions to answer:**
- Top 3–7 competitors with full profiles (see Competitor Profile Anatomy below)
- Positioning map — two axes that reveal the market's most meaningful trade-off
- Estimated market share per player where available
- White space: where no incumbent is strongly positioned, and why it hasn't been filled

**Depth standard:**
Every named competitor requires the full **Competitor Profile Anatomy** below. A profile
missing any of the six elements is incomplete. Profiles are 300–500 words in the final
document — shorter than this means elements are missing.

**Analytical prompt set:**
```
Read: {SKILL_DIR}/references/analytical-prompts.md → Section: Competitive Landscape
```

**Source priority:** Public filings (10-K, S-1, earnings transcripts), analyst reports,
company websites, job postings as capability signals (Tier 3 — context only).

**Handoff to competitive-moat-assessment:**

Level 2 output feeds `competitive-moat-assessment` — the downstream skill that produces
the moat verdict per competitor. Every Competitor Profile's Element 3 (Sustainable
advantage) is a moat-assessment input: the classification into network effect / switching
cost / scale economies / proprietary IP / brand directly matches moat-assessment's
classification taxonomy.

When market research is running in IC Memo Mode (see IC Memo Mode section below),
competitive-moat-assessment runs immediately after Level 2 completes and before Phase 3
theme development begins — its moat verdicts inform which themes are load-bearing.

When market research runs standalone for sector analysis, invoke moat-assessment
optionally — use it when the research question depends on relative defensibility of
named competitors, skip it when the focus is market sizing or customer research.

```
Downstream load: /mnt/skills/user/competitive-moat-assessment/SKILL.md
```

#### Competitor Profile Anatomy — apply to every named competitor

**Element 1 — Core product and GTM** (1–2 sentences)
What they actually do and how they go to market. Specific, not categorical.

**Element 2 — Customer base**
Named segments served. Include customer count, revenue, or ARR if publicly available.
If not available, state that explicitly — do not omit and do not estimate without basis.

**Element 3 — Sustainable advantage**
The single most defensible structural advantage. Must be one of: network effect /
switching cost / scale economies / proprietary IP / brand. Generic descriptors
("best-in-class product," "strong team") do not qualify — name the mechanism.

**Element 4 — Key weakness**
The most exploitable structural gap. State it as a specific, observable limitation —
not a broad category. "Limited geographic coverage" is a category.
"No fulfillment infrastructure outside the US, limiting enterprise contract eligibility
for multinational buyers" is a weakness.

**Element 5 — Strategic trajectory**
Where they appear to be moving and what signals evidence it. Required signals: at least
two of — product launches, acquisition activity, job posting patterns, public executive
statements, partnership announcements. Trajectory without signals is speculation.

**Element 6 — Competitive verdict**
One sentence: what does this competitor's position mean for the subject company or
investment thesis? This is the only element that is interpretive — all others are
evidenced description.

---

### Level 1: Company / Client Position

**Questions to answer:**
- Current strategy and business model
- Capabilities that exist vs. what is required to win (gap analysis)
- SWOT with mandatory cross-analysis: SO / ST / WO / WT
- Build / buy / partner framing for each critical gap

**Depth standard:**
- Capability assessment must use a three-state taxonomy: exists / can build / must acquire
- SWOT cross-analysis is mandatory — a SWOT without SO/ST/WO/WT is incomplete
- Every gap requires a stated build/buy/partner disposition with rationale

**Analytical prompt set:**
```
Read: {SKILL_DIR}/references/analytical-prompts.md → Section: Company Position & Strategy
```

---

## Phase 3: Theme Development

**This is the most analytically demanding phase. Do not compress it.**

After completing all four pyramid levels, synthesize findings into 4–6 governing themes.
A theme is a structural observation about the market that has strategic significance. It
is the layer between evidence and implication — it is neither a data point nor a
recommendation.

**What a theme is:**
> "Returns are becoming infrastructure rather than a cost center — and the winner in that
> transition will be whoever controls the data layer, not the logistics layer."

**What a theme is not:**
> "The returns market is growing." ← data point
> "Companies should invest in returns technology." ← recommendation

**Theme development process:**

1. List all significant findings across all four pyramid levels
2. Group findings by structural relationship — what do multiple findings from different
   levels have in common?
3. Name the structural observation that explains the grouping — this is the theme headline
4. Identify the strategic implication for the subject company or investment thesis
5. Order themes by analytical importance — the most consequential theme leads

**Theme quality gates — each theme must pass all five:**
- [ ] Structural observation, not a data point or recommendation
- [ ] At least 3 pyramid-level findings from at least 2 different levels support it
- [ ] Has a specific strategic implication — "so what" is concrete, not generic
- [ ] Is distinguishable from every other theme — no overlap
- [ ] Would not be dismissed as obvious by a skeptical IC member

**Count calibration:** 4 themes minimum, 6 maximum. Fewer than 4 means insufficient
synthesis — findings are still siloed by pyramid level. More than 6 means themes haven't
been consolidated and are still closer to data points.

### NTB Readiness Check — run at end of Phase 3

When the research will feed an IC memo with a Need-to-Believe registry, each theme must
be tested for NTB alignment before drafting begins. This ensures the research output is
structured to feed the NTB evidence column rather than requiring manual translation.

**For each NTB in the IC memo (or anticipated NTBs):**
```
NTB ALIGNMENT CHECK

NTB [#]: [Statement]
Theme(s) that address it: [Theme names]
Evidence in hand [F]: [Named sources with confidence tier]
Evidence conditional [E]: [Reasoned estimates with stated assumptions]
Evidence missing [GAP]: [Specific data not yet obtained — name the gap precisely]
Minimum bullets for NTB findings column: 6 (see calibration below)
```

**The 6-bullet rule — calibration and exceptions:**

The minimum of 6 evidence bullets per NTB comes from ntb-diligence Phase 3 — the
downstream skill that consumes this research's NTB-ready findings. Fewer than 6 means
the evidence base is too thin to support confidence in the NTB, and the downstream
stress test in ntb-diligence will inherit that weakness.

- **If 6 bullets aren't achievable:** That's informative, not a research failure. Flag
  the NTB explicitly as GAP-state and note the thin evidence in the Phase 3 output —
  do not pad with weak evidence to hit the count.
- **If an NTB has 12+ bullets:** Also informative — it usually means the NTB is
  over-scoped and should be split into two tighter NTBs, or some bullets are
  redundant and should be consolidated. Flag for Phase 2 NTB revision.
- **Target range for a well-scoped NTB:** 6–10 bullets. Numbers outside this range
  signal either a coverage gap (low) or an NTB that hasn't been sharpened enough (high).

If a research theme produces findings that cannot be mapped to any NTB, that theme is
contextual background — label it as such in the document structure. NTB-mapped themes
lead; contextual themes follow.

**Findings format for NTB-destined evidence:**

When findings will populate the NTB Key Findings column (either in an IC memo NTB
registry or as input to ntb-diligence Phase 3), write them in NTB-ready format during
research (not during drafting) so they transfer without reformatting.

**Format — matches ntb-diligence Phase 3 evidence inventory structure:**

For each NTB, organize findings as four grouped blocks:

```
NTB [#]: [Statement]

Confirmed evidence [F] — lead with hardest evidence; named sources; include confidence tier:
  • [Finding] [F — Source name Month Year, HIGH]
  • [Finding] [F — Source name Month Year, MEDIUM]
  • ...

Conditional evidence [E] — reasoned estimates with stated assumptions:
  • [Finding] [E — Pattern derivation from X and Y, assumption: Z]
  • ...

Hypothesis [H] — directionally plausible but not yet tested:
  • [Finding] [H — inferred from MELI analogy; not confirmed by primary data]
  • ...

Gaps [GAP] — primary data not yet obtained:
  • GAP: [Specific data not yet obtained] — [Info Gap number if assigned]
  • ...
```

**Rules:**
- Lead each bullet with the specific fact, figure, or observation — not an interpretive sentence
- Group by tag type ([F], [E], [H], [GAP]) — do not intersperse
- One finding per bullet — do not combine two observations into one bullet
- GAP format uses the explicit "GAP:" prefix for visibility in downstream rendering

This format transfers directly into ntb-diligence Phase 3 evidence inventory without
reformatting — the grouped-by-tag structure is the same. It is also compatible with
the DATA GAP callout format in pattern-docx, which uses an orange left-border paragraph
for unresolved primary data items.

---

## Phase 4: Draft — Report Architecture

**The report is organized by themes, not pyramid levels.** Pyramid levels are analytical
scaffolding. They do not appear as section headers in the final output.

### Document Structure

```
1.  Cover
2.  Executive Summary       — governing synthesis: themes distilled to 3–5 sentences,
                               answer first, then the evidence that earns it
3.  Market Context          — condensed Level 4 findings: establishes the stage
                               (1–2 pages / 1–2 slides). Not the full analysis.
4.  [Theme 1 Section]
5.  [Theme 2 Section]
6.  [Theme 3 Section]
7.  [Theme 4 Section]
8.  [Theme 5–6 Section]     — if warranted
9.  Strategic Implications  — what the themes mean for the company or investment decision
                               Owner + timeline per implication
10. Appendix                — sources, methodology, detailed sizing model, CRAAP scores
```

**When feeding an IC memo:** Add a section after Strategic Implications:

```
11. NTB Evidence Summary    — for each NTB, a bulleted evidence inventory in NTB-ready
                               format (evidence-tagged, gap-flagged, source-cited)
                               This section feeds the NTB registry directly — it is not
                               a narrative summary of the research
```

**Calibration:**
- Market context: 1–2 pages
- Each theme section: 2–4 pages (DOCX) / 2–3 slides (PPTX)
- Strategic implications: 1–2 pages
- NTB Evidence Summary (if applicable): 1 page per NTB
- Appendix: as needed

### Section Anatomy — apply to every theme section

Every theme section must follow this internal structure exactly. Sections that deviate
produce the data-dump output the iteration loop exists to catch.

**1. Section headline — governing insight**
A complete declarative sentence stating the theme as a finding. Not a label. Not a
data point. A reader who sees only this sentence must understand the structural
observation and why it matters.

❌ Label: "Competitive Landscape"
❌ Data point: "The market has grown 34% over three years"
✅ Governing insight: "Two platforms have structurally separated from the field —
   but the separation is built on logistics density that smaller entrants cannot
   replicate without a decade of capital deployment"

**2. Framing paragraph — SCR construction**
3–4 sentences maximum. Situation → Complication → Resolution:
- *Situation:* What is true and uncontested — the shared starting point
- *Complication:* What has changed or is at stake — the tension this section addresses
- *Resolution:* The structural observation this section will substantiate

The framing paragraph orients the reader. It contains no evidence. Evidence comes next.

**3. Evidence blocks — 2–4 per section**
Each block establishes one supporting point for the theme:
- Opening sentence: states the point being evidenced
- Body: 2–4 sentences of specific evidence (named sources, named companies,
  specific numbers with inline citations)
- Closing sentence: draws the implication of this evidence for the theme

Evidence blocks are not data dumps. Every figure must connect to the argument.
A statistic cited without an interpretive sentence is not an analytical finding.

**4. Section synthesis — so-what close**
1–2 sentences. States what the evidence in this section means for the governing
argument. Every section closes with an implication. Sections that trail off into
data without drawing a conclusion are unfinished.

---

## Phase 5: Iteration Loop

Three sequential passes. Each pass must complete and all flagged issues must be hardened
before advancing to the next pass. Do not run passes in parallel. Do not skip passes
because the draft "looks good."

**Pre-mortem is not part of market-research.** Pre-mortem is an investment-thesis
stress-test that assumes the thesis has failed and works backward to failure modes.
Market research is evidence gathering and synthesis, not thesis stress-testing — so
pre-mortem runs in the IC memo workflow (after red-team), not here. If a market
research project is producing evidence that will feed a downstream investment thesis,
the downstream workflow (ic-memo or ntb-diligence) invokes pre-mortem against the
thesis, using this research as input.

### Pass 1 — writing-style self-review
**Owner:** writing-style skill
**Scope:** Every section of the draft
**What it checks:**
- Claim tagging (F/E/H) — every material claim tagged
- Absolute assertion test — unsupported superlatives, consulting boilerplate, circular
  constructions, exclusivity terms
- Epistemic language standards — causal claims have stated mechanisms; multi-step causal
  claims have complete inductive chains (outcome → proximate driver → gating constraint
  → observable condition, no skipped links)
- Data gap flagging — thin or conflicting evidence flagged inline, not papered over
- Prose standards — paragraph architecture, sentence construction, transitions, tables

**Hardening before Pass 2:** Rewrite every flagged item. Do not advance with open flags.

### Pass 2 — claim-scrutinizer redline
**Owner:** claim-scrutinizer skill
**Scope:** Every material claim
**What it checks:**
- Logic tree reconstruction — does the argument structure hold?
- Assumption audit — unstated premises surfaced and rated
- 7-part test per claim: evidence standard, logic, MECE, quantification, circular
  reasoning, cherry-picking, projection scrutiny
- Derivative integrity — math checked, cascade validated
- Base rate check — thesis-critical quantitative claims benchmarked
- CRAAP-scored evidence — every cited source rated; thesis-critical claims require HIGH
  confidence (3+ converging Tier 1–2 sources)

**Hardening before Pass 3:** Address every flagged claim. For NEEDS EVIDENCE flags:
either find the evidence and add it, or downgrade the claim to hypothesis and flag it
explicitly. Do not advance claims that fail the evidence standard.

### Pass 3 — red-team adversarial pass
**Owner:** red-team skill
**Scope:** Governing thesis and all load-bearing pillars
**What it checks:**
- Logic tree — load-bearing vs. non-load-bearing pillars
- Attack vectors per pillar — affirmative counter-claims with substantiation
- Kill scenarios — top 3 scenarios under which the thesis fails entirely
- Claim-level adversarial verdicts — Scrutinizer Verdict + Attack Severity per claim
- Unstated assumption attacks
- Bear case — coherent adversarial argument against the governing conclusion
- Adversarial scorecard — KILL / WOUND / EXPOSE / SURVIVES counts, thesis survivability

**Hardening before Phase 6:** Address every KILL and WOUND. For KILL-rated claims: either
harden with additional evidence, qualify the claim to match what the evidence supports,
or remove it. A document with open KILL-rated claims is not publication-ready.

### Exit criteria — Phase 5 complete when:
- All Pass 1 writing-style flags addressed
- All Pass 2 claim-scrutinizer flags hardened; no open NEEDS EVIDENCE on thesis-critical claims
- All Pass 3 red-team KILL and WOUND ratings addressed
- Draft is ready for file generation in Phase 6

---

## Phase 6: Output

Generate the final file via pattern-docx (long-form report) or pattern-investment-pptx
(deck). writing-style runs one more time inside the production skill before any code is
written. Final output is transplanted into the canonical Pattern template shell for
correct header, footer, logo, and gradient rendering.

---

## Phase 7: QA Gate — doc-quality-checker

**Owner:** doc-quality-checker skill
**Scope:** Entire produced file (.docx or .pptx)
**Runs:** Immediately after Phase 6 output — do not wait to be asked

**What it checks:**
- Brand formatting compliance (fonts, colors, spacing, margins)
- Structural logic (heading hierarchy, page breaks, orphaned headings)
- Header/footer integrity
- Table integrity (widths, column headers, alternating rows, borders)
- Content quality (placeholder text, number formatting, internal consistency)
- Narrative flow — slide/section titles are insight statements, not labels; titles
  tell a coherent story in sequence; exec summary states a point of view

**Output is final only when doc-quality-checker returns zero CRITICAL issues.**

---

## Source Strategy

The tiers below define which sources qualify for which kinds of claims. The CRAAP scoring
rubric — which determines how individual sources within a tier are rated for Currency,
Relevance, Authority, Accuracy, and Purpose — lives in `mckinsey-consultant`. Load it
before rating any source:

```
Read: /mnt/skills/user/mckinsey-consultant/references/VALIDATION_FRAMEWORKS.md
```

The tier structure here tells you which sources are acceptable; CRAAP tells you how to
rate them within that tier.

### Tier 1 — Primary Evidence
Require for all thesis-critical findings. Minimum 2–3 independent Tier 1–2 sources
for triangulation.
- Government data: Census, BLS, BEA, SEC EDGAR, FDA, FTC, World Bank, IMF, OECD
- Peer-reviewed research: Google Scholar, SSRN, JSTOR, PubMed
- Public company filings: 10-K, 10-Q, S-1, earnings transcripts, earnings call
  transcripts

### Tier 2 — Supporting Evidence
Corroborate Tier 1. Do not use as sole source for thesis-critical claims.
- Industry associations and trade body research
- Established analyst firms: Gartner, IDC, Forrester, McKinsey Global Institute,
  Deloitte Insights, PwC, BCG (public research only)
- Trade publications with editorial standards
- Think tanks: Brookings, Pew Research

### Tier 3 — Context Only
Frame and orient. Never substantiate.
- Company white papers and marketing content
- General media (WSJ, FT, Bloomberg) for narrative context
- LinkedIn, job postings — capability signals only

**Triangulation rule:** All thesis-critical findings must be validated with 2–3
independent Tier 1–2 sources. A single Tier 1 source is insufficient for any claim
that, if wrong, would weaken the governing thesis.

**Confidence labeling (mandatory on all claims):**
- **High [H]:** 3+ independent Tier 1–2 sources converge
- **Medium [M]:** 2 sources align; some methodology limitations
- **Low [L]:** Single source or sources diverge — always state caveat explicitly in prose

**Free sources directory:**
```
Read: {SKILL_DIR}/references/FREE_SOURCES_GUIDE.md
```

---

## Citation Format

Apply inline during research — not retrospectively during drafting.

**Inline format (every claim that uses external evidence):**
```
[Source name, Year] [H/M/L]
```
Example: *"Southeast Asian e-commerce GMV reached $131B in 2023 [Google-Temasek-Bain, 2023] [H]"*

**Full entry format (source-bibliography.md):**
```
[Author/Org]. ([Year]). [Title]. [Publisher]. [URL]
Pyramid level: L4 / L3 / L2 / L1
CRAAP: C[x] / R[x] / A[x] / A[x] / P[x] = [total] / 25
Confidence: HIGH / MEDIUM / LOW
Triangulation: Converged / Partial / Single source
Key findings used: [bullet list]
```

**Data gap flag format (when evidence is thin):**
```
DATA GAP: "[Claim]" — [reason: single source / sources conflict / no third-party
validation / web search returned no usable results]. Warrants [specific action]
before treating as confirmed.
```

---

## Validation Protocol

Apply CRAAP scoring to all sources. Minimum score of 18/25 required for Tier 1
evidence use. Load full scoring rubric:
```
Read: /mnt/skills/user/mckinsey-consultant/references/VALIDATION_FRAMEWORKS.md
```

| Criterion | Score 1–5 | Key question |
|-----------|-----------|--------------|
| **Currency** | | Published within timeframe appropriate for this market's rate of change? |
| **Relevance** | | Right geography, sector, and audience? Direct or requires extrapolation? |
| **Authority** | | Tier 1 → Tier 2 → Tier 3? Credentials and incentives? |
| **Accuracy** | | Methodology transparent? Claims verifiable? Citations present? |
| **Purpose** | | Research intent vs. promotional or advocacy bias? |

---

## Quality Gates — Final Checklist

A deliverable is ready for output only when every item below passes.

**Research completeness**
- [ ] All four pyramid levels completed; no level skipped or abbreviated
  (IC Memo Mode: L4, L3, L2 only; L1 skipped per constrained mode)
- [ ] Domain template checked at Phase 1 intake; if loaded, pre-loaded data marked
      [F] and open questions in brief
- [ ] Staleness check run on domain template; time-sensitive data refreshed in Phase 2
- [ ] Every thesis-critical quantitative claim triangulated (2–3 independent Tier 1–2 sources)
- [ ] All confidence levels labeled inline (H/M/L)
- [ ] All data gaps flagged explicitly — none papered over

**Theme development**
- [ ] 4–6 themes developed; each passes all five theme quality gates
- [ ] Themes are structural observations, not data points or recommendations
- [ ] Each theme has a specific strategic implication for the subject company/thesis
- [ ] NTB Readiness Check complete (when research feeds an IC memo with NTB registry):
      every NTB mapped to ≥1 theme; 6-bullet minimum calibrated per NTB; grouped-by-tag
      format used for findings intended to transfer to ntb-diligence

**Draft architecture**
- [ ] Document organized by themes, not pyramid levels
- [ ] Every theme section follows the four-element Section Anatomy
- [ ] Every named competitor has a complete six-element Competitor Profile
- [ ] Executive summary leads with the governing synthesis, not a topic preview
- [ ] Every section headline is a governing insight statement, not a label

**Iteration loop (Phase 5 — 3 passes)**
- [ ] Pass 1 complete — all writing-style flags hardened
- [ ] Pass 2 complete — all claim-scrutinizer flags addressed; no open NEEDS EVIDENCE
      on thesis-critical claims
- [ ] Pass 3 complete — all red-team KILL and WOUND ratings addressed
- [ ] Pre-mortem explicitly not run in this skill (runs in downstream ic-memo workflow
      if applicable)

**Output + QA (Phase 6 + Phase 7)**
- [ ] Phase 6 output file generated via pattern-docx or pattern-investment-pptx
- [ ] Phase 7 doc-quality-checker returned zero CRITICAL issues on the produced file

**Claim integrity (governed by writing-style and claim-scrutinizer)**
- [ ] Every material claim tagged F / E / H
- [ ] No unsupported superlatives, consulting boilerplate, or circular constructions
- [ ] Every multi-step causal claim has a complete inductive chain
- [ ] Every gap-closing or timeline claim is condition-based unless a known rate
      produces the number
- [ ] No exclusivity terms ("only," "solely," "inevitably") without eliminated alternatives

---

## References

**Research brief template:**
```
Read: {SKILL_DIR}/references/research-brief.md
```

**Analytical prompt sets by pyramid level:**
```
Read: {SKILL_DIR}/references/analytical-prompts.md
```

**Source bibliography tracker (CRAAP scoring, triangulation matrix):**
```
Read: {SKILL_DIR}/references/source-bibliography.md
```

**Free data sources directory (Tier 1–3 by category):**
```
Read: {SKILL_DIR}/references/FREE_SOURCES_GUIDE.md
```

**CRAAP scoring rubric and triangulation matrix (full):**
```
Read: /mnt/skills/user/mckinsey-consultant/references/VALIDATION_FRAMEWORKS.md
```
