"""Pull a Google Sheet into a local .xlsx for use with build_deliverable.py.

Usage:
    py pull_from_sheets.py --url <sheets-url> --out <local.xlsx>
    py pull_from_sheets.py --sheet-id <id> --out <local.xlsx>

Auth: requires GOOGLE_SHEETS_TOKEN env var (OAuth access token), OR falls back to
gcloud application-default credentials (`gcloud auth application-default login`).

The Pattern Competitive Landscape sheet ID is 159cKsL9YEWmIoo0BTt6NelobAmAm6qan-VyOagUJuJ4.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

try:
    from openpyxl import Workbook
except ImportError:
    print("openpyxl required: pip install openpyxl", file=sys.stderr)
    sys.exit(1)


def extract_sheet_id(url: str) -> str:
    m = re.search(r"/spreadsheets/d/([A-Za-z0-9_-]+)", url)
    if m:
        return m.group(1)
    return url  # assume it's already an ID


def get_token() -> str:
    tok = os.environ.get("GOOGLE_SHEETS_TOKEN")
    if tok:
        return tok
    try:
        out = subprocess.check_output(["gcloud", "auth", "application-default", "print-access-token"], text=True).strip()
        if out:
            return out
    except Exception:
        pass
    print("ERROR: set GOOGLE_SHEETS_TOKEN env var or run: gcloud auth application-default login", file=sys.stderr)
    sys.exit(2)


def api_get(url: str, token: str) -> dict:
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def pull(sheet_id: str, out_path: Path, tab_name: str = "Competitive Landscape") -> Path:
    token = get_token()
    base = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}"

    # Get metadata
    meta = api_get(base, token)
    tabs = [s["properties"]["title"] for s in meta.get("sheets", [])]
    print(f"sheet has tabs: {tabs}")

    target_tab = tab_name if tab_name in tabs else tabs[0]
    print(f"pulling tab: {target_tab}")

    # Fetch full values
    quoted = urllib.request.quote(target_tab)
    values = api_get(f"{base}/values/{quoted}?valueRenderOption=FORMATTED_VALUE", token)
    rows = values.get("values", [])
    print(f"rows fetched: {len(rows)}")

    # Build local workbook
    wb = Workbook()
    ws = wb.active
    ws.title = target_tab
    for ri, row in enumerate(rows, start=1):
        for ci, val in enumerate(row, start=1):
            ws.cell(row=ri, column=ci, value=val)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out_path)
    print(f"saved: {out_path}")
    return out_path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--url", default=None)
    p.add_argument("--sheet-id", default=None)
    p.add_argument("--tab", default="Competitive Landscape")
    p.add_argument("--out", required=True)
    args = p.parse_args()

    if not args.url and not args.sheet_id:
        print("provide --url or --sheet-id", file=sys.stderr)
        sys.exit(2)

    sid = args.sheet_id or extract_sheet_id(args.url)
    out = Path(args.out).expanduser().resolve()
    pull(sid, out, args.tab)


if __name__ == "__main__":
    main()
