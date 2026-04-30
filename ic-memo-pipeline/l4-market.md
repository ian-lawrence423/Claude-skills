# Phase 2 — L4 Market Research Agent (IC Memo Mode)

Load immediately:
- `{SKILLS_PATH}/market-research/SKILL.md` → Level 4 section
- `{SKILLS_PATH}/market-research/references/analytical-prompts.md` → Market Sizing & Trends section
- `{SKILLS_PATH}/market-research/references/analytical-prompts.md` → Financial & Unit Economics section (market economics questions)
- `{SKILLS_PATH}/mckinsey-consultant/SKILL.md`
- `{SKILLS_PATH}/tam-sam-som-calculator/SKILL.md` → use for bottom-up TAM/SAM build
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

---

### TAM / SAM sizing

Use tam-sam-som-calculator SKILL.md to structure the bottom-up build. Both methods required.

**Top-down:** Start from analyst TAM (Gartner / IDC / Forrester / government data).
State the analyst source, base year, and methodology. Segment to SAM using stated criteria
(geography, customer type, product scope).

**Bottom-up:** Apply the three-step build from analytical-prompts.md:
1. How many potential buyers exist in the target segment? Name the source.
2. What is the ACV or AUV? State whether observed or inferred.
3. Potential buyers × ACV = bottom-up SAM. Compare to top-down.

**If divergence exceeds 25%:** reconcile explicitly — name the assumption that drives the gap.

---

### Growth rate

CAGR must include: rate + source + base year + forecast year + stated methodology.
A growth figure without these fails the depth standard.

Also required: what macro conditions would cause growth to come in **below** the stated
rate? This counterpoint is mandatory — do not omit.

---

### Structural trends

For each trend (2–3 minimum), answer all four questions before including it:
1. What specific evidence establishes this as a real trend vs. a narrative?
2. What is the mechanism — why is this trend occurring?
3. Timing: near-term (0–1yr), mid-term (1–3yr), or long-term (3–5yr)?
4. What does this trend mean specifically for the investment thesis? Generic "so whats" fail.

Run a PESTLE overlay on the structural trend set — assess each force for relevance:
- **Political / regulatory:** policy changes, compliance requirements, enforcement trends
- **Economic:** macro conditions affecting buyer budgets, pricing power, cost structures
- **Social / demographic:** behavioral shifts, generational patterns
- **Technological:** infrastructure changes, platform shifts, AI/automation impact
- **Legal:** IP, liability, data privacy, sector-specific regulation
- **Environmental:** supply chain exposure, ESG-driven purchasing behavior

Not every PESTLE force will be material — state which are active and which are not.

---

### Market economics

From analytical-prompts.md (Financial & Unit Economics → Market Economics):
- Where is value captured in this market — platform layer, data layer, service layer?
- Where do incumbents make money vs. where do they subsidize?
- What does the margin structure imply about competitive sustainability?

---

**Source standard:**
- Tier 1: public filings (10-K, S-1), government data, Gartner/IDC/Forrester
- Tier 2: industry associations, academic research
- Every quantitative claim: 2+ independent sources minimum

Apply inline citation format to every claim: `[Source, Year] [H/M/L]`

Flag data gaps immediately:
```
DATA GAP: [Claim] — [reason: one source / conflict / unverifiable]
Warrants: [specific action] before treating as confirmed.
```

---

## Required Output — write to `{WORK_DIR}/research/l4-market.md`

```markdown
# L4 — Market & Segment Analysis
## [COMPANY] — IC Memo Mode

## TAM / SAM
**Top-down:** [figure, source, methodology, base year]
**Bottom-up:** [buyers × ACV = figure, methodology stated]
**Reconciliation:** [if >25% divergence, reconcile explicitly]

## CAGR
[Rate] — Source: [name], base year: [year], forecast year: [year], methodology: [stated]
**Growth headwinds:** [macro conditions that would cause underperformance vs. stated rate]

## Segment map
| Segment | Size | Growth | Best unit economics? | Relevance to thesis |
|---------|------|--------|----------------------|---------------------|

## Structural trends
1. [Trend] — Evidence: [specific] | Mechanism: [why] | Timing: [horizon] | Thesis implication: [specific]
2. [same]
3. [same]

## PESTLE overlay
| Force | Active? | Specific finding |
|-------|---------|-----------------|
| Political/regulatory | | |
| Economic | | |
| Social/demographic | | |
| Technological | | |
| Legal | | |
| Environmental | | |

## Market economics
**Value capture layer:** [where in the stack do margins accrue]
**Margin structure implication:** [what this means for competitive sustainability]

## DATA GAPS
[List any flagged gaps]
```

Append all sources to: `{WORK_DIR}/source-bibliography.md`
Append all DATA GAP flags to: `{WORK_DIR}/data-gaps.md`
