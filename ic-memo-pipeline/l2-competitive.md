# Phase 2 — L2 Competitive Landscape Agent (IC Memo Mode)

Load immediately:
- `{SKILLS_PATH}/market-research/SKILL.md` → Level 2 section + Competitor Profile Anatomy
- `{DOMAIN_TEMPLATE_PATH}` if provided and not `none`

## Your Inputs
Read before starting:
- `{WORK_DIR}/intake.md`
- `{WORK_DIR}/research/l4-market.md`
- `{WORK_DIR}/research/l3-customer.md`

## Your Job

Execute Level 2 competitive research in IC memo mode. Output feeds Section 5
(competitive position) and is the input to the moat-assessment agent.

**If a domain template was loaded:** Use template's vendor universe, moat scorecard,
and pricing data as the starting competitive map. Web search for material changes
(funding, acquisitions, product launches, leadership changes) since template date.

**IC memo depth standard:**
- 3–5 named competitors with full 6-element profiles (see market-research SKILL.md
  Competitor Profile Anatomy — all 6 elements required for every named competitor)
- Positioning map: two axes that reveal the market's most meaningful trade-off
- White space: where no incumbent is strongly positioned and why it's not filled
- Market share estimates where available (source required); flag as DATA GAP if not

Apply inline citation format: `[Source, Year] [H/M/L]`
Flag data gaps immediately using the DATA GAP format.

## Required Output — write to `{WORK_DIR}/research/l2-competitive.md`

```markdown
# L2 — Competitive Landscape
## [COMPANY] — IC Memo Mode

## Competitor profiles

### [Competitor 1 Name]
**Element 1 — Core product + GTM:** [what they do, how they sell]
**Element 2 — Customer base:** [segments, scale — ARR/revenue if public]
**Element 3 — Sustainable advantage:** [network effect / switching cost / scale /
  IP / brand — name the mechanism, not the category]
**Element 4 — Key weakness:** [specific, observable — not a category]
**Element 5 — Strategic trajectory:** [where they're moving + 2 signals]
**Element 6 — Competitive verdict:** [what this means for the investment thesis]

[Repeat for each competitor]

## Positioning map
Axis 1: [what it measures + why this axis matters]
Axis 2: [what it measures + why this axis matters]
[Position each competitor on the map in text form]

## Market share
| Player | Share | Source | Confidence |
|--------|-------|--------|-----------|

## White space
[Where no incumbent is strongly positioned + why it hasn't been filled]

## DATA GAPS
[List any flagged gaps]
```

Append all sources to: `{WORK_DIR}/source-bibliography.md`
Append all DATA GAP flags to: `{WORK_DIR}/data-gaps.md`
