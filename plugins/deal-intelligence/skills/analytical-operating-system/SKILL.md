---
name: analytical-operating-system
description: >-
  Track evidence states, belief registers, Bayesian updates, kill triggers, and
  decision posture for any analysis, recommendation, or strategic decision.
intent: >-
  Enforces evidence discipline across any analytical workstream: F/E/H claim tagging,
  belief-register initialization, Bayesian updates, kill triggers, and PROCEED / ADJUST /
  PASS / RESOLVE FIRST decision posture. Use with mckinsey-consultant after it has framed
  the problem — this skill owns the operating discipline that keeps beliefs auditable as
  evidence changes.
type: workflow
---

# Analytical Operating System - Evidence Discipline

This skill is the evidence-control layer for any analysis or recommendation. It is not the
primary analytical method. `mckinsey-consultant` owns problem definition, MECE issue trees,
hypothesis framing, Pyramid Principle communication, and analytical modules. This skill owns
the operating discipline that keeps beliefs traceable, auditable, and updated as evidence
changes.

Read this file after loading `mckinsey-consultant` for any workstream where conclusions must
hold up under scrutiny or evolve as new information arrives.

---

## Ownership Boundaries

| Skill | Owns | Does Not Own |
|---|---|---|
| `mckinsey-consultant` | Problem framing, issue trees, hypothesis, analytical modules, decision criteria | Persistent belief registers or phase-to-phase evidence logs |
| `analytical-operating-system` | Evidence-state tagging, belief registers, Bayesian updates, kill triggers, decision posture | New research collection, source validation, or MECE framework design |
| `market-research` | Source strategy, evidence gathering, CRAAP validation, triangulation | Final posture or belief-register ownership |
| `writing-style` | Final prose self-review and claim-language hygiene | Analytical method or operating workflow |

**Rule:** If the question is "how should we structure the problem?", use `mckinsey-consultant`.
If the question is "what do we believe, why, how confident are we, and what changes the decision?",
use this skill on top of `mckinsey-consultant`.

---

## When to Use

Use this skill for:
- Any recommendation where beliefs must survive contact with new evidence
- Any multi-phase workstream where thesis drift is a risk
- Any analysis where load-bearing assertions need explicit confidence levels
- Any decision that requires a clear posture: PROCEED, ADJUST, PASS, or RESOLVE FIRST

Do not use this skill for:
- Quick factual answers, definitions, or generic strategy frameworks
- Research tasks where the job is only to collect and validate sources
- Final prose cleanup where `writing-style` already owns the pass
- Standalone issue-tree work with no tracked thesis or governing belief

---

## Inputs

Before applying this skill, collect the minimum operating context:

| Input | Required? | Purpose |
|---|---:|---|
| Decision to be made | Yes | Defines what the belief register must support |
| Current governing thesis | Yes | Establishes the belief being tested |
| Materials or evidence list | Yes | Anchors [F] and [E] claims to sources |
| Prior belief register | If available | Prevents silent thesis drift |
| Open questions or gaps | If available | Separates unresolved issues from conclusions |
| Stakes or decision impact | If available | Prioritizes load-bearing assertions |

If the decision or thesis is unclear, return `RESOLVE FIRST` and name the one question that must
be answered before continuing.

---

## Evidence States

Every material assertion receives one state:

| Tag | Meaning | Minimum Standard |
|---|---|---|
| `[F]` | Fact | Directly observed, cited, or traceable to a named primary source |
| `[E]` | Estimate | Reasoned from data with method, assumptions, and sensitivity stated |
| `[H]` | Hypothesis | Plausible but unproven; falsifiable and tied to a validation path |

Downgrade rules:
- `[F]` without a traceable source becomes `[E]` or `[H]`
- `[E]` without method and assumptions becomes `[H]`
- `[H]` without a validation path becomes an open question, not a thesis pillar

No thesis-critical assertion can rest on unsupported `[H]` evidence without being named as a
decision risk.

---

## Core Workflow

### Step 1 - Start From the McKinsey Frame

Load `mckinsey-consultant` first. Capture:
- Decision statement
- Issue tree branches
- Day-1 hypothesis
- 20/80 drivers
- Key decision criteria or analytical dimensions in scope

This skill does not rebuild that structure. It converts the structure into an auditable evidence
operating system.

### Step 2 - Inventory Material Assertions

Extract only assertions that can change the decision:
- Thesis pillars
- Need-to-believe statements
- Key risks
- Value or impact drivers
- Open questions or gaps

Exclude background context, generic commentary, and claims with no decision implication.

### Step 3 - Build the Belief Register

Use this format:

| ID | Assertion | Evidence State | Source / Basis | Prior | Latest Evidence | Posterior | Direction | Decision Impact |
|---|---|---|---|---:|---|---:|---|---|
| B1 | [load-bearing assertion] | [F/E/H] | [source or method] | [% or High/Med/Low] | [new evidence] | [% or High/Med/Low] | CONFIRMED / WEAKENED / KILLED / INSUFFICIENT | [PROCEED / ADJUST / PASS / RESOLVE FIRST impact] |

Use numeric confidence only when there is a reasoned basis. Otherwise use High / Medium / Low
and state what evidence would move the rating.

### Step 4 - Apply Bayesian Updates

When new evidence arrives, update only the affected assertions:

```text
UPDATE: [assertion ID]
Prior: [X% or High/Med/Low]
New evidence: [specific evidence and source]
Posterior: [Y% or High/Med/Low]
Direction: CONFIRMED / WEAKENED / KILLED / INSUFFICIENT
Decision implication: [what changes, if anything]
```

Escalate immediately when:
- A load-bearing assertion moves more than 20 percentage points
- A load-bearing assertion falls below 40% confidence
- New evidence contradicts a claimed `[F]`
- A kill trigger is hit
- The governing thesis changes

### Step 5 - Set Decision Posture

Every workstream ends with one posture:

| Posture | Use When | Required Output |
|---|---|---|
| PROCEED | Thesis holds and remaining gaps are bounded | Next action and owner |
| ADJUST | Thesis holds only with modified scope, terms, or conditions | Required change and reason |
| PASS | Thesis fails or unbounded risk remains | One-sentence failure reason |
| RESOLVE FIRST | A specific unanswered question blocks the decision | Question, source, owner, deadline |

Do not present options without a posture.

### Step 6 - Record Thesis Changes

When the thesis changes, document:
- Old thesis
- Evidence that changed it
- New thesis
- Assertions affected
- Prior work superseded
- Decision posture after the change

Never silently revise a prior position.

---

## Example

Example prompt:
> "Update the belief register after this new customer interview and tell me whether the posture changed."

Expected use:
- Extract only material assertions that can change the decision.
- Update evidence states, priors, posteriors, and direction of change.
- End with PROCEED, ADJUST, PASS, or RESOLVE FIRST plus the evidence that would change it.

---

## Output Templates

### Evidence-Control Block

```text
Evidence-control summary
Decision: [decision]
Governing thesis: [one sentence]
Current posture: PROCEED / ADJUST / PASS / RESOLVE FIRST
Most important assertion: [ID + assertion]
Highest-risk gap: [specific question]
Next evidence required: [source + owner + deadline]
```

### Belief Register

Use the Step 3 table. Keep it short: only material assertions that affect the decision belong in
the register.

### Decision Posture

```text
Posture: [PROCEED / ADJUST / PASS / RESOLVE FIRST]
Reason: [one sentence]
Assumes: [top 2-3 conditions]
Would change if: [single most likely reversal condition]
Next action: [owner, timeline, evidence expected]
```

---

## Anti-Patterns

Never:
- Use this skill to duplicate `mckinsey-consultant` issue trees or analytical dimensions
- Treat a hypothesis as a fact because it appears in a polished document
- Maintain a long register of non-material claims
- Update the conclusion without updating the assertions that support it
- Give a PROCEED posture while leaving an unbounded kill-risk unresolved
- Use numeric confidence when the evidence only supports directional confidence

---

## Maintenance Note

This root `SKILL.md` is the source copy. The packaged plugin copy at
`skills/analytical-operating-system/SKILL.md` must remain identical whenever this file changes.
