"""Exact all-horizon equivalence tools for coarse-grained stationary Markov chains.

A deterministic observation of a finite Markov chain is represented as a finite
linear/weighted-automaton process.  Observed all-horizon time reversibility is
then equivalence between the observed forward chain and the observation of the
stationary time-reversed micro chain.

The equivalence test closes an exact rational reachable row space instead of
extending a brute-force trajectory horizon.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

from .coarse_grain import canonical_partition, observation_map
from .markov import FractionMatrix, stationary_distribution, validate_transition_matrix

RowVector = tuple[Fraction, ...]
Word = tuple[int, ...]


@dataclass(frozen=True)
class EquivalenceResult:
    """Exact result of comparing an observed process with its time reverse."""

    equivalent: bool
    detection_horizon: int | None
    witness_word: Word | None
    forward_probability: Fraction | None
    reverse_probability: Fraction | None
    reachable_dimension: int
    expanded_basis_vectors: int


def time_reversed_transition(
    matrix: Sequence[Sequence[int | float | Fraction]],
) -> FractionMatrix:
    """Return the exact stationary time-reversed transition matrix.

    For stationary distribution ``pi``, the reversed chain is

    ``P_rev[i,j] = pi[j] * P[j,i] / pi[i]``.

    Stage 4 benchmarks are irreducible and have strictly positive stationary
    mass.  Zero-mass stationary states are rejected rather than silently
    choosing an arbitrary reversal on unreachable states.
    """

    transition = validate_transition_matrix(matrix)
    pi = stationary_distribution(transition)
    if any(value <= 0 for value in pi):
        raise ValueError("time reversal requires strictly positive stationary mass")
    n_states = len(transition)
    reversed_matrix = tuple(
        tuple(pi[j] * transition[j][i] / pi[i] for j in range(n_states))
        for i in range(n_states)
    )
    return validate_transition_matrix(reversed_matrix)


def _row_times_matrix(vector: RowVector, matrix: FractionMatrix) -> RowVector:
    return tuple(
        sum((vector[i] * matrix[i][j] for i in range(len(vector))), Fraction(0))
        for j in range(len(matrix))
    )


def _row_times_symbol_transition(
    vector: RowVector,
    matrix: FractionMatrix,
    mapping: tuple[int, ...],
    symbol: int,
) -> RowVector:
    filtered = tuple(
        value if mapping[state] == symbol else Fraction(0)
        for state, value in enumerate(vector)
    )
    return _row_times_matrix(filtered, matrix)


def observed_word_probability(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
    word: Sequence[int],
) -> Fraction:
    """Return an exact observed word probability without path enumeration."""

    transition = validate_transition_matrix(matrix)
    n_states = len(transition)
    canonical = canonical_partition(partition, n_states)
    mapping = observation_map(canonical, n_states)
    symbols = tuple(int(symbol) for symbol in word)
    if not symbols:
        return Fraction(1)
    if any(symbol < 0 or symbol >= len(canonical) for symbol in symbols):
        raise ValueError("word contains an observation symbol outside the partition alphabet")

    vector: RowVector = stationary_distribution(transition)
    for symbol in symbols:
        vector = _row_times_symbol_transition(vector, transition, mapping, symbol)
    # The symbol operator is D_y P.  Since P 1 = 1, the final row sum equals
    # pi D_y0 P ... D_yk 1, the stationary observed word probability.
    return sum(vector, Fraction(0))


def _row_rank(vectors: Sequence[RowVector]) -> int:
    """Exact rational row rank for the tiny Stage 4 reachable spaces."""

    rows = [list(vector) for vector in vectors if any(value != 0 for value in vector)]
    if not rows:
        return 0
    n_rows = len(rows)
    n_cols = len(rows[0])
    if any(len(row) != n_cols for row in rows):
        raise ValueError("rank input vectors must have equal length")

    rank = 0
    for col in range(n_cols):
        pivot = next((row for row in range(rank, n_rows) if rows[row][col] != 0), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][col]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for row in range(n_rows):
            if row == rank:
                continue
            factor = rows[row][col]
            if factor == 0:
                continue
            rows[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(rows[row], rows[rank], strict=True)
            ]
        rank += 1
        if rank == n_rows:
            break
    return rank


def _combined_symbol_step(
    vector: RowVector,
    forward: FractionMatrix,
    reverse: FractionMatrix,
    mapping: tuple[int, ...],
    symbol: int,
) -> RowVector:
    n_states = len(forward)
    forward_part = _row_times_symbol_transition(vector[:n_states], forward, mapping, symbol)
    reverse_part = _row_times_symbol_transition(vector[n_states:], reverse, mapping, symbol)
    return forward_part + reverse_part


def observed_time_reversal_equivalence(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
) -> EquivalenceResult:
    """Decide exact all-horizon observed time reversibility.

    The forward and reversed observed processes are encoded in a direct-sum
    linear representation of dimension ``2*n``.  Starting from
    ``[pi, -pi]``, every observation word produces a reachable row vector whose
    sum is exactly ``Pr_forward(word) - Pr_reverse(word)``.

    Breadth-first closure adds only linearly independent reachable rows.  The
    reachable space therefore stabilizes after at most ``2*n`` basis vectors.
    If the output functional (row sum) vanishes on that closed space, every
    finite word has equal forward/reverse probability.  Otherwise the first
    mismatch encountered is a shortest word witness.
    """

    forward = validate_transition_matrix(matrix)
    n_states = len(forward)
    canonical = canonical_partition(partition, n_states)
    mapping = observation_map(canonical, n_states)
    reverse = time_reversed_transition(forward)
    pi = stationary_distribution(forward)

    initial: RowVector = tuple(pi) + tuple(-value for value in pi)
    basis: list[RowVector] = [initial]
    queue: deque[tuple[RowVector, Word]] = deque([(initial, ())])
    expanded = 0

    while queue:
        vector, prefix = queue.popleft()
        expanded += 1
        for symbol in range(len(canonical)):
            candidate = _combined_symbol_step(vector, forward, reverse, mapping, symbol)
            word = prefix + (symbol,)
            difference = sum(candidate, Fraction(0))
            if difference != 0:
                forward_probability = observed_word_probability(forward, canonical, word)
                reverse_probability = observed_word_probability(reverse, canonical, word)
                if forward_probability - reverse_probability != difference:
                    raise AssertionError("linear representation and direct word probability disagree")
                horizon = len(word) - 1
                if horizon < 1:
                    raise AssertionError("stationary observation cannot differ at the one-symbol marginal")
                return EquivalenceResult(
                    equivalent=False,
                    detection_horizon=horizon,
                    witness_word=word,
                    forward_probability=forward_probability,
                    reverse_probability=reverse_probability,
                    reachable_dimension=len(basis),
                    expanded_basis_vectors=expanded,
                )

            if _row_rank((*basis, candidate)) > len(basis):
                basis.append(candidate)
                if len(basis) > 2 * n_states:
                    raise AssertionError("reachable difference space exceeded its ambient dimension")
                queue.append((candidate, word))

    return EquivalenceResult(
        equivalent=True,
        detection_horizon=None,
        witness_word=None,
        forward_probability=None,
        reverse_probability=None,
        reachable_dimension=len(basis),
        expanded_basis_vectors=expanded,
    )
