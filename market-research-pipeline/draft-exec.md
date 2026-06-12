# Draft — Executive Summary Agent

Load immediately:
- `{SKILLS_PATH}/executive-summary-writer/SKILL.md`
- `{SKILLS_PATH}/mckinsey-consultant/SKILL.md` -> Pyramid Principle and SCR narrative

## Your Inputs

Read all draft files before writing:
- `{WORK_DIR}/draft/context-and-market-sizing.md`
- Every `{WORK_DIR}/draft/[section-slug].md`
- Every `{WORK_DIR}/draft/competitor-[name].md`
- `{WORK_DIR}/themes.md`
- `{WORK_DIR}/source-bibliography.md`
- `{WORK_DIR}/data-gaps.md`

## Constraint

Write a two-page, six-section executive summary using the canonical spine:
Company Overview, Product Offering, Market Dynamic, Business Model,
Thesis: What You Need To Believe, Open Questions.

Do not write a topic preview. The summary must stand alone as the shortest
decision-grade version of the full report.

## Evidence Rules

- Every fact must be supported by a named source already present in `source-bibliography.md`.
- Every estimate must show the relevant assumption or refer to the arithmetic in the body.
- Every hypothesis must be labeled `[H]` and tied to a falsification test.
- Do not use unsupported superlatives such as "leading", "best", "unique",
  "massive", "robust", or "world-class" unless a cited metric proves the statement.

## Output

Write to `{WORK_DIR}/draft/exec-summary.md`.

The summary must:
- Explain the market/company/category orientation first.
- Describe the product/workflow offering when a target company or archetype exists.
- State the market dynamic and business model implication.
- Convert the governing synthesis into 3-5 testable beliefs.
- End with decision-changing open questions.
- Retain only the most important evidence; do not duplicate body sections.
- Avoid the phrase "this report" and all variants.

