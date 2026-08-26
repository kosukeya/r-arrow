"""Frozen Stage 1 benchmark transition matrices."""

from __future__ import annotations

from fractions import Fraction

from .markov import FractionMatrix, validate_transition_matrix


def _three_cycle(clockwise: Fraction, counterclockwise: Fraction, self_loop: Fraction) -> FractionMatrix:
    matrix = []
    n = 3
    for i in range(n):
        row = [Fraction(0) for _ in range(n)]
        row[i] = self_loop
        row[(i + 1) % n] = clockwise
        row[(i - 1) % n] = counterclockwise
        matrix.append(row)
    return validate_transition_matrix(matrix)


def biased_three_cycle() -> FractionMatrix:
    """Stage 1 irreversible benchmark: p=1/2, q=1/4, s=1/4."""
    return _three_cycle(Fraction(1, 2), Fraction(1, 4), Fraction(1, 4))


def reversible_three_cycle() -> FractionMatrix:
    """Stage 1 reversible control: p=q=3/8, s=1/4."""
    return _three_cycle(Fraction(3, 8), Fraction(3, 8), Fraction(1, 4))
