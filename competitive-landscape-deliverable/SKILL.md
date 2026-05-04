---
name: competitive-landscape-deliverable
description: Triggers when converting a competitive landscape, market mapping, or M&A target spreadsheet into a board-ready executive deliverable. Preserves the raw research sheet and adds a second sheet using 7–10-word phrases, verdict-led layout, Pattern brand styling, and consulting-grade formatting. Mines the rating-and-rationale source format produced by the Pattern competitive landscape pipeline and emits crisp executive language.
---

# Competitive Landscape Deliverable

## Core outcome

Transform a detailed competitive landscape workbook into a board/executive-ready deliverable while preserving the raw research. Add or replace a second sheet (`Executive Deliverable`) that:

1. Leads with the verdict (ACQUIRE / MONITOR / PASS) per company
2. Compresses ~100 raw fields into 7–10-word executive phrases
3. Re-sorts companies by deal priority (configurable)
4. Renders with Pattern brand styling (Wix Madefor Display, Pattern blues)

Default workflow:

```
Source workbook (.xlsx or Google Sheets URL)
   → scripts/pull_from_sheets.py  (if URL)
   → scripts/build_deliverable.py
   → Same workbook with new "Executive Deliverable" sheet added
```

## When to invoke

Trigger this skill when the user asks to:
- "Convert / summarize / clean up the competitive landscape sheet"
- "Make an executive view / board view / deliverable from the competitor research"
- "Add a one-pager / summary tab to the competitive landscape"
- "Make a McKinsey-style deliverable from the M&A target grid"

## Source format

The Pattern competitive landscape template produced by the n8n orchestrator (`L8mR6NM9u6VoVdrJ`) has:
- Sheet name: `Competitive Landscape`
- Row 1: title `Competitive Landscape Mapping`
- Row 4: company headers (column C onward, alphabetical or insertion order)
- Column A: section labels (`1. Entity identity`, `2. Market taxonomy`, etc.)
- Column B: field names (`Company Name`, `Legal Entity Name`, ...)
- Rows 5–155: research data, organized into 9 sections
- **Cell format**: `"Rating value — McKinsey-style rationale"` (em-dash separator)

See `references/template-fields.md` for the complete field map.

**Robust detection rule:** never hardcode rows. Scan column B for known field names (e.g., `Company Name`, `Total Moat Score`) and anchor relative positions from there. The engine script does this automatically.

## Use the engine script

The mechanical work — read source, build sheet, apply formatting — happens in `scripts/build_deliverable.py`. Do **not** generate XLSX/XML by hand. Invocation:

```bash
py scripts/build_deliverable.py \
  --source "<path-to-source.xlsx>" \
  --output "<path-or-blank-for-in-place>" \
  [--sort-by priority|fit|moat|source]
```

The script:
1. Loads the source workbook with openpyxl, preserving the original sheet
2. Detects header row, section column, field column dynamically
3. Reads each cell as `(rating, rationale)` by splitting on em-dash
4. For each output row, runs the synthesis mapping (see below) and writes a 7–10-word phrase derived from the rating + rationale
5. Builds the `Executive Deliverable` sheet with verdict block + 8 grouped sections
6. Applies Pattern brand styling
7. Saves in place (or to `--output`)

If the synthesis logic needs new mappings or richer phrasing, edit `build_deliverable.py` rather than re-implementing the logic per invocation.

## Google Sheets ingestion

For a Google Sheets URL, run:

```bash
py scripts/pull_from_sheets.py --url <sheets-url> --out <local.xlsx>
```

This uses the Google Sheets v4 API (set `GOOGLE_SHEETS_TOKEN` env var to an OAuth access token, or it falls back to gcloud-application-default-credentials). Output is a local `.xlsx` snapshot ready for `build_deliverable.py`.

The Pattern Competitive Landscape sheet ID is `159cKsL9YEWmIoo0BTt6NelobAmAm6qan-VyOagUJuJ4`.

## Executive Deliverable layout

### Title block (rows 1–2)
- Row 1: `Competitive Landscape — Executive View` (24pt, white, on `#0F4761` band)
- Row 2: `Concise strategic readout from detailed research` (10pt, `#4280F4`)

### Verdict block (rows 3–6)
| Row | Label (col B) | Cell content |
|---|---|---|
| 3 | Verdict | `ACQUIRE` / `MONITOR` / `PASS` — green/amber/grey conditional fill |
| 4 | Recommended posture | 7–10-word phrase from posture vocabulary |
| 5 | Score triplet | `moat / fit / ma` (e.g., `16 / 8.2 / 6.8`) |
| 6 | Acquisition thesis | 10–14-word one-liner |

Freeze panes at `C7` (below verdict block, after both label columns).

### Section blocks (row 7 onward)
Eight sections, each preceded by a styled section header row:

1. **Market taxonomy** (~11 rows)
2. **Product capability** (~17 rows)
3. **Data and compliance** (~10 rows)
4. **Commercial traction** (~16 rows)
5. **Competitive position** (~16 rows)
6. **Pattern fit** (~12 rows)
7. **M&A lens** (~14 rows)
8. **Pipeline operations** (~12 rows)

Total ~108 rows + 6-row header = ~114-row deliverable.

See `references/output-row-spec.md` for the exact label list and source-field mapping.

## Phrase rules

Every company-facing cell must be a 7–10-word phrase, not a paragraph.

Rules:
- 7–10 words target; never exceed 12 unless cell explicitly requires nuance
- No trailing periods
- Sentence case (proper nouns Title Case)
- Active, precise; strategic implication > generic description
- Banned filler: `leading`, `robust`, `innovative`, `comprehensive`, `cutting-edge`, `best-in-class` (unless backed by specific evidence)
- Uncertainty qualifiers: `Likely`, `Reported`, `Unclear`, `Validate`, `Requires confirmation`
- Empty source → `—` (em-dash, NOT empty string)
- Low-confidence source → prefix `Validate:` or suffix `(unconfirmed)`

Good:
- `Returns orchestration for enterprise merchants`
- `Post-purchase system of record across 1,200+ carriers`
- `High switching cost from OMS workflow embedding`
- `Likely partner before acquisition target`

Bad:
- `This company provides a comprehensive returns platform.` (full sentence + filler)
- `AI` (too sparse)
- `High` (no content)

### Mining the rationale

Source cells follow `"Rating — McKinsey rationale"`. The rationale is the goldmine. Example:

```
Source cell:  "Yes — embedded across OMS, helpdesk, and customer notification workflows"
Output cell:  "Embedded across OMS, helpdesk, and notifications"
```

The engine script does this transform automatically; do not re-derive phrases that the rationale already supplies.

## Field synthesis rules

The 100+ output rows are derived from raw fields per the mapping in `references/output-row-spec.md`. Defaults:

- Combine 2–3 raw fields into one executive label
- If primary source is empty, fall back to listed adjacents
- For numeric scores (1–5 or 1–10), pass the number through; for categorical, mine the rationale

The full mapping lives in the reference file and is implemented in `build_deliverable.py:SYNTHESIS_MAP`.

## Sort and prioritization

By default: re-sort companies by **deal priority**:
1. ACQUIRE candidates (by descending strategic fit score)
2. MONITOR candidates (by descending moat score)
3. PASS candidates (by source order)

CLI flags:
- `--sort-by priority` (default)
- `--sort-by fit` — descending strategic fit score
- `--sort-by moat` — descending total moat score
- `--sort-by source` — preserve raw sheet order

## Posture vocabulary

When generating the row 4 "Recommended posture" cell:

| Pattern in source | Posture phrase |
|---|---|
| High fit + high priority + low complexity | `Pursue active diligence this quarter` |
| High fit + high complexity | `Partner first, revisit acquisition next year` |
| High moat + low Pattern fit | `Useful benchmark, weak Pattern fit` |
| Recently acquired | `Off-market, monitor competitive impact` |
| Low confidence | `Validate thesis before leadership outreach` |
| Strong moat + early stage | `Track for inflection, no near-term action` |

## Pattern brand styling

All formatting uses the Pattern visual system (matches Word doc standard):

| Element | Font | Size | Color | Fill |
|---|---|---|---|---|
| Title row 1 | Wix Madefor Display SemiBold | 24pt | `#FFFFFF` | `#0F4761` |
| Subtitle row 2 | Wix Madefor Display | 10pt | `#4280F4` | none |
| Verdict ACQUIRE | Wix Madefor Display SemiBold | 11pt | `#1A5C1A` | `#E2EFDA` |
| Verdict MONITOR | Wix Madefor Display SemiBold | 11pt | `#7A5C00` | `#FFF3CD` |
| Verdict PASS | Wix Madefor Display SemiBold | 11pt | `#8B1A1A` | `#FFE0E0` |
| Section header | Wix Madefor Display SemiBold | 11pt | `#0F4761` | `#F5F8FF` |
| Field label (col B) | Wix Madefor Display | 9pt | `#000000` | none |
| Body cell | Wix Madefor Display | 9pt | `#000000` | alt rows `#F5F8FF` |
| Borders | thin | — | `#DDDDDD` | — |

Cell formatting:
- Wrap text everywhere
- Top-aligned
- Column A (section): 18 width, bold
- Column B (label): 26 width, bold
- Company columns: 32 width, wrap
- Row height: 22 default, 36 for verdict block, 14 for section headers

## Quality checks

Before returning the workbook, the engine script asserts:
1. Source sheet `Competitive Landscape` (or detected source) exists and is byte-identical to input
2. `Executive Deliverable` sheet exists with ≥80 rows and N+2 columns (where N = company count)
3. Company headers in deliverable match source order or sort criterion
4. Random-sample 12 cells: each is ≤12 words and contains no banned filler
5. Verdict cells contain only `ACQUIRE`, `MONITOR`, `PASS`, or `—`
6. Output saved as `.xlsx` (not `.xlsm` or `.xltx`)

If any check fails, the script raises and prints the specific failure.

## Folder layout

```
competitive-landscape-deliverable/
├── SKILL.md                     (this file)
├── references/
│   ├── template-fields.md       (full Pattern field map)
│   └── output-row-spec.md       (executive deliverable row spec)
├── scripts/
│   ├── build_deliverable.py     (engine — openpyxl)
│   └── pull_from_sheets.py      (Google Sheets ingestion)
└── assets/
    └── (sample output.xlsx if available)
```
