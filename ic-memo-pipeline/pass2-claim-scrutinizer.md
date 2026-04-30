# Phase 5 — Pass 2: Claim Scrutinizer Agent

Load immediately:
- `{SKILLS_PATH}/claim-scrutinizer/SKILL.md`
- `{SKILLS_PATH}/mckinsey-consultant/references/investment-evaluation-framework.md`

## Your Inputs
Read before starting:
- All draft files (post-Pass 1): `{WORK_DIR}/draft/s1-cover.md` through `s10-recommendation.md`
- `{WORK_DIR}/source-bibliography.md`
- `{WORK_DIR}/data-gaps.md`
- `{WORK_DIR}/iteration/pass1-writing-style.md`

## Your Job

Run the full seven-part claim-scrutinizer test on every material claim in the
draft. This is a Type A investment document — load the investment attack lenses.

**Mandatory focus areas (per ic-memo SKILL.md):**
- Section 4: every pillar sub-claim passes logic and evidence tests
- Section 6: management track record passes circular reasoning check
- Section 7: financial projections pass projection scrutiny and base rate check
- Section 10: walk-away conditions are binary (not risk categories)

**Verdict taxonomy:**
- `KILL` — claim must be removed or fundamentally revised
- `NEEDS EVIDENCE` — claim requires sourced support to stand
- `WOUND` — claim weakened by specific vulnerability; note but do not kill
- `EXPOSE` — claim will draw fire; ensure document acknowledges the risk

**Blocking issues (must resolve before Pass 3):**
- Any `KILL`-rated claim
- Any `NEEDS EVIDENCE` on a thesis-critical claim
- Any open DATA GAP that is thesis-critical

Update draft files in place with hardened claims.
Unresolved `WOUND` and `EXPOSE` flags carry forward to open-issues.md.

## Required Output — write to `{WORK_DIR}/iteration/pass2-claim-scrutinizer.md`

```markdown
# Pass 2 — Claim Scrutinizer Redline
## [COMPANY]

## KILL verdicts resolved
[Claim | Section | Issue | Resolution]

## NEEDS EVIDENCE resolved
[Claim | Section | Evidence added]

## WOUND flags (carried forward)
[Claim | Section | Vulnerability | Carried to open-issues]

## EXPOSE flags (carried forward)
[Claim | Section | Risk | Carried to open-issues]

## Status: PASS / FAIL
```
