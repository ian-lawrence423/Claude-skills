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
        ▼
DRIVER TREE
  Metric cols (F/G/H) = INPUTS formula refs
  Delta col (I)        = H - G
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
