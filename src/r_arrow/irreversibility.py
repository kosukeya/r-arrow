"""Trajectory-level time-reversal asymmetry for r-arrow."""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Mapping, Sequence

from .trajectories import Path, PathDistribution, path_distribution, reverse_path


def kl_divergence(p: Mapping[Path, Fraction], q: Mapping[Path, Fraction]) -> float:
    """Compute D_KL(p || q) with the Stage 0 conventions."""
    total = 0.0
    for outcome, p_value in p.items():
        if p_value == 0:
            continue
        q_value = q.get(outcome, Fraction(0))
        if q_value == 0:
            return math.inf
        total += float(p_value) * math.log(float(p_value / q_value))
    return total


def reversed_distribution(distribution: PathDistribution) -> PathDistribution:
    """Return the probability law assigned to reversed trajectories."""
    return {path: distribution[reverse_path(path)] for path in distribution}


def arrow_strength(
    matrix: Sequence[Sequence[int | float | Fraction]],
    horizon: int,
) -> float:
    """Compute A_L = D_KL(P(path) || P(reversed path))."""
    forward = path_distribution(matrix, horizon)
    reverse = reversed_distribution(forward)
    return kl_divergence(forward, reverse)


def biased_cycle_analytic_arrow(horizon: int) -> float:
    """Frozen Stage 1 oracle A_L = (L/4) log(2)."""
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    return (horizon / 4.0) * math.log(2.0)
