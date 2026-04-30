# Phase 3 — NTB Diligence Agent

Load immediately:
- `{SKILLS_PATH}/ntb-diligence/SKILL.md`
- `{SKILLS_PATH}/mckinsey-consultant/references/investment-evaluation-framework.md`
- `{DOMAIN_TEMPLATE_PATH}` if provided and not `none`

## Your Inputs
Read before starting:
- `{WORK_DIR}/intake.md`
- `{WORK_DIR}/research/l4-market.md`
- `{WORK_DIR}/research/l3-customer.md`
- `{WORK_DIR}/research/l2-competitive.md`
- `{WORK_DIR}/research/moat-assessment.md`

## Your Job

Produce a structured NTB registry for this deal. The registry becomes the
structural frame for Section 4 (Investment Thesis pillars), the diligence plan
feeds Section 10 (open items), and the stress tests feed Section 9 (risks).

**If a domain template was loaded and it contains a prior NTB registry:**
- Use the template's NTB registry as the starting point
- Verify each NTB against the current research findings
- Update evidence state and confidence levels
- Add new NTBs if research surfaces material new assumptions
- Do NOT re-derive NTBs that are already confirmed in the template

**NTB standard (from ntb-diligence SKILL.md):**
Each NTB must be:
- A specific, testable assumption (binary: true or false)
- Tied to a specific MOIC impact if false
- Supported by evidence at a stated tier (T1–T4)
- Associated with a specific diligence action that can confirm or refute it

## Required Output — write to `{WORK_DIR}/ntb-registry.md`

```markdown
# NTB Registry — [COMPANY]

## Governing thesis
[One sentence — the single most important reason this is a good investment]

## NTB Registry

### NTB-1: [Name]
**Statement:** [Specific, testable assumption]
**MOIC impact if false:** [quantified]
**Evidence tier:** T[1-4]
**Evidence:** [source + confidence]
**Diligence action:** [specific action that confirms or refutes]
**Status:** Confirmed / Unconfirmed / Refuted

[Repeat for each NTB — minimum 3, maximum 7]

## Diligence plan
| NTB | Action | Owner | Due | Binary outcome |
|-----|--------|-------|-----|----------------|

## Stress test summary
[For each NTB scoring high MOIC impact: brief stress test of what happens to
the thesis if this NTB is refuted]

## Kill criteria
[Specific NTB outcomes that, if confirmed, cause the recommendation to reverse]
```
