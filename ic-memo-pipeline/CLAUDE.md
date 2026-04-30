# IC Memo Pipeline

Multi-agent pipeline for producing Pattern-branded Investment Committee memos.

## Agent files (invoke in order per orchestrator.md)

| File | Phase | Agent role |
|------|-------|-----------|
| `orchestrator.md` | — | Main orchestrator — reads this first |
| `intake.md` | 1 | Structured intake + Six Screening Questions |
| `l4-market.md` | 2 | Market sizing + trends (IC memo mode) |
| `l3-customer.md` | 2 | Customer segments + JTBD (IC memo mode) |
| `l2-competitive.md` | 2 | Competitor profiles + white space (IC memo mode) |
| `moat-assessment.md` | 2 | Competitive moat verdict per competitor |
| `ntb-diligence.md` | 3 | NTB registry + diligence plan (if NTB_MODE=full) |
| `draft-sections.md` | 4 | All 10 IC memo sections (SECTION_INDEX param) |
| `pass1-writing-style.md` | 5 | Claim tagging, inductive chains, artifact removal |
| `pass2-claim-scrutinizer.md` | 5 | Seven-part claim test |
| `pass3-red-team.md` | 5 | Adversarial attack pass |
| `pass4-pre-mortem.md` | 5 | Pre-mortem + numeric reconciliation + boundability |
| `output-docx.md` | 6 | pattern-docx body gen + template transplant |

## Key skills consumed

- ic-memo, market-research, mckinsey-consultant
- ntb-diligence, competitive-moat-assessment
- writing-style, claim-scrutinizer, red-team, pre-mortem, boundability
- pattern-docx, doc-quality-checker

## Output location convention

`C:\Users\IanLawrence\OneDrive - Pattern\Ian Productivity\Claude\artifacts\research\[company]-ic-memo\`
