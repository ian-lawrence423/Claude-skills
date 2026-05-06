---
name: kpi-tree-builder
description: build, audit, and maintain company-specific kpi trees that decompose a budget, forecast, or operating target into causal drivers and atomic inputs. use when a user wants to break revenue, margin, opex, headcount, cash flow, or other plan lines into measurable drivers; create a diligence-ready budget framework; translate a model into operating inputs; or define what should be tracked weekly and monthly post-close. especially useful in late diligence, annual planning, monthly business reviews, and post-acquisition operating cadence design.
---

Build KPI trees that connect financial outcomes to measurable operational inputs.

The purpose of this skill is to turn a budget, forecast, or target metric into a usable operating architecture. The output must help the user:
1. understand how the plan is built,
2. identify what has to go right,
3. see which drivers management controls,
4. define what should be tracked over time,
5. convert underwriting assumptions into an operating cadence.

## Core principle

Always decompose:

**Outcome -> driver -> sub-driver -> atomic input**

Stop only when the input is:
- directly measurable,
- owned by a function,
- observable at a reporting cadence,
- usable in budget setting or tracking.

Do not stop at vague labels like "sales productivity", "retention", or "utilization". Keep decomposing until each branch can be defined operationally.

## What this skill owns

This skill owns:
- KPI tree design
- budget decomposition
- driver logic and formulas
- mapping financial outcomes to operating inputs
- owner and cadence assignment
- conversion of budget assumptions into tracking metrics
- identification of leading and lagging indicators

This skill is responsible for the structure of the tree itself. Keep the work focused on decomposition, classification, reconciliation, and tracking architecture.

## When given a model, spreadsheet, or existing budget tree

If the user provides a model or budget tree:
1. identify the target output line,
2. trace the logic into major branches,
3. translate technical model labels into business language,
4. identify where the current tree is causal vs. presentation-only,
5. tighten the tree into mutually exclusive, economically coherent branches,
6. add missing operating inputs needed for tracking,
7. propose a cleaner management version of the tree.

Preserve useful structure, but do not mirror a management model blindly if the structure is not causal.

## Two operating modes

### Mode 1: diligence / budget-underwrite mode
Use this when the user is evaluating whether a management budget is credible.

In this mode:
- reconstruct the plan logic from output to inputs,
- identify explicit and hidden assumptions,
- test whether branches reconcile mathematically,
- flag where assumptions are unsupported or too aggregated,
- identify which assumptions need confirmatory diligence,
- define which inputs should be tracked post-close.

Always ask:
- what has to be true for this budget to be achieved?
- which assumptions are volume, conversion, price, retention, mix, productivity, or timing?
- which are supported by historical evidence?
- which are management estimates?
- which are measurable leading indicators?

### Mode 2: post-close / operating management mode
Use this when the user wants a tree that can be tracked over time.

In this mode:
- convert the plan tree into a management operating tree,
- separate structural drivers from noise,
- specify weekly, monthly, and quarterly metrics,
- define early-warning indicators,
- attach owners,
- make the tree usable in monthly business reviews.

Always ask:
- what is the earliest signal that this branch is off plan?
- who owns the metric?
- how should a miss be diagnosed?
- what management action follows from that miss?

## Build sequence

Follow this sequence.

### Step 1: define the target metric
Start with the outcome the user cares about:
- revenue
- arr / mrr
- gross profit
- contribution margin
- ebitda
- cash flow
- net working capital
- headcount productivity
- any company-specific operating target

State:
- exact metric,
- time period,
- unit,
- budget / forecast / actual context.

### Step 2: select decomposition logic
Choose the right decomposition based on the business model.

Common patterns are in `references/decomposition-patterns.md`.

If the business is hybrid, build separate trees by revenue or cost stream first, then roll them up.

### Step 2b: apply SaaS GTM decomposition when relevant

For B2B SaaS, recurring software, or other GTM-driven businesses, combine the economic decomposition in `references/decomposition-patterns.md` with the GTM metric system in `references/example-output-gtm-kpi-tree.md`.

For these businesses, do not stop the tree at generic branches such as:
- sales productivity
- retention
- customer health
- pipeline
- efficiency

Instead, decompose those branches into explicit GTM metrics when relevant, including:

- ARR funnel metrics:
  - Beginning ARR
  - Gross New ARR
  - New Logo ARR
  - Expansion ARR
  - Downsell
  - Logo Churn
  - Net New ARR
  - Ending ARR

- Funnel and pipeline metrics:
  - MEL, MQL, SAL, SQL
  - Opportunities
  - Pipeline $
  - Weighted Pipeline $
  - Pipeline Coverage
  - Weighted Pipeline Coverage
  - Cycle Time
  - Win Rate
  - Close Rate
  - Average Deal Size / ACV
  - Forecast as % of Sales Target
  - Forecast as % of Capacity

- Retention and health metrics:
  - Net Dollar Retention
  - Gross Dollar Retention
  - Logo Retention
  - Logo Churn Rate
  - Cohort NDR
  - Churn and lost reasons
  - Active User Rate
  - Adoption Rate
  - Time to Implement vs Goal
  - NPS / CES / CSAT

- Efficiency and economics metrics:
  - Gross Margin
  - Net Magic Number
  - Gross Magic Number
  - CAC
  - LTV
  - LTV / CAC
  - Payback Period

- Team productivity metrics:
  - S&M OpEx per S&M FTE
  - NNARR per S&M FTE
  - Sales Capacity
  - Quota Attainment
  - Ramp Rate

Use these metrics only where they improve causal clarity. Do not force every metric into every tree. Prefer the smallest tree that still explains the outcome and supports management action.

### Step 3: force economic buckets
Every major branch must be classified into one of:
- volume
- conversion
- price / rate
- retention
- mix
- productivity
- timing / realization
- external / non-operating
- one-time item

This is mandatory. It makes later tracking and diagnostic work consistent.

### Step 4: decompose to atomic inputs
For each branch, keep drilling down until inputs are:
- measurable,
- owned,
- trackable,
- actionable.

Use `references/node-classification.md` to decide whether the decomposition has gone deep enough.

For GTM-driven businesses, a node is not deep enough if it cannot be mapped to a defined operational metric or formula.

Examples of valid GTM atomic inputs:
- Pipeline Coverage
- Win Rate
- Close Rate
- Average Deal Size
- Net Dollar Retention
- Gross Dollar Retention
- Logo Churn Rate
- CAC
- Gross Margin
- Sales Capacity
- Quota Attainment
- Ramp Rate

Avoid stopping at labels like:
- sales execution
- customer health
- pipeline quality
- commercial efficiency

Those labels are too broad unless they are decomposed into measurable sub-metrics.

### Step 5: classify each node
For every node, assign:
- node type: output / driver / atomic input / derived
- signal class: leading / coincident / lagging
- owner
- frequency
- controllability: high / medium / low
- variance lens
- evidence status: historical / management estimate / diligence hypothesis / observed post-close

### Step 6: reconcile math
The tree must reconcile bottom-up and top-down.

Always:
- show formulas where possible,
- separate assumptions from derived metrics,
- identify balancing items,
- flag circular logic,
- flag overlap or double-counting,
- flag unexplained plugs.

### Step 7: define the tracking architecture
Translate the tree into a tracking cadence.

Typical rule:
- weekly = early-warning indicators and flow metrics
- monthly = realized outputs and core driver KPIs
- quarterly = structural and strategic reviews

Use `references/tracking-architecture.md` to specify cadence, owners, and management actions.

## Output requirements

Default to this structure.

### A. top-line summary
State:
- target metric
- decomposition logic used
- biggest branches
- key takeaways
- key underwriting or operating implications

### B. KPI tree
Present as an indented tree.

For formatting, labeling, and depth, use `references/example-output-revenue-tree.md` as the default example.

When the company is a B2B SaaS or GTM-driven business, also use `references/example-output-gtm-kpi-tree.md` as a default example for full-funnel and operating-metric decomposition.

### C. driver dictionary
For each node, include:
- node
- parent node
- definition
- formula
- unit
- owner
- cadence
- leading / lagging
- controllability
- variance lens
- evidence source
- comments

### D. diligence view
If in diligence mode, include:
- explicit assumptions
- hidden assumptions inferred from the model
- unsupported assumptions
- branches that require confirmatory diligence
- branches that must be tracked post-close

### E. tracking pack
Recommend a focused set of:
- weekly metrics
- monthly metrics
- quarterly metrics

The weekly list must only contain early-warning indicators.

## Mandatory operating rules

### Rule 1: prefer causality over presentation logic
Do not preserve a hierarchy just because it exists in a deck or model. Rebuild around economic logic.

### Rule 2: separate stock and flow
Distinguish:
- beginning stock,
- in-period flow,
- ending stock.

### Rule 3: separate bookings, activation, billing, and recognition
Do not collapse booked, live, billable, and recognized value into one node.

### Rule 4: separate churn, contraction, and expansion
Do not hide them inside net retention if the user is trying to manage the business.

### Rule 5: break mix out explicitly
If segment, product, geography, channel, or cohort mix matters, create a mix branch.

### Rule 6: separate controllable from non-controllable
External effects such as FX, regulation, or one-time timing items should not be mixed into management-controlled performance.

### Rule 7: force ownership
A KPI tree without owners is incomplete.

### Rule 8: make it trackable
If a node cannot be measured, say so and propose the closest practical proxy.

## Integration with adjacent skills

### driver-tree
`driver-tree` decomposes an investment thesis into causal drivers for IC memo purposes — revenue, cost, capital, and competitive dynamics — and maps each driver to NTBs and MOIC outcomes. `kpi-tree-builder` operates downstream of that: it converts the same causal structure into a trackable operating architecture with owners, cadences, and management actions. In a PE deal workflow, run `driver-tree` during diligence to build the thesis structure, then run `kpi-tree-builder` post-close to convert it into the operating model management tracks.

### ntb-diligence
`ntb-diligence` identifies what must be true for the investment thesis to hold and flags which assumptions are unconfirmed. The diligence mode of `kpi-tree-builder` is the mechanism for resolving those gaps — the atomic inputs in the KPI tree are the measurable things that confirm or refute each NTB. When ntb-diligence has produced a GAP item, the kpi-tree-builder diligence view should map that gap to the specific tree node that resolves it.

## Interaction with gtm-metrics-analyzer

`gtm-metrics-analyzer` is the measurement and calculation companion to this skill.

Use `kpi-tree-builder` to design the operating architecture:
- outcome
- drivers
- sub-drivers
- atomic inputs
- tracking cadence

Use `gtm-metrics-analyzer` to calculate and interpret the GTM metrics that sit inside those nodes:
- ARR funnel metrics
- pipeline and conversion metrics
- retention metrics
- efficiency metrics
- productivity metrics
- attainment and forecast metrics

This skill may name the metric nodes that should exist in the tree, but it should not perform the full metric-calculation workflow owned by `gtm-metrics-analyzer`.

## Success standard

A good output should let the user answer:
- how is this plan actually built?
- what has to go right?
- which assumptions are fragile?
- which inputs are leading indicators?
- what should management track weekly, monthly, and quarterly?
- who owns each branch?
- where should diligence focus?
