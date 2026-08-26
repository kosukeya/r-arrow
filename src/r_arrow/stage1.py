"""Executable Stage 1 benchmark summary."""

from __future__ import annotations

import json
from fractions import Fraction

from .benchmarks import biased_three_cycle, reversible_three_cycle
from .irreversibility import arrow_strength, biased_cycle_analytic_arrow
from .markov import detailed_balance_holds, probability_current, stationary_distribution

HORIZONS = (1, 2, 3, 4)


def _fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _model_summary(name: str, matrix, include_oracle: bool) -> dict:
    pi = stationary_distribution(matrix)
    current = probability_current(matrix, pi)
    rows = []
    for horizon in HORIZONS:
        measured = arrow_strength(matrix, horizon)
        expected = biased_cycle_analytic_arrow(horizon) if include_oracle else 0.0
        rows.append(
            {
                "L": horizon,
                "path_count": 3 ** (horizon + 1),
                "A_L": measured,
                "expected_A_L": expected,
                "absolute_error": abs(measured - expected),
            }
        )
    return {
        "model": name,
        "stationary_distribution": [_fraction_text(x) for x in pi],
        "detailed_balance": detailed_balance_holds(matrix, pi),
        "current_matrix": [[_fraction_text(x) for x in row] for row in current],
        "horizons": rows,
    }


def run_stage1() -> dict:
    """Return the complete frozen Stage 1 benchmark payload."""
    return {
        "stage": 1,
        "status": "benchmark_evaluated",
        "horizon_set": list(HORIZONS),
        "reversible": _model_summary("reversible_control", reversible_three_cycle(), False),
        "irreversible": _model_summary("biased_three_cycle", biased_three_cycle(), True),
        "guards": [
            "observable irreversibility != ontological becoming",
            "path-level time asymmetry != thermodynamic entropy production without additional physical assumptions",
            "Stage 1 calibration != new empirical discovery",
        ],
    }


def main() -> None:
    print(json.dumps(run_stage1(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
