# Pattern Production Spec Split

Date: 2026-06-10
Branch: `codex/pattern-production-spec-split`

## Scope

This branch reduces root skill size for the two production-heavy Pattern output skills without changing their generation rules.

Moved reference material:
- `pattern-docx/references/production-spec.md`
  - Brand constants
  - Paragraph type reference
  - Numbering config
  - Table style reference
  - Fallback-only Python patch workflow
  - Section layout reference
- `pattern-investment-pptx/references/deck-production-spec.md`
  - Brand constants and color methodology
  - Slide layout and grid
  - Recurring slide elements
  - Slide templates
  - Bullet hierarchy
  - Chart rules
  - Table rules
  - Layout selection guide

## Root Skill Role

The root `SKILL.md` files now own:
- Triggering and examples
- Required upstream technical references
- Asset discovery
- Canonical template / production workflow routing
- Critical rules
- Writing-style and QA gates
- Final output handoff to `doc-quality-checker`

The reference files own implementation detail that should be loaded only when generating or modifying the underlying DOCX/PPTX production code.

## Package Sync

Matching reference folders were synced into:
- `deal-output/skills/pattern-docx/references/`
- `deal-output/skills/pattern-investment-pptx/references/`
- `plugins/deal-intelligence/skills/pattern-docx/references/`
- `plugins/deal-intelligence/skills/pattern-investment-pptx/references/`

## Validation Targets

Before commit:
- Root metadata remains compliant.
- Root `SKILL.md` files contain readable reference pointers.
- Package copies match root `SKILL.md` and reference files.
- `git diff --check` passes.
