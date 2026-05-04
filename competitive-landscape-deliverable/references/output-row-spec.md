# Executive Deliverable — Output Row Specification

The `Executive Deliverable` sheet has a fixed row order. Each row maps to one or more raw fields from the source `Competitive Landscape` sheet. The engine script (`scripts/build_deliverable.py`) implements this as `SYNTHESIS_MAP`.

## Top block (rows 1–6)

| Row | Col A | Col B | Col C+ (per company) |
|---|---|---|---|
| 1 | (merged) | `Competitive Landscape — Executive View` | (title band, white on `#0F4761`) |
| 2 | (merged) | `Concise strategic readout from detailed research` | (subtitle) |
| 3 | `Verdict` | `Recommendation` | ACQUIRE / MONITOR / PASS (color-coded) |
| 4 | | `Recommended posture` | 7–10-word phrase |
| 5 | | `Score (moat / fit / ma)` | `XX / X.X / X.X` |
| 6 | | `Acquisition thesis` | 10–14-word one-liner |

Freeze panes at `C7`.

## Section 1 — Market taxonomy (~11 rows)

| Output label | Source fields |
|---|---|
| Value chain stage | Commerce Value Chain Stage |
| Category and subcategory | Primary Category + Sub-Category |
| Workflow layer | Workflow Layer + Primary Use Case |
| Buyer and ICP focus | Buyer Segment + Primary ICP |
| Secondary buyer segment | Secondary ICP + Buyer Segment |
| Customer scale focus | Customer Scale Focus + Enterprise Customer Count |
| Geography served | Geography Served + HQ Country |
| Platform ecosystem | Platform Ecosystem + Native Platform Integrations |
| Channel focus | Channel Focus + Sales Motion + Partner Motion |
| Category maturity | Category Maturity + Category Leadership Position |
| Market tailwinds | Market Tailwind Tags + White-Space Relevance |

## Section 2 — Product capability (~17 rows)

| Output label | Source fields |
|---|---|
| Core product wedge | Core Product Description + Primary Use Case |
| Primary use case | Primary Use Case + Workflow Criticality |
| Key feature set | Key Features + Core Product Description |
| Differentiated capability | Differentiated Features + Competitive Differentiation |
| AI and agent posture | AI Capability + Agentic Capability |
| API and protocol maturity | Agent-Callable API Availability + Protocol Support + API Documentation Quality |
| Integration breadth | Integration Breadth + Native Platform Integrations |
| Commerce platform depth | Native Platform Integrations + Platform Ecosystem |
| Enterprise systems depth | ERP/OMS/WMS Integrations + Implementation Model |
| Payments and carrier depth | Payment/PSP Integrations + Carrier Integrations |
| Implementation model | Implementation Model + Estimated Time to Value |
| Time to value | Estimated Time to Value + Implementation Model |
| Workflow criticality | Workflow Criticality + Workflow Criticality if Removed |
| System-of-record role | System of Record Status + Owns Operational Records |
| Operational record ownership | Owns Operational Records + Data Captured |
| Switching cost driver | Switching Cost Driver + Switching Cost Score |
| Removal impact | Workflow Criticality if Removed + Replacement Risk |

## Section 3 — Data and compliance (~10 rows)

| Output label | Source fields |
|---|---|
| Data captured | Data Captured + Owns Operational Records |
| PII and sensitivity exposure | PII Exposure + Data Sensitivity Tier |
| PCI and payment exposure | PCI Exposure + Payment/PSP Integrations |
| Security posture | SOC 2 Status + Security Risk Level |
| Privacy readiness | GDPR/CCPA Readiness + Data Retention Policy |
| AI and product compliance | EU AI Act Exposure + ESPR Exposure |
| Cross-retailer data use | Cross-Retailer Data Usage + Data Network Effect |
| Data network effect | Data Network Effect + Data Network Score |
| Compliance risk notes | Compliance Risk Notes + Security Risk Level |
| Data retention posture | Data Retention Policy + Compliance Risk Notes |

## Section 4 — Commercial traction (~16 rows)

| Output label | Source fields |
|---|---|
| Revenue scale | Estimated ARR/Revenue + Estimated Enterprise Value |
| Growth trajectory | Revenue Growth Rate + Hiring Velocity |
| Customer proof | Customer Count + Notable Customers |
| Enterprise penetration | Enterprise Customer Count + Primary ICP |
| Notable customer signal | Notable Customers + Customer Scale Focus |
| Transaction volume signal | GMV/Order/Shipment Volume + Customer Count |
| Retention quality | Retention/NRR + Gross Retention |
| Churn risk | Churn Risk + Gross Retention |
| ACV range | ACV Range + Pricing Model |
| Pricing model | Pricing Model + Usage-Based Pricing Exposure |
| Usage pricing exposure | Usage-Based Pricing Exposure + GMV/Order/Shipment Volume |
| Margin profile | Gross Margin Estimate + Implementation Model |
| Sales motion | Sales Motion + Sales Cycle Length |
| Sales cycle | Sales Cycle Length + ACV Range |
| Partner motion | Partner Motion + Channel Focus |
| Marketplace presence | App Store/Marketplace Presence + Platform Ecosystem |

## Section 5 — Competitive position (~16 rows)

| Output label | Source fields |
|---|---|
| Direct competitor set | Direct Competitors + Primary Category |
| Substitute pressure | Substitute Competitors + Replacement Risk |
| Platform-native threat | Platform-Native Threats + Platform Lock-In Score |
| Differentiation angle | Competitive Differentiation + Differentiated Features |
| Competitive weakness | Competitive Weakness + Red Flags |
| Moat type | Moat Type + Total Moat Score |
| Data network strength | Data Network Score + Data Network Effect |
| Switching cost strength | Switching Cost Score + Switching Cost Driver |
| Platform lock-in strength | Platform Lock-In Score + Native Platform Integrations |
| Regulatory or liability moat | Regulatory/Liability Score + Compliance Risk Notes |
| Physical network moat | Physical Network Score + Fit with Pattern Fulfillment Network |
| Overall moat score | Total Moat Score + Moat Durability |
| Moat durability | Moat Durability + Replacement Risk |
| Replacement risk | Replacement Risk + Substitute Competitors + Platform-Native Threats |
| Category leadership | Category Leadership Position + Category Maturity |
| White-space relevance | White-Space Relevance + Market Tailwind Tags |

## Section 6 — Pattern fit (~12 rows)

| Output label | Source fields |
|---|---|
| Strategic relevance | Pattern Strategic Relevance + Strategic Fit Score |
| Capability fit | Fit with Pattern Capabilities + New Capability Unlocked |
| Customer base fit | Fit with Pattern Customer Base + Cross-Sell Potential |
| Data asset fit | Fit with Pattern Data Assets + Data Captured |
| Fulfillment network fit | Fit with Pattern Fulfillment Network + Carrier Integrations |
| AI strategy fit | Fit with Pattern AI/Agent Strategy + AI Capability |
| Cross-sell potential | Cross-Sell Potential + Revenue Synergy Potential |
| Product integration potential | Product Integration Potential + Integration Breadth |
| Revenue synergy potential | Revenue Synergy Potential + Fit with Pattern Customer Base |
| Cost synergy potential | Cost Synergy Potential + Implementation Model |
| Defensive value | Defensive Value + Platform-Native Threats |
| New capability unlocked | New Capability Unlocked + Capability Fit |

## Section 7 — M&A lens (~14 rows)

| Output label | Source fields |
|---|---|
| Acquisition thesis | Acquisition Thesis + Pattern Strategic Relevance |
| Build-buy-partner stance | Build/Buy/Partner Recommendation + Deal Priority |
| Deal priority | Deal Priority + Strategic Fit Score |
| Valuation signal | Estimated Enterprise Value + Estimated Revenue Multiple |
| Comparable transaction signal | Comparable Transactions + Estimated Revenue Multiple |
| Funding and investor context | Funding Raised + Last Funding Round + Key Investors |
| Exit pressure | Investor Pressure/Exit Likelihood + Seller Motivation |
| Seller motivation | Seller Motivation + Likely Process Timing |
| Cap table complexity | Cap Table Complexity + Key Investors |
| Process timing | Likely Process Timing + Pipeline Status |
| Acquisition difficulty | Acquisition Difficulty + Integration Complexity |
| Integration complexity | Integration Complexity + Product Integration Potential |
| Diligence risk | Diligence Risk + Compliance Risk Notes + Data Sensitivity Tier |
| Red flags | Red Flags + Competitive Weakness + Churn Risk |
| Open diligence question | Key Open Questions + Diligence Risk |

## Section 8 — Pipeline operations (~12 rows)

| Output label | Source fields |
|---|---|
| Pipeline status | Pipeline Status + Deal Owner |
| Deal ownership | Deal Owner + Relationship Strength |
| Research ownership | Research Owner + Human Review Status |
| Review freshness | Last Reviewed Date + Last Updated Date |
| Outreach recency | Last Outreach Date + Relationship Strength |
| Recommended next action | Next Action + Build/Buy/Partner Recommendation |
| Next action owner | Next Action Owner + Deal Owner |
| Target contact | Target Contact + Key Executives |
| Relationship strength | Relationship Strength + Intro Path |
| Intro path | Intro Path + Relationship Strength |
| Evidence quality | Evidence Links + Source Confidence Score |
| Human review status | Human Review Status + Agent-Generated Summary |
