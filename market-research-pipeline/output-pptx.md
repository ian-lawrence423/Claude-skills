# Output — PPTX Agent

Load immediately:
- `{SKILLS_PATH}/pattern-investment-pptx/SKILL.md`

## Your Inputs

Read:
- All draft files in `{WORK_DIR}/draft/`
- `{WORK_DIR}/themes.md`
- `{WORK_DIR}/open-issues.md`
- `{WORK_DIR}/source-bibliography.md`
- `{WORK_DIR}/comprehensive-market-pack-plan.md` if present

## Slide Structure

1. Cover
2. Executive Summary
3. Context and Scope
4. Market Sizing
5. Customer Segmentation and Buying Behavior
6. Competitive Landscape
7. Pricing Models and Unit Economics
8. Technology Trends and Disruption Vectors
9. Regulatory Environment and External Risk
10. Competitive Moat Analysis
11. Strategic Implications and Key Takeaways
12. Comprehensive market-pack modules marked `Yes`, if any were produced and not
    already covered by the base sections
13. Appendix: sources, methodology, and open items

## Output Rules

- Every slide title must be an insight statement.
- Every chart or table must identify source, period, and scope.
- Use evidence tags for uncertain or hypothesis-driven claims.
- Do not use unsupported superlatives or promotional language.
- Keep recommendations specific to the evaluated company, market, asset, operator,
  or investor. Do not default to Pattern unless Pattern is explicitly the subject.
- If open issues are material, surface them before the appendix.

Write final deck to `{WORK_DIR}/final-output.pptx`.

