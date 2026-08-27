"""Executable Stage 2 coarse-graining survival census."""

from __future__ import annotations

import json
from typing import Any

from .benchmarks import biased_four_cycle
from .coarse_grain import (
    Partition,
    declared_partitions,
    is_strongly_lumpable,
    observed_arrow_strength,
    partition_label,
    robustness_ratio,
)
from .irreversibility import arrow_strength

HORIZONS = (1, 2, 3, 4)
ZERO_TOL = 1e-12


def _classify_ratio(ratio: float) -> str:
    if abs(ratio) <= ZERO_TOL:
        return "undetected_at_L"
    if abs(ratio - 1.0) <= ZERO_TOL:
        return "preserved_at_L"
    if 0.0 < ratio < 1.0:
        return "retained_at_L"
    raise AssertionError(f"robustness ratio outside expected bounds: {ratio}")


def _merged_pair_geometry(partition: Partition) -> str | None:
    if len(partition) != 3:
        return None
    merged = next((block for block in partition if len(block) == 2), None)
    if merged is None:
        return None
    a, b = merged
    separation = (a - b) % 4
    return "adjacent_pair" if separation in {1, 3} else "opposite_pair"


def _summary_classification(arrows: dict[int, float], label: str) -> str:
    detected = [horizon for horizon, value in arrows.items() if value > ZERO_TOL]
    if label == "0|1|2|3":
        return "full_reference"
    if not detected:
        return "undetected_through_L4"
    if 1 not in detected:
        return "memory_revealed_arrow"
    return "retained_through_L4"


def _structural_note(partition: Partition, classification: str) -> str:
    label = partition_label(partition, 4)
    if label == "0|1|2|3":
        return "full-state identity reference"

    geometry = _merged_pair_geometry(partition)
    if geometry == "adjacent_pair":
        return "three-state observation formed by merging one adjacent pair on the cycle"
    if geometry == "opposite_pair":
        return "three-state observation formed by merging one opposite pair on the cycle"
    if len(partition) == 2:
        if classification == "undetected_through_L4":
            return "two-macrostate observation; no time-reversal asymmetry detected through L=4"
        return "two-macrostate observation"
    return "deterministic state partition"


def stage2_census() -> dict[str, Any]:
    """Return the complete frozen 14-observation Stage 2 census."""
    matrix = biased_four_cycle()
    reference = {horizon: arrow_strength(matrix, horizon) for horizon in HORIZONS}

    rows: list[dict[str, Any]] = []
    for partition in declared_partitions(4):
        label = partition_label(partition, 4)
        arrows = {
            horizon: observed_arrow_strength(matrix, horizon, partition)
            for horizon in HORIZONS
        }
        ratios = {
            horizon: robustness_ratio(arrows[horizon], reference[horizon])
            for horizon in HORIZONS
        }
        classifications = {
            horizon: _classify_ratio(ratios[horizon])
            for horizon in HORIZONS
        }
        summary_classification = _summary_classification(arrows, label)
        detected = [horizon for horizon in HORIZONS if arrows[horizon] > ZERO_TOL]

        rows.append(
            {
                "partition": [list(block) for block in partition],
                "label": label,
                "macro_states": len(partition),
                "arrow": {str(horizon): arrows[horizon] for horizon in HORIZONS},
                "r": {str(horizon): ratios[horizon] for horizon in HORIZONS},
                "classification_at_L": {
                    str(horizon): classifications[horizon] for horizon in HORIZONS
                },
                "summary_classification": summary_classification,
                "L_star": min(detected) if detected else None,
                "strongly_lumpable": is_strongly_lumpable(matrix, partition),
                "structural_note": _structural_note(partition, summary_classification),
            }
        )

    return {
        "stage": 2,
        "benchmark": {
            "states": 4,
            "clockwise": "1/2",
            "counterclockwise": "1/4",
            "self_loop": "1/4",
        },
        "horizons": list(HORIZONS),
        "observation_count": len(rows),
        "reference_arrow": {str(horizon): reference[horizon] for horizon in HORIZONS},
        "rows": rows,
    }


def main() -> None:
    print(json.dumps(stage2_census(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
