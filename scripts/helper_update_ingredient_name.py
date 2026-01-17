#!/usr/bin/env python3
"""
Update an ingredient name everywhere it appears in recipe sources.
"""

import argparse
import os
import sys
from pathlib import Path

DEFAULT_PATHS = [
    Path('IngredientList.py'),
    Path('recipes_for_book_input'),
]

ALLOWED_EXTS = {'.py', '.json', '.md', '.txt', '.t'}


def iter_candidate_files(paths):
    for path in paths:
        path = Path(path)
        if path.is_dir():
            for root, _, files in os.walk(path):
                for filename in files:
                    file_path = Path(root) / filename
                    if file_path.suffix.lower() in ALLOWED_EXTS:
                        yield file_path
        elif path.is_file():
            if path.suffix.lower() in ALLOWED_EXTS:
                yield path
        else:
            sys.stderr.write("Warning: path not found: %s\n" % path)


def update_file(path, old, new, dry_run=False):
    try:
        content = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        sys.stderr.write("Warning: could not read %s as utf-8\n" % path)
        return 0
    except OSError as exc:
        sys.stderr.write("Warning: could not read %s: %s\n" % (path, exc))
        return 0

    if old not in content:
        return 0

    updated = content.replace(old, new)
    if updated == content:
        return 0

    if not dry_run:
        path.write_text(updated, encoding='utf-8')

    return content.count(old)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Update ingredient name strings across recipe sources."
    )
    parser.add_argument('--old', required=True, help='Exact ingredient name to replace.')
    parser.add_argument('--new', required=True, help='New ingredient name.')
    parser.add_argument(
        '--path',
        action='append',
        default=[],
        help='Additional file or directory to scan (repeatable).'
    )
    parser.add_argument('--dry-run', action='store_true', help='Report changes without writing.')
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    if args.old == args.new:
        sys.stderr.write("Old and new ingredient names are identical.\n")
        return 1

    paths = DEFAULT_PATHS + [Path(p) for p in args.path]
    total_hits = 0
    changed_files = []

    for file_path in sorted(set(iter_candidate_files(paths))):
        hits = update_file(file_path, args.old, args.new, dry_run=args.dry_run)
        if hits:
            total_hits += hits
            changed_files.append((file_path, hits))

    if not changed_files:
        print("No matches found for: %s" % args.old)
        return 0

    for file_path, hits in changed_files:
        print("%s: %s" % (file_path, hits))

    action = "Would update" if args.dry_run else "Updated"
    print("%s %s occurrence(s) across %s file(s)." % (
        action,
        total_hits,
        len(changed_files)
    ))
    return 0


if __name__ == '__main__':
    sys.exit(main())
