"""
patch_docs_v3.py
================
Updates both docs to reflect skills added since April 29, 2026:

CheatSheet_v2.docx  (currently "31 skills"):
  + vibe-coding            L7
  + skill-authoring-workflow  L8
  + deal-workbook-builder  L4
  + earnings-reviewer      Plugin (summary row)
  → subtitle: "35 skills · 2 pipelines · 1 plugin · Pattern Investment Team · May 2026"

Claude_Skill_Library_External (Finance)_v6.docx  (currently "30 skills"):
  + managing-up            L4 -- Production
  + written-communication  L4 -- Production
  + giving-presentations   L4 -- Production
  + executive-briefing     L4 -- Production
  + vibe-coding            L6 -- Utility
  + skill-authoring-workflow  L6 -- Utility
  + deal-workbook-builder  L4 -- Production
  → subtitle: "37 skills"
"""
import zipfile, shutil, os

# ─────────────────────────────────────────────────────────────────────────────
# CheatSheet helpers
# ─────────────────────────────────────────────────────────────────────────────

def cs_make_row(para_base, layer, skill_name, description, output_fmt):
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

# ─────────────────────────────────────────────────────────────────────────────
# Library helpers
# ─────────────────────────────────────────────────────────────────────────────

FL_CELL_STYLE = (
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
        f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{FL_CELL_STYLE}</w:tcPr>'
        f'<w:p><w:r><w:rPr><w:sz w:val="15"/><w:szCs w:val="15"/></w:rPr>'
        f'<w:t xml:space="preserve">{text}</w:t></w:r></w:p></w:tc>'
    )

def fl_row(para_id, layer, skill, description, depends):
    return (
        f'<w:tr w:rsidR="001556A8" w14:paraId="{para_id}" w14:textId="77777777">'
        + fl_cell(1200, layer)
        + fl_cell(2400, skill)
        + fl_cell(4200, description)
        + fl_cell(3000, depends)
        + '</w:tr>'
    )

# ─────────────────────────────────────────────────────────────────────────────
# Shared helpers
# ─────────────────────────────────────────────────────────────────────────────

def insert_after(xml, anchor_skill, new_row, label):
    anchor = f'{anchor_skill}</w:t>'
    idx = xml.find(anchor)
    if idx == -1:
        print(f'  ERROR: anchor not found — {anchor_skill!r}')
        return xml
    end_idx = xml.find('</w:tr>', idx) + len('</w:tr>')
    xml = xml[:end_idx] + new_row + xml[end_idx:]
    print(f'  Inserted: {label} after {anchor_skill}')
    return xml

def insert_before_last_table_close(xml, new_row, label):
    idx = xml.rfind('</w:tbl>')
    if idx == -1:
        print(f'  ERROR: </w:tbl> not found')
        return xml
    xml = xml[:idx] + new_row + xml[idx:]
    print(f'  Inserted: {label} at end of last table')
    return xml

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

# ─────────────────────────────────────────────────────────────────────────────
# New rows — CheatSheet
# ─────────────────────────────────────────────────────────────────────────────

CS_VIBE = cs_make_row(
    'A1B2C3D4', 'L7',
    'vibe-coding',
    'AI-assisted rapid prototyping — building functional tools, scripts, and apps without deep technical skills. '
    'Optimized for speed-to-working-artifact. Produces code that runs, not production-ready code.',
    'Working script, app, or tool (Python, JS, HTML — whatever fits the task)'
)

CS_SAUTH = cs_make_row(
    'B2C3D4E5', 'L8',
    'skill-authoring-workflow',
    'Standards and process for creating or updating a skill without breaking conventions. '
    'Covers SKILL.md structure, trigger language, integration rules, quality checks, and README/agents.md updates.',
    'SKILL.md + README/agents.md entries ready to commit'
)

CS_DWB = cs_make_row(
    'C3D4E5F6', 'L4',
    'deal-workbook-builder',
    'Builds and maintains the PE/M&amp;A deal workbook: formula-linked Driver Tree, KPI Tree, NTB Registry, '
    'and MOIC Bridge tabs chained to the FINANCIAL MODEL. Variance columns smart-formatted (ppt for margins, '
    '% for volumes). Runs automated quality checks after every build.',
    'Deal workbook (.xlsx) — Driver Tree, KPI Tree, NTB Registry, MOIC Bridge linked to source model'
)

CS_ER = cs_make_row(
    'D4E5F6A7', 'Plugin',
    'earnings-reviewer',
    '6-skill equity research plugin: earnings-analysis, earnings-preview, model-update, morning-note, '
    'audit-xls, xlsx-author. Processes an earnings event end-to-end — reads transcript, updates coverage '
    'model, and drafts the post-earnings note.',
    'Post-earnings note (.docx), updated model (.xlsx), morning call note'
)

# ─────────────────────────────────────────────────────────────────────────────
# New rows — Library
# ─────────────────────────────────────────────────────────────────────────────

FL_MANAGING_UP = fl_row(
    'F1A2B3C4',
    '4 -- Production',
    'managing-up',
    'Frameworks for executive relationship management, influencing leadership without authority, '
    'and navigating organizational dynamics. Covers upward communication, alignment, and managing difficult conversations.',
    'mckinsey-consultant, writing-style'
)

FL_WCOM = fl_row(
    'F2A3B4C5',
    '4 -- Production',
    'written-communication',
    'Emails, memos, strategy documents, and announcements. Tone calibration for audience and stakes, '
    'structure selection (BLUF vs. narrative), and edit passes. For external communications and internal alignment.',
    'writing-style, mckinsey-consultant'
)

FL_PRES = fl_row(
    'F3A4B5C6',
    '4 -- Production',
    'giving-presentations',
    'Talk track preparation, slide deck narrative design, and delivery coaching. '
    'Maps content to audience decision needs. Structures opening hook, logical flow, and close.',
    'writing-style, mckinsey-consultant'
)

FL_EBRF = fl_row(
    'F4A5B6C7',
    '4 -- Production',
    'executive-briefing',
    'Executive-ready briefing documents: memos, one-pagers, board notes, C-suite briefings. '
    'Enforces BLUF structure and decision-oriented formatting. Output is action-forcing, not informational.',
    'pattern-docx, writing-style'
)

FL_VIBE = fl_row(
    'F5A6B7C8',
    '6 -- Utility',
    'vibe-coding',
    'AI-assisted rapid prototyping for functional tools, scripts, and apps. '
    'Optimized for speed-to-working-artifact. Useful for one-off data transforms, scrapers, and automation.',
    'None — standalone'
)

FL_SAUTH = fl_row(
    'F6A7B8C9',
    '6 -- Utility',
    'skill-authoring-workflow',
    'Standards and process for creating or updating a skill. '
    'Covers SKILL.md structure, trigger language, integration rules, quality checks, and README/agents.md updates.',
    'None — meta-skill'
)

FL_DWB = fl_row(
    'F7A8B9C0',
    '4 -- Production',
    'deal-workbook-builder',
    'Builds and maintains the PE/M&amp;A deal workbook: formula-linked Driver Tree, KPI Tree, NTB Registry, '
    'and MOIC Bridge tabs chained to the FINANCIAL MODEL. Variance columns smart-formatted (ppt for margins, '
    '% for volumes). Automated quality checks after every build.',
    'financial-model-builder, driver-tree, kpi-tree-builder, ntb-diligence'
)

# ─────────────────────────────────────────────────────────────────────────────
# Patch CheatSheet
# ─────────────────────────────────────────────────────────────────────────────

CS_SRC  = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skills_CheatSheet_v2.docx'
CS_DEST = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skills_CheatSheet_v2.docx'
CS_TMP  = r'C:/Users/IanLawrence/github/Claude-skills/docs/_tmp_cs3'

print('=== Patching CheatSheet ===')
unpack(CS_SRC, CS_TMP)
with open(os.path.join(CS_TMP, 'word', 'document.xml'), encoding='utf-8') as f:
    xml = f.read()

if 'vibe-coding' not in xml:
    xml = insert_after(xml, 'kpi-tree-builder', CS_VIBE, 'vibe-coding')
else:
    print('  SKIP: vibe-coding already present')

if 'skill-authoring-workflow' not in xml:
    xml = insert_after(xml, 'vibe-coding', CS_SAUTH, 'skill-authoring-workflow')
else:
    print('  SKIP: skill-authoring-workflow already present')

if 'deal-workbook-builder' not in xml:
    xml = insert_after(xml, 'driver-tree', CS_DWB, 'deal-workbook-builder')
else:
    print('  SKIP: deal-workbook-builder already present')

if 'earnings-reviewer' not in xml:
    xml = insert_before_last_table_close(xml, CS_ER, 'earnings-reviewer')
else:
    print('  SKIP: earnings-reviewer already present')

# Update subtitle
for old in ['35 skills', '34 skills', '33 skills', '32 skills', '31 skills',
            '30 skills', '29 skills', '28 skills']:
    if old in xml:
        xml = xml.replace(old, '35 skills', 1)
        print(f'  Updated count: {old!r} -> 35 skills')
        break

for old in ['April 2026', 'March 2026']:
    if old in xml:
        xml = xml.replace(old, 'May 2026', 1)
        print(f'  Updated date: {old!r} -> May 2026')
        break

with open(os.path.join(CS_TMP, 'word', 'document.xml'), 'w', encoding='utf-8') as f:
    f.write(xml)
repack(CS_TMP, CS_DEST)
print(f'  Saved: {CS_DEST}')

# verify
with zipfile.ZipFile(CS_DEST) as z:
    xml2 = z.read('word/document.xml').decode('utf-8')
for skill in ['vibe-coding', 'skill-authoring-workflow', 'deal-workbook-builder', 'earnings-reviewer', '35 skills', 'May 2026']:
    status = 'OK' if skill in xml2 else 'MISSING'
    print(f'  {status}: {skill}')

# ─────────────────────────────────────────────────────────────────────────────
# Patch Library
# ─────────────────────────────────────────────────────────────────────────────

FL_SRC  = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skill_Library_External (Finance)_v6.docx'
FL_DEST = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skill_Library_External (Finance)_v6.docx'
FL_TMP  = r'C:/Users/IanLawrence/github/Claude-skills/docs/_tmp_fl3'

print('\n=== Patching Library ===')
unpack(FL_SRC, FL_TMP)
with open(os.path.join(FL_TMP, 'word', 'document.xml'), encoding='utf-8') as f:
    xml = f.read()

# Insert after pattern-investment-pptx (last Production skill before QA/ER block)
if 'managing-up' not in xml:
    xml = insert_after(xml, 'pattern-investment-pptx', FL_MANAGING_UP, 'managing-up')
else:
    print('  SKIP: managing-up already present')

if 'written-communication' not in xml:
    xml = insert_after(xml, 'managing-up', FL_WCOM, 'written-communication')
else:
    print('  SKIP: written-communication already present')

if 'giving-presentations' not in xml:
    xml = insert_after(xml, 'written-communication', FL_PRES, 'giving-presentations')
else:
    print('  SKIP: giving-presentations already present')

if 'executive-briefing' not in xml:
    xml = insert_after(xml, 'giving-presentations', FL_EBRF, 'executive-briefing')
else:
    print('  SKIP: executive-briefing already present')

if 'vibe-coding' not in xml:
    xml = insert_after(xml, 'executive-briefing', FL_VIBE, 'vibe-coding')
else:
    print('  SKIP: vibe-coding already present')

if 'skill-authoring-workflow' not in xml:
    xml = insert_after(xml, 'vibe-coding', FL_SAUTH, 'skill-authoring-workflow')
else:
    print('  SKIP: skill-authoring-workflow already present')

if 'deal-workbook-builder' not in xml:
    xml = insert_after(xml, 'skill-authoring-workflow', FL_DWB, 'deal-workbook-builder')
else:
    print('  SKIP: deal-workbook-builder already present')

# Update skill count
for old in ['37 skills', '36 skills', '35 skills', '34 skills', '33 skills',
            '32 skills', '31 skills', '30 skills', '29 skills', '28 skills', '27 skills']:
    if old in xml:
        xml = xml.replace(old, '37 skills', 1)
        print(f'  Updated count: {old!r} -> 37 skills')
        break

for old in ['April 2026', 'March 2026']:
    if old in xml:
        xml = xml.replace(old, 'May 2026', 1)
        print(f'  Updated date: {old!r} -> May 2026')
        break

with open(os.path.join(FL_TMP, 'word', 'document.xml'), 'w', encoding='utf-8') as f:
    f.write(xml)
repack(FL_TMP, FL_DEST)
print(f'  Saved: {FL_DEST}')

# verify
with zipfile.ZipFile(FL_DEST) as z:
    xml2 = z.read('word/document.xml').decode('utf-8')
for skill in ['managing-up', 'written-communication', 'giving-presentations',
              'executive-briefing', 'vibe-coding', 'skill-authoring-workflow',
              'deal-workbook-builder', '37 skills', 'May 2026']:
    status = 'OK' if skill in xml2 else 'MISSING'
    print(f'  {status}: {skill}')

print('\nDone.')
