# Phase 5 — Pass 3: Red Team Agent

Load immediately:
- `{SKILLS_PATH}/red-team/SKILL.md`
- `{SKILLS_PATH}/red-team/references/red-team-investment-attacks.md`

## Your Inputs
Read before starting:
- All draft files (post-Pass 2)
- `{WORK_DIR}/iteration/pass2-claim-scrutinizer.md`
- `{WORK_DIR}/ntb-registry.md` (if exists)

## Your Job

Load Type A investment attack lenses. Attack load-bearing thesis pillars first.
For each pillar in Section 4: generate the strongest credible bear case and test
whether the document acknowledges and addresses it.

**Attack priority order:**
1. Thesis pillars (Section 4) — each pillar individually
2. Financial projections (Section 7) — revenue CAGR and exit multiple
3. Moat claims (Section 6d) — durability under stress
4. Management assessment (Section 6c) — track record specificity

**Verdict taxonomy:**
- `KILL` — attack destroys the claim with no counter-argument possible
- `WOUND` — attack creates material risk; document must acknowledge it
- `EXPOSE` — attack is plausible and IC will raise it; preemptive acknowledgment needed

**Blocking (must resolve before Pass 4):**
- Any `KILL`-rated attack with no counter-argument
- Bear case that directly contradicts governing thesis without acknowledgement in text

Update draft files: add counter-arguments or acknowledgements where needed.

## Required Output — write to `{WORK_DIR}/iteration/pass3-red-team.md`

```markdown
# Pass 3 — Red Team
## [COMPANY]

## Attack vectors by pillar

### Pillar 1 — [Name]
**Attack:** [strongest bear case]
**Verdict:** KILL / WOUND / EXPOSE
**Counter-argument / acknowledgement added:** [yes/no + what was added]

[Repeat for each pillar and major claim]

## KILL verdicts
[Any remaining KILLs after revision — must be empty to pass Gate 3]

## WOUND flags (carried forward)
[Acknowledged in text — carried to open-issues for IC prep]

## Status: PASS / FAIL
```
