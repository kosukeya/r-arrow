from fractions import Fraction

from r_arrow.benchmarks import (
    biased_four_cycle,
    higher_order_hidden_arrow_four_state,
    reversible_four_cycle,
)
from r_arrow.equivalence import (
    observed_time_reversal_equivalence,
    observed_word_probability,
    time_reversed_transition,
)
from r_arrow.markov import detailed_balance_holds, stationary_distribution


def test_time_reversed_transition_preserves_stationary_distribution() -> None:
    matrix = higher_order_hidden_arrow_four_state()
    reversed_matrix = time_reversed_transition(matrix)
    assert stationary_distribution(matrix) == stationary_distribution(reversed_matrix)
    assert all(sum(row, Fraction(0)) == 1 for row in reversed_matrix)


def test_reversible_control_equals_its_time_reverse() -> None:
    matrix = reversible_four_cycle()
    assert detailed_balance_holds(matrix)
    assert time_reversed_transition(matrix) == matrix


def test_reverse_chain_word_probability_matches_reversed_forward_word() -> None:
    matrix = higher_order_hidden_arrow_four_state()
    partition = ((0, 1), (2, 3))
    reverse = time_reversed_transition(matrix)
    word = (0, 0, 1, 0)
    assert observed_word_probability(reverse, partition, word) == observed_word_probability(
        matrix, partition, tuple(reversed(word))
    )


def test_stage3_binary_witness_has_exact_L3_detection() -> None:
    matrix = higher_order_hidden_arrow_four_state()
    partition = ((0, 1), (2, 3))
    result = observed_time_reversal_equivalence(matrix, partition)
    assert not result.equivalent
    assert result.detection_horizon == 3
    assert result.witness_word == (0, 0, 1, 0)
    assert result.forward_probability == Fraction(55, 1024)
    assert result.reverse_probability == Fraction(467, 8192)
    assert result.forward_probability - result.reverse_probability == Fraction(-27, 8192)
    assert result.reachable_dimension <= 8


def test_stage2_adjacent_and_opposite_merges_get_finite_vs_infinite_certificates() -> None:
    matrix = biased_four_cycle()
    adjacent = observed_time_reversal_equivalence(matrix, ((0, 1), (2,), (3,)))
    opposite = observed_time_reversal_equivalence(matrix, ((0, 2), (1,), (3,)))
    assert adjacent.detection_horizon == 1
    assert not adjacent.equivalent
    assert opposite.equivalent
    assert opposite.detection_horizon is None


def test_one_block_observation_is_all_horizon_reversible() -> None:
    for matrix in (biased_four_cycle(), higher_order_hidden_arrow_four_state(), reversible_four_cycle()):
        result = observed_time_reversal_equivalence(matrix, ((0, 1, 2, 3),))
        assert result.equivalent
        assert result.detection_horizon is None
        assert result.reachable_dimension <= 8
