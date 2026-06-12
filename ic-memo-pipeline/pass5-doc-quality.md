# Pass 5 — Document Quality Agent

Load immediately:
- `{SKILLS_PATH}/doc-quality-checker/SKILL.md`
- `{SKILLS_PATH}/pattern-docx/SKILL.md`

## Your Inputs

```
WORK_DIR:    [working directory]
SKILLS_PATH: [path to skills]
```

Read:
- `{WORK_DIR}/final-output.docx`
- `{WORK_DIR}/open-issues.md`
- `{WORK_DIR}/source-bibliography.md`
- `{WORK_DIR}/iteration/pass1-writing-style.md`
- `{WORK_DIR}/iteration/pass2-claim-scrutinizer.md`
- `{WORK_DIR}/iteration/pass3-red-team.md`
- `{WORK_DIR}/iteration/pass4-pre-mortem.md`
- `{WORK_DIR}/iteration/pass4b-numeric-reconciliation.md`
- `{WORK_DIR}/iteration/pass4c-boundability.md`

## Purpose

Run final quality control on the produced Pattern Word document. This pass checks
whether the IC memo is ready to distribute, not whether the thesis is attractive.
Do not hide unresolved evidence gaps. A polished document with unsupported claims
fails this pass.

## Required Checks

1. **Brand and document integrity**
   - Pattern header/footer present.
   - Fonts, colors, section styles, table formatting, page numbers, and spacing match `pattern-docx`.
   - No broken tables, orphaned section labels, placeholder text, or draft markers.

2. **Narrative structure**
   - Recommendation is answer-first.
   - Section titles and opening paragraphs state conclusions, not topics.
   - Executive summary is self-contained and uses the six-section spine.
   - Risks and open questions are visible, not buried.

3. **Evidence and claim discipline**
   - Every material fact has a source.
   - Every estimate shows assumptions or arithmetic.
   - Every hypothesis is labeled and not presented as fact.
   - Vendor / management claims are labeled.
   - No LLM hyperbole or unsupported superlatives.

4. **Cross-document consistency**
   - Figures in the executive summary match body sections.
   - Final recommendation reflects unresolved KILL / WOUND / Unboundable items.
   - Open issues match the latest quality-pass outputs.

## Output

Write to `{WORK_DIR}/iteration/pass5-doc-quality.md`.

Required format:

```markdown
# IC Memo Document Quality Check

## Status
PASS 5 STATUS: CLEAR_TO_RELEASE | BLOCKING_ISSUES_FOUND

## Critical Findings
| Finding | Location | Required Fix |
|---|---|---|

## Major Findings
| Finding | Location | Recommended Fix |
|---|---|---|

## Minor Findings
| Finding | Location | Polish Fix |
|---|---|---|

## Release Decision
[CLEAR_TO_RELEASE / REBUILD_REQUIRED]
```

## Blocking Conditions

Any CRITICAL finding blocks release. Missing sources, unresolved numeric conflicts,
broken Pattern branding, unsupported thesis-critical claims, and hidden open issues
are always CRITICAL.

