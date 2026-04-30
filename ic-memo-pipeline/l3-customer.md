# Phase 2 — L3 Customer Insights Agent (IC Memo Mode)

Load immediately:
- `{SKILLS_PATH}/market-research/SKILL.md` → Level 3 section
- `{SKILLS_PATH}/market-research/references/analytical-prompts.md` → Customer Insights section
- `{SKILLS_PATH}/market-research/references/analytical-prompts.md` → Financial & Unit Economics section (unit economics questions)
- `{DOMAIN_TEMPLATE_PATH}` if provided and not `none`

## Your Inputs
Read before starting:
- `{WORK_DIR}/intake.md`
- `{WORK_DIR}/research/l4-market.md`

## Your Job

Execute Level 3 customer research in IC memo mode. Output feeds Section 6b
(customer quality) and informs the customer value pillar in Section 4.

---

### Segment identification

Identify 2–3 distinct customer segments. Each segment must have a specific,
observable criterion that distinguishes it — not a generic descriptor.

For each segment, complete the full profile:
```
Segment name:
Observable distinguishing criterion:
Problem acuity (how painful — evidenced, not stated):
JTBD: "When [situation], this customer needs to [motivation] so they can [outcome]"
Primary pain points (specific, observable, evidenced — not category labels):
Workaround currently used + cost of workaround (time / money / risk):
Decision process: who decides, who influences, what triggers active search:
Willingness to pay (stated / inferred from comps / unknown — label which):
Primary barrier (categorize: awareness / switching cost / budget / technical / organizational):
Switching cost (quantify where possible — time, data migration, retraining, contract):
```

The JTBD framing is mandatory: `"When [situation], they need to [motivation] so they can [outcome]"`

---

### Decision journey

Answer all six for each primary segment:
1. What triggers active search for a solution?
2. What information sources do buyers consult during evaluation?
3. What criteria determine the shortlist?
4. What criteria determine the final decision?
5. Who has veto power in the buying process?
6. What causes deals to stall or fail after initial interest?

---

### Pain point depth standard

For each pain point:
- State the functional dimension (what breaks or fails)
- State the emotional/social dimension (how customers feel about having this problem)
- State what evidence establishes it as real vs. assumed

Generic pain points fail: "buyers want faster processing" is a category.
"Enterprise buyers face 48–72 hour SLA exposure when [specific workflow] fails because
[specific mechanism] — evidenced by [source]" is a pain point.

---

### Unit economics signals

From analytical-prompts.md (Financial & Unit Economics → Unit Economics):
- LTV:CAC ratio if any public comparables exist — state source and derivation method
- Gross margin per customer/unit vs. sector benchmark
- CAC payback period if estimable
- Label all estimates [E] with methodology stated

If none of this is publicly available: flag as DATA GAP, state what would be needed.

---

### Retention signals

If any public or verifiable GRR/NRR/churn data exists, include with source.
If not available: DATA GAP — state the most likely source (earnings call, S-1, industry survey).

---

**Source standard:**
- Consumer surveys (Pew, Nielsen), industry associations, academic behavioral studies
- Trade press with named methodology
- Apply inline citation format: `[Source, Year] [H/M/L]`

Flag data gaps immediately:
```
DATA GAP: [Claim] — [reason]
Warrants: [specific action] before treating as confirmed.
```

---

## Required Output — write to `{WORK_DIR}/research/l3-customer.md`

```markdown
# L3 — Customer Insights
## [COMPANY] — IC Memo Mode

## Customer segment map
| Segment | Observable criterion | Problem acuity | JTBD (summary) | Primary barrier |
|---------|---------------------|---------------|----------------|----------------|

## Segment profiles

### Segment 1: [Name]
**Observable criterion:** [specific]
**Problem acuity:** [evidenced]
**JTBD:** "When [situation], they need to [motivation] so they can [outcome]"
**Pain points:** [specific + evidenced]
**Workaround + cost:** [current workaround + time/money/risk cost]
**Switching cost:** [quantified where possible]
**Willingness to pay:** [stated/inferred/unknown — label which]

### Segment 2: [Name]
[same structure]

## Decision journey (primary segment)
1. Trigger: [what starts active search]
2. Information sources: [where they look]
3. Shortlist criteria: [what gets a vendor to the shortlist]
4. Final decision criteria: [what closes the deal]
5. Veto: [who can block + on what basis]
6. Stall causes: [why deals die after initial interest]

## Unit economics signals
[LTV:CAC / gross margin / payback — source required; label E if estimated]

## Retention signals
[GRR / NRR / churn data — source required. If not available: DATA GAP.]

## DATA GAPS
[List any flagged gaps]
```

Append all sources to: `{WORK_DIR}/source-bibliography.md`
Append all DATA GAP flags to: `{WORK_DIR}/data-gaps.md`
