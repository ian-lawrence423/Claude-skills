# Phase 6 — Output Agent (pattern-docx)

Load immediately:
- `{SKILLS_PATH}/pattern-docx/SKILL.md`

## Your Inputs
Read before starting:
- `{WORK_DIR}/draft/s1-cover.md` through `s10-recommendation.md`
- `{WORK_DIR}/open-issues.md`
- `{WORK_DIR}/source-bibliography.md`

## Your Job

Generate the final Pattern-branded IC memo DOCX following the two-phase process
in pattern-docx SKILL.md.

**Phase 1 — Body generation (docx-js):**
Build all 10 sections using the brand constants and paragraph type reference
from pattern-docx SKILL.md. Apply these section-specific rules:

- Cover block: Normal paragraphs with run-level formatting (not H1 style)
  Company name: 36pt SemiBold, color 1F4E79
  "Investment Committee Memorandum": 20pt, color 2E75B6
  Deal type | Date | CONFIDENTIAL: italic, color 595959
  CONFIDENTIAL footer line: 9pt Bold, color C00000

- Sections 1–10: H1 for section headers (numbered, page break before, blue 4280F4)
  H2 for subsections (6a-6d, 7a-7c, 8a-8b) — indigo 3A00FD
  Body text: Wix Madefor Display, 18 half-pt, black
  All [F/E/H] labels remain in the final document — do not strip them

- Risk table (Section 9): standard data table with 0F4761 header row
  Score column: color cells by value — ≥15 red (C00000), 9–14 orange (C55A11), <9 standard
  Adequacy column: color by value — Adequate green (375623), Partial orange (C55A11),
  Insufficient red (C00000)

- Open issues appendix: include content from open-issues.md if non-empty

**Phase 2 — Template transplant (Python):**
Transplant canonical header/footer from:
`C:\Users\IanLawrence\OneDrive - Pattern\Ian Productivity\Claude\artifacts\research\pattern-redo-pe\Pattern_Redo_PE_Memo_v7_2026-03-20.docx`

Update header title to: `[COMPANY] — Investment Committee Memorandum`

Writes: `{WORK_DIR}/final-output.docx`

**After output:** Do NOT invoke doc-quality-checker here — that is a separate
Phase 7 agent invocation. Simply confirm the file was written and report its
byte size.
