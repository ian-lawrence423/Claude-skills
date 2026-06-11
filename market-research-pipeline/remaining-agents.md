# Draft — Exec Summary Agent

Load: `{SKILLS_PATH}/executive-summary-writer/SKILL.md`
Also load: `{SKILLS_PATH}/mckinsey-consultant/SKILL.md` -> Pyramid Principle + SCR Narrative

## Your Inputs
All section files + context-and-market-sizing.md + themes.md + competitor files.
Read everything before writing a single word.

## Constraint
Two-page six-section executive summary. Use the canonical spine:
Company Overview, Product Offering, Market Dynamic, Business Model,
Thesis: What You Need To Believe, Open Questions.

Do not write a topic preview. The summary must stand alone as the shortest
decision-grade version of the full report.

## Output — write to `{WORK_DIR}/draft/exec-summary.md`

The summary must:
- Explain the market/company/category orientation first
- Describe the product/workflow offering when a target company or archetype exists
- State the market dynamic and business model implication
- Convert the governing synthesis into 3-5 testable beliefs
- End with decision-changing open questions
- Retain only the most important evidence; do not duplicate body sections
- Not use the word "this report" or any variant

---

# Pass 1 — Writing Style Agent

Load: `{SKILLS_PATH}/writing-style/SKILL.md`

## Your Inputs
All draft files (post-draft, pre-scrutinizer).

## Your Job
Run the writing-style self-review pass on every draft file.

Flag and fix:
- Claims missing [F/E/H] tag (tag them)
- Absolute or exclusivity terms without eliminated alternatives
  ("only", "solely", "inevitably", "always", "never")
- Multi-step causal claims without complete inductive chain
- Consulting boilerplate ("leverage", "synergies", "best-in-class")
- Unsupported superlatives
- Prose where the conclusion does not lead

Blocking issue: any thesis-critical claim missing [F/E/H] tag.
Non-blocking: style improvements.

## Output
Write redline to `{WORK_DIR}/iteration/pass1-writing-style.md`
Update draft files in place with hardened prose.

Status line at end: `PASS 1 STATUS: BLOCKING_ISSUES_FOUND | CLEAR_TO_ADVANCE`

---

# Pass 3 — Red Team Agent

Load: `{SKILLS_PATH}/market-research/SKILL.md` → Section: Pass 3

## Your Inputs
All draft files (post-Pass-2) + pass2-claim-scrutinizer.md

## Your Job
Assume the governing thesis is wrong. Work backward.

For each theme (load-bearing pillar):
- State the strongest affirmative counter-claim with substantiation
- Name the attack vector (disconfirming evidence / structural alternative /
  timing risk / assumption failure)
- Rate attack severity: KILL | WOUND | EXPOSE

Produce:
1. **Kill scenarios** — top 3 conditions under which the thesis fails entirely
2. **Bear case** — coherent adversarial argument against the governing conclusion
3. **Unstated assumption attacks** — assumptions never flagged in the draft
4. **Adversarial scorecard**: KILL / WOUND / EXPOSE / SURVIVES counts

Blocking issues before output:
- Any KILL-rated attack with no counter-argument in the draft
- Bear case that directly contradicts governing thesis without acknowledgement

## Output
Write to `{WORK_DIR}/iteration/pass3-red-team.md`
Update draft files to acknowledge KILL attacks and the bear case.
Status line: `PASS 3 STATUS: BLOCKING_ISSUES_FOUND | CLEAR_TO_ADVANCE`

---

# Post-Output Doc Quality Checker Agent

Load: `{SKILLS_PATH}/doc-quality-checker/SKILL.md`

## Your Inputs
Final output file + relevant output skill spec:
- If OUTPUT_FORMAT=docx: `{SKILLS_PATH}/pattern-docx/SKILL.md`
- If OUTPUT_FORMAT=pptx: `{SKILLS_PATH}/pattern-investment-pptx/SKILL.md`

## Your Job
Check brand formatting compliance, structural logic, table rendering, and narrative flow.

Severity ratings:
- **CRITICAL** — blocks output (missing brand elements, broken structure)
- **MAJOR** — degrades quality significantly (inconsistent formatting, orphaned sections)
- **MINOR** — polish items (spacing, capitalisation, number formatting)

Blocking issues: any CRITICAL flag.

Check specifically:
- Every section headline is an insight statement, not a label
- Exec summary states a point of view — not a topic preview
- Titles tell a coherent story in sequence
- No placeholder text, "TBD", or draft artifacts
- Numbers formatted: $2.3B not $2,300M; 34% not 0.34
- Internal consistency: numbers cited in exec summary match section bodies

## Output
Write to `{WORK_DIR}/iteration/post-output-doc-quality.md`
Status line: `PASS 4 STATUS: BLOCKING_ISSUES_FOUND | CLEAR_TO_ADVANCE`

---

# Output — DOCX Agent

Load: `{SKILLS_PATH}/pattern-docx/SKILL.md`
Also load: `{SKILLS_PATH}/public/docx/SKILL.md`

## Your Inputs
All draft files + open-issues.md + source-bibliography.md

## Document Structure (in order)
1. Cover
2. Executive summary (from exec-summary.md)
3. Context and Scope
4. Market Sizing
5. Customer Segmentation and Buying Behavior
6. Competitive Landscape
7. Pricing Models and Unit Economics
8. Technology Trends and Disruption Vectors
9. Regulatory Environment and External Risk
10. Competitive Moat Analysis
11. Strategic Implications and Key Takeaways
12. Appendix: sources + methodology + arithmetic corrections + open issues

If open-issues.md is non-empty, add a clearly labeled "Open items" section
before the appendix. Do not bury or omit open issues.

Write final document to: `{WORK_DIR}/final-output.docx`

---

# Output — PPTX Agent

Load: `{SKILLS_PATH}/pattern-investment-pptx/SKILL.md`
Also load: `{SKILLS_PATH}/public/pptx/SKILL.md`

## Your Inputs
All draft files + themes.md + open-issues.md

## Slide Structure
1. Cover
2. Executive summary (1-2 slides using executive-summary-writer spine)
3. Context and Scope
4. Market Sizing
5. Customer Segmentation and Buying Behavior
6. Competitive Landscape
7. Pricing Models and Unit Economics
8. Technology Trends and Disruption Vectors
9. Regulatory Environment and External Risk
10. Competitive Moat Analysis
11. Strategic Implications and Key Takeaways
12. Appendix: sources + open items

Every slide title must be an insight statement. No label titles.
Apply all pattern-investment-pptx brand rules (Wix Madefor Display, no-bold rule, etc.)

Write final deck to: `{WORK_DIR}/final-output.pptx`
