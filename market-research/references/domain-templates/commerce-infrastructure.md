# Commerce Infrastructure Domain Template

**Load this file when running market research on digital commerce infrastructure.**

This template encodes Pattern's accumulated analytical context for the digital commerce
infrastructure market: the seven-stage value chain framing, data sensitivity tiering,
vendor universe with known data points, analytical guardrails developed across prior
research iterations, and the deep dive document structure calibrated to this market.

Loading this file activates deep dive mode automatically. Do not run standard mode
for commerce infrastructure research without explicit confirmation from Ian.

---

## 1. The Seven-Stage Digital Commerce Value Chain

This is the governing analytical frame for all commerce infrastructure research.
Every vendor, market size, and competitive analysis must be mapped to a specific
stage. Cross-stage analysis requires explicit labeling of which stages are included
and why.

```
Stage 1 — Discovery & Awareness         (out of scope unless specified)
Stage 2 — Demand Generation             (out of scope unless specified)
Stage 3 — Product Data & Merchandising  (out of scope unless specified)
Stage 4 — Cart & Checkout               ← in scope when specified
Stage 5 — Order Fulfillment             ← in scope when specified
Stage 6 — Post-Purchase Experience      ← in scope when specified
Stage 7 — Retention & Loyalty           (adjacent — note if vendors span S6/S7)
```

**Scope declaration rule:** Every research report must declare which stages are in
scope in the first paragraph of the market sizing section. Mixed-stage analysis must
use separate market sizing frames per stage — never aggregate into a single blended
number without labeling it explicitly as a Pattern internal composite.

**Stage boundary enforcement:**
- Stage 4 ends at order confirmation. Post-confirmation workflows are Stage 5 or 6.
- Stage 5 covers fulfillment, OMS, routing, WISMO, and demand forecasting.
- Stage 6 covers tracking, returns management, return fraud, and agentic resolution.
- Stage 7 (retention/loyalty) is adjacent — flag when vendors span S6/S7 (e.g., Yotpo).
- WISMO/CX AI tools (Gorgias, eDesk) span Stage 5 and 6 — label their stage coverage
  explicitly rather than assigning them to one stage only.

---

## 2. Data Sensitivity Tiering Framework

Pattern's proprietary analytical lens for commerce infrastructure diligence.
Apply to any vendor assessment, DDR scoping, or risk analysis in this market.

| Bucket | Stage | Data Sensitivity | Typical PII & Data Captured | Diligence Implication |
|--------|-------|-----------------|---------------------------|----------------------|
| 1. Discovery | S1 | Low (1–2) | Anonymous IP, search queries, device types | Low churn risk; data non-identifiable at individual level |
| 2. Demand Gen | S2 | High (4) | Email, phone, social handles, purchase intent signals | TCPA (SMS) and GDPR/CCPA regulatory exposure; high frequency write |
| 3. Product Data | S3 | Low (1–2) | SKU metadata, pricing, inventory levels, imagery | Performance/latency risk; data is public-facing |
| 4. Cart & Checkout | S4 | Critical (5) | Full PCI data: credit card tokens, CVV, billing addresses, SSNs (BNPL) | System of Record: total merchant dependency. Require SOC2 Type II + PCI-DSS Level 1. Uptime SLA ≥99.99% |
| 5. Order Fulfillment | S5 | Critical (5) | Full recipient names, physical home addresses, phone numbers, order contents | Operational backbone: essential for physical execution. GDPR right-to-erasure complexity on physical fulfillment records |
| 6. Post-Purchase | S6 | Medium (3–4) | Tracking numbers, return reasons, support transcripts, fraud behavior signals | Brand equity: owns "emotional" data of customer journey. Cross-retailer reuse rights require explicit data governance audit |
| 7. Retention | S7 | Medium (3) | Loyalty balances, birthday/anniversary, referral history, communication preferences | Growth asset: high-value behavioral data for 1P advertising; data retention policy audit required |

**Diligence check triggers:**
- Any S4/S5 vendor: require SOC2 Type II + PCI-DSS Level 1 compliance documentation
- Any S6 vendor with cross-retailer data network: audit data reuse rights, GDPR/CCPA
  "right to be forgotten" automation, and consent framework for cross-brand usage
- Any AI agent product (S5/S6): EU AI Act risk classification assessment (effective Aug 2026)
- Any consumer-funded coverage model (Redo, Route): state-by-state insurance licensing
  status — this is not a solved regulatory question

---

## 3. Evidence & Arithmetic Guardrails

These rules were developed across prior research iterations to prevent the most common
analytical errors in commerce infrastructure market sizing. Apply them before writing
any market sizing claim.

### Three evidence categories — label every figure

| Label | What qualifies | How to use |
|-------|---------------|------------|
| Official/Primary | Company filings, regulator publications, NRF, Shopify annual data, Baymard | Market structure, product capability, regulatory scope, operational benchmarks |
| Vendor/Commissioned | Vendor marketing, PR, commissioned TEI studies, self-reported metrics | Product positioning and directional customer value — not independent market sizing |
| Pattern Analytic | Internal constructions, scenario cases, bridge estimates | Label separately; never sum with consensus market figures without disclosure |

### CAGR arithmetic check — mandatory before publishing any growth rate

Before including any CAGR in the report, verify the math:
- Start value × (1 + CAGR)^years = End value
- If the implied end value differs from the stated end value by >5%, flag and correct
- Document every correction in Appendix A

**Known corrections from prior iterations (do not repeat these errors):**
- Stage 4: ~$3.0B → ~$5.4B by 2028 at ~22% CAGR (not $6.5B — that implied ~29%)
- Stage 6: ~$5.2B → ~$9.0B at ~20% CAGR (base case); ~$11.5B is aggressive case, not base
- Combined 4+5+6 blended total: do not use as an underwriting anchor — use stage-specific frames

### Market definition consistency rule

Every market sizing statement must use the same definition from start to finish.
Three common definition failures in this market:
1. **Total returns vs. e-commerce returns:** US total returns = $850B (NRF); US e-commerce
   returns = $280B. The capture rate framing changes materially — state which base.
2. **Software-pure vs. total market:** OMS total market includes legacy on-premise;
   AI-native SaaS sub-segments grow 3× faster. Always separate the two views.
3. **Reference market vs. Pattern analytic slice:** Externally sized markets and
   Pattern-defined analytic constructions must be labeled separately and never summed
   without disclosure.

### Agentic upside — treat separately

Agentic commerce TAM (AI agent-initiated orders, autonomous resolution) is not yet
independently sized by any analyst firm. Pattern internal estimate only. Label as
[Pattern Analytic] and show separately from base case market sizing — never include
in base case without explicit disclosure.

---

## 4. Known Market Sizing (as of March 2026)

Reference figures from the Commerce v8 research. Update with web search for any
figure more than 6 months old. Label every figure with source and confidence level.

### Stage 4: Cart & Checkout

| Frame | 2025E | 2028E | CAGR | Source | Confidence |
|-------|-------|-------|------|--------|------------|
| Payment orchestration reference market | $2.65B | ~$4.4B | 18.3% | Mordor Intelligence | M |
| Software-pure analytic view (orchestration + checkout optimization SaaS) | ~$3.0B | ~$5.4B | ~22% | Pattern composite | L |
| BNPL integration layer | Adjacency | Adjacency | N/A | Excluded from base | — |
| Checkout-layer fraud | Adjacency | Adjacency | N/A | Shown separately | — |

### Stage 5: Order Fulfillment

| Frame | 2025E | 2028E | CAGR | Source | Confidence |
|-------|-------|-------|------|--------|------------|
| OMS reference market (total, incl. legacy) | $6.8B | ~$8.8B | 8% | Virtue Market Research 2025 | M |
| AI-native composite (AI routing + demand forecasting + WISMO AI) | ~$4.8B | ~$9.2B | ~24% | Pattern composite (weighted sub-segment) | L |

*Note: 24% CAGR reflects AI-native sub-segments only (AI routing ~26%, demand forecasting
~26%, WISMO AI ~33%) weighted by estimated sub-segment size. Do not apply 24% to the
full OMS reference market.*

### Stage 6: Post-Purchase Experience

| Frame | 2025E | 2028E | CAGR | Source | Confidence |
|-------|-------|-------|------|--------|------------|
| Base case (tracking + returns mgmt + fraud + agentic resolution) | ~$5.2B | ~$9.0B | ~20% | Pattern composite | L |
| Aggressive case | ~$5.2B | ~$11.5B | ~30% | Pattern internal | L |
| Agentic upside (separate) | ~$1.5B+ | N/A | N/A | Pattern internal only | L |

### Sub-segment growth rates (AI-native vs. legacy)

AI-native sub-segments grow 3–4× the total market rate. Use these when analyzing
specific vendor categories:
- AI routing / order optimization: ~26% CAGR
- Demand forecasting AI: ~26% CAGR
- WISMO / AI customer resolution: ~33% CAGR
- Returns management software: ~20% CAGR (base)
- Return fraud prevention: fastest growing, no consensus size yet

### Geography

| Region | OMS Share | PPX Share | Growth Outlook | Key Dynamic |
|--------|-----------|-----------|----------------|-------------|
| North America | ~40% | ~40% | Steady leader | Largest enterprise OMS installed base; highest return rates (~18% e-comm) |
| Europe | ~27% | ~25% | Accelerating | GDPR mature operating constraint; ESPR tailwind for returns disposition |
| Asia-Pacific | ~25% | ~22% | Fastest (~12.7% CAGR) | Mobile-first (80% of transactions); same-day fulfillment baseline |
| Rest of World | ~8% | ~13% | Emerging | MENA and LATAM rapid e-commerce penetration; returns culture nascent |

---

## 5. Vendor Universe

Known vendors with data points as of March 2026. Web search to update any figure
before citing. All revenue figures are estimates unless labeled [Public].

### Stage 4: Cart & Checkout

**Payment processing / infrastructure:**
- Stripe: $4.5B+ revenue (2024 est.) [Sacra]; powers ~41% of top 65K e-commerce sites
- Adyen: €1.8B+ net revenue (2024) [Public — AMS:ADYEN]; unified online + in-store
- Checkout.com: $400M+ ARR (est.); modular architecture; direct card network connections

**One-click / universal checkout:**
- Shop Pay: bundled in Shopify; 150M+ shopper accounts [Shopify, 2024]; highest-converting
- Link by Stripe: bundled in Stripe; requires Stripe PSP; not portable
- Bolt: ~$100M ARR (est.); non-Shopify stacks (BigCommerce, WooCommerce, Magento, custom)

**BNPL:**
- Klarna: $2.8B+ revenue (2024) [Klarna IPO filing, 2024]; 150M users, 45 countries
- Affirm: $2.7B+ revenue (2024) [Public — NASDAQ:AFRM]; Shopify investor; US-centric

**Fraud / chargeback:**
- Signifyd: ~$100M ARR (est.); 100% chargeback guarantee model
- Riskified: ~$300M ARR [Public — RSKD]; chargeback guarantee; publicly traded

**Payment orchestration:**
- Spreedly: ~$40M ARR (est.); 100+ PSP connections; middleware model
- IXOPAY: ~$20M ARR (est.); white-label for PSPs and enterprise

### Stage 5: Order Fulfillment

**Enterprise OMS:**
- Manhattan Associates: $1.04B revenue [Public — NASDAQ:MANH]; 6× Forrester Wave Leader;
  Morningstar Wide Moat rating; 18–24 month implementations; ~$500K–$2M ACV
- Blue Yonder (Panasonic): $1.36B FY24 [disclosed Feb 2025]; Luminate AI platform;
  Panasonic acquisition (2021) creates roadmap uncertainty
- IBM Sterling OMS: ~$500M+ (est.); ~998 enterprise deployments [Enlyft]; losing new logos
  to MACH architecture; 24–52 week implementation
- Salesforce OMS: bundled in SFCC; Einstein AI; platform lock-in limits cross-channel brands
- Oracle OMS / NetSuite: bundled in ERP; usage-based pricing added 2024

**Mid-market OMS / MACH:**
- Kibo Commerce: ~$40–60M ARR; MACH OMS; Agentic Commerce platform (March 2025);
  167% ROI, sub-6-month implementation [Kibo disclosed]; Forrester Wave Leader
- OneStock: ~$20–30M ARR; EU omnichannel leader; ship-from-store; SFCC/SAP/Shopware
- Linnworks: ~$30–40M ARR; Amazon + eBay + Shopify depth; SKU-level forecasting
- Brightpearl (Sage): ~$40M ARR; Sage ownership limits roadmap; no AI differentiation
- Deposco: ~$30–50M ARR; Gartner Magic Quadrant; strong in industrial/B2B

**WISMO / AI customer support:**
- Gorgias: ~$69–75M ARR [Sacra estimate ±~20%, 2024]; #1 Shopify App Store CX;
  AI Agent 2.0 (July 2025): 50%+ email auto-resolution at $1/resolution
- eDesk: ~$20–30M ARR; only multi-marketplace CX with native Amazon + eBay + Walmart;
  PE-backed [Tenzing Private Equity]

**Supply chain / visibility:**
- project44: ~$100M+ ARR; $2.4B valuation [Tracxn]; supply chain visibility; predictive ETAs
- o9 Solutions: ~$100–150M ARR; AI demand sensing; $500K–$3M ACV; CPG-first

**3PL / fulfillment:**
- Extensiv: ~$30M ARR; multi-warehouse 3PL; strong for outsourced fulfillment models

### Stage 6: Post-Purchase Experience

**Enterprise PPX:**
- Narvar: $105M ARR [Estimated — no public filing]; IRIS AI (74B+ interactions, 14yr history,
  125M consumers); NAVI autonomous resolution (launched NRF Jan 2026 — only purpose-built
  enterprise agentic resolution product as of March 2026); Narvar Shield (return fraud);
  no funding since 2018; ~10% ARR growth constrained by flat contract structure;
  highest composite moat score in Stage 6 (see moat scorecard)
- AfterShip: $85M revenue FY2024 [Latka estimate]; 1,200+ carrier integrations [disclosed];
  multi-platform; tracking commoditizing; enterprise pitch improving
- parcelLab: ~$30–40M ARR; EU enterprise leader; AI Email Editor + pL Copilot (NRF 2025);
  limited US penetration; no cross-retailer data moat

**Shopify-native PPX:**
- Loop Returns: $53M ARR; exchange-first (Shop Now, Shop Later); Return Bar (Happy Returns
  partnership); Shopify-exclusive — primary moat is also TAM ceiling
- Redo: $75M CY25 revenue; consumer-funded coverage model (shopper pays optional fee;
  merchant receives software free); ReturnBear acquisition expands physical footprint;
  Shopify-exclusive; coverage revenue depends on take rate sustainability
- Route: ~$40–60M ARR; package protection insurance + tracking; 13,000+ merchants;
  state-by-state insurance licensing risk
- Malomo: ~$5–10M ARR; branded order tracking with in-tracking upsell; Shopify-native only

**Physical / omnichannel:**
- Happy Returns (UPS): N/D (UPS-bundled); 12,000+ Return Bar locations (label-free);
  UPS P&L integration limits standalone software value capture

**Cross-border:**
- ZigZag Global: ~$15–20M ARR; own carrier accounts; EU/UK focus; limited US penetration

**Adjacent (S6/S7 span):**
- Yotpo: $213M revenue FY2024 [Latka estimate]; reviews + UGC + loyalty + SMS;
  primarily Stage 7; note when research scope includes loyalty adjacency
- Bazaarvoice: ~$200M revenue; enterprise review syndication; 6,500 retail network;
  no returns or tracking capability — outside S5/S6 core

---

## 6. Porter's Five Forces — Known Scores

Verified scores from Commerce v8 research. Update with web search for material
changes in market structure before citing.

### Stage 4: Cart & Checkout

| Force | Score | Key Insight |
|-------|-------|-------------|
| Supplier power | 4/10 | Card networks (Visa/Mastercard) set interchange unilaterally |
| Buyer power | 6/10 | Enterprise extracts sub-0.1% pricing; near-zero leverage for SMB |
| Competitive rivalry | 9/10 | Highest rivalry of any commerce infrastructure stage |
| Threat of substitution | 7/10 | Agentic commerce routes around checkout — most consequential threat |
| Threat of new entry | 5/10 | PCI-DSS and card network relationships create real barriers |
| **Industry attractiveness** | **7/10** | **Attractive for data network owners; challenging for new entrants** |

### Stage 5: Order Fulfillment

| Force | Score | Key Insight |
|-------|-------|-------------|
| Supplier power | 3/10 | Cloud infrastructure commodity; carrier data is bilateral |
| Buyer power | 7/10 | High at procurement; structurally low post-deployment (switching cost) |
| Competitive rivalry | 7/10 | Intense in mid-market; enterprise tier more protected |
| Threat of substitution | 6/10 | Shopify native OMS sufficient for pure DTC; MACH lowers barrier |
| Threat of new entry | 5/10 | AI-native entrants viable at mid-market; enterprise protected |
| **Industry attractiveness** | **6.2/10** | **Attractive for incumbents; challenging for greenfield entrants** |

### Stage 6: Post-Purchase Experience

| Force | Score | Key Insight |
|-------|-------|-------------|
| Supplier power | 2/10 | Carrier APIs are bilateral; no single carrier has leverage |
| Buyer power | 5/10 | Enterprise negotiates at RFP; $500K–$2M switching cost post-deployment |
| Competitive rivalry | 5/10 | Enterprise rivalry manageable; cross-tier competition is the real risk |
| Threat of substitution | 4/10 | Low for agentic resolution; moderate for basic tracking |
| Threat of new entry | 3/10 | Narvar's 74B-interaction IRIS dataset is a structural entry barrier |
| **Industry attractiveness** | **8.0/10** | **Most attractive single-stage investment profile in Stages 5–6** |

---

## 7. Pricing Architecture

Known pricing models across all three stages. Update vendor-specific figures with
web search — most private company pricing is undisclosed and marked [Estimate].

| Model | Stage | Vendors | Billing Unit | Price Range | Strategic Implication |
|-------|-------|---------|--------------|-------------|----------------------|
| Payment take rate | S4 | Stripe (2.9%+$0.30), Adyen (~0.3–0.8% net) | % GMV + per-transaction flat fee | 0.15–2.9% GMV | Auto-expands with merchant GMV; compresses merchant margin |
| Orchestration SaaS + usage hybrid | S4 | Spreedly, IXOPAY, Primer.io | Monthly platform + per-transaction routing fee | $500–$5K/month + $0.001–$0.01/txn | Separates routing logic from processing economics |
| BNPL merchant fee | S4 | Klarna, Affirm, Afterpay | % of order value at POS | 2–8% of order value [Estimate] | Vendor absorbs credit risk; consumer pays $0 interest |
| Chargeback guarantee | S4 | Signifyd, Riskified | % of GMV screened | 0.3–0.6% GMV screened [Estimate] | Vendor accepts full financial liability for approved fraud |
| Annual flat SaaS (volume-tiered) | S5/S6 | Narvar, parcelLab, AfterShip, IBM Sterling | Annual contract; shipment/GMV volume tiers | $10K–$800K/yr | Undermonetizes volume growth — 30% GMV growth ≠ 30% more revenue |
| Seat-based SaaS | S5 | IBM Sterling (legacy), Oracle, SAP (legacy) | Per user/admin/month | $50–$500/seat/month | Misaligned: commerce value scales with volume, not users |
| Per-transaction / per-shipment | S5/S6 | Narvar Shield, Signifyd, project44 | Per shipment tracked / per order screened | $0.05–$0.25/shipment; $0.10–$1.50/order | Auto-expands with merchant GMV; aligns incentives |
| Per-resolution (AI agents) | S6 | Gorgias ($1/resolution), Intercom Fin AI ($0.99) | Per automated ticket resolution | $0.33–$2.00/resolution | Most value-aligned for AI: charges only on successful automation |
| Consumer-funded coverage | S6 | Redo, Route | Consumer pays optional fee at checkout | $1–3/order (consumer-paid) | Aligns all incentives; Redo is software-free to merchants |
| Usage-based (compute / API) | S5 | o9, Blue Yonder Luminate, Kibo Agentic | Per planning run / routing decision / API call | $500K–$3M+ ACV enterprise; $0.001–$0.01/API call | Snowflake-analogue for commerce: scales with usage, not headcount |

**Pricing transition signal:** Market is mid-transition from flat annual SaaS toward
usage-based and per-resolution billing. Narvar's flat contract structure is its primary
monetization constraint — this is a known thesis-critical claim that warrants a
specific diligence question in any Narvar-related research.

---

## 8. Competitive Moat Scorecard

20-company scored matrix from Commerce v8. Scores are [Estimate] unless labeled.
Update via web search for material changes (new funding, acquisitions, product launches).

Scoring: 1–5 per dimension (25 total).
≥18 = Structural | 12–17 = Conditional | <12 = Transient

| Company | Data Network | Switch Cost | Platform | Regulatory | Physical | Total | Assessment |
|---------|-------------|-------------|----------|------------|----------|-------|------------|
| Manhattan Associates | 3 | 5 | 2 | 1 | 2 | 13/25 | CONDITIONAL (Morningstar: Wide Moat, May 2024) |
| Blue Yonder | 3 | 4 | 2 | 1 | 2 | 12/25 | CONDITIONAL |
| IBM Sterling OMS | 2 | 4 | 2 | 1 | 1 | 10/25 | CONDITIONAL (declining) |
| Kibo Commerce | 2 | 3 | 2 | 1 | 1 | 9/25 | TRANSIENT (strengthening) |
| Salesforce OMS | 2 | 4 | 4 | 1 | 1 | 12/25 | CONDITIONAL |
| Linnworks | 2 | 3 | 3 | 1 | 1 | 10/25 | TRANSIENT |
| Gorgias | 3 | 3 | 5 | 1 | 1 | 13/25 | CONDITIONAL |
| eDesk | 2 | 3 | 3 | 1 | 1 | 10/25 | TRANSIENT |
| project44 | 4 | 3 | 2 | 1 | 2 | 12/25 | CONDITIONAL |
| o9 Solutions | 3 | 4 | 2 | 1 | 1 | 11/25 | CONDITIONAL |
| Narvar | 5 | 5 | 3 | 1 | 2 | 16/25 | CONDITIONAL (approaching STRUCTURAL) |
| Loop Returns | 2 | 4 | 5 | 2 | 4 | 16/25 | CONDITIONAL (strengthening) |
| Redo | 3 | 3 | 5 | 2 | 1 | 14/25 | CONDITIONAL (improving) |
| AfterShip | 2 | 2 | 2 | 1 | 1 | 8/25 | LOW |
| parcelLab | 2 | 3 | 2 | 1 | 1 | 9/25 | TRANSIENT |
| Happy Returns (UPS) | 2 | 3 | 2 | 1 | 5 | 13/25 | CONDITIONAL |
| Route | 2 | 2 | 3 | 3 | 1 | 11/25 | CONDITIONAL |
| Yotpo | 2 | 3 | 3 | 1 | 1 | 10/25 | CONDITIONAL |
| Bazaarvoice | 2 | 3 | 2 | 1 | 1 | 9/25 | TRANSIENT |
| Shippo | 1 | 2 | 2 | 1 | 1 | 7/25 | LOW |

**Moat type reference:**
- Data network: transaction/interaction volume, cross-retailer breadth, ML model lift
- Switch cost: implementation depth, ERP integration, data portability friction
- Platform: ecosystem distribution (Shopify App Store rank, platform investor status)
- Regulatory: financial liability models (chargeback guarantee, insurance), compliance moat
- Physical: reverse logistics infrastructure, drop-off network density

---

## 9. Regulatory Environment

Known regulations as of March 2026. Verify effective dates and enforcement status
before citing — this area changes faster than market sizing.

| Regulation | Jurisdiction | Core Requirement | Stage 5/6 Impact | Do Not Over-Claim |
|------------|-------------|-----------------|-----------------|-------------------|
| GDPR | EU/EEA | Lawful basis; right to erasure; data minimization | Cross-retailer consumer identity graphs require explicit consent framework audit | Not a new catalyst — mature operating constraint since May 2018 |
| CCPA/CPRA | California (de facto US) | Right to know, delete, opt-out of sale | Cross-brand PII for fraud detection requires explicit opt-in | California-specific; federal US privacy law still absent |
| EU AI Act | EU (effective Aug 2026) | Risk classification; high-risk systems require conformity assessment | Return fraud AI scoring consumer behavior is potentially high-risk classification | Fact-specific and still evolving; do not model broad AI Act TAM uplift pending guidance |
| EU Returns Directive | EU | 14-day minimum return window; clear policy disclosure | Mandated windows increase return volume → direct growth for returns management software | Already law; model as baseline, not as new catalyst |
| ESPR Destruction Ban | EU/EEA (effective Jul 2026) | Large companies banned from destroying unsold apparel/clothing/footwear | Returns disposition becomes compliance-critical — creates workflow-specific tailwind for resale, grading, compliant disposition software | Applies to apparel only; do not generalize to universal retail software re-rating |
| Paid Returns Shift | US + UK | 76% of UK fashion retailers charge for postal returns [ZigZag/Retail Gazette] | Real niche tailwind for coverage and returns-tech in stricter return policy segments | Also raises conversion and loyalty risk — model both sides |
| FTC Return Policy Rules | United States | Clear disclosure; no deceptive practices | Drives standardization of return portal disclosures; AI-powered policy enforcement benefits | Compliance baseline, not a growth driver |
| Shipping insurance regulation | US (state-by-state) | Insurance products require state licensing; premium collection rules | Redo's coverage model and Route's package protection face state-level licensing risk | Not yet resolved — flag as open regulatory question in any Redo/Route analysis |

---

## 10. Technology Trends & Disruption Vectors

Quantified signals as of March 2026. Verify before citing.

| Trend | Horizon | Quantified Signal | Stage 5/6 Impact |
|-------|---------|-------------------|-----------------|
| Agentic AI resolves post-purchase autonomously | Now–2027 | Gartner: 40% of enterprise apps will include task-specific AI agents by 2026 | Returns, exchanges, delivery exceptions are lowest-risk, highest-frequency autonomous agent actions |
| Agentic commerce protocols in production | 2026 | MCP (Anthropic, 97M monthly SDK downloads Mar 2026), ACP (Stripe + OpenAI, production Jan 2026), UCP (Shopify + Google, launched Jan 11, 2026) | OMS, checkout, and returns vendors must expose callable protocol interfaces — not roadmap; already in production at major platforms |
| Agentic commerce traffic surge | 2025–2027 | Adobe: AI-driven retail site traffic up 4,700% YoY (July 2025) | OMS must handle agent-initiated orders with different authentication and fraud profiles |
| MACH architecture democratizing OMS | 2024–2027 | Cloud/API-first is now standard OMS buyer requirement [enterprise RFP trend] | Mid-market brands can implement enterprise-grade distributed OMS in 6 months vs. 18–24 months |
| Return fraud industrialization | 2024–2026 | NRF: $103B return fraud in 2024 [Fact]; Signifyd: abusive return behavior up 64% YoY (updated v9 — prior figure 21% was stale) | Organized rings operate across multiple retailers simultaneously — single-retailer detection is structurally insufficient |
| AI in demand forecasting | 2025–2028 | IDC: AI spending growing 31.9% CAGR 2025–2029; Walmart AI inventory optimization [disclosed] | ML demand sensing replacing statistical models (ARIMA); real-time agentic replenishment emerging |

### Structural Disruption Map

| Capability Layer | Durable (3–5yr) | At Risk | Disruptive Force |
|-----------------|-----------------|---------|-----------------|
| Enterprise OMS routing | Deep ERP integration; distributed order management; multi-node logic | Static rule-based routing; on-premise deployments; proprietary carrier APIs | AI-native routing learns optimal fulfillment paths continuously |
| Order tracking / notifications | Cross-retailer carrier intelligence; IRIS 74B-interaction dataset | Standalone tracking tools; single-carrier specialty | Consumers query AI agents for status rather than visiting tracking portals |
| Returns management | Cross-retailer fraud signal networks; physical drop-off infrastructure | Single-retailer rule-based portals; flat annual contracts | NAVI-style autonomous resolution; per-return pricing models |
| Return fraud prevention | Cross-retailer behavioral signal networks (IRIS: 125M consumers) | Single-retailer fraud rules; chargeback-based detection | AI-powered synthetic identity fraud; deepfake video returns |
| WISMO / AI customer support | AI policy-enforcement agents; multi-channel resolution | Human support for tier-1 queries; per-seat helpdesk | LLM agents resolving 80–90% of tier-1 support by 2029 [Estimate] |
| Demand forecasting | Multi-brand cross-channel demand signal; ML trained on years of data | Statistical forecasting (ARIMA, regression); single-brand demand only | Real-time agentic replenishment: AI agents autonomously placing purchase orders |

---

## 11. Key Open Questions (Carry-Forward from Prior Research)

These questions were surfaced in prior iterations. Status updated after v9 research (April 2026).
Address any OPEN items explicitly in any new commerce infrastructure research.

**High priority — changes the thesis if wrong:**

1. **[RESOLVED — v9] Does Narvar's IRIS data include return fraud behavioral signals?**
   CONFIRMED: IRIS explicitly covers cross-retailer fraud detection (125M consumer profiles,
   74B interactions). The data network moat rating at 5/5 stands. Shield product directly
   confirms fraud signal scope.

2. **[OPEN] Has Narvar actually migrated any customer from flat annual SaaS to per-resolution
   or per-return pricing?** The monetization upside thesis depends on contract
   renegotiation, not just product capability. No public proof of realized net ARR expansion
   after pricing migration found in v9 research. Remains IC-critical — do not advance
   repricing thesis to [F] without primary diligence evidence.

3. **[OPEN] What is Redo's regulatory status in all 50 US states for its consumer-funded
   coverage model?** Some states classify this as insurance requiring licensure.
   If Redo must restructure the model in any major e-commerce state (California,
   New York), the revenue model changes. Note: Redo acquired Contextual (April 2026) —
   verify if the acquisition changes the regulatory exposure profile.

4. **[OPEN] What is the actual competitive dynamic between Narvar and parcelLab for new
   US enterprise logos in 2025–2026?** parcelLab won several US enterprise accounts
   in late 2024. No win/loss data resolved in v9. Remains open for primary diligence.

**Medium priority — material for specific deal contexts:**

5. **[OPEN]** What is the realistic agentic resolution automation rate for enterprise returns
   (NAVI)? The 50%+ claim is from Gorgias's AI Agent 2.0 for customer support —
   returns resolution is a harder problem. Primary diligence required.

6. **[RESOLVED — v9] ESPR market expansion vs. feature upgrade?**
   CONFIRMED as market expansion event: destruction ban (effective July 19, 2026) creates
   mandatory new disposition/resale/grading workflow demand for large EU apparel companies.
   Not merely a feature upgrade to existing returns portals — requires new compliance
   reporting, Digital Product Passport integration, and alternative disposition workflows.

7. **[OPEN]** What share of Loop Returns' $53M ARR is exchange revenue vs. returns portal fee?
   The exchange-first model is the primary thesis, but if most revenue is still from
   basic returns, the differentiation is narrower than it appears.

8. **[RESOLVED — v9] Is AfterShip's carrier integration a genuine data network effect?**
   CONFIRMED as primarily technical API integration, not a data network moat. AfterShip
   lacks the cross-retailer behavioral signal layer that defines Narvar IRIS. AfterShip
   moat score 8/25 (LOW) is confirmed. Do not upgrade without evidence of proprietary
   signal data accumulation.

---

## 12. IC Scrutiny Framework for This Market

Questions that have historically faced the hardest IC pushback in commerce infrastructure.
Address proactively in any investment memo or market research report for this space.

| Decision Area | Harder Question | What Passes IC Scrutiny |
|--------------|----------------|------------------------|
| Market sizing | Is the market definition consistent from start to finish? | Stage-specific reference markets + separately labeled Pattern analytic slices; never blended without disclosure |
| Protocol risk | Can the vendor expose commerce actions through reliable callable interfaces today? | Evidence of usable APIs or protocol support — not roadmap announcements or press releases |
| Monetization | Has the vendor actually migrated contracts to new pricing, or only proposed it? | Proof of realized net ARR expansion after pricing migration; management claim alone is insufficient |
| Competitive moat | Does the advantage survive substitute workflows from adjacent stages? | Measured ML lift, deep ERP embeds, or financial liability/physical assets that resist substitution |
| Regulation | Is the regulatory tailwind tied to a specific documented scope? | Narrow, workflow-specific impacts with clear legal grounding; not a broad sector re-rating |
| Displacement thesis | Is share gain from greenfield, adjacencies, or real incumbent displacement? | Explicit separation of new-logo growth from installed-base displacement; win/loss data required |

---

## 13. Loading Instructions

When this template is loaded, apply the following to all research on this market:

1. **Scope declaration:** Confirm with Ian which stages are in scope before beginning
   research. Do not assume S4+5+6 — confirm explicitly.

2. **Vendor list:** Ask which specific vendors require coverage. The full vendor
   universe in Section 5 is a reference — not every vendor needs a full profile
   in every report.

3. **Known data points:** Use the figures in this template as starting points for
   research, not as current ground truth. Web search to verify and update before
   citing. Note in the evidence label if a figure is from this template and may
   be outdated.

4. **Open questions:** Review Section 11 before finalizing any research output.
   If the research addresses any of those questions, update this template with
   the new findings.

5. **Arithmetic checks:** Apply the guardrails in Section 3 to every market sizing
   claim before the draft is complete. Do not skip the CAGR verification step.

6. **Data sensitivity:** Apply the tiering framework in Section 2 to any vendor
   assessment, DDR, or IC memo for any vendor in this market.

---

**Template version:** v9 — Last updated: 2026-04-29
**Research basis:** Commerce_Market_Research_v9_2026-04-29.docx
**Open questions resolved this cycle:** Q1 (Narvar IRIS fraud scope), Q6 (ESPR expansion vs. feature), Q8 (AfterShip moat)
**Still open:** Q2 (Narvar repricing proof), Q3 (Redo regulatory), Q4 (Narvar/parcelLab win-loss), Q5 (NAVI automation rate), Q7 (Loop ARR mix)
