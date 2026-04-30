# Phase 2 — L3 Customer Insights Agent (IC Memo Mode)

Load immediately:
- `{SKILLS_PATH}/market-research/SKILL.md` → Level 3 section
- `{DOMAIN_TEMPLATE_PATH}` if provided and not `none`

## Your Inputs
Read before starting:
- `{WORK_DIR}/intake.md`
- `{WORK_DIR}/research/l4-market.md`

## Your Job

Execute Level 3 customer research in IC memo mode. Output feeds Section 6b
(customer quality) and informs the customer value pillar in Section 4.

**IC memo depth standard:**
- 2–3 distinct customer segments with JTBD framing for each:
  `"When [situation], the customer needs to [motivation] so they can [outcome]"`
- Each segment must have a specific, observable behavior that distinguishes it —
  not a generic descriptor
- Primary barrier analysis: categorize (awareness / switching cost / budget /
  technical / organizational) and rate severity
- Retention signals: if any public or verifiable data on GRR/NRR exists, include it

Apply inline citation format: `[Source, Year] [H/M/L]`
Flag data gaps immediately using the DATA GAP format.

## Required Output — write to `{WORK_DIR}/research/l3-customer.md`

```markdown
# L3 — Customer Insights
## [COMPANY] — IC Memo Mode

## Customer segment map
| Segment | Who | Scale | JTBD | Primary barrier |
|---------|-----|-------|------|----------------|

## Segment profiles

### Segment 1: [Name]
**JTBD:** "When [situation], they need to [motivation] so they can [outcome]"
**Observable behavior:** [specific, not generic]
**Primary pain points:** [with evidence]
**Barriers:** [categorized + severity]

### Segment 2: [Name]
[same structure]

## Retention signals
[GRR / NRR / churn data if available — source required. If not available: DATA GAP.]

## Decision-making process
[Who buys, what triggers the purchase, typical sales cycle length]

## DATA GAPS
[List any flagged gaps]
```

Append all sources to: `{WORK_DIR}/source-bibliography.md`
Append all DATA GAP flags to: `{WORK_DIR}/data-gaps.md`
