# Draft - Gold-Standard Analytical Section Agent

Load: `{SKILLS_PATH}/market-research/SKILL.md` -> Phase 4, Section Anatomy
Load: `market-research/references/gold-standard-report-template.md`

## Your Inputs

```
SECTION_NAME: [Customer Segmentation and Buying Behavior / Competitive Landscape / Pricing Models and Unit Economics / Technology Trends and Disruption Vectors / Regulatory Environment and External Risk / Competitive Moat Analysis / Strategic Implications and Key Takeaways]
SECTION_ARTIFACT: [artifact assigned in artifact-plan.md]
THEMES:       {WORK_DIR}/themes.md
RESEARCH:     all four research files
COMPETITORS:  competitor files when relevant
```

## Section Anatomy

Apply the four-element section anatomy exactly:

1. **Headline** - insight statement, not a label
   - Wrong: "Competitive dynamics"
   - Right: "Platform consolidation is accelerating while workflow substitutes are expanding the real competitor set"

2. **Framing paragraph** - 3-4 sentences using Situation -> Complication -> Resolution
   - Orient the reader
   - Do not dump evidence before stating the point

3. **Decision-grade artifact** - use the assigned artifact from `artifact-plan.md`
   - Examples: buyer archetype table, substitute map, pricing archetype table,
     disruption map, regulatory scope table, moat scorecard, IC underwriting table
   - The artifact must be interpreted in prose; do not leave a naked table

4. **Evidence blocks and synthesis** - 2-4 evidence blocks plus a so-what close
   - Every material claim tagged [F/E/H] + [H/M/L] confidence
   - DATA GAPs acknowledged where they exist
   - Close with the implication for Pattern, an operator, or an investor

## Output - write to `{WORK_DIR}/draft/[section-slug].md`

Target length: 2-4 pages (DOCX) / 2-3 slides (PPTX).
