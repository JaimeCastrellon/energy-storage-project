"""
Sanity tests for the repo scaffold itself.

These aren't testing 'real' logic yet (there isn't any — that starts in
Phase 1), but they give CI something genuine to run from the very first
commit, and they document the structure the rest of the code should
assume exists.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def test_expected_top_level_dirs_exist():
    expected = ["data", "src", "tests", "notebooks", "results"]
    for name in expected:
        assert (PROJECT_ROOT / name).is_dir(), f"missing expected dir: {name}"


def test_expected_src_modules_exist():
    expected = ["data_pipeline", "models", "sim_engine", "bindings", "rl"]
    for name in expected:
        assert (PROJECT_ROOT / "src" / name).exists(), f"missing src/{name}"


def test_data_subdirs_exist_but_are_not_committed_with_data():
    for sub in ["raw", "processed"]:
        d = PROJECT_ROOT / "data" / sub
        assert d.is_dir()
        # .gitkeep should exist (dir is tracked); real data files should not be
        assert (d / ".gitkeep").exists()
