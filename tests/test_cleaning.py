import pandas as pd
from src.data_pipeline.cleaning import clean_pjm_lmp_data

def test_dst_fallback_hour_not_lost():

    raw = pd.DataFrame({
        "datetime_beginning_utc": ["11/2/2025 5:00:00 AM", "11/2/2025 6:00:00 AM"],
        "datetime_beginning_ept": ["11/2/2025 1:00:00 AM", "11/2/2025 1:00:00 AM"],
        "total_lmp_da": [44.15, 39.914945],
    })

    cleaned = clean_pjm_lmp_data(raw)

    assert len(cleaned) == 2

