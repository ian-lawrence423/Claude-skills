# Phase 2 — Moat Assessment Agent

Load immediately:
- `{SKILLS_PATH}/competitive-moat-assessment/SKILL.md`
- `{DOMAIN_TEMPLATE_PATH}` if provided and not `none`

## Your Inputs
Read before starting:
- `{WORK_DIR}/intake.md`
- `{WORK_DIR}/research/l2-competitive.md`

## Your Job

Run competitive-moat-assessment using the L2 competitor profiles as inputs.
Produce a moat verdict per named competitor. The verdict — not the profiles
themselves — is the primary output of the competitive section in the IC memo.

**Do not re-research competitors.** Use the L2 profiles as your evidence base.
If the L2 profile is missing evidence for a specific moat dimension, flag it
as DATA GAP — do not invent evidence.

**Moat classification taxonomy** (from competitive-moat-assessment SKILL.md):
- Network effect: value grows with each additional user/participant
- Switching cost: cost to change supplier (financial + operational + contractual)
- Scale economies: unit cost advantage from volume
- Proprietary IP: patents, trade secrets, data assets, algorithms
- Brand: willingness to pay premium or trust asymmetry vs. alternatives

**For the subject company specifically:** Produce a moat verdict that directly
answers the investment thesis question — is the moat real, measurable, and durable
over the hold period? This verdict feeds Section 6d (Business Quality / Competitive Moat).

## Required Output — write to `{WORK_DIR}/research/moat-assessment.md`

```markdown
# Competitive Moat Assessment
## [COMPANY]

## Subject company moat verdict
**Moat type:** [network effect / switching cost / scale / IP / brand]
**Evidence:** [specific, observable — not generic claims]
**Durability:** [what would neutralize this moat in 3–5 years?]
**Verdict:** Strong / Moderate / Weak — [one sentence why]

## Competitor moat verdicts
| Competitor | Moat type | Evidence quality | Verdict |
|------------|-----------|-----------------|---------|
| [Name] | [type] | [H/M/L] | [Strong/Moderate/Weak] |

## Relative moat positioning
[Who has the strongest moat in this market and why? One paragraph.]

## Investment implication
[What does the moat analysis mean for the investment thesis? Does the subject
company's moat justify the entry multiple / hold period return assumption?
One paragraph — direct, no hedging.]
```

Append any new DATA GAP flags to: `{WORK_DIR}/data-gaps.md`
