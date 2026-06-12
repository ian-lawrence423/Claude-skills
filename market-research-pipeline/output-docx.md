# Output — DOCX Agent

Load immediately:
- `{SKILLS_PATH}/pattern-docx/SKILL.md`

## Your Inputs

Read:
- All draft files in `{WORK_DIR}/draft/`
- `{WORK_DIR}/open-issues.md`
- `{WORK_DIR}/source-bibliography.md`
- `{WORK_DIR}/data-gaps.md`

## Document Structure

Build a Pattern-branded Word document in this order:

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
12. Open Items, if any
13. Appendix: sources, methodology, arithmetic checks, and data gaps

## Output Rules

- Preserve source labels and evidence tags.
- Do not convert hypotheses into facts.
- Include market-sizing arithmetic in the body or appendix.
- If `open-issues.md` is non-empty, include a clearly labeled Open Items section
  before the appendix.
- Do not use unsupported promotional language.

Write final document to `{WORK_DIR}/final-output.docx`.

