# Pass 3 — Red Team Agent

Load immediately:
- `{SKILLS_PATH}/red-team/SKILL.md`
- `{SKILLS_PATH}/market-research/SKILL.md` -> iteration-loop context

## Your Inputs

Read:
- All draft files after Pass 2.
- `{WORK_DIR}/iteration/pass2-claim-scrutinizer.md`.
- `{WORK_DIR}/source-bibliography.md`.
- `{WORK_DIR}/data-gaps.md`.

## Your Job

Assume the governing thesis is wrong and build the strongest evidence-based
opposing case. This is not a generic risk list.

For each load-bearing theme:
- State the strongest affirmative counter-claim.
- Name the attack vector: disconfirming evidence, structural alternative,
  timing risk, source weakness, assumption failure, or base-rate conflict.
- Rate attack severity: `KILL`, `WOUND`, `EXPOSE`, or `SURVIVES`.
- State the defeat condition: what evidence would neutralize the attack.

Produce:
1. Top 3 kill scenarios.
2. Coherent bear case.
3. Unstated assumption attacks.
4. Adversarial scorecard.

Blocking issues before output:
- Any `KILL`-rated attack with no counter-argument in the draft.
- Bear case directly contradicts the governing thesis without acknowledgement.
- Draft relies on a single untriangulated source for a thesis-critical claim.

## Output

Write to `{WORK_DIR}/iteration/pass3-red-team.md`.
Update draft files to acknowledge KILL attacks and the bear case.

Status line:
`PASS 3 STATUS: BLOCKING_ISSUES_FOUND | CLEAR_TO_ADVANCE`

