"""Exact structural certificates for all-horizon observed arrow hiding.

Stage 7 distinguishes two certificate classes:

- an observation-preserving hidden-state permutation that conjugates the
  forward chain to its stationary time reverse;
- a similarity/intertwiner between exact minimal weighted-linear realizations
  of the observed forward and reverse word processes.

The first is a transparent sufficient mechanism.  The second is more general
and lives only at the observable representation level.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from typing import Sequence

from .coarse_grain import canonical_partition, observation_map
from .equivalence import observed_time_reversal_equivalence, time_reversed_transition
from .markov import FractionMatrix, stationary_distribution, validate_transition_matrix

RowVector = tuple[Fraction, ...]
ColumnVector = tuple[Fraction, ...]
LinearMatrix = tuple[tuple[Fraction, ...], ...]
Word = tuple[int, ...]


@dataclass(frozen=True)
class PermutationCertificate:
    permutation: tuple[int, ...]
    cycle_notation: str
    observation_preserving: bool
    stationary_preserving: bool
    reversal_conjugacy: bool


@dataclass(frozen=True)
class MinimalScalarRealization:
    rank: int
    initial: RowVector
    operators: tuple[LinearMatrix, ...]
    output: ColumnVector
    prefix_basis_words: tuple[Word, ...]


@dataclass(frozen=True)
class LinearIntertwinerCertificate:
    rank: int
    intertwiner: LinearMatrix
    prefix_basis_words: tuple[Word, ...]
    is_identity: bool


def _rank(vectors: Sequence[Sequence[Fraction]]) -> int:
    rows = [list(vector) for vector in vectors if any(value != 0 for value in vector)]
    if not rows:
        return 0
    n_rows = len(rows)
    n_cols = len(rows[0])
    if any(len(row) != n_cols for row in rows):
        raise ValueError("rank vectors must have equal dimension")

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


def _row_times_matrix(vector: RowVector, matrix: LinearMatrix) -> RowVector:
    return tuple(
        sum((vector[i] * matrix[i][j] for i in range(len(vector))), Fraction(0))
        for j in range(len(matrix))
    )


def _matrix_times_column(matrix: LinearMatrix, vector: ColumnVector) -> ColumnVector:
    return tuple(
        sum((matrix[i][j] * vector[j] for j in range(len(vector))), Fraction(0))
        for i in range(len(matrix))
    )


def _matrix_multiply(left: LinearMatrix, right: LinearMatrix) -> LinearMatrix:
    if not left or not right:
        raise ValueError("matrix multiplication requires non-empty matrices")
    if len(left[0]) != len(right):
        raise ValueError("matrix dimensions are incompatible")
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def _matrix_inverse(matrix: LinearMatrix) -> LinearMatrix:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("inverse requires a non-empty square matrix")
    augmented = [
        list(matrix[i]) + [Fraction(1 if i == j else 0) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((row for row in range(col, n) if augmented[row][col] != 0), None)
        if pivot is None:
            raise ValueError("matrix is singular")
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        pivot_value = augmented[col][col]
        augmented[col] = [value / pivot_value for value in augmented[col]]
        for row in range(n):
            if row == col:
                continue
            factor = augmented[row][col]
            if factor == 0:
                continue
            augmented[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(augmented[row], augmented[col], strict=True)
            ]
    return tuple(tuple(row[n:]) for row in augmented)


def _symbol_matrix(
    transition: FractionMatrix,
    mapping: tuple[int, ...],
    symbol: int,
) -> LinearMatrix:
    n_states = len(transition)
    return tuple(
        tuple(
            transition[i][j] if mapping[i] == symbol else Fraction(0)
            for j in range(n_states)
        )
        for i in range(n_states)
    )


def _reachable_basis_with_words(
    initial: RowVector,
    operators: Sequence[LinearMatrix],
) -> tuple[tuple[RowVector, Word], ...]:
    basis: list[tuple[RowVector, Word]] = []
    queue: list[tuple[RowVector, Word]] = []
    if any(initial):
        basis.append((initial, ()))
        queue.append((initial, ()))
    while queue:
        row, word = queue.pop(0)
        for symbol, operator in enumerate(operators):
            candidate = _row_times_matrix(row, operator)
            if _rank([item[0] for item in basis] + [candidate]) > len(basis):
                record = (candidate, word + (symbol,))
                basis.append(record)
                queue.append(record)
    return tuple(basis)


def _observable_basis(
    output: ColumnVector,
    operators: Sequence[LinearMatrix],
) -> tuple[ColumnVector, ...]:
    basis: list[ColumnVector] = []
    queue: list[ColumnVector] = []
    if any(output):
        basis.append(output)
        queue.append(output)
    while queue:
        column = queue.pop(0)
        for operator in operators:
            candidate = _matrix_times_column(operator, column)
            if _rank((*basis, candidate)) > len(basis):
                basis.append(candidate)
                queue.append(candidate)
    return tuple(basis)


def _cycle_notation(permutation: tuple[int, ...]) -> str:
    visited: set[int] = set()
    cycles: list[str] = []
    for start in range(len(permutation)):
        if start in visited:
            continue
        cycle: list[int] = []
        current = start
        while current not in visited:
            visited.add(current)
            cycle.append(current)
            current = permutation[current]
        if len(cycle) > 1:
            cycles.append("(" + " ".join(str(value) for value in cycle) + ")")
    return "identity" if not cycles else "".join(cycles)


def observation_preserving_permutation(
    partition: Sequence[Sequence[int]],
    permutation: Sequence[int],
    n_states: int,
) -> bool:
    canonical = canonical_partition(partition, n_states)
    mapping = observation_map(canonical, n_states)
    perm = tuple(int(value) for value in permutation)
    if sorted(perm) != list(range(n_states)):
        raise ValueError("permutation must contain every state exactly once")
    return all(mapping[perm[state]] == mapping[state] for state in range(n_states))


def permutation_reversal_certificates(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
) -> tuple[PermutationCertificate, ...]:
    """Enumerate exact observation-preserving reversal-conjugating permutations."""

    forward = validate_transition_matrix(matrix)
    reverse = time_reversed_transition(forward)
    stationary = stationary_distribution(forward)
    n_states = len(forward)
    canonical = canonical_partition(partition, n_states)

    certificates: list[PermutationCertificate] = []
    for perm in permutations(range(n_states)):
        observation_ok = observation_preserving_permutation(canonical, perm, n_states)
        if not observation_ok:
            continue
        stationary_ok = all(stationary[perm[state]] == stationary[state] for state in range(n_states))
        conjugacy_ok = all(
            reverse[i][j] == forward[perm[i]][perm[j]]
            for i in range(n_states)
            for j in range(n_states)
        )
        if stationary_ok and conjugacy_ok:
            certificates.append(
                PermutationCertificate(
                    permutation=tuple(perm),
                    cycle_notation=_cycle_notation(tuple(perm)),
                    observation_preserving=True,
                    stationary_preserving=True,
                    reversal_conjugacy=True,
                )
            )
    return tuple(certificates)


def minimal_scalar_realization(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
) -> MinimalScalarRealization:
    """Return an exact minimal weighted-linear realization of one observed process."""

    transition = validate_transition_matrix(matrix)
    n_states = len(transition)
    canonical = canonical_partition(partition, n_states)
    mapping = observation_map(canonical, n_states)
    stationary = stationary_distribution(transition)
    operators = tuple(
        _symbol_matrix(transition, mapping, symbol)
        for symbol in range(len(canonical))
    )
    output: ColumnVector = tuple(Fraction(1) for _ in range(n_states))

    reachable = _reachable_basis_with_words(stationary, operators)
    observable = _observable_basis(output, operators)
    full_pairing = tuple(
        tuple(
            sum((row[k] * column[k] for k in range(n_states)), Fraction(0))
            for column in observable
        )
        for row, _ in reachable
    )
    rank = _rank(full_pairing)
    if rank < 1:
        raise AssertionError("a normalized stochastic word process must have positive rank")

    selected_row_indices: list[int] = []
    selected_pairing_rows: list[tuple[Fraction, ...]] = []
    for index, pairing_row in enumerate(full_pairing):
        if _rank((*selected_pairing_rows, pairing_row)) > len(selected_pairing_rows):
            selected_row_indices.append(index)
            selected_pairing_rows.append(pairing_row)
            if len(selected_row_indices) == rank:
                break

    selected_column_indices: list[int] = []
    for column_index in range(len(observable)):
        candidate_indices = selected_column_indices + [column_index]
        candidate_matrix = tuple(
            tuple(full_pairing[row_index][j] for j in candidate_indices)
            for row_index in selected_row_indices
        )
        if _rank(candidate_matrix) > len(selected_column_indices):
            selected_column_indices.append(column_index)
            if len(selected_column_indices) == rank:
                break

    if len(selected_row_indices) != rank or len(selected_column_indices) != rank:
        raise AssertionError("failed to select a full-rank Hankel minor")

    selected_rows = tuple(reachable[index][0] for index in selected_row_indices)
    selected_words = tuple(reachable[index][1] for index in selected_row_indices)
    selected_columns = tuple(observable[index] for index in selected_column_indices)

    hankel = tuple(
        tuple(
            sum((row[k] * column[k] for k in range(n_states)), Fraction(0))
            for column in selected_columns
        )
        for row in selected_rows
    )
    hankel_inverse = _matrix_inverse(hankel)

    reduced_operators: list[LinearMatrix] = []
    for operator in operators:
        shifted = tuple(
            tuple(
                sum(
                    (
                        _row_times_matrix(row, operator)[k] * column[k]
                        for k in range(n_states)
                    ),
                    Fraction(0),
                )
                for column in selected_columns
            )
            for row in selected_rows
        )
        reduced_operators.append(_matrix_multiply(hankel_inverse, shifted))

    initial = tuple(
        sum((stationary[k] * column[k] for k in range(n_states)), Fraction(0))
        for column in selected_columns
    )
    row_output = tuple(
        sum((row[k] * output[k] for k in range(n_states)), Fraction(0))
        for row in selected_rows
    )
    reduced_output = tuple(
        sum((hankel_inverse[i][j] * row_output[j] for j in range(rank)), Fraction(0))
        for i in range(rank)
    )

    return MinimalScalarRealization(
        rank=rank,
        initial=initial,
        operators=tuple(reduced_operators),
        output=reduced_output,
        prefix_basis_words=selected_words,
    )


def reduced_state_for_word(
    realization: MinimalScalarRealization,
    word: Sequence[int],
) -> RowVector:
    state = realization.initial
    for symbol in word:
        state = _row_times_matrix(state, realization.operators[int(symbol)])
    return state


def linear_intertwiner_certificate(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
) -> LinearIntertwinerCertificate | None:
    """Construct an exact minimal linear similarity certificate when word series agree."""

    equivalence = observed_time_reversal_equivalence(matrix, partition)
    if not equivalence.equivalent:
        return None

    forward = validate_transition_matrix(matrix)
    reverse = time_reversed_transition(forward)
    forward_realization = minimal_scalar_realization(forward, partition)
    reverse_realization = minimal_scalar_realization(reverse, partition)
    if forward_realization.rank != reverse_realization.rank:
        raise AssertionError("equivalent minimal scalar series must have equal rank")

    rank = forward_realization.rank
    words = forward_realization.prefix_basis_words
    forward_basis = tuple(reduced_state_for_word(forward_realization, word) for word in words)
    reverse_basis = tuple(reduced_state_for_word(reverse_realization, word) for word in words)
    if _rank(forward_basis) != rank or _rank(reverse_basis) != rank:
        raise AssertionError("shared prefix basis must span both equivalent minimal realizations")

    intertwiner = _matrix_multiply(_matrix_inverse(forward_basis), reverse_basis)
    if _rank(intertwiner) != rank:
        raise AssertionError("minimal-realization intertwiner must be invertible")

    if _row_times_matrix(forward_realization.initial, intertwiner) != reverse_realization.initial:
        raise AssertionError("intertwiner does not map initial state")
    for forward_operator, reverse_operator in zip(
        forward_realization.operators,
        reverse_realization.operators,
        strict=True,
    ):
        if _matrix_multiply(forward_operator, intertwiner) != _matrix_multiply(
            intertwiner, reverse_operator
        ):
            raise AssertionError("intertwiner does not conjugate symbol operators")
    if _matrix_times_column(intertwiner, reverse_realization.output) != forward_realization.output:
        raise AssertionError("intertwiner does not map output functional")

    identity = tuple(
        tuple(Fraction(1 if i == j else 0) for j in range(rank))
        for i in range(rank)
    )
    return LinearIntertwinerCertificate(
        rank=rank,
        intertwiner=intertwiner,
        prefix_basis_words=words,
        is_identity=intertwiner == identity,
    )
