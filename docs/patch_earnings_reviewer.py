"""
patch_earnings_reviewer.py

Adds 6 new earnings-reviewer plugin skills to Claude_Skill_Library_External (Finance).docx:
  - earnings-reviewer:earnings-analysis   (5 -- Equity Research)
  - earnings-reviewer:earnings-preview    (5 -- Equity Research)
  - earnings-reviewer:model-update        (5 -- Equity Research)
  - earnings-reviewer:morning-note        (5 -- Equity Research)
  - earnings-reviewer:audit-xls           (5 -- Equity Research)
  - earnings-reviewer:xlsx-author         (5 -- Equity Research)

Also:
  - Adds "5 — Equity Research" row to the Layer Architecture table
  - Updates skill count from "27 skills" to "33 skills"
  - Updates "four layers" to "five layers"
  - Updates subtitle to "May 2026"
"""

import zipfile, shutil, os

SRC  = '/sessions/modest-keen-davinci/mnt/docs/Claude_Skill_Library_External (Finance).docx'
DEST = '/sessions/modest-keen-davinci/mnt/docs/Claude_Skill_Library_External (Finance).docx'
TMP  = '/tmp/patch_er_tmp'

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
    """Insert new_row after the </w:tr> that contains anchor_skill."""
    anchor = f'{anchor_skill}</w:t>'
    idx = xml.find(anchor)
    if idx == -1:
        print(f'  ERROR: anchor not found — {anchor_skill}')
        return xml
    end_idx = xml.find('</w:tr>', idx) + len('</w:tr>')
    xml = xml[:end_idx] + new_row + xml[end_idx:]
    print(f'  Inserted: {label} after {anchor_skill}')
    return xml

# ── row builder — Finance Library style ──────────────────────────────────────
# Matches the existing table: 4 columns with widths 1200, 2400, 4200, 3000

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
        f'<w:t xml:space="preserve">{text}</w:t></w:r></w:p></w:tc>'
    )

def er_row(para_id, skill_name, description, depends):
    return (
        f'<w:tr w:rsidR="001556A8" w14:paraId="{para_id}" w14:textId="77777777">'
        + fl_cell(1200, '5 -- Equity Research')
        + fl_cell(2400, skill_name)
        + fl_cell(4200, description)
        + fl_cell(3000, depends)
        + '</w:tr>'
    )

# ── 6 new skill rows ──────────────────────────────────────────────────────────

ROW_ANALYSIS = er_row(
    'E1F2A3B4',
    'earnings-reviewer:earnings-analysis',
    'Creates institutional-quality 8–12 page earnings update reports (3,000–5,000 words) '
    'within 24–48 hours of a print. Beat/miss analysis, segment breakdown, margin '
    'commentary, updated estimates, and revised thesis. 8–12 embedded charts. '
    'Full citations with clickable hyperlinks to SEC filings and earnings materials.',
    'pattern-docx, writing-style, doc-quality-checker; Python (matplotlib, pandas)'
)

ROW_PREVIEW = er_row(
    'E2F3A4B5',
    'earnings-reviewer:earnings-preview',
    'Builds pre-earnings analysis with estimate models, scenario frameworks, and key '
    'metrics to watch. Sets up bull/bear/base scenarios and identifies what will move '
    'the stock. Use before a company reports to prepare positioning notes.',
    'mckinsey-consultant, writing-style'
)

ROW_MODEL = er_row(
    'E3F4A5B6',
    'earnings-reviewer:model-update',
    'Updates financial models with new quarterly actuals, management guidance, or '
    'revised assumptions. Adjusts forward estimates, recalculates valuation, and '
    'flags material changes vs. prior estimates. Works on uploaded XLSX models.',
    'earnings-reviewer:xlsx-author, financial-model-builder'
)

ROW_MORNING = er_row(
    'E4F5A6B7',
    'earnings-reviewer:morning-note',
    'Drafts concise morning meeting notes summarizing overnight developments, trade '
    'ideas, and key events for coverage stocks. Tight 7am format — opinionated, '
    'actionable, 200–400 words. Structured for verbal delivery at morning call.',
    'writing-style'
)

ROW_AUDIT = er_row(
    'E5F6A7B8',
    'earnings-reviewer:audit-xls',
    'Audits a spreadsheet for formula accuracy, errors, and common mistakes. Scopes '
    'to a selected range, a single sheet, or the entire model — including financial '
    'model integrity checks: balance sheet balance, cash tie-out, and logic sanity.',
    'earnings-reviewer:xlsx-author'
)

ROW_XLSX = er_row(
    'E6F7A8B9',
    'earnings-reviewer:xlsx-author',
    'Produces a .xlsx file on disk (headless) instead of driving a live Excel '
    'workbook. Use in managed-agent sessions with no open Office application. '
    'Supports formula authoring, formatting, named ranges, and chart stubs.',
    'None — leaf skill'
)

# ── Layer Architecture table row for Layer 5 ─────────────────────────────────
# Matches the architecture table format (4 cols, same widths 1200/2400/4200/3000)
# Inserted after the "4b — QA" row

ARCH_CELL = (
    '<w:tcBorders>'
    '<w:top w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:left w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '<w:right w:val="single" w:sz="4" w:space="0" w:color="DDDDDD"/>'
    '</w:tcBorders><w:shd w:val="clear" w:color="auto" w:fill="FFFFFF"/>'
    '<w:tcMar><w:top w:w="80" w:type="dxa"/><w:left w:w="120" w:type="dxa"/>'
    '<w:bottom w:w="80" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar>'
)

def arch_cell(width, text):
    return (
        f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{ARCH_CELL}</w:tcPr>'
        f'<w:p><w:r><w:rPr><w:sz w:val="15"/><w:szCs w:val="15"/></w:rPr>'
        f'<w:t xml:space="preserve">{text}</w:t></w:r></w:p></w:tc>'
    )

ARCH_LAYER5 = (
    '<w:tr w:rsidR="001556A8" w14:paraId="F1A2B3C4" w14:textId="77777777">'
    + arch_cell(1200, '5 — Equity Research')
    + arch_cell(2400, 'earnings-reviewer (6 skills)')
    + arch_cell(4200,
        'Earnings update reports, pre-earnings previews, model updates, '
        'morning notes, spreadsheet auditing, and headless XLSX authoring '
        'for public equity coverage')
    + arch_cell(3000, 'After research and quality layers; triggered by earnings events')
    + '</w:tr>'
)

# ── main patch ────────────────────────────────────────────────────────────────

print('=== Patching Finance Library ===')
unpack(SRC, TMP)

with open(os.path.join(TMP, 'word', 'document.xml'), encoding='utf-8') as f:
    xml = f.read()

# 1. Add Layer Architecture row after "4b — QA" / "doc-quality-checker" arch row
if 'earnings-reviewer' not in xml:
    if '4b — QA' in xml:
        # Find the architecture table row for 4b — QA and insert after it
        idx = xml.find('4b — QA')
        if idx != -1:
            end_idx = xml.find('</w:tr>', idx) + len('</w:tr>')
            xml = xml[:end_idx] + ARCH_LAYER5 + xml[end_idx:]
            print('  Inserted: Layer 5 architecture row after 4b — QA')
    else:
        print('  WARN: 4b — QA anchor not found in architecture table')

# 2. Add skill inventory rows for the 6 earnings-reviewer skills
# Insert all 6 after "doc-quality-checker" in the inventory table (last skill = doc-quality-checker)
if 'earnings-reviewer:earnings-analysis' not in xml:
    xml = insert_after(xml, 'doc-quality-checker', ROW_ANALYSIS, 'earnings-reviewer:earnings-analysis')
else:
    print('  SKIP: earnings-reviewer:earnings-analysis already present')

if 'earnings-reviewer:earnings-preview' not in xml:
    xml = insert_after(xml, 'earnings-reviewer:earnings-analysis', ROW_PREVIEW, 'earnings-reviewer:earnings-preview')
else:
    print('  SKIP: earnings-reviewer:earnings-preview already present')

if 'earnings-reviewer:model-update' not in xml:
    xml = insert_after(xml, 'earnings-reviewer:earnings-preview', ROW_MODEL, 'earnings-reviewer:model-update')
else:
    print('  SKIP: earnings-reviewer:model-update already present')

if 'earnings-reviewer:morning-note' not in xml:
    xml = insert_after(xml, 'earnings-reviewer:model-update', ROW_MORNING, 'earnings-reviewer:morning-note')
else:
    print('  SKIP: earnings-reviewer:morning-note already present')

if 'earnings-reviewer:audit-xls' not in xml:
    xml = insert_after(xml, 'earnings-reviewer:morning-note', ROW_AUDIT, 'earnings-reviewer:audit-xls')
else:
    print('  SKIP: earnings-reviewer:audit-xls already present')

if 'earnings-reviewer:xlsx-author' not in xml:
    xml = insert_after(xml, 'earnings-reviewer:audit-xls', ROW_XLSX, 'earnings-reviewer:xlsx-author')
else:
    print('  SKIP: earnings-reviewer:xlsx-author already present')

# 3. Update skill count
for old_count in ['27 skills', '26 skills', '25 skills']:
    if old_count in xml:
        xml = xml.replace(old_count, '33 skills', 1)
        print(f'  Updated count: {old_count} -> 33 skills')
        break

# 4. Update "four layers" -> "five layers"
if 'four layers' in xml:
    xml = xml.replace('four layers', 'five layers', 1)
    print('  Updated: four layers -> five layers')

# 5. Update date in subtitle
for old_date in ['April 2026', 'March 2026', 'February 2026', 'January 2026']:
    if old_date in xml:
        xml = xml.replace(old_date, 'May 2026', 1)
        print(f'  Updated date: {old_date} -> May 2026')
        break

with open(os.path.join(TMP, 'word', 'document.xml'), 'w', encoding='utf-8') as f:
    f.write(xml)

# Write to a new file (avoid mount overwrite restriction)
OUT = '/sessions/modest-keen-davinci/mnt/docs/Claude_Skill_Library_External (Finance)_v2.docx'
repack(TMP, OUT)
print(f'\n  Saved -> {OUT}')
print(f'  Size: {os.path.getsize(OUT):,} bytes')

# ── verify ────────────────────────────────────────────────────────────────────
print('\n=== Verification ===')
with zipfile.ZipFile(OUT, 'r') as z:
    xml_check = z.read('word/document.xml').decode('utf-8')

checks = [
    'earnings-reviewer:earnings-analysis',
    'earnings-reviewer:earnings-preview',
    'earnings-reviewer:model-update',
    'earnings-reviewer:morning-note',
    'earnings-reviewer:audit-xls',
    'earnings-reviewer:xlsx-author',
    '33 skills',
    'five layers',
    '5 -- Equity Research',
    'May 2026',
]
all_ok = True
for c in checks:
    status = 'OK' if c in xml_check else 'MISSING'
    if status == 'MISSING':
        all_ok = False
    print(f'  {status}: {c}')

print(f'\n  ALL PASS: {all_ok}')
