import pandas as pd

EXPECTED_EMPTY_HUB_COLUMNS = ["voltage", "equipmennt", "zone"]

def clean_pjm_lmp_data(df: pd.DataFrame) -> pd.DataFrame:

    df["datetime_beginning_utc"] = pd.to_datetime(
        df["datetime_beginning_utc"], format="%m/%d/%Y %I:%M:%S %p"
    )

    df = df.sort_values("datetime_beginning_utc")

    df = df.drop_duplicates(subset=["datetime_beginning_utc"])

    df = df.set_index("datetime_beginning_utc")

    df = df.drop(columns = ["datetime_beginning_ept"], errors = "ignore")

    for col in EXPECTED_EMPTY_HUB_COLUMNS:
        if col in df.columns and df[col].isna().all():
            df = df.drop(columns = col)

    return df