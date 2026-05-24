#!/usr/bin/env python3
"""Lightweight BibTeX sanity check for PaperCraft (Module 5 helper)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_FIELDS = {
    "article": {"author", "title", "journal", "year"},
    "inproceedings": {"author", "title", "booktitle", "year"},
    "book": {"author", "title", "publisher", "year"},
    "misc": {"title"},
}

ENTRY_START = re.compile(r"@(\w+)\s*[\{(]", re.IGNORECASE)
FIELD = re.compile(r"(\w+)\s*=\s*[\{\"](.+?)[\}\"]\s*,?", re.DOTALL | re.IGNORECASE)


def parse_entries(text: str) -> list[tuple[str, str, dict[str, str]]]:
    entries: list[tuple[str, str, dict[str, str]]] = []
    pos = 0
    while m := ENTRY_START.search(text, pos):
        etype = m.group(1).lower()
        open_char = text[m.end() - 1]
        close_char = "}" if open_char == "{" else ")"
        depth = 1
        i = m.end()
        while i < len(text) and depth:
            if text[i] == open_char:
                depth += 1
            elif text[i] == close_char:
                depth -= 1
            i += 1
        block = text[m.start() : i]
        key_m = re.search(r"[\{(]\s*([^,\s]+)\s*,", block)
        key = key_m.group(1) if key_m else "?"
        fields: dict[str, str] = {}
        for fm in FIELD.finditer(block):
            fields[fm.group(1).lower()] = fm.group(2).strip()
        entries.append((etype, key, fields))
        pos = i
    return entries


def validate(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    entries = parse_entries(text)
    if not entries:
        print(f"ERROR: no @entries found in {path}")
        return 1

    errors = 0
    keys_seen: set[str] = set()
    for etype, key, fields in entries:
        if key in keys_seen:
            print(f"ERROR: duplicate key '{key}'")
            errors += 1
        keys_seen.add(key)

        req = REQUIRED_FIELDS.get(etype, {"title"})
        missing = req - set(fields)
        if missing:
            print(f"ERROR: @{etype}{{{key}}} missing fields: {', '.join(sorted(missing))}")
            errors += 1

        if "year" in fields and not re.fullmatch(r"\d{4}", fields["year"][:4]):
            print(f"WARN: @{etype}{{{key}}} suspicious year: {fields['year']!r}")

        if "doi" in fields and not fields["doi"].startswith("10."):
            print(f"WARN: @{etype}{{{key}}} doi may be invalid: {fields['doi']!r}")

    if errors:
        print(f"\n{errors} error(s) in {path}")
        return 1
    print(f"OK: {len(entries)} entries in {path}")
    return 0


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_bibtex.py <file.bib> [file2.bib ...]")
        sys.exit(2)
    code = 0
    for arg in sys.argv[1:]:
        p = Path(arg)
        if not p.is_file():
            print(f"ERROR: not found: {p}")
            code = 1
            continue
        code = max(code, validate(p))
    sys.exit(code)


if __name__ == "__main__":
    main()
