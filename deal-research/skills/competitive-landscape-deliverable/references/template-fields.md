# Pattern Competitive Landscape Template — Field Map

The Pattern competitive landscape workbook uses a 9-section structure with field labels in column B and company data from column C onward. Each analytic cell is formatted as `"Rating value — McKinsey-style rationale"` (em-dash separator) when produced by the n8n orchestrator pipeline.

Sheet name: `Competitive Landscape`

## 1. Entity identity (rows 5–21)
- Company Name
- Legal Entity Name
- Website
- LinkedIn URL
- Crunchbase / PitchBook URL
- HQ Country
- HQ City
- Founded Year
- Company Status
- Ownership Type
- Parent Company
- Key Executives
- Founder Status
- Employee Count
- Hiring Velocity
- Last Updated Date
- Source Confidence Score

## 2. Market taxonomy (rows 23–35)
- Commerce Value Chain Stage
- Primary Category
- Sub-Category
- Workflow Layer
- Buyer Segment
- Primary ICP
- Secondary ICP
- Customer Scale Focus
- Geography Served
- Platform Ecosystem
- Channel Focus
- Category Maturity
- Market Tailwind Tags

## 3. Product capability (rows 37–57)
- Core Product Description
- Primary Use Case
- Key Features
- Differentiated Features
- AI Capability
- Agentic Capability
- Agent-Callable API Availability
- Protocol Support
- API Documentation Quality
- Integration Breadth
- Native Platform Integrations
- ERP / OMS / WMS Integrations
- Payment / PSP Integrations
- Carrier Integrations
- Implementation Model
- Estimated Time to Value
- Workflow Criticality
- System of Record Status
- Owns Operational Records
- Switching Cost Driver
- Workflow Criticality if Removed

## 4. Data and compliance (rows 59–71)
- Data Captured
- PII Exposure
- Data Sensitivity Tier
- PCI Exposure
- SOC 2 Status
- GDPR / CCPA Readiness
- EU AI Act Exposure
- ESPR Exposure
- Data Retention Policy
- Cross-Retailer Data Usage
- Data Network Effect
- Security Risk Level
- Compliance Risk Notes

## 5. Commercial traction (rows 73–89)
- Estimated ARR / Revenue
- Revenue Growth Rate
- Customer Count
- Enterprise Customer Count
- Notable Customers
- GMV / Order / Shipment Volume
- Retention / NRR
- Gross Retention
- Churn Risk
- ACV Range
- Pricing Model
- Usage-Based Pricing Exposure
- Gross Margin Estimate
- Sales Motion
- Sales Cycle Length
- Partner Motion
- App Store / Marketplace Presence

## 6. Competitive position (rows 91–106)
- Direct Competitors
- Substitute Competitors
- Platform-Native Threats
- Competitive Differentiation
- Competitive Weakness
- Moat Type
- Data Network Score
- Switching Cost Score
- Platform Lock-In Score
- Regulatory / Liability Score
- Physical Network Score
- Total Moat Score
- Moat Durability
- Replacement Risk
- Category Leadership Position
- White-Space Relevance

## 7. Strategic fit for Pattern (rows 108–120)
- Pattern Strategic Relevance
- Fit with Pattern Capabilities
- Fit with Pattern Customer Base
- Fit with Pattern Data Assets
- Fit with Pattern Fulfillment Network
- Fit with Pattern AI / Agent Strategy
- Cross-Sell Potential
- Product Integration Potential
- Revenue Synergy Potential
- Cost Synergy Potential
- Defensive Value
- New Capability Unlocked
- Strategic Fit Score

## 8. M&A attractiveness (rows 122–139)
- Acquisition Thesis
- Build / Buy / Partner Recommendation
- Deal Priority
- Estimated Enterprise Value
- Estimated Revenue Multiple
- Comparable Transactions
- Funding Raised
- Last Funding Round
- Key Investors
- Investor Pressure / Exit Likelihood
- Seller Motivation
- Cap Table Complexity
- Likely Process Timing
- Acquisition Difficulty
- Integration Complexity
- Diligence Risk
- Red Flags
- Key Open Questions

## 9. Pipeline operations (rows 141–155)
- Pipeline Status
- Deal Owner
- Research Owner
- Last Reviewed Date
- Last Outreach Date
- Next Action
- Next Action Owner
- Target Contact
- Relationship Strength
- Intro Path
- Source of Lead
- Evidence Links
- Internal Notes
- Agent-Generated Summary
- Human Review Status

## Cell format

When the source is the Pattern n8n orchestrator output, every analytic cell follows:

```
<rating> — <rationale>
```

Where:
- `<rating>` is a categorical value (e.g., `Yes`, `Strong`, `Tier B`, `4`) or short list
- ` — ` is an em-dash separator (U+2014) with single spaces
- `<rationale>` is a 1-sentence McKinsey-style claim+evidence justification (~12–25 words)

Example:
```
Partial — owns return and exchange records but synchronizes core order data from Shopify and OMS upstream
```

Free-text fields (Company Name, Notable Customers, etc.) typically have no em-dash and are passed through.

Numeric score fields (Total Moat Score, Strategic Fit Score, Data Network Score, etc.) may either appear as bare numbers or as `"4 — rationale"`. The engine script handles both.
