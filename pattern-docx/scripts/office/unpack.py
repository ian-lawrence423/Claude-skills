#!/usr/bin/env python3
"""Unpack a DOCX/PPTX/XLSX zip package into a directory."""

from __future__ import annotations

import argparse
import shutil
import sys
import zipfile
from pathlib import Path


def _safe_target(root: Path, member_name: str) -> Path:
    target = (root / member_name).resolve()
    if root.resolve() not in target.parents and target != root.resolve():
        raise ValueError(f"Unsafe archive member path: {member_name}")
    return target


def unpack_package(source: Path, destination: Path, force: bool = False) -> None:
    if not source.exists():
        raise FileNotFoundError(f"Source package not found: {source}")
    if not zipfile.is_zipfile(source):
        raise ValueError(f"Source is not a valid Office zip package: {source}")

    if destination.exists():
        if not force and any(destination.iterdir()):
            raise FileExistsError(
                f"Destination exists and is not empty: {destination}. Use --force to replace it."
            )
        if force:
            shutil.rmtree(destination)

    destination.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(source) as archive:
        for member in archive.infolist():
            target = _safe_target(destination, member.filename)
            if member.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(member) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Source .docx/.pptx/.xlsx file")
    parser.add_argument("destination", type=Path, help="Directory to unpack into")
    parser.add_argument("--force", action="store_true", help="Replace destination if it exists")
    args = parser.parse_args(argv)

    unpack_package(args.source, args.destination, args.force)
    print(f"Unpacked {args.source} -> {args.destination}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
