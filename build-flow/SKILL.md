---
name: build-flow
description: >-
  Use when building a skill or application, or when a build missed what you wanted. Routes the fixed flow: grill, research, brainstorm, plan, build with tests, review, verify, ship.
intent: >-
  Single reference for the build lifecycle across superpowers, engineering, and productivity skills. Tells Ian which skill to run at each phase, how the flow differs for a skill versus an application, and how to recover when a finished build is not what was imagined. Does not replace the skills it routes to; it only sequences them.
type: workflow
---

## Purpose

Remove the need to remember which of ~25 skills runs when. Superpowers is the spine (order of work). Engineering skills are specialist depth inside the spine. Productivity skills sit at the two points where thinking or writing quality decides the outcome.

Use it at the start of any build, and again whenever a build does not match the intent.

## Key Concepts

### The Flow

| # | Phase | Skill | Output |
|---|-------|-------|--------|
| 1 | Pressure-test the idea | `productivity:grilling` | Weak assumptions found before building |
| 2 | Research what exists | `engineering:research` | Constraints, prior art, build-vs-reuse call |
| 3 | Define what to build | `superpowers:brainstorming` | Agreed requirements and design |
| 4 | Model and architect (apps only) | `engineering:domain-modeling`, `engineering:codebase-design` | Entities, boundaries, structure |
| 5 | Plan | `superpowers:writing-plans` | Step-by-step plan, approved by Ian |
| 6 | Isolate | `superpowers:using-git-worktrees` | Work off the main branch |
| 7 | Build | `superpowers:test-driven-development`, then `executing-plans` or `subagent-driven-development`; `dispatching-parallel-agents` for independent pieces | Tested code |
| 8 | Fix what breaks | `superpowers:systematic-debugging` (`engineering:diagnosing-bugs` as specialist) | Root-cause fixes |
| 9 | Review | `requesting-code-review`, `receiving-code-review` (`engineering:code-review` as second lens) | Reviewed diff |
| 10 | Prove it works | `superpowers:verification-before-completion` | Evidence, not assertion |
| 11 | Ship | `finishing-a-development-branch`, `engineering:pr` | Merged or PR'd |

### What Counts as an Application

An application is anything with inputs, logic, and outputs that is reused. Hosting is not part of the definition: an Excel workbook rerun with new data is an application; a one-off analysis is not.

For Excel applications, the steps translate as follows:
- Step 4: tab structure with inputs, calcs, and outputs separated (see `financial-model-builder`).
- Step 6: a versioned copy of the file, or the file in git.
- Step 7: known-answer test cases, check cells, and reconciliation rows that tie to source. Build with `xlsx`, `financial-model-builder`, `deal-workbook-builder`, `kpi-tree-builder`, or `gtm-metrics-analyzer`.
- Step 9: formula audit for hardcodes, inconsistent formulas across a row, and broken references.
- Step 10: recalculate with test inputs, confirm no `#REF!`, and confirm totals tie to source.
- Step 11: save to the agreed location with a version name.

### Skill vs. Application

- **Skill:** steps 4 and 6 are mostly optional. Replace step 7 with `superpowers:writing-skills` plus `skill-authoring-workflow`. Run `productivity:writing-for-agents` on the SKILL.md text. Test against scenarios built to make it fail, not only the happy path.
- **Application:** all 11 steps apply. Steps 4 and 7 carry the most weight.

### Rules That Keep the Flow Clean

1. Steps 1 and 3 are never skipped. Most bad builds are fuzzy requirements, not bad code.
2. The plan (step 5) is approved before execution. It is the cheapest control point.
3. Where superpowers and engineering overlap (TDD, code review), pick one per project. Default to superpowers; use engineering as a deeper second pass.
4. One session per phase block. Brainstorm and plan in one; build in another with the approved plan pasted in, so the spec does not drift.
5. Every redo is scoped explicitly ("change only X, leave Y untouched") and the diff is checked.

## Application

### Starting a Build

1. State what is being built and whether it is a skill or an application.
2. Run steps 1-5 in order. Stop at step 5 for approval.
3. Run steps 6-11. If a named skill is not installed, do that step inline and say so.

### When the Build Is Not What Was Imagined

1. Commit the current state as a checkpoint.
2. Write the gap as concrete deltas: "wanted X, got Y." If the deltas cannot be written, treat it as a spec gap.
3. Classify the gap:
   - **Spec gap** (the wanted outcome was never defined): return to steps 1 and 3, write the real spec, then plan only the delta.
   - **Execution gap** (spec was clear, build missed it): plan only the listed deltas and fix them test-first.
4. Decide salvage vs. rebuild. Salvage if fixes touch the surface. Rebuild if fixing the deltas means changing the foundation.
5. Scope each fix explicitly and review the diff for unrelated changes.

## Examples

### Example: New Skill

"Build a skill that drafts board updates." Run grilling on the idea, research existing skills (`executive-briefing` may already cover it), brainstorm the spec, plan, build with `writing-skills` and `skill-authoring-workflow`, then `writing-for-agents` on the text, verify against failure scenarios, ship.

### Example: Build Missed Intent

An app was built but the dashboard is wrong. Deltas written: "wanted weekly cohorts, got monthly totals." Classified as an execution gap. Plan covers only the cohort query and chart; the rest is listed as untouched.

### Anti-Pattern

"It's not quite right, redo it." No deltas, no scope, no checkpoint. The correction then reshapes everything, including parts that were fine.

## Common Pitfalls

- Starting at step 7 because the idea feels clear.
- Running both superpowers and engineering versions of TDD or review, which doubles the process.
- Skipping plan approval and finding the misread at step 10.
- Treating a spec gap as an execution gap and patching forever.
- Carrying one long session through every phase until compaction blurs the approved spec.

## References

- `skill-authoring-workflow/SKILL.md`
- `superpowers/skills/using-superpowers/SKILL.md`
- `superpowers/skills/writing-skills/SKILL.md`
- `CHEATSHEET.md`
- `agents.md` (Group 8: Meta / Workflow)
