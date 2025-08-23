# Open-Ended Neighborhood Scores

This repo contains a small HTML table ranking a selection of neighborhoods in the southeastern United States. The scoring system is out of 27 and each entry includes short notes—mainly about how state tax policies affect affordability.

The `index.html` file wraps the table with basic HTML and CSS so it can be viewed as a standalone page. The `live.html` file contains the same table without additional page chrome.

Columns in the table:

- **Rank** – emoji numbers representing the position.
- **Neighborhood** – name of the neighborhood.
- **Location** – city and state.
- **New Score (/27)** – composite score out of 27.
- **Notes** – contextual notes (e.g., tax situations).

These files are static and intended only for reference.

## Metrics

The `metrics.py` helper aggregates recordings or event logs to simple counts per day. Provide a JSON lines or CSV file containing a `timestamp` (or `date`) field for each recording:

```bash
python metrics.py recordings.jsonl
```

This prints one line per day with the number of records observed on that date.
Pass ``--output`` with a ``.json`` or ``.csv`` file to write the aggregated
counts in that format instead of printing them.

## Dream Script

The `dream.py` program prints a randomly generated field of ASCII stars—
a tiny fragment of a cosmic dream rendered in the terminal.
