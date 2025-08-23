import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Aggregate metric counts per day")
    parser.add_argument("file", help="Input file containing recordings")
    parser.add_argument(
        "--format",
        choices=["json", "csv"],
        default="json",
        help="Format of the input file: json lines or CSV",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to write the aggregated counts as JSON or CSV",
    )
    return parser.parse_args()


def load_records(path: Path, fmt: str):
    if fmt == "json":
        with path.open() as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                yield json.loads(line)
    else:
        with path.open() as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row


def metric_counts_per_day(records):
    counts = defaultdict(int)
    for rec in records:
        ts = rec.get("timestamp") or rec.get("date")
        if not ts:
            continue
        try:
            dt = datetime.fromisoformat(ts)
        except ValueError:
            # if date only, just parse that
            dt = datetime.fromisoformat(ts + "T00:00:00")
        day = dt.date().isoformat()
        counts[day] += 1
    return counts


def write_counts(counts, path: Path) -> None:
    """Write ``counts`` mapping to ``path``.

    The format is determined by the file suffix: ``.json`` produces a JSON
    object mapping days to counts, while ``.csv`` writes a two-column CSV with
    ``date`` and ``count`` headers.
    """

    with path.open("w", newline="") as f:
        if path.suffix == ".csv":
            writer = csv.writer(f)
            writer.writerow(["date", "count"])
            for day, count in sorted(counts.items()):
                writer.writerow([day, count])
        else:
            json.dump(dict(counts), f, indent=2)


def main():
    args = parse_args()
    path = Path(args.file)
    records = list(load_records(path, args.format))
    counts = metric_counts_per_day(records)
    if args.output:
        write_counts(counts, args.output)
    else:
        for day in sorted(counts):
            print(f"{day} {counts[day]}")


if __name__ == "__main__":
    main()
