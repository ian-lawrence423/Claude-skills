---
name: pattern-docx
description: >-
  Generate Pattern-branded Word documents using the canonical template shell, exact
  typography, colors, tables, headers, footers, and QA workflow.
intent: >-
  Generate professional, on-brand Word documents (.docx) for Pattern. Use this skill
  whenever Ian asks to create a memo, report, analysis, due diligence document, or any
  professional Word document for Pattern. This skill encodes Pattern's exact typography
  (Wix Madefor Display), brand colors, header/footer with logo, section structure, table
  styles, and paragraph formatting — all extracted directly from Pattern's canonical Word
  template. Always use this skill instead of the generic docx skill when working on
  Pattern materials.
type: workflow
---

# Pattern Word Document Generator

You are generating a professional, on-brand Word document for Pattern. Every paragraph, table,
and header/footer must exactly match Pattern's canonical template. Read this entire file before
writing any code.

---

## Example And Anti-Pattern

Example prompt:
> "Turn this approved IC memo draft into a Pattern DOCX using the canonical template shell."

Expected use:
- Start from the base DOCX skill and the canonical Pattern template workflow.
- Preserve header/footer assets, section properties, typography, tables, and brand colors.
- Run render/structural QA and then `doc-quality-checker` after production.

Anti-pattern:
- Do not build a Pattern document from scratch with generic DOCX defaults or skip template transplant verification.

---
## Step 1: Read the Base DOCX Skill First

Before writing any code, read the base docx skill for API usage, pitfalls, and XML repair patterns:

```
Read: /mnt/skills/public/docx/SKILL.md
```

---

## Step 1A: Check for Canonical Template Before Generating

Before building a fresh docx from brand constants, check whether a prior Pattern document
for this deal (or a comparable canonical template) already exists. Pattern documents
often contain richer template assets than the skill's stock `{SKILL_DIR}/assets/` folder
provides — specifically:

- 6 header/footer files (header1/2/3, footer1/2/3) supporting first/even/default
  page behavior where the cover can use a different header/footer than body pages
- Multiple media assets (logo image, icon mark, gradient rule SVG) that render
  differently in header vs. footer contexts
- Specific page margins (typically 720 DXA all sides, 1080 DXA top) matching
  Pattern's canonical look

**When to transplant from a canonical template instead of stock assets:**

1. **Deal iteration** — Prior version (v1, v2, ..., vN) of the same memo exists.
   Always transplant from the most recent version rather than rebuilding. The
   template is deal-specific at that point.

2. **Same-sector canonical exists** — Another deal in the same sector has produced
   a memo with the full 6-file template structure. Transplant if the sector/deal-
   type alignment is close (e.g., another public equity long memo).

3. **Ian provides a reference document** — When Ian uploads or points to a specific
   Pattern document and says "use this template," transplant even if the provided
   document has different body content. The request is explicitly for the template
   shell.

**When to use stock assets (`{SKILL_DIR}/assets/`):**

1. The canonical template path is unavailable
2. Ian has not provided another Pattern reference document
3. The task explicitly allows a stock Pattern shell

**Transplant procedure:**

Start by unpacking the canonical template shell:

```bash
# 1. Unpack canonical template
py "{SKILL_DIR}/scripts/office/unpack.py" "/path/to/canonical_template.docx" "/tmp/pattern_unpack"

# 2. Inventory assets
ls word/                  # Should show header1/2/3.xml, footer1/2/3.xml, media/
ls word/media/            # Should show image1 (logo), image2 (icon), image3 (gradient SVG)
ls word/_rels/            # header*.xml.rels and footer*.xml.rels define image anchors

# 3. Inspect sectPr to capture page setup
python3 -c "
with open('word/document.xml') as f: c = f.read()
import re
m = re.search(r'<w:sectPr[^>]*>.*?</w:sectPr>', c, re.DOTALL)
print(m.group() if m else 'NOT FOUND')
"
```

Then replace the body content inside the unpacked template:

1. Build the new body XML according to the paragraph and table specs below.
2. Replace the existing body children in `word/document.xml`.
3. Preserve the canonical `<w:sectPr>` exactly, including 6 header/footer references,
   any title-page behavior, canonical margins, header distance, and footer distance.
4. Update only the document title text in the canonical header XML.
5. Repack the existing shell with `py "{SKILL_DIR}/scripts/office/pack.py" ... --validate false`.

**CRITICAL — first-page behavior:** The canonical template may express first-page behavior
through first/even/default header and footer references, with or without an explicit
`<w:titlePg/>` element. Preserve the canonical `<w:sectPr>` exactly instead of trying to
recreate this logic. Otherwise the cover page can inherit the body header/footer or lose
the Pattern shell.

**Semantic color verification after transplant:** Canonical templates use Pattern's
full brand palette, not just H1/H2 colors:
- `#4280F4` — H1 section titles (bright blue)
- `#3A00FD` — H2 subsection titles (indigo)
- `#0F4761` — Table header fill (dark teal) + accent text
- `#F5F8FF` — Alternating table row fill
- `#D9E2F3` — Highlighted/totals row fill
- `#C00000` — Red callouts (negative values, GAP, FAILED, CRITICAL)
- `#C55A11` — Orange callouts (CONDITIONAL, WATCH, STRUCTURAL, OPEN)
- `#375623` — Green status callouts (CONFIRMED, STABLE, positive values)
- `#E2EFDA` / `#1A5C1A` — ACQUIRE verdict fill/text
- `#FFE0E0` / `#8B1A1A` — PASS verdict fill/text
- `#444444` — Dark grey body/metadata text
- `#666666` — Mid grey captions/secondary text

A common failure mode: docx-js body generation uses a default color scheme (e.g.,
`#D5E8F0` light-blue table fills, `#F5F9FC` alt rows) that does not match Pattern's
canonical palette. After transplant, scan the body for off-palette colors and correct
them. The semantic callout colors (red/orange/green) must be applied based on text
content — the Post-transplant Color Correction section below documents the pattern-matching
rules.

### Post-transplant Color Correction

After Phase 2 transplant, apply these body-color corrections:

```python
# H1 headings: swap to brand blue
# Find all paragraphs with pStyle="Heading1" and update color to #4280F4

# Table header rows: dark teal fill with white text
# Swap fill #D5E8F0 -> #0F4761; swap text color #0F4761 -> #FFFFFF within those rows

# Alternating row shading: Pattern light blue
# Swap fill #F5F9FC or #F2F2F2 -> #F5F8FF

# Semantic callouts: pattern-match text content to assign color
# CONFIRMED/STABLE/positive values -> #375623 (green)
# CONDITIONAL/WATCH/STRUCTURAL/OPEN -> #C55A11 (orange)
# GAP/FAILED/CRITICAL -> #C00000 (red)
```

These rules are deterministic and run programmatically — they do not require human
inspection of each cell.

---

## Step 2: Canonical Template XML Workflow

Pattern's header contains a **gradient line shape** and an **anchored logo image** that cannot
be produced by docx-js. The default workflow is the canonical-template XML workflow:

**Canonical source**

Use this template when available:

```text
C:\Users\IanLawrence\OneDrive - Pattern\Ian Productivity\Claude\artifacts\research\agentic-commerce-pattern\Commerce_Market_Research_v9_2026-04-29.docx
```

**Phase 1 - Unpack the canonical shell**

```powershell
py "{SKILL_DIR}/scripts/office/unpack.py" "<canonical-template.docx>" "<working-unpack-dir>"
```

Preserve the unpacked header, footer, relationships, media, styles, settings, numbering,
theme, and `[Content_Types].xml` files. These are part of the Pattern template system.

**Phase 2 - Replace the body XML only**

1. Generate new `word/document.xml` body content using the XML specs below.
2. Replace only the document body content.
3. Preserve the canonical `<w:sectPr>` from the template.
4. Update only the header title text in the canonical header XML.
5. Leave all other header/footer XML, rels, media, styles, settings, and theme files untouched.

**Phase 3 - Repack**

```powershell
py "{SKILL_DIR}/scripts/office/pack.py" "<working-unpack-dir>" "<final.docx>" --validate false
```

Use docx-js body generation only as a fallback when no canonical template is available. If
using that fallback, the XML patch step is mandatory because docx-js cannot reproduce the
Pattern header/footer shell.

**Critical:** Never overwrite canonical header/footer/media/theme files when the canonical
template exists. The only safe edits to the template shell are replacing body content and
updating the header title text.

---

## Step 3: Read DOCX Production Reference Before Generating

Read the implementation reference before writing code:

```
Read: {SKILL_DIR}/references/production-spec.md
```

This reference owns the detailed Pattern DOCX production specs:
- Brand constants and semantic colors
- Paragraph types and numbering configuration
- Table styles and exact DXA widths
- Fallback-only Python patch workflow
- Section layout patterns and cover-page XML examples

Use the reference as the implementation source of truth. Keep this file focused on routing,
template choice, critical rules, and QA gates.

---

## Step 4: Critical Rules

1. **Never use Arial** — all text must use Wix Madefor Display or Wix Madefor Display SemiBold
2. **Use bold only where the template requires `<w:b/>`** — H1 section labels and Body Bold Lead use `font: 'Wix Madefor Display'` plus bold; H2, header title, footer page numbers, notes, table headers, and callouts use `font: 'Wix Madefor Display SemiBold'` without an extra bold flag.
3. **Content width = 10800 DXA** — all tables must use this width; columnWidths must sum to 10800
4. **ShadingType.CLEAR** — always use CLEAR, never SOLID (SOLID turns backgrounds black)
5. **Never use unicode bullets directly** — always use `numbering` config with `LevelFormat.BULLET`
6. **Canonical template first** — unpack the canonical Pattern .docx, replace body XML, preserve canonical sectPr, and repack
7. **Header/footer XML is template-owned** — update the header title text only; do not rewrite logos, gradient rules, rels, media, theme, styles, or footer XML
8. **docx-js is fallback only** — if no canonical template is available, generate body content with docx-js and then run the XML patch workflow
9. **Content_Types.xml Override entries are mandatory in fallback mode** — missing them = invisible header/footer
10. **Footer tab stop** — use `<w:tab w:val="right" w:pos="10800"/>` in pPr tabs + `<w:tab/>` run element; do NOT use `<w:ptab>` (unreliable across renderers)
11. **Page margins are 0.5 inch (720 DXA)** — not the docx-js default of 1 inch
12. **characterSpacing: 40** on H1 text runs — this is the slight tracking on section headers

---

## Step 5: Full Working Example

See the Sea Limited PE Strategy Analysis document as the canonical reference implementation.
It demonstrates all paragraph types, all table variants, multi-section layout, and the complete
canonical-template XML workflow, with the fallback patch workflow used only when a template is
unavailable.
