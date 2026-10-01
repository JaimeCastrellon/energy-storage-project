from pathlib import Path

import pandas as pd

from src.data_pipeline.cleaning import clean_pjm_lmp_data

def save_processed(df: pd.DataFrame, path: str) -> None:
    out = Path(path)
    out.parent.mkdir(parents = True, exist_ok = True)
    df.to_parquet(out)

if __name__ == "__main__":

    raw_path = "data/raw/pjm_western_hub_da_2025-09-18_to_2026-09-18.csv"
    out_path = "data/processed/pjm_western_hub_da_2025-09-18_to_2026-09-18.parquet"

    raw_df = pd.read_csv(raw_path)
    clean_df = clean_pjm_lmp_data(raw_df)

    save_processed(clean_df, out_path)

    loaded = pd.read_parquet(out_path)
    print(loaded.dtypes)
    print(loaded.index.dtype)
    print(loaded.shape)
