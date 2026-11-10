#!/usr/bin/env python3
"""StudyCards - turn simple study notes into an Anki-ready flashcard CSV.

Notes format: one study item per line as "term :: definition".
Python standard library only.
"""

import argparse
import csv
import sys


def parse_notes(path):
    cards = []
    skipped = 0
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if " :: " not in line:
                skipped += 1
                continue
            front, back = line.split(" :: ", 1)
            cards.append((front.strip(), back.strip()))
    return cards, skipped


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Turn study notes (term :: definition) into a flashcard CSV."
    )
    parser.add_argument("--file", required=True, help="Path to the notes text file.")
    parser.add_argument(
        "--out", default="flashcards.csv", help="Output CSV path (default: flashcards.csv)."
    )
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Also add a reversed card for each line (definition as front).",
    )
    args = parser.parse_args(argv)

    try:
        cards, skipped = parse_notes(args.file)
    except OSError as exc:
        print(f"error: could not read notes file: {exc}", file=sys.stderr)
        return 2

    rows = []
    for front, back in cards:
        rows.append((front, back))
        if args.reverse:
            rows.append((back, front))

    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerows(rows)

    print(f"Wrote {len(rows)} cards to {args.out}")
    if skipped:
        print(f"Skipped {skipped} lines without the :: separator.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
