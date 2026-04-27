---
name: pattern-docx
description: >
  Generate professional, on-brand Word documents (.docx) for Pattern. Use this skill whenever
  Ian asks to create a memo, report, analysis, due diligence document, or any professional
  Word document for Pattern. This skill encodes Pattern's exact typography (Wix Madefor Display),
  brand colors, header/footer with logo, section structure, table styles, and paragraph
  formatting — all extracted directly from Pattern's canonical Word template. Always use this
  skill instead of the generic docx skill when working on Pattern materials.
---

# Pattern Word Document Generator

You are generating a professional, on-brand Word document for Pattern. Every paragraph, table,
and header/footer must exactly match Pattern's canonical template. Read this entire file before
writing any code.

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

- 6 header/footer files (header1/2/3, footer1/2/3) supporting titlePg behavior where
  the first page (cover) uses a different header/footer than body pages
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

1. First memo in a new deal
2. No canonical reference available
3. Ian has not specified a template source

**Transplant procedure:**

Before Phase 1 (body generation), unpack the canonical template:

```bash
# 1. Unzip canonical template
mkdir -p /tmp/canonical_unpack
cd /tmp/canonical_unpack
unzip -q /path/to/canonical_template.docx

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

After Phase 1 (body generation), apply the transplant in Phase 2:

1. Unzip the body-only docx produced by docx-js
2. Replace single header1.xml / footer1.xml with the canonical set of 6 files
3. Copy canonical media folder (image1, image2, image3)
4. Copy header*.xml.rels and footer*.xml.rels from canonical
5. Replace sectPr in body document.xml with canonical sectPr (6 header/footer references,
   titlePg flag, canonical margins)
6. Update document.xml.rels to reference all 6 header/footer files (rId7-rId12)
7. Add Override entries in [Content_Types].xml for header2/3 and footer2/3

**CRITICAL — titlePg behavior:** The canonical template uses a `<w:titlePg/>` element in
sectPr so that the cover page (first page) uses header3/footer3 (typically empty) while
body pages use header2/footer2 (with logo and icon mark). Without titlePg, the cover
page shows the logo header overlaying the title block — a visible distribution-blocking
defect.

**Semantic color verification after transplant:** Canonical templates use Pattern's
full brand palette, not just H1/H2 colors:
- `#4280F4` — H1 section titles (bright blue)
- `#3A00FD` — H2 subsection titles (indigo)
- `#0F4761` — Table header fill (dark teal) + accent text
- `#C00000` — Red callouts (negative values, GAP, FAILED, CRITICAL)
- `#C55A11` — Orange callouts (CONDITIONAL, WATCH, STRUCTURAL, OPEN)
- `#375623` — Green callouts (PASS, CONFIRMED, STABLE)
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

# Alternating row shading: standard grey
# Swap fill #F5F9FC -> #F2F2F2

# Semantic callouts: pattern-match text content to assign color
# PASS/CONFIRMED/STABLE -> #375623 (green)
# CONDITIONAL/WATCH/STRUCTURAL/OPEN -> #C55A11 (orange)
# GAP/FAILED/CRITICAL -> #C00000 (red)
```

These rules are deterministic and run programmatically — they do not require human
inspection of each cell.

---

## Step 2: Understand the Two-Phase Build Process

Pattern's header contains a **gradient line shape** and an **anchored logo image** that cannot
be produced by docx-js. The correct workflow is always:

**Phase 1 — Generate body with docx-js**
Write all document content (paragraphs, tables, bullets) via docx-js. Do NOT attempt to create
header or footer in docx-js — leave sections with no header/footer.

**Phase 2 — Python XML patch**
After generating the .docx:
1. Unzip the file
2. Copy in the template header1.xml, footer1.xml, their rels, and media assets from `{SKILL_DIR}/assets/`
3. Add header/footer relationship entries to `word/_rels/document.xml.rels`
4. Inject `<w:headerReference>` and `<w:footerReference>` into `<w:sectPr>` in document.xml
5. Add Override entries for header1.xml and footer1.xml to `[Content_Types].xml`
6. Repack

**CRITICAL — Content_Types.xml**: Without Override entries for header1.xml and footer1.xml,
Word silently ignores them even if everything else is wired correctly. This is the #1 cause
of missing headers/footers.

---

## Step 3: Brand Constants

Use these exact values everywhere. Never approximate.

### Colors
```
SECTION_HEADER  = '4280F4'   # H1 text: brand blue
SUBHEADER       = '3A00FD'   # H2 text: deep blue/purple
BODY            = '000000'   # Normal body text
BODY_BOLD_LEAD  = '000000'   # Bold lead paragraph
BODY_SECONDARY  = '444444'   # Secondary/supporting body
BODY_NOTE       = '0F4761'   # Dark navy — callout/important note (SemiBold)
BODY_SUBTLE     = '333333'   # Subtle variation
CAPTION         = '666666'   # Footnotes, captions (sz=16)
RED             = 'C00000'   # Risk items, critical callouts
ORANGE          = 'C55A11'   # Warnings, conditional verdicts
GREEN           = '375623'   # Pass verdicts
TABLE_HEADER    = '0F4761'   # Table header row fill (dark teal/navy)
TABLE_ROW_ALT   = 'F2F2F2'   # Alternating data row fill
TABLE_HIGHLIGHT = 'D9E2F3'   # Highlighted/totals row fill
TABLE_BORDER    = 'DDDDDD'   # Cell borders
SECTION_RULE    = 'BBBBBB'   # H1 bottom rule
FOOTER_BORDER   = 'D9D9D9'   # Footer top rule
WHITE           = 'FFFFFF'
```

### Typography
```
FONT      = 'Wix Madefor Display'          # All body, headings, bullets, tables
FONT_SB   = 'Wix Madefor Display SemiBold' # Subheaders (H2), footer page numbers
```

**No other fonts.** docx-js will fall back to system fonts if Wix Madefor Display is not
installed, but the font name must still be set correctly in the XML — Word/Google Docs will
render it correctly when opened.

### Page Layout
```
Page size:    12240 × 15840 DXA  (US Letter)
Margins:      top=720  right=720  bottom=720  left=720  (all 0.5 inch)
Header dist:  432 DXA
Footer dist:  288 DXA
Content width: 10800 DXA  (= 12240 − 720 − 720)
```

---

## Step 4: Paragraph Type Reference

Every paragraph in a Pattern document maps to one of these types. Use the exact spec.

### H1 — Section Header
```javascript
new Paragraph({
  spacing: { before: 160, after: 100 },
  pageBreakBefore: true,           // Always starts a new page (except first H1)
  border: {
    bottom: { style: BorderStyle.SINGLE, size: 4, color: 'BBBBBB', space: 2 }
  },
  children: [new TextRun({
    text,
    font: 'Wix Madefor Display SemiBold',
    size: 22,                      // 11pt
    color: '4280F4',
    characterSpacing: 40,          // Slight tracking
  })]
})
```
**First H1 only**: set `pageBreakBefore: false` — it sits at the top of page 1.

### H2 — Subheader
```javascript
new Paragraph({
  spacing: { before: 200, after: 80 },
  children: [new TextRun({
    text,
    font: 'Wix Madefor Display SemiBold',
    size: 18,                      // 9pt — same size as body, weight carries it
    color: '3A00FD',
  })]
})
```
**No bold flag** — SemiBold font name carries the weight. Setting `bold: true` double-bolds it.

### H2 Small — Table/subsection label
```javascript
// Same as H2 but tighter spacing — use for labels above tables
spacing: { before: 140, after: 60 }
```

### Body — Normal paragraph
```javascript
new Paragraph({
  spacing: { before: 0, after: 80 },
  children: [new TextRun({
    text,
    font: 'Wix Madefor Display',
    size: 18,
    color: '000000',
  })]
})
```

### Body Bold Lead — Opening paragraph of a section
```javascript
// Same as Body but font: 'Wix Madefor Display SemiBold' — used as the first paragraph after H1
spacing: { before: 0, after: 120 }
font: 'Wix Madefor Display SemiBold'
```

### Body Secondary — Supporting context
```javascript
color: '444444'   // Everything else same as Body
```

### Body Note — Important callout (dark navy, SemiBold)
```javascript
font: 'Wix Madefor Display SemiBold'
color: '0F4761'
after: 80
```

### Caption / Footnote
```javascript
size: 16    // 8pt — smaller than body
color: '666666'
```

### Bullet
```javascript
new Paragraph({
  style: 'ListParagraph',
  numbering: { reference: 'bullets', level: 0 },
  spacing: { before: 0, after: 40 },
  children: [new TextRun({
    text,
    font: 'Wix Madefor Display',
    size: 18,
    color: '000000',
  })]
})
```
Bullet character: `●` (U+25CF filled circle), indent left=720, hanging=360.

### Sub-bullet (level 1)
```javascript
numbering: { reference: 'bullets', level: 1 }
// Character: ○ (U+25CB), indent left=1440, hanging=360
```

### Verdict / Callout box (colored text blocks)
Use standard Body paragraph with font set to SemiBold and color:
- Red callout: `font: 'Wix Madefor Display SemiBold'`, `color: 'C00000'`
- Orange/conditional: `color: 'C55A11'`
- Green/pass: `color: '375623'`

---

## Step 5: Numbering Config

Always include this in the Document constructor:

```javascript
const doc = new Document({
  numbering: {
    config: [
      {
        reference: 'bullets',
        levels: [
          {
            level: 0,
            format: LevelFormat.BULLET,
            text: '\u25CF',         // ● filled circle
            alignment: AlignmentType.LEFT,
            style: {
              paragraph: { indent: { left: 720, hanging: 360 } }
            }
          },
          {
            level: 1,
            format: LevelFormat.BULLET,
            text: '\u25CB',         // ○ open circle
            alignment: AlignmentType.LEFT,
            style: {
              paragraph: { indent: { left: 1440, hanging: 360 } }
            }
          }
        ]
      }
    ]
  },
  styles: {
    default: {
      document: { run: { font: 'Wix Madefor Display', size: 18, color: '000000' } }
    },
    paragraphStyles: [
      {
        id: 'ListParagraph',
        name: 'List Paragraph',
        basedOn: 'Normal',
        quickFormat: true,
        run: { font: 'Wix Madefor Display', size: 18, color: '000000' },
        paragraph: { indent: { left: 720 } }
      }
    ]
  },
  sections: [{ ... }]
});
```

---

## Step 6: Table Style Reference

### Standard data table
```javascript
// Table width = CONTENT_W = 10800 DXA always
// columnWidths must sum to 10800

const CELL_BORDER = { style: BorderStyle.SINGLE, size: 4, color: 'DDDDDD' };
const CELL_BORDERS = { top: CELL_BORDER, bottom: CELL_BORDER, left: CELL_BORDER, right: CELL_BORDER };
const CELL_MARGINS = { top: 80, bottom: 80, left: 120, right: 120 };

new Table({
  width: { size: 10800, type: WidthType.DXA },
  columnWidths: [...],   // must sum to 10800
  rows: [
    // Header row
    new TableRow({ children: headers.map((text, i) =>
      new TableCell({
        borders: CELL_BORDERS,
        width: { size: colWidths[i], type: WidthType.DXA },
        shading: { fill: '0F4761', type: ShadingType.CLEAR, color: 'auto' },
        margins: CELL_MARGINS,
        verticalAlign: VerticalAlign.CENTER,
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({
            text, font: 'Wix Madefor Display SemiBold', size: 18,
            color: 'FFFFFF'
          })]
        })]
      })
    )}),
    // Data rows — alternate FFFFFF / F2F2F2
    ...dataRows.map((row, ri) => new TableRow({ children: row.map((text, ci) =>
      new TableCell({
        borders: CELL_BORDERS,
        width: { size: colWidths[ci], type: WidthType.DXA },
        shading: { fill: ri % 2 === 0 ? 'FFFFFF' : 'F2F2F2', type: ShadingType.CLEAR, color: 'auto' },
        margins: CELL_MARGINS,
        verticalAlign: VerticalAlign.CENTER,
        children: [new Paragraph({
          children: [new TextRun({
            text, font: 'Wix Madefor Display', size: 18, color: '000000'
          })]
        })]
      })
    )}))
  ]
})
```

### Highlighted / totals row
```
shading fill: 'D9E2F3'
font: 'Wix Madefor Display SemiBold'
```

### Risk/condition cell (red text)
```
font: 'Wix Madefor Display SemiBold', color: 'C00000'
```

---

## Step 7: Phase 2 — Python Patch Script

Use this exact script structure. Substitute `{DOC_TITLE}` with the document title for the header.

```python
import zipfile, os, shutil, re

BODY_DOCX  = '/home/claude/output_body.docx'
SKILL_DIR  = '{SKILL_DIR}'                    # absolute path to this skill's directory
OUT        = '/mnt/user-data/outputs/final.docx'

shutil.rmtree('/tmp/pat_patch', ignore_errors=True)
with zipfile.ZipFile(BODY_DOCX, 'r') as z:
    z.extractall('/tmp/pat_patch')

# ── 1. Copy header, footer, media from skill assets ───────────────────────
assets = SKILL_DIR + '/assets'
os.makedirs('/tmp/pat_patch/word/media', exist_ok=True)
os.makedirs('/tmp/pat_patch/word/_rels', exist_ok=True)

shutil.copy2(f'{assets}/pattern_header_logo.png',  '/tmp/pat_patch/word/media/image1.png')
shutil.copy2(f'{assets}/pattern_footer_logo.png',  '/tmp/pat_patch/word/media/image2.png')
shutil.copy2(f'{assets}/pattern_icon_mark.svg',    '/tmp/pat_patch/word/media/image3.svg')

# ── 2. Write header1.xml ──────────────────────────────────────────────────
# Title text appears in the header paragraph
DOC_TITLE = '{DOC_TITLE}'

HEADER_XML = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:hdr xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas"
  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
  xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
  xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"
  xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing"
  xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
  xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
  xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"
  xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml"
  xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape"
  mc:Ignorable="w14 w15 wp14">
<w:p>
  <w:pPr>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold" w:cs="Wix Madefor Display SemiBold"/>
      <w:sz w:val="22"/><w:szCs w:val="22"/>
    </w:rPr>
  </w:pPr>
  <!-- Pattern logo: anchored top-right, behind text -->
  <w:r>
    <w:rPr><w:noProof/>
      <w:rFonts w:ascii="Wix Madefor Display" w:hAnsi="Wix Madefor Display" w:cs="Wix Madefor Display"/>
      <w:color w:val="000000"/><w:sz w:val="24"/><w:szCs w:val="24"/>
    </w:rPr>
    <w:drawing>
      <wp:anchor distT="0" distB="0" distL="114300" distR="114300"
        simplePos="0" relativeHeight="251660288" behindDoc="1"
        locked="0" layoutInCell="1" allowOverlap="1">
        <wp:simplePos x="0" y="0"/>
        <wp:positionH relativeFrom="margin">
          <wp:posOffset>5822995</wp:posOffset>
        </wp:positionH>
        <wp:positionV relativeFrom="paragraph">
          <wp:posOffset>-21191</wp:posOffset>
        </wp:positionV>
        <wp:extent cx="1143000" cy="228600"/>
        <wp:effectExtent l="0" t="0" r="3810" b="3175"/>
        <wp:wrapTight wrapText="bothSides">
          <wp:wrapPolygon edited="0">
            <wp:start x="1204" y="0"/><wp:lineTo x="0" y="7975"/>
            <wp:lineTo x="0" y="17945"/><wp:lineTo x="4416" y="19938"/>
            <wp:lineTo x="6424" y="19938"/><wp:lineTo x="21279" y="17945"/>
            <wp:lineTo x="21279" y="0"/><wp:lineTo x="14052" y="0"/>
            <wp:lineTo x="1204" y="0"/>
          </wp:wrapPolygon>
        </wp:wrapTight>
        <wp:docPr id="887584906" name="Pattern Logo"/>
        <wp:cNvGraphicFramePr>
          <a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/>
        </wp:cNvGraphicFramePr>
        <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
            <pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
              <pic:nvPicPr>
                <pic:cNvPr id="887584906" name="Pattern Logo"/>
                <pic:cNvPicPr/>
              </pic:nvPicPr>
              <pic:blipFill>
                <a:blip r:embed="rId1"/>
                <a:stretch><a:fillRect/></a:stretch>
              </pic:blipFill>
              <pic:spPr>
                <a:xfrm><a:off x="0" y="0"/><a:ext cx="1143000" cy="228600"/></a:xfrm>
                <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
              </pic:spPr>
            </pic:pic>
          </a:graphicData>
        </a:graphic>
      </wp:anchor>
    </w:drawing>
  </w:r>
  <!-- Gradient rule line: full width, behind text -->
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold"/>
      <w:sz w:val="36"/><w:szCs w:val="36"/>
    </w:rPr>
    <mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">
      <mc:Choice Requires="wps">
        <w:drawing>
          <wp:anchor distT="0" distB="0" distL="114300" distR="114300"
            simplePos="0" relativeHeight="251658240" behindDoc="0"
            locked="0" layoutInCell="1" allowOverlap="1">
            <wp:simplePos x="0" y="0"/>
            <wp:positionH relativeFrom="column">
              <wp:posOffset>-896620</wp:posOffset>
            </wp:positionH>
            <wp:positionV relativeFrom="paragraph">
              <wp:posOffset>266065</wp:posOffset>
            </wp:positionV>
            <wp:extent cx="9144000" cy="12065"/>
            <wp:effectExtent l="0" t="0" r="0" b="0"/>
            <wp:wrapNone/>
            <wp:docPr id="4" name="Gradient Line"/>
            <wp:cNvGraphicFramePr/>
            <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
              <a:graphicData uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
                <wps:wsp>
                  <wps:cNvSpPr/>
                  <wps:spPr bwMode="gray">
                    <a:xfrm><a:off x="0" y="0"/><a:ext cx="9144000" cy="12065"/></a:xfrm>
                    <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
                    <a:gradFill>
                      <a:gsLst>
                        <a:gs pos="0"><a:srgbClr val="009BFF"/></a:gs>
                        <a:gs pos="52999"><a:srgbClr val="3C53FF"/></a:gs>
                        <a:gs pos="100000"><a:srgbClr val="FCFCFC"/></a:gs>
                      </a:gsLst>
                      <a:lin ang="0" scaled="0"/>
                    </a:gradFill>
                    <a:ln><a:noFill/></a:ln>
                  </wps:spPr>
                  <wps:bodyPr spcFirstLastPara="1" wrap="square"
                    lIns="91425" tIns="91425" rIns="91425" bIns="91425"
                    anchor="ctr" anchorCtr="0">
                    <a:noAutofit/>
                  </wps:bodyPr>
                </wps:wsp>
              </a:graphicData>
            </a:graphic>
          </wp:anchor>
        </w:drawing>
      </mc:Choice>
    </mc:AlternateContent>
  </w:r>
  <!-- Document title text -->
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold"/>
      <w:color w:val="000000"/>
      <w:sz w:val="22"/><w:szCs w:val="24"/>
    </w:rPr>
    <w:t>{DOC_TITLE}</w:t>
  </w:r>
</w:p>
<w:p>
  <w:pPr>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold" w:cs="Wix Madefor Display SemiBold"/>
      <w:sz w:val="28"/><w:szCs w:val="28"/>
    </w:rPr>
  </w:pPr>
</w:p>
</w:hdr>'''

with open('/tmp/pat_patch/word/header1.xml', 'w', encoding='utf-8') as f:
    f.write(HEADER_XML)

# ── 3. Write footer1.xml ──────────────────────────────────────────────────
# Layout: icon LEFT │ tab-to-right │ page# | Page
# Key: jc=LEFT + explicit tab stop at 10800 DXA + <w:tab/> before page field
# Do NOT use ptab — it behaves inconsistently; use a defined tab stop instead.

FOOTER_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
  xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
  xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
  xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
  xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"
  xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing"
  mc:Ignorable="w14 wp14">
<w:p>
  <w:pPr>
    <w:pBdr>
      <w:top w:val="single" w:sz="4" w:space="1" w:color="D9D9D9"/>
    </w:pBdr>
    <w:tabs>
      <w:tab w:val="right" w:pos="10800"/>
    </w:tabs>
    <!-- jc deliberately omitted = left-aligned -->
  </w:pPr>
  <!-- Icon mark: inline, sits at left -->
  <w:r>
    <w:rPr><w:noProof/></w:rPr>
    <w:drawing>
      <wp:inline distT="0" distB="0" distL="0" distR="0">
        <wp:extent cx="244475" cy="189865"/>
        <wp:effectExtent l="0" t="0" r="3175" b="635"/>
        <wp:docPr id="1" name="Pattern Icon"/>
        <wp:cNvGraphicFramePr>
          <a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/>
        </wp:cNvGraphicFramePr>
        <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
            <pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
              <pic:nvPicPr>
                <pic:cNvPr id="1" name="Pattern Icon"/>
                <pic:cNvPicPr><a:picLocks noChangeAspect="1"/></pic:cNvPicPr>
              </pic:nvPicPr>
              <pic:blipFill>
                <a:blip r:embed="rId1">
                  <a:extLst>
                    <a:ext uri="{96DAC541-7B7A-43D3-8B79-37D633B846F1}">
                      <asvg:svgBlip xmlns:asvg="http://schemas.microsoft.com/office/drawing/2016/SVG/main" r:embed="rId2"/>
                    </a:ext>
                  </a:extLst>
                </a:blip>
                <a:stretch><a:fillRect/></a:stretch>
              </pic:blipFill>
              <pic:spPr>
                <a:xfrm><a:off x="0" y="0"/><a:ext cx="244475" cy="189865"/></a:xfrm>
                <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
              </pic:spPr>
            </pic:pic>
          </a:graphicData>
        </a:graphic>
      </wp:inline>
    </w:drawing>
  </w:r>
  <!-- Tab jumps to right margin (10800 DXA tab stop defined above) -->
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold" w:cs="Wix Madefor Display SemiBold"/>
      <w:sz w:val="16"/><w:szCs w:val="16"/>
    </w:rPr>
    <w:tab/>
  </w:r>
  <!-- Page number field -->
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold" w:cs="Wix Madefor Display SemiBold"/>
      <w:sz w:val="16"/><w:szCs w:val="16"/>
    </w:rPr>
    <w:fldChar w:fldCharType="begin"/>
  </w:r>
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold" w:cs="Wix Madefor Display SemiBold"/>
      <w:sz w:val="16"/><w:szCs w:val="16"/>
    </w:rPr>
    <w:instrText xml:space="preserve"> PAGE   \* MERGEFORMAT </w:instrText>
  </w:r>
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold" w:cs="Wix Madefor Display SemiBold"/>
      <w:sz w:val="16"/><w:szCs w:val="16"/>
    </w:rPr>
    <w:fldChar w:fldCharType="separate"/>
  </w:r>
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold" w:cs="Wix Madefor Display SemiBold"/>
      <w:noProof/><w:sz w:val="16"/><w:szCs w:val="16"/>
    </w:rPr>
    <w:t>1</w:t>
  </w:r>
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold" w:cs="Wix Madefor Display SemiBold"/>
      <w:sz w:val="16"/><w:szCs w:val="16"/>
    </w:rPr>
    <w:fldChar w:fldCharType="end"/>
  </w:r>
  <!-- Separator -->
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold" w:cs="Wix Madefor Display SemiBold"/>
      <w:sz w:val="16"/><w:szCs w:val="16"/>
    </w:rPr>
    <w:t xml:space="preserve"> | </w:t>
  </w:r>
  <w:r>
    <w:rPr>
      <w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold" w:cs="Wix Madefor Display SemiBold"/>
      <w:color w:val="7F7F7F"/>
      <w:spacing w:val="60"/>
      <w:sz w:val="16"/><w:szCs w:val="16"/>
    </w:rPr>
    <w:t>Page</w:t>
  </w:r>
</w:p>
</w:ftr>'''

with open('/tmp/pat_patch/word/footer1.xml', 'w', encoding='utf-8') as f:
    f.write(FOOTER_XML)

# ── 4. Write header rels ──────────────────────────────────────────────────
with open('/tmp/pat_patch/word/_rels/header1.xml.rels', 'w', encoding='utf-8') as f:
    f.write('''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image1.png"/>
</Relationships>''')

# ── 5. Write footer rels ──────────────────────────────────────────────────
with open('/tmp/pat_patch/word/_rels/footer1.xml.rels', 'w', encoding='utf-8') as f:
    f.write('''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image2.png"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image3.svg"/>
</Relationships>''')

# ── 6. Update document.xml.rels ───────────────────────────────────────────
rels_path = '/tmp/pat_patch/word/_rels/document.xml.rels'
with open(rels_path, 'r', encoding='utf-8') as f:
    drels = f.read()

import re
rids = re.findall(r'Id="rId(\d+)"', drels)
max_rid = max(int(r) for r in rids) if rids else 0

additions = []
if 'header' not in drels:
    max_rid += 1
    header_rid = f'rId{max_rid}'
    additions.append(f'<Relationship Id="{header_rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>')
else:
    header_rid = re.search(r'Id="(rId\d+)"[^>]*header', drels).group(1)

if 'footer' not in drels:
    max_rid += 1
    footer_rid = f'rId{max_rid}'
    additions.append(f'<Relationship Id="{footer_rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>')
else:
    footer_rid = re.search(r'Id="(rId\d+)"[^>]*footer', drels).group(1)

if 'theme' not in drels:
    max_rid += 1
    additions.append(f'<Relationship Id="rId{max_rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>')

for a in additions:
    drels = drels.replace('</Relationships>', f'  {a}\n</Relationships>')

with open(rels_path, 'w', encoding='utf-8') as f:
    f.write(drels)

# ── 7. Inject headerReference + footerReference into sectPr ──────────────
doc_path = '/tmp/pat_patch/word/document.xml'
with open(doc_path, 'r', encoding='utf-8') as f:
    doc_xml = f.read()

if 'headerReference' not in doc_xml:
    doc_xml = doc_xml.replace(
        '</w:sectPr>',
        f'  <w:headerReference w:type="default" r:id="{header_rid}"/>\n</w:sectPr>'
    )
if 'footerReference' not in doc_xml:
    doc_xml = doc_xml.replace(
        '</w:sectPr>',
        f'  <w:footerReference w:type="default" r:id="{footer_rid}"/>\n</w:sectPr>'
    )

with open(doc_path, 'w', encoding='utf-8') as f:
    f.write(doc_xml)

# ── 8. Fix Content_Types.xml ─────────────────────────────────────────────
# CRITICAL: without these Override entries Word silently ignores header/footer
ct_path = '/tmp/pat_patch/[Content_Types].xml'
with open(ct_path, 'r', encoding='utf-8') as f:
    ct = f.read()

ct_additions = []
if 'header1.xml' not in ct:
    ct_additions.append('<Override ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml" PartName="/word/header1.xml"/>')
if 'footer1.xml' not in ct:
    ct_additions.append('<Override ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml" PartName="/word/footer1.xml"/>')
if 'theme1.xml' not in ct:
    ct_additions.append('<Override ContentType="application/vnd.openxmlformats-officedocument.theme+xml" PartName="/word/theme/theme1.xml"/>')
if 'svg' not in ct:
    ct_additions.append('<Default ContentType="image/svg+xml" Extension="svg"/>')

for a in ct_additions:
    ct = ct.replace('</Types>', f'  {a}\n</Types>')

with open(ct_path, 'w', encoding='utf-8') as f:
    f.write(ct)

# ── 9. Repack ─────────────────────────────────────────────────────────────
import os
tmp_out = OUT + '.tmp'
with zipfile.ZipFile(tmp_out, 'w', zipfile.ZIP_DEFLATED) as zout:
    for root, dirs, files in os.walk('/tmp/pat_patch'):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, '/tmp/pat_patch')
            zout.write(filepath, arcname)
os.replace(tmp_out, OUT)
print(f'Done: {OUT}  ({os.path.getsize(OUT):,} bytes)')
```

---

## Step 8: Section Layout Reference

### Standard document structure
```
Cover page (no H1, no page break before)
  ├── Title block (large company/doc name)
  ├── Subtitle / metadata line
  ├── Metrics table (optional)
  └── Summary table (optional)

Section pages (H1 starts each)
  ├── H1 — Section title (page break before, bottom rule)
  ├── Lead paragraph (body bold, after=120)
  ├── H2 — Subsection
  ├── Body paragraphs / bullets
  └── Tables as needed

Footnote line (last element on last page)
  └── Paragraph with top border BBBBBB, caption text, italic
```

### Cover title block
```javascript
// Company/document name — large, SemiBold, navy
new Paragraph({
  spacing: { before: 120, after: 40 },
  children: [new TextRun({
    text: 'Document Title',
    font: 'Wix Madefor Display SemiBold',
    size: 52,
    color: '0F4761',
  })]
})

// Subtitle
new Paragraph({
  spacing: { before: 0, after: 40 },
  children: [new TextRun({
    text: 'Subtitle — Framework Name',
    font: 'Wix Madefor Display',
    size: 26,
    color: '444444',
  })]
})

// Metadata (date, price, confidential)
new Paragraph({
  spacing: { before: 0, after: 200 },
  children: [new TextRun({
    text: 'March 24, 2026  ·  Confidential',
    font: 'Wix Madefor Display',
    size: 18,
    italics: true,
    color: '666666',
  })]
})
```

---

## Step 9: Critical Rules

1. **Never use Arial** — all text must use Wix Madefor Display or Wix Madefor Display SemiBold
2. **Never use bold: true** — use `font: 'Wix Madefor Display SemiBold'` instead for all emphasis (H1, H2, Body Bold Lead, Body Note, table headers, callouts). Setting `bold: true` alongside SemiBold double-bolds and breaks the visual system.
3. **Content width = 10800 DXA** — all tables must use this width; columnWidths must sum to 10800
4. **ShadingType.CLEAR** — always use CLEAR, never SOLID (SOLID turns backgrounds black)
5. **Never use unicode bullets directly** — always use `numbering` config with `LevelFormat.BULLET`
6. **Phase 2 is always required** — never try to generate header/footer in docx-js
7. **Content_Types.xml Override entries are mandatory** — missing them = invisible header/footer
8. **Footer tab stop** — use `<w:tab w:val="right" w:pos="10800"/>` in pPr tabs + `<w:tab/>` run element; do NOT use `<w:ptab>` (unreliable across renderers)
9. **Page margins are 0.5 inch (720 DXA)** — not the docx-js default of 1 inch
10. **characterSpacing: 40** on H1 text runs — this is the slight tracking on section headers

---

## Step 10: Full Working Example

See the Sea Limited PE Strategy Analysis document as the canonical reference implementation.
It demonstrates all paragraph types, all table variants, multi-section layout, and the complete
Phase 2 patch workflow.
