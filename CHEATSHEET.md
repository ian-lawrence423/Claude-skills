# Claude Skills — Quick Reference

> Full documentation: `README.md` · Full operating system: `agents.md`

---

## What to invoke for common tasks

| Task | Skill(s) to invoke |
|------|--------------------|
| Structure a problem / build issue tree | `mckinsey-consultant` |
| Market research — full project | `market-research` |
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
| Executive summary (compress analysis) | `executive-summary-writer` |
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
1. mckinsey-consultant   — frame the problem, govern methodology
2. market-research       — gather evidence (L4→L3→L2)
3. writing-style         — prose quality, claim tagging       ← AUTO
4. claim-scrutinizer     — seven-part claim test
5. red-team              — adversarial pass
6. pre-mortem            — failure mode inventory
7. pattern-docx / pptx  — produce the file
8. doc-quality-checker   — brand + QA gate                   ← AUTO
```

Not every output requires all 8 steps. Steps 3 and 8 are always mandatory.
Steps 4–6 are mandatory for IC memos and investment documents.

---

## Pipelines (multi-agent workflows)

| Pipeline | When to use | Mode flags |
|----------|-------------|-----------|
| `ic-memo-pipeline` | Full IC memo from intake to branded DOCX | `NTB_MODE`: full/skip · `KPI_MODE`: full/skip |
| `market-research-pipeline` | Standalone market research report | — |

---

## Skills that always pair

| If you invoke... | Also load... |
|-----------------|-------------|
| `market-research` | `mckinsey-consultant`, `competitive-moat-assessment` (post-L2) |
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
| Canonical template | `Commerce_Market_Research_v9_2026-04-29.docx` |
