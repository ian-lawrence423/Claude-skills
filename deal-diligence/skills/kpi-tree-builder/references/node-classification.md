# Node Classification

Use this file to classify every node in the KPI tree consistently.

## Required fields for every node

Each node should be assigned:
- node type
- signal class
- owner
- frequency
- controllability
- variance lens
- evidence status

## 1. Node type

### Output
The top financial or operating metric being explained.

Examples:
- Revenue
- Gross profit
- EBITDA
- Cash flow

### Driver
A meaningful branch that explains a material portion of the outcome.

Examples:
- New logo revenue
- Gross retention
- Pricing
- Utilization
- Working capital

### Atomic input
A direct measurable input that should be observable in a reporting process.

Examples:
- opportunities created
- win rate
- average deal size
- implementation lag
- churned customers
- billed usage units

### Derived metric
A calculated measure that combines other nodes and is useful diagnostically.

Examples:
- net retention
- pipeline coverage
- realized ASP
- contribution margin

## 2. Signal class

### Leading
Moves before the outcome moves.

Examples:
- pipeline created
- implementation starts
- customer health scores
- collections delinquency flags

### Coincident
Moves roughly with the outcome.

Examples:
- bookings
- billable usage
- recognized revenue in-month

### Lagging
Observed after performance is already set or mostly set.

Examples:
- quarter-end EBITDA
- fully reported churn
- quarterly cash flow

## 3. Owner

Assign a function or named operating owner.

Common owners:
- Sales
- Marketing
- Customer success
- Operations
- Product
- Finance
- Revenue operations
- Implementation
- Collections / AR
- General manager / BU lead

A node without an owner is incomplete.

## 4. Frequency

Assign the tightest realistic cadence:
- daily
- weekly
- monthly
- quarterly

Use weekly for early-warning indicators.
Use monthly for realized financial and operating outputs.
Use quarterly for strategic and structural review metrics.

## 5. Controllability

### High
Management can directly influence the metric in the near term.

Examples:
- rep activity
- discount approval
- staffing level
- collections cadence

### Medium
Management influences the metric, but with lag or only indirectly.

Examples:
- churn
- mix
- expansion
- implementation speed

### Low
Mostly external or difficult to influence in the short term.

Examples:
- FX
- regulation
- macro demand shocks

## 6. Variance lens

Every node should map to one primary variance lens:
- volume
- conversion
- price / rate
- retention
- mix
- productivity
- timing / realization
- external
- one-time item

This is required to make later variance work consistent.

## 7. Evidence status

Use one of:
- historical
- management estimate
- diligence hypothesis
- observed post-close

This is especially important in diligence mode.

## Decision rules

### When is a node not deep enough?
A node is not deep enough if:
- it cannot be measured,
- it has no owner,
- it cannot be acted on,
- it hides multiple effects inside one label,
- it is just a management phrase rather than a real KPI.

### When is a node too deep?
A node is too deep if:
- it is no longer managerially useful,
- it cannot be observed reliably,
- it becomes system-specific rather than decision-useful,
- it adds noise without improving actionability.

### How to choose between two decompositions
Prefer the decomposition that:
1. is more causal,
2. better separates distinct economic effects,
3. is more trackable,
4. is easier to assign to an owner,
5. is more useful in management review.

## Example classification

### Example: New logo recurring revenue
- node type: driver
- signal class: coincident
- owner: sales
- frequency: monthly
- controllability: high
- variance lens: volume / conversion
- evidence status: historical + management estimate

### Example: Win rate
- node type: atomic input
- signal class: leading
- owner: sales
- frequency: weekly
- controllability: medium
- variance lens: conversion
- evidence status: historical

### Example: Average discount rate
- node type: atomic input
- signal class: coincident
- owner: sales / finance
- frequency: weekly or monthly
- controllability: high
- variance lens: price / rate
- evidence status: historical
