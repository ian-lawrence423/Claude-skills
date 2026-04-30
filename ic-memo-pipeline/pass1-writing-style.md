# Phase 5 — Pass 1: Writing Style Agent

Load immediately:
- `{SKILLS_PATH}/writing-style/SKILL.md`
- `{SKILLS_PATH}/ic-memo/SKILL.md` → Iteration Protocol / Pass 1

## Your Inputs
Read all draft files:
- `{WORK_DIR}/draft/s1-cover.md` through `s10-recommendation.md`

## Your Job

Run writing-style Steps 1–5 on every section. This is a self-review — you
produce a redline AND update the draft files directly.

**Blocking issues (must fix before advancing):**
- Any thesis-critical claim missing [F/E/H] tag
- Any Group E draft artifact language:
  - Version labels (v1, v2, "DRAFT") in body text
  - "(NEW)" tags in section headers
  - "pre-mortem addition:" prefixes
  - FM codes (FM-XX) in body text
  - Changelog subtitles ("Updated: [date]")
- Any broken inductive chain in Section 4 thesis pillars

**Non-blocking (flag but advance):**
- Style suggestions, word choice
- WOUND-level epistemic issues

For each blocking issue: state the location (section + paragraph), the issue,
and the corrected text.

Update draft files in place with hardened prose.

## Required Output — write to `{WORK_DIR}/iteration/pass1-writing-style.md`

```markdown
# Pass 1 — Writing Style Redline
## [COMPANY]

## Blocking issues resolved
[List each issue + fix applied]

## Non-blocking flags
[List each flag — not fixed, carried forward]

## Status: PASS / FAIL
[PASS if all blocking issues resolved; FAIL if any remain after 2 revision cycles]
```
