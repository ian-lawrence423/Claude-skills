# New Deal Pipeline - Quality Contract

This contract applies to every phase and every output in the new-deal pipeline.
It is mandatory. If a phase cannot satisfy it, the phase must halt or carry a
visible `GAP`; it must not fill the gap with plausible prose.

Thoroughness outranks speed and polish. A complete answer with explicit gaps is
better than a smooth answer that hides missing evidence.

## Non-Negotiable Standard

The output must be:

1. **Thorough** - covers the full decision question, not only the easy evidence.
2. **Fact-oriented** - facts are sourced, estimates show assumptions, hypotheses
   are labeled.
3. **Well-sourced** - source quality, date, methodology, and independence are
   visible.
4. **MECE** - issue trees, market maps, risk lists, and recommendations do not
   overlap and do not omit material branches.
5. **Low-hype** - no unsupported superlatives, promotional adjectives, or generic
   "strategic" claims.
6. **Decision-linked** - every major section states what changes in the decision.
7. **Claim-economical** - every paragraph validates a point, shows the evidence,
   explains the decision implication, or names a gap.

## Evidence Tags

Every material assertion must carry one tag:

| Tag | Meaning | Use standard |
|---|---|---|
| `[F]` | Fact | Directly sourced from a named source with date and scope |
| `[E]` | Estimate | Derived from facts; formula and assumptions shown |
| `[H]` | Hypothesis | Plausible but untested; includes falsification trigger |
| `[VENDOR]` | Vendor claim | From seller/vendor/company marketing; not independent proof |
| `[MGMT]` | Management claim | From management interview, CIM, or forecast; not independent proof |
| `[GAP]` | Missing evidence | Evidence required before the claim can support a decision |

## Source Rules

1. A thesis-critical fact requires a named source, source date, and scope.
2. A thesis-critical estimate requires visible arithmetic and source inputs.
3. A thesis-critical claim should have at least two independent sources. If only
   one exists, label it `SINGLE-SOURCE DEPENDENCY`.
4. Vendor and management claims can orient the analysis but cannot independently
   validate a thesis-critical conclusion.
5. If sources conflict, show the range and explain why.
6. If methodology is undisclosed, downgrade confidence.

## Claim Economy Rule

Every sentence in a final output must do at least one of these jobs:

1. Define scope, boundary, or decision context.
2. State a sourced fact with period and scope.
3. Show an estimate with arithmetic and assumptions.
4. Explain why the evidence changes the decision, risk posture, or valuation.
5. Identify a gap, uncertainty, open question, or kill trigger.

Remove sentences that only add emphasis, generic setup, or promotional tone. If a
claim cannot be validated from available evidence, move it to `open-issues.md`
instead of keeping it in the narrative.

## MECE Gate

Every phase must run this check before advancing:

| Test | Required output |
|---|---|
| Mutually exclusive | No duplicated branches, competitors, risks, or thesis pillars |
| Collectively exhaustive | Material missing branches named as `GAP` if not researched |
| Same level | Items in a list operate at the same abstraction level |
| Decision relevance | Each item can change the recommendation, sizing, priority, or risk posture |

## Anti-Hyperbole Rule

Do not use these terms unless a cited metric or source directly proves the
claim: `leading`, `best-in-class`, `unique`, `unmatched`, `robust`, `massive`,
`world-class`, `dominant`, `transformational`, `sticky`, `mission-critical`,
`category-defining`, `innovative`.

Allowed replacement pattern:

```text
Instead of: "Company has a best-in-class product."
Write: "[F] Company wins 42% of competitive bakeoffs in the provided sales data
for FY2025; this supports a product-conversion advantage but does not prove a
structural moat without churn, switching-cost, or pricing-power evidence."
```

## Required Registers

Every run maintains these files:

| File | Purpose |
|---|---|
| `shared/source-bibliography.md` | Every source with date, tier, methodology, independence, and CRAAP score |
| `shared/evidence-register.md` | Every material claim with tag, confidence, source, and downstream use |
| `shared/belief-register.md` | Load-bearing beliefs, priors, updates, and kill triggers |
| `shared/claim-ledger.md` | Claims reused across deliverables and whether each survived quality passes |
| `shared/open-issues.md` | Gaps and unresolved issues carried visibly into outputs |
| `shared/number-register.md` | Every recurring number, authoritative value, source, and location used |

## Quality Gates

Each gate must return `PASS`, `PASS_WITH_GAPS`, or `HALT`.

| Gate | PASS condition | HALT condition |
|---|---|---|
| Evidence gate | All thesis-critical claims tagged and sourced | Untagged or unsourced thesis-critical claim |
| Source gate | Critical claims triangulated or labeled single-source | Vendor/management claim used as independent proof |
| MECE gate | No overlap or missing material branch | Framework has duplicated or missing material branches |
| Arithmetic gate | Sizing, growth, valuation, and return math shown | Formulaic claim without arithmetic |
| Hype gate | Unsupported superlatives removed | Promotional language remains in final text |
| Claim economy gate | Every paragraph validates evidence, implication, or gap | Narrative padding, generic praise, or unneeded adjectives remain |
| Cross-output gate | Same claim/number means same thing across outputs | Conflicting claims or numbers across deliverables |
