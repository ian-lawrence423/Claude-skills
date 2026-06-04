---
name: ntb-diligence
description: |
  Standalone Need-to-Believe (NTB) diligence skill. Produces a comprehensive NTB registry,
  a prioritised diligence plan keyed to each gap, and adversarial stress tests of every NTB
  assumption. Use this skill
  whenever Ian asks to "run NTB diligence", "run NTB analysis", "build the NTB registry",
  "what do I need to believe about [company]", "stress test the thesis", "map out the NTBs",
  "work out the need-to-believes", "figure out the diligence plan for [deal]", "surface the
  assumptions", "what's the NTB on this", "map the base case assumptions", or "early-stage
  diligence triage". Runs standalone for early-stage diligence when no IC memo exists yet;
  its output plugs directly into ic-memo when the full memo is later produced. Structured
  workflow with intake protocol and four sequential phases — not a one-pass tool. Default
  output is evidence-tagged markdown; .docx output on explicit request via pattern-docx.
  Complementary to ic-memo (runs before it), claim-scrutinizer (tests a completed thesis
  whereas this skill builds the scaffolding), pre-mortem (enumerates failure modes against
  this skill's NTBs), and boundability (converts this skill's gaps into underwriting action).
---

# NTB Diligence — Standalone Skill

You are producing a comprehensive NTB diligence package. This skill owns the Need-to-Believe
registry as a deliverable in its own right — upstream of any IC memo. The output is directly
reusable: it plugs into `ic-memo` at drafting time, or serves as a standalone diligence
deliverable for a deal team.

Read this entire file before beginning.

---

## Skill Architecture — Where This Fits

```
ntb-diligence        ← YOU ARE HERE — NTB registry, diligence plan, stress test
      │
      ├── mckinsey-consultant          ← analytical OS; loaded for thesis structuring
      ├── investment-evaluation        ← NTB format spec (claim-scrutinizer/references/)
      ├── market-research              ← invoked if evidence gathering is required
      ├── claim-scrutinizer            ← runs on the stress-test output
      ├── writing-style                ← runs on all prose before delivery
      └── pattern-docx                 ← optional .docx output on explicit request
```

**Relationship to `ic-memo`:**
`ic-memo` previously produced the NTB registry inline during drafting. When `ntb-diligence`
has run, `ic-memo` consumes that output instead of re-deriving it. The transfer mapping is:

- NTB registry → Section 4 (Investment Thesis) — each NTB becomes a thesis pillar; the
  Section 2 executive summary cites the registry verbatim
- Diligence plan → Section 10 (IC Recommendation) open items block
- Stress tests (leading indicators, kill triggers, cascade effects) → Section 9 (Risks
  & Mitigants) risk register
- Cross-NTB correlation matrix → Section 9 as a compound-risk annotation

**Relationship to `pre-mortem`:**
`pre-mortem` enumerates failure modes and maps them to NTBs. `ntb-diligence` produces the
NTBs themselves and stress-tests each one. Run `ntb-diligence` first if no NTB registry
exists yet; run `pre-mortem` after to extend coverage.

**When this skill is sufficient:**
- Early-stage diligence where full IC memo is premature
- Standalone "what do I need to believe" question for a deal screen
- Refreshing an existing NTB registry with new evidence or new NTBs

**When to escalate to `ic-memo`:**
- Full 10-section memo required
- Gate 1/2/3 scoring tables needed
- Returns disaggregation table, metric bridge, valuation triangulation needed

---

## Trigger Phrases

Any of these phrases should load this skill:

- "Run NTB diligence on [company]"
- "Build the NTB registry for [company]"
- "What do I need to believe about [company]?"
- "Work out the need-to-believes"
- "Map out the NTBs for [company]"
- "Stress test the thesis on [company]"
- "What's the diligence plan for [deal]?"
- "Figure out what has to be true for [company] to work"
- "Run standalone NTB analysis on [company]" (with "standalone" qualifier)

**Do NOT load this skill for:**
- General references to NTBs inside an in-flight IC memo workflow — mckinsey-consultant
  and ic-memo derive the NTB registry inline via investment-evaluation-framework.md
  Section 3.2 without requiring this skill's four-phase workflow
- Short discussion of "what are the NTBs" where the user wants a quick list, not a
  diligence package with checkpoints and stress tests
- When the user has already completed an NTB registry and wants to extend it with new
  failure modes — that is `pre-mortem`'s job, not a re-run of this skill

---

## Execution Flow — Four Phases

```
Phase 1 │ INTAKE
        │ Six-question intake protocol fired in one message.
        │ Do not proceed until all six answered.
        │
Phase 2 │ NTB DERIVATION            ← checkpoint 1
        │ Derive candidate NTBs from the thesis.
        │ Confirm count and coverage with the user before proceeding.
        │
Phase 3 │ EVIDENCE & DILIGENCE      ← checkpoint 2
        │ Populate evidence for each NTB, flag gaps, build diligence plan.
        │ Deliver interim output for user review before stress test.
        │
Phase 4 │ STRESS TEST & DELIVERY
        │ Adversarial pass on each NTB assumption.
        │ Final output: markdown by default, .docx on request.
```

Sequencing is mandatory. The checkpoints exist because an NTB derived from an unconfirmed
thesis is worse than no NTB — the rest of the work builds on top of it.

---

## Phase 1: Intake Protocol

Fire all six questions in one message. Do not begin derivation until every question is
answered — an NTB derived without these inputs will be generic and fail the quality gate.

```
NTB DILIGENCE INTAKE — please answer all six questions in one reply

1. COMPANY + ONE-LINE DESCRIPTION
   What company, and one sentence on what it does. If ticker/private, state both.

2. WORKING INVESTMENT THESIS
   One to three sentences. What is the bull case? NTBs are derived from this — a vague
   thesis produces vague NTBs.

3. DEAL CONTEXT
   Public equity long / PE buyout / M&A sell-side / M&A buy-side / venture.
   Entry valuation or implied entry multiple if known.
   Hold period (3-year, 5-year, open-ended).

4. INFORMATION STATE
   CIM only / management calls / QoE / sell-side coverage only / prior Pattern research /
   full primary research. Determines the expected Boundable/Partially Boundable/Unboundable distribution.

5. KNOWN DATA + SOURCE MATERIAL
   Attach: CIM, management deck, prior research, filings, expert transcripts, prior IC
   memo if one exists. Name specific data points already in hand.

6. DECISION CONTEXT + TIMELINE
   Early screen / pre-LOI / final IC / post-close monitoring.
   Target delivery date. Determines depth and whether primary research is scoped in.
```

**Before proceeding, scan for a domain template match:**

Check `/mnt/skills/user/ic-memo/references/domain-templates/` for any file whose trigger
list matches the company or topic. If a match is found, load it immediately — it pre-loads
confirmed data, known gaps, and prior NTB work that would otherwise be re-derived. State in
Phase 2 output: "Domain template loaded: [filename]. [N] confirmed data points pre-loaded.
[N] open questions carried forward from prior analysis."

---

## Phase 2: NTB Derivation (Checkpoint 1)

Derive candidate NTBs from the thesis. An NTB is a declarative base-case assumption that
must be true for the investment to work — not a risk, not a question, not a KPI.

### Derivation Rules

**Every NTB must be:**
- **Falsifiable** — a specific observable would prove it wrong
- **Base-case framed** — states what must be true, not what might go wrong
- **Quantitatively linked** — connects to a material return driver
- **Company-specific** — not a generic sector claim any company could make

**Format for each NTB:**

> NTB [#]: [One declarative sentence. Specific numbers where possible. Mechanism stated.]

Examples of good NTBs (from Sea Ltd template):
✅ *"Indonesia GMV — 37% of SEA platform GMV — reaccelerates to 15–20% YoY in 2026 after 2025 structural noise, sustaining the base case volume assumption."*
✅ *"Monee seasoned-cohort NPL holds below 1.5% through FY2027, with no Silent Credit Cliff from the 6–9 month aggregate NPL lag at 80%+ loan book growth."*

Examples of bad NTBs:
❌ Too generic: *"The market will grow."*
❌ Risk framing: *"TikTok competition does not escalate."*
❌ KPI, not assumption: *"Revenue grows 20% YoY."* (no mechanism, not connected to thesis)

### What makes a good NTB statement

An NTB is a single declarative sentence stating what must be true for the base case
to hold. Test each NTB statement against these examples before finalising:

❌ Too generic: *"The market will grow."*
❌ Risk framing (inverted): *"Competition does not escalate."*
❌ Not quantified: *"Customer retention holds."*
❌ Not specific: *"The company executes well."*

✅ Correct: *"Net revenue retention sustains above 115% through FY2028 on the enterprise
  cohort, which drives 60% of base case revenue growth."*
✅ Correct: *"EBITDA margin expands from 12% to 18% by FY2028 via 400bps of gross margin
  improvement (product mix shift) and 200bps of G&A leverage."*
✅ Correct: *"Shopee ad take-rate expands from ~2% of GMV toward 3%+ by CY2029, with a
  structural ceiling above 2.5%, validating the primary EBITDA compounding mechanism."*

The common failure mode is under-specificity. An NTB is useful for diligence prioritisation
only if the specific claim inside it can be falsified. "The market grows" cannot be
falsified without a quantified threshold.

### NTB Count and Coverage

**NTB count calibration:**
- **4 NTBs minimum** — below this, the thesis is under-decomposed and the stress
  test will be shallow
- **5–7 NTBs typical** — most deals resolve cleanly in this range
- **8+ NTBs** — consolidate sub-drivers under parent assumptions before finalising;
  10+ signals the thesis is being described rather than structured

### Coverage Rules

- **Minimum 4, maximum 7.** Fewer than 4 means the thesis decomposition is incomplete;
  more than 7 means NTBs are being split into sub-assumptions that should be consolidated.
- **Each NTB must govern >5% of total MOIC impact.** NTBs with trivial return stakes are
  removed or rolled into a larger NTB.
- **Coverage test:** If every NTB were confirmed, would the thesis hold? If any NTB could
  fail without affecting the thesis, it's not a real NTB — remove it.
- **Independence test:** Two NTBs should not both fail together for the same reason. If
  they would, they are the same NTB framed differently — consolidate.

### CHECKPOINT 1 — Output and User Confirmation

Before proceeding to Phase 3, produce the candidate NTB list with this format:

```
NTB DILIGENCE — CHECKPOINT 1: Candidate NTBs

Thesis (restated): [the working thesis from intake]

Candidate NTBs:
  NTB 1: [statement]
  NTB 2: [statement]
  NTB 3: [statement]
  NTB 4: [statement]
  [...]

Coverage rationale: [one paragraph — why these [N] NTBs collectively cover the thesis]

Memo author MOIC weight estimate: [rough weighting per NTB from first-pass intuition — formally derived in Phase 3 Section 3.3 once returns model inputs are explicit. Label as [H, memo author inference] unless backed by an underlying Pattern model artifact.]

REVIEW REQUIRED: Please confirm the NTB list or request revisions before I proceed to
evidence gathering and diligence planning. Revisions typical at this stage: adding an
NTB you think is missing, removing one that doesn't belong, or resharpening a statement
so it's specifically falsifiable.
```

Wait for user confirmation. Do not proceed to Phase 3 on your own judgment — the
checkpoint exists because downstream work compounds errors in the NTB set.

**Handling user rejection at Checkpoint 1:**

If the user rejects the candidate NTB list, determine which type of revision is needed:
- **Add an NTB I missed:** user names a specific assumption the thesis requires that
  isn't in the list. Add it, re-verify the count is still ≤7, re-run the independence
  test against all other NTBs, and re-issue Checkpoint 1.
- **Remove an NTB that doesn't belong:** user identifies an NTB that isn't actually
  required for the thesis to hold. Remove it, re-run the coverage test (if thesis still
  holds with the remaining NTBs, accept removal; if not, ask the user whether the thesis
  itself needs revision). Re-issue Checkpoint 1.
- **Resharpen an NTB statement:** user says an NTB is directionally right but not
  specific or falsifiable enough. Rewrite that NTB using the Derivation Rules above,
  then re-issue just that NTB for approval — no need to re-issue the full list.
- **Reject the thesis decomposition entirely:** user says the NTBs don't add up to the
  thesis. Do not patch at the NTB level — ask the user to restate the thesis more
  specifically, then re-derive NTBs from the revised thesis.

Do NOT proceed to Phase 3 with any NTB the user has flagged. If more than two rounds
of revision occur at Checkpoint 1, pause and ask whether the underlying thesis itself
needs restating — repeated NTB revisions usually signal a thesis problem, not an NTB
problem.

---

## Phase 3: Evidence & Diligence Plan (Checkpoint 2)

For each confirmed NTB, produce: (1) full evidence inventory with [F]/[E]/[H] tags and
sources; (2) explicit gap list in GAP: format; (3) returns impact quantification;
(4) boundability narrative; (5) diligence action mapped to the gap.

### 3.1 — Evidence Inventory Per NTB

For each NTB:
- **Confirmed evidence [F]** — lead with hardest evidence; named sources; include confidence tier (HIGH/MEDIUM/LOW)
- **Conditional evidence [E]** — reasoned estimates with stated assumptions
- **Hypothesis [H]** — directionally plausible but not yet tested
- **Gaps [GAP]** — primary data not yet obtained; state exactly what is missing and reference the diligence plan item number

Minimum 6 evidence bullets per NTB. Fewer means the evidence base is too thin to support
confidence in the NTB; if that's the genuine state, flag it explicitly rather than
padding.

### 3.2 — Evidence State Classification

Per NTB, assign one of:
- **CONFIRMED** — primary data in hand without material remaining gap
- **CONDITIONAL** — directionally supported but ≥1 material gap remains
- **GAP** — primary data required to test the assumption not yet obtained

Classification is not subjective — it follows these rules:
- Any NTB where the key mechanism is [H] = GAP regardless of surrounding evidence
- Any NTB where the evidence relies on a single source with known bias (e.g., sell-side
  with active coverage relationship) = at best CONDITIONAL
- Any NTB where the data for verification is structurally unavailable (Unboundable) = GAP

### 3.3 — Returns Impact Per NTB

State: EBITDA impact (upside/downside in $M at the exit year), MOIC impact delta,
derivation formula used.

Standard formula: MOIC delta = EBITDA variance × exit multiple ÷ entry equity.
State all inputs explicitly — hold period, entry equity, exit multiple, EBITDA base case.

**Reconciliation with Phase 2 rough weights:** Compare each NTB's formally quantified
MOIC impact here against the rough weighting stated at Checkpoint 1. If any NTB diverges
>20%, that divergence is a signal — not noise. A large upward divergence means the NTB
is more load-bearing than first-pass intuition suggested (consider promoting in priority).
A large downward divergence means the NTB may govern less of the return than the thesis
implies (consider whether it should be consolidated or removed). State the divergence
explicitly in the Checkpoint 2 output.

**Coverage check:** The sum of upside MOIC deltas across all NTBs should approximate the
bull-to-base MOIC spread. The sum of downside deltas should approximate the base-to-bear
spread. **Tolerance: within ±15% of the spread.** If the sum lands within tolerance,
note the variance and proceed. If it lands outside tolerance in either direction, either
the NTBs are missing material drivers or the scenario analysis is internally inconsistent
— flag and reconcile before moving on.

Common diagnoses for out-of-tolerance sums:
- Sum <85% of spread: at least one material driver is missing from the NTB set, or a
  driver is under-weighted. Add or re-scope before proceeding.
- Sum >115% of spread: NTBs are overlapping (double-counting the same driver across two
  NTBs) or the scenario table itself is too narrow. Consolidate NTBs or widen scenarios.
- Sum within tolerance but one NTB >50% of total: acceptable but dangerous — the thesis
  is concentrated. Flag as a "load-bearing NTB" requiring extra diligence priority.

### 3.4 — Boundability Narrative

For each NTB, write 3–5 sentences answering:
1. What specific data would sharpen this NTB's assessment?
2. Where is the Boundable/Partially Boundable/Unboundable boundary within this NTB? (Some NTBs have split boundability —
   e.g., Partially Boundable for probability but Unboundable for timing.)
3. For Unboundable components, name precisely what makes them structurally unboundable.

Do not suppress Unboundable items. The entire value of the stress test in Phase 4 depends on Unboundable
assumptions being explicit.

### 3.5 — Diligence Plan

Produce a prioritised diligence action plan keyed to the GAP items in the NTB registry.
The plan is organised by urgency — CRITICAL items block deal advancement; HIGH items
sharpen assessment materially; MEDIUM items refine at the margin.

**Prioritisation Rules:**

**CRITICAL** — GAP items where ALL of:
- The NTB is rated GAP (not CONDITIONAL)
- The MOIC at stake is >0.15x on either upside or downside
- Without this data the position cannot be sized confidently

**HIGH** — GAP items where ANY of:
- NTB is rated GAP with MOIC impact 0.08–0.15x
- NTB is rated CONDITIONAL but has a specific gap with MOIC >0.15x impact
- The data addresses a kill trigger resolution

**MEDIUM** — GAP items where:
- NTB is rated CONDITIONAL with MOIC impact <0.15x
- The gap is bounded in time (will resolve naturally at known earnings or filing date)

**Action Specificity (mandatory):**

"Further diligence" is not an acceptable action. Every diligence item must state:
- **Mechanism** — IR request, AlphaSense/Tegus expert call, primary consumer research,
  3PL industry contact, management meeting, data room request, regulatory filing review
- **Timeline** — expected resolution date or window (e.g., "Q1 2026 earnings — May 2026"
  or "2–3 weeks for Tegus expert network")
- **Cost/effort** — if commissioning primary research, state the expected cost
  ($X–Y thousand) and duration

**Required Format (table):**

| Priority | Data Item | NTB Resolved | Mechanism | Timeline | Cost |
|----------|-----------|--------------|-----------|----------|------|
| CRITICAL | [specific data] | NTB [#] | [mechanism] | [date/window] | [$ or N/A] |
| HIGH | [specific data] | NTB [#] | [mechanism] | [date/window] | [$ or N/A] |
| MEDIUM | [specific data] | NTB [#] | [mechanism] | [date/window] | [$ or N/A] |

Cross-reference from the NTB registry to Info Gap priority numbers only — do not
duplicate the full action description in both tables.

### CHECKPOINT 2 — Interim Output

Deliver the full Phase 3 output in this structure:

```
NTB DILIGENCE — CHECKPOINT 2: Evidence Base + Diligence Plan

For each NTB:
  Statement
  Evidence state: CONFIRMED / CONDITIONAL / GAP
  Confirmed evidence [F] — minimum 3 bullets, named sources
  Conditional evidence [E] — reasoned estimates
  Hypotheses [H] — directional only
  Gaps [GAP] — explicit list; cross-referenced to diligence plan
  Returns impact: EBITDA $X up / $X down; MOIC +Xx / -Xx
  Boundability: [tag] + 3–5 sentence narrative

Returns footnote:
  Hold period, entry equity, exit multiple, MOIC derivation formula.
  MOIC sum check: sum of upside deltas vs. bull-base spread; sum of downside vs. base-bear.

Diligence Plan (prioritised table):
  CRITICAL items first, then HIGH, then MEDIUM. Every GAP maps to a row.

REVIEW REQUIRED: Please review the evidence base and diligence plan. Common revisions
at this stage: flagging a piece of evidence you have but I don't; correcting a source
tier; reprioritising a diligence item; noting a data point is stale. I'll apply revisions
before running the stress test.
```

Wait for user confirmation before proceeding to Phase 4.

**Handling user rejection at Checkpoint 2:**

Phase 3 output is more complex than Phase 2, so rejections typically target specific
elements rather than the whole package. Handle by type:
- **Missing evidence piece:** user flags evidence they have but the Phase 3 inventory
  doesn't reflect. Add it with source and tier; re-check whether it changes the evidence
  state classification (CONFIRMED/CONDITIONAL/GAP). Re-issue the affected NTB.
- **Wrong source tier:** user corrects a HIGH/MEDIUM/LOW rating. Update and reassess
  whether the evidence state classification should change. Re-issue the affected NTB.
- **Diligence plan priority wrong:** user reprioritises a CRITICAL/HIGH/MEDIUM rating.
  Update and reissue the diligence plan table only.
- **Stale data flag:** user notes a data point is outdated. Mark as [E] and add a
  diligence plan row to refresh it. Re-issue the affected NTB's evidence inventory.
- **MOIC sum out of tolerance:** if the coverage check flagged a sum outside the ±15%
  tolerance and the user identifies which driver is missing/overlapping, do NOT proceed
  to Phase 4 — return to Phase 2 to add/consolidate the NTB, then redo Phase 3 for the
  affected NTB(s) and re-issue Checkpoint 2.

If the user rejects the NTB registry fundamentally at this point (e.g., "these NTBs
aren't right after all"), that is a signal Checkpoint 1 was agreed prematurely — back
up to Phase 2, redo the NTB derivation, and re-issue both checkpoints in sequence.

---

## Phase 4: Stress Test & Delivery

### 4.1 — Adversarial Stress Test

For each NTB, produce a stress test that assumes the NTB is wrong and traces the
consequences. This is distinct from the returns impact calculation in Phase 3 — returns
impact quantifies the financial outcome; the stress test examines the mechanism.

**Format per NTB:**

```
STRESS TEST — NTB [#]

Assumption being tested: [restate the NTB]

Failure mode: [the specific way this NTB fails — mechanism, not label]

Leading indicator(s): [what would be observable before the failure fully materialises?
                      If none exists, state that explicitly — this is critical information]

Early exit window: [if detectable, how much advance warning does the monitoring framework
                    provide? Specify the unit that matches the deal type: quarters for
                    public equity, monthly mgmt reports for post-close PE, annual
                    filings + intermediate reports for M&A, or a named other cadence.
                    If no warning is available before failure materialises, state that
                    explicitly — "no leading indicator" is critical information]

Cascade effects: [does this NTB's failure trigger secondary failures? Name the NTBs
                  that would move from CONDITIONAL to FAILED as a result]

MOIC impact if NTB fails: [from Phase 3] — but note if compound-path MOIC is worse
                          than single-driver estimate

Pre-mortem mapping: [On first-pass ntb-diligence runs, mark N/A — pre-mortem runs AFTER
                     this skill. On any subsequent re-run triggered by new evidence or
                     after pre-mortem has completed, cross-reference each stress-test
                     failure mode to the named pre-mortem FM number and any compound
                     path it participates in.]

Kill trigger: [can this NTB's failure be codified as a specific observable threshold
                 that would trigger position exit? If yes, state it. If no, state that
                 no kill trigger can be defined — this itself is important information]
```

### 4.2 — Cross-NTB Correlation Analysis

After stress-testing each NTB individually, produce a correlation matrix:

```
NTB CORRELATION MATRIX

For each pair of NTBs, classify:
- INDEPENDENT: failure of one does not affect the other
- PARTIALLY CORRELATED: shared driver affects joint probability
- STRUCTURALLY LINKED: failure of one directly causes or enables the other
```

This matters because the sum of individual NTB downside MOIC impacts understates the
compound failure scenario. Structurally linked NTB pairs produce worse-than-additive
outcomes that single-driver returns tables do not capture.

### 4.3 — Kill Triggers Summary

From the stress tests, consolidate the kill triggers that emerged:

- Three to five concrete observables that, if confirmed, require thesis reassessment
- Each with a named resolution timeline
- Each linked to the NTB it kills

### 4.4 — Quality Pass (claim-scrutinizer on stress tests)

Before delivery, run `claim-scrutinizer` on the stress test output from Section 4.1. The
stress tests are the most claim-dense part of the deliverable — each stress test asserts
a failure mechanism, a leading indicator, cascade effects, and a kill trigger. Each of
those is a testable claim.

```
Load: /mnt/skills/user/claim-scrutinizer/SKILL.md
```

Run claim-scrutinizer's seven-part test against the full Phase 4 output. Focus areas:
- Failure mode mechanisms pass the logic and evidence tests (not label-framed)
- Leading indicators are genuinely observable, not restatements of the failure itself
- Kill triggers are binary and observable, not risk categories
- Cross-NTB correlation classifications are reasoned, not asserted

Apply all claim-scrutinizer findings before producing the delivery output. If
claim-scrutinizer surfaces a 🔴 CRITICAL issue on any stress test, that stress test
must be rewritten — do not deliver over an unresolved CRITICAL flag.

### 4.5 — Open Questions — Carry Forward

After the stress tests and quality pass, produce the carry-forward Open Questions list.
Source material:
- Any GAP items from Phase 3 that remain unresolved after the diligence plan has been
  executed (or that cannot be resolved before the decision deadline)
- Any Unboundable components flagged in Phase 3 boundability narratives
- Any cascade effects in Phase 4 stress tests that would require monitoring beyond the
  hold period
- Any kill triggers that depend on data not yet in hand

Format as numbered questions (not topic labels). Each question should be specific enough
that a next-cycle researcher can act on it. These questions feed directly into the next
diligence cycle — or into `ic-memo` Section 10 (open items).

### 4.6 — Delivery Format

**Default: markdown**

Deliver the full NTB diligence package as a single markdown document. Sections:

```
NTB DILIGENCE — [COMPANY NAME]

1. Thesis
2. Information State
3. NTB Registry (full, from Phase 3)
4. Returns Impact Summary
5. Diligence Plan (prioritised)
6. Stress Tests (per NTB)
7. NTB Correlation Matrix
8. Kill Triggers
9. Open Questions — Carry Forward

Appendix A: Evidence Sources with Confidence Ratings
Appendix B: Glossary of Evidence Tags and Boundability Classifications
```

**On explicit .docx request:**

If the user asks for a .docx deliverable explicitly (e.g., "output this as a Pattern doc",
"give me the .docx version"), hand off to `pattern-docx` with the markdown as input.
Do not default to .docx — the skill is designed for evidence-tagged markdown as the
primary handoff format because it plugs cleanly into `ic-memo` without reformatting.

---

## Dependencies

**Hard dependencies:**
- `mckinsey-consultant` — thesis structuring and MECE discipline
- `investment-evaluation-framework.md` (at `claim-scrutinizer/references/`) — NTB format spec

**Conditional dependencies:**
- `market-research` — invoked only if evidence gathering requires primary research
- `claim-scrutinizer` — should run on the final stress test output before delivery
- `writing-style` — runs on all prose before final handoff
- `pattern-docx` — only when .docx output is explicitly requested

**Relationship to `ic-memo`:**
`ic-memo` now consumes `ntb-diligence` output rather than producing the NTB registry from
scratch. When both skills are in the workflow, run `ntb-diligence` first; `ic-memo` then
transfers its output per this mapping:
- NTB registry → Section 4 (Investment Thesis) as thesis pillars; Section 2 (Executive
  Summary) cites the registry
- Diligence plan → Section 10 (IC Recommendation) open items
- Stress tests → Section 9 (Risks & Mitigants) risk register
- Cross-NTB correlation matrix → Section 9 compound-risk annotation

Beat 2 of the IC memo sequential prompts (Research & Evidence Gathering) is largely
satisfied by `ntb-diligence` Phase 3 output. Beat 4 (Claim Scrutinizer Pass) still
runs on the full IC memo draft to verify the NTB-to-returns linkage.

---

## Quality Standards

Every `ntb-diligence` output must pass all of the following before delivery:

**Scope**
- [ ] Single-asset analysis only — no portfolio construction, position sizing, or
  cross-position aggregation. Those are downstream decisions taking this skill's
  output as input.

**Structural integrity**
- [ ] 4–7 NTBs; each governs >5% of MOIC; independence test passed
- [ ] Each NTB is falsifiable, base-case framed, company-specific
- [ ] Coverage test: if all NTBs are true, the thesis holds
- [ ] Every GAP item appears in the diligence plan with a specific action
- [ ] MOIC sum check: upside deltas approximate bull-base spread

**Evidence discipline**
- [ ] Every claim carries [F]/[E]/[H] tag with named source for [F]
- [ ] GAP items prefixed "GAP:" and cross-referenced to diligence plan row
- [ ] Source confidence tier stated (HIGH/MEDIUM/LOW) for every [F] bullet
- [ ] No paraphrased source labels — use named sources or "per [specific source]"

**Stress test discipline**
- [ ] Each NTB tested individually with mechanism, not label
- [ ] Leading indicator stated or explicitly flagged as absent
- [ ] Correlation matrix completed — no "independent" default without analysis
- [ ] Kill triggers derived from stress tests, not asserted

**Executive readiness**
- [ ] Markdown structure matches the Section 4.6 format exactly
- [ ] Open questions carry forward — state what the next diligence cycle should address
- [ ] No draft artifact language: no "v[N]" labels, no "NEW", no "addition:" prefixes

---

## Integration with Other Skills

**Before `ntb-diligence` runs:**
- If a domain template exists at `ic-memo/references/domain-templates/` matching the
  company, load it first. It may already contain an NTB registry that becomes the
  starting point for refinement rather than derivation from scratch.

**After `ntb-diligence` runs:**
- `pre-mortem`: reads the NTB registry and extends failure mode coverage. Every pre-mortem
  failure mode should map to the NTB it threatens.
- `claim-scrutinizer`: stress tests can be redlined for logic gaps before final delivery.
- `ic-memo`: consumes the full package when the IC memo is built. Skip ic-memo's internal
  NTB derivation step — it's already done.
- `kpi-tree-builder` (post-close): the GAP items from Phase 3 map to specific atomic nodes
  in the KPI tree — the measurable inputs that confirm or refute each NTB post-close. Run
  kpi-tree-builder after close to convert the NTB registry into a management tracking system.

**Skill precedence when both are active:**
- `ntb-diligence` owns the NTB registry as a deliverable
- `ic-memo` owns the full 10-section memo structure
- `mckinsey-consultant` owns the NTB format spec and the Six Screening Questions context
- If there's ambiguity about whose output is canonical, `ntb-diligence`'s registry is the
  source of truth for the NTB portion; `ic-memo` references it rather than redefining it.

---

## References

```
NTB format spec (mandatory load in Phase 3):
  /mnt/skills/user/claim-scrutinizer/references/investment-evaluation-framework.md
  → Section 3.2: Need-to-Believe Registry — Required Format

Domain templates (auto-load if company matches):
  /mnt/skills/user/ic-memo/references/domain-templates/

Pre-mortem coordination:
  /mnt/skills/user/pre-mortem/SKILL.md

IC memo integration:
  /mnt/skills/user/ic-memo/SKILL.md
```
