# Claude Skills — Quick Reference

> Full documentation: `README.md` · Full operating system: `agents.md`

---

## What to invoke for common tasks

| Task | Skill(s) to invoke |
|------|--------------------|
| Start or resume a deal workflow | `deal-master` |
| Structure a problem / build issue tree | `mckinsey-consultant` |
| Track evidence state / belief register for a deal | `analytical-operating-system` |
| Market research — full project | `market-research` + `docs/market-research-gold-standard-guide.md` + `gold-standard-report-template.md` |
| Size a market (TAM/SAM/SOM) | `tam-sam-som-calculator` |
| Competitive landscape + moat verdict | `market-research` → `competitive-moat-assessment` |
| Porter's Five Forces | `market-research` (L2 agent) |
| Write an IC memo | `ic-memo-pipeline` (full run) or `ic-memo` (standalone) |
| NTB diligence | `ntb-diligence` |
| Build a driver / causal tree | `driver-tree` |
| Decompose a KPI / operating target | `kpi-tree-builder` |
| Boundability verdict on an NTB | `boundability` |
| Pre-mortem on a deal | `pre-mortem` |
| Adversarial bear case | `red-team` |
| Redline claims / pressure-test doc | `claim-scrutinizer` |
| Write / clean up any formal prose | `writing-style` (auto-runs) |
| Two-page executive summary | `executive-summary-writer` |
| Executive briefing / one-pager | `executive-briefing` |
| Build a financial model | `financial-model-builder` |
| Generate a DDR | `diligence-ddr` |
| GTM diagnostic workbook | `gtm-metrics-analyzer` |
| SaaS metric lookup | `finance-metrics-quickref` |
| Post-close KPI tree + 100-day plan | `kpi-tree-builder` (via ic-memo-pipeline Phase 8) |
| Executive view of competitive landscape sheet | `competitive-landscape-deliverable` |
| Pattern Word document | `pattern-docx` |
| Pattern investment deck | `pattern-investment-pptx` |
| QA a Pattern document | `doc-quality-checker` (auto-runs) |
| Create or update a skill | `skill-authoring-workflow` |

---

## Mandatory layer sequence for any formal output

```
0. deal-master                 — inventory existing work, route deal workflow
1. mckinsey-consultant         — frame the problem, govern methodology
2. analytical-operating-system — maintain evidence states, belief register, decision posture
3. market-research             — gather evidence (L4→L3→L2)
4. writing-style               — prose quality, claim tagging       ← AUTO
5. claim-scrutinizer           — seven-part claim test
6. red-team                    — adversarial pass
7. pre-mortem                  — failure mode inventory
8. pattern-docx / pptx         — produce the file
9. doc-quality-checker         — brand + QA gate                   ← AUTO
```

Not every output requires the full sequence. Step 0 applies to full deal workflows. Steps 4 and 9 are always mandatory when a formal file is produced.
Step 2 is mandatory for deal-master, IC memo, diligence, and investment thesis workflows.
Steps 5–7 are mandatory for IC memos and investment documents.

---

## Pipelines (multi-agent workflows)

| Pipeline | When to use | Mode flags |
|----------|-------------|-----------|
| `ic-memo-pipeline` | Full IC memo from intake to branded DOCX | `NTB_MODE`: full/skip · `KPI_MODE`: full/skip |
| `market-research-pipeline` | Standalone gold-standard market research report | — |

---

## Full market research report minimum spine

Use this when the user asks for a full standalone market research report, board-ready market study, or IC-supporting market analysis.

| Section | Required artifact |
|---------|-------------------|
| Cover and KPI strip | 4-6 category-framing metrics |
| Context and scope | Scope table or value-chain map |
| Executive Summary | Two-page six-section summary |
| Market Sizing | Frame comparison + source/scope + arithmetic checks |
| Customer Segmentation | Buyer archetype + JTBD table |
| Competitive Landscape | Competitor map + substitute workflow table |
| Pricing and Unit Economics | Pricing archetype + economics benchmark table |
| Technology Trends | Trend signal + disruption map |
| Regulatory/Risk | Regulation table with "do not over-claim" column |
| Moat Analysis | Moat scorecard + replicability horizon |
| Strategic Implications | Underwriting/action table |
| Appendix | Methodology, source labels, arithmetic corrections, open questions |

Reference docs: `docs/market-research-gold-standard-guide.md` and `market-research/references/gold-standard-report-template.md`.

---

## Skills that always pair

| If you invoke... | Also load... |
|-----------------|-------------|
| `deal-master` | `mckinsey-consultant`, `analytical-operating-system` |
| `ic-memo-pipeline` | `mckinsey-consultant`, `analytical-operating-system` |
| `market-research` | `mckinsey-consultant`, `competitive-moat-assessment` (post-L2), `writing-style` before production |
| `ic-memo` | `ntb-diligence` (if NTB_MODE=full), `driver-tree`, `executive-summary-writer` (S2) |
| `driver-tree` | `boundability` (use load-bearing nodes as boundability units) |
| `pre-mortem` | `boundability` (pass 4c converts failure modes to underwriting actions) |
| `pattern-docx` | `doc-quality-checker` (auto-runs after file delivery) |
| `ntb-diligence` | `driver-tree` (maps NTBs to gating nodes) |
| `tam-sam-som-calculator` | `market-research` L4 (TAM/SAM sizing step) |

---

## Skills that are intentionally NOT paired

| Skip this... | When... | Why |
|-------------|---------|-----|
| `kpi-tree-builder` | Inside ic-memo-pipeline (pre-close) | Post-close only — don't build a KPI tree on pre-diligence assumptions |
| `market-research` L1 (company position) | IC memo mode | ic-memo intake + CIM already covers L1 — running it duplicates work |
| `writing-style` | Never skip | Always runs on formal output — skipping produces a draft, not a deliverable |

---

## ic-memo-pipeline — phase map

```
Phase 0   Domain template check
Phase 1   Intake → Gate 1
Phase 2   L4 market → L3 customer → L2 competitive → Moat assessment → Gate 2
Phase 3   NTB diligence (NTB_MODE=full)
Phase 3b  Driver tree
Phase 4   S1 → [S3/S4/S5/S6/S7/S8 parallel] → S9 → S10 → S2 (exec summary last)
Phase 5   Pass 1 (writing-style) → Pass 2 (claim-scrutinizer) → Pass 3 (red-team)
          → Pass 4 (pre-mortem + numeric reconciliation) → Pass 4c (boundability) → Gate 3
Phase 6   Output (pattern-docx)
Phase 7   QA gate (doc-quality-checker) → Gate 4
Phase 8   KPI tree (KPI_MODE=full) — post-close, no gate
```

---

## Output location convention

```
C:\Users\IanLawrence\OneDrive - Pattern\Ian Productivity\Claude\artifacts\research\[company]-[type]\
```

---

## Pattern brand quick-ref

| Element | Value |
|---------|-------|
| Font | Wix Madefor Display / Wix Madefor Display SemiBold |
| Section headers (H1) | `#4280F4` |
| Subheaders (H2) | `#3A00FD` |
| Table headers | `#0F4761` (fill) + `#FFFFFF` (text) |
| Body | `#000000` |
| Red callouts | `#C00000` |
| Orange callouts | `#C55A11` |
| Green callouts | `#375623` |
| Word doc header | Pattern logo + gradient line — Python XML patch, NOT docx-js |
| Canonical template | `Commerce_Market_Research_v9_2026-04-29.docx` + `market-research/references/gold-standard-report-template.md` |

---

## Generated reference docs

| File | Purpose |
|------|---------|
| `docs/Claude_Skills_README.docx` | Word version of the skill library overview |
| `docs/Claude_Skills_CheatSheet_v2.docx` | Quick-reference task map and layer checklist |
| `docs/Claude_Skill_Library_External (Finance)_v6.docx` | Finance and investment workflow reference |
| `docs/Market_Research_Gold_Standard_Guide.docx` | Standalone guide for the most thorough market research report |
| `docs/IC_Memo_Gold_Standard_Guide.docx` | Standalone guide for the most thorough IC memo |
| `docs/Competitive_Assessment_Gold_Standard_Guide.docx` | Standalone guide for competitive assessment and moat analysis |
| `docs/Executive_Summary_Gold_Standard_Guide.docx` | Standalone guide for a two-page executive summary |
| `docs/Strategic_Diligence_Gold_Standard_Guide.docx` | Standalone guide for NTB diligence and underwriting handoff |

Regenerate with `docs/generate_claude_docs.py` after source Markdown changes.
