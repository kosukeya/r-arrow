import math

import pytest

from r_arrow.stage2 import HORIZONS, stage2_census


def _row_by_label(summary: dict, label: str) -> dict:
    return next(row for row in summary["rows"] if row["label"] == label)


def test_stage2_census_covers_frozen_observation_family() -> None:
    summary = stage2_census()
    assert summary["observation_count"] == 14
    assert summary["horizons"] == [1, 2, 3, 4]
    assert len({row["label"] for row in summary["rows"]}) == 14


def test_full_reference_matches_stage1_arrow_rate() -> None:
    summary = stage2_census()
    identity = _row_by_label(summary, "0|1|2|3")
    for horizon in HORIZONS:
        expected = (horizon / 4.0) * math.log(2.0)
        assert summary["reference_arrow"][str(horizon)] == pytest.approx(expected, abs=1e-12)
        assert identity["arrow"][str(horizon)] == pytest.approx(expected, abs=1e-12)
        assert identity["r"][str(horizon)] == pytest.approx(1.0, abs=1e-12)
        assert identity["classification_at_L"][str(horizon)] == "preserved_at_L"


def test_data_processing_bound_holds_for_every_declared_case() -> None:
    summary = stage2_census()
    for row in summary["rows"]:
        for horizon in HORIZONS:
            ratio = row["r"][str(horizon)]
            assert ratio >= -1e-12
            assert ratio <= 1.0 + 1e-12
            assert row["arrow"][str(horizon)] >= -1e-12


def test_same_resolution_adjacent_vs_opposite_merge_has_structural_contrast() -> None:
    summary = stage2_census()
    adjacent = _row_by_label(summary, "01|2|3")
    opposite = _row_by_label(summary, "02|1|3")

    assert adjacent["macro_states"] == opposite["macro_states"] == 3
    assert adjacent["r"]["1"] == pytest.approx(0.75, abs=1e-12)
    assert all(adjacent["r"][str(horizon)] > 0.0 for horizon in HORIZONS)
    assert all(opposite["r"][str(horizon)] == pytest.approx(0.0, abs=1e-12) for horizon in HORIZONS)
    assert adjacent["summary_classification"] == "retained_through_L4"
    assert opposite["summary_classification"] == "undetected_through_L4"


def test_all_adjacent_pair_three_state_merges_are_symmetry_equivalent() -> None:
    summary = stage2_census()
    labels = ["01|2|3", "0|12|3", "0|1|23", "03|1|2"]
    rows = [_row_by_label(summary, label) for label in labels]
    reference = rows[0]["r"]
    assert all(row["r"] == pytest.approx(reference, abs=1e-12) for row in rows[1:])


def test_opposite_pair_three_state_merges_are_undetected_through_L4() -> None:
    summary = stage2_census()
    for label in ["02|1|3", "0|13|2"]:
        row = _row_by_label(summary, label)
        assert row["summary_classification"] == "undetected_through_L4"
        assert row["L_star"] is None
        assert all(row["arrow"][str(horizon)] == pytest.approx(0.0, abs=1e-12) for horizon in HORIZONS)


def test_all_two_macrostate_observations_are_undetected_through_L4() -> None:
    summary = stage2_census()
    two_state_rows = [row for row in summary["rows"] if row["macro_states"] == 2]
    assert len(two_state_rows) == 7
    for row in two_state_rows:
        assert row["summary_classification"] == "undetected_through_L4"
        assert row["L_star"] is None
        assert all(row["r"][str(horizon)] == pytest.approx(0.0, abs=1e-12) for horizon in HORIZONS)


def test_no_memory_revealed_arrow_occurs_in_frozen_L1_to_L4_census() -> None:
    summary = stage2_census()
    assert all(row["summary_classification"] != "memory_revealed_arrow" for row in summary["rows"])


def test_adjacent_pair_retention_increases_over_frozen_horizons() -> None:
    summary = stage2_census()
    row = _row_by_label(summary, "01|2|3")
    ratios = [row["r"][str(horizon)] for horizon in HORIZONS]
    assert ratios == sorted(ratios)
    assert ratios[0] == pytest.approx(0.75, abs=1e-12)
    assert ratios[-1] == pytest.approx(0.947203072883, abs=1e-12)
