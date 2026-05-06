---
name: writing-style
description: |
  Governs prose quality, claim standards, and epistemic discipline for all formal outputs
  via an explicit self-review pass after drafting. Auto-runs on every formal output —
  market research reports, IC memos, investment theses, strategy memos, and PPTX narrative
  text — without needing to be explicitly invoked. Always runs alongside mckinsey-consultant,
  market-research, diligence-ddr, pattern-docx, and pattern-investment-pptx. Does NOT run
  on conversational responses or interim analytical work — only on final or near-final
  formal outputs.
---

# Writing Style — Formal Outputs

You produce a draft using the primary skill governing the output type. Then — before
delivering — you run the self-review pass in this file. The review is not optional and
is not abbreviated. Read this entire file before beginning the review.

---

## The Self-Review Pass

The self-review has five sequential steps. Run them in order. Each step produces either
a clean bill or a list of specific edits. Apply all edits before delivering the output.

---

### Step 1: Claim Tagging

Scan every material claim in the draft. A material claim is any assertion that, if wrong,
would weaken the document's governing argument. Tag each one:

| Tag | Definition |
|-----|------------|
| `[F]` | **Fact** — verifiable, sourced, or directly observable |
| `[E]` | **Estimate** — reasoned from available data; assumptions stated |
| `[H]` | **Hypothesis** — directionally plausible; not yet validated |

**Downgrade rules — apply before anything else:**
- Any `[F]` claim without a traceable source or direct observation → downgrade to `[E]`
- Any `[E]` claim resting on an unstated assumption → surface the assumption in the prose
- Any `[H]` claim not signaled as such in the prose → add epistemic language (see Step 3)

The purpose of this step is to make the epistemic status of every claim visible — to you
and to the reader. A document where facts, estimates, and hypotheses are indistinguishable
is not analytically credible.

---

### Step 1B: Source Attribution Integrity

Epistemic tagging (Step 1) tells the reader how confident to be in a claim. Source
attribution tells the reader *who produced* the underlying work. Both must be accurate.
A claim can be correctly tagged `[E]` (reasoned from available data) and still carry
an attribution that overclaims — e.g., citing "Pattern internal model" when no such
model was consulted. This is attribution inflation, and it is as misleading as the
wrong epistemic tag.

**Scan every claim that carries a source tag.** Each source attribution must satisfy:

| Attribution type | What it must mean | What it must not mean |
|------------------|-------------------|----------------------|
| Named external source (JPM, UBS, Sensor Tower, Bloomberg, 10-K, earnings call) | A specific document or dataset from that source was consulted | A general impression of what that source would say |
| "[Firm name] analysis" or "[Firm name] internal model" | A specific artifact (model file, memo, deck, spreadsheet) produced by the firm exists and was consulted | The author's own reasoning in the current drafting session, styled as firm-level work |
| "[Firm name]-side" as executor label | Who will execute the action or carry the exposure (buy-side role) | A source citation — role labels are not attribution |
| "Memo author inference" or "Memo author estimate" | The reasoning was produced by the author of this memo in the current session, cited transparently | — |

**The Attribution Test — apply to every `[F]` or `[E]` tag:**

1. Can you point to the specific artifact that produced this claim? (document, dataset,
   model file, dated conversation)
2. If yes: cite it specifically — name and date of the artifact.
3. If no: the claim is `[H, memo author inference from <named external source>]` — not
   `[E, firm internal model]`.

**Attribution inflation patterns to flag:**

| Pattern | Corrective |
|---------|------------|
| `[E, Pattern analysis]` / `[E, Pattern internal model]` / `[E, Pattern estimate]` without a pointer to an underlying Pattern artifact | Rewrite as `[H, memo author inference from <external source that was consulted>]` |
| "Pattern's assessment is..." in prose, where "Pattern" means the author's in-session reasoning | Rewrite as "Our assessment is..." or "This memo's assessment is..." — do not use the firm name as author |
| "Per our internal model..." when no internal model was consulted | Rewrite as "Our analysis suggests..." or delete the clause if the analysis did not exist |
| Citing "[Firm name]'s view" when the view was synthesized from multiple external sources, not stated by the firm | Rewrite as "A synthesis of [named sources] suggests..." |

**Role labels are distinct from source citations.** "Pattern-side" used to label a
mitigant or diligence action (e.g., "Pattern-side: commission AlphaSense primary
research") is a role label, not a source attribution — keep these as written. The
inflation problem is specifically about source attributions that imply firm-level
analytical artifacts that do not exist.

**The test for readers:** An IC member reading "[E, Pattern internal model MEDIUM]"
infers that a Pattern-firm model exists, is recent, and produces this estimate. If
that is not true, the reader is being misled about how much analytical weight to give
the claim. Every source attribution in the document must pass this reader-expectation
test.

---

### Step 2: Absolute Assertion Test

Scan for every instance of the following. These are not stylistic preferences — they are
enforced. Each instance requires a specific corrective action.

**Group A — Unsupported superlatives and magnitude claims**
These phrases make strong claims that require evidence. If the evidence exists, lead with
it; the assertion follows. If it does not, rewrite.

| Prohibited | Required corrective action |
|------------|---------------------------|
| "the leading," "the dominant," "best-in-class," "market leader" | Name the ranking, source, and date — or reframe as relative: "among the vendors assessed..." |
| "world-class," "best-in-class," "state-of-the-art," "cutting-edge" | Replace with the specific capability or metric that earns the descriptor |
| "significant," "substantial," "massive," "enormous," "impressive" | Replace with the actual figure or a stated range |
| "clearly," "obviously," "undeniably," "unquestionably" | Delete. If the claim needs an adverb to carry it, the evidence is doing insufficient work |
| "strong growth," "rapid expansion," "exceptional performance" | Replace with the growth rate, the period, and the comparison basis |

**Group B — Consulting boilerplate**
These phrases carry no analytical content. Delete and replace with specific substance.

- "robust," "scalable," "leverage" (as a verb), "synergies," "value creation," "unlock value"
- "actionable insights," "strategic imperatives," "key takeaways," "core competencies"
- "move the needle," "low-hanging fruit," "game-changer," "paradigm shift"
- "in today's rapidly evolving landscape," "in an increasingly competitive environment"
- "at the end of the day," "it goes without saying"

**Group C — Circular constructions**
Remove the stated reason and re-read the claim. If the meaning is unchanged, the reasoning
is circular. Common forms:

- "Strong retention because customers stay" → circular; restate the mechanism
- "High margins because the business is efficient" → circular; state what drives efficiency
- "Management is experienced because they have a track record" → circular; name the track record

For every circular construction found: state the mechanism explicitly or remove the claim.

**Group D — Exclusivity and closure terms**
These terms assert that a single mechanism is the exclusive driver, or that a gap closes
under a specific and sufficient condition. They are permitted only when every alternative
mechanism has been explicitly considered and ruled out in the prose.

| Term | Required corrective action |
|------|---------------------------|
| "only," "solely," "exclusively" | State the alternative mechanisms that have been ruled out, or replace with "primarily," "the principal lever," "the dominant constraint" |
| "closes when," "resolved by," "requires" (as a causal gate) | Replace with a condition-based construction: "closes as [X] progresses," "the principal constraint is [X]" — unless the gating relationship is proven |
| "depends entirely on," "is entirely a function of" | Replace with "is primarily driven by" unless exclusive dependence is demonstrated |
| "will," "must," "inevitably" in forward-looking claims | Replace with "is likely to," "the evidence suggests," or reframe as conditional: "if [condition], then [outcome]" |

**Group E — Draft artifact language**

These phrases are internal scaffolding that must never appear in a final IC-distribution
document. They are produced during iteration — by the pre-mortem, red-team, or claim-
scrutinizer passes — and serve as analytical labels during drafting. Before any document
is distributed, every instance must be located and rewritten as substantive prose.

**Version and iteration annotations — delete or rewrite:**

| Prohibited pattern | Required corrective action |
|-------------------|---------------------------|
| `(NEW v[N])`, `(v[N] NEW)`, `v[N] incorporates` | Remove entirely. The finding stands on its own — the version it was added in is not analytically relevant to an IC reader. |
| `FM[N]`, `FM[N], v[N] NEW` | Remove the failure mode code. Name the finding directly: "Silent Credit Cliff" not "FM1". |
| `updated from v[N]`, `Compound Path [N] (updated from v[N])` | Remove the version suffix. The path is described by its mechanism, not its revision history. |
| `INVESTMENT COMMITTEE MEMORANDUM — v[N]` | Strip version suffix for IC distribution: `INVESTMENT COMMITTEE MEMORANDUM` only. |
| Cover subtitle carrying changelog text: `v[N] adds: [list of changes]` | Replace with distribution metadata: `[Month Year] · [Team] · CONFIDENTIAL · For IC Distribution` |
| Document footnote: `v[N] incorporates: [list]` | Replace with source citation string: named data sources, date ranges, and legal disclaimer. |

**Analytical framing artifacts — rewrite as substantive prose:**

| Prohibited pattern | Required corrective action |
|-------------------|---------------------------|
| `Pre-mortem addition:` / `Pre-mortem addition —` | Remove prefix. The finding is substantive — state it directly. Add a label that describes what the finding is: "Capital allocation timing risk:", "Logistics race-to-zero risk:", etc. |
| `Pre-mortem update:` / `Pre-mortem note:` | Remove prefix entirely. Integrate the substance into the analytical paragraph without attribution to the analytical process that produced it. |
| `[analysis pass] adds [N] new findings` | Not appropriate in body text. Document version provenance belongs in an internal changelog, not in prose delivered to an IC. |
| Section headers: `[Topic] — v[N] (N Failure Modes)` | Remove version annotation: `[Topic]` only. The count is visible from the table. |
| `(updated from v[N] analysis)` in section headers | Remove entirely. |

**The test:** Read every paragraph as if you are an IC member seeing this document for
the first time with no prior context. Any phrase that would prompt the question "what is
v4?" or "what pre-mortem?" has failed. Rewrite until the document is self-contained.

---

### Step 3: Epistemic Language Standards

For claims that survived Step 2 but require qualification, use this register. These
constructions are calibrated to MBB senior engagement manager standard — they signal
rigor without undermining conviction.

**For estimates:**
> "We estimate [X] at approximately [figure], based on [methodology or source]."
> "The data suggests [X], though the estimate carries uncertainty around [specific variable]."
> "Available figures point to [X]; the range across sources is [low]–[high]."

**For directional claims with partial evidence:**
> "The evidence is consistent with [X], though a definitive conclusion would require [missing data]."
> "The pattern suggests [X]; the key uncertainty is [Y]."

**For hypotheses:**
> "We believe [X] — this is a working hypothesis and warrants validation through [specific action]."
> "[X] is plausible given [evidence], but has not been tested against [counterevidence]."

**For comparative claims:**
> "Among the [N] vendors assessed, [X] ranks [position] on [specific metric], versus [Y] at [metric]."
> "[X] commands the largest share of the customer segment we examined — [source, date]."

**For causal claims — single-step:**
> "[X] drives [Y] through [mechanism], evidenced by [Z]."
> Not: "[X] drives [Y]." Causation requires a stated mechanism. Absent one, reframe as correlation.

**For causal claims — multi-step (the inductive chain standard):**

Any causal claim involving more than one link must be constructed inductively before it
is written. This is a drafting discipline, not a prose requirement — the chain is built
internally; the output is the earned conclusion.

Build the chain as follows:
1. **Outcome variable** — what is the end state being claimed?
2. **Proximate driver** — what directly moves the outcome variable?
3. **Gating constraint** — what must change for the proximate driver to operate?
4. **Observable condition** — what specific, measurable thing resolves the constraint?

Write only what the chain can prove. Rules:

- If the chain supports a direction but not a specific number or timeline, write a
  condition-based statement, not a time range. "The gap narrows as [gating constraint]
  resolves" is correct. "The gap closes in 3–5 years" is not, unless the chain produces
  that number from a known rate.
- If a link in the chain is an assumption rather than demonstrated evidence, label it
  as such in the prose or downgrade the conclusion to a hypothesis.
- If the chain rules out alternative mechanisms at any link, state that explicitly.
  If it does not, do not use exclusivity terms (see Step 2, Group D).
- A conclusion that skips a link is not a conclusion — it is an assertion. Rewrite or
  remove it.

**Example — incorrect (skips links):**
> "The AOV gap closes when electronics GMV share exceeds 20%."
This states a threshold without proving: (1) why electronics share drives AOV, (2) what
gates electronics share growth, (3) why 20% is the threshold. The chain is absent.

**Example — correct (chain is built, conclusion is earned):**
> "The AOV gap is primarily a category mix problem — MELI's 3.2× AOV premium reflects
> its 62% electronics penetration versus Shopee's near-zero. Electronics adoption on
> Shopee is gated by delivery reliability; reliability at that level requires FBS; FBS
> deployment is constrained by FC density, currently 3 versus MELI's 27. The gap
> narrows at the rate FC buildout enables FBS enrollment."

**For forward-looking claims:**
> "If [condition holds], we would expect [outcome] — consistent with [comparable situation or base rate]."
> "[Analyst / source] projects [X] at [figure] by [year], assuming [key condition]."
> Not: "[X] is poised to [outcome]." Phrasing like "poised to" is projection without basis.

---

### Step 4: Data Quality Flagging

When the underlying research for a claim returned thin, conflicting, or unverifiable data,
flag it explicitly in the output. Do not paper over data gaps with qualified language alone —
the gap itself is material information.

**Flag format — insert inline or in a footnote/callout adjacent to the affected claim:**

> **Data note:** [Specific claim] is based on [source / methodology]. [State the limitation:
> e.g., "Only one primary source was available," "Sources conflict on this figure — range is
> [X]–[Y]," "No third-party validation found."] This warrants [specific follow-on action]
> before treating the figure as confirmed.

**Trigger this flag when:**
- Only a single source was found for a thesis-critical quantitative claim
- Two or more sources conflict on a figure by more than 20%
- The most recent data available is more than 24 months old for a fast-moving market
- The claimed figure comes from the subject company's own materials without independent corroboration
- Web search returned no usable results for a named claim — do not interpolate; flag as unverified

**Do not flag:**
- Widely accepted industry figures with multiple corroborating sources
- Internal estimates that are already labeled `[E]` with stated methodology
- Claims that are structural or definitional rather than empirical

---

### Step 5: Structure and Prose Standards

After claims are resolved, apply these construction standards. These are the final pass
before delivery.

**Paragraph architecture:**
- First sentence states the conclusion. Supporting sentences provide evidence.
  Final sentence states the implication. No exceptions for thesis-critical paragraphs.
- Maximum 5 sentences per body paragraph. If more are needed, split and add a subheader.
- Every section must open with a governing sentence — the section's thesis in one line.
- Every section must close with an implication — what the content means for the argument.
  Sections that only present data without drawing a conclusion are not finished.

**Sentence construction:**
- One idea per sentence. If a sentence requires a semicolon to hold together, split it.
- Active voice over passive. "The company grew revenue 40%" not "Revenue was grown by 40%."
- Numbers beat adjectives. If a number is available, use it. If not, state the basis for
  the qualitative descriptor.

**Transitions:**
- "However," "in contrast," "this suggests," "as a result" — correct; use them.
- "Additionally," "furthermore," "it is worth noting," "notably" — filler; delete or replace
  with a sentence that states the logical relationship explicitly.

**Tables and exhibits:**
- Every table or chart must be preceded or followed by a sentence stating what the data
  shows and why it matters to the argument. Data without an interpretive sentence is not
  an analytical finding.

---

## Integration with Other Skills

This skill runs after the primary drafting skill completes. It does not replace analytical
methodology — it governs how the output of that methodology is written and reviewed.

| Primary skill | Self-review trigger |
|---------------|---------------------|
| `mckinsey-consultant` | Any Step 6 recommendation or final deliverable |
| `market-research` | Final report and any vendor assessment section |
| `diligence-ddr` | Any narrative section; not applied to question lists |
| `pattern-investment-pptx` | All slide body text and callouts; thesis slides in full |
| `pattern-docx` | Any document with a governing thesis or investment recommendation |

When `claim-scrutinizer` is also active (full redline mode), Steps 1–4 of this skill are
superseded by claim-scrutinizer's seven-part test. Step 5 (structure and prose) remains
active regardless.

---

## Pre-Delivery Checklist

Run this before every formal output is delivered. Every item must be checked — not skimmed.

**Claim integrity**
- [ ] Every material claim tagged as fact, estimate, or hypothesis — implicitly or explicitly
- [ ] No `[F]` claim without a traceable source or direct observation
- [ ] Every `[E]` claim signals its basis in the prose
- [ ] Every `[H]` claim uses explicit hypothesis language

**Absolute assertion test**
- [ ] No unsupported superlatives or magnitude claims (Group A)
- [ ] No consulting boilerplate (Group B)
- [ ] No circular constructions (Group C)
- [ ] No exclusivity or closure terms without eliminated alternatives (Group D)

**Epistemic language**
- [ ] Every comparative superiority claim cites a specific benchmark or is reframed
- [ ] Every single-step causal claim states a mechanism
- [ ] Every multi-step causal claim has a complete inductive chain — outcome → proximate
      driver → gating constraint → observable condition — with no skipped links
- [ ] Every gap-closing or timeline claim is condition-based unless a known rate produces
      the number
- [ ] Every projection claim is sourced or labeled as an internal estimate with stated assumptions

**Data quality**
- [ ] Every data gap flagged inline with a data note where required
- [ ] No claim papering over a thin or conflicting data source without disclosure

**Structure and prose**
- [ ] Every section opens with a governing sentence
- [ ] Every section closes with an implication
- [ ] Every table or exhibit has an interpretive sentence
- [ ] No filler transitions remain
- [ ] No paragraph exceeds 5 sentences without a structural reason
