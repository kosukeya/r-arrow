import csv
from pathlib import Path

import pytest

from r_arrow.stage2 import HORIZONS, stage2_census


RESULT_PATH = Path(__file__).parents[1] / "results" / "stage2_arrow_survival_map.csv"


def test_machine_readable_stage2_artifact_matches_executable_census() -> None:
    summary = stage2_census()
    expected = {row["label"]: row for row in summary["rows"]}

    with RESULT_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == summary["observation_count"] == 14
    assert {row["label"] for row in rows} == set(expected)

    for artifact in rows:
        computed = expected[artifact["label"]]
        assert int(artifact["macro_states"]) == computed["macro_states"]
        assert artifact["summary_classification"] == computed["summary_classification"]
        expected_l_star = "" if computed["L_star"] is None else str(computed["L_star"])
        assert artifact["L_star"] == expected_l_star
        assert (artifact["strongly_lumpable"].lower() == "true") is computed["strongly_lumpable"]

        for horizon in HORIZONS:
            assert float(artifact[f"A{horizon}"]) == pytest.approx(
                computed["arrow"][str(horizon)], abs=1e-12
            )
            assert float(artifact[f"r{horizon}"]) == pytest.approx(
                computed["r"][str(horizon)], abs=1e-12
            )
