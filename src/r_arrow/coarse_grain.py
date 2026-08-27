"""Exact deterministic state coarse-graining for r-arrow Stage 2.

The primary observed process is defined by summing compatible microtrajectories.
No first-order Markov approximation is introduced here.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from typing import Sequence

from .irreversibility import kl_divergence, reversed_distribution
from .markov import validate_transition_matrix
from .trajectories import PathDistribution, path_distribution

Partition = tuple[tuple[int, ...], ...]


def canonical_partition(
    partition: Sequence[Sequence[int]],
    n_states: int,
) -> Partition:
    """Validate and canonicalize a set partition of ``range(n_states)``."""
    if n_states <= 0:
        raise ValueError("n_states must be positive")
    if not partition:
        raise ValueError("partition must contain at least one block")

    blocks = [tuple(sorted(int(state) for state in block)) for block in partition]
    if any(len(block) == 0 for block in blocks):
        raise ValueError("partition blocks must be non-empty")

    flat = [state for block in blocks for state in block]
    if len(flat) != len(set(flat)):
        raise ValueError("partition contains duplicate states")
    if set(flat) != set(range(n_states)):
        raise ValueError("partition must cover every microstate exactly once")

    return tuple(sorted(blocks, key=lambda block: block[0]))


def set_partitions(n_states: int) -> tuple[Partition, ...]:
    """Enumerate every set partition of ``range(n_states)`` exactly once."""
    if n_states <= 0:
        raise ValueError("n_states must be positive")

    partitions: list[Partition] = [((0,),)]
    for state in range(1, n_states):
        next_partitions: list[Partition] = []
        for partition in partitions:
            for block_index in range(len(partition)):
                blocks = list(partition)
                blocks[block_index] = blocks[block_index] + (state,)
                next_partitions.append(tuple(blocks))
            next_partitions.append(partition + ((state,),))
        partitions = next_partitions

    canonical = {canonical_partition(partition, n_states) for partition in partitions}
    return tuple(sorted(canonical, key=lambda p: (-len(p), p)))


def declared_partitions(n_states: int = 4) -> tuple[Partition, ...]:
    """Return the Stage 2 primary observation family: every partition with >=2 blocks."""
    return tuple(partition for partition in set_partitions(n_states) if len(partition) >= 2)


def partition_label(partition: Sequence[Sequence[int]], n_states: int) -> str:
    """Return a stable compact label such as ``01|2|3``."""
    canonical = canonical_partition(partition, n_states)
    return "|".join("".join(str(state) for state in block) for block in canonical)


def observation_map(partition: Sequence[Sequence[int]], n_states: int) -> tuple[int, ...]:
    """Map each microstate to its canonical macrostate index."""
    canonical = canonical_partition(partition, n_states)
    mapping = [-1] * n_states
    for macrostate, block in enumerate(canonical):
        for microstate in block:
            mapping[microstate] = macrostate
    return tuple(mapping)


def observed_path_distribution(
    matrix: Sequence[Sequence[int | float | Fraction]],
    horizon: int,
    partition: Sequence[Sequence[int]],
) -> PathDistribution:
    """Compute the exact coarse-grained path law by summing compatible microtrajectories."""
    transition = validate_transition_matrix(matrix)
    n_states = len(transition)
    mapping = observation_map(partition, n_states)
    micro_distribution = path_distribution(transition, horizon)

    observed: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for micro_path, probability in micro_distribution.items():
        macro_path = tuple(mapping[state] for state in micro_path)
        observed[macro_path] += probability

    result = dict(observed)
    if sum(result.values(), Fraction(0)) != 1:
        raise AssertionError("observed path distribution must normalize exactly")
    return result


def observed_arrow_strength(
    matrix: Sequence[Sequence[int | float | Fraction]],
    horizon: int,
    partition: Sequence[Sequence[int]],
) -> float:
    """Compute A_L for an exact deterministic coarse-grained trajectory law."""
    observed = observed_path_distribution(matrix, horizon, partition)
    return kl_divergence(observed, reversed_distribution(observed))


def robustness_ratio(observed_arrow: float, reference_arrow: float) -> float:
    """Return r_L = A_L(observed) / A_L(identity) for an irreversible reference."""
    if reference_arrow <= 0.0:
        raise ValueError("reference arrow must be positive")
    ratio = observed_arrow / reference_arrow
    # Suppress harmless floating residuals at the exact data-processing boundaries.
    if abs(ratio) < 1e-14:
        return 0.0
    if abs(ratio - 1.0) < 1e-14:
        return 1.0
    return ratio


def is_strongly_lumpable(
    matrix: Sequence[Sequence[int | float | Fraction]],
    partition: Sequence[Sequence[int]],
) -> bool:
    """Check the exact strong-lumpability criterion for a deterministic partition."""
    transition = validate_transition_matrix(matrix)
    n_states = len(transition)
    canonical = canonical_partition(partition, n_states)

    for source_block in canonical:
        anchor = source_block[0]
        for source in source_block[1:]:
            for target_block in canonical:
                anchor_total = sum((transition[anchor][target] for target in target_block), Fraction(0))
                source_total = sum((transition[source][target] for target in target_block), Fraction(0))
                if anchor_total != source_total:
                    return False
    return True
