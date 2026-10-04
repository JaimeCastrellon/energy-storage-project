import warnings

import pandas as pd

EXPECTED_EMPTY_HUB_COLUMNS = ["voltage", "equipment", "zone"]

def clean_pjm_lmp_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df["datetime_beginning_utc"] = pd.to_datetime(
        df["datetime_beginning_utc"], format="%m/%d/%Y %I:%M:%S %p", utc=True
    )

    df = df.sort_values("datetime_beginning_utc")

    n_dupes = df["datetime_beginning_utc"].duplicated().sum()
    if n_dupes:
        warnings.warn(
            f"Dropping {n_dupes} duplicate UTC timestamp row(s); keeping first occurrence."
        )
    df = df.drop_duplicates(subset=["datetime_beginning_utc"])

    df = df.set_index("datetime_beginning_utc")

    df = df.drop(columns = ["datetime_beginning_ept"], errors = "ignore")

    for col in EXPECTED_EMPTY_HUB_COLUMNS:
        if col in df.columns and df[col].isna().all():
            df = df.drop(columns = col)

    return df