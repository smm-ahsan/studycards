# StudyCards

Turn simple study notes into an Anki-ready flashcard CSV.

## Notes format

Write one study item per line, with the term and its definition separated by ` :: ` (a space, two colons, a space). Blank lines and lines starting with `#` are ignored. Lines without the separator are skipped, and the tool tells you how many were skipped.

Sample notes file:

```
# Biology basics
Photosynthesis :: The process plants use to turn sunlight into energy
Mitochondria :: The part of the cell that produces most of its energy
```

## Usage

```bash
python3 studycards.py --file notes.txt --out cards.csv
```

Add `--reverse` to also create a reversed card for every line, with the definition as the front:

```bash
python3 studycards.py --file notes.txt --out cards.csv --reverse
```

## Importing into Anki

1. Open Anki and choose **File > Import**.
2. Select the CSV file StudyCards produced.
3. Make sure the import maps the two CSV fields to the Front and Back fields of your note type (the CSV has no header, just two columns: front, back).
4. Click Import. Your cards are ready to study.

## Requirements

Python 3. Standard library only, nothing to install.

## License

MIT License - see the LICENSE file. Copyright (c) 2026 Muhammad Ahsan Anwar.
