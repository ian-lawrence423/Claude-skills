---
name: competitive-landscape-deliverable
description: Triggers when converting a competitive landscape, market mapping, or M&A target spreadsheet into a board-ready executive deliverable. Preserves the raw research sheet and adds a second sheet that compresses each cell while preserving the full rating + key evidence — fidelity over brevity. Verdict-led layout, Pattern brand styling, and consulting-grade formatting. Mines the rating-and-rationale source format produced by the Pattern competitive landscape pipeline.
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

## Phrase rules — fidelity over brevity

The deliverable must be **as concise as possible without losing or transforming meaning**. Compression is achieved by removing filler and transitional language, NOT by truncating substantive content.

### Core principle: preserve the rating, compress the rationale

Source cells follow `"Rating — McKinsey rationale"`. Both halves carry meaning:
- **The rating IS the answer** for many fields (e.g., `Yes`, `Tier B`, `Strong`, `Critical`, `4`). Never drop it.
- **The rationale provides the evidence** that makes the rating credible. Compress, but don't truncate mid-clause.

### Output format by field type

| Source pattern | Output format | Example |
|---|---|---|
| Both rating and rationale | `Rating — compressed rationale` | `Yes — embedded across OMS, helpdesk, customer notifications` |
| Rating only (no rationale) | `Rating` (verbatim) | `Tier B` |
| Numeric score + rationale | `N — qualifier` | `4 — captures returns data across 1,200+ carriers` |
| Rationale only (no rating) | Compressed rationale | `Recently acquired by Blue Yonder August 2025` |
| List values (Notable Customers, etc.) | First 5 items + `(+N more)` | `Sephora, Levi's, Patagonia, Adidas, Lululemon (+12 more)` |
| Empty source | `—` (em-dash) | `—` |

### Compression rules

Apply in this order:

1. **Strip citations** (`<cite index="...">` tags from agent output)
2. **Remove transitional filler** (`for example`, `notably`, `in particular`, `as evidenced by`, `the company`, `which is`, etc.)
3. **Remove banned hype** (`leading`, `robust`, `innovative`, `comprehensive`, `cutting-edge`, `best-in-class`) UNLESS the rating itself contains it (then preserve)
4. **Collapse whitespace**, strip trailing punctuation
5. **If still over budget**: break at clause boundary (comma, semicolon) — never mid-sentence

### Length targets (NOT hard caps)

- **Combined cell** (rating + rationale): 12–18 words typical, up to 22 acceptable
- **Rating-only cells**: as long as the rating itself
- **Free-text pass-through fields**: up to 22 words
- **Hard ceiling for QC warning**: 26 words (above this, the script flags for review)

These are fidelity ceilings, not aspirational caps. Going under doesn't earn points if it sacrifices meaning.

### Good vs bad transformations

✅ **Good** (rating preserved, evidence compressed):
```
Source: "Partial — owns return and exchange records but synchronizes core order data from Shopify or OMS upstream"
Output: "Partial — owns return/exchange records, syncs orders from Shopify or OMS"
```

✅ **Good** (rating + rich rationale):
```
Source: "Strong — implementation complexity creates ~12-month migration cost; deeply embedded in helpdesk, OMS, and customer notification workflows"
Output: "Strong — embedded in helpdesk, OMS, customer notifications; ~12mo migration"
```

❌ **Bad** (drops the rating, loses verdict):
```
Source: "Yes — embedded across OMS, helpdesk, and customer notification workflows"
Output: "embedded across OMS, helpdesk, and notifications"        # missing "Yes"
```

❌ **Bad** (truncates mid-clause, loses meaning):
```
Source: "Tier B — captures order, return, and shipment data but excludes payment card data and PII routed to Stripe"
Output: "captures order, return, and shipment data but excludes"   # mid-clause cut
```

❌ **Bad** (over-compresses to the point of distortion):
```
Source: "Pass — Blue Yonder's August 2025 acquisition eliminates buy option while returns management represents non-core capability"
Output: "Off the table"                                            # loses the WHY
```

### Free-text fields — pass through, don't synthesize

For fields where the source is already a list or descriptive text rather than a rated assessment, use lighter cleanup:
- Notable Customers / Key Investors / Direct Competitors / Comparable Transactions: trim to 5 items, add `(+N more)` if more
- Funding Raised: pass through (`$208M Series D`)
- Target Contact / Owners: pass through verbatim

The engine script handles this via `is_passthrough_field()` and `trim_list()`.

### Empty / low-confidence handling

- Truly empty source → `—`
- Source has rating like `Unknown` or `Unclear` → keep verbatim, don't substitute
- If the rationale starts with `Likely`, `Reported`, `Validate`, preserve that qualifier — it's the epistemic signal the executive needs

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
