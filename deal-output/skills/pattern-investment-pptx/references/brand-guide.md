# Pattern Investment Deck — Brand Guide Reference

> Complete edge-case reference for charts, tables, lines, buttons, editorial, and layout.
> Read sections as needed. SKILL.md contains the core rules; this file contains full detail.

---

## 1. COLOR SYSTEM

### Full Palette

| Name | Hex | Usage |
|---|---|---|
| white | FFFFFF | All content slide backgrounds |
| lightGray | F5F6F8 | Card fills, subtle panels |
| panelGray | E8ECF0 | Callout boxes, shaded table cells |
| black | 000000 | Primary headings and body text |
| textDark | 333333 | Secondary body text |
| textMid | 3C4043 | Supporting text, axis labels |
| textMuted | 6E6F73 | Captions, footnotes |
| textFaint | B5B5B5 | De-emphasized text, gridlines |
| brandBlue | 4285F4 | Primary accent — all blue highlights |
| midBlue | 2563EB | Secondary accent, table headers |
| deepBlue | 3B82F6 | Tertiary, timeline bars |
| navyDark | 0F1B2D | Dark table headers |
| navyMid | 1E293B | Alternate dark fills |
| navyDeep | 002060 | Strong-emphasis table headers |
| tealPrimary | 22655A | Positive data |
| tealLight | 4CC3AE | Positive callout fills |
| tealFaint | DBF3EF | Light positive backgrounds |
| alertRed | 900000 | Negative data, risk |
| alertLight | FFBFBF | Light negative backgrounds |
| tableHeaderDark | 002060 | Primary table header fill |
| tableHeaderMid | 1E293B | Alternate table header fill |
| tableRowAlt | D9E2F3 | Alternating highlight row |
| tableBorder | E0E0E0 | Table cell borders, 0.75pt |

### Data Viz Sequence (always in this order)

1. `4285F4` — Brand Blue (primary series)
2. `0D5BDC` — Mid Blue
3. `2700A8` — Deep Blue
4. `3A00FD` — True Blue
5. `6E6F73` — Medium Gray (de-emphasis)
6. `B5B5B5` — Light Gray (lightest de-emphasis)

### Color Application Rules

- Never use more than 3 colors on a single slide (excluding logos and photography)
- Use `brandBlue` for the primary/highlight series; gray for supporting series
- Positive data: `tealLight` or `tealPrimary`; Negative data: `alertRed`
- Shading: use only to highlight key information, never to define rows/columns structurally
- Dark slides: `090A0F` background (only the title slide uses a dark background)

### Color Methodology

- Start with a neutral foundation: use `black`, `textDark`, `textMid`, `textMuted`, `textFaint`, and white space to create the base structure before adding accent color
- Use `brandBlue` as the primary highlight, not as a decoration. Apply it to the single most important message, data point, series, heading, or visual entry point
- De-emphasize before adding color: push supporting elements to gray before introducing another accent
- Avoid color-coding entire blocks of text, long bullet groups, headings that merely mirror diagram segments, or table sections. Use default text colors first, then add selective text highlight only where it changes meaning
- Do not use color-filled text boxes to organize slide content. Use whitespace, alignment, size, text weight, outlines, and dividing lines before using filled shapes
- Do not highlight words inside titles, subtitles, sentences, or dense paragraphs. Highlight whole labels, key data values, short headings, or chart elements
- Use secondary colors only when they encode a distinct meaning: `tealPrimary`/`tealLight` for positive information, `alertRed` for negative information, and the blue sequence only for data visualization that requires multiple series
- Keep color consistent across the deck: the same color should mean the same thing on every slide

---

## 2. TYPOGRAPHY

### Font Weights

| Weight | Usage |
|---|---|
| Wix Madefor Display SemiBold | Slide titles, table column headers, key emphasis |
| Wix Madefor Display Medium | Sub-headings, callout labels, table body when emphasis needed |
| Wix Madefor Display | Body text, bullets, captions, footnotes, axis labels |
| Calibri | Fallback only if Wix is unavailable |

### Type Scale

| Element | Size | Weight | Color |
|---|---|---|---|
| Slide title | 14pt | SemiBold | black (000000) |
| Body level-1 (main bullet) | 10pt | Medium | brandBlue (4285F4) |
| Body level-2 (sub-bullet) | 9pt | Medium | black (000000) |
| Body level-3 (tertiary) | 9pt | Medium | black (000000) |
| Caption / axis label | 7pt | Regular | textMid or textMuted |
| Footnote / source | 7pt | Regular | textMuted (6E6F73) |
| Table header | 9pt | SemiBold | white on dark fill |
| Table body | 8pt | Regular or Medium | black |
| Big metric / KPI | 24pt | SemiBold | brandBlue or black |
| Slide number | 8pt | Regular | textFaint (B5B5B5) |
| Title slide — deck name | 24pt | SemiBold | white (FFFFFF) |
| Title slide — subtitle/date | 11pt | Regular | textFaint (B5B5B5) |

> **Bold rule:** Never use `bold: true`. All emphasis is achieved by switching to
> `Wix Madefor Display SemiBold`. This applies everywhere — slide titles, table headers,
> bold runs within bullets, callout labels, and the title slide deck name.

### Typography Rules

- Slide titles: sentence case, except title slide = Title Case
- Tight letter-spacing on large display text (charSpacing: -0.5)
- No underlines for emphasis — use bold or brandBlue color
- Avoid widows and orphans — use soft return (Shift+Enter) or trim
- Two font weights max per slide

---

## 3. LINES

### Line Types and Usage

| Type | Weight | Dash | Color | Use |
|---|---|---|---|---|
| Division — solid | 0.75pt | Solid | B5B5B5 | Primary separation of content blocks |
| Division — solid strong | 1.5pt | Solid | B5B5B5 | Stronger division |
| Division — dotted | 0.75pt | sysDot (round) | B5B5B5 | Sub-division within a block |
| Accent / blue rule | 1.5pt | Solid | 4285F4 | Below title, every content slide |
| Footnote divider | 0.75pt | Solid | B5B5B5 | Above footnote zone, left half only |
| Leader line | 0.75pt | Solid | B5B5B5 | Manual callout lines to data labels |

**Rules:**
- Default weights: 0.75pt, 1.5pt, 3pt — multiples of 3 above that
- Dotted lines must use round caps and round join type (dashType: "sysDot")
- Dotted lines never thinner than 0.75pt
- Solid = divides the whole content block; dotted = divides subgroups within
- No lines between every row — use sparingly for organization only
- Prefer whitespace over adding a line

### Leader Lines (Manual)

- Single node: filled circle (size 5) at one end — for labels
- Double node: filled circles both ends — for spans (time, date ranges)
- Arrow: use plain Arrow style, size 5 — for directional flow from a single point
- Never use default chart auto-leader lines — always draw manually

---

## 4. DIRECTIONAL BUTTONS

- Filled `brandBlue` circle with white "›" chevron
- Can be used with or without a line behind it
- Line behind: solid or dotted, 0.75–1.5pt, `textFaint`
- Placement: center of line (default) or top/lollipop (when line is above)
- Resize as needed; recolor to `midBlue` or `navyDark` to subdue
- Use when strong directional alignment is already present and a line would add noise

---

## 5. CHARTS — FULL DETAIL

### Anatomy Checklist (include only what is needed)

- Chart title: use slide title instead — avoid redundant title inside chart area
- Y-axis title: aligned to outside boundary; omit for Key Message slides if context is clear
- X-axis title: aligned to outside boundary
- X-axis line: 0.75pt, always include
- Y-axis line: 0.75pt, include only if needed for context
- Gridlines: horizontal major only, 0.75pt, `E8ECF0`; no minor gridlines
- Data labels: strategic — use instead of gridlines/legend when readable
- Legend: position left-to-right matching category order; below chart preferred; omit if labels are used
- Plot area: transparent, no border, no fill
- Source: always in footnote

### Reducing Clutter

Remove: gratuitous icons, logos, photography near charts, bevels, shadows, 3D effects.
Remove: plot area boundaries, tick marks, axis lines unless they aid understanding.
Remove: gridlines if data is labeled. Add gridlines only if data is not labeled or chart is very wide.

### Chart Types — Detail

**Bar chart:**
- Frequently misused — use for: ranking, long category labels, single group, showing correlation
- Column chart is better for time-series comparison
- 1–2 colors max. Nominal = monochromatic blue. Highlight = gray base + `brandBlue` bar.

**Column chart:**
- Use for comparing groups or tracking change over time
- Max ~12 data points before switching type
- When content is dense, consider readability of x-axis labels

**Stacked column chart:**
- Part-to-whole composition only
- Individual data point values are hard to read — use callout labels for key values
- Nominal = monochromatic blue; Differentiate = gray with single `brandBlue` segment

**Line chart:**
- 2.5pt stroke weight, round line caps
- Smooth lines preferred
- No area fill unless intentional area chart

### Callout Boxes on Charts

- Border: 1pt `brandBlue`; fill: white or `panelGray`
- Text: 7–8pt, Wix Madefor Display Medium, `black`
- Use to define a key idea, not just to repeat a data label
- Place close to the data point it annotates

---

## 6. TABLES — FULL DETAIL

### Content Structure

- Order and group information logically before styling
- Make headings clear — abbreviate where understood, include units in parentheses
- For Key Message slides: show only what's needed to support the main point
- For Detail slides: full table with supporting annotations

### Whitespace Rules

- Generous cell padding — whitespace is the first tool for readability
- Subheadings naturally create rows of whitespace — use them instead of gridlines
- Use bottom gridlines to separate the table from footnotes when whitespace isn't enough
- Don't add extra labels or callouts around the table — add a Detail slide instead

### Gridline Specifications

- Weight: 0.75pt
- Color: `E0E0E0` (tableBorder) or `B5B5B5` (textFaint)
- Always: bottom gridline under column header row
- When table has title above: top gridline on column header row
- When close to footnote: bottom table outline
- Vertical gridlines: only when column spacing is so tight that misreading is likely
- Use font color and row grouping to organize before resorting to vertical lines

### Styling Hierarchy

1. Column headers: `tableHeaderDark` (`002060`) fill, white `SemiBold` 8pt
2. Row group subheadings: `brandBlue` text, bold
3. Subtotal / total rows: bold, may use light `panelGray` fill
4. Key callout rows: `tableRowAlt` (`D9E2F3`) fill — sparingly
5. Secondary hierarchy text: `midBlue` — very sparingly
6. Normal body: Regular 7pt, `black`

**Bold rules:** Only for headings, totals, grouping subheadings, key rows/columns — never for individual cells within the body.

---

## 7. LAYOUT — FULL DETAIL

### Layout Selection

| Content | Layout |
|---|---|
| Single chart/diagram/table | Title Only |
| Chart + supporting text | Two Column |
| Wide visual + key points | Three Column 2/3+1/3 |
| Three equal topics | Three Column Equal |
| Four equal parallel topics | Four Column |
| Process/ranked content | Any + Numbering System |

### Two Column Rules

- Left heading: `brandBlue`, SemiBold, sentence case, max 2 lines
- Dividing line: only when dense; 0.75pt `textFaint`
- Directional button between columns when showing cause→effect
- Key idea: use color + position + size — not a filled shape callout

### Three Column (2/3 + 1/3) Rules

- Right column: succinct numbered points only — move details to speaker notes
- Chart highlight: `brandBlue` on key series; gray for supporting
- Dividing line grounds the right column — don't leave it floating

### Four Column Rules

- No bullets at first level — wide paragraph spacing serves this role
- Left-align all elements (headings, icons, text) to maintain the whitespace grid
- Reduce icon size so text remains visually dominant
- Don't push content all the way up to the slide title

### Numbering System Rules

- Default: filled `brandBlue` circle, white number
- On `brandBlue`/dark background: white circle, `brandBlue` number
- When circles compete with content: outlined circle (no fill, `brandBlue` border) or plain bold number
- Never number balls in slide titles — type number as plain text
- Use only for genuine process flow or ranked hierarchy

### Navigation Breadcrumb Rules

- Triangle tab flush top-right corner
- Light background: `brandBlue` fill, white icon, `textMid` text
- Dark background: white fill, `brandBlue` icon, white text
- Icon: 0.4" tall or 0.5" wide, whichever is larger
- Text: 10pt, max 2 lines, must fit within placeholder
- Alternative: filled circle with number or letter
- Set up on first slide of a section; copy/paste forward
- Never use as a content stamp

---

## 8. EDITORIAL — FULL DETAIL

### Case Rules

- Title slide title: Title Case (skip articles/prepositions/conjunctions under 5 letters: the, a, an, and, or, but, at)
- All other slide text: Sentence case — titles, headings, subheadings, bullets, labels, table headers, axis titles

### Punctuation Reference

| Mark | Rule | Example |
|---|---|---|
| Period | No periods at end of bullets. Use in running text. | "Revenue grew 40%" (no period) |
| En dash | Ranges and routes, no spaces | 100–150, 10:00–11:00 |
| Em dash | Parenthetical, no spaces | 50% off—today only |
| Ellipsis | Omitted quoted material only, space before/after | "Four score … years ago" |
| Slash | No spaces | and/or, 1920/21 |
| Comma | Thousands separator; serial comma per region | 8,000; eggs, bacon, and beans |
| Quotes | Double for main; single for quote-within-quote | "She said, 'Go.'" |

### Number Rules

| Context | Rule | Example |
|---|---|---|
| Under 10 in text | Spell out | "nine companies" |
| Under 10 with unit symbol | Use numeral | "$9", "£9" |
| Fractions in text | Spell out | "one-half" |
| Fractions in tables | Decimal | 0.5 |
| Thousands | Comma separator | 8,000 |
| Large numbers | T/B/M/K, no space | 42K, 17.4M, $2.3B, 1.1T |
| "000" as thousands | Never | Use K instead |

### Units of Measure

- Always lowercase: kg, km, lb, rpm
- Space between number and unit: 15 kg, 9.84 m
- No periods: kg not kg.
- No pluralization: kg not kgs
- In chart/table headers: parentheses — Revenue ($M), Population (K)
- Approved abbreviations: kg/kilos, km, mph, kph, T, B, M, K

### Date Formats

| Context | US | UK |
|---|---|---|
| Full date in text | October 23, 2025 | 23 October 2025 |
| Abbreviated | Oct. 23, 25 | 23 Oct 25 |
| Tables/charts | Jan, Feb, Mar… | Same |
| Cardinal only | October 19 (not 19th) | Same |

### Abbreviation Rules

- No punctuation: US, UK, GDP, EBITDA, GMV, NRR, GRR, CAC, LTV
- Always punctuate: e.g., i.e., p.a., vs., etc., et al., avg., ca., excl., incl., esp.
- "versus" in prose; "vs." in tables/charts only

### Vernacular

- Anglicized foreign words: no capitalize, no italics (ad hoc, bona fide, per se, vice versa, a priori, vis-à-vis, cum laude, status quo)
- Common nouns: lowercase unless starting sentence or part of proper noun (spring, north, federal government)
- Titles with name: capitalize (President Smith, Managing Director Jones)
- Titles without name: lowercase (the president, the managing director)

---

## 9. SLIDE QA CHECKLIST

Run after generating every deck:

**Structure:**
- [ ] Title slide is dark (`090A0F`), all others white
- [ ] Blue rule (1.5pt `4285F4`) below title on every content slide
- [ ] Slide number on every slide, bottom-right, `textFaint`
- [ ] Logo on title slide only
- [ ] No thesis divider slides

**Content:**
- [ ] Every slide title is a sentence-case insight statement (not a label)
- [ ] No periods at end of bullets
- [ ] Numbers over 10 use numeral; under 10 spelled out (unless unit symbol)
- [ ] T/B/M/K used correctly with no space
- [ ] Units in parentheses in chart/table headers
- [ ] Source in footnote for every chart and table

**Visual:**
- [ ] Chart colors match defined palette (not Office defaults)
- [ ] Table headers use `tableHeaderDark` fill with white text
- [ ] No gridlines between every row — whitespace preferred
- [ ] Column headings in sentence case, `brandBlue` on content slides
- [ ] No text overflow or cutoff
- [ ] No logo on content slides
