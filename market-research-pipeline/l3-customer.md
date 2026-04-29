# L3 — Customer Insights Agent

Load immediately:
- `{SKILLS_PATH}/market-research/SKILL.md`  → Section: Level 3
- `{SKILLS_PATH}/market-research/references/analytical-prompts.md` → Section: Customer Insights

## Your Inputs
```
BRIEF:     {WORK_DIR}/brief.md
L4_OUTPUT: {WORK_DIR}/research/l4-market.md
```

Read L4 output before beginning. Your segment analysis must be consistent with
the L4 segment map — do not introduce new segment definitions without noting
the discrepancy.

## Depth Requirements

- Each segment profile needs a specific observable behavior that distinguishes it
  from other segments. Generic descriptions fail.
- Barrier analysis must categorize (awareness / switching cost / budget /
  technical / organizational) and rate severity — not just list.
- JTBD framing required for each segment:
  "When [situation], the customer needs to [motivation] so they can [outcome]"

Apply inline citation format and DATA GAP flags throughout.
Append to `{WORK_DIR}/data-gaps.md` and `{WORK_DIR}/source-bibliography.md`.

## Output — write to `{WORK_DIR}/research/l3-customer.md`

```markdown
# L3 — Customer Insights — [COMPANY]

## Customer segments (3–5)
[For each segment:]
### Segment [N]: [name]
- Observable distinguishing behavior: [specific, evidenced]
- JTBD: "When [situation], needs to [motivation] so they can [outcome]"
- Primary pain points: [categorized, rated]
- Barriers: [categorized by type, severity rated]
- Decision process + purchase triggers: [specific]

## Cross-segment patterns
[What do multiple segments share? What creates switching between them?]
```
