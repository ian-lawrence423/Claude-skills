"""Patch Claude_Skills_CheatSheet.docx:
- Remove saas-revenue-growth-metrics row
- Add gtm-metrics-analyzer row after kpi-tree-builder
- Update subtitle count from "24 skills" to "21 skills"
"""
import zipfile, shutil, os, re

SRC  = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skills_CheatSheet.docx'
DEST = r'C:/Users/IanLawrence/github/Claude-skills/docs/Claude_Skills_CheatSheet.docx'
TMP  = r'C:/Users/IanLawrence/github/Claude-skills/docs/_tmp_cheatsheet'

# ── new row XML ───────────────────────────────────────────────────────────────
GTM_ROW = (
    '<w:tr w:rsidR="00EE7BB4" w14:paraId="B1C2D3E4" w14:textId="77777777">'
    '<w:tc><w:tcPr><w:tcW w:w="650" w:type="dxa"/>'
    '<w:shd w:val="clear" w:color="auto" w:fill="E6EFFD"/>'
    '<w:tcMar><w:top w:w="30" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
    '<w:bottom w:w="30" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
    '</w:tcPr>'
    '<w:p w14:paraId="B2C3D4E5" w14:textId="77777777" w:rsidR="00EE7BB4" w:rsidRDefault="008712F0">'
    '<w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr>'
    '<w:r><w:rPr><w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold"/>'
    '<w:b/><w:color w:val="4280F4"/><w:sz w:val="16"/></w:rPr><w:t>L2</w:t></w:r>'
    '</w:p></w:tc>'
    '<w:tc><w:tcPr><w:tcW w:w="1700" w:type="dxa"/>'
    '<w:tcMar><w:top w:w="30" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
    '<w:bottom w:w="30" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
    '</w:tcPr>'
    '<w:p w14:paraId="B3C4D5E6" w14:textId="77777777" w:rsidR="00EE7BB4" w:rsidRDefault="008712F0">'
    '<w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>'
    '<w:r><w:rPr><w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold"/>'
    '<w:b/><w:color w:val="0F4761"/><w:sz w:val="17"/></w:rPr>'
    '<w:t>gtm-metrics-analyzer</w:t></w:r>'
    '</w:p></w:tc>'
    '<w:tc><w:tcPr><w:tcW w:w="6500" w:type="dxa"/>'
    '<w:tcMar><w:top w:w="30" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
    '<w:bottom w:w="30" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
    '</w:tcPr>'
    '<w:p w14:paraId="B4C5D6E7" w14:textId="77777777" w:rsidR="00EE7BB4" w:rsidRDefault="008712F0">'
    '<w:pPr><w:spacing w:after="0" w:line="252" w:lineRule="auto"/></w:pPr>'
    '<w:r><w:rPr><w:rFonts w:ascii="Wix Madefor Display" w:hAnsi="Wix Madefor Display"/>'
    '<w:color w:val="000000"/><w:sz w:val="16"/></w:rPr>'
    '<w:t>Builds a 4-tab GTM diagnostic workbook from uploaded source files. '
    'Calculates 48 metrics across 6 families: ARR funnel, pipeline, retention, efficiency &amp; economics, '
    'team &amp; productivity, fiscal maturity. Separates provided inputs from derived outputs. '
    'Requires Excel 365/2019+ (XLOOKUP).</w:t></w:r>'
    '</w:p></w:tc>'
    '<w:tc><w:tcPr><w:tcW w:w="5850" w:type="dxa"/>'
    '<w:tcMar><w:top w:w="30" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
    '<w:bottom w:w="30" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
    '</w:tcPr>'
    '<w:p w14:paraId="B5C6D7E8" w14:textId="77777777" w:rsidR="00EE7BB4" w:rsidRDefault="008712F0">'
    '<w:pPr><w:spacing w:after="0" w:line="252" w:lineRule="auto"/></w:pPr>'
    '<w:r><w:rPr><w:rFonts w:ascii="Wix Madefor Display" w:hAnsi="Wix Madefor Display"/>'
    '<w:i/><w:color w:val="000000"/><w:sz w:val="16"/></w:rPr>'
    '<w:t>.xlsx workbook: Input_Fields + Metric_Calcs + Diagnostic_Output + README tabs</w:t></w:r>'
    '</w:p></w:tc>'
    '</w:tr>'
)

# ── unpack ────────────────────────────────────────────────────────────────────
if os.path.exists(TMP):
    shutil.rmtree(TMP)
with zipfile.ZipFile(SRC, 'r') as z:
    z.extractall(TMP)

with open(os.path.join(TMP, 'word', 'document.xml'), encoding='utf-8') as f:
    xml = f.read()

# ── 1. remove saas-revenue-growth-metrics row ─────────────────────────────────
parts = xml.split('</w:tr>')
new_parts = []
removed = 0
for part in parts:
    if 'saas-revenue-growth-metrics' in part:
        removed += 1
        print(f'Removed: saas-revenue-growth-metrics row')
    else:
        new_parts.append(part)
xml = '</w:tr>'.join(new_parts)
print(f'Total rows removed: {removed}')

# ── 2. add gtm-metrics-analyzer row after kpi-tree-builder ───────────────────
if 'gtm-metrics-analyzer' in xml:
    print('gtm-metrics-analyzer already present — skipping insert')
else:
    xml = xml.replace('kpi-tree-builder</w:t>', 'kpi-tree-builder</w:t>', 1)
    # Find end of kpi-tree-builder row and insert after
    idx = xml.find('kpi-tree-builder</w:t>')
    if idx == -1:
        print('ERROR: could not find kpi-tree-builder row')
    else:
        end_idx = xml.find('</w:tr>', idx) + len('</w:tr>')
        xml = xml[:end_idx] + GTM_ROW + xml[end_idx:]
        print('Inserted gtm-metrics-analyzer row after kpi-tree-builder')

# ── 3. update subtitle count ──────────────────────────────────────────────────
old_count = '24 skills'
new_count = '21 skills'
if old_count in xml:
    xml = xml.replace(old_count, new_count, 1)
    print(f'Updated subtitle: {old_count!r} -> {new_count!r}')
else:
    print(f'WARNING: could not find {old_count!r} in subtitle')

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
