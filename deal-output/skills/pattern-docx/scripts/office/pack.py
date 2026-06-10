#!/usr/bin/env python3
"""Pack an unpacked Office document directory into a DOCX/PPTX/XLSX zip package."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path


REQUIRED_DOCX_PARTS = (
    "[Content_Types].xml",
    "_rels/.rels",
    "word/document.xml",
)


def _parse_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError("expected true or false")


def validate_package_dir(source_dir: Path) -> None:
    missing = [part for part in REQUIRED_DOCX_PARTS if not (source_dir / part).exists()]
    if missing:
        raise FileNotFoundError(
            "Missing required DOCX package parts: " + ", ".join(missing)
        )


def pack_package(source_dir: Path, output: Path, validate: bool = True) -> None:
    if not source_dir.exists() or not source_dir.is_dir():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    if validate:
        validate_package_dir(source_dir)

    output.parent.mkdir(parents=True, exist_ok=True)

    files = sorted(path for path in source_dir.rglob("*") if path.is_file())
    if not files:
        raise ValueError(f"Source directory contains no files: {source_dir}")

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(source_dir).as_posix())

    if not zipfile.is_zipfile(output):
        raise ValueError(f"Packed output is not a valid zip package: {output}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_dir", type=Path, help="Unpacked Office package directory")
    parser.add_argument("output", type=Path, help="Output .docx/.pptx/.xlsx file")
    parser.add_argument(
        "--validate",
        type=_parse_bool,
        default=True,
        help="Validate required DOCX package parts before packing. Default: true",
    )
    args = parser.parse_args(argv)

    pack_package(args.source_dir, args.output, args.validate)
    print(f"Packed {args.source_dir} -> {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
