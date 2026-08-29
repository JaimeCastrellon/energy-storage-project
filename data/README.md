# Data

This folder is intentionally empty in git (see `.gitignore` — only `.gitkeep`
placeholder files are tracked). Historical price data is:

- too large to sensibly store in a git repo
- freely re-downloadable from EIA/PJM, so there's no need to version it here

## Structure

- `raw/` — data exactly as pulled from source APIs, never modified by hand
- `processed/` — cleaned, aligned, analysis-ready data (Parquet format)

## To populate

Run the data pipeline scripts in `src/data_pipeline/` (Phase 1) once they exist.
Each script documents which API it hits and what date range it pulls.
