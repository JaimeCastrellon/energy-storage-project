import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/pjm_western_hub_da_2025-09-18_to_2026-09-18.csv")
df["datetime_beginning_ept"] = pd.to_datetime(
    df["datetime_beginning_ept"], format="%m/%d/%Y %I:%M:%S %p"
)


df = df.sort_values("datetime_beginning_ept")

plt.plot(df["datetime_beginning_ept"], df["total_lmp_da"])

plt.xlabel("Time")
plt.ylabel("Total LMP Day-Ahead ($/MWh)")

plt.title("PJM Western Hub — Day-Ahead Price, 9/18/2025–9/18/2026")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("results/western_hub_first_year.png")

print(df["total_lmp_da"].describe())

print(df["datetime_beginning_ept"].duplicated().sum())
print(len(df))

dupe_mask = df["datetime_beginning_ept"].duplicated(keep=False)
print(df.loc[dupe_mask, ["datetime_beginning_ept", "total_lmp_da"]])

dupe_utc = df["datetime_beginning_utc"].duplicated(keep=False)
print(dupe_utc.sum())