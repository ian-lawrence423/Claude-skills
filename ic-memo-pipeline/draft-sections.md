# Phase 4 — Section Draft Agent

This prompt handles all 10 section drafts. Each agent invocation receives a
SECTION_INDEX parameter specifying which section to write.

Load immediately:
- `{SKILLS_PATH}/ic-memo/SKILL.md` → Section-by-Section Instructions
- `{SKILLS_PATH}/writing-style/SKILL.md`
- `{DOMAIN_TEMPLATE_PATH}` if provided and not `none`

## Your Inputs
```
SECTION_INDEX: [1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10]
WORK_DIR:      [working directory]
SKILLS_PATH:   [path to skills]
```

Read before starting:
- `{WORK_DIR}/intake.md`
- `{WORK_DIR}/ntb-registry.md` (if exists)
- `{WORK_DIR}/research/l4-market.md`
- `{WORK_DIR}/research/l3-customer.md`
- `{WORK_DIR}/research/l2-competitive.md`
- `{WORK_DIR}/research/moat-assessment.md`

For SECTION_INDEX 2 only: also read all other draft sections (they must exist first).
For SECTION_INDEX 9 only: also read all sections 3–8.
For SECTION_INDEX 10 only: also read all sections 3–9.

---

## Section routing

### SECTION_INDEX=1 → s1-cover.md
Write the Cover Block per ic-memo SKILL.md Section 1 spec.
Output: `{WORK_DIR}/draft/s1-cover.md`

Content:
- Company name (36pt SemiBold)
- "Investment Committee Memorandum"
- Deal type | Date | CONFIDENTIAL
- CONFIDENTIAL footer line

Note for output-docx agent: Cover Block uses run-level formatting (not H1 style).
Document format spec for the cover XML in CLAUDE.md.

---

### SECTION_INDEX=3 → s3-overview.md
Write Section 3: Company Overview per ic-memo SKILL.md.
Output: `{WORK_DIR}/draft/s3-overview.md`

Required elements (all from intake.md — facts only, no estimates):
- Business description: what they do, how they make money, who they serve
- Scale: revenue/ARR, headcount, geography, customer count
- History: founding, key milestones, ownership history
- Current ownership and deal origin (proprietary / lightly banked / auctioned)

Hard ceiling: 1 page. Flag any overflow for the appendix.
All figures must be [F] tagged with source.

---

### SECTION_INDEX=4 → s4-thesis.md
Write Section 4: Investment Thesis per ic-memo SKILL.md.
Output: `{WORK_DIR}/draft/s4-thesis.md`

If ntb-registry.md exists: derive the three thesis pillars from the NTB registry.
Governing thesis = NTB governing thesis. Pillars = top 3 NTBs by MOIC impact.
Do NOT re-derive NTBs inline.

If ntb-registry.md does not exist: derive three pillars from research, each
covering one of Gates 1 (Company Quality), 2 (Sector Timing), 3 (Investment
Attractiveness).

Each pillar must have a complete inductive chain:
- Outcome variable
- Proximate driver
- Gating constraint
- Observable condition

Label every claim [F] / [E] / [H].

---

### SECTION_INDEX=5 → s5-market-competitive.md
Write Section 5: Market & Competitive Position per ic-memo SKILL.md.
Output: `{WORK_DIR}/draft/s5-market-competitive.md`

Sources:
- Market block: draw from l4-market.md findings — do not re-research
- Competitive block: draw from l2-competitive.md profiles + moat-assessment.md verdict
- Each competitor: 2–3 sentences (full profiles in appendix if needed)
- Moat verdict: from moat-assessment.md — state it directly

Addresses Gate 2 (Sector Timing) and Gate 1 competitive position sub-question.

---

### SECTION_INDEX=6 → s6-business-quality.md
Write Section 6: Business Quality per ic-memo SKILL.md.
Output: `{WORK_DIR}/draft/s6-business-quality.md`

Four subsections required (6a–6d):
- 6a: Business Model & Unit Economics (draw from intake + l3 customer findings)
- 6b: Customer Quality (draw from l3-customer.md + intake materials)
- 6c: Management Assessment (from intake materials — specific outcomes, not titles)
- 6d: Competitive Moat summary (from moat-assessment.md — 3 sentences max)

If a metric is unavailable (GRR, NRR, CAC, LTV): label as DATA GAP, do not estimate
without basis. Append to data-gaps.md.

Addresses Gate 1 (Company Quality) in full.

---

### SECTION_INDEX=7 → s7-financials.md
Write Section 7: Financial Analysis per ic-memo SKILL.md.
Output: `{WORK_DIR}/draft/s7-financials.md`

Three subsections (7a–7c):
- 7a: Historical performance — from intake materials / CIM
- 7b: Base case model — state 3 key assumptions explicitly, labeled [F/E/H]
- 7c: Return analysis — base case + downside (50% revenue, no margin expansion, −2× exit multiple)

**CRITICAL:** Establish the Base Assumptions Table here. Every figure used in
subsequent sections (pre-mortem failure spectrums, risk register) must reconcile
to this table. State clearly:
- Entry equity
- Exit multiple (base)
- Hold period
- Base case exit EBITDA/GMV
- Bear case exit EBITDA/GMV

Addresses Gate 3 (Investment Attractiveness).

---

### SECTION_INDEX=8 → s8-deal-structure.md
Write Section 8: Deal Structure & Exit per ic-memo SKILL.md.
Output: `{WORK_DIR}/draft/s8-deal-structure.md`

Two subsections (8a–8b):
- 8a: Deal Structure — entry valuation, capital structure, key terms, co-investors
- 8b: Exit Analysis — primary exit path with named buyers, exit multiple basis,
  timeline + milestones, backup paths

Skip if DEAL_TYPE=public equity long (no deal structure section — note the omission
and state it is N/A for public equity longs per ic-memo SKILL.md compressed structure).

Addresses Gate 4 (Exit Realization) and Gate 5 (Owner Fit).

---

### SECTION_INDEX=9 → s9-risks.md
Write Section 9: Risks & Mitigants per ic-memo SKILL.md.
Output: `{WORK_DIR}/draft/s9-risks.md`

Depends on: all sections 3–8 (read them before drafting this section).

Format: Risk register table
| # | Risk | P (1–5) | M (1–5) | Score | Mitigant | Adequacy |

Rules:
- Minimum 5 risks, maximum 8
- At least one risk must score ≥15
- All risks scoring ≥9 must have a stated mitigant with Adequate/Partial/Insufficient
- Primary risk from Section 2 Executive Summary must appear here with highest or
  second-highest score
- Risks must be specific and testable — not categories

Addresses Gate 6 (Adversarial Diligence).

---

### SECTION_INDEX=10 → s10-recommendation.md
Write Section 10: IC Recommendation per ic-memo SKILL.md.
Output: `{WORK_DIR}/draft/s10-recommendation.md`

Depends on: s9-risks.md (read before drafting).

Four mandatory elements — all required:
1. Recommendation statement: direct binary (proceed / pass / conditional)
2. Walk-away conditions: observable facts that reverse the recommendation
3. Key assumption: the single premise the recommendation rests on
4. Open items: specific questions, named owners, named deadlines

No hedging. "Merits further consideration" fails.

Synthesizes all six Gates into a final binary verdict.

---

### SECTION_INDEX=2 → s2-exec-summary.md
Write Section 2: Executive Summary per ic-memo SKILL.md.
Output: `{WORK_DIR}/draft/s2-exec-summary.md`

Depends on: ALL other sections (read all draft files before writing this).

Load executive-summary-writer SKILL.md → Format A (One-Page Memo).

Structure (five blocks in order):
1. Governing thesis (2 sentences) — conclusion first
2. Three supporting arguments (1 paragraph each ~60 words)
3. Primary risk (2 sentences) — named directly
4. Recommended action (3–4 bullets) — owner, timeline, binary
5. Key assumption (1 sentence)

~400 words. Self-contained — passes cold read test. No section cross-references.
