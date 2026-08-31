"""Executable Stage 6 minimal arrow-memory synthesis."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import Any

from .arrow_memory import (
    filter_matches_direct_word_probability,
    likelihood_ratio_insufficiency_witness,
    linear_memory_profile,
)
from .benchmarks import higher_order_hidden_arrow_four_state, reversible_four_cycle
from .coarse_grain import Partition, partition_label, set_partitions
from .equivalence import observed_time_reversal_equivalence


REPRESENTATIVES: tuple[tuple[str, Partition], ...] = (
    ("order_1_direct", ((0,), (1, 2), (3,))),
    ("order_2_hidden", ((0,), (1,), (2, 3))),
    ("order_3_hidden", ((0, 1), (2, 3))),
    ("all_horizon_hidden", ((0, 2), (1,), (3,))),
)


def _fraction(value: Fraction | None) -> str | None:
    return None if value is None else str(value)


def _word(value: tuple[int, ...] | None) -> list[int] | None:
    return None if value is None else list(value)


def _witness_record(witness: Any) -> dict[str, Any] | None:
    if witness is None:
        return None
    return {
        "prefix_a": list(witness.prefix_a),
        "prefix_b": list(witness.prefix_b),
        "current_ratio": _fraction(witness.current_ratio),
        "extension_symbol": witness.extension_symbol,
        "updated_ratio_a": _fraction(witness.updated_ratio_a),
        "updated_ratio_b": _fraction(witness.updated_ratio_b),
    }


def _memory_row(matrix: Any, partition: Partition) -> dict[str, Any]:
    label = partition_label(partition, 4)
    equivalence = observed_time_reversal_equivalence(matrix, partition)
    profile = linear_memory_profile(matrix, partition)
    witness = likelihood_ratio_insufficiency_witness(matrix, partition, max_prefix_symbols=3)

    if equivalence.equivalent and profile.reversal_contrast_rank != 0:
        raise AssertionError("all-horizon reversible observation must have zero contrast rank")
    if not equivalence.equivalent and profile.reversal_contrast_rank == 0:
        raise AssertionError("irreversible observed word series must have positive contrast rank")

    return {
        "label": label,
        "partition": [list(block) for block in partition],
        "macro_states": len(partition),
        "L_arrow": equivalence.detection_horizon,
        "all_horizon_reversible": equivalence.equivalent,
        "forward_linear_rank": profile.forward_rank,
        "reverse_linear_rank": profile.reverse_rank,
        "joint_forward_reverse_linear_rank": profile.joint_forward_reverse_rank,
        "reversal_contrast_linear_rank": profile.reversal_contrast_rank,
        "joint_ambient_dimension": profile.joint_ambient_dimension,
        "ratio_only_insufficiency_witness_within_prefix_3": witness is not None,
        "ratio_witness": _witness_record(witness),
    }


@lru_cache(maxsize=1)
def stage6_memory_depth_map() -> dict[str, Any]:
    """Return the bounded Stage 6 exact Memory–Depth Map."""

    witness_matrix = higher_order_hidden_arrow_four_state()
    partitions = tuple(set_partitions(4))
    primary_rows = [_memory_row(witness_matrix, partition) for partition in partitions]

    # Filter correctness is checked on the shortest Stage 5 witness where one exists.
    for row, partition in zip(primary_rows, partitions, strict=True):
        equivalence = observed_time_reversal_equivalence(witness_matrix, partition)
        word = equivalence.witness_word
        if word is not None and not filter_matches_direct_word_probability(witness_matrix, partition, word):
            raise AssertionError("recursive filter must reproduce direct exact word likelihoods")

    reversible_rows = [_memory_row(reversible_four_cycle(), partition) for partition in partitions]
    if any(row["reversal_contrast_linear_rank"] != 0 for row in reversible_rows):
        raise AssertionError("reversible control must have zero contrast rank for every partition")

    by_detection_depth: defaultdict[str, list[int]] = defaultdict(list)
    by_detection_depth_contrast: defaultdict[str, list[int]] = defaultdict(list)
    for row in primary_rows:
        key = "infinity" if row["L_arrow"] is None else str(row["L_arrow"])
        by_detection_depth[key].append(row["joint_forward_reverse_linear_rank"])
        by_detection_depth_contrast[key].append(row["reversal_contrast_linear_rank"])

    finite_rows = [row for row in primary_rows if row["L_arrow"] is not None]
    finite_ratio_counterexamples = sum(
        bool(row["ratio_only_insufficiency_witness_within_prefix_3"])
        for row in finite_rows
    )
    if finite_ratio_counterexamples != len(finite_rows):
        raise AssertionError("every finite-arrow partition must have the frozen exact ratio-only counterexample")

    representative_rows: list[dict[str, Any]] = []
    row_by_label = {row["label"]: row for row in primary_rows}
    for name, partition in REPRESENTATIVES:
        label = partition_label(partition, 4)
        representative_rows.append({"name": name, **row_by_label[label]})

    rank_pair_counts: Counter[str] = Counter(
        f"L={('infinity' if row['L_arrow'] is None else row['L_arrow'])},joint={row['joint_forward_reverse_linear_rank']}"
        for row in primary_rows
    )

    return {
        "stage": 6,
        "model": "higher_order_hidden_arrow_four_state",
        "state_count": 4,
        "partition_count": len(partitions),
        "primary_memory_definition": "minimal exact weighted-linear realization rank for the joint forward/reverse observed word-likelihood series",
        "contrast_definition": "minimal exact weighted-linear realization rank for P_forward(word)-P_reverse(word)",
        "ratio_only_audit_bound": "prefix length <=3; a found witness is an exact insufficiency proof, absence alone is not a general sufficiency proof",
        "primary_rows": primary_rows,
        "representatives": representative_rows,
        "joint_rank_values_by_detection_depth": {
            key: sorted(set(values)) for key, values in sorted(by_detection_depth.items())
        },
        "contrast_rank_values_by_detection_depth": {
            key: sorted(set(values)) for key, values in sorted(by_detection_depth_contrast.items())
        },
        "finite_arrow_partition_count": len(finite_rows),
        "finite_arrow_partitions_with_ratio_only_counterexample": finite_ratio_counterexamples,
        "rank_pair_counts": dict(sorted(rank_pair_counts.items())),
        "reversible_control_partition_count": len(reversible_rows),
        "reversible_control_all_contrast_ranks_zero": all(
            row["reversal_contrast_linear_rank"] == 0 for row in reversible_rows
        ),
        "causal_state_track_status": "not promoted to a primary success condition; no open-ended or approximate mixed-state closure search performed",
    }


def main() -> None:
    print(json.dumps(stage6_memory_depth_map(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
