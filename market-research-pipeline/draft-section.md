# Draft — Theme Section Agent

Load: `{SKILLS_PATH}/market-research/SKILL.md` → Section: Phase 4, Section Anatomy

## Your Inputs
```
THEME_INDEX: [N]
THEME_FILE:  {WORK_DIR}/themes.md  (read theme N)
RESEARCH:    all four research files
```

## Section Anatomy (apply exactly — four elements, in order)

1. **Headline** — insight statement, not a label
   - Wrong: "Competitive dynamics"
   - Right: "Platform consolidation is accelerating — the window for independent
     point solutions is closing faster than most incumbents recognize"

2. **Evidence block** — 3–5 specific findings with inline citations
   - Every claim tagged [F/E/H] + [H/M/L] confidence
   - DATA GAPs acknowledged where they exist

3. **Strategic implication** — what this means for the company or investment thesis
   - Specific and actionable — not generic
   - Tied to the theme's "so what" from themes.md

4. **Data gaps and caveats** (if any) — acknowledged explicitly, not buried

## Output — write to `{WORK_DIR}/draft/section-[N].md`
Target length: 2–4 pages (DOCX) / 2–3 slides (PPTX)
