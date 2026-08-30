import json
from pathlib import Path

from r_arrow.stage6 import stage6_memory_depth_map


ARTIFACT = Path("results/stage6_memory_depth_map.json")


def _projection(report: dict) -> dict:
    rows = [
        {
            "label": row["label"],
            "L_arrow": row["L_arrow"],
            "forward_rank": row["forward_linear_rank"],
            "reverse_rank": row["reverse_linear_rank"],
            "joint_rank": row["joint_forward_reverse_linear_rank"],
            "contrast_rank": row["reversal_contrast_linear_rank"],
            "ratio_counterexample": row["ratio_only_insufficiency_witness_within_prefix_3"],
        }
        for row in report["primary_rows"]
    ]

    representative_ratio_witnesses = []
    for row in report["representatives"]:
        witness = row["ratio_witness"]
        if witness is None:
            representative_ratio_witnesses.append(
                {"name": row["name"], "label": row["label"], "witness": None}
            )
        else:
            representative_ratio_witnesses.append(
                {
                    "name": row["name"],
                    "label": row["label"],
                    **witness,
                }
            )

    return {
        "stage": report["stage"],
        "model": report["model"],
        "partition_count": report["partition_count"],
        "finite_arrow_partition_count": report["finite_arrow_partition_count"],
        "finite_arrow_partitions_with_ratio_only_counterexample": report[
            "finite_arrow_partitions_with_ratio_only_counterexample"
        ],
        "joint_rank_values_by_detection_depth": report["joint_rank_values_by_detection_depth"],
        "contrast_rank_values_by_detection_depth": report[
            "contrast_rank_values_by_detection_depth"
        ],
        "rows": rows,
        "representative_ratio_witnesses": representative_ratio_witnesses,
        "reversible_control_partition_count": report["reversible_control_partition_count"],
        "reversible_control_all_contrast_ranks_zero": report[
            "reversible_control_all_contrast_ranks_zero"
        ],
        "causal_state_track_status": report["causal_state_track_status"],
    }


def test_stage6_machine_readable_artifact_matches_runtime() -> None:
    frozen = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    assert frozen == _projection(stage6_memory_depth_map())
