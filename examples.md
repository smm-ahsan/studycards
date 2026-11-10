# Examples

Real output from StudyCards, captured from actual runs.

## Sample notes file (`notes.txt`)

```
Photosynthesis :: The process plants use to turn sunlight into energy
Mitochondria :: The part of the cell that produces most of its energy
One bad line without separator
```

## Basic run

Command:

```bash
python3 studycards.py --file notes.txt --out cards.csv
```

Output:

```
Wrote 2 cards to cards.csv
Skipped 1 lines without the :: separator.
```

The resulting `cards.csv` (no header, two columns: front, back):

```
Photosynthesis,The process plants use to turn sunlight into energy
Mitochondria,The part of the cell that produces most of its energy
```

## With reversed cards

Command:

```bash
python3 studycards.py --file notes.txt --out cards.csv --reverse
```

Output:

```
Wrote 4 cards to cards.csv
Skipped 1 lines without the :: separator.
```

The resulting `cards.csv`:

```
Photosynthesis,The process plants use to turn sunlight into energy
The process plants use to turn sunlight into energy,Photosynthesis
Mitochondria,The part of the cell that produces most of its energy
The part of the cell that produces most of its energy,Mitochondria
```
