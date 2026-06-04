---
name: diligence-ddr
description: >
  Generate or customize a comprehensive Due Diligence Request List (DDR) for PE buyout or M&A sell-side transactions. Use this skill whenever the user mentions due diligence, a DDR, data room requests, diligence checklist, or wants to prepare or tailor a request list for a deal. Trigger even if the user just says "I need a DDR for [company]", "help me build out diligence questions for [deal]", or "customize this request list." This skill covers full DDR generation from scratch given a company description, and targeted customization of an existing DDR to a specific business model, sector, and deal context.
---

# Due Diligence Request List (DDR) Skill

Generates or customizes comprehensive, investment-grade DDRs for PE buyout and M&A sell-side transactions. Output should feel like it was written by an experienced deal team — precise, specific to the business model, and structured to surface real investment risks.

---

## Step 1: Gather Context

Before writing anything, collect the following. If the user has already provided some of this, extract it from context and only ask for what's missing.

**Required:**
- **Company name and one-line description** (what do they do, who do they sell to)
- **Business model** (SaaS, marketplace, services, product, hybrid — subscription vs usage vs transactional)
- **Deal type** (PE buyout vs M&A sell-side) — this affects framing and emphasis
- **Sector** (e.g., B2B SaaS, retail tech, healthcare, fintech, logistics) — drives which risk areas matter most

**Helpful but optional:**
- Revenue range / scale (e.g., "$50M ARR" or "pre-revenue")
- Known deal issues or investment thesis (e.g., "platform roll-up", "international expansion story", "margin improvement")
- An existing DDR to customize rather than build from scratch
- Any specific sections to prioritize or deprioritize

If the user provides a document (DDR, CIM, pitch deck), read it first to extract context before asking questions.

---

## Step 2: Choose Mode

**Mode A — Generate from Scratch**
User provides company/deal context. Build a full DDR tailored to the business model and sector.

**Mode B — Customize Existing DDR**
User provides an existing DDR. Tailor every section to the specific company: replace generic placeholders with company-specific terminology, add business-model-specific requests, remove irrelevant sections, and sharpen questions to reflect known deal risks.

---

## Step 3: Structure and Output

### DDR Structure

A high-quality DDR has 8–12 numbered sections. Always include the core sections below, and add sector-specific sections as appropriate (see references/).

**Universal Core Sections (always include):**

1. **Financial Performance, Planning, and Quality of Earnings**
2. **Revenue Model and Pricing Strategy**
3. **Customer Base, Scale Metrics, and Cohort Health**
4. **Go-to-Market Engine** (Sales cycle, pipeline, win/loss, land & expand)
5. **Product Strategy and Roadmap**
6. **Technology, Infrastructure, and Data**
7. **Customer Success, Implementation, and Operating Model**
8. **Strategic Positioning and Expansion**
9. **Key Risks, Compliance, and Legal**
10. **Diligence Materials / Data Room Request** (always last — the "what to send us" section)

**Sector-specific additions:** See `references/sector-modules.md` for add-on sections by vertical (e.g., fraud/risk for fintech, carrier/logistics for supply chain, clinical/regulatory for healthcare).

### Output Format

- Use numbered top-level sections with descriptive headers
- Use a subtitle under each header that captures the "so what" (e.g., `## 3. Customer Base, Scale Metrics, and Cohort Health` → subtitle: `Logos, Volumes, and Retention`)
- Each section contains bullet-point questions — typically 6–12 per section
- Questions should be **specific, operational, and multi-part** — not generic ("describe your pricing") but precise ("provide the distribution of ACV by segment, including median, quartiles, and top-decile values, and describe how pricing has evolved over the last 24 months")
- The Data Room section (always last) should be a concrete artifact request list — name specific files, views, and data exports needed
- Include a header block: Company name, "Due Diligence Request List", subtitle "Comprehensive Information Request | Confidential", and a CONFIDENTIAL notice

### Writing-Style Review — Narrative Content Only

Before generating any code, run the writing-style self-review on the DDR's narrative
elements: the cover block text, any section framing sentences, and any introductory
language above question lists.

**Does NOT apply to:** Bullet questions, sub-questions, or the data room request list.
These are operational requests, not prose — applying prose standards to them would
make them worse, not better.

**Applies to:** Cover subtitle text, any section-level framing paragraph if used,
and any executive summary or context paragraph added at the top of the document.

```
Read: /mnt/skills/user/writing-style/SKILL.md
```

### Quality Bar

Calibrate to the Narvar DDR standard:
- **Depth**: Questions anticipate second-order issues. Don't just ask "what is churn" — ask for GLR/GRR/NRR by cohort, vintage curves, and the operational definition of churn
- **Specificity**: Name the company's actual products, segments, or business model constructs in the questions wherever possible
- **Coverage**: Every major value driver and risk area has dedicated questions
- **Actionability**: Each question maps to something a deal team can actually get — a file, a metric, a table, a management answer

---

## Step 4: Sector and Deal-Type Adjustments

### PE Buyout vs. M&A Sell-Side

| Dimension | PE Buyout | M&A Sell-Side |
|---|---|---|
| Emphasis | Operational detail, cost structure, management depth | Strategic fit, revenue quality, integration complexity |
| Financials | QoE focus, EBITDA bridge, working capital | Revenue recognition, ARR bridge, customer concentration |
| Forward look | LRP, hiring plan, margin expansion levers | Pipeline quality, NRR trajectory, platform scalability |
| Risk focus | Key person, retention, leverage capacity | Synergy assumptions, platform dependency, data portability |

Adjust question framing and emphasis based on deal type — but the overall structure stays the same.

### Business Model Adjustments

**SaaS / subscription:**
- Heavy emphasis on ARR metrics (NRR, GRR, cohorts, expansion)
- Pricing architecture, contract terms, renewal mechanics
- Product adoption → retention correlation

**Usage-based / transactional:**
- Volume trends and predictability
- Take rate / monetization efficiency
- Customer commitment levels vs. actual consumption

**Services / implementation-heavy:**
- Services margin and whether it's a profit center or deployment cost
- Utilization rates, blended billing rates, project profitability
- Dependency between services and software retention

**Marketplace / network:**
- Supply and demand-side metrics separately
- Take rate trends and competitive pressure
- Network effects evidence and defensibility

---

## Step 5: Delivery — Formatting and Output

Deliver the DDR as a **Pattern-branded Word document (.docx)**.

**Before writing any code, read both skill files:**
```
Read: /mnt/skills/user/pattern-docx/SKILL.md
Read: {SKILL_DIR}/references/narvar-example.md
```

The narvar-example.md is the canonical formatting reference. It specifies exact font
sizes, colors, spacing, bullet levels, and the orange highlight convention. Do not
deviate from it.

### Document Formatting Spec

**Cover block** (Normal paragraphs, run-level formatting — not heading styles):
```
[Company Name]          36pt, SemiBold, color 1F4E79
Due Diligence Request List    20pt, color 2E75B6
Comprehensive Information Request | Confidential    italic, color 595959
[blank line]
CONFIDENTIAL — FOR AUTHORIZED RECIPIENTS ONLY    9pt, Bold, color C00000
```

**Page layout:**
- Size: 8.5" × 11" (US Letter)
- Margins: top=1.0in, left=0.88in, right=0.88in, bottom=0.88in
- Note: DDR uses 0.88in side margins (not the standard pattern-docx 0.5in)

**H1 — Section headers:**
- 18pt, Bold, color 1F4E79, space_before=18pt, space_after=8pt
- Numbered inline: `1. Section Name`
- Page break before: true (except first H1)

**H2 — Section subtitles:**
- 13pt, Bold, color 2E75B6, space_before=14pt, space_after=6pt
- Descriptive label (3–5 words), not a question

**List Paragraph — bullet questions:**
- Bullet character (•) at ilvl=0 for top-level questions
- Decimal numbering at ilvl=1 for sub-questions within a question
- space_before=3pt, space_after=3pt

**Orange highlight (E97132):**
- Apply to 2–4 priority/thesis-critical questions maximum
- Applied at run level — entire question text in orange
- Signals highest-priority diligence items to management

**Header and footer:**
- Must be injected via the pattern-docx Python patch script (asset pipeline)
- Do NOT attempt to write header/footer in docx-js
- Header: `[Company Name] — Due Diligence Request List` (left, gray) + `CONFIDENTIAL` (right, Bold, red)
- Footer: `[Company Name] Due Diligence` (left) + `Page X of Y` (right)
- Follow the exact pipeline in pattern-docx SKILL.md Step 3

### After Delivering the File

- Note any sections where significant company-specific customization was applied
- Flag the 2–4 orange-highlighted questions and explain why they were prioritized
- Offer to go deeper on any section or add a sector-specific module
- **Immediately run doc-quality-checker** — do not wait to be asked. State "Running
  quality check..." and produce the full issue report. If zero issues, state that explicitly.

---

## Reference Files

- `references/sector-modules.md` — Add-on DDR sections by vertical (fintech/fraud,
  logistics/supply chain, healthcare, consumer/retail)
- `references/narvar-example.md` — Canonical formatting reference and quality
  calibration standard. Load before generating any DDR.
