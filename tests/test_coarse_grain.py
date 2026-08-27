from fractions import Fraction

import pytest

from r_arrow.benchmarks import biased_four_cycle
from r_arrow.coarse_grain import (
    canonical_partition,
    declared_partitions,
    is_strongly_lumpable,
    observed_arrow_strength,
    observed_path_distribution,
    partition_label,
    set_partitions,
)
from r_arrow.trajectories import path_distribution


def test_four_state_partition_counts_are_complete() -> None:
    partitions = set_partitions(4)
    declared = declared_partitions(4)
    assert len(partitions) == 15
    assert len(set(partitions)) == 15
    assert len(declared) == 14
    assert all(len(partition) >= 2 for partition in declared)


def test_partition_validation_rejects_missing_or_duplicate_states() -> None:
    with pytest.raises(ValueError):
        canonical_partition(((0, 1), (1, 2, 3)), 4)
    with pytest.raises(ValueError):
        canonical_partition(((0, 1), (2,)), 4)


def test_identity_observation_reproduces_exact_micro_path_law() -> None:
    matrix = biased_four_cycle()
    identity = ((0,), (1,), (2,), (3,))
    for horizon in range(1, 5):
        assert observed_path_distribution(matrix, horizon, identity) == path_distribution(matrix, horizon)


def test_observed_path_laws_normalize_exactly() -> None:
    matrix = biased_four_cycle()
    for partition in declared_partitions(4):
        for horizon in range(1, 5):
            observed = observed_path_distribution(matrix, horizon, partition)
            assert sum(observed.values(), Fraction(0)) == 1


def test_compact_partition_labels_are_stable() -> None:
    assert partition_label(((0, 1), (2,), (3,)), 4) == "01|2|3"
    assert partition_label(((0, 2), (1,), (3,)), 4) == "02|1|3"
    assert partition_label(((0, 2), (1, 3)), 4) == "02|13"


def test_one_block_sanity_control_has_zero_arrow() -> None:
    matrix = biased_four_cycle()
    one_block = ((0, 1, 2, 3),)
    for horizon in range(1, 5):
        assert observed_arrow_strength(matrix, horizon, one_block) == pytest.approx(0.0, abs=1e-15)


def test_strong_lumpability_diagnostic_is_exact() -> None:
    matrix = biased_four_cycle()
    assert is_strongly_lumpable(matrix, ((0,), (1,), (2,), (3,)))
    assert is_strongly_lumpable(matrix, ((0, 2), (1, 3)))
    assert not is_strongly_lumpable(matrix, ((0, 1), (2,), (3,)))
