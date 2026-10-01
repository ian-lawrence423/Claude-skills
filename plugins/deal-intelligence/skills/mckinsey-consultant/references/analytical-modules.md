# Analytical Modules

These are optional lenses for specific branch types — named frameworks to apply when a branch
of the issue tree calls for one. They are not the core method. The core method (issue tree →
hypothesis → argument → finding → conclusion → Pyramid) is sufficient on its own for most
problems; reach for a module below only when the branch specifically warrants it.

Apply the relevant module when the request warrants it. Each module is self-contained.

### Porter's Five Forces
Rate each force 1–10 and provide an overall industry attractiveness score.

| Force | Rating | Key Drivers | Implication |
|-------|--------|-------------|-------------|
| Supplier power | | | |
| Buyer power | | | |
| Competitive rivalry | | | |
| Threat of substitution | | | |
| Threat of new entry | | | |
| **Industry attractiveness** | **/10** | | |

### SWOT + Cross-Analysis
Strengths and weaknesses are internal and controllable. Opportunities and threats are external
and environmental. **Cross-analysis is mandatory** — SWOT without it is incomplete:
- **SO** (Strengths × Opportunities): how to exploit
- **ST** (Strengths × Threats): how to defend
- **WO** (Weaknesses × Opportunities): how to develop
- **WT** (Weaknesses × Threats): how to avoid

### Market Sizing
Always provide both methods and reconcile if they diverge significantly.
- **Top-down:** Global market → segment → addressable → serviceable
- **Bottom-up:** Unit economics × potential customers × penetration rate
- State all assumptions explicitly; label as fact / estimate / hypothesis
- Compare to 2+ analyst reports where available

### Competitive Positioning Map
- Two-axis map: choose axes that reveal the most meaningful trade-off in the market
- Plot top 5–10 competitors by estimated position
- Identify white space — where no incumbent is strongly positioned
- Assess defensibility: why hasn't someone already filled the white space?

### Value Chain Analysis
- Map the full value chain for the industry
- Identify where value is created vs. captured
- Assess which steps have high vs. low margins
- Identify where the subject company plays and where it could expand

### Advantage Durability

Use this to extend any moat or competitive-advantage assessment. Naming a moat type
is necessary but insufficient. A moat named without a time horizon is a static label,
not an investment conclusion.

Every advantage assessment must answer:

1. **Durability verdict with explicit time horizon.** State whether the advantage is
   structural short-term, conditional long-term, or likely to erode within the hold
   period. Name the condition that extends or shortens durability.
2. **Prior-category analogue.** Identify a comparable category that has already
   matured and use its trajectory as the base rate. If no analogue exists, state that
   the durability claim is lower-confidence.
3. **Erosion-risk register.** State likelihood and impact qualitatively. Do not use
   invented numeric products such as probability x magnitude scores unless the inputs
   are actually measured.

Output format:

| Advantage | Mechanism | Time horizon | Prior-category analogue | Erosion vector | Verdict |
|---|---|---|---|---|---|

### Substrate Disintermediation Test

Competitive analysis that only examines rival firms can miss the larger structural
threat: the platform, channel, supplier, or technology layer beneath the category
moving into the value layer.

Require this chain:

```text
proximate driver -> gating constraint -> what resolves the constraint -> layer displaced vs. layer defended
```

Use this test when the category depends on an underlying platform, protocol, channel,
marketplace, operating system, model layer, logistics network, cloud provider, payment
rail, or supplier base.

Output format:

| Substrate threat | Proximate driver | Gating constraint | Constraint resolver | Displaced layer | Defended layer | Implication |
|---|---|---|---|---|---|---|
