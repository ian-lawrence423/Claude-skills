# Skill Workflow Tests

Date: 2026-06-10
Branch: `codex/skill-dependency-contracts`

## Purpose

These tests validate skill routing, dependency order, mode selection, and handoff outputs.
They are prompt-level smoke tests, not content-quality tests. A test passes when the agent
loads the expected skills in order, uses the correct mode, and produces the minimum handoff
artifact without invoking unnecessary downstream skills.

## Test Matrix

| Test | User Prompt | Expected Mode | Expected Skill Chain | Required Handoff | Failure Condition |
|---|---|---|---|---|---|
| Market quick view | "What's the market look like for agentic commerce?" | Quick | `mckinsey-consultant` -> `market-research` | Scope, hypothesis, 3-5 findings, caveats, next research step | Produces a full report or invokes production skills |
| Market research brief | "Build a research brief for agentic commerce in enterprise procurement." | Standard | `mckinsey-consultant` -> `market-research` | Research brief, hypothesis tree, source plan, validation standard | Skips problem framing or source strategy |
| Full market deliverable | "Run full market research and produce a Pattern memo." | Full | `mckinsey-consultant` -> `market-research` -> `writing-style` -> `claim-scrutinizer` -> `red-team` -> `pattern-docx` -> `doc-quality-checker` | Research brief, source bibliography, themes, hardened draft, DOCX QA | Produces DOCX before quality passes |
| Competitive durability | "Assess whether Company X has a defensible moat." | Standard | `mckinsey-consultant` -> `market-research` -> `competitive-moat-assessment` | Competitor evidence, moat verdict, durability tests | Runs moat assessment without competitor evidence |
| Standalone NTB triage | "What do I need to believe about this deal?" | Quick | `mckinsey-consultant` -> `ntb-diligence` | Candidate NTBs, evidence gaps, top diligence questions | Forces four-phase workflow without user asking |
| Full NTB diligence | "Run NTB diligence for Company X and build the diligence plan." | Full | `mckinsey-consultant` -> `analytical-operating-system` -> `ntb-diligence` -> `claim-scrutinizer` -> `writing-style` | Confirmed NTB registry, evidence states, diligence plan, stress tests | Skips checkpoint before stress testing |
| IC memo draft | "Write the IC memo for Company X using these materials." | Standard | `deal-master` -> `mckinsey-consultant` -> `analytical-operating-system` -> `ic-memo` -> `writing-style` | 10-section draft, sourced claims, risks, open items | Starts DOCX generation before draft review |
| IC-ready package | "Build the IC-ready package for Company X." | Full | `deal-master` -> `mckinsey-consultant` -> `analytical-operating-system` -> `market-research` -> `ntb-diligence` -> `driver-tree` -> `ic-memo` -> `writing-style` -> `claim-scrutinizer` -> `red-team` -> `pre-mortem` -> `pattern-docx` -> `doc-quality-checker` | Belief register, evidence base, NTB registry, driver tree, hardened memo, QA clean file | Skips evidence control or adversarial passes |
| Driver tree | "Decompose the thesis into a driver tree and show what is load-bearing." | Standard | `mckinsey-consultant` -> `driver-tree` | Driver tree, segment tables, tiers, base-rate overlay, evidence gaps | Produces deal verdict or position sizing |
| Claim redline | "Pressure-test this memo for IC." | Standard | `claim-scrutinizer` -> `red-team` when requested or warranted | Logic tree, assumption audit, claim verdicts, fixes | Runs market research before identifying claim gaps |
| Writing auto-run skip | "Help me think through possible market questions." | None / no auto-run | No `writing-style` unless final prose is requested | Structured working notes only | Auto-runs writing-style on scratch analysis |

## Review Checklist

- Expected chain starts with the governing method skill, not a production skill.
- Quick mode does not create files or run full quality stack by default.
- Standard mode produces reusable handoff artifacts without over-processing.
- Full mode includes evidence control, quality passes, and production QA when a file is requested.
- `writing-style` runs only on final or near-final formal prose.
- `claim-scrutinizer` runs only after a draft, thesis, or claim set exists.
- `pattern-docx` and `pattern-investment-pptx` run only after prose is hardened.

## So What?

Use this file as a smoke-test checklist before publishing future skill changes. If a workflow
fails here, fix the dependency contract or trigger language before editing the methodology.
