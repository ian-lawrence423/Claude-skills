# deal-intelligence

**Author:** Pattern  
**Version:** 0.1.0

Full PE/M&A/public equity deal workflow — sourcing through IC memo production. Sequences 22 skills across 7 phases. Each phase gates on a verifiable output before proceeding.

## Skills (22)

### Analytical OS
| Skill | Trigger phrases |
|---|---|
| `mckinsey-consultant` | "structure this problem", "screen this deal", "evaluate this investment", "Six Screening Questions", "issue tree" |

### Research & Diligence
| Skill | Trigger phrases |
|---|---|
| `market-research` | "run market research on X", "deep dive on X", "competitive landscape", "size this market" |
| `tam-sam-som-calculator` | "what's the TAM", "size the market", "TAM/SAM/SOM" |
| `competitive-moat-assessment` | "assess the moat", "how defensible is X", "moat depth" |
| `boundability` | "where does the moat hold", "test the limits of this advantage", "boundary conditions" |
| `competitive-landscape-deliverable` | "make an executive view of this landscape", "build deliverable from competitor sheet" |
| `ntb-diligence` | "NTB diligence", "new-to-brand analysis", "customer acquisition quality", "cohort analysis" |
| `driver-tree` | "build a driver tree", "decompose this thesis", "what drives MOIC here" |
| `financial-model-builder` | "build financial model", "3-tab model", "turn this P&L into a model" |
| `gtm-metrics-analyzer` | "analyze these GTM metrics", "build a GTM workbook", "diagnostic on this ARR table" |
| `kpi-tree-builder` | "audit this plan", "break down this budget", "what should we track post-close" |
| `finance-metrics-quickref` | "what's the formula for", "define [metric]", "what's a good benchmark for" |

### Deal Execution
| Skill | Trigger phrases |
|---|---|
| `ic-memo` | "IC memo", "investment committee memo", "write up this deal", "deal memo" |
| `diligence-ddr` | "DDR", "due diligence request list", "data room requests", "diligence checklist" |

### Quality & Adversarial
| Skill | Trigger phrases | Auto-runs? |
|---|---|---|
| `writing-style` | *(auto)* | ✅ before all production |
| `claim-scrutinizer` | "redline this", "scrutinize", "pressure-test", "is this IC-ready" | No |
| `red-team` | "red team this", "attack this thesis", "make the bear case" | No |
| `pre-mortem` | "pre-mortem this deal", "how does this investment fail", "what kills this deal" | No |

### Output Production
| Skill | Trigger phrases | Auto-runs? |
|---|---|---|
| `pattern-docx` | "create a Pattern memo / report / doc" | No |
| `pattern-investment-pptx` | "create an investment deck / IC deck / deal deck" | No |
| `executive-summary-writer` | "write the executive summary", "compress this into one page" | No |
| `doc-quality-checker` | *(auto)* | ✅ after every Pattern doc |

## Agent

**`deal-intelligence`** — Orchestrates the full 7-phase workflow.

| Phase | Skills | Gate |
|---|---|---|
| 0 — Sourcing context | `competitive-landscape-deliverable` | Landscape framing confirmed |
| 1 — Intake & screen | `mckinsey-consultant` · `diligence-ddr` | Gates 1/2/3 scored; DDR issued |
| 2 — Market & competitive | `market-research` · `tam-sam-som-calculator` · `competitive-moat-assessment` · `boundability` | Gate 2 complete; moat verdict; NTB Alignment Check |
| 3 — Deep diligence | `ntb-diligence` · `driver-tree` · `financial-model-builder` · `gtm-metrics-analyzer` · `kpi-tree-builder` | Model built; GTM workbook complete; NTBs evidenced |
| 4 — Draft IC memo | `ic-memo` · `writing-style` | 10-section draft; all claims tagged |
| 5 — Quality passes | `claim-scrutinizer` · `red-team` · `pre-mortem` | All 🔴 CRITICAL resolved; KILL claims hardened |
| 6 — Output | `pattern-docx` / `pattern-investment-pptx` · `doc-quality-checker` · `executive-summary-writer` | Zero 🔴 CRITICAL QC issues |

## Loading policy

This plugin is **opt-in only**. It is not auto-loaded. Reference it explicitly:
- *"Load deal-intelligence"*
- *"Run deal intelligence on [company]"*
- Or invoke any individual skill by name
