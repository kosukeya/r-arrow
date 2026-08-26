from fractions import Fraction

from r_arrow.benchmarks import biased_three_cycle
from r_arrow.trajectories import enumerate_paths, path_distribution, path_probability, reverse_path


def test_path_counts_match_three_state_exhaustive_enumeration():
    for horizon in (1, 2, 3, 4):
        assert len(list(enumerate_paths(3, horizon))) == 3 ** (horizon + 1)


def test_path_distribution_normalizes_exactly():
    for horizon in (1, 2, 3, 4):
        distribution = path_distribution(biased_three_cycle(), horizon)
        assert sum(distribution.values(), Fraction(0)) == 1


def test_frozen_example_forward_and_reverse_probabilities():
    matrix = biased_three_cycle()
    assert path_probability((0, 1, 2), matrix) == Fraction(1, 12)
    assert path_probability((2, 1, 0), matrix) == Fraction(1, 48)
    assert reverse_path((0, 1, 2)) == (2, 1, 0)
