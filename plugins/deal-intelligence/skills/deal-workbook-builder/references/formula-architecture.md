# Deal Workbook Formula Architecture

## Data flow

```
FINANCIAL MODEL (read-only source)
        │
        ▼
INPUTS rows 48-62  ← auto-links: GMV, attach rate, GPV%, MRR, revenue, net cash
INPUTS rows 65-85  ← editable blue inputs: GPV $/100bps, GMV alloc %, incr EBITDA margins, MRR sub-drivers
INPUTS row 86      ← derived: Revenue/MRR multiplier = C60/C54
        │
        ├──► KPI TREE
        │      G = FY2025A Actual  ('FM'!F{row})
        │      H = FY2026E Budget  ('FM'!G{row})
        │      I = FY2028E Exit    ('FM'!I{row})
        │      J = Δ vs Budget     ppt for margins, % change for dollars
        │      K = Status          IF formula: On Track / Watch / Behind Plan
        │      L = Notes
        │
        ▼
DRIVER TREE
  Metric cols (F/G/H) = INPUTS formula refs
  Delta col (I)        = H - G  (except I15 GPV%: see note below)
  Revenue impact (J)   = formula chain from metric delta × rate assumptions
  EBITDA impact (L)    = J × K (incremental margin from INPUTS)
  EV impact (M)        = L × INPUTS!C18 (entry multiple, Paasche)
  MOIC delta (N)       = M / INPUTS!C21 (entry equity)
        │
        ├──► NTB REGISTRY
        │      E7: ='DRIVER TREE'!M13+'DRIVER TREE'!M16+'DRIVER TREE'!M23  (NTB 1 GMV)
        │      E8: ='DRIVER TREE'!M15                                        (NTB 2 Payments/GPV)
        │      E10: ='DRIVER TREE'!M22                                       (NTB 4 Enterprise Plus)
        │      E11: ='DRIVER TREE'!L31                                       (Multiple compression)
        │      E12: =SUM(E7:E11)+'DRIVER TREE'!L32                          (Total + net cash)
        │      F7-F12: =IFERROR(En/INPUTS!C21,"-")                          (MOIC deltas)
        │      F13: =IFERROR(1+F12,"-")                                     (MOIC check)
        │
        └──► MOIC BRIDGE
               C8-C11: ='NTB REGISTRY'!E7-E10   (NTB 1-4 EV)
               D8-D11: ='NTB REGISTRY'!F7-F10   (NTB 1-4 MOIC delta)
               C14: ='DRIVER TREE'!L31           (Multiple compression EV)
               D14: ='DRIVER TREE'!N31           (Multiple compression MOIC delta)
               C15: ='DRIVER TREE'!L32           (Net cash EV)
               D15: ='DRIVER TREE'!N32           (Net cash MOIC delta)
               E7-E15: cumulative MOIC chain (E_prev + D_current)
               E16: =INPUTS!C30/INPUTS!C21       (independent check: exit equity / entry equity)
```

## Revenue decomposition (Paasche)

Merchant Solutions:
```
Revenue = GMV ($B) × Attach Rate (bps/10000) × 1000 → $M

Volume effect  = ΔGMV ($B) × entry_attach_rate (bps/10000) × 1000
               = (exit_GMV - entry_GMV) × C50/10000 × 1000

Attach effect  = exit_GMV × Δattach_rate (bps/10000) × 1000
               = = total_merch_delta - volume_effect
               = INPUTS!C57 - INPUTS!C56 - J13

  GPV component    = (exit_GPV% - entry_GPV%) × 100 × $67M/100bps × (exit_GMV / base_GMV)
                   = (H15-G15)*100*INPUTS!C65*INPUTS!C49/INPUTS!C62
  Non-payments     = residual = J17 - J15
```

Subscription Solutions:
```
Revenue ≈ MRR × (entry_sub_rev / entry_MRR)   [implied Revenue/MRR multiplier]

Plus MRR delta    = C82 - C81   → revenue = delta × C86
Core MRR delta    = C85 - C84   → revenue = delta × C86
```

## EV and MOIC bridge (Paasche)

```
EV(exit) - EV(entry) = EBITDA_delta × entry_multiple   (revenue component)
                     + (exit_mult - entry_mult) × exit_EBITDA  (compression component)

Equity value created = Revenue_EV + Multiple_compression_EV + Net_cash_build
                     = (L18+L24) × C18  +  (C27-C18)×C26  +  -(C29-C20)

MOIC = 1 + equity_value_created / entry_equity
     = 1 + N33                    [DRIVER TREE row 34]
     = INPUTS!C30 / INPUTS!C21    [independent check, MOIC BRIDGE row 16]
```

## INPUTS row index

| Row | Content | Type |
|-----|---------|------|
| 18 | Entry EV multiple | Hardcode |
| 19 | Entry EV ($M) = C16×C18 | Formula |
| 20 | Entry net cash ($M, negative = cash) | Hardcode |
| 21 | Entry equity ($M) = C19-C20 | Formula |
| 26 | Exit EBITDA ($M) | Hardcode |
| 27 | Exit EV multiple | Hardcode |
| 28 | Exit EV = C26×C27 | Formula |
| 29 | Exit net cash ($M, negative = cash) | Hardcode |
| 30 | Exit equity = C28-C29 | Formula |
| 34 | MOIC = C30/C21 | Formula |
| 48 | Entry GMV ($B) | =FINANCIAL MODEL!G41 |
| 49 | Exit GMV ($B) | =FINANCIAL MODEL!I41 |
| 50 | Entry attach rate (bps) | =FINANCIAL MODEL!G43×10000 |
| 51 | Exit attach rate (bps) | =FINANCIAL MODEL!I43×10000 |
| 52 | Entry GPV penetration | =FINANCIAL MODEL!G42 |
| 53 | Exit GPV penetration | =FINANCIAL MODEL!I42 |
| 54 | Entry MRR ($M) | =FINANCIAL MODEL!G44 |
| 55 | Exit MRR ($M) | =FINANCIAL MODEL!I44 |
| 56 | Entry merch rev ($M) | =G41×G43×1000 |
| 57 | Exit merch rev ($M) | =I41×I43×1000 |
| 58 | Entry total rev ($M) | =FINANCIAL MODEL!G17 |
| 59 | Exit total rev ($M) | =FINANCIAL MODEL!I17 |
| 60 | Entry sub rev = C58-C56 | Formula |
| 61 | Exit sub rev = C59-C57 | Formula |
| 62 | Base GMV FY2025A ($B) | =FINANCIAL MODEL!F41 |
| 65 | GPV $M per 100bps at base GMV | 67 (IC Memo input) |
| 68-71 | GMV sub-driver allocations (must sum 100%) | Blue inputs |
| 75 | Merch incr EBITDA margin | 0.214 (calibrated) |
| 76 | Sub incr EBITDA margin | 0.676 (calibrated) |
| 80-85 | MRR sub-drivers (Plus / Core, entry / exit) | Blue inputs |
| 86 | Revenue/MRR multiplier = C60/C54 | Formula |

## FINANCIAL MODEL column mapping

| Period | Column index | Excel col |
|--------|-------------|-----------|
| FY2025A | 66 | BO |
| FY2026E | 71 | BT |
| FY2027E | 76 | BY |
| FY2028E | 81 | CD |

Key row references (IS sheet):
- Row 17: Total Revenue
- Row 41: GMV ($B)
- Row 42: GPV% of GMV
- Row 43: Attach Rate (decimal)
- Row 44: MRR ($M)
- Row 26: EBITDA margin

## NTB-to-driver mapping

| NTB | Theme | DRIVER TREE source |
|-----|-------|-------------------|
| NTB 1 | GMV Flywheel | M13 + M16 + M23 |
| NTB 2 | Payments / GPV | M15 |
| NTB 3 | AI Commerce | 0 (no base model) |
| NTB 4 | Enterprise Plus | M22 |
| NTB 5 | Multiple Compression | L31 |
| — | Net Cash Build | L32 (in total E12 only) |

Verification: NTB1 + NTB2 + NTB4 = M18 + M24 (total revenue EV). Always check.

---

## KPI TREE column layout

| Col | Header | Content | Number format |
|-----|--------|---------|---------------|
| B | Lvl | NS / 1 / 2 hierarchy level | General |
| C | KPI Name | Metric label | General |
| D | Category | Growth / Margin / Payments / Cash / Efficiency | General |
| E | Financial Model Line | Source row reference text | General |
| F | Frequency | Monthly / Quarterly | General |
| G | FY2025A Actual | `='FINANCIAL MODEL'!F{row}` | metric-specific |
| H | FY2026E Budget | `='FINANCIAL MODEL'!G{row}` or INPUTS link | metric-specific |
| I | FY2028E Exit | `='FINANCIAL MODEL'!I{row}` | metric-specific |
| J | Δ vs Budget | Smart delta formula — ppt or % per metric type | see below |
| K | Status | IF formula — On Track / Watch / Behind Plan | General |
| L | Notes | Analyst commentary (wrap text, grey italic) | General |

### Δ vs Budget formula rules (col J)

The formula and number format are both required. Getting one wrong silently
produces bad output — e.g., an absolute dollar delta with `%` format
shows `570%` instead of `+5.7B`.

| Row type | Formula | Number format |
|----------|---------|---------------|
| Margin / rate rows (EBITDA%, gross margin, GPV%, take rate, cost %s, capex%) | `=IFERROR((G{r}-H{r})*100,"-")` | `+0.0"ppt";-0.0"ppt";"-"` |
| Dollar / volume rows (Revenue $M, GMV $B, MRR $M, FCF $M) | `=IFERROR((G{r}-H{r})/ABS(H{r}),"-")` | `+0.0%;-0.0%;"-"` |

Margin rows in v7 Shopify workbook: `{12,13,14,15,16,17,18,20,21,22,23,25,26}`
Dollar rows: `{7,8,9,10,11,24}`

### KPI TREE model links by row

| Row | KPI | G (Actual) | H (Budget) | I (Exit) |
|-----|-----|-----------|-----------|---------|
| 7 | GMV ($B) | `'FM'!F41` | `'FM'!G41` | `'FM'!I41` |
| 8 | Total Revenue ($M) | `'FM'!F17` | `'FM'!G17` | `'FM'!I17` |
| 9 | Sub Solutions ($M) | Derived | `INPUTS!C60` | `INPUTS!C61` |
| 10 | Merch Solutions ($M) | Derived | `INPUTS!C56` | `INPUTS!C57` |
| 11 | MRR ($M) | `'FM'!F44` | `'FM'!G44` | `'FM'!I44` |
| 12 | Blended Gross Margin | `F19/F17` | `'FM'!G8` | `I19/I17` |
| 15 | Adj. EBITDA Margin | `'FM'!F26` | `'FM'!G26` | `'FM'!I26` |
| 20 | GPV Penetration % | `'FM'!F42` | `'FM'!G42` | `'FM'!I42` |
| 21 | Payments Take Rate | `'FM'!F43` | `'FM'!G43` | `'FM'!I43` |
| 24 | Free Cash Flow ($M) | `'FM'!F38` | `'FM'!G38` | `'FM'!I38` |

(`'FM'` = `'FINANCIAL MODEL'`)

---

## DRIVER TREE delta column (col I) — unit rules

Most delta cells use `=H{r}-G{r}`. One exception:

| Row | Metric | Formula | Format | Reason |
|-----|--------|---------|--------|--------|
| I15 | GPV% penetration | `=(H15-G15)*100` | `+0.0"ppt";-0.0"ppt";"-"` | Values are stored as decimals (0.71, 0.79); `H-G` gives 0.08 which `%` format would show as `8.0%` — ambiguous. Multiply by 100 so the stored value is 8.0 and use the `"ppt"` literal suffix. |
| All other I col rows | — | `=H{r}-G{r}` | `#,##0.0` or `#,##0` | Native units (bps, $B, $M) |

**Rule:** never apply `%` format to a raw decimal difference. Either store
the value as a ratio and use `%` format (Excel multiplies by 100), OR
multiply by 100 in the formula and use a `"ppt"` literal suffix.

---

## McKinsey formatting palette

Applied after formulas are verified. Color is structural signal, not decoration.

| Role | Hex | Applied via |
|------|-----|-------------|
| Section headers (navy) | `0F4761` | PatternFill solid, white bold font |
| Subtotal rows (light grey) | `F0F0F0` | PatternFill solid |
| Total rows | None / white | Bold font + thin top+bottom border `AAAAAA` |
| Data rows | None / white | Default |
| MOIC CHECK row | `0F4761` | PatternFill solid, white bold font |
| Status: On Track | — | Text color `375623` only (no fill) |
| Status: Watch | — | Text color `9C5700` only (no fill) |
| Status: Behind Plan | — | Text color `C00000` only (no fill) |
| Notes / footnotes | — | Text color `666666`, italic |

### DRIVER TREE row classification

| Rows | Type | Fill | Font |
|------|------|------|------|
| 6 | Col header | Navy `0F4761` | White bold |
| 7, 20, 28 | Section header | Navy `0F4761` | White bold |
| 8, 14 | Sub-section label | None | Black bold |
| 9–12, 15–16, 21–23, 29–33 | Driver data | None | Normal |
| 13, 17, 24 | Subtotal | `F0F0F0` | Bold |
| 18, 26 | Section total | None | Bold + thin border |
| 34 | MOIC CHECK | Navy `0F4761` | White bold |
| 35 | Footnote | None | Grey `666666` italic 8pt |

### KPI TREE row classification

| Rows | Type | Fill | Font |
|------|------|------|------|
| 6 | Col header | Navy `0F4761` | White bold |
| L1 rows (`{7,8,12,15,19,24}`) | Section KPI | None | Bold + thin top border |
| L2 rows (all others 7–26) | Sub-KPI | None | Normal |
| K col | Status | None | Conditional text color |
| L col | Notes | None | Grey italic |
