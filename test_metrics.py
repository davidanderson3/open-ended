import csv
import json
from pathlib import Path

import pytest

from metrics import metric_counts_per_day, write_counts


def test_metric_counts_per_day_and_write(tmp_path: Path) -> None:
    records = [
        {"timestamp": "2024-04-01T12:00:00"},
        {"date": "2024-04-01"},
        {"timestamp": "2024-04-02T00:00:00"},
    ]

    counts = metric_counts_per_day(records)
    assert counts == {"2024-04-01": 2, "2024-04-02": 1}

    out_file = tmp_path / "counts.json"
    write_counts(counts, out_file)
    data = json.loads(out_file.read_text())
    assert data == counts


def test_write_counts_csv(tmp_path: Path) -> None:
    counts = {"2024-04-01": 2, "2024-04-02": 1}
    out_file = tmp_path / "counts.csv"
    write_counts(counts, out_file)
    with out_file.open() as f:
        rows = list(csv.DictReader(f))
    assert rows == [
        {"date": "2024-04-01", "count": "2"},
        {"date": "2024-04-02", "count": "1"},
    ]

