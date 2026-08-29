import json
from pathlib import Path

from r_arrow.stage5 import stage5_hierarchy


ARTIFACT = Path(__file__).resolve().parents[1] / "results" / "stage5_temporal_order_hierarchy.json"


def test_stage5_json_artifact_matches_executable_summary():
    artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    result = stage5_hierarchy()

    assert artifact["stage"] == result["stage"]
    assert artifact["model"] == result["model"]
    assert artifact["state_count"] == result["state_count"]
    assert artifact["partition_count"] == result["partition_count"]
    assert artifact["detection_class_summary"] == result["detection_class_summary"]

    expected_rows = [
        {
            "label": row["label"],
            "L_arrow": row["L_arrow"],
            "odd_pair_count": row["first_detection_odd_pair_count"],
            "odd_mass": row["first_detection_odd_mass"],
        }
        for row in result["rows"]
    ]
    assert artifact["first_detection_classes"] == expected_rows


def test_stage5_json_representatives_match_executable_profiles_and_cancellation():
    artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    result = stage5_hierarchy()
    result_by_name = {row["name"]: row for row in result["representatives"]}

    for expected in artifact["representatives"]:
        actual = result_by_name[expected["name"]]
        assert expected["label"] == actual["label"]
        assert expected["L_arrow"] == actual["L_arrow"]
        assert expected["shortest_witness"] == actual["shortest_witness"]

        projected_profile = [
            {
                "L": entry["L"],
                "odd_pair_count": entry["odd_pair_count"],
                "odd_mass": entry["odd_mass"],
            }
            for entry in actual["odd_profile_L1_to_L3"]
        ]
        assert expected["odd_profile"] == projected_profile

        if expected["name"] == "all_horizon_hidden":
            assert actual["all_horizon_reversible"] is True
            assert actual["cancellation"] is None
            assert expected["all_horizon_reversible"] is True
        else:
            assert expected["cancellation"] == actual["cancellation"]["summary"]
