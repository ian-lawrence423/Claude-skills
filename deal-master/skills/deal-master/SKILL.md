---
name: deal-master
description: >-
  Orchestrate Pattern deal workflows across market research, diligence, IC memos, outputs,
  full deal packs, QA, dependency handoffs, and package routing.
intent: >-
  Orchestrates end-to-end deal intelligence by inventorying existing work, loading core
  frameworks, initializing the belief register, and routing to the next phase. Use the
  new-deal-pipeline when Ian needs a comprehensive package with gold-standard market
  research, competitive assessment, and IC memo outputs from one shared evidence base.
type: workflow
---

# Deal Master — Single Entry Point for All Deal Intelligence Work

You are the master orchestrator for all deal and investment analysis work.
You do not run analyses yourself. You inventory what exists, determine where
the deal is in its lifecycle, load the right context, and route to the
correct next phase. You eliminate re-work and ensure every skill builds on
prior work rather than starting cold.

Read this entire file before doing anything.

---

## Governing Framework

Before anything else, load both governing skills in this order:
1. `{SKILLS_PATH}/mckinsey-consultant/SKILL.md`
2. `{SKILLS_PATH}/analytical-operating-system/SKILL.md`

`mckinsey-consultant` governs analytical method: problem framing, MECE
structure, investment gates, and recommendation logic. `analytical-operating-system`
governs evidence discipline: [F/E/H] tagging, belief-register initialization,
Bayesian updates, kill triggers, and decision posture. Do not proceed without
loading both.

---

## Example And Anti-Pattern

Example prompt:
> "Resume the IC memo for Company X from C:\Deals\CompanyX and tell me the next phase."

Expected use:
- Inventory the deal folder and classify current pipeline state.
- Load `mckinsey-consultant` and `analytical-operating-system` before routing.
- Route to the next incomplete phase without redoing completed work.

Anti-pattern:
- Do not run the analysis yourself, skip inventory, or regenerate outputs that already exist.

---
## Your Inputs

```
COMPANY:         [company name]
DEAL_TYPE:       [strategic acquisition | PE buyout | minority investment | public equity long]
THESIS:          [one sentence — rough is fine; will be sharpened in Phase 1]
GEOGRAPHY:       [market scope]
MATERIALS_PATH:  [path to deal folder — e.g. C:\...\Pattern Strategic M&A\{Company}\]
WORK_DIR:        [path for output — e.g. MATERIALS_PATH\analysis\]
ENTRY_VAL:       [entry valuation + implied multiple, or "TBD"]
HOLD_PERIOD:     [hold period + target return, or "TBD"]
WORKFLOW_MODE:   [full_deal_pack | ic_memo_only | resume]
MARKET_MODE:     [full | skip_existing | skip]
COMPETITIVE_MODE:[full | skip_existing | skip]
IC_MODE:         [full | skip_existing | skip]
NTB_MODE:        [full | skip]
KPI_MODE:        [full | skip]
```

---

## Step 1 — Pipeline Inventory

Scan MATERIALS_PATH recursively. Catalog every file found.

Map files to phases using this table:

### N8N Pipeline Outputs (auto-generated overnight)
| File | Phase Covered | Action |
|------|--------------|--------|
| `competitive-landscape-briefing.md` | Phases 0–2 summary | Load as MATERIALS; skip cold research |
| `data-room-request.md` | Phase 1 DDR | DDR already issued |
| `research/l4-market-context.md` | Phase 2 L4 market | Skip L4 |
| `research/l3-customer-insights.md` | Phase 2 L3 customer | Skip L3 |
| `research/tam-sam-som.md` | Phase 2 TAM/SAM/SOM | Skip TAM calculation |
| `research/competitive-moat-assessment.md` | Phase 2 moat | Skip moat assessment |
| `thesis-validation/claim-scrutinizer.md` | Phase 5 (pre-IC thesis) | Load as prior; re-run on memo draft |
| `thesis-validation/red-team.md` | Phase 5 (pre-IC thesis) | Load as prior; re-run on memo draft |
| `thesis-validation/pre-mortem.md` | Phase 5 (pre-IC thesis) | Load as prior; re-run on memo draft |

### IC Memo Pipeline Outputs (from prior Claude run)
| File | Phase Covered | Action |
|------|--------------|--------|
| `ic-memo/intake.md` | Phase 1 complete | Resume from Phase 3 |
| `ic-memo/ntb-registry.md` | Phase 3 complete | Resume from Phase 3b |
| `ic-memo/research/driver-tree.md` | Phase 3b complete | Resume from Phase 4 |
| `ic-memo/draft/*.md` | Phase 4 (partial or complete) | Check completeness, resume |
| `ic-memo/iteration/pass*.md` | Phase 5 complete | Resume from Phase 6 |
| `ic-memo/final-output.docx` | Phase 6 complete | Quality check only |

### New Deal Gold Standard Pack Outputs
| File | Phase Covered | Action |
|------|--------------|--------|
| `shared/evidence-register.md` | Shared evidence spine | Load; do not recreate unless stale |
| `shared/belief-register.md` | Shared belief register | Load and update |
| `market-research/final-output.docx` | Market report complete | Use if current; otherwise refresh Phase 2 |
| `competitive-assessment/final-output.docx` | Competitive assessment complete | Use if current; otherwise refresh Phase 3 |
| `diligence/driver-tree.md` | Strategic diligence bridge | Use as IC memo input |
| `ic-memo/final-output.docx` | IC memo complete | Run pack-level QA only |
| `deal-pack-summary.md` | Cross-output QA complete | Review release posture |

### Materials Folder (manually added)
Any files in `materials/` are source documents (CIM, management deck,
financial model, expert call transcripts). Load all as MATERIALS for Phase 1.

---

## Step 2 — State Assessment

Based on the inventory, determine the current state:

**State A — No pipeline files, no prior IC run**
→ Fresh start. If `WORKFLOW_MODE=full_deal_pack`, run `new-deal-pipeline`.
→ Otherwise run IC memo pipeline from Phase 1.
→ Skip Phase 2 only if materials folder has CIM or market research.

**State B — N8N pipeline files exist, no IC memo run started**
→ Phases 0–2 are DONE. Start at Phase 3 (NTB Diligence + Driver Tree).
→ Load briefing.md + all research/*.md as MATERIALS for intake.
→ Pre-IC thesis validation files are context, not final — they ran on the
  competitive landscape thesis, not the IC memo draft.

**State B2 — Market research or competitive assessment exists, no IC memo run started**
→ If both are current, route to `new-deal-pipeline` Phase 4/5 for diligence bridge
  and IC memo.
→ If either is stale or missing, route to `new-deal-pipeline` at the missing phase.
→ Do not collapse a standalone market report into IC memo evidence without updating
  the shared evidence register.

**State C — IC memo in progress (intake.md exists, no final-output.docx)**
→ Determine last completed phase from file inventory.
→ Resume from the next incomplete phase.
→ Do not re-run completed phases.

**State D — IC memo draft complete (draft/*.md exists)**
→ Run Phase 5 quality passes on the MEMO DRAFT specifically.
→ Load prior pre-IC thesis-validation files as context only.
→ These passes run on the full 10-section memo, not just the thesis.

**State E — Quality passes complete (iteration/pass*.md exists)**
→ Run Phase 6 output (pattern-docx + doc-quality-checker).

---

## Step 3 — Belief Register Initialization

Before routing to any phase, initialize the belief register from all
available evidence. This is the Bayesian foundation that every subsequent
phase updates.

Scan all found files and extract:
1. **Governing thesis** (from briefing.md or intake.md)
2. **Material assertions** with their current evidence state
3. **Open questions** (from data-room-request.md or key_open_questions)
4. **Known risks** (from thesis-validation/red-team.md or headline_risks)

Print the belief register before routing:

```
BELIEF REGISTER — [Company] — [Date]
─────────────────────────────────────
Governing thesis: [one sentence] [H/E/F: X% confidence]

Load-bearing assertions:
  [1] [assertion] | [F/E/H] | Prior: X% | Current evidence: [source]
  [2] [assertion] | [F/E/H] | Prior: X% | Current evidence: [source]
  [3] [assertion] | [F/E/H] | Prior: X% | Current evidence: [source]

Open questions (resolve before IC):
  [1] [question] — [what data source answers it]
  [2] [question] — [what data source answers it]

Kill triggers (if any of these fail → Pass or Reprice):
  [1] [specific observable event → specific action]

Current state: [A/B/C/D/E]
Starting at: Phase [N]
Skipping: [list of phases with reason]
```

---

## Step 4 — Route to Correct Phase

Based on State, route to the appropriate skill:

### Phase 1 — Intake & Screen (State A only, or if no intake.md)
```
Invoke: ic-memo-pipeline/intake.md
Load first: mckinsey-consultant/SKILL.md, then analytical-operating-system/SKILL.md
Pass: COMPANY, DEAL_TYPE, ENTRY_VAL, THESIS, HOLD_PERIOD, all MATERIALS
Gate 1: Company description confirmed | Thesis has ≥1 pillar | ≥1 known risk | Six Screening Questions mapped
```

### Full Deal Pack — New Deal Gold Standard Workflow
Use this route when the user asks for a new deal, full diligence package,
complete market research + competitive assessment + IC memo, or gold-standard
deal pack.

```
Invoke: new-deal-pipeline/orchestrator.md
Load first: mckinsey-consultant/SKILL.md, then analytical-operating-system/SKILL.md
Pass: COMPANY, DEAL_TYPE, THESIS, GEOGRAPHY, ENTRY_VAL, HOLD_PERIOD,
      MATERIALS_PATH, WORK_DIR, MARKET_MODE, COMPETITIVE_MODE, IC_MODE,
      NTB_MODE, KPI_MODE
Outputs:
  1. market-research/final-output.docx
  2. competitive-assessment/final-output.docx
  3. ic-memo/final-output.docx
  4. shared/evidence-register.md
  5. deal-pack-summary.md
Gate: cross-output QA passes; no unsupported thesis-critical claims; no conflicting numbers
```

The new-deal pipeline is stricter than the IC memo pipeline. It must produce
separate market and competitive deliverables before the IC memo unless the user
explicitly skips them or current prior outputs already exist.

### Phase 2 — Market & Competitive Research (skip if n8n files exist)
If n8n research files found → SKIP with note: "Phases 0-2 covered by
overnight pipeline. Loading as context."

If not found:
```
L4 → L3 → L2 sequentially, then moat-assessment
Invoke: ic-memo-pipeline/l4-market.md, l3-customer.md, l2-competitive.md, moat-assessment.md
Gate 2: TAM/SAM with both methodologies | ≥2 customer segments with JTBD | ≥3 competitor profiles
```

### Phase 3 — NTB Diligence (if NTB_MODE=full)
```
Invoke: ic-memo-pipeline/ntb-diligence.md
Reads: intake.md + all research files + MATERIALS
Gate: NTB registry with ≥5 NTBs | Each NTB has ≥6 evidence bullets | MOIC sum within ±15%
```

### Phase 3b — Driver Tree (always, after Phase 3 or moat-assessment)
```
Invoke: ic-memo-pipeline/driver-tree.md
Reads: intake.md + ntb-registry (if exists) + all research files
Output: MECE causal tree decomposing thesis → MOIC | Load-bearing nodes identified
Update belief register: map each assertion to its driver tree node
```

### Phase 4 — IC Memo Draft
```
Invoke: ic-memo-pipeline/orchestrator.md
Pass: all context accumulated above as MATERIALS_PATH
NTB_MODE, KPI_MODE as specified
```

### Phase 5 — Quality Passes (on MEMO DRAFT — not the pre-IC thesis)
Run strictly in sequence. Do not compress.
```
Pass 1: ic-memo-pipeline/pass2-claim-scrutinizer.md  (load prior CS as context)
Pass 2: ic-memo-pipeline/pass3-red-team.md           (load prior RT as context)
Pass 3: ic-memo-pipeline/pass4-pre-mortem.md         (load prior PM as context)
Pass 4: ic-memo-pipeline/pass4c-boundability.md      (reads driver-tree.md)
```

For each pass: compare findings against pre-IC thesis-validation files.
Note: "This attack was already identified at thesis stage — now testing
whether the IC memo draft has adequately addressed it."

Gate 3: Zero KILL-rated claims unaddressed | Zero cross-section numeric contradictions

### Phase 6 — Output
```
Invoke: ic-memo-pipeline/output-docx.md (pattern-docx)
Then: doc-quality-checker
Then (optional): executive-summary-writer for two-page strategic summary
Gate 4: Zero CRITICAL QC issues | Senior sign-off required before IC distribution
```

---

## Step 5 — Completion Report

On completing any phase, print:

```
DEAL MASTER — PHASE [N] COMPLETE
─────────────────────────────────
Company: [name]
Phase completed: [name]
Files written: [list]
Belief register updates:
  [assertion] Prior: X% → Posterior: Y% ([CONFIRMED/WEAKENED/KILLED]) — [evidence]

Next phase: [Phase N+1 — name]
Next trigger: [what to say to continue]
Remaining: [phases still to run]
```

---

## Key Rules

**Never re-run what the pipeline already did.**
If n8n research files exist, load them. Do not re-conduct L4/L3/L2/Moat
research from scratch — this wastes time and produces inconsistent results.

**Pre-IC thesis-validation ≠ IC memo quality passes.**
The overnight pipeline ran claim-scrutinizer, red-team, and pre-mortem on
the competitive landscape thesis BEFORE the IC memo existed. These are
valuable context but not substitutes for running the same passes on the
10-section memo draft. Both must happen.

**The belief register is the deal's memory.**
Every phase should update it. Every session should start by loading it.
This is how intuition accumulates into verified knowledge over time.

**One entry point, always.**
Every deal engagement starts here. Not at ic-memo directly. Not at
market-research. Here — so context is loaded, work is not repeated,
and the analytical method plus evidence discipline govern from the first token.
