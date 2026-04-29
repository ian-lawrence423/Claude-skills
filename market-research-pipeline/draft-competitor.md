# Draft — Competitor Profile Agent

Load: `{SKILLS_PATH}/market-research/SKILL.md` → Section: Competitor Profile Anatomy

## Your Inputs
```
COMPETITOR:  [company name]
L2_OUTPUT:   {WORK_DIR}/research/l2-competitive.md
L3_OUTPUT:   {WORK_DIR}/research/l3-customer.md
```

Read the competitor's raw research from l2-competitive.md and expand into a
full prose profile. All six elements are required. 300–500 words total.

## Output — write to `{WORK_DIR}/draft/competitor-[name].md`

Six elements in order:
1. Core product and GTM
2. Customer base
3. Sustainable advantage (named mechanism only)
4. Key weakness (specific observable limitation)
5. Strategic trajectory (named signals only — no speculation)
6. Competitive verdict (one interpretive sentence)

All claims retain inline citations from L2 research.
