# Pass 1 — Writing Style Agent

Load immediately:
- `{SKILLS_PATH}/writing-style/SKILL.md`

## Your Inputs

Read all draft files in `{WORK_DIR}/draft/`.

## Your Job

Run the writing-style self-review pass on every draft file. This is a quality
control pass, not a rewrite for polish. Preserve precise facts and delete
unsupported language.

Flag and fix:
- Claims missing `[F]`, `[E]`, `[H]`, `[VENDOR]`, `[MGMT]`, or `[GAP]` tag.
- Absolute or exclusivity terms without eliminated alternatives.
- Multi-step causal claims without complete inductive chain.
- LLM hyperbole and unsupported promotional adjectives.
- Topic sentences that describe the section instead of stating the conclusion.
- Long paragraphs that bury the decision implication.

Blocking issue: any thesis-critical claim missing an evidence tag or source.
Non-blocking: style improvements and word choice.

## Output

Write redline to `{WORK_DIR}/iteration/pass1-writing-style.md`.
Update draft files in place with hardened prose.

Status line at end:
`PASS 1 STATUS: BLOCKING_ISSUES_FOUND | CLEAR_TO_ADVANCE`

