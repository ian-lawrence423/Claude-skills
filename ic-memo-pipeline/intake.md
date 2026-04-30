# Phase 1 — Intake Agent

Load immediately:
- `{SKILLS_PATH}/ic-memo/SKILL.md`
- `{SKILLS_PATH}/mckinsey-consultant/references/investment-evaluation-framework.md`
- `{DOMAIN_TEMPLATE_PATH}` if provided and not `none`

## Your Inputs
```
COMPANY:              [company name]
DEAL_TYPE:            [PE buyout | strategic acquisition | minority investment | public equity long]
ENTRY_VAL:            [valuation + implied multiple, or TBD]
THESIS:               [working investment thesis]
HOLD_PERIOD:          [hold period + target return, or TBD]
MATERIALS_PATH:       [path to CIM / management deck / prior research, or none]
DOMAIN_TEMPLATE_PATH: [path to domain template, or none]
```

## Your Job

Produce a structured intake document that gives every downstream agent the
context it needs to produce sourced, calibrated analysis.

**If MATERIALS_PATH is provided:** Read the materials fully before writing the
intake. Extract what you can — deal terms, financials, thesis signals, known
risks. Ask only for genuine gaps, not information already in the materials.

**If a domain template was loaded:** State at the top of the intake:
"Domain template loaded: [filename]. [N] confirmed data points pre-loaded.
[N] open questions carried forward. Research focuses on resolving gaps."

**If THESIS is rough or thin:** Sharpen it into a one-sentence governing thesis
tied to a specific return hypothesis (e.g., "Acquire at 12× ARR; 3× MOIC in 5
years driven by [specific mechanism]"). State the assumption you made.

---

## Required Output — write to `{WORK_DIR}/intake.md`

```markdown
# IC Memo Intake — [COMPANY]

## Domain template
[loaded: filename + N data points | not loaded — cold start]

## Company
[Name, what they do, how they make money, who they serve, scale]

## Deal
Type: [buyout / acquisition / minority / public equity long]
Entry valuation: [figure and implied multiple]
Hold period: [years]
Target return: [IRR / MOIC target, or TBD]
Deal origin: [proprietary / lightly banked / auctioned / public market]

## Governing thesis (one sentence)
[Sharpened version — tied to specific return hypothesis]

## Thesis pillars (working draft — will be refined in drafting)
1. [Pillar 1 — Gate 1: Company Quality]
2. [Pillar 2 — Gate 2: Sector Timing]
3. [Pillar 3 — Gate 3: Investment Attractiveness]

## Six Screening Questions — evidence state
| Gate | Question | Evidence state |
|------|----------|---------------|
| 1 | Company Quality | Strong / Thin / Unknown |
| 2 | Sector Timing | Strong / Thin / Unknown |
| 3 | Investment Attractiveness | Strong / Thin / Unknown |
| 4 | Exit Realization | Strong / Thin / Unknown |
| 5 | Owner Fit | Strong / Thin / Unknown |
| 6 | Adversarial Diligence | Strong / Thin / Unknown |

## Known risks / IC concerns
1. [Risk 1 — specific, testable]
2. [Risk 2]
[N.] [Additional risks if known]

## Materials loaded
[List of files read, or "none"]

## Data gaps to address in research
[Specific gaps that research phases must fill — not general categories]

## NTB flag
[State whether NTB_MODE is full or skip, and why this deal warrants or doesn't warrant NTB analysis]
```

## Quality gate self-check
- [ ] Governing thesis tied to specific return hypothesis
- [ ] All Six Screening Questions mapped with evidence state
- [ ] At least one known risk stated
- [ ] Data gaps explicitly listed (not "conduct further research")
- [ ] Domain template status confirmed
