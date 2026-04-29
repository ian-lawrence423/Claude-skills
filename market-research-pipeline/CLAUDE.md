# Market Research Pipeline — Claude Code Entry Point

This is a multi-agent market research pipeline. Drop this directory into your
Claude Code workspace. Run via the command below.

---

## Usage

```bash
claude "Run the market research pipeline.

COMPANY: [company or market name]
QUESTION: [your specific research question tied to a decision]
OUTPUT_FORMAT: docx   # or pptx
SKILLS_PATH: /path/to/your/skills/user
WORK_DIR: /path/to/output/directory/for/this/run
"
```

**Example:**
```bash
claude "Run the market research pipeline.

COMPANY: Narvar
QUESTION: Is the post-purchase infrastructure market structurally attractive enough to justify a $150M acquisition at 4x ARR?
OUTPUT_FORMAT: docx
SKILLS_PATH: /Users/ian/skills/user
WORK_DIR: /Users/ian/research-runs/narvar-2025-04
"
```

---

## What This Does

Runs a six-phase market research pipeline:

| Phase | What happens |
|-------|-------------|
| P1 — Brief | Sharpens your question, builds MECE hypothesis tree |
| P2 — Research | Sequential L4→L3→L2→L1 pyramid research with web search |
| P3 — Themes | Synthesizes 4–6 structural themes from all evidence |
| P4 — Draft | Market context → theme sections + competitor profiles → exec summary |
| P5 — Iteration | 4 sequential QA passes: writing style → claim scrutinizer → red team → doc quality |
| P6 — Output | Pattern-branded DOCX or PPTX |

Expected runtime: 25–45 minutes depending on market complexity and number of competitors.

---

## Directory Structure

```
market-research-pipeline/
├── CLAUDE.md                   ← you are here (Claude Code reads this first)
├── orchestrator.md             ← main agent — reads this to run the pipeline
└── prompts/
    ├── brief.md
    ├── l4-market.md
    ├── l3-customer.md
    ├── l2-competitive.md
    ├── l1-company.md
    ├── theme-synthesis.md
    ├── draft-context.md
    ├── draft-section.md
    ├── draft-competitor.md
    ├── draft-exec.md
    ├── pass1-writing-style.md
    ├── pass2-claim-scrutinizer.md
    ├── pass3-red-team.md
    ├── pass4-doc-quality.md
    ├── output-docx.md          ← split from remaining-agents.md before use
    └── output-pptx.md          ← split from remaining-agents.md before use
```

**Note:** `remaining-agents.md` contains the prompts for draft-exec, all four
iteration passes, and both output agents in a single file for convenience.
Before first run, split each `---` section into its own file with the filename
matching the header (e.g. `pass1-writing-style.md`, `output-docx.md`, etc.)
OR reference the combined file from orchestrator.md and parse by header.

---

## Skills Required

The pipeline reads these skill files at runtime. Confirm they exist at your
SKILLS_PATH before running:

```
user/mckinsey-consultant/SKILL.md
user/market-research/SKILL.md
user/writing-style/SKILL.md
user/claim-scrutinizer/SKILL.md
user/doc-quality-checker/SKILL.md
user/pattern-docx/SKILL.md
user/pattern-investment-pptx/SKILL.md
public/docx/SKILL.md
public/pptx/SKILL.md
```

---

## Output Files (written to WORK_DIR)

```
brief.md                          Research brief
research/l4-market.md             Market & segment analysis
research/l3-customer.md           Customer insights
research/l2-competitive.md        Competitive landscape
research/l1-company.md            Company position
themes.md                         4–6 structural themes
draft/market-context.md           Draft: market context section
draft/section-[N].md              Draft: one file per theme
draft/competitor-[name].md        Draft: one file per named competitor
draft/exec-summary.md             Draft: executive summary
iteration/pass1-writing-style.md  QA redline: writing style
iteration/pass2-claim-scrutinizer.md  QA redline: claim scrutinizer
iteration/pass3-red-team.md       QA redline: red team
iteration/pass4-doc-quality.md    QA redline: doc quality
source-bibliography.md            All sources with CRAAP scores
data-gaps.md                      All DATA GAP flags across all phases
open-issues.md                    Unresolved issues after iteration loop
run-log.md                        Phase gate log with timestamps
final-output.[docx|pptx]          Final deliverable
```

---

## Gate Summary

| Gate | When | Fails if |
|------|------|---------|
| Gate 1 | After P1 | Brief question not tied to decision, hypothesis tree not MECE |
| Gate 2 | After P3 | Fewer than 4 themes, themes are data points, themes overlap |
| Gate 3 | After P5 | Open KILL claims, open CRITICAL doc issues, unacknowledged thesis-critical gaps |

On gate failure: orchestrator re-runs the responsible agent up to 2 times,
then halts with `GATE_N_FAILED` and writes the blocking issue list to run-log.md.
