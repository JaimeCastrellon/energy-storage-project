import pandas as pd

def clean_pjm_lmp_data(df: pd.DataFrame) -> pd.DataFrame:

    df["datetime_beginning_utc"] = pd.to_datetime(
        df["datetime_beginning_utc"], format="%m/%d/%Y %I:%M:%S %p"
    )

    df = df.sort_values("datetime_beginning_utc")

    df = df.drop_duplicates(subset=["datetime_beginning_utc"])

    df = df.set_index("datetime_beginning_utc")

    return df

if __name__ == "__main__":
    file_name = input("Enter the CSV file name: ")
    df = pd.read_csv(file_name)
    df = clean_pjm_lmp_data(df)
    print(df.head())

    print(df.shape)
    print(df.index.dtype)
    print(df.index.name)
    print(df.loc["2025-11-02 05:00:00"])
    print(df.loc["2025-11-02 06:00:00"])