"""Exact structural criteria for coarse-grained arrow visibility.

Stage 3A characterizes one-step visibility by stationary macro-flux symmetry.
Stage 3B uses exact path reversal symmetry to detect higher-order arrows without
re-Markovizing the observed process.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Mapping, Sequence

from .coarse_grain import Partition, canonical_partition, observed_path_distribution
from .markov import FractionMatrix, stationary_distribution, validate_transition_matrix
from .trajectories import Path, PathDistribution, reverse_path

MacroFluxMatrix = tuple[tuple[Fraction, ...], ...]


def stationary_macro_flux(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
) -> MacroFluxMatrix:
    """Return exact stationary one-step fluxes between observed macrostates.

    ``F[a][b]`` equals ``Pr(Y_0=a, Y_1=b)`` for the deterministic observation
    defined by ``partition``.
    """

    transition = validate_transition_matrix(matrix)
    n_states = len(transition)
    canonical: Partition = canonical_partition(partition, n_states)
    pi = stationary_distribution(transition)

    return tuple(
        tuple(
            sum(
                (
                    pi[source] * transition[source][target]
                    for source in source_block
                    for target in target_block
                ),
                Fraction(0),
            )
            for target_block in canonical
        )
        for source_block in canonical
    )


def macro_flux_is_symmetric(flux: Sequence[Sequence[Fraction]]) -> bool:
    """Return True iff the exact macro-flux matrix equals its transpose."""

    rows = tuple(tuple(value for value in row) for row in flux)
    if not rows:
        raise ValueError("macro-flux matrix must be non-empty")
    n = len(rows)
    if any(len(row) != n for row in rows):
        raise ValueError("macro-flux matrix must be square")
    return all(rows[i][j] == rows[j][i] for i in range(n) for j in range(n))


def one_step_arrow_visible_by_flux(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
) -> bool:
    """Exact Stage 3A criterion: one-step arrow iff macro flux is asymmetric."""

    return not macro_flux_is_symmetric(stationary_macro_flux(matrix, partition))


def path_distribution_is_reversal_symmetric(
    distribution: Mapping[Path, Fraction],
) -> bool:
    """Return True iff every path has exactly the same probability as its reverse."""

    return all(
        probability == distribution.get(reverse_path(path), Fraction(0))
        for path, probability in distribution.items()
    )


def observed_paths_are_reversal_symmetric(
    matrix: Sequence[Sequence[int | float | Fraction]],
    horizon: int,
    partition: Sequence[Sequence[int]],
) -> bool:
    """Check exact observed path-reversal symmetry at one declared horizon."""

    observed = observed_path_distribution(matrix, horizon, partition)
    return path_distribution_is_reversal_symmetric(observed)


def first_asymmetric_horizon(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
    horizons: Iterable[int],
) -> int | None:
    """Return the first declared horizon with exact observed path asymmetry."""

    checked = tuple(int(horizon) for horizon in horizons)
    if any(horizon < 0 for horizon in checked):
        raise ValueError("horizons must be non-negative")
    for horizon in checked:
        if not observed_paths_are_reversal_symmetric(matrix, horizon, partition):
            return horizon
    return None


def reversal_asymmetry_witnesses(distribution: PathDistribution) -> tuple[tuple[Path, Fraction, Path, Fraction], ...]:
    """Return one representative from each exact path/reverse probability mismatch."""

    witnesses: list[tuple[Path, Fraction, Path, Fraction]] = []
    seen: set[Path] = set()
    for path in sorted(distribution):
        if path in seen:
            continue
        reverse = reverse_path(path)
        reverse_probability = distribution.get(reverse, Fraction(0))
        probability = distribution[path]
        seen.add(path)
        seen.add(reverse)
        if probability != reverse_probability:
            witnesses.append((path, probability, reverse, reverse_probability))
    return tuple(witnesses)
