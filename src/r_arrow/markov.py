"""Exact finite-state Markov-chain diagnostics for r-arrow Stage 1."""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Sequence

FractionMatrix = tuple[tuple[Fraction, ...], ...]
FractionVector = tuple[Fraction, ...]


def _as_fraction(value: int | float | Fraction) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, float):
        return Fraction(str(value))
    return Fraction(value)


def validate_transition_matrix(
    matrix: Sequence[Sequence[int | float | Fraction]],
) -> FractionMatrix:
    """Validate and normalize a square row-stochastic matrix exactly."""
    rows = tuple(tuple(_as_fraction(x) for x in row) for row in matrix)
    if not rows:
        raise ValueError("transition matrix must be non-empty")
    n = len(rows)
    if any(len(row) != n for row in rows):
        raise ValueError("transition matrix must be square")
    for row in rows:
        if any(x < 0 for x in row):
            raise ValueError("transition probabilities must be non-negative")
        if sum(row, Fraction(0)) != 1:
            raise ValueError("each transition-matrix row must sum to one")
    return rows


def _solve_linear_system(a: list[list[Fraction]], b: list[Fraction]) -> FractionVector:
    """Solve a nonsingular linear system with Fraction Gaussian elimination."""
    n = len(a)
    augmented = [row[:] + [rhs] for row, rhs in zip(a, b, strict=True)]

    for col in range(n):
        pivot = next((r for r in range(col, n) if augmented[r][col] != 0), None)
        if pivot is None:
            raise ValueError("linear system is singular")
        if pivot != col:
            augmented[col], augmented[pivot] = augmented[pivot], augmented[col]

        pivot_value = augmented[col][col]
        augmented[col] = [x / pivot_value for x in augmented[col]]

        for row in range(n):
            if row == col:
                continue
            factor = augmented[row][col]
            if factor == 0:
                continue
            augmented[row] = [
                x - factor * y
                for x, y in zip(augmented[row], augmented[col], strict=True)
            ]

    return tuple(augmented[i][-1] for i in range(n))


def stationary_distribution(matrix: Sequence[Sequence[int | float | Fraction]]) -> FractionVector:
    """Return the unique stationary distribution for the finite benchmark chain.

    The Stage 1 benchmark is irreducible/aperiodic, so the stationary solution is
    unique. The solver uses exact rational arithmetic.
    """
    p = validate_transition_matrix(matrix)
    n = len(p)

    # Solve (P^T - I) pi = 0, replacing the final equation by sum(pi)=1.
    a: list[list[Fraction]] = []
    b: list[Fraction] = []
    for i in range(n - 1):
        row = [p[j][i] - (Fraction(1) if i == j else Fraction(0)) for j in range(n)]
        a.append(row)
        b.append(Fraction(0))
    a.append([Fraction(1) for _ in range(n)])
    b.append(Fraction(1))

    pi = _solve_linear_system(a, b)
    if any(x < 0 for x in pi):
        raise ValueError("stationary solution contains a negative probability")
    return pi


def probability_current(
    matrix: Sequence[Sequence[int | float | Fraction]],
    pi: Sequence[int | float | Fraction] | None = None,
) -> FractionMatrix:
    """Return antisymmetric stationary edge-current matrix J_ij."""
    p = validate_transition_matrix(matrix)
    stationary = stationary_distribution(p) if pi is None else tuple(_as_fraction(x) for x in pi)
    n = len(p)
    if len(stationary) != n or sum(stationary, Fraction(0)) != 1:
        raise ValueError("stationary distribution has incompatible shape or normalization")
    return tuple(
        tuple(stationary[i] * p[i][j] - stationary[j] * p[j][i] for j in range(n))
        for i in range(n)
    )


def detailed_balance_holds(
    matrix: Sequence[Sequence[int | float | Fraction]],
    pi: Sequence[int | float | Fraction] | None = None,
) -> bool:
    """Return True iff every stationary edge current is exactly zero."""
    current = probability_current(matrix, pi)
    return all(value == 0 for row in current for value in row)
