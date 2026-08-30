"""Exact finite-dimensional memory tools for r-arrow Stage 6.

Stage 6 distinguishes raw temporal detection depth from exact linear state
complexity.  It provides:

- a recursive forward/reverse hidden-state filter;
- exact likelihood-ratio sufficiency counterexamples;
- minimal weighted-linear realization ranks for forward, reverse, joint, and
  signed reversal-contrast word series.

The linear ranks are representation dimensions, not physical memory bits.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Sequence

from .coarse_grain import canonical_partition, observation_map
from .equivalence import observed_word_probability, time_reversed_transition
from .markov import FractionMatrix, stationary_distribution, validate_transition_matrix

RowVector = tuple[Fraction, ...]
ColumnVector = tuple[Fraction, ...]
LinearMatrix = tuple[tuple[Fraction, ...], ...]
Word = tuple[int, ...]


@dataclass(frozen=True)
class ArrowFilterModel:
    """Exact forward/reverse observed-process filter model."""

    forward: FractionMatrix
    reverse: FractionMatrix
    mapping: tuple[int, ...]
    alphabet_size: int
    stationary: RowVector


@dataclass(frozen=True)
class ArrowFilterState:
    """Unnormalized recursive state for forward and reverse hypotheses."""

    forward_row: RowVector
    reverse_row: RowVector

    @property
    def forward_likelihood(self) -> Fraction:
        return sum(self.forward_row, Fraction(0))

    @property
    def reverse_likelihood(self) -> Fraction:
        return sum(self.reverse_row, Fraction(0))

    @property
    def likelihood_ratio(self) -> Fraction | None:
        denominator = self.reverse_likelihood
        if denominator == 0:
            return None
        return self.forward_likelihood / denominator

    @property
    def normalized_forward(self) -> RowVector | None:
        total = self.forward_likelihood
        if total == 0:
            return None
        return tuple(value / total for value in self.forward_row)

    @property
    def normalized_reverse(self) -> RowVector | None:
        total = self.reverse_likelihood
        if total == 0:
            return None
        return tuple(value / total for value in self.reverse_row)


@dataclass(frozen=True)
class LinearMemoryProfile:
    """Exact weighted-linear realization ranks for one observation map."""

    forward_rank: int
    reverse_rank: int
    joint_forward_reverse_rank: int
    reversal_contrast_rank: int
    joint_ambient_dimension: int


@dataclass(frozen=True)
class RatioInsufficiencyWitness:
    """Two prefixes with equal current ratio but different next-symbol updates."""

    prefix_a: Word
    prefix_b: Word
    current_ratio: Fraction
    extension_symbol: int
    updated_ratio_a: Fraction
    updated_ratio_b: Fraction


def build_arrow_filter_model(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
) -> ArrowFilterModel:
    """Build the exact forward/reverse model for a deterministic observation."""

    forward = validate_transition_matrix(matrix)
    n_states = len(forward)
    canonical = canonical_partition(partition, n_states)
    reverse = time_reversed_transition(forward)
    return ArrowFilterModel(
        forward=forward,
        reverse=reverse,
        mapping=observation_map(canonical, n_states),
        alphabet_size=len(canonical),
        stationary=stationary_distribution(forward),
    )


def initial_arrow_filter_state(model: ArrowFilterModel) -> ArrowFilterState:
    """Return the empty-prefix state; both hypothesis likelihoods equal one."""

    return ArrowFilterState(model.stationary, model.stationary)


def _row_times_symbol(
    vector: RowVector,
    matrix: FractionMatrix,
    mapping: tuple[int, ...],
    symbol: int,
) -> RowVector:
    if symbol < 0 or symbol >= max(mapping) + 1:
        raise ValueError("symbol lies outside the observation alphabet")
    filtered = tuple(
        value if mapping[state] == symbol else Fraction(0)
        for state, value in enumerate(vector)
    )
    return tuple(
        sum((filtered[i] * matrix[i][j] for i in range(len(vector))), Fraction(0))
        for j in range(len(vector))
    )


def advance_arrow_filter(
    model: ArrowFilterModel,
    state: ArrowFilterState,
    symbol: int,
) -> ArrowFilterState:
    """Update the exact internal state by one observed symbol."""

    if symbol < 0 or symbol >= model.alphabet_size:
        raise ValueError("symbol lies outside the observation alphabet")
    return ArrowFilterState(
        forward_row=_row_times_symbol(state.forward_row, model.forward, model.mapping, symbol),
        reverse_row=_row_times_symbol(state.reverse_row, model.reverse, model.mapping, symbol),
    )


def arrow_filter_state_for_word(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
    word: Sequence[int],
) -> ArrowFilterState:
    """Return the exact recursive filter state after an observed word."""

    model = build_arrow_filter_model(matrix, partition)
    state = initial_arrow_filter_state(model)
    for symbol in word:
        state = advance_arrow_filter(model, state, int(symbol))
    return state


def filter_matches_direct_word_probability(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
    word: Sequence[int],
) -> bool:
    """Check the recursive filter against direct exact word probabilities."""

    state = arrow_filter_state_for_word(matrix, partition, word)
    reverse = time_reversed_transition(matrix)
    return (
        state.forward_likelihood == observed_word_probability(matrix, partition, word)
        and state.reverse_likelihood == observed_word_probability(reverse, partition, word)
    )


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


def _rank(vectors: Sequence[Sequence[Fraction]]) -> int:
    """Exact rational row rank; zero vectors do not increase rank."""

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


def _symbol_matrix(
    transition: FractionMatrix,
    mapping: tuple[int, ...],
    symbol: int,
) -> LinearMatrix:
    """Return the row-state symbol operator D_symbol P."""

    n_states = len(transition)
    return tuple(
        tuple(
            transition[i][j] if mapping[i] == symbol else Fraction(0)
            for j in range(n_states)
        )
        for i in range(n_states)
    )


def _direct_sum(left: LinearMatrix, right: LinearMatrix) -> LinearMatrix:
    if len(left) != len(right):
        raise ValueError("direct-sum blocks must have equal size in Stage 6")
    n = len(left)
    zero = Fraction(0)
    return tuple(
        tuple(
            left[i][j] if i < n and j < n
            else right[i - n][j - n] if i >= n and j >= n
            else zero
            for j in range(2 * n)
        )
        for i in range(2 * n)
    )


def _reachable_basis(initial: RowVector, operators: Sequence[LinearMatrix]) -> tuple[RowVector, ...]:
    basis: list[RowVector] = []
    queue: list[RowVector] = []
    if any(initial):
        basis.append(initial)
        queue.append(initial)
    while queue:
        row = queue.pop(0)
        for operator in operators:
            candidate = _row_times_matrix(row, operator)
            if _rank((*basis, candidate)) > len(basis):
                basis.append(candidate)
                queue.append(candidate)
    return tuple(basis)


def _observable_basis(
    outputs: Sequence[ColumnVector],
    operators: Sequence[LinearMatrix],
) -> tuple[ColumnVector, ...]:
    basis: list[ColumnVector] = []
    queue: list[ColumnVector] = []
    for output in outputs:
        if _rank((*basis, output)) > len(basis):
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


def _minimal_pairing_rank(
    initial: RowVector,
    operators: Sequence[LinearMatrix],
    outputs: Sequence[ColumnVector],
) -> int:
    reachable = _reachable_basis(initial, operators)
    observable = _observable_basis(outputs, operators)
    pairing_rows = tuple(
        tuple(
            sum((row[k] * column[k] for k in range(len(row))), Fraction(0))
            for column in observable
        )
        for row in reachable
    )
    return _rank(pairing_rows)


def _scalar_process_rank(
    transition: FractionMatrix,
    mapping: tuple[int, ...],
    alphabet_size: int,
    stationary: RowVector,
) -> int:
    operators = tuple(_symbol_matrix(transition, mapping, symbol) for symbol in range(alphabet_size))
    ones: ColumnVector = tuple(Fraction(1) for _ in range(len(transition)))
    return _minimal_pairing_rank(stationary, operators, (ones,))


def linear_memory_profile(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
) -> LinearMemoryProfile:
    """Compute exact minimal weighted-linear ranks for arrow comparison.

    ``joint_forward_reverse_rank`` is the minimal linear realization dimension of
    the vector-valued word series ``(P_forward(w), P_reverse(w))``.

    ``reversal_contrast_rank`` is the minimal scalar realization dimension of
    ``P_forward(w) - P_reverse(w)``.  It is zero for an exactly all-horizon
    reversible observed process.
    """

    model = build_arrow_filter_model(matrix, partition)
    n = len(model.forward)
    forward_ops = tuple(
        _symbol_matrix(model.forward, model.mapping, symbol)
        for symbol in range(model.alphabet_size)
    )
    reverse_ops = tuple(
        _symbol_matrix(model.reverse, model.mapping, symbol)
        for symbol in range(model.alphabet_size)
    )
    joint_ops = tuple(
        _direct_sum(forward_op, reverse_op)
        for forward_op, reverse_op in zip(forward_ops, reverse_ops, strict=True)
    )

    forward_rank = _scalar_process_rank(
        model.forward, model.mapping, model.alphabet_size, model.stationary
    )
    reverse_rank = _scalar_process_rank(
        model.reverse, model.mapping, model.alphabet_size, model.stationary
    )

    zero = Fraction(0)
    one = Fraction(1)
    output_forward: ColumnVector = tuple(one for _ in range(n)) + tuple(zero for _ in range(n))
    output_reverse: ColumnVector = tuple(zero for _ in range(n)) + tuple(one for _ in range(n))
    output_difference: ColumnVector = tuple(one for _ in range(2 * n))

    joint_initial: RowVector = tuple(model.stationary) + tuple(model.stationary)
    difference_initial: RowVector = tuple(model.stationary) + tuple(-value for value in model.stationary)

    return LinearMemoryProfile(
        forward_rank=forward_rank,
        reverse_rank=reverse_rank,
        joint_forward_reverse_rank=_minimal_pairing_rank(
            joint_initial, joint_ops, (output_forward, output_reverse)
        ),
        reversal_contrast_rank=_minimal_pairing_rank(
            difference_initial, joint_ops, (output_difference,)
        ),
        joint_ambient_dimension=2 * n,
    )


def likelihood_ratio_insufficiency_witness(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
    max_prefix_symbols: int = 3,
) -> RatioInsufficiencyWitness | None:
    """Find a bounded exact proof that the current ratio is not recursive state.

    Two prefixes are a witness when they have the same current likelihood ratio
    but, after the same next symbol, have different updated ratios.

    Returning ``None`` means only that no witness was found within the declared
    prefix bound; it is not a general sufficiency certificate.
    """

    if max_prefix_symbols < 1:
        raise ValueError("max_prefix_symbols must be positive")
    model = build_arrow_filter_model(matrix, partition)

    records: list[tuple[Word, ArrowFilterState]] = []
    for length in range(1, max_prefix_symbols + 1):
        for word in product(range(model.alphabet_size), repeat=length):
            state = initial_arrow_filter_state(model)
            for symbol in word:
                state = advance_arrow_filter(model, state, symbol)
            if state.forward_likelihood > 0 and state.reverse_likelihood > 0:
                records.append((tuple(word), state))

    for index, (prefix_a, state_a) in enumerate(records):
        ratio = state_a.likelihood_ratio
        if ratio is None:
            continue
        for prefix_b, state_b in records[:index]:
            if state_b.likelihood_ratio != ratio:
                continue
            for symbol in range(model.alphabet_size):
                next_a = advance_arrow_filter(model, state_a, symbol)
                next_b = advance_arrow_filter(model, state_b, symbol)
                ratio_a = next_a.likelihood_ratio
                ratio_b = next_b.likelihood_ratio
                if ratio_a is None or ratio_b is None:
                    continue
                if ratio_a != ratio_b:
                    return RatioInsufficiencyWitness(
                        prefix_a=prefix_a,
                        prefix_b=prefix_b,
                        current_ratio=ratio,
                        extension_symbol=symbol,
                        updated_ratio_a=ratio_a,
                        updated_ratio_b=ratio_b,
                    )
    return None
