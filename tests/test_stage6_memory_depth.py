from r_arrow.stage6 import stage6_memory_depth_map


EXPECTED = {
    "0|1|2|3": (1, 3, 3, 6, 6, True),
    "0|1|23": (2, 3, 3, 6, 6, True),
    "0|12|3": (1, 3, 3, 6, 6, True),
    "0|13|2": (1, 2, 2, 4, 4, True),
    "01|2|3": (1, 3, 3, 6, 6, True),
    "02|1|3": (None, 2, 2, 2, 0, False),
    "03|1|2": (2, 3, 3, 6, 6, True),
    "0|123": (None, 2, 2, 2, 0, False),
    "01|23": (3, 3, 3, 6, 6, True),
    "012|3": (None, 2, 2, 2, 0, False),
    "013|2": (None, 1, 1, 1, 0, False),
    "02|13": (None, 1, 1, 1, 0, False),
    "023|1": (None, 2, 2, 2, 0, False),
    "03|12": (3, 3, 3, 6, 6, True),
    "0123": (None, 1, 1, 1, 0, False),
}


def test_stage6_complete_rank_census() -> None:
    report = stage6_memory_depth_map()
    assert report["partition_count"] == 15
    rows = {row["label"]: row for row in report["primary_rows"]}
    assert set(rows) == set(EXPECTED)

    for label, expected in EXPECTED.items():
        row = rows[label]
        actual = (
            row["L_arrow"],
            row["forward_linear_rank"],
            row["reverse_linear_rank"],
            row["joint_forward_reverse_linear_rank"],
            row["reversal_contrast_linear_rank"],
            row["ratio_only_insufficiency_witness_within_prefix_3"],
        )
        assert actual == expected


def test_stage6_depth_and_linear_rank_are_distinct_axes() -> None:
    report = stage6_memory_depth_map()
    assert report["joint_rank_values_by_detection_depth"] == {
        "1": [4, 6],
        "2": [6],
        "3": [6],
        "infinity": [1, 2],
    }
    assert report["contrast_rank_values_by_detection_depth"] == {
        "1": [4, 6],
        "2": [6],
        "3": [6],
        "infinity": [0],
    }
    # The same exact joint rank occurs at three different finite detection depths.
    rows = {row["label"]: row for row in report["primary_rows"]}
    assert rows["0|12|3"]["joint_forward_reverse_linear_rank"] == 6
    assert rows["0|1|23"]["joint_forward_reverse_linear_rank"] == 6
    assert rows["01|23"]["joint_forward_reverse_linear_rank"] == 6
    assert [rows[label]["L_arrow"] for label in ("0|12|3", "0|1|23", "01|23")] == [1, 2, 3]


def test_stage6_ratio_only_state_fails_for_every_finite_arrow_partition() -> None:
    report = stage6_memory_depth_map()
    assert report["finite_arrow_partition_count"] == 8
    assert report["finite_arrow_partitions_with_ratio_only_counterexample"] == 8


def test_stage6_all_horizon_hidden_and_reversible_controls_have_zero_contrast_rank() -> None:
    report = stage6_memory_depth_map()
    hidden = [row for row in report["primary_rows"] if row["L_arrow"] is None]
    assert len(hidden) == 7
    assert all(row["reversal_contrast_linear_rank"] == 0 for row in hidden)
    assert report["reversible_control_partition_count"] == 15
    assert report["reversible_control_all_contrast_ranks_zero"] is True
