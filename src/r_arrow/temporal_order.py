"""Exact temporal-order structure for observed trajectory irreversibility.

Stage 5 treats time-reversal asymmetry as the reversal-odd component of an
exact finite-horizon path law and decomposes selected macro-word differences
into signed microtrajectory contributions.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping, Sequence

from .coarse_grain import canonical_partition, observation_map, observed_path_distribution
from .markov import validate_transition_matrix
from .trajectories import Path, PathDistribution, path_distribution, reverse_path


@dataclass(frozen=True)
class ReversalOddPair:
    """One unordered word/reverse pair carrying a nonzero signed difference."""

    word: Path
    reverse_word: Path
    probability: Fraction
    reverse_probability: Fraction
    delta: Fraction


@dataclass(frozen=True)
class MicroReversalContribution:
    """Signed microtrajectory contribution to one observed word difference."""

    micro_path: Path
    reverse_micro_path: Path
    probability: Fraction
    reverse_probability: Fraction
    delta: Fraction


@dataclass(frozen=True)
class CancellationSummary:
    """Exact positive/negative cancellation summary for one observed word."""

    compatible_micro_paths: int
    nonzero_micro_contributions: int
    zero_micro_contributions: int
    positive_total: Fraction
    negative_total: Fraction
    net_delta: Fraction
    absolute_total: Fraction
    cancelled_mass: Fraction


def reversal_odd_distribution(distribution: Mapping[Path, Fraction]) -> PathDistribution:
    """Return O(w)=(P(w)-P(Rw))/2, omitting exact zero entries."""

    support = set(distribution)
    support.update(reverse_path(path) for path in tuple(support))
    odd: dict[Path, Fraction] = {}
    for path in sorted(support):
        value = (
            distribution.get(path, Fraction(0))
            - distribution.get(reverse_path(path), Fraction(0))
        ) / 2
        if value != 0:
            odd[path] = value
    return odd


def reversal_odd_pairs(distribution: Mapping[Path, Fraction]) -> tuple[ReversalOddPair, ...]:
    """Return one lexicographic representative from each nonzero reversal pair."""

    support = set(distribution)
    support.update(reverse_path(path) for path in tuple(support))
    pairs: list[ReversalOddPair] = []
    seen: set[Path] = set()
    for path in sorted(support):
        if path in seen:
            continue
        reverse = reverse_path(path)
        seen.add(path)
        seen.add(reverse)
        probability = distribution.get(path, Fraction(0))
        reverse_probability = distribution.get(reverse, Fraction(0))
        delta = probability - reverse_probability
        if delta != 0:
            pairs.append(
                ReversalOddPair(
                    word=path,
                    reverse_word=reverse,
                    probability=probability,
                    reverse_probability=reverse_probability,
                    delta=delta,
                )
            )
    return tuple(pairs)


def reversal_odd_mass(distribution: Mapping[Path, Fraction]) -> Fraction:
    """Return exact TV distance between a path law and its reversed law."""

    return sum((abs(pair.delta) for pair in reversal_odd_pairs(distribution)), Fraction(0))


def marginalize_last(distribution: Mapping[Path, Fraction]) -> PathDistribution:
    """Drop the final symbol of an equal-length path-valued signed measure."""

    if not distribution:
        return {}
    lengths = {len(path) for path in distribution}
    if len(lengths) != 1:
        raise ValueError("all paths must have equal length")
    length = next(iter(lengths))
    if length < 2:
        raise ValueError("cannot marginalize a one-symbol path distribution")

    result: dict[Path, Fraction] = {}
    for path, value in distribution.items():
        prefix = path[:-1]
        result[prefix] = result.get(prefix, Fraction(0)) + value
    return {path: value for path, value in result.items() if value != 0}


def observed_reversal_odd_distribution(
    matrix: Sequence[Sequence[int | float | Fraction]],
    horizon: int,
    partition: Sequence[Sequence[int]],
) -> PathDistribution:
    """Return the exact observed reversal-odd component at one horizon."""

    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    observed = observed_path_distribution(matrix, horizon, partition)
    return reversal_odd_distribution(observed)


def observed_odd_marginalization_matches(
    matrix: Sequence[Sequence[int | float | Fraction]],
    horizon: int,
    partition: Sequence[Sequence[int]],
) -> bool:
    """Check marginalize(O_L)=O_(L-1) exactly for one stationary observation."""

    if horizon < 1:
        raise ValueError("horizon must be at least one")
    current = observed_reversal_odd_distribution(matrix, horizon, partition)
    previous = observed_reversal_odd_distribution(matrix, horizon - 1, partition)
    return marginalize_last(current) == previous


def micro_reversal_contributions(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
    word: Sequence[int],
) -> tuple[MicroReversalContribution, ...]:
    """Decompose one macro word/reverse difference into exact micro contributions.

    For every micro path x observed as ``word``, the signed contribution is
    ``P_X(x)-P_X(Rx)``.  Their exact sum equals
    ``P_g(word)-P_g(reverse(word))``.
    """

    transition = validate_transition_matrix(matrix)
    n_states = len(transition)
    canonical = canonical_partition(partition, n_states)
    mapping = observation_map(canonical, n_states)
    macro_word = tuple(int(symbol) for symbol in word)
    if len(macro_word) < 2:
        raise ValueError("word must contain at least two symbols")
    if any(symbol < 0 or symbol >= len(canonical) for symbol in macro_word):
        raise ValueError("word contains a symbol outside the observation alphabet")

    micro = path_distribution(transition, len(macro_word) - 1)
    rows: list[MicroReversalContribution] = []
    for path in sorted(micro):
        if tuple(mapping[state] for state in path) != macro_word:
            continue
        reverse = reverse_path(path)
        probability = micro[path]
        reverse_probability = micro.get(reverse, Fraction(0))
        rows.append(
            MicroReversalContribution(
                micro_path=path,
                reverse_micro_path=reverse,
                probability=probability,
                reverse_probability=reverse_probability,
                delta=probability - reverse_probability,
            )
        )
    if not rows:
        raise ValueError("observed word has no compatible microtrajectory")
    return tuple(rows)


def cancellation_summary(
    contributions: Sequence[MicroReversalContribution],
) -> CancellationSummary:
    """Summarize signed cancellation among compatible microtrajectory differences."""

    rows = tuple(contributions)
    if not rows:
        raise ValueError("at least one contribution is required")
    positive = sum((row.delta for row in rows if row.delta > 0), Fraction(0))
    negative = sum((row.delta for row in rows if row.delta < 0), Fraction(0))
    net = positive + negative
    absolute = positive - negative
    cancelled = min(positive, -negative)
    nonzero = sum(row.delta != 0 for row in rows)
    return CancellationSummary(
        compatible_micro_paths=len(rows),
        nonzero_micro_contributions=nonzero,
        zero_micro_contributions=len(rows) - nonzero,
        positive_total=positive,
        negative_total=negative,
        net_delta=net,
        absolute_total=absolute,
        cancelled_mass=cancelled,
    )


def macro_word_delta(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
    word: Sequence[int],
) -> Fraction:
    """Return exact P_g(word)-P_g(reverse(word)) by observed path enumeration."""

    macro_word = tuple(int(symbol) for symbol in word)
    observed = observed_path_distribution(matrix, len(macro_word) - 1, partition)
    return observed.get(macro_word, Fraction(0)) - observed.get(reverse_path(macro_word), Fraction(0))
