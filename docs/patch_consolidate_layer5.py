"""
patch_consolidate_layer5.py

Replaces the 6 individual earnings-reviewer skill rows in the inventory table
with a single consolidated "earnings-reviewer plugin" row listing all 6 skills.
Also removes the now-redundant architecture table individual entry
(keeps the single "5 — Equity Research" arch row already there).

Input:  Claude_Skill_Library_External (Finance)_v2.docx
Output: Claude_Skill_Library_External (Finance)_v2.docx  (overwrite)
"""

import zipfile, shutil, os, re

SRC = '/sessions/modest-keen-davinci/mnt/docs/Claude_Skill_Library_External (Finance)_v2.docx'
TMP = '/tmp/patch_consolidate_tmp'

def unpack(src, tmp):
    if os.path.exists(tmp): shutil.rmtree(tmp)
    with zipfile.ZipFile(src, 'r') as z:
        z.extractall(tmp)

def repack(tmp, dest):
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as zout:
        for root, dirs, files in os.walk(tmp):
            for file in files:
                fpath = os.path.join(root, file)
                zout.write(fpath, os.path.relpath(fpath, tmp))
    shutil.rmtree(tmp)

BORDER = (
    '<w:tcBorders>'
    '<w:top w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:left w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:right w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '</w:tcBorders>'
)
FILL  = '<w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/>'
MAR   = '<w:tcMar><w:top w:w="80" w:type="dxa"/><w:left w:w="120" w:type="dxa"/><w:bottom w:w="80" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar>'
CELL_PROPS = BORDER + FILL + MAR

def simple_cell(width, text):
    """Single-paragraph cell — plain text."""
    return (
        f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{CELL_PROPS}</w:tcPr>'
        f'<w:p><w:r><w:rPr><w:sz w:val="15"/><w:szCs w:val="15"/></w:rPr>'
        f'<w:t xml:space="preserve">{text}</w:t></w:r></w:p></w:tc>'
    )

def multi_para_cell(width, paras):
    """
    Multi-paragraph cell. Each entry in paras is either:
      - str  → plain body line
      - ('bold', str) → SemiBold skill name line
    """
    parts = [f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{CELL_PROPS}</w:tcPr>']
    for p in paras:
        if isinstance(p, tuple) and p[0] == 'bold':
            text = p[1]
            parts.append(
                f'<w:p><w:r><w:rPr>'
                f'<w:rFonts w:ascii="Wix Madefor Display SemiBold" w:hAnsi="Wix Madefor Display SemiBold"/>'
                f'<w:color w:val="0F4761"/><w:sz w:val="15"/><w:szCs w:val="15"/>'
                f'</w:rPr><w:t xml:space="preserve">{text}</w:t></w:r></w:p>'
            )
        else:
            parts.append(
                f'<w:p><w:r><w:rPr><w:sz w:val="15"/><w:szCs w:val="15"/></w:rPr>'
                f'<w:t xml:space="preserve">{p}</w:t></w:r></w:p>'
            )
    parts.append('</w:tc>')
    return ''.join(parts)

# ── The single consolidated row ───────────────────────────────────────────────

CONSOLIDATED_ROW = (
    '<w:tr w:rsidR="001556A8" w14:paraId="E0F1A2B3" w14:textId="77777777">'
    + simple_cell(1200, '5 — Equity Research')
    + multi_para_cell(2400, [
        ('bold', 'earnings-reviewer'),
        'plugin · 6 skills',
    ])
    + multi_para_cell(4200, [
        ('bold', 'earnings-analysis'),
        '8–12 page institutional earnings update report with beat/miss analysis, segment breakdown, updated estimates, 8–12 charts, and clickable citations. Delivered within 24–48 hrs of print.',
        ('bold', 'earnings-preview'),
        'Pre-earnings analysis: estimate model, bull/bear/base scenarios, and key metrics to watch. Use before a company reports to set positioning.',
        ('bold', 'model-update'),
        'Plugs quarterly actuals and new guidance into an uploaded XLSX model. Adjusts forward estimates, recalculates valuation, flags material changes.',
        ('bold', 'morning-note'),
        'Drafts concise 7am morning call notes: overnight developments, trade ideas, key events. Opinionated and actionable, 200–400 words.',
        ('bold', 'audit-xls'),
        'Audits spreadsheet formulas for errors, logic gaps, and model integrity: balance sheet balance, cash tie-out, sanity checks.',
        ('bold', 'xlsx-author'),
        'Headless XLSX authoring for sessions with no open Office app. Supports formulas, formatting, named ranges.',
    ])
    + simple_cell(3000, 'pattern-docx, writing-style, doc-quality-checker; Python (matplotlib, pandas); source Excel upload (model-update, audit-xls)')
    + '</w:tr>'
)

# ── patch ─────────────────────────────────────────────────────────────────────

print('=== Consolidating Layer 5 rows ===')
unpack(SRC, TMP)

with open(os.path.join(TMP, 'word', 'document.xml'), encoding='utf-8') as f:
    xml = f.read()

# Find the span of the 6 individual ER rows (first ER skill → end of last ER row)
idx_first = xml.find('earnings-reviewer:earnings-analysis')
idx_last  = xml.rfind('earnings-reviewer:xlsx-author')

if idx_first == -1:
    print('  ERROR: earnings-reviewer:earnings-analysis not found')
    exit(1)
if idx_last == -1:
    print('  ERROR: earnings-reviewer:xlsx-author not found')
    exit(1)

# Walk back to find start of the row containing the first ER skill
row_start = xml.rfind('<w:tr ', 0, idx_first)
# Walk forward to find end of row containing xlsx-author
row_end = xml.find('</w:tr>', idx_last) + len('</w:tr>')

removed_block = xml[row_start:row_end]
er_skills_in_block = removed_block.count('5 -- Equity Research')
print(f'  Found {er_skills_in_block} ER skill rows to consolidate (span {row_end - row_start} chars)')

xml = xml[:row_start] + CONSOLIDATED_ROW + xml[row_end:]
print('  Replaced with single consolidated row')

with open(os.path.join(TMP, 'word', 'document.xml'), 'w', encoding='utf-8') as f:
    f.write(xml)

repack(TMP, SRC)
print(f'  Saved -> {SRC}  ({os.path.getsize(SRC):,} bytes)')

# ── verify ────────────────────────────────────────────────────────────────────
print('\n=== Verification ===')
with zipfile.ZipFile(SRC) as z:
    xml2 = z.read('word/document.xml').decode()

checks = {
    'earnings-reviewer:earnings-analysis removed': 'earnings-reviewer:earnings-analysis' not in xml2,
    'earnings-reviewer:xlsx-author removed':       'earnings-reviewer:xlsx-author' not in xml2,
    'consolidated row present':                    'earnings-reviewer' in xml2 and 'plugin · 6 skills' in xml2,
    'earnings-analysis description present':       'beat/miss analysis' in xml2,
    'audit-xls description present':              'balance sheet balance' in xml2,
    '33 skills retained':                          '33 skills' in xml2,
    'five layers retained':                        'five layers' in xml2,
}

all_ok = True
for label, result in checks.items():
    status = 'OK' if result else 'FAIL'
    if not result: all_ok = False
    print(f'  {status}: {label}')

print(f'\n  ALL PASS: {all_ok}')
