"""
patch_reorder_layers.py

Reorganises skill inventory tables in both documents into strict layer order.

Finance Library v3 changes:
  - Merges 6 stray L2 rows (driver-tree etc.) into the main inventory
  - Adds missing: boundability (L3), ntb-diligence (L2), earnings-reviewer consolidated (L5)
  - Moves competitive-landscape-deliverable to L4 position
  - Cleans up duplicate architecture-table rows for earnings-reviewer
  - Normalises all rows to main-inventory column widths (1800/1400/4700/2900)
  - Layer order: L1 → L2 → L3 → L4 → L4b → L5

CheatSheet changes:
  - Moves L2 skills (driver-tree, tam-sam-som, etc.) from rows 021-027 up to L2 block
  - Moves competitive-landscape-deliverable from row 029 to L4 block
  - Moves managing-up (L5) from row 007 to after L4b block
  - Everything else stays in place
"""

import zipfile, shutil, os, re

# ── helpers ───────────────────────────────────────────────────────────────────
def unpack(src, tmp):
    if os.path.exists(tmp): shutil.rmtree(tmp)
    with zipfile.ZipFile(src, 'r') as z:
        z.extractall(tmp)

def save(tmp, dest):
    """Write to a new file (avoids mount overwrite restriction)."""
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as zout:
        for root, dirs, files in os.walk(tmp):
            for file in files:
                fp = os.path.join(root, file)
                zout.write(fp, os.path.relpath(fp, tmp))
    shutil.rmtree(tmp)

# ── Finance Library row builder ───────────────────────────────────────────────
# Main inventory column widths: Skill=1800, Layer=1400, Description=4700, Depends=2900

BORDER = (
    '<w:tcBorders>'
    '<w:top w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:left w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:right w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '</w:tcBorders>'
)
MAR = '<w:tcMar><w:top w:w="80" w:type="dxa"/><w:left w:w="120" w:type="dxa"/><w:bottom w:w="80" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar>'

def fl_cell(width, text, fill='F2F2F2'):
    shd = f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>'
    return (
        f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{BORDER}{shd}{MAR}</w:tcPr>'
        f'<w:p><w:r><w:rPr><w:sz w:val="15"/><w:szCs w:val="15"/></w:rPr>'
        f'<w:t xml:space="preserve">{text}</w:t></w:r></w:p></w:tc>'
    )

def fl_row(pid, skill, layer, desc, depends, fill='F2F2F2'):
    return (
        f'<w:tr w:rsidR="001556A8" w14:paraId="{pid}" w14:textId="77777777">'
        + fl_cell(1800, skill, fill)
        + fl_cell(1400, layer, fill)
        + fl_cell(4700, desc, fill)
        + fl_cell(2900, depends, fill)
        + '</w:tr>'
    )

# ── Complete Finance Library inventory in target order ────────────────────────
# Format: (paraId, skill_name, layer, description, depends_on)

FL_ROWS = [
    # ── L1 ────────────────────────────────────────────────────────────────────
    ('2A4C7915', 'mckinsey-consultant *',
     '1 — Analytical OS',
     'Problem structuring, MECE trees, 7 strategy dimensions, Six Screening Questions, Pyramid Principle, analytical modules. Investment Evaluation Mode governs 5 mandatory IC memo components: Gate scoring tables, NTB registry, 5-point NTB thesis, returns disaggregation table, information gaps table.',
     'investment-evaluation-framework.md'),

    # ── L2 ────────────────────────────────────────────────────────────────────
    ('13D05053', 'market-research *',
     '2 — Research',
     'Full research workflow: intake → brief → pyramid (L4→L3→L2→L2b→L1) → deep dive A/B/C → draft → iteration loop. NTB Alignment Check at end of Phase 3 confirms evidence maps to each NTB before drafting. NTB Evidence Summary section for IC memo feeds.',
     'mckinsey-consultant, writing-style, claim-scrutinizer, red-team, competitive-moat-assessment (L2b), pattern-docx / pattern-investment-pptx'),

    ('1DEB3F06', 'competitive-moat-assessment *',
     '2 — Research',
     '5-step moat evidence methodology: classify → existence test → strength rating → durability → verdict. Market-wide moat scorecard mode for deep dive. Mandatory at L2b in all market research.',
     'writing-style, red-team-investment-attacks.md'),

    ('38B5E38B', 'ic-memo *',
     '2 — Research',
     'IC memo document architecture: 10-section structure, length calibration, gates mapped to sections. Requires NTB registry in exec summary, Gate 2 12-criterion scorecard in market analysis, and 5-point NTB-structured thesis in Section 4.',
     'investment-evaluation-framework.md, market-research, competitive-moat-assessment, mckinsey-consultant, writing-style, claim-scrutinizer, red-team, pre-mortem, pattern-docx'),

    ('29CCED29', 'executive-summary-writer',
     '2 — Research',
     'Compresses completed analysis into publication-ready executive summary. Four format variants: one-page memo, deck slide, briefing paragraph, multi-section summary.',
     'writing-style, claim-scrutinizer, pattern-docx / pattern-investment-pptx'),

    ('D1E2F3A4', 'driver-tree',
     '2 — Research',
     'Decomposes investment thesis into causal driver tree — revenue, cost, capital, and competitive dynamics. Maps each driver to NTBs and MOIC outcomes.',
     'mckinsey-consultant'),

    ('D2E3F4A5', 'tam-sam-som-calculator',
     '2 — Research',
     'Market sizing — TAM/SAM/SOM with bottoms-up and tops-down approaches, labeled assumptions (fact/estimate/hypothesis), and sensitivity analysis.',
     'mckinsey-consultant'),

    ('D3E4F5A6', 'statistics-fundamentals',
     '2 — Research',
     'Applied statistics for investment analysis — regression interpretation, confidence intervals, A/B test validity, correlation vs. causation, and common statistical errors.',
     'None — leaf skill'),

    ('D4E5F6A7', 'finance-metrics-quickref',
     '2 — Research',
     'Quick-reference lookup for financial metric definitions, formulas, and benchmarks. Covers SaaS, PE, and general corporate finance metrics.',
     'None — leaf skill'),

    ('D5E6F7A8', 'kpi-tree-builder',
     '2 — Research',
     'Decomposes a budget, forecast, or operating target into causal drivers and atomic inputs. Two modes: diligence (audit management budget credibility) and post-close (define tracking architecture). Produces KPI tree, driver dictionary, and tracking pack.',
     'driver-tree, ntb-diligence'),

    ('D6E7F8A9', 'gtm-metrics-analyzer',
     '2 — Research',
     'Builds a 4-tab GTM diagnostic workbook from uploaded source files. Calculates 48 metrics across 6 families: ARR funnel, pipeline, retention, efficiency &amp; economics, team &amp; productivity, fiscal maturity. Separates provided inputs from derived outputs. Requires Excel 365/2019+.',
     'financial-model-builder, driver-tree, ntb-diligence, kpi-tree-builder'),

    ('D7E8F9B1', 'ntb-diligence',
     '2 — Research',
     'Stress-tests each candidate NTB for investment thesis validity: confirms the NTB is real, bounded, and actionable at entry. Produces NTB registry with confidence ratings, underwriting conditions, and open diligence items per NTB.',
     'mckinsey-consultant, driver-tree'),

    # ── L3 ────────────────────────────────────────────────────────────────────
    ('0F090DE4', 'writing-style *',
     '3 — Quality',
     'Prose standards and claim discipline. Runs on all prose before code is generated. Five-step self-review: claim tagging, absolute assertion test (includes Group E — draft artifact language), inductive chain check, data gap flagging, prose standards.',
     'None — leaf skill'),

    ('36839D53', 'claim-scrutinizer *',
     '3 — Quality',
     'Seven-part claim test, assumption audit, derivative integrity, base rate checks. Type A (investment docs): Six Screening Questions as analytical lens. Section 5: IC Memo Structure Check — verifies NTB registry, Gate 2 scorecard, NTB-structured thesis, returns table, and NTB↔returns linkage.',
     'investment-evaluation-framework.md (Type A), VALIDATION_FRAMEWORKS.md'),

    ('392A6B64', 'red-team',
     '3 — Quality',
     'Adversarial stress-test. Attack vectors, kill scenarios, bear case, adversarial scorecard. Type A (investment): investment attack lenses.',
     'red-team-investment-attacks.md (Type A), investment-evaluation-framework.md'),

    ('109F325F', 'pre-mortem *',
     '3 — Quality',
     'Failure mode inventory across 10 structural categories. Assumes the deal has failed and works backward. Diagnoses information state (B1/B2/B3 boundability). Maps every failure mode to the NTB it threatens. Step 4d: NTB Gap Prioritisation — ranks unresolved NTBs by MOIC impact.',
     'claim-scrutinizer (cross-reference if already run), investment-evaluation-framework.md'),

    ('C3D4E5F6', 'boundability',
     '3 — Quality',
     'Tests geographic, segment, and product boundaries of a competitive advantage. 6-module scoring, 5 disqualification gates. Converts NTBs into explicit underwriting actions with boundary conditions.',
     'competitive-moat-assessment, driver-tree, pre-mortem'),

    # ── L4 ────────────────────────────────────────────────────────────────────
    ('D4E5F6A7', 'competitive-landscape-deliverable',
     '4 — Production',
     'Converts a competitive landscape spreadsheet (n8n pipeline output or manual) into a board-ready executive deliverable. Verdict-led layout. Preserves Rating + McKinsey rationale with Pattern brand styling.',
     'market-research, competitive-moat-assessment, pattern-docx'),

    ('5A96B3F2', 'pattern-docx',
     '4 — Production',
     'Pattern-branded Word documents. Two-phase build: docx-js body + Python XML patch transplanted into canonical template shell (header with logo anchor + gradient line; footer with SVG icon mark). writing-style runs before code; doc-quality-checker auto-runs after delivery.',
     'public/docx skill, writing-style, doc-quality-checker, pattern assets, canonical template .docx'),

    ('2EB7DBD6', 'pattern-investment-pptx',
     '4 — Production',
     'Institutional-grade investment decks for IC, PE firms, acquirers. Use for all investment or deal materials. writing-style + doc-quality-checker in loop.',
     'public/pptx skill, writing-style, doc-quality-checker, pattern assets'),

    ('72EA9DEA', 'pattern-pptx',
     '4 — Production',
     'General Pattern-branded presentations. For internal, operational, partner content — not investment materials.',
     'public/pptx skill'),

    ('773A1B79', 'diligence-ddr',
     '4 — Production',
     'Generates or customizes DDRs for PE buyout / M&amp;A sell-side. Tailored to business model and sector.',
     'pattern-docx, writing-style (narrative only), doc-quality-checker, sector-modules.md'),

    ('169D5125', 'financial-model-builder',
     '4 — Production',
     'Reads source Excel P&amp;L and builds standardized 3-tab model: Input Page + Financial Model Template + Output Tab. 6+6 analysis (actuals + forecast).',
     'Source Excel file (required upload)'),

    # ── L4b ───────────────────────────────────────────────────────────────────
    ('610CF682', 'doc-quality-checker *',
     '4b — QA',
     'Auto-runs after every pattern-docx or pattern-investment-pptx output. Checks brand compliance, formatting, structural logic, table integrity, narrative flow. Draft artifact language check: flags version labels, changelog subtitles, "pre-mortem addition:" prefixes, FM codes in body text — all at CRITICAL severity.',
     'pattern-docx or pattern-investment-pptx brand spec'),

    # ── L5 ────────────────────────────────────────────────────────────────────
    ('E0F1A2B3', 'earnings-reviewer  (plugin · 6 skills)',
     '5 — Equity Research',
     'earnings-analysis: 8–12 page institutional earnings update with beat/miss, segment breakdown, updated estimates, 8–12 charts, clickable citations. | earnings-preview: pre-earnings scenarios and key metrics to watch. | model-update: plugs actuals into XLSX model, adjusts estimates. | morning-note: 7am morning call notes, 200–400 words. | audit-xls: formula audit with model integrity checks. | xlsx-author: headless XLSX authoring.',
     'pattern-docx, writing-style, doc-quality-checker; Python (matplotlib, pandas); source Excel upload (model-update, audit-xls)'),
]

# ═════════════════════════════════════════════════════════════════════════════
# 1. PATCH FINANCE LIBRARY
# ═════════════════════════════════════════════════════════════════════════════
FL_SRC = '/sessions/modest-keen-davinci/mnt/docs/Claude_Skill_Library_External (Finance)_v3.docx'
FL_TMP = '/tmp/patch_reorder_fl'
FL_OUT = '/sessions/modest-keen-davinci/mnt/docs/Claude_Skill_Library_External (Finance)_v4.docx'

print('=== Rebuilding Finance Library inventory ===')
unpack(FL_SRC, FL_TMP)

with open(os.path.join(FL_TMP, 'word', 'document.xml'), encoding='utf-8') as f:
    xml = f.read()

# 1a. Find inventory table boundaries
inv_header_pos = xml.find('What it does')
beats_pos = xml.find('BEAT 1')

# Extract the header row XML
pre_inv = xml[:inv_header_pos]
last_tr_start = pre_inv.rfind('<w:tr ')
header_row_end = xml.find('</w:tr>', inv_header_pos) + len('</w:tr>')
header_row = xml[last_tr_start:header_row_end]

# The inventory section: from start of header row to end of last data row
# (end of doc-quality-checker row, just before BEAT 1)
inv_table_start = last_tr_start
# Find the </w:tbl> after the inventory rows (before BEAT 1)
# The inventory rows end at doc-quality-checker then the table closes
# Find the position of the table end tag after the last inventory row
after_dqc = xml.rfind('doc-quality-checker', inv_header_pos, beats_pos)
inv_table_end = xml.find('</w:tr>', after_dqc) + len('</w:tr>')

print(f'  Inventory header row starts at: {inv_table_start}')
print(f'  Last inventory row ends at: {inv_table_end}')
print(f'  Content span: {inv_table_end - inv_table_start} chars')

# 1b. Build new inventory rows
new_rows = [header_row]
for pid, skill, layer, desc, depends in FL_ROWS:
    new_rows.append(fl_row(pid, skill, layer, desc, depends))

new_inventory = ''.join(new_rows)

# 1c. Replace
xml = xml[:inv_table_start] + new_inventory + xml[inv_table_end:]

# 1d. Also clean up the stray table rows BEFORE the inventory
# The stray rows are in the architecture table area — find and remove the
# duplicate rows (driver-tree etc. that are no longer needed there)
# Remove individual earnings-reviewer row (duplicate) from arch table
for stray_skill in ['driver-tree', 'tam-sam-som-calculator', 'statistics-fundamentals',
                     'finance-metrics-quickref', 'kpi-tree-builder', 'gtm-metrics-analyzer']:
    # Find and remove the stray <w:tr> containing this skill
    idx = xml.find(stray_skill)
    if idx != -1 and idx < inv_table_start:
        # check it's before inventory (stray)
        row_start = xml.rfind('<w:tr ', 0, idx)
        row_end = xml.find('</w:tr>', idx) + len('</w:tr>')
        if row_end < inv_table_start + 50000:  # safety check
            xml = xml[:row_start] + xml[row_end:]
            print(f'  Removed stray row: {stray_skill}')
            # Recalculate inv_table_start after removal
            inv_table_start -= (row_end - row_start)

# Remove duplicate earnings-reviewer rows from arch area
# Keep only the "5 — Equity Research" architecture summary row
for dup_text in ['plugin · 6 skills', 'Earnings update reports, pre-earnings previews']:
    idx = xml.find(dup_text)
    if idx != -1:
        row_start = xml.rfind('<w:tr ', 0, idx)
        row_end = xml.find('</w:tr>', idx) + len('</w:tr>')
        xml = xml[:row_start] + xml[row_end:]
        print(f'  Removed duplicate arch row containing: {dup_text[:40]}')

with open(os.path.join(FL_TMP, 'word', 'document.xml'), 'w', encoding='utf-8') as f:
    f.write(xml)

save(FL_TMP, FL_OUT)
print(f'\n  Saved: {FL_OUT}  ({os.path.getsize(FL_OUT):,} bytes)')

# 1e. Verify
with zipfile.ZipFile(FL_OUT) as z:
    xml2 = z.read('word/document.xml').decode()

inv2 = xml2[xml2.find('What it does'):xml2.find('BEAT 1')]
rows2 = re.findall(r'<w:tr\b[^>]*>.*?</w:tr>', inv2, re.DOTALL)
print(f'\n  Inventory rows (excl. header): {len(rows2)}  (expected 25 incl header = 24 data)')

print('\n  Layer order check:')
for row in rows2:
    texts = re.findall(r'<w:t[^>]*>([^<]+)</w:t>', row)
    texts = [t.strip() for t in texts if t.strip() and len(t.strip()) > 1]
    if texts and len(texts) >= 2:
        print(f'    {texts[1]:<20} | {texts[0]}')

# ═════════════════════════════════════════════════════════════════════════════
# 2. PATCH CHEATSHEET
# ═════════════════════════════════════════════════════════════════════════════
CS_SRC = '/sessions/modest-keen-davinci/mnt/docs/Claude_Skills_CheatSheet.docx'
CS_TMP = '/tmp/patch_reorder_cs'
CS_OUT = '/sessions/modest-keen-davinci/mnt/docs/Claude_Skills_CheatSheet_v2.docx'

print('\n\n=== Reordering CheatSheet ===')
unpack(CS_SRC, CS_TMP)

with open(os.path.join(CS_TMP, 'word', 'document.xml'), encoding='utf-8') as f:
    cs_xml = f.read()

# Extract all rows
all_rows = re.findall(r'<w:tr\b[^>]*>.*?</w:tr>', cs_xml, re.DOTALL)
print(f'  Total rows: {len(all_rows)}')

# Identify each row by its text content
def get_skill_name(row):
    texts = re.findall(r'<w:t[^>]*>([^<]+)</w:t>', row)
    texts = [t.strip() for t in texts if t.strip() and len(t.strip()) > 1]
    return texts[1] if len(texts) >= 2 else (texts[0] if texts else '')

def get_layer(row):
    texts = re.findall(r'<w:t[^>]*>([^<]+)</w:t>', row)
    texts = [t.strip() for t in texts if t.strip() and len(t.strip()) > 1]
    return texts[0] if texts else ''

# Map skill name -> row XML
skill_row_map = {}
header_rows = []
for row in all_rows:
    layer = get_layer(row)
    skill = get_skill_name(row)
    if layer in ('Skill', 'Say this...'):
        header_rows.append(('__header__' + layer, row))
    elif any(x in layer for x in ['L1','L2','L3','L4','L5','Pipeline']):
        skill_row_map[skill] = row
    else:
        header_rows.append(('__other__' + layer[:20], row))

print(f'  Skill rows found: {len(skill_row_map)}')
print(f'  Header/other rows: {len(header_rows)}')

# Define target order (skill names as keys into skill_row_map)
TARGET_ORDER = [
    # L1
    'mckinsey-consultant',
    # L2
    'market-research',
    'ntb-diligence',
    'ic-memo',
    'competitive-moat-assessment',
    'executive-summary-writer',
    'driver-tree',
    'statistics-fundamentals',
    'tam-sam-som-calculator',
    'kpi-tree-builder',
    'gtm-metrics-analyzer',
    'finance-metrics-quickref',
    # L3
    'writing-style',
    'claim-scrutinizer',
    'red-team',
    'pre-mortem',
    'boundability',
    # L4
    'pattern-docx',
    'pattern-investment-pptx',
    'written-communication',
    'giving-presentations',
    'diligence-ddr',
    'executive-briefing',
    'financial-model-builder',
    'doc-quality-checker',
    'competitive-landscape-deliverable',
    # L5
    'managing-up',
    # Pipeline
    'ic-memo-pipeline',
    'market-research-pipeline',
]

# Build new sorted rows block
sorted_rows = []
for target in TARGET_ORDER:
    # Find in map (handle asterisk variants)
    found = None
    for key in skill_row_map:
        if key.startswith(target):
            found = skill_row_map[key]
            break
    if found:
        sorted_rows.append(found)
        print(f'  ✓ {target}')
    else:
        print(f'  ✗ NOT FOUND: {target}')

# Replace all skill rows in the XML with the sorted block
# Strategy: find the first skill row and last skill row, replace entire block
first_skill_start = cs_xml.find(all_rows[1])  # row 1 = first skill (after header)
# Actually find by pattern matching the first data row
# Find the span covering all skill rows
first_row_idx = None
last_row_idx = None
for i, row in enumerate(all_rows):
    layer = get_layer(row)
    if any(x in layer for x in ['L1','L2','L3','L4','L5','Pipeline']):
        if first_row_idx is None: first_row_idx = i
        last_row_idx = i

first_data_row = all_rows[first_row_idx]
last_data_row = all_rows[last_row_idx]

start_pos = cs_xml.find(first_data_row)
end_pos = cs_xml.find(last_data_row) + len(last_data_row)

print(f'\n  Replacing rows {first_row_idx}–{last_row_idx} (span: {end_pos-start_pos} chars)')

cs_xml = cs_xml[:start_pos] + ''.join(sorted_rows) + cs_xml[end_pos:]

with open(os.path.join(CS_TMP, 'word', 'document.xml'), 'w', encoding='utf-8') as f:
    f.write(cs_xml)

save(CS_TMP, CS_OUT)
print(f'\n  Saved: {CS_OUT}  ({os.path.getsize(CS_OUT):,} bytes)')

# 2b. Verify
with zipfile.ZipFile(CS_OUT) as z:
    cs_xml2 = z.read('word/document.xml').decode()

print('\n  CheatSheet layer order check:')
rows2 = re.findall(r'<w:tr\b[^>]*>.*?</w:tr>', cs_xml2, re.DOTALL)
for row in rows2:
    texts = re.findall(r'<w:t[^>]*>([^<]+)</w:t>', row)
    texts = [t.strip() for t in texts if t.strip() and len(t.strip()) > 1]
    if texts and len(texts) >= 2 and any(x in texts[0] for x in ['L1','L2','L3','L4','L5','Pipeline']):
        print(f'    {texts[0]:<14} | {texts[1]}')

print('\nDone.')
