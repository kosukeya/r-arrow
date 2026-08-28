from collections import Counter

from r_arrow.stage4 import partition_hasse_edges, partition_refines, stage4_frontier
from r_arrow.coarse_grain import set_partitions


def _counts_for_model(frontier: dict, model: str) -> Counter:
    counts = Counter()
    for row in frontier["rows"]:
        if row["model"] != model:
            continue
        counts["infinity" if row["L_arrow"] is None else row["L_arrow"]] += 1
    return counts


def test_partition_refinement_relation_and_hasse_edges_are_well_formed() -> None:
    partitions = set_partitions(4)
    identity = ((0,), (1,), (2,), (3,))
    one_block = ((0, 1, 2, 3),)
    assert partition_refines(identity, one_block)
    assert not partition_refines(one_block, identity)
    edges = partition_hasse_edges(partitions)
    assert edges
    assert all(partition_refines(fine, coarse) for fine, coarse in edges)


def test_stage4_census_has_45_rows_and_no_refinement_violation() -> None:
    frontier = stage4_frontier()
    assert frontier["model_count"] == 3
    assert frontier["partitions_per_model"] == 15
    assert frontier["row_count"] == 45
    assert frontier["refinement_monotonicity_violations"] == []


def test_biased_cycle_stage2_nondetections_upgrade_to_all_horizon_certificates() -> None:
    frontier = stage4_frontier()
    counts = _counts_for_model(frontier, "biased_four_cycle")
    assert counts == Counter({"infinity": 10, 1: 5})

    primary_rows = [
        row
        for row in frontier["rows"]
        if row["model"] == "biased_four_cycle" and row["macro_states"] >= 2
    ]
    # Stage 2 had 9 primary observations undetected through L=4; Stage 4 now
    # certifies all 9 as all-horizon reversible under their observations.
    assert sum(row["all_horizon_reversible"] for row in primary_rows) == 9


def test_stage3_witness_frontier_realizes_L1_L2_L3_and_infinity() -> None:
    frontier = stage4_frontier()
    counts = _counts_for_model(frontier, "higher_order_hidden_arrow_four_state")
    assert counts == Counter({"infinity": 7, 1: 4, 2: 2, 3: 2})

    binary = next(
        row
        for row in frontier["rows"]
        if row["model"] == "higher_order_hidden_arrow_four_state" and row["label"] == "01|23"
    )
    assert binary["L_arrow"] == 3
    assert binary["witness_word"] == [0, 0, 1, 0]


def test_reversible_control_is_all_horizon_reversible_under_every_partition() -> None:
    frontier = stage4_frontier()
    counts = _counts_for_model(frontier, "reversible_four_cycle")
    assert counts == Counter({"infinity": 15})


def test_detection_depth_never_exceeds_three_in_frozen_family() -> None:
    frontier = stage4_frontier()
    finite = [row["L_arrow"] for row in frontier["rows"] if row["L_arrow"] is not None]
    assert finite
    assert max(finite) == 3
