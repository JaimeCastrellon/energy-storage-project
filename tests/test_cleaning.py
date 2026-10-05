import pandas as pd
import pytest
from src.data_pipeline.cleaning import clean_pjm_lmp_data

def test_dst_fallback_hour_not_lost():

    raw = pd.DataFrame({
        "datetime_beginning_utc": ["11/2/2025 5:00:00 AM", "11/2/2025 6:00:00 AM"],
        "datetime_beginning_ept": ["11/2/2025 1:00:00 AM", "11/2/2025 1:00:00 AM"],
        "total_lmp_da": [44.15, 39.914945],
    })

    cleaned = clean_pjm_lmp_data(raw)

    assert len(cleaned) == 2


def test_empty_hub_columns_dropped_but_populated_kept():

    raw = pd.DataFrame({
        "datetime_beginning_utc": ["11/2/2025 5:00:00 AM", "11/2/2025 6:00:00 AM"],
        "datetime_beginning_ept": ["11/2/2025 1:00:00 AM", "11/2/2025 1:00:00 AM"],
        "voltage": [None, None],
        "equipment": [None, None],
        "zone": ["WEST", "WEST"],
        "total_lmp_da": [44.15, 39.914945],
    })

    cleaned = clean_pjm_lmp_data(raw)

    assert "voltage" not in cleaned.columns
    assert "equipment" not in cleaned.columns
    assert "datetime_beginning_ept" not in cleaned.columns
    assert "zone" in cleaned.columns


def test_input_dataframe_not_mutated():

    raw = pd.DataFrame({
        "datetime_beginning_utc": ["11/2/2025 6:00:00 AM", "11/2/2025 5:00:00 AM"],
        "datetime_beginning_ept": ["11/2/2025 1:00:00 AM", "11/2/2025 1:00:00 AM"],
        "total_lmp_da": [39.914945, 44.15],
    })
    original = raw.copy()

    clean_pjm_lmp_data(raw)

    pd.testing.assert_frame_equal(raw, original)


def test_index_is_sorted_utc():

    raw = pd.DataFrame({
        "datetime_beginning_utc": ["11/2/2025 6:00:00 AM", "11/2/2025 5:00:00 AM"],
        "total_lmp_da": [39.914945, 44.15],
    })

    cleaned = clean_pjm_lmp_data(raw)

    assert str(cleaned.index.tz) == "UTC"
    assert cleaned.index.is_monotonic_increasing
    assert cleaned["total_lmp_da"].tolist() == [44.15, 39.914945]


def test_duplicate_utc_rows_dropped_with_warning():

    raw = pd.DataFrame({
        "datetime_beginning_utc": ["11/2/2025 5:00:00 AM", "11/2/2025 5:00:00 AM"],
        "total_lmp_da": [44.15, 44.15],
    })

    with pytest.warns(UserWarning, match="duplicate"):
        cleaned = clean_pjm_lmp_data(raw)

    assert len(cleaned) == 1
