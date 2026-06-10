# Skill Metadata Audit

Date: 2026-06-10
Branch: `codex/skill-metadata-cleanup`

## Scope

Work Package 3 cleaned discovery metadata without changing skill bodies or analytical workflows.

Applied changes:
- Added standardized `name`, `description`, `intent`, and `type` frontmatter to root skills.
- Shortened root `description` fields to concise discovery summaries under the 200-character standard.
- Moved previous long trigger/context prose into `intent`.
- Synced matching packaged copies from their root skill sources.

## Naming Decision

Frontmatter `name` is canonical for invocation and discovery. Folder names remain packaging paths.

This keeps the existing legacy folders:
- `Deck_Check/` with `name: ib-check-deck`
- `Deck_Refresh/` with `name: deck-refresh`

## Package Sync Policy

Root skill folders remain the canonical authoring source. When root skill metadata changes, matching package copies should be regenerated or copied from root before commit.

Synced package families:
- `plugins/deal-intelligence/skills/`
- `deal-output/skills/`
- `deal-research/skills/`
- `deal-diligence/skills/`
- standalone packaged copies under `analytical-operating-system/skills/` and `deal-master/skills/`

## Validation Targets

Before committing this work package:
- No root skill `description` exceeds 200 characters.
- Every root skill has `name`, `description`, `intent`, and `type`.
- Matching packaged copies are byte-identical to their root `SKILL.md` sources.
- `git diff --check` is clean.
