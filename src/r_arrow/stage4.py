"""Executable Stage 4 observation-resolution / history-depth frontier."""

from __future__ import annotations

import json
from collections import Counter
from math import inf
from typing import Any, Sequence

from .benchmarks import (
    biased_four_cycle,
    higher_order_hidden_arrow_four_state,
    reversible_four_cycle,
)
from .coarse_grain import Partition, canonical_partition, partition_label, set_partitions
from .equivalence import observed_time_reversal_equivalence


def partition_refines(
    fine: Sequence[Sequence[int]],
    coarse: Sequence[Sequence[int]],
    n_states: int = 4,
) -> bool:
    """Return True iff every fine block lies inside one coarse block."""

    fine_canonical = canonical_partition(fine, n_states)
    coarse_canonical = canonical_partition(coarse, n_states)
    coarse_sets = tuple(set(block) for block in coarse_canonical)
    return all(any(set(block) <= coarse_block for coarse_block in coarse_sets) for block in fine_canonical)


def partition_hasse_edges(partitions: Sequence[Partition], n_states: int = 4) -> tuple[tuple[Partition, Partition], ...]:
    """Return fine->coarse cover relations in the finite partition lattice."""

    edges: list[tuple[Partition, Partition]] = []
    for fine in partitions:
        for coarse in partitions:
            if fine == coarse or not partition_refines(fine, coarse, n_states):
                continue
            has_intermediate = any(
                middle not in {fine, coarse}
                and partition_refines(fine, middle, n_states)
                and partition_refines(middle, coarse, n_states)
                for middle in partitions
            )
            if not has_intermediate:
                edges.append((fine, coarse))
    return tuple(sorted(edges, key=lambda edge: (partition_label(edge[0], n_states), partition_label(edge[1], n_states))))


def _horizon_order(value: int | None) -> float:
    return inf if value is None else float(value)


def stage4_frontier() -> dict[str, Any]:
    """Return the complete fixed three-model / fifteen-partition Stage 4 census."""

    benchmarks = (
        ("biased_four_cycle", biased_four_cycle()),
        ("higher_order_hidden_arrow_four_state", higher_order_hidden_arrow_four_state()),
        ("reversible_four_cycle", reversible_four_cycle()),
    )
    partitions = tuple(set_partitions(4))
    edges = partition_hasse_edges(partitions, 4)

    rows: list[dict[str, Any]] = []
    horizon_by_model_partition: dict[tuple[str, str], int | None] = {}
    for model_name, matrix in benchmarks:
        for partition in partitions:
            label = partition_label(partition, 4)
            result = observed_time_reversal_equivalence(matrix, partition)
            horizon_by_model_partition[(model_name, label)] = result.detection_horizon
            rows.append(
                {
                    "model": model_name,
                    "partition": [list(block) for block in partition],
                    "label": label,
                    "macro_states": len(partition),
                    "L_arrow": result.detection_horizon,
                    "all_horizon_reversible": result.equivalent,
                    "witness_word": list(result.witness_word) if result.witness_word is not None else None,
                    "witness_forward_probability": str(result.forward_probability) if result.forward_probability is not None else None,
                    "witness_reverse_probability": str(result.reverse_probability) if result.reverse_probability is not None else None,
                    "reachable_dimension": result.reachable_dimension,
                    "expanded_basis_vectors": result.expanded_basis_vectors,
                }
            )

    violations: list[dict[str, Any]] = []
    for model_name, _ in benchmarks:
        for fine, coarse in edges:
            fine_label = partition_label(fine, 4)
            coarse_label = partition_label(coarse, 4)
            fine_horizon = horizon_by_model_partition[(model_name, fine_label)]
            coarse_horizon = horizon_by_model_partition[(model_name, coarse_label)]
            if _horizon_order(fine_horizon) > _horizon_order(coarse_horizon):
                violations.append(
                    {
                        "model": model_name,
                        "fine": fine_label,
                        "coarse": coarse_label,
                        "fine_L_arrow": fine_horizon,
                        "coarse_L_arrow": coarse_horizon,
                    }
                )

    summaries: dict[str, dict[str, int]] = {}
    for model_name, _ in benchmarks:
        counts: Counter[str] = Counter()
        for row in rows:
            if row["model"] != model_name:
                continue
            key = "infinity" if row["L_arrow"] is None else str(row["L_arrow"])
            counts[key] += 1
        summaries[model_name] = dict(sorted(counts.items()))

    return {
        "stage": 4,
        "state_count": 4,
        "model_count": len(benchmarks),
        "partitions_per_model": len(partitions),
        "row_count": len(rows),
        "L_arrow_definition": "minimum L>=1 with observed path-reversal asymmetry; null means exact all-horizon equivalence",
        "rows": rows,
        "refinement_edges": [
            {
                "fine": partition_label(fine, 4),
                "coarse": partition_label(coarse, 4),
            }
            for fine, coarse in edges
        ],
        "refinement_monotonicity_violations": violations,
        "detection_depth_summary": summaries,
    }


def main() -> None:
    print(json.dumps(stage4_frontier(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
