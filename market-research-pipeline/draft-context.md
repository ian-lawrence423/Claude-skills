# Draft - Context And Market Sizing Agent

Load: `{SKILLS_PATH}/market-research/SKILL.md` -> Phase 4, Report Architecture
Load: `market-research/references/gold-standard-report-template.md`

## Your Inputs
brief.md + l4-market.md + themes.md + artifact-plan.md

## Constraint
Produce the Context and Scope plus Market Sizing foundation for the report. This
is not a raw L4 dump. It must define scope and make the market sizing defensible.

Required content:
- Value-chain, workflow, or category-scope definition
- In-scope vs. out-of-scope boundaries
- Market sizing frame comparison
- Source/scope reconciliation table
- CAGR and total arithmetic checks
- Key sub-segment or geography cut when it changes the answer
- For strategic-analysis runs, a bottom-up buyer/ICP build when the addressable
  population is narrower than the broad market
- Explicit separation between reference market, analytic slice, and upside scenario

## Output - write to `{WORK_DIR}/draft/context-and-market-sizing.md`

Use two headings:
1. `Context and Scope`
2. `Market Sizing`

All claims retain inline citations from L4 research. Pattern internal constructions
must be labeled separately from external reference markets.

If a strategic-analysis-plan exists, read it before drafting. Any module that depends
on market boundary, buyer population, regulatory scope, data sensitivity, or unit
economics should have its core assumptions introduced here so later sections do not
redefine the market.
