# New Deal Gold Standard Prompt Sequence

Use this file when starting a new deal analysis that needs a complete, repeatable
package:

1. Gold-standard market research report.
2. Gold-standard competitive assessment.
3. Pattern IC memo.
4. Shared evidence registers and cross-output QA.

The default mode is strict. Thoroughness, source quality, arithmetic, MECE
structure, and visible gaps matter more than speed or polished prose.

---

## Fill These Inputs First

```text
COMPANY: [company name]
DEAL_TYPE: [PE buyout | strategic acquisition | minority investment | public equity long]
THESIS: [rough investment thesis]
GEOGRAPHY: [market scope]
ENTRY_VAL: [entry valuation and implied multiple, or TBD]
HOLD_PERIOD: [hold period and target return]
MATERIALS_PATH: [absolute path to source materials]
WORK_DIR: [absolute path for output]
SKILLS_PATH: C:\Users\IanLawrence\github\Claude-skills
OUTPUT_FORMAT: docx
MARKET_MODE: full
COMPETITIVE_MODE: full
IC_MODE: full
NTB_MODE: full
KPI_MODE: skip
SOURCE_STRICTNESS: strict
```

---

## Option A - Master Kickoff Prompt

Use this when you want the agent to run the whole workflow, but still stop at
phase gates when evidence is incomplete.

```text
Run `deal-master` for a full new-deal package.

Inputs:
COMPANY: [company name]
DEAL_TYPE: [PE buyout | strategic acquisition | minority investment | public equity long]
THESIS: [rough investment thesis]
GEOGRAPHY: [market scope]
ENTRY_VAL: [entry valuation and implied multiple, or TBD]
HOLD_PERIOD: [hold period and target return]
MATERIALS_PATH: [absolute path to source materials]
WORK_DIR: [absolute path for output]
SKILLS_PATH: C:\Users\IanLawrence\github\Claude-skills
OUTPUT_FORMAT: docx
WORKFLOW_MODE: full_deal_pack
MARKET_MODE: full
COMPETITIVE_MODE: full
IC_MODE: full
NTB_MODE: full
KPI_MODE: skip
SOURCE_STRICTNESS: strict

Load in this order:
1. mckinsey-consultant
2. analytical-operating-system
3. new-deal-pipeline/quality-contract.md

Run `new-deal-pipeline/orchestrator.md`.

Required outputs:
1. market-research/final-output.docx
2. competitive-assessment/final-output.docx
3. ic-memo/final-output.docx
4. shared/source-bibliography.md
5. shared/evidence-register.md
6. shared/belief-register.md
7. shared/number-register.md
8. shared/open-issues.md
9. deal-pack-summary.md

Hard rules:
- Every material claim must be tagged [F], [E], [H], [VENDOR], [MGMT], or [GAP].
- Vendor and management claims can orient the work but cannot independently prove thesis-critical conclusions.
- Estimates must show arithmetic and assumptions.
- Market, competitive, and IC memo outputs must use the same evidence spine.
- Do not use unsupported superlatives or promotional language.
- Do not hide evidence gaps in polished prose.
- Return HALT if a thesis-critical claim lacks support, arithmetic is missing, or outputs conflict.

Stop at each phase gate and report PASS, PASS_WITH_GAPS, or HALT before continuing.
```

---

## Option B - Checkpointed Phase Prompts

Use this when quality matters more than speed. Run each prompt separately and
review the gate output before continuing.

### Prompt 1 - Inventory And Evidence Spine

```text
Run `deal-master` for a full new-deal package, but stop after Phase 1.

Inputs:
COMPANY: [company name]
DEAL_TYPE: [PE buyout | strategic acquisition | minority investment | public equity long]
THESIS: [rough investment thesis]
GEOGRAPHY: [market scope]
ENTRY_VAL: [entry valuation and implied multiple, or TBD]
HOLD_PERIOD: [hold period and target return]
MATERIALS_PATH: [absolute path to source materials]
WORK_DIR: [absolute path for output]
SKILLS_PATH: C:\Users\IanLawrence\github\Claude-skills
WORKFLOW_MODE: full_deal_pack
MARKET_MODE: full
COMPETITIVE_MODE: full
IC_MODE: full
NTB_MODE: full
KPI_MODE: skip
SOURCE_STRICTNESS: strict

Load:
1. mckinsey-consultant
2. analytical-operating-system
3. new-deal-pipeline/quality-contract.md

Create:
- shared/materials-index.md
- shared/deal-brief.md
- shared/source-bibliography.md
- shared/evidence-register.md
- shared/belief-register.md
- shared/number-register.md
- shared/open-issues.md

Do not draft market research, competitive assessment, or IC memo yet.

Gate:
- PASS only if the decision, MECE issue tree, source inventory, and belief register exist.
- HALT if there are no usable source materials or the thesis has no decision context.
```

### Prompt 2 - Gold-Standard Market Research

```text
Continue the new-deal package with Phase 2 only: gold-standard market research.

Use:
- market-research-pipeline/orchestrator.md
- docs/market-research-gold-standard-guide.md
- market-research/references/gold-standard-report-template.md
- shared/source-bibliography.md
- shared/evidence-register.md
- shared/belief-register.md
- shared/number-register.md
- shared/open-issues.md

Produce:
- market-research/final-output.docx
- supporting markdown research files
- updated shared/source-bibliography.md
- updated shared/evidence-register.md
- updated shared/number-register.md
- updated shared/open-issues.md

Minimum standard:
- Define market boundary, in-scope, out-of-scope, adjacent markets, and substitutes.
- Size the market with source, scope, period, and arithmetic.
- Identify growth drivers and headwinds with source quality notes.
- Segment customers with JTBD, budget owner, buying trigger, and switching friction.
- Name direct competitors, substitutes, and platform threats.
- Address pricing, unit economics, regulatory risk, technology risk, and adoption risk.

Hard rules:
- No unsupported market-size or growth claims.
- No vendor claim can independently validate a thesis-critical point.
- Every paragraph must validate a point, show evidence, explain implication, or name a gap.

Return market research status: PASS, PASS_WITH_GAPS, or HALT.
```

### Prompt 3 - Gold-Standard Competitive Assessment

```text
Continue the new-deal package with Phase 3 only: gold-standard competitive assessment.

Use:
- new-deal-pipeline/competitive-assessment.md
- market-research/SKILL.md
- competitive-moat-assessment/SKILL.md
- red-team/SKILL.md
- docs/competitive-assessment-gold-standard-guide.md
- shared evidence registers
- market-research output from Phase 2

Produce:
- competitive-assessment/competitive-assessment.md
- competitive-assessment/source-map.md
- competitive-assessment/open-issues.md
- competitive-assessment/final-output.docx
- updated shared/evidence-register.md
- updated shared/number-register.md
- updated shared/open-issues.md

Required analysis:
- Direct competitors.
- Substitutes.
- Adjacent platforms.
- Non-consumption.
- Buyer, user, economic decision-maker, blocker.
- Buying criteria and rank order.
- Switching threshold and migration risk.
- Competitor evidence table.
- Moat mechanism, metric, evidence, strength, durability, erosion vector, and verdict.
- Displacement path.

Hard rules:
- Do not call product breadth, UX, relationships, or current execution a moat unless it creates measurable resistance to displacement.
- Vendor websites can describe product claims but cannot prove traction, retention, pricing power, or adoption.
- HALT if the moat verdict lacks mechanism, metric, evidence, or replicability horizon.

Return competitive assessment status: PASS, PASS_WITH_GAPS, or HALT.
```

### Prompt 4 - Strategic Diligence Bridge

```text
Continue the new-deal package with Phase 4 only: strategic diligence bridge.

Use:
- ntb-diligence/SKILL.md
- driver-tree/SKILL.md
- boundability/SKILL.md
- market research output
- competitive assessment output
- shared evidence registers

Produce:
- diligence/ntb-registry.md
- diligence/driver-tree.md
- diligence/boundability.md
- updated shared/belief-register.md
- updated shared/open-issues.md

Required standard:
- Create 4 to 7 Need-to-Believe statements.
- Every NTB must map to evidence, source, decision impact, kill trigger, and diligence owner.
- Driver tree must decompose the thesis into causal drivers with evidence tiers.
- Boundability must test where the thesis holds versus degrades by geography, segment, product, customer type, and operating condition.

Hard rules:
- Stop if a base-case thesis depends on a T4 unsupported driver.
- Do not convert weak evidence into softened prose.
- Carry unresolved diligence items into open-issues.md.

Return diligence bridge status: PASS, PASS_WITH_GAPS, or HALT.
```

### Prompt 5 - IC Memo

```text
Continue the new-deal package with Phase 5 only: IC memo.

Use:
- ic-memo-pipeline/orchestrator.md
- ic-memo/SKILL.md
- executive-summary-writer/SKILL.md
- pattern-docx/SKILL.md
- market-research/final-output.docx
- competitive-assessment/final-output.docx
- diligence/ntb-registry.md
- diligence/driver-tree.md
- diligence/boundability.md
- shared evidence registers

Produce:
- ic-memo/final-output.docx
- ic-memo supporting markdown files
- updated shared/claim-ledger.md
- updated shared/open-issues.md

Required memo behavior:
- Treat market research and competitive assessment as upstream evidence, not optional background.
- Do not re-research Phase 2 or Phase 3 unless source staleness or gaps require it.
- Retain evidence tags and sources for reused claims.
- Use the executive summary spine: Company Overview, Product Offering, Market Dynamic, Business Model, Thesis, Open Questions.
- Keep unresolved gaps visible in the executive summary, risk section, and recommendation.

Hard rules:
- Zero unaddressed KILL claims.
- Zero conflicting recurring numbers.
- Zero thesis-critical claims without evidence tag and source.
- Do not convert open questions into generic risk language.

Return IC memo status: PASS, PASS_WITH_GAPS, or HALT.
```

### Prompt 6 - Cross-Output QA

```text
Run Phase 6: cross-output QA for the full new-deal package.

Compare:
- market-research/final-output.docx
- competitive-assessment/final-output.docx
- ic-memo/final-output.docx
- shared/evidence-register.md
- shared/number-register.md
- shared/open-issues.md

Create:
- deal-pack-summary.md

Check:
- Same market definition across all outputs.
- Same competitor set or explicit reason for differences.
- Same source and value for repeated market size, growth, valuation, retention, and margin figures.
- Same moat verdict or explicit explanation for changed confidence.
- Same open questions carried into the IC memo.
- No unsupported superlatives or promotional language.
- No thesis-critical vendor or management claim used as independent proof.

Return release posture:
- CLEAR_TO_RELEASE
- RELEASE_WITH_GAPS
- HALTED

If HALTED, list the exact blocking claims, missing sources, conflicting numbers, and required next evidence.
```

---

## Resume Prompt

Use this when a run already exists and you want the agent to continue from the
last completed phase.

```text
Resume the full new-deal package from this folder:
WORK_DIR: [absolute path]
MATERIALS_PATH: [absolute path]
SKILLS_PATH: C:\Users\IanLawrence\github\Claude-skills

Load:
1. deal-master
2. mckinsey-consultant
3. analytical-operating-system
4. new-deal-pipeline/quality-contract.md

Inventory all existing outputs and classify the current state.

Do not rerun completed phases unless:
- sources are stale,
- a register is missing,
- outputs conflict,
- or a prior phase has thesis-critical gaps.

Print:
- completed phases,
- skipped phases with reason,
- next phase,
- blocking gaps,
- current release posture.
```

---

## Final Quality Standard

The work is not complete until all requested outputs exist and the cross-output
QA gate has run.

Do not accept:
- unsupported thesis-critical claims,
- formulaic claims without arithmetic,
- vendor or management claims as independent proof,
- missing market boundaries,
- moat claims without mechanism and metric,
- conflicting numbers across outputs,
- unsupported superlatives,
- polished narrative that hides gaps.

