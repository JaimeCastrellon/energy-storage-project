import pandas as pd
from src.data_pipeline.cleaning import clean_pjm_lmp_data
from src.data_pipeline.storage import save_processed

def test_save_processed_parquet_round_trip(tmp_path):

    raw = pd.DataFrame({
        "datetime_beginning_utc": ["11/2/2025 5:00:00 AM", "11/2/2025 6:00:00 AM"],
        "total_lmp_da": [44.15, 39.914945],
    })
    cleaned = clean_pjm_lmp_data(raw)

    out_path = tmp_path / "nested" / "lmp.parquet"
    save_processed(cleaned, str(out_path))

    loaded = pd.read_parquet(out_path)

    pd.testing.assert_frame_equal(loaded, cleaned, check_freq=False)
