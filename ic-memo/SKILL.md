---
name: ic-memo
description: |
  Write a structured, publication-ready Investment Committee memo for a PE buyout,
  acquisition, or strategic investment. Use this skill whenever Ian asks to "write
  the IC memo," "draft the investment memo," "build the IC package," "write up the
  deal," "draft the investment thesis memo," or "put together the IC write-up."
  Also triggers for: "memo for IC," "investment committee write-up," "deal memo,"
  "write up the thesis," "IC-ready memo."

  This skill governs IC memo document architecture — section structure, length
  calibration, how the Six Screening Questions map to memo sections, and formatting
  via pattern-docx. It does not govern: analytical methodology (mckinsey-consultant),
  Six Screening Questions content (investment-evaluation-framework.md), claim standards
  (writing-style), logic redlining (claim-scrutinizer), adversarial stress-testing
  (red-team), or moat evidence methodology (competitive-moat-assessment). Defer to
  those skills for their respective responsibilities.
---

# IC Memo Skill

You are writing an Investment Committee memo. Read this entire file before beginning.

An IC memo is not a market research report. It is not a strategy deck. It is a document
that makes a specific, evidence-backed recommendation to a small group of experienced
investors who will challenge every assertion. The governing discipline is precision under
pressure — every claim must survive a hostile question from an IC member who has read
the same CIM and talked to the same management team.

---

## Skill Architecture

```
ic-memo              ← YOU ARE HERE — document architecture, section structure, formatting
      │
      ├── investment-evaluation-framework.md  ← Six Screening Questions as gate structure
      │   Read: /mnt/skills/user/mckinsey-consultant/references/investment-evaluation-framework.md
      │
      ├── mckinsey-consultant          ← analytical methodology, pyramid principle, SCR
      │
      ├── ntb-diligence                ← (OPTIONAL UPSTREAM) standalone NTB diligence
      │   Run FIRST when the deal warrants structured NTB analysis.
      │   Produces NTB registry + diligence plan + stress test that feed Sections 4, 7, 9.
      │   When ntb-diligence has run, do NOT re-derive NTBs inline — consume its output.
      │   Read: /mnt/skills/user/ntb-diligence/SKILL.md
      │
      ├── market-research              ← evidence gathering for Sections 4, 5, 6
      │   Runs in IC memo mode: no standalone intake, no standalone output
      │   Pyramid levels: L4 (market) → L3 (customer) → L2 (competitive) only
      │   L1 (company position) handled by ic-memo directly via intake materials
      │   Theme count: 3–4 (not 4–6) — IC memo is tighter than a standalone report
      │   Output: evidence inputs to memo sections, not a standalone deliverable
      │
      ├── competitive-moat-assessment  ← moat evidence methodology (load after L2 research)
      │   Uses L2 findings as inputs — run after market-research L2 completes
      │
      ├── writing-style                ← prose standards, inductive chain, claim tagging
      │                                   Run self-review before generating any file
      │
      ├── claim-scrutinizer            ← seven-part test, assumption audit, base rates
      │                                   Run full redline after first draft
      │
      ├── red-team                     ← adversarial pass using investment attack lenses
      │                                   Run after claim-scrutinizer hardening
      │
      ├── pre-mortem                   ← failure mode inventory with NTB mapping
      │                                   Run after red-team; extends stress test coverage
      │
      └── pattern-docx                 ← file output
          doc-quality-checker          ← run immediately after file delivery
```

**Load order:** Read investment-evaluation-framework.md first. Then follow this skill
for document architecture. Defer to named skills for their responsibilities.

**market-research in IC memo context:** market-research runs in a constrained mode
within the IC memo workflow. It does not run its own intake protocol (ic-memo already
captured the required inputs). It does not produce a standalone deliverable. It
produces evidence — sourced, cited, triangulated findings — that feed directly into
memo sections. This is the critical distinction: market-research is the evidence
layer; ic-memo is the document layer.

**ntb-diligence in IC memo context:** ntb-diligence is optional but recommended for any
deal where the investment thesis rests on 4+ distinct assumptions with meaningful MOIC
impact each. When it has been run upstream of this skill, its output is the authoritative
source for the NTB framing — the NTB registry feeds Section 4 (thesis pillars are
derived from NTBs), the diligence plan feeds Section 10 open items, and the stress
tests feed Section 9 (risks) with ready-made leading indicators and kill criteria.
Do NOT re-derive the NTBs inline when ntb-diligence has already produced them.

---

## Before Writing Anything

**Load the investment evaluation framework:**
```
Read: /mnt/skills/user/mckinsey-consultant/references/investment-evaluation-framework.md
```

**Check for a matching domain template:**
Scan the company or topic against `/mnt/skills/user/ic-memo/references/domain-templates/`
for any file whose trigger list matches. If a match is found, load it immediately — it
pre-loads confirmed data, prior NTB diligence output, Gate 2 scorecards, pre-mortem
failure modes, and open questions that would otherwise require re-gathering.

Currently available IC memo domain templates:
- `sea-ltd-sea-brazil.md` — Sea Limited (NYSE: SE), Shopee, Monee, SPX Express, Garena,
  SEA e-commerce investment, MELI vs Sea, TikTok Shop SEA, any SEA country e-commerce

State in the intake output: "Domain template loaded: [filename]. [N] confirmed data
points pre-loaded. [N] open questions carried forward from prior analysis."

**Check for ntb-diligence upstream output:**
If ntb-diligence has already been run on this deal (either in the current session or
referenced as prior work), treat its Phase 3 NTB registry, Phase 3 diligence plan, and
Phase 4 stress tests as authoritative inputs. Do NOT re-derive the NTBs during drafting.
The NTB registry becomes the structural frame for Section 4 thesis pillars; the diligence
plan feeds Section 10 open items; the stress tests feed Section 9 risks.

Then collect the following. Do not begin writing until all critical inputs are in hand.

**Required:**
- Company name and one-line description
- Deal type: PE buyout / strategic acquisition / minority investment / other
- Entry valuation and deal structure
- Investment thesis (working hypothesis — will be refined)
- Hold period and target return

**Helpful but not blocking:**
- CIM, management presentation, or prior research (attach or paste)
- Known diligence findings to date
- Specific IC concerns or questions to address
- Any prior investment memos on comparable deals for calibration
- Prior ntb-diligence output if one exists (skip NTB re-derivation)
- Prior pre-mortem output if one exists (feeds Section 9 risks)

If a CIM or research document is attached, read it fully before asking any questions.
Extract what you can; ask only for genuine gaps.

---

## Intake Protocol

When this skill is triggered without sufficient context, ask all of the following in
one structured message. Do not ask questions one at a time.

---
Before I draft the IC memo, I need a few inputs:

**1. The company**
Name, what they do, who they sell to, revenue/ARR scale.

**2. The deal**
Type (buyout / acquisition / minority), entry valuation, deal structure, hold period.

**3. The thesis**
Your working investment thesis — what makes this a good investment at this price?
Even a rough version is fine; I'll pressure-test and sharpen it.

**4. The decision context**
Is this a first look, a go/no-go before LOI, or a final IC presentation?
This determines depth and emphasis.

**5. Known risks or IC concerns**
What are the 1–2 things that will face the hardest questions at IC?

**6. Existing materials**
Attach or paste any CIM, management deck, research, or prior memos.

---

**After receiving inputs:**
- Confirm your understanding of the thesis in one sentence
- Flag any critical inputs still missing
- State which Six Screening Questions have strong vs. thin evidence before beginning

---

## IC Memo Architecture

A Pattern IC memo has nine sections in this exact order. Do not reorder or combine.
Section length calibrations assume a final memo of 8–12 pages for a standard buyout.
Adjust proportionally for first-look (4–6 pages) vs. final IC (12–15 pages).

```
1.  Cover Block
2.  Executive Summary          (1 page)
3.  Company Overview           (0.5–1 page)
4.  Investment Thesis          (1–1.5 pages)
5.  Market & Competitive       (1–1.5 pages)
6.  Business Quality           (1.5–2 pages)
7.  Financial Analysis         (1–1.5 pages)
8.  Deal Structure & Returns   (1 page)
9.  Risks & Mitigants          (1 page)
10. IC Recommendation          (0.5 page)
```

---

## Market Research Phase — Runs Before Drafting

**Before writing any memo sections, execute the market-research pyramid for Levels
4, 3, and 2.** This produces the evidence base that Sections 4, 5, and 6 draw from.
Without this phase, those sections will rely on CIM-sourced claims that have not been
independently triangulated — which will fail claim-scrutinizer Pass 2.

```
Read: /mnt/skills/user/market-research/SKILL.md → IC Memo Mode (below)
```

### IC Memo Mode — How market-research Runs Within an IC Memo

market-research runs in a constrained mode here. Three differences from standalone:

**1. No intake protocol**
The ic-memo intake already captured: company, market, deal context, key questions,
and known data challenges. Do not run market-research's own intake. Pass the ic-memo
intake responses directly as context.

**2. Scoped pyramid — L4, L3, L2 only**
- **Level 4 (Market):** TAM/SAM with top-down and bottom-up, CAGR with source and
  base year, 2–3 structural trends with named evidence. Feeds Section 5 (market block)
  and Section 4 (thesis — sector timing pillar).
- **Level 3 (Customer):** Who has the problem, top 2–3 segments with JTBD framing,
  primary barriers. Feeds Section 6b (customer quality) and Section 4 (customer
  value pillar).
- **Level 2 (Competitive):** Top 3–5 competitors with full 6-element profiles,
  positioning map, white space. Feeds Section 5 (competitive block) and hands off
  to competitive-moat-assessment.
- **Level 1 (Company position):** Skip — ic-memo handles this directly via intake
  materials, CIM, and management presentation.

**3. No standalone deliverable**
market-research does not produce a report or deck here. It produces a structured
evidence summary — findings organized by pyramid level with inline citations
([Source, Year] [H/M/L]) — that feeds directly into memo drafting. Theme development
is condensed: 3–4 themes maximum, structured around the investment thesis pillars
rather than independent structural observations.

### Evidence Handoff Format

After market-research completes, organize findings as:

```
MARKET RESEARCH EVIDENCE SUMMARY — [Company Name]

L4 FINDINGS (feeds Sections 4 + 5 market block):
  - Market size: [figure] [source] [confidence]
  - CAGR: [figure] [source, base year] [confidence]
  - Trend 1: [finding] → [implication for thesis]
  - Trend 2: [finding] → [implication for thesis]
  - DATA GAPS: [any flagged gaps]

L3 FINDINGS (feeds Section 6b):
  - Segment 1: [JTBD framing] [evidence]
  - Segment 2: [JTBD framing] [evidence]
  - Primary barrier: [finding] [evidence]
  - DATA GAPS: [any flagged gaps]

L2 FINDINGS (feeds Section 5 competitive block + competitive-moat-assessment):
  - Competitor 1: [6-element profile]
  - Competitor 2: [6-element profile]
  - Positioning: [white space finding]
  - DATA GAPS: [any flagged gaps]
```

Once this summary is produced, run **competitive-moat-assessment** using the L2
findings as inputs before beginning memo drafting.

---

## Section-by-Section Instructions

### Section Architecture — Prescribed vs. Custom

The 10-section structure below is the default prescribed architecture for a PE buyout or
acquisition memo. Public equity long memos and certain deal structures may use a
compressed 8-section variant that combines some sections:

| Prescribed (PE buyout) | Compressed (public equity long) |
|------------------------|----------------------------------|
| 1. Cover Block | 1. Cover Block |
| 2. Executive Summary | 2. Executive Summary |
| 3. Company Overview | 3. Company Overview |
| 4. Investment Thesis | 4. Investment Thesis (with NTB registry) |
| 5. Market & Competitive Position | 5. Market & Competitive Position |
| 6. Business Quality | (merged into Section 4 Investment Thesis) |
| 7. Financial Analysis | 6. Unit Economics & Valuation (combined) |
| 8. Deal Structure & Exit | (N/A for public equity long) |
| 9. Risks & Mitigants | 7. Risk Analysis & Pre-Mortem |
| 10. IC Recommendation | 8. Investment Recommendation |

**When to use compressed 8-section:** Public equity long positions where Deal Structure &
Exit is not a discrete negotiation item (you buy shares at market), and where Business
Quality is most naturally integrated with the Investment Thesis pillars rather than
stood up as a separate section.

**When to use prescribed 10-section:** PE buyout, acquisition, or strategic investment
where deal structure is a live negotiation, where Gates 4-5 (Exit Realization and Owner
Fit) require their own treatment, and where Gate 1 (Company Quality) warrants a full
Business Quality section distinct from the thesis argument.

**The discipline is the same for both.** The Six Screening Questions map to sections
in each architecture; claim standards, reconciliation, and output passes apply
identically. The divergence is structural, not analytical.

If you are unsure which architecture applies, ask before drafting — the answer depends
on deal type and Ian's preference for the specific investment.

---

### Section 1: Cover Block

Pattern-docx Normal paragraphs with run-level formatting. No heading style.

```
[Company Name]                          36pt, SemiBold, color 1F4E79
Investment Committee Memorandum         20pt, color 2E75B6
[Deal type] | [Date] | CONFIDENTIAL     italic, color 595959
[blank line]
CONFIDENTIAL — FOR AUTHORIZED RECIPIENTS ONLY    9pt, Bold, color C00000
```

---

### Section 2: Executive Summary (1 page / ~400 words)

**This is the most important section.** IC members read this first and many read only
this. If the executive summary is unclear or buried, the memo fails regardless of
the quality of subsequent sections.

**Invoke executive-summary-writer skill for this section:**
```
Read: /mnt/skills/user/executive-summary-writer/SKILL.md → Format A (One-Page Memo)
```

Structure (five blocks in order):
1. **Governing thesis** (2 sentences) — conclusion first, specific and direct
2. **Three supporting arguments** (1 paragraph each, ~60 words) — pillar → evidence → implication
3. **Primary risk** (2 sentences) — named directly, not softened
4. **Recommended action** (3–4 bullets) — owner, timeline, binary
5. **Key assumption** (1 sentence) — the single premise the recommendation rests on

The executive summary must be self-contained. A reader who reads only this section
must be able to answer: what is the conclusion, why is it correct, what is the biggest
risk, and what happens next.

---

### Section 3: Company Overview (0.5–1 page)

Factual orientation. Not analytical. Sets the stage for the thesis.

**Required elements:**
- Business description: what they do, how they make money, who they serve
- Scale: revenue/ARR, headcount, geography, customer count
- History: founding, key milestones, ownership history
- Current ownership and deal origin (proprietary / lightly banked / auctioned)

**Length discipline:** This section has a hard ceiling of 1 page. If it runs longer,
content belongs in the Business Quality section or an appendix.

**Claim standard:** All figures cited here are facts — sourced from CIM, management
presentation, or public filings. No estimates in this section without explicit labeling.

---

### Section 4: Investment Thesis (1–1.5 pages)

The affirmative case for the investment, structured as a pyramid.

**Structure:**
- **Governing thesis** (1 sentence) — the single most important reason this is a
  good investment at this price
- **Three thesis pillars** (1 paragraph each) — each must independently support the
  governing thesis; together they must make it inescapable

**Pillar construction standard:**
Each pillar follows inductive chain discipline (governed by writing-style):
- Outcome variable: what end state is being claimed?
- Proximate driver: what directly produces that outcome?
- Gating constraint: what must be true for the driver to operate?
- Observable condition: what specific, measurable thing confirms the constraint is met?

A pillar that skips any link in the chain is an assertion, not an argument.

**Label every claim:** [F] fact / [E] estimate / [H] hypothesis

**Gate coverage:** The three pillars must collectively address at minimum:
- Gate 1 (Company Quality) — why is this a genuinely good business?
- Gate 2 (Sector Timing) — why is now the right time?
- Gate 3 (Investment Attractiveness) — why at this price?

Gates 4–6 are addressed in subsequent sections. Do not try to cover all six gates
in the thesis section — that produces an unfocused document.

---

### Section 5: Market & Competitive Position (1–1.5 pages)

**Evidence source:** Draw from the Market Research Evidence Summary produced in the
Market Research Phase above. Do not re-research here — compress and synthesize the
L4 and L2 findings into the memo's length constraints.

**Structure:**
- **Market** (0.5 page): TAM/SAM with methodology stated, CAGR with source and base
  year, 2–3 structural trends with named evidence. All figures drawn from L4 findings
  — cite inline as [Source, Year] [H/M/L].
- **Competitive position** (0.5–1 page): top 3–5 competitors summarized from L2
  profiles. Each competitor gets 2–3 sentences: what they do, their primary advantage,
  and their key weakness. Full 6-element profiles live in the appendix if needed.
  Moat verdict drawn from competitive-moat-assessment output.

**For competitive position — invoke competitive-moat-assessment using L2 findings:**
```
Read: /mnt/skills/user/competitive-moat-assessment/SKILL.md
```
competitive-moat-assessment receives the L2 competitor profiles as inputs and produces
the moat verdict. This verdict — not the competitor profiles themselves — is the
primary output of the competitive section.

This section must name competitors and state their positions. Generic competitive
landscape descriptions ("the market is fragmented with many players") do not pass.

**Gate coverage:** Addresses Gate 2 (Sector Timing) and Gate 1 competitive position
sub-question.

---

### Section 6: Business Quality (1.5–2 pages)

The deepest analytical section. Addresses Gate 1 in full.

**Required subsections:**

**6a. Business Model & Unit Economics**
- Revenue model mechanics: how money is made, what drives it
- Gross margin with benchmark comparison [E if estimated, source if cited]
- Unit economics: CAC, LTV, payback period — label each as fact/estimate/hypothesis
- Key margin lever: the single most important driver of economics improvement

**6b. Customer Quality**
- Retention metrics: GRR, NRR — with cohort-level data if available
- Customer concentration: top 10 as % of revenue
- Expansion signals: net expansion rate, upsell attach rate
- Any known customer health issues — do not omit

**6c. Management Assessment**
- Track record: specific companies, specific roles, specific outcomes — not titles
- Alignment: equity, vesting, earnout structure
- Gap: the single most important capability gap and how it gets filled

**6d. Competitive Moat** (summary — full analysis in Section 5)
- Moat type stated explicitly (network effect / switching cost / scale / IP / brand)
- Durability assessment: what would it take to neutralize this moat in 3–5 years?
- One sentence verdict: strong / moderate / weak — and why

**Gate coverage:** Addresses Gate 1 (Company Quality) in full.

---

### Section 7: Financial Analysis (1–1.5 pages)

**Required elements:**

**7a. Historical Performance**
- Revenue and EBITDA for last 3 years — monthly cadence signals, annual for context
- Growth rate trajectory — is it accelerating, stable, or decelerating?
- Margin trajectory — are margins expanding or compressing and why?
- Any non-recurring items, restatements, or QoE adjustments — flag explicitly

**7b. Base Case Model**
- Revenue CAGR over hold period with stated assumptions
- EBITDA margin at exit with stated expansion mechanism
- Three key assumptions that drive the model — label each F/E/H
- Sensitivity: what happens if the single most optimistic assumption reverts to
  historical average or sector median?

**7c. Return Analysis**
- Base case IRR and MOIC at stated entry and exit multiples
- Exit multiple assumption vs. current comps — justify any premium
- Downside case: revenue at 50% of base, no margin expansion, exit multiple −2 turns.
  State the IRR. If below fund hurdle, explain why downside is unlikely.

**Gate coverage:** Addresses Gate 3 (Investment Attractiveness) in full.

---

### Section 8: Deal Structure & Exit (1 page)

**Structure:**

**8a. Deal Structure**
- Entry valuation and implied multiple
- Capital structure: equity, debt, any seller rollover or earnout
- Key terms: governance rights, board composition, protective provisions
- Co-investors if any

**8b. Exit Analysis**
- Primary exit path with named likely buyers (strategic) or buyer universe (sponsor)
- Exit multiple assumption and basis for it
- Timeline and what milestones enable it
- Backup exit paths if primary path is unavailable

**Gate coverage:** Addresses Gate 4 (Exit Realization) and Gate 5 (Owner Fit).

---

### Section 9: Risks & Mitigants (1 page)

**Format:** Risk register table — not a narrative list.

| # | Risk | P | M | Score | Mitigant | Adequacy |
|---|------|---|---|-------|----------|----------|
| 1 | [specific risk] | 1–5 | 1–5 | P×M | [specific mitigant] | Adequate/Partial/Insufficient |

P = Probability (1=unlikely, 5=very likely)
M = Magnitude (1=negligible, 5=thesis-killing)
Score = P × M (range 1–25)

**Risk selection rules:**
- Minimum 5 risks, maximum 8
- At least one risk must score ≥15 (near-disqualifying)
- Risks must be specific and testable — not categories ("market risk," "execution risk")
- The primary risk from Section 2 (Executive Summary) must appear here with the
  highest or second-highest score
- Every risk scoring ≥9 must have a stated mitigant with adequacy assessment

**Gate coverage:** Addresses Gate 6 (Adversarial Diligence).

---

### Section 10: IC Recommendation (0.5 page)

**Four mandatory elements — all required, no exceptions:**

**1. Recommendation statement**
Direct, binary: "We recommend proceeding to LOI" / "We recommend passing at this
price" / "We recommend conditional approval subject to [specific conditions]."
No hedging. No "we believe this merits further consideration."

**2. Walk-away conditions**
Specific binary findings that, if confirmed, cause the recommendation to reverse.
Stated as observable facts, not risk categories.
- ❌ "Material customer concentration risk"
- ✅ "Top customer (18% of ARR) exercises termination-for-convenience clause confirmed
  in data room"

**3. Key assumption**
The single assumption the recommendation rests on, labeled explicitly as an assumption.
Named — not "market growth" but the specific figure, mechanism, and the evidence
that currently supports it.

**4. Open items before proceeding**
The specific questions that must be answered before a yes-vote is defensible. Named
questions, named owners, named deadlines — not "conduct further diligence."

**Gate coverage:** Synthesizes all six gates into a final binary verdict.

---

## Iteration Protocol

Run all five passes before delivering the final file.

**Pass 1 — writing-style self-review**
Draft all prose in plain text first. Run writing-style Steps 1–5 on every section.
Fix all flags before generating any code. Focus especially on: inductive chains in
Section 4 thesis pillars, exclusivity terms in moat claims, timeline claims in
financial analysis. Pass 1 also catches Group E draft artifact language — no "v[N]"
labels on cover, no "(NEW)" tags in section headers, no "pre-mortem addition:"
prefixes in body text, no FM codes in body text.
```
Read: /mnt/skills/user/writing-style/SKILL.md
```

**Pass 2 — claim-scrutinizer redline**
Full seven-part test on every material claim. Mandatory focus areas:
- Section 4: every pillar sub-claim passes logic and evidence tests
- Section 6: management track record claims pass the circular reasoning check
- Section 7: financial projections pass projection scrutiny and base rate check
- Section 10: walk-away conditions are binary, not risk categories
```
Read: /mnt/skills/user/claim-scrutinizer/SKILL.md
```

**Pass 3 — red-team adversarial pass**
Load Type A investment attack lenses. Attack load-bearing pillars first.
```
Read: /mnt/skills/user/red-team/SKILL.md
Read: /mnt/skills/user/red-team/references/red-team-investment-attacks.md
```

**Pass 4 — pre-mortem (failure mode inventory)**
Run after red-team hardening. Pre-mortem assumes the deal has already failed and works
backward through failure modes, extending the risk register with named mechanisms,
leading indicators, boundability assessments, and compound failure paths.
- If ntb-diligence ran upstream, pre-mortem maps every failure mode to the NTB it
  threatens using ntb-diligence's NTB numbering
- If the NTB registry was derived inline (no upstream ntb-diligence), pre-mortem uses
  the inline registry for NTB mapping
- Output feeds Section 9 risks and may trigger updates to Section 10 open items
```
Read: /mnt/skills/user/pre-mortem/SKILL.md
```

**Pass 4b — Numeric Consistency Reconciliation (mandatory after pre-mortem)**

The pre-mortem produces dollar and MOIC impact numbers in every material failure mode
deep dive. These numbers must reconcile to the valuation section — otherwise the document
contradicts itself internally.

Produce the reconciliation before Pass 5:

1. From Section 7 (Financial Analysis) or wherever the valuation lives, extract the
   authoritative Base Assumptions Table: entry equity, exit multiple, hold period, base
   case FY exit EBITDA and GMV, contribution margin rules.

2. For every pre-mortem 9-field deep dive's Failure Spectrum field, verify:
   - Every dollar figure reconciles to values in the Base Assumptions Table
   - Exit multiple used in MOIC conversion matches the valuation section base multiple
   - Hold period is consistent across every Failure Spectrum
   - "Severe failure" scenarios reconcile to the valuation section's Bear scenario
   - "Mild failure" scenarios do not exceed the Bull scenario deltas
   - No "Base case" language is used to label failure scenarios (collision with thesis
     base case) — Mild / Moderate / Severe or Failure spectrum language only

3. For every numeric claim that appears in more than one section (e.g., "$159B FY2029E
   GMV" in both investment thesis and valuation), verify the value is identical
   everywhere it appears. Flag any divergence.

4. For every multi-section metric with distinct period (e.g., "$127B FY2025 GMV" vs.
   "$159B FY2029E GMV"), verify the period label is explicit in every occurrence.

If any check fails, fix before Pass 5. Cross-section numeric contradictions are more
damaging than draft artifact language and must be resolved first.

This pass is owned by the pre-mortem skill's Section 6 ↔ Section 7 Reconciliation
procedure but must be explicitly re-run at the IC memo level because the pre-mortem
author may have drafted impact fields before the valuation section was finalized.

**Pass 4c — boundability (convert risk to underwriting action)**

Run after Pass 4 (pre-mortem) and Pass 4b (numeric reconciliation). Boundability
takes the failure mode registry produced by pre-mortem and converts each material
diligence item into specific underwriting actions across five buckets (model, price,
leverage, docs, operations) plus a deal-level verdict.

The unit of assessment in boundability is typically the NTB, not the individual
failure mode — this keeps the output organized around the thesis claims the IC will
debate rather than the underlying risk mechanisms. Each NTB receives one issue
object with six module scores (Perimeter, Timing, Data Quality, Outcome Range,
Precedent/Observability, Mitigants) and a final classification (Boundable /
Partially Boundable / Unboundable).

Boundability terminology matches pre-mortem (deliberately). An NTB classified
Boundable here must score ≥25/30 on the six modules; an NTB classified Partially
Boundable or Unboundable by pre-mortem should score <25. If pre-mortem and
boundability disagree on classification for the same item, resolve before delivery.

For public equity long positions (where there is no deal negotiation), the Leverage
and Docs buckets collapse; Price becomes "entry discipline" and Operations becomes
"monitoring cadence." For PE control buyouts, all five buckets are fully active.

```
Read: /mnt/skills/user/boundability/SKILL.md
```

**Pass 5 — doc-quality-checker**
Run immediately after file delivery. Do not wait to be asked. Catches any remaining
Group E draft artifact language that survived Pass 1 (version labels, changelog
subtitles, "pre-mortem addition:" prefixes, FM codes in body text) — all rated at
🔴 CRITICAL.
```
Read: /mnt/skills/user/doc-quality-checker/SKILL.md
```

---

## Formatting — Defer to pattern-docx

Before generating any code:
```
Read: /mnt/skills/user/pattern-docx/SKILL.md
```

**DDR-specific formatting notes:**
- Cover block: Normal paragraphs with run-level formatting (see cover block spec above)
- H1 sections: numbered, page break before each (except first)
- H2 subsections: used within Sections 6 and 7 for the lettered subsections
- Risk table: pattern-docx table style — header row 0F4761, alternating rows
- Body text: all claims labeled [F]/[E]/[H] inline — do not strip labels in final doc
- Header: "[Company Name] — Investment Committee Memorandum" (left) + "CONFIDENTIAL" (right)
- Footer: "[Company Name] IC Memo" (left) + "Page X of Y" (right)

---

## Quality Gates

The memo is ready for IC only when all items below pass.

**Analytical integrity**
- [ ] Investment-evaluation-framework.md loaded and all six gates addressed
- [ ] Every thesis pillar has a complete inductive chain — no skipped links
- [ ] Every quantitative claim is labeled F / E / H with source for all [F] claims
- [ ] Management track record states specific outcomes, not titles
- [ ] Financial projections pass base rate check against sector benchmarks
- [ ] Downside case modeled — IRR stated at base−50% revenue, no margin expansion, −2 turn exit

**Document structure**
- [ ] All ten sections present in correct order
- [ ] Executive summary is self-contained — passes cold read test
- [ ] Risk table has ≥5 risks, at least one scoring ≥15
- [ ] All risks scoring ≥9 have mitigants with adequacy assessments
- [ ] Section 10 has all four mandatory elements (recommendation, walk-away, assumption, open items)

**Iteration loop**
- [ ] Pass 1 complete — all writing-style flags hardened, Group E draft artifacts cleared
- [ ] Pass 2 complete — all claim-scrutinizer flags addressed
- [ ] Pass 3 complete — all red-team KILL and WOUND ratings addressed
- [ ] Pass 4 complete — pre-mortem failure modes incorporated into Section 9 risks;
      open items updated in Section 10 if new gaps surfaced; NTB mapping applied if
      NTB registry exists
- [ ] Pass 5 complete — doc-quality-checker returns zero CRITICAL issues (including
      no draft artifact language: version labels, changelog subtitles, addition prefixes,
      FM codes)

---

## References

```
Read: /mnt/skills/user/mckinsey-consultant/references/investment-evaluation-framework.md
Read: /mnt/skills/user/ntb-diligence/SKILL.md                    (optional upstream)
Read: /mnt/skills/user/competitive-moat-assessment/SKILL.md
Read: /mnt/skills/user/executive-summary-writer/SKILL.md
Read: /mnt/skills/user/writing-style/SKILL.md
Read: /mnt/skills/user/claim-scrutinizer/SKILL.md
Read: /mnt/skills/user/red-team/SKILL.md
Read: /mnt/skills/user/red-team/references/red-team-investment-attacks.md
Read: /mnt/skills/user/pre-mortem/SKILL.md
Read: /mnt/skills/user/pattern-docx/SKILL.md
Read: /mnt/skills/user/doc-quality-checker/SKILL.md
```

**Domain templates (auto-load on matching trigger):**
```
/mnt/skills/user/ic-memo/references/domain-templates/sea-ltd-sea-brazil.md
```
