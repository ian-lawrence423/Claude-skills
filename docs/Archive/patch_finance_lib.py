"""Patch Claude_Skill_Library_External (Finance).docx:
- Remove saas-revenue-growth-metrics row
- Remove saas-economics-efficiency-metrics row
- Add gtm-metrics-analyzer row after kpi-tree-builder
- Update Layer 2 summary row to remove the deleted skills
- Update count from "26 skills" to "25 skills"
"""
import zipfile, shutil, os, re

SRC  = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skill_Library_External (Finance).docx'
DEST = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skill_Library_External (Finance).docx'
TMP  = r'C:/Users/IanLawrence/github/Claude-skills/docs/_tmp_finance'

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

def make_cell(width, text):
    return (
        f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{CELL}</w:tcPr>'
        f'<w:p><w:r><w:rPr><w:sz w:val="15"/><w:szCs w:val="15"/></w:rPr>'
        f'<w:t>{text}</w:t></w:r></w:p></w:tc>'
    )

GTM_ROW = (
    '<w:tr w:rsidR="001556A8" w14:paraId="C1D2E3F4" w14:textId="77777777">'
    + make_cell(1200, '2 -- Research')
    + make_cell(2400, 'gtm-metrics-analyzer')
    + make_cell(4200,
        'Builds a 4-tab GTM diagnostic workbook from uploaded source files. '
        'Calculates 48 metrics across 6 families: ARR funnel, pipeline, retention, '
        'efficiency &amp; economics, team &amp; productivity, fiscal maturity. '
        'Separates provided inputs from derived outputs. Requires Excel 365/2019+.')
    + make_cell(3000, 'financial-model-builder, driver-tree, ntb-diligence, kpi-tree-builder')
    + '</w:tr>'
)

# ── unpack ────────────────────────────────────────────────────────────────────
if os.path.exists(TMP):
    shutil.rmtree(TMP)
with zipfile.ZipFile(SRC, 'r') as z:
    z.extractall(TMP)

with open(os.path.join(TMP, 'word', 'document.xml'), encoding='utf-8') as f:
    xml = f.read()

# ── 1. remove deleted skill rows ──────────────────────────────────────────────
to_remove = ['saas-revenue-growth-metrics', 'saas-economics-efficiency-metrics']
parts = xml.split('</w:tr>')
new_parts = []
removed = 0
for part in parts:
    if any(s in part for s in to_remove):
        for s in to_remove:
            if s in part:
                print(f'Removed row: {s}')
        removed += 1
    else:
        new_parts.append(part)
xml = '</w:tr>'.join(new_parts)
print(f'Total rows removed: {removed}')

# ── 2. add gtm-metrics-analyzer after kpi-tree-builder ───────────────────────
if 'gtm-metrics-analyzer' in xml:
    print('gtm-metrics-analyzer already present — skipping insert')
else:
    idx = xml.find('kpi-tree-builder</w:t>')
    if idx == -1:
        print('ERROR: could not find kpi-tree-builder row')
    else:
        end_idx = xml.find('</w:tr>', idx) + len('</w:tr>')
        xml = xml[:end_idx] + GTM_ROW + xml[end_idx:]
        print('Inserted gtm-metrics-analyzer row after kpi-tree-builder')

# ── 3. update Layer 2 summary row ─────────────────────────────────────────────
# The summary row lists Layer 2 skills in a cell — remove the deleted ones
for skill in ['saas-revenue-growth-metrics', 'saas-economics-efficiency-metrics']:
    # Remove "skillname, " or ", skillname" patterns
    for pattern in [skill + ', ', ', ' + skill, skill]:
        if pattern in xml:
            xml = xml.replace(pattern, '', 1)
            print(f'Removed from summary cell: {pattern!r}')
            break

# ── 4. update count ───────────────────────────────────────────────────────────
old = '26 skills'
new = '25 skills'
if old in xml:
    xml = xml.replace(old, new, 1)
    print(f'Updated count: {old!r} -> {new!r}')
else:
    print(f'WARNING: could not find {old!r}')

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
print(f'Saved: {DEST}')
