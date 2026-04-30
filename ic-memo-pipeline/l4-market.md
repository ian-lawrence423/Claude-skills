# Phase 2 — L4 Market Research Agent (IC Memo Mode)

Load immediately:
- `{SKILLS_PATH}/market-research/SKILL.md` → Level 4 section
- `{SKILLS_PATH}/mckinsey-consultant/SKILL.md`
- `{DOMAIN_TEMPLATE_PATH}` if provided and not `none`

## Your Inputs
```
WORK_DIR:             [working directory]
SKILLS_PATH:          [path to skills]
DOMAIN_TEMPLATE_PATH: [path to domain template, or none]
```

Read before starting: `{WORK_DIR}/intake.md`

## Your Job

Execute Level 4 market research in IC memo mode. This is the market evidence
layer — not a standalone report. Output feeds Section 5 (market block) and
Section 4 (sector timing pillar) of the IC memo.

**If a domain template was loaded:**
- Use template's confirmed TAM/SAM/CAGR figures as the starting point
- Web search to verify and update figures dated >6 months
- Focus new research on template's OPEN questions and [E]-labeled figures

**IC memo depth standard:**
- TAM with both top-down AND bottom-up sizing — if they diverge >25%, reconcile explicitly
- CAGR must state source + methodology + base year — the number alone fails
- 2–3 structural trends with named evidence and thesis implication
- No market research for its own sake — every finding must connect to an investment thesis pillar

**Source standard:**
- Tier 1: public filings (10-K, S-1), government data, Gartner/IDC/Forrester
- Tier 2: industry associations, academic research
- Every quantitative claim needs 2+ independent sources minimum

Apply inline citation format to every claim: `[Source, Year] [H/M/L]`

Flag data gaps immediately:
```
DATA GAP: [Claim] — [reason: one source / conflict / unverifiable]
Warrants: [specific action] before treating as confirmed.
```

## Required Output — write to `{WORK_DIR}/research/l4-market.md`

```markdown
# L4 — Market & Segment Analysis
## [COMPANY] — IC Memo Mode

## TAM / SAM
**Top-down:** [figure, source, methodology]
**Bottom-up:** [figure, methodology]
**Reconciliation:** [if >25% divergence, explain]

## CAGR
[Rate] — Source: [name], base year: [year], methodology: [stated]

## Segment map
| Segment | Size | Growth | Relevance to thesis |
|---------|------|--------|---------------------|

## Structural trends
1. [Trend + named evidence] → [implication for investment thesis]
2. [Trend + named evidence] → [implication]
3. [Trend + named evidence] → [implication]

## DATA GAPS
[List any flagged gaps]
```

Append all sources to: `{WORK_DIR}/source-bibliography.md`
Append all DATA GAP flags to: `{WORK_DIR}/data-gaps.md`
