"""Exact finite trajectory enumeration for r-arrow."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from typing import Iterable, Sequence

from .markov import FractionMatrix, FractionVector, stationary_distribution, validate_transition_matrix

Path = tuple[int, ...]
PathDistribution = dict[Path, Fraction]


def reverse_path(path: Sequence[int]) -> Path:
    return tuple(reversed(path))


def enumerate_paths(n_states: int, horizon: int) -> Iterable[Path]:
    """Enumerate all paths (x_0,...,x_L) for a finite state space."""
    if n_states <= 0:
        raise ValueError("n_states must be positive")
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    return product(range(n_states), repeat=horizon + 1)


def path_probability(
    path: Sequence[int],
    matrix: Sequence[Sequence[int | float | Fraction]],
    pi: Sequence[int | float | Fraction] | None = None,
) -> Fraction:
    """Compute exact stationary path probability."""
    p = validate_transition_matrix(matrix)
    if len(path) == 0:
        raise ValueError("path must contain at least one state")
    n = len(p)
    if any(state < 0 or state >= n for state in path):
        raise ValueError("path contains an out-of-range state")
    stationary = stationary_distribution(p) if pi is None else tuple(Fraction(x) for x in pi)
    if len(stationary) != n or sum(stationary, Fraction(0)) != 1:
        raise ValueError("stationary distribution has incompatible shape or normalization")

    probability = stationary[path[0]]
    for left, right in zip(path, path[1:], strict=True):
        probability *= p[left][right]
    return probability


def path_distribution(
    matrix: Sequence[Sequence[int | float | Fraction]],
    horizon: int,
    pi: Sequence[int | float | Fraction] | None = None,
) -> PathDistribution:
    """Return exact distribution over every path at the declared horizon."""
    p = validate_transition_matrix(matrix)
    stationary = stationary_distribution(p) if pi is None else tuple(Fraction(x) for x in pi)
    distribution = {
        path: path_probability(path, p, stationary)
        for path in enumerate_paths(len(p), horizon)
    }
    total = sum(distribution.values(), Fraction(0))
    if total != 1:
        raise AssertionError(f"path distribution must normalize exactly; got {total}")
    return distribution
