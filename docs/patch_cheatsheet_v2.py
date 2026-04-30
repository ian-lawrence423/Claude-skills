"""Patch Claude_Skills_CheatSheet.docx v2:
- Remove pattern-pptx row (duplicate of pattern-investment-pptx)
- Add 8 missing skills: tam-sam-som-calculator, finance-metrics-quickref,
  executive-briefing, managing-up, written-communication, giving-presentations,
  vibe-coding, skill-authoring-workflow
- Update subtitle from "21 skills · 4 layers" to "28 skills · 2 pipelines"
"""
import zipfile, shutil, os, re

SRC  = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skills_CheatSheet.docx'
DEST = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skills_CheatSheet.docx'
TMP  = r'C:/Users/IanLawrence/github/Claude-skills/docs/_tmp_cs2'

# ── row builder helper ────────────────────────────────────────────────────────
def make_row(para_base, layer, skill_name, description, output_fmt):
    p = para_base
    return (
        f'<w:tr w:rsidR="00EE7BB4" w14:paraId="{p}A0" w14:textId="77777777">'
        f'<w:tc><w:tcPr><w:tcW w:w="650" w:type="dxa"/>'
        f'<w:shd w:val="clear" w:color="auto" w:fill="E6EFFD"/>'
        f'<w:tcMar><w:top w:w="30" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
        f'<w:bottom w:w="30" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
        f'</w:tcPr>'
        f'<w:p w14:paraId="{p}A1" w14:textId="77777777" w:rsidR="00EE7BB4" w:rsidRDefault="008712F0">'
        f'<w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr>'
        f'<w:r><w:rPr><w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold"/>'
        f'<w:b/><w:color w:val="4280F4"/><w:sz w:val="16"/></w:rPr><w:t>{layer}</w:t></w:r>'
        f'</w:p></w:tc>'
        f'<w:tc><w:tcPr><w:tcW w:w="1700" w:type="dxa"/>'
        f'<w:tcMar><w:top w:w="30" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
        f'<w:bottom w:w="30" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
        f'</w:tcPr>'
        f'<w:p w14:paraId="{p}A2" w14:textId="77777777" w:rsidR="00EE7BB4" w:rsidRDefault="008712F0">'
        f'<w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>'
        f'<w:r><w:rPr><w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold"/>'
        f'<w:b/><w:color w:val="0F4761"/><w:sz w:val="17"/></w:rPr>'
        f'<w:t>{skill_name}</w:t></w:r>'
        f'</w:p></w:tc>'
        f'<w:tc><w:tcPr><w:tcW w:w="6500" w:type="dxa"/>'
        f'<w:tcMar><w:top w:w="30" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
        f'<w:bottom w:w="30" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
        f'</w:tcPr>'
        f'<w:p w14:paraId="{p}A3" w14:textId="77777777" w:rsidR="00EE7BB4" w:rsidRDefault="008712F0">'
        f'<w:pPr><w:spacing w:after="0" w:line="252" w:lineRule="auto"/></w:pPr>'
        f'<w:r><w:rPr><w:rFonts w:ascii="Wix Madefor Display" w:hAnsi="Wix Madefor Display"/>'
        f'<w:color w:val="000000"/><w:sz w:val="16"/></w:rPr>'
        f'<w:t>{description}</w:t></w:r>'
        f'</w:p></w:tc>'
        f'<w:tc><w:tcPr><w:tcW w:w="5850" w:type="dxa"/>'
        f'<w:tcMar><w:top w:w="30" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
        f'<w:bottom w:w="30" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
        f'</w:tcPr>'
        f'<w:p w14:paraId="{p}A4" w14:textId="77777777" w:rsidR="00EE7BB4" w:rsidRDefault="008712F0">'
        f'<w:pPr><w:spacing w:after="0" w:line="252" w:lineRule="auto"/></w:pPr>'
        f'<w:r><w:rPr><w:rFonts w:ascii="Wix Madefor Display" w:hAnsi="Wix Madefor Display"/>'
        f'<w:i/><w:color w:val="000000"/><w:sz w:val="16"/></w:rPr>'
        f'<w:t>{output_fmt}</w:t></w:r>'
        f'</w:p></w:tc>'
        f'</w:tr>'
    )

# ── new rows ──────────────────────────────────────────────────────────────────
TAM_ROW = make_row(
    'C1D2E3F4', 'L2',
    'tam-sam-som-calculator',
    'Market sizing with both top-down and bottom-up approaches. Labels every assumption as fact/estimate/hypothesis. '
    'Requires both methods; reconciles divergences &gt;25%. Includes sensitivity analysis on key drivers.',
    'TAM/SAM/SOM table + bottoms-up build + sensitivity matrix (inline or as structured output)'
)

MGUP_ROW = make_row(
    'D2E3F4A5', 'L5',
    'managing-up',
    'Frameworks for executive relationship management, influencing leadership without authority, '
    'and navigating organizational dynamics. Covers upward communication, alignment, and managing difficult conversations.',
    'Structured advice, communication scripts, or frameworks — no formal document output'
)

WCOM_ROW = make_row(
    'E3F4A5B6', 'L4',
    'written-communication',
    'Emails, memos, strategy documents, and announcements. Covers tone calibration for audience and stakes, '
    'structure selection (BLUF vs. narrative), and edit passes. For external communications and internal alignment.',
    'Polished email, memo, or announcement in Pattern voice'
)

PRES_ROW = make_row(
    'F4A5B6C7', 'L4',
    'giving-presentations',
    'Talk track preparation, slide deck narrative design, and presentation delivery coaching. '
    'Maps content to audience decision needs. Structures opening hook, logical flow, and close.',
    'Talk track outline, narrative arc, or slide-by-slide notes'
)

EBRF_ROW = make_row(
    'A5B6C7D8', 'L4',
    'executive-briefing',
    'Executive-ready briefing documents: memos, one-pagers, board notes, C-suite briefings. '
    'Enforces BLUF structure and decision-oriented formatting. Output is action-forcing, not informational.',
    'Pattern-branded one-pager, board note, or executive memo (.docx)'
)

FMQR_ROW = make_row(
    'B6C7D8E9', 'L2',
    'finance-metrics-quickref',
    'Quick-reference lookup for financial metric definitions, formulas, and benchmarks. '
    'Covers SaaS, PE, and general corporate finance. Returns definition, formula, and benchmark range with source.',
    'Inline definition + formula + benchmark (no separate document)'
)

VIBE_ROW = make_row(
    'C7D8E9F0', 'L7',
    'vibe-coding',
    'AI-assisted rapid prototyping — building functional tools, scripts, and apps without deep technical skills. '
    'Optimized for speed-to-working-artifact. Produces code that runs, not code that is production-ready.',
    'Working script, app, or tool (Python, JS, HTML — whatever fits the task)'
)

SAUTH_ROW = make_row(
    'D8E9F0A1', 'L8',
    'skill-authoring-workflow',
    'Standards and process for creating or updating a skill without breaking conventions. '
    'Covers SKILL.md structure, trigger language, integration rules, quality checks, and README/agents.md updates.',
    'SKILL.md file + README/agents.md entries ready to commit'
)

# ── unpack ────────────────────────────────────────────────────────────────────
if os.path.exists(TMP):
    shutil.rmtree(TMP)
with zipfile.ZipFile(SRC, 'r') as z:
    z.extractall(TMP)

with open(os.path.join(TMP, 'word', 'document.xml'), encoding='utf-8') as f:
    xml = f.read()

# ── 1. remove pattern-pptx row ────────────────────────────────────────────────
parts = xml.split('</w:tr>')
new_parts = []
removed = 0
for part in parts:
    if 'pattern-pptx</w:t>' in part and 'pattern-investment-pptx' not in part:
        removed += 1
        print('Removed: pattern-pptx row')
    else:
        new_parts.append(part)
xml = '</w:tr>'.join(new_parts)
print(f'Rows removed: {removed}')

# ── helper: insert row after anchor skill ─────────────────────────────────────
def insert_after(xml, anchor_skill, new_row, label):
    anchor = f'{anchor_skill}</w:t>'
    idx = xml.find(anchor)
    if idx == -1:
        print(f'ERROR: could not find anchor "{anchor_skill}"')
        return xml
    end_idx = xml.find('</w:tr>', idx) + len('</w:tr>')
    xml = xml[:end_idx] + new_row + xml[end_idx:]
    print(f'Inserted: {label} after {anchor_skill}')
    return xml

def insert_at_end_of_table(xml, new_row, label):
    """Insert just before the closing </w:tbl> tag of the last table."""
    idx = xml.rfind('</w:tbl>')
    if idx == -1:
        print(f'ERROR: could not find </w:tbl>')
        return xml
    xml = xml[:idx] + new_row + xml[idx:]
    print(f'Inserted: {label} at end of table')
    return xml

# ── 2. add new skill rows ─────────────────────────────────────────────────────
# tam-sam-som-calculator: after statistics-fundamentals
if 'tam-sam-som-calculator' not in xml:
    xml = insert_after(xml, 'statistics-fundamentals', TAM_ROW, 'tam-sam-som-calculator')

# managing-up: after executive-summary-writer
if 'managing-up' not in xml:
    xml = insert_after(xml, 'executive-summary-writer', MGUP_ROW, 'managing-up')

# written-communication: after pattern-investment-pptx
if 'written-communication' not in xml:
    xml = insert_after(xml, 'pattern-investment-pptx', WCOM_ROW, 'written-communication')

# giving-presentations: after written-communication
if 'giving-presentations' not in xml:
    xml = insert_after(xml, 'written-communication', PRES_ROW, 'giving-presentations')

# executive-briefing: after diligence-ddr
if 'executive-briefing' not in xml:
    xml = insert_after(xml, 'diligence-ddr', EBRF_ROW, 'executive-briefing')

# vibe-coding: after kpi-tree-builder
if 'vibe-coding' not in xml:
    xml = insert_after(xml, 'kpi-tree-builder', VIBE_ROW, 'vibe-coding')

# finance-metrics-quickref: after gtm-metrics-analyzer
if 'finance-metrics-quickref' not in xml:
    xml = insert_after(xml, 'gtm-metrics-analyzer', FMQR_ROW, 'finance-metrics-quickref')

# skill-authoring-workflow: at end of table
if 'skill-authoring-workflow' not in xml:
    xml = insert_at_end_of_table(xml, SAUTH_ROW, 'skill-authoring-workflow')

# ── 3. update subtitle ────────────────────────────────────────────────────────
# The subtitle uses bullet character · (middle dot) which may appear as ? in some encodings
# Try multiple patterns
old_subs = [
    '21 skills · 4 layers',
    '21 skills · 4 layers · Pattern Investment Team · April 2026',
    '21 skills',
]
updated = False
for old in old_subs:
    if old in xml:
        new_sub = xml.replace(old, '28 skills · 2 pipelines · Pattern Investment Team · April 2026', 1)
        if new_sub != xml:
            xml = new_sub
            print(f'Updated subtitle: found {old!r}')
            updated = True
            break

if not updated:
    # Try raw bytes search
    print('WARNING: subtitle pattern not found by string match — trying partial replace')
    if '21 skills' in xml:
        xml = xml.replace('21 skills', '28 skills', 1)
        print('Updated: replaced "21 skills" -> "28 skills"')
    if '4 layers' in xml:
        xml = xml.replace('4 layers', '2 pipelines', 1)
        print('Updated: replaced "4 layers" -> "2 pipelines"')

# ── repack ────────────────────────────────────────────────────────────────────
with open(os.path.join(TMP, 'word', 'document.xml'), 'w', encoding='utf-8') as f:
    f.write(xml)

with zipfile.ZipFile(DEST, 'w', zipfile.ZIP_DEFLATED) as zout:
    for root, dirs, files in os.walk(TMP):
        for file in files:
            fpath = os.path.join(root, file)
            arcname = os.path.relpath(fpath, TMP)
            zout.write(fpath, arcname)

shutil.rmtree(TMP)
print(f'\nSaved: {DEST}')

# ── verify ────────────────────────────────────────────────────────────────────
print('\n=== Verification ===')
with zipfile.ZipFile(DEST, 'r') as z:
    xml2 = z.read('word/document.xml').decode('utf-8')

expected = [
    'mckinsey-consultant', 'market-research', 'ntb-diligence', 'ic-memo',
    'competitive-moat-assessment', 'executive-summary-writer', 'managing-up',
    'writing-style', 'claim-scrutinizer', 'red-team', 'pre-mortem', 'boundability',
    'pattern-docx', 'pattern-investment-pptx', 'written-communication',
    'giving-presentations', 'diligence-ddr', 'executive-briefing',
    'financial-model-builder', 'doc-quality-checker', 'driver-tree',
    'statistics-fundamentals', 'tam-sam-som-calculator', 'kpi-tree-builder',
    'vibe-coding', 'gtm-metrics-analyzer', 'finance-metrics-quickref',
    'skill-authoring-workflow',
]
all_ok = True
for skill in expected:
    present = skill in xml2
    status = 'OK' if present else 'MISSING'
    print(f'  {status}: {skill}')
    if not present:
        all_ok = False

# Check pattern-pptx removed (not as standalone entry)
if 'pattern-pptx</w:t>' in xml2 and 'pattern-investment-pptx' not in xml2[xml2.find('pattern-pptx</w:t>')-200:xml2.find('pattern-pptx</w:t>')]:
    print('  WARNING: pattern-pptx still present as standalone row')
else:
    print('  OK: pattern-pptx standalone row removed')

print(f'\nAll OK: {all_ok}')
if '28 skills' in xml2:
    print('OK: subtitle updated to 28 skills')
elif '21 skills' in xml2:
    print('WARNING: subtitle still shows 21 skills')
