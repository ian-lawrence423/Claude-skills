# Build Flow Cheat Sheet

**Spine = superpowers. Depth = engineering. Quality checkpoints = productivity.**

## The flow

| # | Do this | Skill |
|---|---------|-------|
| 1 | Pressure-test the idea | `productivity:grilling` |
| 2 | Check what already exists | `engineering:research` |
| 3 | Define what to build | `superpowers:brainstorming` |
| 4 | Structure it (apps only) | `engineering:domain-modeling`, `engineering:codebase-design` |
| 5 | Write the plan, **approve it** | `superpowers:writing-plans` |
| 6 | Work on a separate copy | `superpowers:using-git-worktrees` |
| 7 | Build, tests first | `superpowers:test-driven-development` + `executing-plans` / `subagent-driven-development` |
| 8 | Something broke | `superpowers:systematic-debugging` |
| 9 | Review | `requesting-code-review` / `receiving-code-review` |
| 10 | Prove it works | `superpowers:verification-before-completion` |
| 11 | Ship | `finishing-a-development-branch`, `engineering:pr` |

## By type

- **Skill:** skip 4 and 6. Step 7 = `superpowers:writing-skills` + `skill-authoring-workflow`. Then `productivity:writing-for-agents` on the text.
- **Application:** all 11 steps.
- **Excel app:** 4 = tab structure (inputs / calcs / outputs). 7 = known-answer tests + check cells. 10 = recalc, no `#REF!`, totals tie to source.

## Build missed what you wanted

1. Commit a checkpoint.
2. Write deltas: "wanted X, got Y."
3. Can't write them? Spec gap, go back to steps 1 and 3.
4. Spec was clear? Execution gap, plan only the deltas.
5. Fixes touch the surface: salvage. Fixes touch the foundation: rebuild.

## Rules

- Never skip 1 and 3.
- Approve the plan before building.
- Pick one TDD and one review skill per project.
- One session per phase block; paste the approved plan into the build session.
- Scope every redo: "change only X, leave Y untouched," then check the diff.
