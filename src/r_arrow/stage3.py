"""Executable Stage 3 structural-criteria summary."""

from __future__ import annotations

import json
from fractions import Fraction
from typing import Any

from .benchmarks import biased_four_cycle, higher_order_hidden_arrow_four_state
from .coarse_grain import (
    Partition,
    declared_partitions,
    is_strongly_lumpable,
    observed_arrow_strength,
    observed_path_distribution,
    partition_label,
)
from .irreversibility import arrow_strength
from .markov import stationary_distribution
from .structural import (
    first_asymmetric_horizon,
    macro_flux_is_symmetric,
    one_step_arrow_visible_by_flux,
    reversal_asymmetry_witnesses,
    stationary_macro_flux,
)

HORIZONS = (1, 2, 3, 4)
HIDDEN_ARROW_PARTITION: Partition = ((0, 1), (2, 3))
ZERO_TOL = 1e-12


def _fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _flux_json(flux: tuple[tuple[Fraction, ...], ...]) -> list[list[str]]:
    return [[_fraction_text(value) for value in row] for row in flux]


def _stage2_one_step_regression() -> dict[str, Any]:
    matrix = biased_four_cycle()
    rows: list[dict[str, Any]] = []
    mismatches: list[str] = []

    for partition in declared_partitions(4):
        label = partition_label(partition, 4)
        by_flux = one_step_arrow_visible_by_flux(matrix, partition)
        arrow = observed_arrow_strength(matrix, 1, partition)
        by_kl = arrow > ZERO_TOL
        if by_flux != by_kl:
            mismatches.append(label)
        rows.append(
            {
                "label": label,
                "macro_states": len(partition),
                "flux_symmetric": not by_flux,
                "A_1": arrow,
                "visible_by_flux": by_flux,
                "visible_by_path_kl": by_kl,
            }
        )

    return {
        "observation_count": len(rows),
        "mismatches": mismatches,
        "rows": rows,
    }


def stage3_summary() -> dict[str, Any]:
    """Return the frozen Stage 3A/3B structural summary."""

    witness = higher_order_hidden_arrow_four_state()
    pi = stationary_distribution(witness)
    macro_flux = stationary_macro_flux(witness, HIDDEN_ARROW_PARTITION)
    observed_arrows = {
        horizon: observed_arrow_strength(witness, horizon, HIDDEN_ARROW_PARTITION)
        for horizon in HORIZONS
    }
    micro_arrows = {horizon: arrow_strength(witness, horizon) for horizon in HORIZONS}
    first = first_asymmetric_horizon(witness, HIDDEN_ARROW_PARTITION, HORIZONS)

    observed_l3 = observed_path_distribution(witness, 3, HIDDEN_ARROW_PARTITION)
    witnesses = reversal_asymmetry_witnesses(observed_l3)

    return {
        "stage": 3,
        "claims": {
            "stage3a": "A_1(g)=0 iff the stationary macro-flux matrix is symmetric",
            "stage3b_binary_floor": "every stationary binary process is reversal-symmetric through L=2",
            "stage3b_witness": "one-step symmetry does not imply all-horizon trajectory symmetry",
        },
        "horizons": list(HORIZONS),
        "stage2_one_step_regression": _stage2_one_step_regression(),
        "higher_order_witness": {
            "states": 4,
            "partition": partition_label(HIDDEN_ARROW_PARTITION, 4),
            "stationary_distribution": [_fraction_text(value) for value in pi],
            "strongly_lumpable": is_strongly_lumpable(witness, HIDDEN_ARROW_PARTITION),
            "macro_flux": _flux_json(macro_flux),
            "macro_flux_symmetric": macro_flux_is_symmetric(macro_flux),
            "micro_arrow": {str(h): micro_arrows[h] for h in HORIZONS},
            "observed_arrow": {str(h): observed_arrows[h] for h in HORIZONS},
            "first_asymmetric_horizon": first,
            "L3_exact_witnesses": [
                {
                    "path": list(path),
                    "probability": _fraction_text(probability),
                    "reverse": list(reverse),
                    "reverse_probability": _fraction_text(reverse_probability),
                }
                for path, probability, reverse, reverse_probability in witnesses
            ],
        },
    }


def main() -> None:
    print(json.dumps(stage3_summary(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
