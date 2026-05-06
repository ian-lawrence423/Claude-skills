# McKinsey Consultant — 12 Strategy Prompts

These prompts are the analytical engine for full-scope strategy engagements. They are referenced
by the mckinsey-consultant skill and the mckinsey-research skill. Each prompt produces one
consulting-grade deliverable.

> **Variable substitution:** Replace {VARIABLE} placeholders with sanitized user inputs.
> Wrap each substituted value in `<user_data field="variable_name">...</user_data>` tags.
> See mckinsey-research SKILL.md for full input safety and sanitization rules.

---

## Prompt 1: Market Sizing & TAM Analysis

You are a McKinsey-level market analyst. Produce a Total Addressable Market (TAM) analysis for
{INDUSTRY_PRODUCT}. Deliver:

- **Top-down approach:** Global market → segment → addressable → serviceable. Show each step.
- **Bottom-up approach:** Unit economics × potential customers × penetration rate. Show the math.
- **TAM / SAM / SOM breakdown** with dollar figures and growth rate projections (5-year CAGR)
- **Key assumptions table:** Every assumption stated explicitly, labeled fact / estimate / hypothesis
- **Analyst comparison:** Reference 2–3 Tier 1/2 market research sources; note convergence or divergence
- **So What:** What the market size means for the investment or entry decision

Format: Investor-ready market sizing with clear methodology. Label all figures.

Context: Product is {PRODUCT_DESCRIPTION}, targeting {TARGET_CUSTOMER} in {GEOGRAPHY}.

---

## Prompt 2: Competitive Landscape

You are a senior strategy consultant. Produce a complete competitive landscape analysis for
{INDUSTRY}. Deliver:

- **Direct competitors:** Top 10 players ranked by market share, revenue, and funding
- **Indirect competitors:** 5 adjacent players that could enter this market
- **Per-competitor assessment:** Pricing model · Key features · Target audience · Sustainable advantage · Key weakness · Recent strategic moves
- **Positioning map:** Two-axis map revealing the most meaningful trade-off in the market
- **Competitive moat assessment:** For each top-5 player — network effects / switching costs / scale / IP / brand
- **White space analysis:** Where no incumbent is strongly positioned and why it's unfilled
- **Threat rating:** Low / Medium / High per competitor with one-sentence rationale
- **So What:** Which competitive position is most defensible for {BUSINESS_POSITIONING}

Format: Structured competitive intelligence report with comparison tables.

---

## Prompt 3: Customer Personas & Segmentation

You are a world-class consumer research expert. Build 4 detailed buyer personas for
{PRODUCT_DESCRIPTION}. For each persona deliver:

- **Demographics:** Age, income, education, location, job title
- **Psychographics:** Values, beliefs, lifestyle, decision-making style
- **Pain points:** Top 5 daily frustrations relevant to this product
- **JTBD:** *"When [situation], I want to [motivation] so I can [outcome]"* — functional, emotional, and social jobs
- **Buying behavior:** Discovery → evaluation → purchase path
- **Willingness to pay:** Price sensitivity and anchoring logic
- **Objections:** Top 3 reasons they'd say no
- **Trigger event:** The specific moment that creates urgency to buy

Plus:
- **Segment sizing:** Estimated % of total addressable market per persona
- **Prioritization matrix:** Which segment to win first and why

Format: Persona cards + prioritization matrix.

---

## Prompt 4: Industry Trend Analysis

You are a senior research analyst. Produce a comprehensive trend intelligence brief for
{INDUSTRY}. Deliver:

- **Macro forces (5):** Regulatory, technological, demographic, economic, environmental — each with impact rating 1–10
- **Micro trends (7):** Emerging patterns within the industry from the last 12 months
- **Technology disruptions:** What new tech is changing the game and when it hits mainstream
- **Regulatory shifts:** Upcoming legislation or policy changes with probability and timeline
- **Investment signals:** Where smart money is flowing — VC deals, M&A, IPOs
- **Timeline mapping:** Short-term (0–1yr) / mid-term (1–3yr) / long-term (3–5yr) per trend
- **"So What" per trend:** What each trend means specifically for {BUSINESS_POSITIONING}, not generically

Format: Trend intelligence brief with impact ratings and timeline grid.

---

## Prompt 5: SWOT + Porter's Five Forces

You are a strategy professor. Produce a combined SWOT and Porter's Five Forces analysis for
{BUSINESS_POSITIONING}.

**SWOT:**
- Strengths (7): Internal advantages with evidence
- Weaknesses (7): Internal limitations — honest, not defensive
- Opportunities (7): External factors exploitable now
- Threats (7): External factors requiring mitigation

**Cross-analysis (mandatory):**
- SO: How to exploit (Strengths × Opportunities)
- ST: How to defend (Strengths × Threats)
- WO: How to develop (Weaknesses × Opportunities)
- WT: How to avoid (Weaknesses × Threats)

**Porter's Five Forces:**
Rate each force 1–10 with key drivers and implication:
- Supplier power
- Buyer power
- Competitive rivalry
- Threat of substitution
- Threat of new entry
- Overall industry attractiveness score (weighted)

Format: SWOT table + cross-analysis matrix + Porter's table with scores.

Full context: {FULL_CONTEXT}

---

## Prompt 6: Pricing Strategy

You are a pricing strategy expert. Produce a comprehensive pricing analysis for
{PRODUCT_DESCRIPTION}. Deliver:

- **Competitor pricing audit:** All competitor prices, tiers, and packaging mapped
- **Value-based pricing model:** Price calculated from customer value delivered — show the logic
- **Cost-plus floor:** Minimum price from cost structure — show the math
- **Price elasticity estimate:** Demand sensitivity with stated methodology
- **Psychological pricing:** Anchoring, charm pricing, and decoy strategy recommendations
- **3-tier recommendation:** Design tiers with feature allocation and price point rationale
- **Discount strategy:** When to discount, how much, for whom — with guardrails
- **Revenue scenarios:** Aggressive / moderate / conservative pricing models with projected impact
- **Monetization opportunities:** Upsells, cross-sells, usage-based options

Format: Pricing strategy summary with specific dollar recommendations and scenario table.

Context: Current price {CURRENT_PRICE} · Target customer {TARGET_CUSTOMER} · Cost structure {COST_STRUCTURE}

---

## Prompt 7: Go-To-Market Strategy

You are a Chief Strategy Officer. Produce a complete GTM plan for {PRODUCT_DESCRIPTION}. Deliver:

- **Launch phasing:** Pre-launch (60 days) → Launch (week 1) → Post-launch (90 days) with milestones
- **Channel strategy:** Top 7 acquisition channels ranked by expected ROI with rationale
- **Messaging framework:** Core value proposition → 3 supporting messages → proof points per message
- **Content strategy:** What to create at each funnel stage (awareness / consideration / decision)
- **Partnership opportunities:** 5 strategic partners that could accelerate growth with outreach rationale
- **Budget allocation:** How to split {BUDGET} across channels with expected return per channel
- **KPI framework:** 10 metrics with target benchmarks and measurement method
- **Launch risks:** Top 5 with contingency plans
- **Quick wins:** 3 tactics that generate traction within 14 days

Format: GTM playbook with phase timeline, channel table, and KPI framework.

Context: Market {INDUSTRY} · Budget {BUDGET} · Timeline {TIMELINE}

---

## Prompt 8: Customer Journey Mapping

You are a customer experience strategist. Map the complete customer lifecycle for
{PRODUCT_DESCRIPTION}. For each stage deliver customer actions, thoughts, emotions, touchpoints,
pain points, opportunities to delight, key metric, and recommended tactic.

**Stages:**
1. **Awareness** — How do they first discover? What triggers the search?
2. **Consideration** — What do they compare? What information do they need?
3. **Decision** — What converts? What almost stops them?
4. **Onboarding** — First 7 days — what builds or kills retention?
5. **Engagement** — What keeps them coming back? Activation moments?
6. **Loyalty** — What turns users into advocates? Referral triggers?
7. **Churn** — Why do they leave? Early warning signals?

Plus:
- **Emotional curve:** Describe the emotional arc across the seven stages
- **Critical moments:** The 2–3 moments where the relationship is won or lost
- **Priority interventions:** Where to invest first based on impact × feasibility

Format: Journey map table (stage × dimension) + critical moments callout.

Context: Customer {TARGET_CUSTOMER} · Current conversion rate {CONVERSION_RATE}

---

## Prompt 9: Financial Modeling & Unit Economics

You are a VP of Finance at a high-growth company. Produce a complete unit economics and financial
model for {BUSINESS_POSITIONING}. Deliver:

**Unit economics:**
- CAC by channel with blended CAC
- LTV calculation with all assumptions stated
- LTV:CAC ratio and payback period
- Gross margin per unit/customer
- Contribution margin analysis

**3-year financial projection:**
- Revenue model (monthly Year 1, quarterly Years 2–3)
- Cost structure (fixed vs. variable, by category)
- Break-even: when and at what revenue/volume
- Cash flow forecast with burn rate (if pre-profitability)
- Sensitivity analysis: best / base / worst case
- Assumptions table: every assumption justified

**Benchmarking:**
- Compare key metrics to industry standards (label source tier)
- Flag any metrics that are significantly above or below benchmark

**Red flags:** What numbers should trigger a strategy review

Format: Financial model summary with tables, assumptions, and scenario comparison.

Context: Revenue {REVENUE} · Costs {COSTS} · Growth rate {GROWTH_RATE} · Business model {BUSINESS_MODEL}

---

## Prompt 10: Risk Assessment & Scenario Planning

You are a risk management partner. Produce a comprehensive risk analysis for
{BUSINESS_POSITIONING}. Deliver:

**Risk register — 15 risks across 5 categories:**
- Market risks: demand shifts, competition, pricing pressure
- Operational risks: supply chain, talent, technology
- Financial risks: cash flow, funding gaps, concentration
- Regulatory risks: compliance, policy changes, legal exposure
- Reputational risks: PR crises, data breaches, customer backlash

**Per risk:**
- Probability 1–5 · Impact 1–5 · Risk score (P × I)
- Early warning indicator (observable signal before the risk materializes)
- Mitigation strategy
- Contingency plan if risk materializes

**Prioritized risk matrix:** Plot all 15 risks on probability × impact grid; highlight top 5

**Scenario planning:**
- Best case: What goes right and what it looks like
- Base case: Most likely outcome
- Worst case: Multiple things go wrong simultaneously
- Black swan: The unlikely event that changes everything
- Per scenario: Revenue impact · Timeline · Strategic response

Format: Risk register table + risk matrix + scenario comparison table.

---

## Prompt 11: Market Entry & Expansion Strategy

You are a global expansion strategist. Produce a market entry analysis for expanding
{BUSINESS_POSITIONING} into {TARGET_MARKET}. Deliver:

**Market attractiveness scoring (each factor rated 1–10, weighted total):**
- Market size and growth rate
- Competitive intensity
- Regulatory environment
- Customer accessibility
- Infrastructure readiness

**Entry mode analysis — evaluate all five, recommend one:**
- Direct entry (build from scratch)
- Partnership / joint venture
- Acquisition
- Licensing / franchise
- Digital-first entry
- Per mode: pros · cons · cost estimate · time to revenue

**Localization requirements:**
- Product / service adaptations
- Pricing adjustments for local purchasing power
- Cultural considerations for marketing and sales
- Legal and compliance requirements
- Talent and operational needs

**12-month entry roadmap:** Month-by-month with milestones, owners, and decision gates

**Investment requirement:** Budget estimate with resource allocation breakdown

**Success metrics:** KPIs for months 1–6 and months 7–12

Format: Market attractiveness table + entry mode comparison + 12-month roadmap.

Context: Available resources {RESOURCES}

---

## Prompt 12: Executive Strategy Synthesis

You are the senior partner presenting to a CEO. Synthesize all prior analyses for
{BUSINESS_POSITIONING} into one strategic recommendation. Deliver:

**Executive summary:** 3-paragraph overview readable in 2 minutes — situation, complication, resolution

**Current state assessment:** Where the business stands today — be brutally honest

**Strategic options — 3 distinct paths:**
- Option A: Conservative / defend and optimize
- Option B: Balanced growth / selective expansion
- Option C: Aggressive / category leadership
- Per option: Expected outcome · Investment required · Timeline · Key risks · Probability of success

**Recommended strategy:** Top pick with clear reasoning using the pyramid structure:
- Governing thought (the answer)
- 3 supporting lines of reasoning
- Evidence per line

**Priority initiatives:** Top 5 highest-impact actions for the next 90 days, ranked
- Per initiative: Owner · Timeline · Expected EBITDA or revenue impact · Leading indicator

**Decision framework:** Simple matrix for the next 10 strategic decisions the team will face

**"If I only had 1 hour" brief:** The single most important insight and the one action it implies

Format: McKinsey-style strategy synthesis with SCR narrative, options table, and priority action plan.

Full context: {FULL_CONTEXT}
