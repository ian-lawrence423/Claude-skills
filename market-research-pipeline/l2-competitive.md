# L2 — Competitive Landscape Agent

Load immediately:
- `{SKILLS_PATH}/market-research/SKILL.md`  → Section: Level 2 + Competitor Profile Anatomy
- `{SKILLS_PATH}/market-research/references/analytical-prompts.md` → Section: Competitive Landscape
- `{SKILLS_PATH}/mckinsey-consultant/SKILL.md` → Section: Porter's Five Forces

## Your Inputs
```
BRIEF:       {WORK_DIR}/brief.md
L4_OUTPUT:   {WORK_DIR}/research/l4-market.md
L3_OUTPUT:   {WORK_DIR}/research/l3-customer.md
```

## Depth Requirements

Every named competitor requires all six Competitor Profile elements. A profile
missing any element is incomplete and will fail the doc-quality check.

**Six required elements per competitor:**
1. Core product and GTM (1–2 sentences — specific, not categorical)
2. Customer base (named segments + revenue/ARR if available; state explicitly if not)
3. Sustainable advantage (must name mechanism: network effect / switching cost /
   scale economies / proprietary IP / brand — generic descriptors fail)
4. Key weakness (specific observable limitation — not a broad category)
5. Strategic trajectory (at least 2 signals: product launches / M&A / job postings /
   exec statements / partnerships — trajectory without signals is speculation)
6. Competitive verdict (one interpretive sentence: what this means for the thesis)

Positioning map: choose two axes that reveal the market's most meaningful trade-off.
White space: where no incumbent is strongly positioned, and why it hasn't been filled.

Strategic-analysis depth requirements:
- Define the competitive arena before listing vendors: direct competitors, substitutes,
  adjacent platforms, and non-consumption.
- Explain customer choice: buyer, user, economic decision-maker, trigger event,
  ranked buying criteria, switching threshold, procurement burden, and price/value metric.
- Include substitute workflows and platform-native threats even when they are not
  standalone vendors. Buyers compare outcomes, not vendor taxonomies.
- For traction, use independent evidence where available: revenue, customer count,
  usage, funding, app-store/marketplace signal, public case study, analyst data,
  filing, or credible third-party coverage. Vendor websites can describe product
  claims but cannot prove traction, differentiation, retention, pricing power, or moat.
- For every moat claim, state mechanism, observable metric, evidence, replicability
  horizon, and erosion vector. Product breadth, UI quality, or current execution is
  not a moat unless it creates measurable resistance to displacement.

Apply inline citations and DATA GAP flags throughout.
Append to `{WORK_DIR}/data-gaps.md` and `{WORK_DIR}/source-bibliography.md`.

## Output — write to `{WORK_DIR}/research/l2-competitive.md`

The output must include these sections in addition to the existing competitor
profile skeleton:
- Competitive arena map: arena branch / definition / named examples / why customers choose it.
- Customer choice model: buyer / user / economic decision-maker / trigger / buying criteria / switching threshold / price-value metric.
- Competitor evidence table: competitor / segment / buyer / workflow / pricing model / traction evidence / advantage / weakness / threat level.
- Substitute workflows and platform threats: substitute or platform / workflow replaced / buyer appeal / adoption evidence / threat mechanism / response.
- Moat proof and durability: moat claim / type / mechanism / metric / evidence / strength 1-5 / replicability horizon / erosion vector / verdict.

```markdown
# L2 — Competitive Landscape — [COMPANY]

## Porter's Five Forces
[Rated table — force / rating / key drivers / implication]
Overall industry attractiveness: [N]/10

## Competitor profiles (top 3–7)
[Full six-element profile per competitor — 300–500 words each in final doc]

## Positioning map
Axis 1: [name + rationale]
Axis 2: [name + rationale]
[Competitor positions + white space identification]

## Market share estimates
[Where available — state source and confidence]

## White space analysis
[Specific gap + why it hasn't been filled]
```
