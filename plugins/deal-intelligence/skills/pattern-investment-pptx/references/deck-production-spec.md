# Pattern Investment PPTX Production Spec

Detailed implementation reference for Pattern investment deck generation. Read this from `pattern-investment-pptx/SKILL.md` before writing or modifying deck code.

---

## Step 3: Brand Constants

Use these exact values. Never improvise with colors or fonts.

### Colors (no `#` prefix in pptxgenjs)

```javascript
const C = {
  // Backgrounds
  white:        "FFFFFF",   // Default — ALL content slides use white background
  lightGray:    "F5F6F8",   // Card fills, subtle panel backgrounds
  panelGray:    "E8ECF0",   // Callout box backgrounds, shaded cells

  // Primary text
  black:        "000000",   // Primary body text, headings on light slides
  textDark:     "333333",   // Secondary body text
  textMid:      "3C4043",   // Supporting text, axis labels
  textMuted:    "6E6F73",   // Captions, footnotes, muted labels
  textFaint:    "B5B5B5",   // De-emphasized text, gridlines, borders

  // Brand blue family (primary accent)
  brandBlue:    "4285F4",   // Primary accent — overlines, chart series 1, key highlights,
                             // numbered circle fills, navigation triangles, footnote line
  midBlue:      "2563EB",   // Secondary accent — table headers, active states, secondary info
  deepBlue:     "3B82F6",   // Tertiary — alternate chart series, timeline bars
  navyDark:     "0F1B2D",   // Dark table headers, section fills
  navyMid:      "1E293B",   // Alternate dark fills
  navyDeep:     "002060",   // Deep navy for strong-emphasis tables

  // Positive indicators
  tealPrimary:  "22655A",   // Positive data, growth indicators
  tealLight:    "4CC3AE",   // Chart fills, positive callouts
  tealFaint:    "DBF3EF",   // Light positive backgrounds

  // Negative / alert
  alertRed:     "900000",   // Negative data, risk callouts, down arrows
  alertLight:   "FFBFBF",   // Light negative backgrounds

  // Data viz palette — use in this exact order for multi-series charts
  chartBlue1:   "4285F4",   // Series 1 — primary
  chartBlue2:   "0D5BDC",   // Series 2
  chartBlue3:   "2700A8",   // Series 3
  chartBlue4:   "3A00FD",   // Series 4
  chartGray:    "6E6F73",   // Series 5 — de-emphasis
  chartGrayLt:  "B5B5B5",   // Series 6 — lightest de-emphasis

  // Table-specific
  tableHeaderDark:  "002060",   // Primary table header row fill
  tableHeaderMid:   "1E293B",   // Alternate table header fill
  tableRowAlt:      "D9E2F3",   // Alternating table row highlight fill
  tableBorder:      "E0E0E0",   // Table cell borders
  tableHighlight:   "4285F4",   // Category/group text color highlight
};
```


## Step 3b: Color Methodology

Keep the Pattern color constants exactly as defined above. Apply them using this methodology:

### Foundation first

- Start with neutrals: `C.white` for content slide backgrounds, `C.black`/`C.textDark` for primary text, `C.textMid`/`C.textMuted` for supporting text, and `C.textFaint` for quiet structure
- Use whitespace, alignment, proximity, font size, and `F.semibold` before adding color
- If the slide works in neutral text and gray structure, do not add emphasis color

### Highlight second

- Use `C.brandBlue` as the primary highlight color for the one element that carries the slide's main message: a key heading, data value, chart series, label, rule, directional marker, or visual entry point
- Highlight only what requires emphasis. Do not color every bullet, every heading, or every data label
- For negative meaning use `C.alertRed`; for positive meaning use `C.tealPrimary` or `C.tealLight`. These colors are semantic, not decorative
- Use secondary blues only when a chart or diagram genuinely needs additional series distinction

### De-emphasize before adding more color

- When one element needs focus, first reduce surrounding elements to `C.textMuted`, `C.textFaint`, `C.chartGray`, or `C.chartGrayLt`
- Prefer a gray base plus one `C.brandBlue` highlight over multiple competing colors
- If a heading, label, icon, line, and chart series are all blue, the slide has lost hierarchy. Keep only the highest-signal blue element and neutralize the rest

### Never use color as structure

- Do not use color-filled text boxes to organize normal slide content. Use whitespace, alignment, size, outlines, and dividing lines instead
- Do not color-code entire blocks of text to match a diagram, process, or chart. Start with default text color, then add selective text highlight only if needed
- Do not color-highlight words inside titles, subtitles, sentences, or dense paragraphs
- Do not mix text highlighting and broad color-coding on the same slide
- Color-filled shapes are acceptable only when they are genuine diagrams, Gantt/task bars, title-slide elements, or intentional big-statement/section moments

### Consistency test

Before generating code, answer: what does each color mean on this slide? If the answer is not clear, remove or neutralize the color. Across a deck, the same color should signal the same role or meaning.

---

### Fonts

```javascript
const F = {
  semibold: "Wix Madefor Display SemiBold",  // ALL bold text — slide titles, table headers, bold runs
  medium:   "Wix Madefor Display Medium",    // Default body, bullet text, sub-headings
  regular:  "Wix Madefor Display",           // Captions, footnotes, slide number, non-emphasis body
  fallback: "Calibri",                       // Fallback if Wix not installed
};
```

> **Critical font rule:** There is no `bold: true` in this deck. "Bold" is always achieved by
> switching to `F.semibold` ("Wix Madefor Display SemiBold"). This applies to:
> - Slide titles (all content slides)
> - Title slide deck name
> - Table header rows
> - Any bolded run within body text
> Never pass `bold: true` with `F.medium` or `F.regular` — always switch fontFace to `F.semibold`.

> **Important:** Wix Madefor Display must be installed for correct rendering. Never substitute
> Inter or Segoe UI — this is a distinct deck from the standard Pattern marketing deck.

### Type Scale (points)

```javascript
const SIZE = {
  slideTitle:   14,   // Slide title — Wix Madefor Display SemiBold
  body1:        10,   // Level-1 bullet (main point, brandBlue)
  body2:         9,   // Level-2 bullet (sub-point, text color)
  body3:         9,   // Level-3 bullet (tertiary, text color)
  caption:       7,   // Captions, axis labels
  footnote:      7,   // Footnotes, source lines — always 7pt Wix Madefor Display
  tableHeader:   9,   // Table column/row headers — F.semibold
  tableBody:     8,   // Table cell content — F.medium or F.regular
  bigMetric:    24,   // Large KPI callout numbers
  metricLabel:   8,   // Label under big metric
  slideNumber:   8,   // Slide number bottom-right
  navText:       9,   // Navigation breadcrumb text (max 2 lines)
  titleSlide:   24,   // Title slide deck name — F.semibold
  titleSubtitle: 11,  // Title slide subtitle/date line
};
```

---

## Step 4: Slide Layout & Grid

```javascript
// Deck uses 10" × 5.625" — NOT the standard 13.333" wide LAYOUT_WIDE
// Set custom dimensions explicitly:
pres.defineLayout({ name: 'CUSTOM_10x5625', width: 10, height: 5.625 });
pres.layout = 'CUSTOM_10x5625';
```

### Master Grid Structure

```
┌──────────────────────────────────────────────────────────┐
│  TITLE BAR  (x:0.366, y:0.174, w:9.077, h:0.346)  [icon: x:9.478, y:0.239, w:0.268, h:0.208] │
├──────────────────────────────────────────────────────────┤ ← blue rule y:0.656, w:10.0, h:0.014
│                                                          │
│  CONTENT AREA  (y:0.94 → y:5.185)                       │
│  ┌───────────────────────┬─────────────────────┐         │
│  │   Upper Left          │   Upper Right       │         │
│  ├───────────────────────┼─────────────────────┤         │
│  │   Lower Left          │   Lower Right       │         │
│  └───────────────────────┴─────────────────────┘         │
├──────────────────────────────────────────────────────────┤
│  FOOTNOTE ZONE  (y:5.276)             [slide number: BR] │
└──────────────────────────────────────────────────────────┘
```

**No-fly zone — authoritative values (confirmed from source presentation settings):**

```
Top margin:    0.94"   → content y starts at 0.94"
Left margin:   0.40"   → content x starts at 0.40"
Right margin:  0.28"   → content right edge at 9.72" (10.0 - 0.28)
Bottom margin: 0.44"   → content bottom at 5.185" (5.625 - 0.44)
Content width: 9.32"   (9.72 - 0.40)
Content height: 4.245" (5.185 - 0.94)
```

The footnote zone (y=5.276) and slide number sit **below** the content no-fly zone bottom — they are exempt from this rule. The slide title and blue rule sit **above** the top margin — also exempt. Everything else (text boxes, charts, tables, shapes) must stay within these bounds.

**Coordinate reference (all values exact from master):**
- Title: x=0.366", y=0.174", w=9.077", h=0.346"
- Blue rule: x=0", y=0.656", w=10.0" (full width), h=0.014", fill `4285F4`
- Icon mark (top-right): x=9.478", y=0.239", w=0.268", h=0.208"
- **Content area: x=0.40", y=0.94", w=9.32", h=4.245"**
- Footnote zone: x=0.401", y=5.276", w=6.71", h=0.3"
- Slide number: x=7.466", y=5.276", w=2.25", h=0.3", align right

---

## Step 5: Recurring Slide Elements

### Slide Title

```javascript
slide.addText(slideTitle, {
  x: 0.366, y: 0.174, w: 9.077, h: 0.346,
  fontFace: F.semibold, fontSize: SIZE.slideTitle,
  color: C.black, align: "left", valign: "middle", margin: 0,
});
```

### Blue Rule (below title, every content slide)

```javascript
slide.addShape(pres.ShapeType.rect, {
  x: 0, y: 0.656, w: 10.0, h: 0.014,
  fill: { color: C.brandBlue }, line: { color: C.brandBlue },
});
```

### Icon Mark (top-right corner, every content slide)

```javascript
slide.addImage({
  path: `${SKILL_DIR}/assets/pattern_icon_mark.svg`,
  x: 9.478, y: 0.239, w: 0.268, h: 0.208,
});
```

### Slide Number

```javascript
slide.addText(String(slideNum), {
  x: 7.466, y: 5.276, w: 2.25, h: 0.3,
  fontFace: F.regular, fontSize: SIZE.slideNumber,
  color: C.textFaint, align: "right", margin: 0,
});
```

### Footnote Zone

Include only lines that are needed. Omit any line with no content.

```javascript
// Short divider line (left half of slide)
slide.addShape(pres.ShapeType.line, {
  x: 0.366, y: 5.24, w: 2.6, h: 0,
  line: { color: C.textFaint, width: 0.75 },
});

// Text block: all footnotes inline on line 1, Note on line 2, Source on line 3
slide.addText("1. [Source Name, Year] — [Confidence: HIGH/MEDIUM/LOW]  2. [footnote]\nNote: [note]", {
  x: 0.401, y: 5.276, w: 6.71, h: 0.3,
  fontFace: F.regular, fontSize: SIZE.footnote,
  color: C.textMuted, align: "left", valign: "top", margin: 0,
});
```

**Footnote rules:**
- Superscript indicator directly after the claim text — no space before the superscript
- All footnote numbers on one line: `1. xxxx  2. xxxx  3. xxxx`
- No new line per footnote; no brackets around numbers; no periods at end
- Indicators run top-left → bottom-right across slide
- Key Message slides: source line only; full footnotes on Detail slides

**Source confidence footnote format:**
Every cited source in a slide's footnote zone must include its confidence tier, determined
by CRAAP scoring (see claim-scrutinizer Step 6b):

```
1. [Source Name, Year] — Confidence: HIGH
2. [Source Name, Year] — Confidence: MEDIUM
```

- **HIGH** = CRAAP total 20–25 — cite directly
- **MEDIUM** = CRAAP total 15–19 — append brief limitation note if space allows
- **LOW** = CRAAP total <15 — do not use as primary evidence; if retained, body text
  must explicitly qualify the claim as unverified or directional

**Numbering rules:**
- Footnote numbers restart at 1 on every slide — never carry across slides
- If the same source appears twice on one slide, reuse the same number
- Maximum 3 footnote entries per slide — if more are needed, consolidate or move to appendix

---

## Step 6: Slide Templates

### A. Title Slide (Dark)

The only dark-background slide in the deck.

```javascript
slide.background = { color: "090A0F" };

slide.addImage({
  path: `${SKILL_DIR}/assets/pattern_logo_white.svg`,
  x: 0.37, y: 0.33, w: 1.65, h: 0.285,
});

// Deck name — Title Case, F.semibold
slide.addText(deckTitle, {
  x: 1.516, y: 2.682, w: 7.085, h: 0.894,
  fontFace: F.semibold, fontSize: SIZE.titleSlide,
  color: "FFFFFF", align: "center", valign: "middle", margin: 0,
});

// Subtitle / date — sentence case, F.regular
slide.addText(subtitle, {
  x: 1.516, y: 3.677, w: 7.085, h: 0.806,
  fontFace: F.regular, fontSize: SIZE.titleSubtitle,
  color: C.textFaint, align: "center", valign: "top", margin: 0,
});
```

### B. Title Only — Full Width

Best for: single wide chart, diagram, or dense table.

```javascript
slide.background = { color: C.white };
// Add title + blue rule + icon (Step 5)
// Content: x:0.366, y:0.801, w:9.398, h:4.399
// Add footnote zone + slide number (Step 5)
```

### C. Two Column

Left: key idea / chart. Right: supporting bullets or secondary chart.

```javascript
// Left:   x:0.366, y:0.801, w:4.5,  h:4.399
// Right:  x:5.0,   y:0.801, w:4.76, h:4.399
// Gutter: 0.134" gap (optional divider line at x:4.88 when content is dense)

// Column headings — left-aligned, sentence case, brandBlue, 2 lines max
slide.addText(colHeading, {
  x: 0.366, y: 0.801, w: 4.5, h: 0.28,
  fontFace: F.semibold, fontSize: SIZE.body2,
  color: C.brandBlue, align: "left", margin: 0,
});
```

**Use directional button** (chevron) to show left→right relationship when applicable.

### D. Three Column — Two-Thirds / One-Third (Key Message)

Best for: wide chart/visual left + numbered key points right.

```javascript
// Wide left (2/3):    x:0.366, y:0.801, w:6.3,  h:4.399
// Narrow right (1/3): x:6.8,   y:0.801, w:2.96, h:4.399
// Divider line: x:6.65, y:0.801, h:4.399, 0.75pt textFaint

// Keep right column minimal — move detail to speaker notes or Detail slides
// Use numbering system for key points (filled brandBlue circle, white number)
```

### E. Three Column — Equal

Best for: three parallel items or combined 2+1.

```javascript
// Col 1: x:0.366, y:0.801, w:2.9,  h:4.399
// Col 2: x:3.43,  y:0.801, w:2.9,  h:4.399
// Col 3: x:6.5,   y:0.801, w:3.16, h:4.399
// Dividers at x:3.28 and x:6.35
// When using multiple charts: align axes and sizes across all columns
```

### F. Four Column

Best for: dense parallel text, four equal categories.

```javascript
// Col 1: x:0.366, y:0.801, w:2.15, h:4.399
// Col 2: x:2.66,  y:0.801, w:2.15, h:4.399
// Col 3: x:4.96,  y:0.801, w:2.15, h:4.399
// Col 4: x:7.26,  y:0.801, w:2.5,  h:4.399
// No bullets at top level — wide paragraph spacing replaces them
// Left-align all headings and icons to maintain the whitespace grid
```

### G. Appendix Header

```javascript
slide.background = { color: C.white };
// Blue rule present; icon mark present; slide number present
slide.addText("Appendix", {
  x: 0.366, y: 2.4, w: 9.398, h: 0.6,
  fontFace: F.semibold, fontSize: 22,
  color: C.black, align: "center", margin: 0,
});
```

---

## Step 6b: Bullet Text Hierarchy

This is the exact bullet system used across all content slides. Confirmed from the slide master.
**Never use `bullet: true` alone** — always specify the character and font explicitly.

### Header (no bullet) — brandBlue SemiBold, section opener

Used when the L1 line is a **section heading** rather than a bulleted assertion. Bullets follow immediately below with zero gap.

```javascript
// Section header — no bullet, brandBlue SemiBold
// paraSpaceBef: 14 between sections, 4 for the first section
{ text: "Header text here", options: {
  fontFace: F.semibold, fontSize: SIZE.body1, color: C.brandBlue,
  bullet: false,
  paraSpaceBef: 14, breakLine: true,
}}

// L2 bullets that follow — paraSpaceBef: 1 (ultra-tight, almost flush to header)
{ text: "Supporting point", options: {
  fontFace: F.medium, fontSize: SIZE.body2, color: C.black,
  bullet: { code: '2022', font: 'Arial', indent: 10 },
  indentLevel: 0, paraSpaceBef: 1, breakLine: true,
}}

// L3 sub-bullets — en-dash, indented, paraSpaceBef: 0 (flush to L2)
{ text: "Sub-detail", options: {
  fontFace: F.medium, fontSize: SIZE.body3, color: C.black,
  bullet: { code: '2013', font: 'Arial', indent: 10 },   // – en-dash
  indentLevel: 1, paraSpaceBef: 0, breakLine: true,
}}
```

> **Spacing rule for this layout:** Header `paraSpaceBef` creates the inter-section gap (14pt). All bullets within a section use `paraSpaceBef: 0–1` — essentially flush. Never use `paraSpaceBef > 4` on body bullets in this layout.

> **Bold within a single-run bullet:** Use `fontFace: F.semibold` on the **entire line** for labelled bullets (e.g., "Key watchout: ..."). Do not split into two runs — pptxgenjs drops the bullet character when a bulleted paragraph spans multiple runs.

### Level 1 — Main point (brandBlue, 10pt) — Master Level 4 paragraph style

Confirmed from slide master Level 4 paragraph style:
- Bullet: `•` (Arial), text color (inherits brandBlue when set on run)
- marL: **14.4pt**, First: **-14.4pt** (hanging)
- Font: Wix Madefor Display, **10pt**, black (override to brandBlue in code)

```javascript
// As single paragraph in array:
{ text: "Main point text", options: {
  fontFace: F.medium, fontSize: SIZE.body1, color: C.brandBlue,
  bullet: { code: '2022', font: 'Arial', indent: 10 },
  indentLevel: 0,
  paraSpaceBef: 1,   // tight within section; 14 between sections (header pattern)
  breakLine: true,
}}

// As standalone addText:
slide.addText(text, {
  x: 0.40, y, w: 9.32, h,
  fontFace: F.medium, fontSize: SIZE.body1, color: C.brandBlue,
  bullet: { code: '2022', font: 'Arial', indent: 10 },
  margin: [0, 0, 0, 14],   // 14.4pt left = master marL
});
```

### Level 2 — Sub-point (black, 9pt) — Master Level 5 paragraph style

Confirmed from slide master Level 5 paragraph style:
- Bullet: Wix Madefor Display bullet character, text color
- marL: **30.24pt**, First: **-13.5pt** (hanging)
- Font: Wix Madefor Display, **9pt**, black

```javascript
{ text: "Sub-point text", options: {
  fontFace: F.medium, fontSize: SIZE.body2, color: C.textDark,
  bullet: { code: '2013', font: 'Arial', indent: 10 },   // – en-dash
  indentLevel: 1,
  paraSpaceBef: 0,   // flush to parent bullet — no gap
  breakLine: true,
}}

// As standalone addText:
slide.addText(text, {
  fontFace: F.medium, fontSize: SIZE.body2, color: C.textDark,
  bullet: { code: '2013', font: 'Arial', indent: 10 },
  margin: [0, 0, 0, 30],   // 30.24pt left = master marL
});
```

> **Bold runs:** Use `fontFace: F.semibold` on the entire single-run paragraph. Never split a bulleted paragraph into multiple runs — pptxgenjs drops the bullet character on multi-run bulleted paragraphs.

### Content text box — correct positioning for no-fly zone

All bullet text boxes must be positioned within the no-fly zone:

```javascript
slide.addText(bulletArray, {
  x: 0.40,     // no-fly left margin
  y: 0.94,     // no-fly top margin
  w: 9.32,     // no-fly width (9.72 - 0.40)
  h: 4.245,    // no-fly height (5.185 - 0.94)
  valign: "top",
  margin: 0,
});
```

### Multi-level array pattern (header + bullets)

```javascript
// Section header (no bullet) + tight bullet block
slide.addText([
  // Section header — no bullet, brandBlue SemiBold, inter-section gap
  { text: "Section heading assertion here", options: {
    fontFace: F.semibold, fontSize: SIZE.body1, color: C.brandBlue,
    bullet: false, paraSpaceBef: 14, breakLine: true,
  }},
  // L1 bullet — 10pt, brandBlue, •, tight (paraSpaceBef:1)
  { text: "Supporting evidence point", options: {
    fontFace: F.medium, fontSize: SIZE.body1, color: C.brandBlue,
    bullet: { code: '2022', font: 'Arial', indent: 10 },
    indentLevel: 0, paraSpaceBef: 1, breakLine: true,
  }},
  // L2 sub-bullet — 9pt, black, –, flush (paraSpaceBef:0)
  { text: "Tertiary detail point", options: {
    fontFace: F.medium, fontSize: SIZE.body2, color: C.textDark,
    bullet: { code: '2013', font: 'Arial', indent: 10 },
    indentLevel: 1, paraSpaceBef: 0, breakLine: true,
  }},
], {
  x: 0.40, y: 0.94, w: 9.32, h: 4.245,
  valign: "top", margin: 0,
});
```



### Dividing Lines

```javascript
// Solid — first-level division (separates whole content blocks)
slide.addShape(pres.ShapeType.line, {
  x, y, w, h: 0,
  line: { color: C.textFaint, width: 0.75 },  // or 1.5pt for stronger emphasis
});

// Dotted — subdivision (two parts of the same whole)
slide.addShape(pres.ShapeType.line, {
  x, y, w, h: 0,
  line: { color: C.textFaint, width: 0.75, dashType: "sysDot" },
});
```

**Rules:** Default weights are 0.75pt, 1.5pt, 3pt. Whitespace is always preferred over
gridlines. Solid = divides the whole; dotted = divides subgroups within a block.

### Directional Buttons (Chevrons)

```javascript
// Filled circle + ">" — guides eye, shows relationships between objects
// Color: brandBlue. Use with solid or dotted line (0.75–1.5pt, textFaint)
// Placement: center of line (default) or top/lollipop style

slide.addShape(pres.ShapeType.ellipse, {
  x: btnX - 0.11, y: btnY - 0.11, w: 0.22, h: 0.22,
  fill: { color: C.brandBlue }, line: { color: C.brandBlue },
});
slide.addText("›", {
  x: btnX - 0.11, y: btnY - 0.11, w: 0.22, h: 0.22,
  fontFace: F.semibold, fontSize: 9,
  color: "FFFFFF", align: "center", valign: "middle", margin: 0,
});
```

### Numbering System

```javascript
// Default: filled brandBlue circle, white number inside — F.semibold
slide.addShape(pres.ShapeType.ellipse, {
  x: numX, y: numY, w: 0.18, h: 0.18,
  fill: { color: C.brandBlue }, line: { color: C.brandBlue },
});
slide.addText(String(n), {
  x: numX, y: numY, w: 0.18, h: 0.18,
  fontFace: F.semibold, fontSize: 7,
  color: "FFFFFF", align: "center", valign: "middle", margin: 0,
});
// When circles compete with content hierarchy: switch to outlined circle
// (no fill, brandBlue border) or drop circle and use plain bold number
// Never use number balls in slide titles
```

### Navigation Breadcrumb (top-right, sectioned decks)

Triangle tab flush to top-right corner of slide.
- Light background: `brandBlue` triangle fill, white icon, `textMid` text at 9pt — F.semibold
- Dark background: white triangle fill, `brandBlue` icon, white text
- Icon height: 0.3–0.4" wide; max 2 lines of text
- Alternative: filled circle with number/letter instead of icon
- Set up on first slide of section; copy/paste to subsequent slides

---

## Step 8: Charts

### Core Principles

- Remove anything not required for validity — no bevels, shadows, photography near charts
- No plot area fill or border unless it is a dashboard
- Start charts in gray, then use `brandBlue` only for the data point, series, label, or callout that carries the main idea
- De-emphasize supporting series with `chartGray` or `chartGrayLt` before adding additional accent colors
- If the whole chart is the key idea, a monochromatic blue scheme is acceptable; otherwise use gray base + one blue highlight
- Data labels: use strategically — if too many become noise, omit; can replace y-axis/legend
- Never use default chart leader lines — draw manually as a shape if one is needed
- Every chart needs a source in the footnote
- Legend positioned left-to-right matching chart category order; keep close to data

### Structural Elements

- Gridlines: horizontal major only, 0.75pt, `E8ECF0` or `B5B5B5`
- X-axis: always include, 0.75pt
- Y-axis: optional — include if needed for context; omit for Key Message slides
- Axis titles: aligned to outside chart boundaries
- No minor gridlines unless chart is wide or scientific

### Color Schemes

```javascript
// Default analytical chart scheme — gray base + one Pattern highlight
const grayBaseWithHighlight = {
  base: [C.chartGray, C.chartGrayLt, C.panelGray],
  highlight: C.brandBlue,
};

// Monochromatic blue — use only when the whole chart is the key idea
const chartColors = ["4285F4", "0D5BDC", "2700A8", "3A00FD", "6E6F73", "B5B5B5"];

// Differentiate — one series is primary
// Primary series: "4285F4"
// All others: "6E6F73" or "B5B5B5"

// Monochromatic gray — supporting/de-emphasis context
const grayScale = ["3C4043", "6E6F73", "B5B5B5", "E8ECF0"];
```

**Method:** decide the chart story first, then color it. For ranking, correlation, or one highlighted variance, default to gray bars/lines plus one `brandBlue` data point or series. For positive/negative variance, use `tealPrimary` or `alertRed` only on the variance or label that encodes valence. Do not use the full blue sequence unless multiple peer series must be distinguished.

### Chart Types

**Bar charts:** 1–2 colors max. Use for ranking, long category labels, single-group comparison.
Nominal = monochromatic blue; Differentiate = gray base + `brandBlue` highlight bar.

**Column charts:** Max ~12 data points. Nominal = monochromatic blue; Differentiate = gray +
highlight. Stacked = callout labels on key values, not data labels on every segment.

**Line charts:** 2.5pt stroke, round caps, no area fill unless intentional area chart.

**Callout boxes:** 1pt `brandBlue` border, white or `panelGray` fill, 7–8pt `F.medium` text.

---

## Step 9: Tables

### Design Principles

- Structure data logically: order/group rows and columns clearly
- Abbreviate headings; include units in parentheses (Revenue ($M), Headcount (FTEs))
- Set margin at the **table level only** — never per-cell (see Common Pitfalls)
- Use alignment, whitespace, and selective horizontal rules before adding fills or gridlines
- Avoid shading to define structure; use shading only to highlight key information, totals, or true callout rows
- Use font color sparingly for category grouping or a key value; never color-code whole table sections when alignment or spacing would work
- Bold only on: headings, totals, grouping subheadings — never individual cells
- Only rotate column header text as a last resort due to space constraints

### Alignment

| Content type | Horizontal | Header matches |
|---|---|---|
| Text | Left | Left |
| Short numbers | Center | Center |
| Long numbers / decimals | Right | Right |
| Graphics / icons | Center | Center |

Column headers: vertically centered; body rows: top-aligned.

### Gridlines

- Horizontal borders only — 0.75pt solid `CDD5E2` for standard rows
- Use `dashed` border type for dotted separator rows (e.g., between Business Overview sub-rows)
- Set `{ pt: 0 }` on right and left borders to suppress vertical lines
- Global table border: `{ pt: 0, color: "FFFFFF" }` — let individual cell borders do the work

### Complete table code pattern

This is the validated pattern that avoids all known pptxgenjs table bugs:

```javascript
// ── Border presets ────────────────────────────────────────────────
// [top, right, bottom, left]
const BS = [{ pt: 0.75, color: "CDD5E2" }, { pt: 0 }, { pt: 0.75, color: "CDD5E2" }, { pt: 0 }];
const BD = [{ pt: 0.75, color: "C0CCE0", type: "dashed" }, { pt: 0 }, { pt: 0.75, color: "C0CCE0", type: "dashed" }, { pt: 0 }];
const BN = [{ pt: 0 }, { pt: 0 }, { pt: 0 }, { pt: 0 }];

// ── Cell factories ────────────────────────────────────────────────
// Header cell
const H = (t) => ({
  text: t,
  options: {
    fontFace: F.semibold, fontSize: SIZE.tableHeader,
    color: "FFFFFF", fill: { color: C.tableHeaderDark },
    align: "left", valign: "middle",
    border: BN,
  },
});

// Section row — MUST build as N explicit cells, NOT colspan
// (colspan causes fill bleed across the whole row in pptxgenjs)
const numCols = 6;
const secRow = (label) => Array.from({ length: numCols }, (_, i) => ({
  text: i === 0 ? label : "",
  options: {
    fontFace: F.semibold, fontSize: SIZE.tableBody,
    color: "FFFFFF", fill: { color: "1C3461" },
    align: "left", valign: "middle",
    border: BN,
  },
}));

// Label cell (left column)
const L = (t, bdr = BS, va = "top") => ({
  text: t,
  options: {
    fontFace: F.medium, fontSize: SIZE.tableBody,
    color: C.textDark, fill: { color: C.white },
    align: "left", valign: va, border: bdr,
  },
});

// Data cell (right columns)
const D = (t, bdr = BS, al = "center", va = "top") => ({
  text: t,
  options: {
    fontFace: F.medium, fontSize: SIZE.tableBody,
    color: C.textDark, fill: { color: C.white },
    align: al, valign: va, border: bdr,
  },
});

// ── Assemble and add ──────────────────────────────────────────────
slide.addTable(rows, {
  x: 0.317, y: 0.630,
  w: 9.447,
  colW: [1.60, 1.57, 1.57, 1.57, 1.57, 1.57],  // must sum to w
  rowH: rowHeightsArray,
  margin: [2, 5, 2, 5],   // ← table-level only; pts: [top, right, bottom, left]
  border: { pt: 0, color: "FFFFFF" },
  autoPage: false,
});
```

### Styling reference

```javascript
// Header row — F.semibold, NOT bold:true, fill tableHeaderDark
{ fill: { color: C.tableHeaderDark }, color: "FFFFFF", fontFace: F.semibold, fontSize: SIZE.tableHeader }

// Section divider row (spans full width via explicit cells, not colspan)
// Use sparingly for actual section breaks; avoid using filled rows as default structure
{ fill: { color: "1C3461" }, color: "FFFFFF", fontFace: F.semibold }

// Body rows
{ fontFace: F.medium, fontSize: SIZE.tableBody, fill: { color: C.white } }

// Alternating highlight row (sparingly — key info only; never candy-striping)
{ fill: { color: C.tableRowAlt } }

// Category / group text highlight — F.semibold, not bold:true
// Use only for row/column groups or a key value that needs a visual entry point
{ color: C.brandBlue, fontFace: F.semibold }

// Shading for callout row
{ fill: { color: C.panelGray } }  // Never to define rows structurally
```

**Table color method:** default body cells to white with dark text. Use `tableHeaderDark` only for the header row, `brandBlue` text for a small number of group labels or key values, and `panelGray`/`tableRowAlt` only for totals or callout rows. Never use full-row or full-column color coding to compensate for weak table structure.

> **Font rule in tables:** Never use `bold: true`. Use `fontFace: F.semibold` for all
> emphasis — header rows, group labels, totals.

### Row height sizing

Calculate row heights so the table fills the full content area (y=0.630 → y=5.18 = 4.55"):

```javascript
// Fixed heights
const hdrH  = 0.200;  // header row
const secH  = 0.145;  // section divider rows
const tallH = 0.570;  // multi-line rows (product lists, 6+ lines)
const medH  = 0.195;  // 2-line rows (monetization, etc.)

// Standard data rows: fill remaining space evenly
const fixedH = hdrH + (numSections * secH) + tallH + medH + (numOtherSpecial * specialH);
const remaining = 4.55 - fixedH;
const dataH = remaining / numStandardRows;
// Typical dataH for a full investment table: 0.210–0.240"
```

---

## Step 10: Layout Selection Guide

| Content type | Layout |
|---|---|
| Single wide chart, diagram, or table | Title Only (full width) |
| Chart + supporting bullets or secondary chart | Two Column |
| Wide chart + numbered takeaways | Three Column (2/3 + 1/3) |
| Three parallel items or combined 2+1 | Three Column (equal) |
| Four equal categories or dense parallel text | Four Column |
| Process flow or ranked list | Any layout + Numbering System |

**Key rules:**
- Two column: headings left-aligned, sentence case, max 2 lines, `brandBlue` only when the heading is a true visual entry point
- Three column (2/3+1/3): right column minimal — detail in speaker notes
- Three column (equal): align all chart axes and labels when multiple charts present
- Four column: no bullets at top level; wide paragraph spacing replaces them; left-align all elements
- For diagrams and process layouts, do not color-code the surrounding text to match each segment; use neutral text and selective `brandBlue` highlight only where meaning changes
- On slides with large color panels or filled diagram shapes, keep text minimal and avoid adding competing color elsewhere

---
