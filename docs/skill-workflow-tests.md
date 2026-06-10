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

## Content Refinement Smoke Tests

These prompts validate that each core skill now has a concrete example path and an explicit
anti-pattern boundary. A test passes when the agent follows the expected use case and avoids
the named anti-pattern.

| Skill | Smoke-Test Prompt | Expected Signal | Anti-Pattern To Catch |
|---|---|---|---|
| `deal-master` | "Resume the IC memo for Company X from this deal folder." | Inventories prior work, loads governing skills, routes to next phase | Starts fresh analysis without inventory |
| `mckinsey-consultant` | "Structure the investment case from these existing materials." | Produces decision, hypothesis, MECE tree, and recommendation logic | Gathers new sources or creates branded output |
| `analytical-operating-system` | "Update the belief register after this transcript." | Updates material assertions, confidence, and posture | Rebuilds the issue tree or tracks immaterial claims |
| `market-research` | "Build a research brief for this market." | Defines scope, hypothesis tree, source plan, and validation standard | Produces final report before evidence validation |
| `ic-memo` | "Draft the IC memo from this source pack." | Consumes upstream evidence and drafts memo sections before production | Starts with DOCX generation |
| `ntb-diligence` | "What do we need to believe for this deal to work?" | Produces load-bearing NTBs, evidence states, and diligence tests | Turns every risk into an NTB |
| `driver-tree` | "Decompose the thesis into value drivers." | Produces causal driver tree and load-bearing tiers | Gives final deal verdict |
| `claim-scrutinizer` | "Pressure-test this memo for IC." | Reconstructs logic tree and redlines claims | Summarizes instead of challenging claims |
| `writing-style` | "Tighten this final memo section." | Fixes claim tags, attribution, language, and flow | Auto-runs on scratch notes |
| `red-team` | "Make the strongest bear case." | Attacks load-bearing assumptions and names kill conditions | Produces generic risk list |
| `pre-mortem` | "Assume this investment failed in year 3." | Maps concrete failure pathways and evidence needs | Recommends proceed/pass instead of diagnosing |
| `boundability` | "Where does this moat stop working?" | Tests geography, segment, and product boundaries | Treats advantage as universal |
| `pattern-docx` | "Turn this approved memo into a Pattern DOCX." | Uses canonical template workflow and runs QA | Builds from generic DOCX defaults |
| `pattern-investment-pptx` | "Build a Pattern investment deck from this approved memo." | Uses Pattern deck system and hardened content | Creates a generic marketing deck |
| `doc-quality-checker` | "QA this Pattern memo before I send it." | Severity-rates exact-location findings | Silently auto-fixes or gives general opinion |

## So What?

Use this file as a smoke-test checklist before publishing future skill changes. If a workflow
fails here, fix the dependency contract or trigger language before editing the methodology.
