import sys
sys.stdout.reconfigure(encoding="utf-8")
from openpyxl import load_workbook

PATH = r"C:\Users\IanLawrence\github\Claude-skills\docs\Archive\Shopify_Deal_Workbook_v6.xlsx"
wb = load_workbook(PATH)
ws = wb["KPI TREE"]

# QC script over-widened K (to 14) and L (to 36) using old specs.
# Correct widths per new layout:
#   K = Variance % → 11
#   L = Status → 15
#   M = Notes (wrap) → 42  (already set correctly by fix script)
ws.column_dimensions["K"].width = 11
ws.column_dimensions["L"].width = 15

wb.save(PATH)
print("Column widths corrected in KPI TREE.")
