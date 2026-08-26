import json

import pytest

from r_arrow.stage1 import run_stage1


def test_stage1_summary_is_serializable_and_calibrated():
    payload = run_stage1()
    json.dumps(payload)

    assert payload["stage"] == 1
    assert payload["status"] == "benchmark_evaluated"
    assert payload["horizon_set"] == [1, 2, 3, 4]

    assert payload["reversible"]["detailed_balance"] is True
    assert payload["irreversible"]["detailed_balance"] is False

    for row in payload["reversible"]["horizons"]:
        assert row["A_L"] == pytest.approx(0.0, abs=1e-15)
        assert row["absolute_error"] == pytest.approx(0.0, abs=1e-15)

    for row in payload["irreversible"]["horizons"]:
        assert row["A_L"] > 0.0
        assert row["A_L"] == pytest.approx(row["expected_A_L"], rel=1e-13, abs=1e-15)
        assert row["absolute_error"] == pytest.approx(0.0, abs=1e-15)
