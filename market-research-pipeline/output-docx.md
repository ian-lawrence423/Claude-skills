# Output — DOCX Agent

Load immediately:
- `{SKILLS_PATH}/pattern-docx/SKILL.md`

## Your Inputs

Read:
- All draft files in `{WORK_DIR}/draft/`
- `{WORK_DIR}/open-issues.md`
- `{WORK_DIR}/source-bibliography.md`
- `{WORK_DIR}/data-gaps.md`
- `{WORK_DIR}/comprehensive-market-pack-plan.md` if present
- `{WORK_DIR}/strategic-analysis-plan.md` if present

## Document Structure

Build a professional Word document in this order. Use Pattern-branded formatting
when Pattern formatting is requested by the run; keep the analysis itself objective
and specific to the evaluated company, market, asset, operator, or investor.

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
12. Comprehensive market-pack modules marked `Yes`, in the order listed in
    `comprehensive-market-pack-plan.md`, if any were produced and not already
    covered by the base sections
13. Strategic-analysis modules marked `Yes`, in the order listed in
    `strategic-analysis-plan.md`, if any were produced
14. Open Items, if any
15. Appendix: sources, methodology, arithmetic checks, and data gaps

## Output Rules

- Preserve source labels and evidence tags.
- Do not convert hypotheses into facts.
- Include market-sizing arithmetic in the body or appendix.
- Include all produced strategic-analysis module sections; do not collapse them into
  Strategic Implications unless the strategic-analysis-plan explicitly says the module
  is summary-only.
- Include all produced comprehensive market-pack module sections; do not collapse
  thesis stress-test, GTM, financial, risk, or market entry work into the executive
  summary.
- If `open-issues.md` is non-empty, include a clearly labeled Open Items section
  before the appendix.
- Do not use unsupported promotional language.

Write final document to `{WORK_DIR}/final-output.docx`.

