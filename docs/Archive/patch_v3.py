"""
patch_v3.py — Add missing skills to CheatSheet and Finance Library docx files.

CheatSheet additions (4 skills):
  - boundability          (L3 Quality)
  - competitive-landscape-deliverable (L4 Production)
  - ic-memo-pipeline      (Pipeline)
  - market-research-pipeline (Pipeline)

Finance Library additions (2 skills):
  - boundability          (L3 Quality)
  - competitive-landscape-deliverable (L4 Production)
"""

import zipfile, shutil, os

# ── helpers ───────────────────────────────────────────────────────────────────

def unpack(src, tmp):
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    with zipfile.ZipFile(src, 'r') as z:
        z.extractall(tmp)

def repack(tmp, dest):
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as zout:
        for root, dirs, files in os.walk(tmp):
            for file in files:
                fpath = os.path.join(root, file)
                arcname = os.path.relpath(fpath, tmp)
                zout.write(fpath, arcname)
    shutil.rmtree(tmp)

def insert_after(xml, anchor_skill, new_row, label):
    anchor = f'{anchor_skill}</w:t>'
    idx = xml.find(anchor)
    if idx == -1:
        print(f'  ERROR: anchor not found — {anchor_skill}')
        return xml
    end_idx = xml.find('</w:tr>', idx) + len('</w:tr>')
    xml = xml[:end_idx] + new_row + xml[end_idx:]
    print(f'  Inserted: {label} after {anchor_skill}')
    return xml

# ── CheatSheet row builder ────────────────────────────────────────────────────

def cs_row(para_base, layer, skill_name, description, output_fmt):
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

BOUND_CS = cs_row(
    'E9F0A1B2', 'L3',
    'boundability',
    'Tests geographic, segment, and product boundaries of a competitive moat — where it holds vs. degrades. '
    '6-module scoring, 5 disqualification gates. Converts load-bearing NTBs into underwriting actions.',
    'Boundary verdict per NTB + underwriting action list (inline or as structured output)'
)

CLD_CS = cs_row(
    'F0A1B2C3', 'L4',
    'competitive-landscape-deliverable',
    'Converts a competitive landscape spreadsheet (Pattern n8n pipeline output or manual) into a board-ready executive deliverable. '
    'Verdict-led layout, preserves Rating + McKinsey rationale, Pattern brand styling. '
    'Handles the full competitive-landscape-mapping template.',
    'Pattern-branded executive deliverable (.docx or structured summary)'
)

IMP_CS = cs_row(
    'A1B2C3D4', 'Pipeline',
    'ic-memo-pipeline',
    'Full 10-section IC memo pipeline: intake → market research → NTB diligence → driver tree → '
    'section drafts → 5 iteration passes → Pattern DOCX → QA. '
    'Mode flags: NTB_MODE (full/skip), KPI_MODE (full/skip).',
    'Pattern-branded IC memo (.docx) — full investment committee deliverable'
)

MRP_CS = cs_row(
    'B2C3D4E5', 'Pipeline',
    'market-research-pipeline',
    'Standalone market research report pipeline: brief → L4→L3→L2 research pyramid → '
    'theme synthesis → iterative draft passes → Pattern DOCX. '
    'Integrates mckinsey-consultant, market-research, writing-style, claim-scrutinizer.',
    'Pattern-branded market research report (.docx)'
)

# ── Finance Library row builder ───────────────────────────────────────────────

CELL = (
    '<w:tcBorders>'
    '<w:top w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:left w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:right w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '</w:tcBorders><w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/>'
    '<w:tcMar><w:top w:w="80" w:type="dxa"/><w:left w:w="120" w:type="dxa"/>'
    '<w:bottom w:w="80" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar>'
)

def fl_cell(width, text):
    return (
        f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{CELL}</w:tcPr>'
        f'<w:p><w:r><w:rPr><w:sz w:val="15"/><w:szCs w:val="15"/></w:rPr>'
        f'<w:t>{text}</w:t></w:r></w:p></w:tc>'
    )

BOUND_FL = (
    '<w:tr w:rsidR="001556A8" w14:paraId="C3D4E5F6" w14:textId="77777777">'
    + fl_cell(1200, '3 -- Quality')
    + fl_cell(2400, 'boundability')
    + fl_cell(4200,
        'Tests geographic, segment, and product boundaries of a competitive advantage. '
        '6-module scoring, 5 disqualification gates. '
        'Converts NTBs into explicit underwriting actions with boundary conditions.')
    + fl_cell(3000, 'competitive-moat-assessment, driver-tree, pre-mortem')
    + '</w:tr>'
)

CLD_FL = (
    '<w:tr w:rsidR="001556A8" w14:paraId="D4E5F6A7" w14:textId="77777777">'
    + fl_cell(1200, '4 -- Production')
    + fl_cell(2400, 'competitive-landscape-deliverable')
    + fl_cell(4200,
        'Converts a competitive landscape spreadsheet (n8n pipeline output or manual) into a '
        'board-ready executive deliverable. Verdict-led layout. '
        'Preserves Rating + McKinsey rationale with Pattern brand styling.')
    + fl_cell(3000, 'market-research, competitive-moat-assessment, pattern-docx')
    + '</w:tr>'
)

# ─────────────────────────────────────────────────────────────────────────────
# 1. PATCH CHEATSHEET
# ─────────────────────────────────────────────────────────────────────────────

CS_SRC  = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skills_CheatSheet.docx'
CS_TMP  = r'C:/Users/IanLawrence/github/Claude-skills/docs/_tmp_cs3'

print('=== Patching CheatSheet ===')
unpack(CS_SRC, CS_TMP)

with open(os.path.join(CS_TMP, 'word', 'document.xml'), encoding='utf-8') as f:
    xml = f.read()

if 'boundability' not in xml:
    xml = insert_after(xml, 'pre-mortem', BOUND_CS, 'boundability')
else:
    print('  SKIP: boundability already present')

if 'competitive-landscape-deliverable' not in xml:
    xml = insert_after(xml, 'skill-authoring-workflow', CLD_CS, 'competitive-landscape-deliverable')
else:
    print('  SKIP: competitive-landscape-deliverable already present')

if 'ic-memo-pipeline' not in xml:
    xml = insert_after(xml, 'competitive-landscape-deliverable', IMP_CS, 'ic-memo-pipeline')
else:
    print('  SKIP: ic-memo-pipeline already present')

if 'market-research-pipeline' not in xml:
    xml = insert_after(xml, 'ic-memo-pipeline', MRP_CS, 'market-research-pipeline')
else:
    print('  SKIP: market-research-pipeline already present')

# Update skill count in subtitle
for old, new in [('28 skills', '31 skills'), ('27 skills', '31 skills')]:
    if old in xml:
        xml = xml.replace(old, '31 skills', 1)
        print(f'  Updated subtitle: {old} -> 31 skills')

with open(os.path.join(CS_TMP, 'word', 'document.xml'), 'w', encoding='utf-8') as f:
    f.write(xml)

repack(CS_TMP, CS_SRC)
print('  Saved CheatSheet\n')

# verify
with zipfile.ZipFile(CS_SRC, 'r') as z:
    xml2 = z.read('word/document.xml').decode('utf-8')
for skill in ['boundability', 'competitive-landscape-deliverable', 'ic-memo-pipeline', 'market-research-pipeline']:
    status = 'OK' if skill in xml2 else 'MISSING'
    print(f'  {status}: {skill}')

# ─────────────────────────────────────────────────────────────────────────────
# 2. PATCH FINANCE LIBRARY
# ─────────────────────────────────────────────────────────────────────────────

FL_SRC  = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skill_Library_External (Finance).docx'
FL_TMP  = r'C:/Users/IanLawrence/github/Claude-skills/docs/_tmp_fl2'

print('\n=== Patching Finance Library ===')
unpack(FL_SRC, FL_TMP)

with open(os.path.join(FL_TMP, 'word', 'document.xml'), encoding='utf-8') as f:
    xml = f.read()

if 'boundability' not in xml:
    xml = insert_after(xml, 'red-team', BOUND_FL, 'boundability')
else:
    print('  SKIP: boundability already present')

if 'competitive-landscape-deliverable' not in xml:
    xml = insert_after(xml, 'pattern-investment-pptx', CLD_FL, 'competitive-landscape-deliverable')
else:
    print('  SKIP: competitive-landscape-deliverable already present')

# Update count
for old, new in [('25 skills', '27 skills'), ('26 skills', '27 skills'), ('24 skills', '27 skills')]:
    if old in xml:
        xml = xml.replace(old, '27 skills', 1)
        print(f'  Updated count: {old} -> 27 skills')

with open(os.path.join(FL_TMP, 'word', 'document.xml'), 'w', encoding='utf-8') as f:
    f.write(xml)

repack(FL_TMP, FL_SRC)
print('  Saved Finance Library\n')

# verify
with zipfile.ZipFile(FL_SRC, 'r') as z:
    xml3 = z.read('word/document.xml').decode('utf-8')
for skill in ['boundability', 'competitive-landscape-deliverable']:
    status = 'OK' if skill in xml3 else 'MISSING'
    print(f'  {status}: {skill}')
