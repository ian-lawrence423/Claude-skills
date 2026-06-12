---
name: claude-code-codex-handoff
description: >-
  Create or consume rigorous handoffs between Claude Code and Codex, preserving repo state,
  branch context, files changed, validation, blockers, and next steps.
intent: >-
  Standardize agent-to-agent handoffs between Claude Code and Codex so work can resume without
  rework, lost branch context, accidental main edits, or unclear validation state.
type: workflow
---

# Claude Code / Codex Handoff

Use this when the user asks to hand work from Claude Code to Codex, from Codex to Claude Code,
to resume from a handoff file, or to prepare a clean re-entry prompt for another coding agent.

## Core Rule

The handoff is a state-transfer artifact, not a status update. It must let the next agent resume
without guessing the repo, branch, files, commands, validation state, or remaining decision.

## Modes

### 1. Create Handoff

Use when handing current work to another agent.

1. Identify the target agent: `Claude Code`, `Codex`, or `Either`.
2. Verify current state before writing:
   - `pwd` / absolute repo path
   - `git status --short --branch`
   - current branch and upstream
   - last relevant commit SHA
   - changed, staged, and untracked files
3. Write the handoff file in the repo or project root unless the user gives another path.
4. Keep unrelated dirty work explicitly labeled as unrelated; never imply it is part of the task.
5. Include exact commands already run and validation results.
6. End with a paste-ready prompt for the next agent.

Default filenames:
- Codex should create `CODEX_TO_CLAUDE_HANDOFF.md` when handing to Claude Code.
- Claude Code should create `CLAUDE_TO_CODEX_HANDOFF.md` when handing to Codex.
- Use an existing project-specific filename if one already exists, such as `CODEX_DESKTOP_HANDOFF.md`.

### 2. Consume Handoff

Use when starting from a handoff file.

1. Read the handoff first.
2. Verify live repo state against the handoff before editing.
3. If branch, cwd, or dirty files differ, state the delta before proceeding.
4. Re-run only the minimum validation needed to confirm the handoff is still current.
5. Continue from the next action; do not restart the whole project unless the handoff is stale.

### 3. Update Handoff

Use after completing part of the work but before handing off again.

1. Append or replace the status section with current state.
2. Record new commits, pushes, deployments, files changed, and validation.
3. Rewrite the next-agent prompt so it reflects the current next step, not the old objective.

## Required Handoff Structure

Use this order.

```markdown
# <Project / Task> Handoff

## Objective
One or two sentences describing the actual goal, not just the last command.

## Target Agent
Claude Code / Codex / Either.

## Current Repo State
- Repo path:
- Current branch:
- Upstream:
- Latest commit:
- Working tree:
- Unrelated dirty files:

## What Changed
- Files changed:
- Data/assets added:
- Commits created:
- Branches pushed:
- Deployments / preview URLs:

## Commands Run
List material commands and short outcomes. Include failed commands if they affect next steps.

## Validation
- Tests/checks run:
- Browser/manual checks:
- Data tie-outs:
- Not run:

## Open Issues
- Blockers:
- Risks:
- Decisions needed:

## Next Steps
1. First exact action for the next agent.
2. Second action.
3. Stop condition.

## Paste-Ready Prompt For Next Agent
Copy/paste prompt that includes the repo path, branch, objective, and first verification command.
```

## Quality Bar

A good handoff answers four questions:

1. **Where am I?** Exact repo path, branch, upstream, and worktree state.
2. **What happened?** Files, commits, pushes, deploys, commands, validation.
3. **What is safe?** Unrelated dirty work, protected branches, files not to touch, restore points.
4. **What next?** The next agent's first command and clear stop condition.

## Paste-Ready Prompt Patterns

### Claude Code to Codex

```text
Continue from <absolute path to CLAUDE_TO_CODEX_HANDOFF.md>.
First verify:
1. cd "<repo path>"
2. git status --short --branch
3. git log -3 --oneline --decorate

Then continue the stated next step. Do not revert unrelated local changes.
If the live branch or dirty files differ from the handoff, report the delta before editing.
```

### Codex to Claude Code

```text
Continue from <absolute path to CODEX_TO_CLAUDE_HANDOFF.md>.
First verify the repo path, current branch, upstream, dirty files, and latest commit.
Then continue the "Next Steps" section only. Preserve unrelated user changes.
If validation is stale, rerun only the checks named in the handoff.
```

## Anti-Patterns

- "Everything is done" without commit SHA, branch, or validation.
- "See recent changes" without listing files.
- Hiding failed commands.
- Handing off from the wrong cwd.
- Writing a handoff that assumes the next agent can inspect your chat history.
- Mixing unrelated dirty files into the task summary.

## So What

The next agent should spend the first minute verifying state, not reconstructing history.
