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

## Codex-Friendly Novel Structure

This project now includes a lightweight novel workspace with a structure designed
for Codex-friendly chunking.

**Recommended file layout**

- `00_outline.md` – act-level outline and chapter map.
- `series_bible.md` – characters, settings, timeline, rules.
- `glossary.md` – key terms, names, recurring motifs.
- `continuity_log.md` – track retcons and major changes.
- `01_ch01.md`, `02_ch02.md`, `03_ch03.md` – one chapter per file.

**Chapter file template**

Each chapter starts with a small context header so the file is editable in
isolation:

```
# Chapter X: Title
## Context
- Timeline position:
- POV:
- Location:
- Key state (before):
- Key state (after):
- Continuity notes / open threads:
```

### Principles

1. Keep files small and coherent (1–3k words when possible).
2. Include a context header in every chapter/scene file.
3. Use consistent filenames with numeric prefixes for ordering.
4. Maintain a single source of truth for canon in `series_bible.md`.
5. Record major changes in `continuity_log.md`.
6. Restate critical dependencies in the current file.
7. Track open threads in the context header.
8. Avoid multi-POV or multi-location jumps in a single file.
9. Summarize transitions in the context header when needed.
10. Prefer explicit structure over hidden conventions.

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
