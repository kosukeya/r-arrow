import json
import math
from pathlib import Path

from r_arrow.stage3 import stage3_summary


ARTIFACT = Path(__file__).resolve().parents[1] / "results" / "stage3_structural_criteria.json"


def test_stage3_machine_readable_artifact_matches_executable_summary():
    frozen = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    live = stage3_summary()

    assert frozen["stage"] == live["stage"] == 3
    assert frozen["stage2_one_step_regression"]["observation_count"] == live["stage2_one_step_regression"]["observation_count"] == 14
    assert frozen["stage2_one_step_regression"]["mismatches"] == live["stage2_one_step_regression"]["mismatches"] == []

    frozen_witness = frozen["higher_order_witness"]
    live_witness = live["higher_order_witness"]

    for key in (
        "states",
        "partition",
        "stationary_distribution",
        "macro_flux",
        "macro_flux_symmetric",
        "first_asymmetric_horizon",
    ):
        assert frozen_witness[key] == live_witness[key]

    for family in ("micro_arrow", "observed_arrow"):
        for horizon in ("1", "2", "3", "4"):
            assert math.isclose(
                frozen_witness[family][horizon],
                live_witness[family][horizon],
                rel_tol=0.0,
                abs_tol=1e-15,
            )

    exact = frozen_witness["exact_L3_witness"]
    matches = [
        witness
        for witness in live_witness["L3_exact_witnesses"]
        if witness["path"] == exact["path"] and witness["reverse"] == exact["reverse"]
    ]
    assert len(matches) == 1
    assert matches[0]["probability"] == exact["probability"]
    assert matches[0]["reverse_probability"] == exact["reverse_probability"]
