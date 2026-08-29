"""Executable Stage 5 temporal-order hierarchy synthesis."""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from typing import Any

from .benchmarks import higher_order_hidden_arrow_four_state
from .coarse_grain import Partition, observed_path_distribution, partition_label, set_partitions
from .equivalence import observed_time_reversal_equivalence
from .temporal_order import (
    cancellation_summary,
    macro_word_delta,
    micro_reversal_contributions,
    observed_odd_marginalization_matches,
    reversal_odd_mass,
    reversal_odd_pairs,
)


REPRESENTATIVES: tuple[tuple[str, Partition], ...] = (
    ("order_1_direct", ((0,), (1, 2), (3,))),
    ("order_2_hidden", ((0,), (1,), (2, 3))),
    ("order_3_hidden", ((0, 1), (2, 3))),
    ("all_horizon_hidden", ((0, 2), (1,), (3,))),
)


def _fraction(value: Fraction) -> str:
    return str(value)


def _word(value: tuple[int, ...] | None) -> list[int] | None:
    return list(value) if value is not None else None


def _odd_summary(matrix: Any, partition: Partition, horizon: int) -> dict[str, Any]:
    distribution = observed_path_distribution(matrix, horizon, partition)
    pairs = reversal_odd_pairs(distribution)
    return {
        "L": horizon,
        "odd_pair_count": len(pairs),
        "odd_mass": _fraction(reversal_odd_mass(distribution)),
        "marginalizes_to_previous_odd": observed_odd_marginalization_matches(matrix, horizon, partition),
        "pairs": [
            {
                "word": list(pair.word),
                "reverse_word": list(pair.reverse_word),
                "probability": _fraction(pair.probability),
                "reverse_probability": _fraction(pair.reverse_probability),
                "delta": _fraction(pair.delta),
            }
            for pair in pairs
        ],
    }


def _cancellation_record(matrix: Any, partition: Partition, word: tuple[int, ...]) -> dict[str, Any]:
    contributions = micro_reversal_contributions(matrix, partition, word)
    summary = cancellation_summary(contributions)
    macro_delta = macro_word_delta(matrix, partition, word)
    if summary.net_delta != macro_delta:
        raise AssertionError("micro contribution sum must equal exact macro word delta")
    return {
        "word": list(word),
        "reverse_word": list(reversed(word)),
        "macro_delta": _fraction(macro_delta),
        "summary": {
            "compatible_micro_paths": summary.compatible_micro_paths,
            "nonzero_micro_contributions": summary.nonzero_micro_contributions,
            "zero_micro_contributions": summary.zero_micro_contributions,
            "positive_total": _fraction(summary.positive_total),
            "negative_total": _fraction(summary.negative_total),
            "net_delta": _fraction(summary.net_delta),
            "absolute_total": _fraction(summary.absolute_total),
            "cancelled_mass": _fraction(summary.cancelled_mass),
        },
        "nonzero_micro_contributions": [
            {
                "micro_path": list(row.micro_path),
                "reverse_micro_path": list(row.reverse_micro_path),
                "probability": _fraction(row.probability),
                "reverse_probability": _fraction(row.reverse_probability),
                "delta": _fraction(row.delta),
            }
            for row in contributions
            if row.delta != 0
        ],
    }


def stage5_hierarchy() -> dict[str, Any]:
    """Return the frozen Stage 5 hierarchy for the existing four-state witness."""

    matrix = higher_order_hidden_arrow_four_state()
    partitions = tuple(set_partitions(4))
    rows: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()

    for partition in partitions:
        label = partition_label(partition, 4)
        result = observed_time_reversal_equivalence(matrix, partition)
        horizon = result.detection_horizon
        class_key = "infinity" if horizon is None else str(horizon)
        counts[class_key] += 1

        first_pairs = None
        first_mass = None
        lower_orders_zero = None
        if horizon is not None:
            if horizon > 3:
                raise AssertionError("Stage 5 must not extend beyond frozen Stage 4 detection depth")
            distribution = observed_path_distribution(matrix, horizon, partition)
            pairs = reversal_odd_pairs(distribution)
            if not pairs:
                raise AssertionError("finite detection horizon must have a nonzero reversal-odd component")
            first_pairs = len(pairs)
            first_mass = _fraction(reversal_odd_mass(distribution))
            lower_orders_zero = all(
                len(reversal_odd_pairs(observed_path_distribution(matrix, lower, partition))) == 0
                for lower in range(1, horizon)
            )
            if not lower_orders_zero:
                raise AssertionError("detection horizon must be the first nonzero odd order")

        rows.append(
            {
                "label": label,
                "partition": [list(block) for block in partition],
                "macro_states": len(partition),
                "L_arrow": horizon,
                "all_horizon_reversible": result.equivalent,
                "shortest_witness": _word(result.witness_word),
                "first_detection_odd_pair_count": first_pairs,
                "first_detection_odd_mass": first_mass,
                "all_lower_orders_zero": lower_orders_zero,
            }
        )

    representatives: list[dict[str, Any]] = []
    for name, partition in REPRESENTATIVES:
        label = partition_label(partition, 4)
        result = observed_time_reversal_equivalence(matrix, partition)
        profile = [_odd_summary(matrix, partition, horizon) for horizon in (1, 2, 3)]
        cancellation = None
        if result.witness_word is not None:
            cancellation = _cancellation_record(matrix, partition, result.witness_word)
        representatives.append(
            {
                "name": name,
                "label": label,
                "L_arrow": result.detection_horizon,
                "all_horizon_reversible": result.equivalent,
                "shortest_witness": _word(result.witness_word),
                "odd_profile_L1_to_L3": profile,
                "cancellation": cancellation,
            }
        )

    return {
        "stage": 5,
        "model": "higher_order_hidden_arrow_four_state",
        "state_count": 4,
        "partition_count": len(partitions),
        "temporal_order_definition": "minimum L>=1 with nonzero exact reversal-odd observed path component; null means exact all-horizon equivalence",
        "detection_class_summary": dict(sorted(counts.items())),
        "rows": rows,
        "representatives": representatives,
        "compact_criterion_status": "exact odd hierarchy and micro-to-macro cancellation decomposition established; no universal motif/partition criterion beyond the frozen family is claimed",
    }


def main() -> None:
    print(json.dumps(stage5_hierarchy(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
