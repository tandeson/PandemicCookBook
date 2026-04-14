#!/usr/bin/env python3
"""
Check whether Bulgarian translation JSON files are up to date with their
corresponding recipe .py files, using the stored SHA256 hash.

Run from the RecipeBook root directory:
    python scripts/helper_check_bulgarian_hashes.py

Exit code 0 = all up to date
Exit code 1 = one or more stale or missing files found
"""

import glob
import hashlib
import json
import os
import sys
from pathlib import Path


def compute_hash(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    base = Path('recipes_for_book_input')
    if not base.exists():
        print("ERROR: Run this script from the RecipeBook root directory.")
        return 1

    stale = []
    missing_hash = []
    missing_bg = []

    for recipe_dir in sorted(base.iterdir()):
        if not recipe_dir.is_dir():
            continue

        py_files = sorted(recipe_dir.glob('recipe_*.py'))
        bg_files = sorted(recipe_dir.glob('bulgarian_*.json'))

        if not py_files:
            continue

        if not bg_files:
            missing_bg.append(recipe_dir.name)
            continue

        py_file = py_files[0]
        bg_file = bg_files[0]

        current_hash = compute_hash(py_file)

        with open(bg_file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"  ERROR: Could not parse {bg_file}: {e}")
                continue

        stored_hash = data.get('recipe_file_hash')

        if stored_hash is None:
            missing_hash.append(recipe_dir.name)
        elif stored_hash != current_hash:
            stale.append(recipe_dir.name)

    # Report
    ok = True

    if stale:
        ok = False
        print(f"STALE ({len(stale)}) — recipe .py changed since Bulgarian file was built:")
        for name in stale:
            print(f"  {name}")

    if missing_hash:
        ok = False
        print(f"MISSING HASH ({len(missing_hash)}) — Bulgarian file has no recipe_file_hash field:")
        for name in missing_hash:
            print(f"  {name}")

    if missing_bg:
        ok = False
        print(f"MISSING BULGARIAN ({len(missing_bg)}) — no Bulgarian JSON file found:")
        for name in missing_bg:
            print(f"  {name}")

    if ok:
        total = len(list(base.iterdir()))
        print(f"All Bulgarian files are up to date ({total} recipes checked).")

    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
