---
name: deal-workbook-builder
description: |
  Builds and maintains the PE/M&A deal workbook: formula-based driver tree,
  KPI tree, NTB registry, and MOIC bridge tabs, all chained live to a source
  FINANCIAL MODEL. Use when asked to "build the deal workbook," "rebuild the
  driver tree," "fix the MOIC contribution," "why are cells hardcoded,"
  "link the NTB registry to the model," "re-run the driver tree," "add a new
  deal to the workbook template," or any time a deal workbook tab shows
  hardcoded values that should be formula-driven. After every build or edit,
  automatically runs scripts/quality_check.py to verify column widths, row
  heights, number formats, and text fit — reports and fixes any layout
  defects before declaring the workbook complete.
---

# Deal Workbook Builder

You build and maintain a deal workbook: a single .xlsx file where every
number is a live formula chained from a source financial model. You never
hardcode a value that belongs to the formula chain. After every build or
edit you run the quality check and fix all layout defects reported.

Read this entire file before starting any build or edit.

---

## Architecture

The workbook has seven tabs. Their data flow is one-directional:

```
FINANCIAL MODEL (read-only source)
    └── INPUTS (formula links + editable analyst inputs)
            ├── DRIVER TREE (decomposition → EBITDA → EV → MOIC)
            │       ├── NTB REGISTRY (thesis-to-value attribution)
            │       └── MOIC BRIDGE (cumulative MOIC waterfall)
            ├── KPI TREE (budget vs. actual by driver)
            └── FINANCIALS (historical IS / BS snapshot)
```

Full formula architecture is in `references/formula-architecture.md`.
Read it before touching any formula.

---

## Step 1 — Map the FINANCIAL MODEL

Before writing a single formula, identify the exact cell coordinates in
the source model for every metric the workbook needs.

Required metrics and their typical model locations:

| Metric | Model row | FY2026E col | FY2028E col |
|--------|-----------|-------------|-------------|
| Total Revenue ($M) | IS row 17 | G | I |
| GMV ($B) | Drivers row 41 | G | I |
| GPV% of GMV | Drivers row 42 | G | I |
| Attach Rate (decimal) | Drivers row 43 | G | I |
| MRR ($M) | Drivers row 44 | G | I |
| EBITDA margin | IS row 26 | G | I |
| FY2025A baseline for each (prior period) | same rows | F | — |

**Do this mapping first, before writing any code.** Read a sample of
cells from the actual file and confirm they contain the expected values.
Wrong row/column assumptions produce silently wrong workbooks.

When columns differ from the defaults above (e.g. the model uses a
different year range or has extra columns), update the mapping and note
it in a comment at the top of the build script.

---

## Step 2 — Build or update INPUTS tab

INPUTS has two zones:

### Zone A — Model links (rows 48-62, black text)
These cells are plain formulas that pull from FINANCIAL MODEL:

```python
# Pattern: single-quoted sheet names for multi-word names
"='FINANCIAL MODEL'!G41"       # Entry GMV
"='FINANCIAL MODEL'!G41*'FINANCIAL MODEL'!G43*1000"  # Entry Merch Rev ($M)
"=C58-C56"                     # Entry Sub Rev (derived)
```

Every metric needed by the driver decomposition must appear here.
Never compute a value in Python and write it as a number.

### Zone B — Analyst inputs (rows 65-85, blue text)
These are editable blue inputs the analyst sets based on diligence:

| Row | Input | Default | Source |
|-----|-------|---------|--------|
| 65 | GPV revenue per 100bps at base GMV ($M) | 67 | IC Memo disclosure |
| 68-71 | GMV sub-driver allocations (must sum 100%) | 40/30/20/10% | Analyst judgment |
| 75 | Merch incr. EBITDA margin | 0.214 | Calibrated to model delta |
| 76 | Sub incr. EBITDA margin | 0.676 | Calibrated to model delta |
| 80-82 | Plus MRR: FY25A / FY26E / FY28E ($M) | from model Drivers sheet | Model read |
| 83-85 | Core MRR: FY25A / FY26E / FY28E ($M) | from model Drivers sheet | Model read |

Row 86 — Revenue/MRR multiplier — is always derived:
`=C60/C54` (entry sub rev ÷ entry MRR)

**Calibration check:** after wiring Zone A, verify:
`Merch_delta × C75 + Sub_delta × C76 = actual EBITDA delta`
If it doesn't match, adjust C75/C76 until it does.

---

## Step 3 — Build DRIVER TREE tab

The driver tree decomposes revenue growth using Paasche multiplicative
decomposition, then cascades through EBITDA to EV and MOIC.

### Revenue decomposition

**Merchant Solutions = GMV × Attach Rate**

```
Volume effect  = ΔGMV ($B) × entry_attach_rate (bps/10000) × 1000
               J_row = (H_row - G_row) × (INPUTS!C50/10000) × 1000

GPV component  = (exit_GPV% - entry_GPV%) × 100 × $67M/100bps × (exit_GMV / base_GMV)
               J15 = (H15-G15)*100*INPUTS!$C$65*INPUTS!$C$49/INPUTS!$C$62

Attach subtotal = total merch delta − volume effect (residual)
               J17 = INPUTS!$C$57-INPUTS!$C$56-J13

Non-payments   = residual within attach subtotal
               J16 = J17-J15
```

**Subscription = MRR delta × Revenue/MRR multiplier**
```
J22 = I22 * INPUTS!$C$86   (Plus MRR delta × multiplier)
J23 = I23 * INPUTS!$C$86   (Core MRR delta × multiplier)
```

### EBITDA and EV cascade

For every driver row:
```
L (EBITDA $M) = J × K      where K = INPUTS!C75 (merch) or C76 (sub)
M (EV $M)     = L × INPUTS!C18   (entry multiple, Paasche)
N (MOIC Δ)    = M / INPUTS!C21   (entry equity)
```

**Reconciliation requirement:** after building, verify:
- J18 (total merch) = INPUTS!C57 − INPUTS!C56 ✓
- J24 (total sub) ≈ INPUTS!C61 − INPUTS!C60 ✓
- L26 (total EBITDA) × C18 = Revenue EV ≈ $92B ✓
- N34 (MOIC check) = 1 + N33 ≈ 1.58× ✓

### Value Creation Bridge (rows 28-34)

```
Row 30  Revenue-driven EV:   J30=L26, K30=C18, L30=J30×K30, N30=L30/C21
Row 31  Multiple compression: J31=(C27-C18)×C26, L31=J31, N31=L31/C21
Row 32  Net cash build:       J32=-(C29-C20), L32=J32, N32=L32/C21
Row 33  Total:                L33=L30+L31+L32, N33=L33/C21
Row 34  MOIC check:           N34=1+N33 (should ≈ INPUTS!C34)
```

Note on net cash sign: INPUTS stores net cash as a negative number
(negative = cash-rich convention). `-(C29-C20)` correctly produces a
positive contribution when the cash position improves.

---

## Step 4 — Build NTB REGISTRY tab

NTB REGISTRY maps investment thesis pillars to model-computed EV. All
base EV and base MOIC columns must be formula-linked to DRIVER TREE.

```
NTB 1 GMV Flywheel:    E7 = ='DRIVER TREE'!M13+'DRIVER TREE'!M16+'DRIVER TREE'!M23
NTB 2 Payments:        E8 = ='DRIVER TREE'!M15
NTB 3 AI (optionality):E9 = 0  (no base model value)
NTB 4 Enterprise Plus: E10= ='DRIVER TREE'!M22
NTB 5 Compression:     E11= ='DRIVER TREE'!L31

MOIC deltas:           F7:F11 = =IFERROR(En/INPUTS!$C$21,"-")

Total base EV:         E12= =SUM(E7:E11)+'DRIVER TREE'!L32  ← includes net cash
Total base MOIC:       F12= =IFERROR(E12/INPUTS!$C$21,"-")
MOIC check:            F13= =IFERROR(1+F12,"-")             ← should = INPUTS!C34
```

**Decomposition check:** NTB1 + NTB2 + NTB4 must equal total revenue
EV: `E7+E8+E10 = 'DRIVER TREE'!M18+'DRIVER TREE'!M24`. If it doesn't,
the NTB mapping is incomplete or double-counting.

Upside EV (G7:H11) is analyst judgment from IC Memo — keep as blue
hardcoded inputs; they are not model-derived.

---

## Step 5 — Build MOIC BRIDGE tab

The bridge is a cumulative waterfall: Entry equity (1.00×) + NTB
contributions + compression + net cash = Exit MOIC.

Column mapping:
- Column C = Equity Value ($M) impact
- Column D = MOIC contribution (Δ×)
- Column E = Cumulative MOIC

```
Row 7:  Entry equity          C7=INPUTS!C21, D7=1, E7=1.00×
Row 8:  NTB-1 GMV             C8='NTB REGISTRY'!E7, D8='NTB REGISTRY'!F7
Row 9:  NTB-2 Payments        C9='NTB REGISTRY'!E8, D9='NTB REGISTRY'!F8
Row 10: NTB-3 AI              C10='NTB REGISTRY'!E9, D10='NTB REGISTRY'!F9
Row 11: NTB-4 Enterprise      C11='NTB REGISTRY'!E10, D11='NTB REGISTRY'!F10
Row 12: NTB-5 FCF             C12=0, D12=0  (not modeled)
Row 13: NTB-6 Macro           C13=0, D13=0  (not modeled)
Row 14: Multiple compression  C14='DRIVER TREE'!L31, D14='DRIVER TREE'!N31
Row 15: Net cash build        C15='DRIVER TREE'!L32, D15='DRIVER TREE'!N32

Cumulative: E8=IFERROR(E7+D8,"-"), E9=IFERROR(E8+D9,"-"), ... E15

Row 16: Exit equity (check)   C16=INPUTS!C30, D16=IFERROR(C30/C21,"-"),
                              E16=IFERROR(C30/C21,"-")
```

E15 and E16 should match. If they diverge by more than ±0.01×, a
formula is broken — audit the chain before saving.

---

## Step 6 — Run quality check (mandatory after every build or edit)

After every build, every formula edit, and every save, run:

```bash
python scripts/quality_check.py <workbook.xlsx> --fix
```

The script checks five dimensions across all tabs and auto-fixes where
it can:

| Check | What it catches | Auto-fix |
|-------|----------------|----------|
| Column widths | Columns too narrow for labels or numbers | Yes — sets to spec |
| Row heights | Wrapped commentary rows truncated | Yes — estimates needed height |
| Number formats | Value cells showing General or @ format | Yes — applies spec format |
| Formula errors | #REF!, #DIV/0!, #VALUE! etc. | No — must fix manually |
| Text overflow | Non-wrapped text visually overflowing column | Report only |

**Column width specs** (defined in `scripts/quality_check.py`):

| Tab | Key columns |
|-----|------------|
| DRIVER TREE | B=34, D=22 (wrap), J-M=12-13 |
| INPUTS | B=40 (label), C=13 (value), E=42 (notes, wrap) |
| KPI TREE | C=32, L=36 (notes, wrap) |
| NTB REGISTRY | D=50 (thesis, wrap), E-H=14 |
| MOIC BRIDGE | B=48 (label), C-E=16 |

**If formula errors are reported**, fix them before delivering. Common
causes:
- Wrong sheet name in cross-sheet reference (check single-quoting of
  multi-word names: `'FINANCIAL MODEL'!...`)
- Row/column offset in FINANCIAL MODEL mapping (re-read the model)
- INPUTS row reference off-by-one (check build script row numbering)
- GMV in $B × attach rate in bps/10000 → multiply by 1000 to get $M
  (the most common unit error)

---

## Quality check: manual visual pass

After the script runs clean, do a visual spot-check in the workbook:

1. **DRIVER TREE row heights**: commentary rows (rows 2-3, row 8, row 14,
   row 35) should be tall enough to show all text without truncation.
2. **NTB REGISTRY thesis col D**: each thesis cell is ~600-800 chars.
   Confirm wrap_text=True and row height ≥ 70pt for data rows 7-11.
3. **MOIC BRIDGE row labels (col B)**: component names are 50-60 chars.
   Confirm col B width ≥ 48 and no truncation.
4. **INPUTS note col E**: each note is 40-100 chars. Confirm wrap and
   row height ≥ 22pt for annotated rows.
5. **DRIVER TREE N column**: verify sign convention — revenue drivers
   should be positive, multiple compression negative, net cash positive.
6. **MOIC check**: open workbook in Excel, navigate to DRIVER TREE
   row 34 col N. Confirm value ≈ INPUTS!C34 ≈ 1.58×. If it shows
   #VALUE! or the wrong number, a formula chain is broken.

---

## Common errors and fixes

### "Why is this cell hardcoded?"
Any cell in DRIVER TREE metric columns (F/G/H), J/L/M/N impact columns,
NTB REGISTRY E/F columns, or MOIC BRIDGE C/D columns that contains a
number literal (not a formula starting with `=`) is hardcoded and wrong.
Trace back through `references/formula-architecture.md` to find the
correct formula and replace it.

### MOIC check ≠ INPUTS!C34
Work backwards:
1. Does N34 = 1+N33? If not, N34 formula is broken.
2. Does N33 = L33/INPUTS!C21? If not, check.
3. Does L33 = L30+L31+L32? If not, check.
4. Is L30 = J30×K30 where J30 = L26 (total EBITDA)? If not, trace L26.
5. Is L26 = L18+L24? Trace L18 and L24.

### NTB1+NTB2+NTB4 ≠ total revenue EV
Check: `'NTB REGISTRY'!E7 + E8 + E10 = 'DRIVER TREE'!M18 + M24`
If not equal, one of the NTB formula assignments is wrong or a driver
row's M column formula is broken.

### Sub revenue doesn't reconcile
J24 (total sub) ≈ INPUTS!C61-C60 via the MRR multiplier approximation.
If the gap is >5%, check:
- C54 (entry MRR from model) vs. C81+C84 (Plus+Core entry MRR hardcodes).
  They should be close. If not, update the hardcoded MRR rows.
- C86 (multiplier = C60/C54). Verify the entry sub rev and MRR references
  are pulling from the right model rows.

### Row heights still truncated after --fix
The auto-fix uses an approximate text-width estimate. For cells with
very long text or unusual font sizes, manually set the row height:
```python
ws.row_dimensions[row_num].height = 80  # e.g., for NTB thesis rows
```

---

## Delivering the workbook

1. Run `python scripts/quality_check.py <file>.xlsx --fix`
2. Confirm 0 formula errors in the output
3. Confirm column width and row height issues are all FIXED
4. Open in Excel, recalculate (Ctrl+Alt+F9), confirm MOIC check ≈ 1.58×
5. Save file to the deal folder, version as vN+1

The workbook is not complete until quality_check.py exits 0 and the
MOIC check passes.
