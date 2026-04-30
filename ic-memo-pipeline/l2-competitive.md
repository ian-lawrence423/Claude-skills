# Phase 2 — L2 Competitive Landscape Agent (IC Memo Mode)

Load immediately:
- `{SKILLS_PATH}/market-research/SKILL.md` → Level 2 section + Competitor Profile Anatomy
- `{SKILLS_PATH}/market-research/references/analytical-prompts.md` → Competitive Landscape section
- `{DOMAIN_TEMPLATE_PATH}` if provided and not `none`

## Your Inputs
Read before starting:
- `{WORK_DIR}/intake.md`
- `{WORK_DIR}/research/l4-market.md`
- `{WORK_DIR}/research/l3-customer.md`

## Your Job

Execute Level 2 competitive research in IC memo mode. Output feeds Section 5
(competitive position) and is the primary input to the moat-assessment agent.

**If a domain template was loaded:** Use template's vendor universe, moat scorecard,
and pricing data as the starting competitive map. Web search for material changes
(funding, acquisitions, product launches, leadership changes) since template date.

---

### Competitor identification

- Direct competitors: top 3–5, ranked by estimated market share / revenue / customer count
- Indirect competitors: companies solving the same problem differently, or adjacent
  players with plausible entry paths
- Competitive intensity: apply Porter's rivalry assessment — number of players, market
  growth rate, switching costs, differentiation, exit barriers

---

### Competitor profiles

For every named direct competitor, complete all six elements from the Competitor Profile
Anatomy in market-research SKILL.md. A profile missing any element is incomplete.

**Element 1 — Core product + GTM:** what they sell and how they acquire customers.
State the primary sales motion (direct / channel / PLG / enterprise).

**Element 2 — Customer base:** segments served + scale (ARR / revenue / customer count
if public). If not available, state that explicitly — do not estimate without basis.

**Element 3 — Sustainable advantage:** one of: network effect / switching cost /
scale economies / proprietary IP / brand. Name the specific mechanism, not the
category. "Strong product" fails.

**Element 4 — Key weakness:** the most exploitable structural gap. Specific and
observable — not a category. Check: geographic limits, product gaps, customer
segment gaps, technical debt, pricing vulnerabilities, channel conflicts.

**Element 5 — Strategic trajectory:** where they appear to be moving. Required signals:
at least two of — last 3 product announcements, acquisitions/partnerships, job posting
patterns, public executive statements, analyst day materials.

**Element 6 — Competitive verdict:** what this competitor's position means for the
subject company's investment thesis. This is the only interpretive element.

---

### Porter's Five Forces — mandatory

Run a full Porter's Five Forces analysis. Rate each force 1–10 (10 = maximum threat
to incumbent profitability). This is not optional — every competitive analysis requires it.

| Force | Rating (1–10) | Specific evidence | Structural implication |
|-------|--------------|-------------------|----------------------|
| Supplier power | /10 | | |
| Buyer power | /10 | | |
| Competitive rivalry | /10 | | |
| Threat of substitution | /10 | | |
| Threat of new entry | /10 | | |

**For each force:** name specific companies, cite specific data points, state the
mechanism. Generic statements fail ("rivalry is high because there are many players" →
name the players, estimate their relative positions, explain what drives rivalry here).

**Overall attractiveness verdict:**
- Weighted score: [average or qualitative]
- Is this an attractive market to be in as an incumbent? As a new entrant?
- The single force most likely to change over the next 3–5 years and in which direction

---

### Positioning map

Two axes that reveal the market's most meaningful structural trade-off. Do NOT use
generic axes (price vs. quality). Find the axes specific to this market's actual dynamics.

Examples of specific axes:
- "Breadth of integration × deployment speed"
- "Enterprise depth × SMB accessibility"
- "Data network size × workflow automation depth"

State why each axis was chosen — what trade-off does it expose?

Position each competitor on the map in text form. Identify white space and state
why it hasn't been filled (capability gap / willingness gap / market timing).

---

### Market share

| Player | Share estimate | Source | Confidence |
|--------|---------------|--------|-----------|

If market share is unavailable: DATA GAP.

---

**Source standard:**
- Public filings (10-K, S-1, earnings transcripts), analyst reports, company websites
- Job postings as capability signals (Tier 3 — context only, never primary evidence)
- Apply inline citation format: `[Source, Year] [H/M/L]`

Flag data gaps immediately:
```
DATA GAP: [Claim] — [reason]
Warrants: [specific action] before treating as confirmed.
```

---

## Required Output — write to `{WORK_DIR}/research/l2-competitive.md`

```markdown
# L2 — Competitive Landscape
## [COMPANY] — IC Memo Mode

## Competitor universe
**Direct:** [list]
**Indirect / adjacent:** [list]
**Competitive intensity:** [Porter's rivalry assessment — 1 sentence]

## Competitor profiles

### [Competitor 1 Name]
**Element 1 — Core product + GTM:** [what they sell, sales motion]
**Element 2 — Customer base:** [segments, scale — ARR/revenue if public]
**Element 3 — Sustainable advantage:** [mechanism named, not category]
**Element 4 — Key weakness:** [specific, observable]
**Element 5 — Strategic trajectory:** [direction + 2 signals]
**Element 6 — Competitive verdict:** [implication for investment thesis]

[Repeat for each competitor]

## Porter's Five Forces

| Force | Rating | Evidence | Implication |
|-------|--------|----------|-------------|
| Supplier power | /10 | [specific] | [structural implication] |
| Buyer power | /10 | [specific] | |
| Competitive rivalry | /10 | [specific] | |
| Threat of substitution | /10 | [specific] | |
| Threat of new entry | /10 | [specific] | |

**Overall attractiveness:** [verdict]
**Force most likely to shift:** [which force, which direction, why]

## Positioning map
**Axis 1:** [what it measures + why chosen]
**Axis 2:** [what it measures + why chosen]
[Text-form positioning of each competitor]
**White space:** [description + why unfilled]

## Market share
| Player | Share | Source | Confidence |
|--------|-------|--------|-----------|

## DATA GAPS
[List any flagged gaps]
```

Append all sources to: `{WORK_DIR}/source-bibliography.md`
Append all DATA GAP flags to: `{WORK_DIR}/data-gaps.md`
