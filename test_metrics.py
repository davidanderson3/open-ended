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

