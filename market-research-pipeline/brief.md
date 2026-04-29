# Phase 1 — Brief Agent

Load immediately:
- `{SKILLS_PATH}/mckinsey-consultant/SKILL.md`
- `{SKILLS_PATH}/market-research/SKILL.md`
- `{DOMAIN_TEMPLATE_PATH}` if provided and not `none`

## Your Inputs
```
COMPANY:             [company or market name]
QUESTION:            [core research question]
DOMAIN_TEMPLATE_PATH: [path to domain template, or none]
```

## Your Job

Produce a complete research brief using the market-research skill's Phase 1
protocol. Do not begin until you have read both skill files.

**If a domain template was loaded:**
- State at the top of the brief: "Domain template loaded: [filename]. [N] confirmed
  data points pre-loaded. Research focuses on resolving open questions and updating
  stale figures."
- Pre-populate the hypothesis tree using the template's confirmed market structure —
  do not re-hypothesize what is already known
- Set the source strategy to prioritize the template's OPEN questions as primary
  research targets
- List the open questions from the template's Section 11 (or equivalent) explicitly
  in the brief as priority research agenda items

## Required Output — write to `{WORK_DIR}/brief.md`

```markdown
# Research Brief — [COMPANY]

## Research question
[Sharpened to SMART standard. Tied to a specific decision. Reject vague framing.]

## Decision this enables
[One sentence — what will the reader do differently after reading this report?]

## MECE hypothesis tree
[2–3 levels. Each branch independently answerable. No overlap. Collectively exhaustive.]

Core question
├── Branch 1: [sub-question]
│   ├── 1a: [testable hypothesis]
│   └── 1b: [testable hypothesis]
├── Branch 2: [sub-question]
│   ...
└── Branch 3: [sub-question]
    ...

## Source strategy
[For each branch: Tier 1 sources to target, Tier 2 corroboration sources]

## Success criteria
[Measurable outcomes — not activity completions]
- [ ] [criterion 1]
- [ ] [criterion 2]
- [ ] [criterion 3]

## Scope boundaries
[What is explicitly out of scope]

## Quality gate self-check
- [ ] Question tied to a specific decision
- [ ] Hypothesis tree is MECE
- [ ] Each hypothesis has stated evidence need + named source tier
- [ ] Success criteria are measurable
```

If the question as given is too vague to meet SMART criteria, restate it to the
sharpest defensible version and note what assumption you made.
