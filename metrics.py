import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Aggregate metric counts per day")
    parser.add_argument("file", help="Input file containing recordings")
    parser.add_argument("--format", choices=["json", "csv"], default="json",
                        help="Format of the input file: json lines or CSV")
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


def main():
    args = parse_args()
    path = Path(args.file)
    records = list(load_records(path, args.format))
    counts = metric_counts_per_day(records)
    for day in sorted(counts):
        print(f"{day} {counts[day]}")


if __name__ == "__main__":
    main()
