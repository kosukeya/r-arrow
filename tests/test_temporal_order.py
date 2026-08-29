from fractions import Fraction

from r_arrow.benchmarks import higher_order_hidden_arrow_four_state
from r_arrow.coarse_grain import observed_path_distribution
from r_arrow.equivalence import observed_time_reversal_equivalence
from r_arrow.temporal_order import (
    cancellation_summary,
    macro_word_delta,
    micro_reversal_contributions,
    observed_odd_marginalization_matches,
    reversal_odd_distribution,
    reversal_odd_mass,
    reversal_odd_pairs,
)


MATRIX = higher_order_hidden_arrow_four_state()
ORDER_1 = ((0,), (1, 2), (3,))
ORDER_2 = ((0,), (1,), (2, 3))
ORDER_3 = ((0, 1), (2, 3))
INFINITY = ((0, 2), (1,), (3,))


def test_reversal_odd_component_is_exactly_antisymmetric():
    distribution = observed_path_distribution(MATRIX, 3, ORDER_3)
    odd = reversal_odd_distribution(distribution)
    assert odd
    for word, value in odd.items():
        assert odd[tuple(reversed(word))] == -value
    assert reversal_odd_mass(distribution) == Fraction(27, 2048)


def test_first_detection_odd_components_marginalize_to_lower_order():
    assert observed_odd_marginalization_matches(MATRIX, 2, ORDER_2)
    assert observed_odd_marginalization_matches(MATRIX, 3, ORDER_3)

    lower_order_2 = reversal_odd_pairs(observed_path_distribution(MATRIX, 1, ORDER_2))
    lower_order_3_a = reversal_odd_pairs(observed_path_distribution(MATRIX, 1, ORDER_3))
    lower_order_3_b = reversal_odd_pairs(observed_path_distribution(MATRIX, 2, ORDER_3))
    assert lower_order_2 == ()
    assert lower_order_3_a == ()
    assert lower_order_3_b == ()


def test_representative_micro_cancellation_sums_are_exact():
    cases = (
        (ORDER_1, (0, 1), Fraction(3, 64), Fraction(0), Fraction(3, 64), 2, 1),
        (ORDER_2, (0, 2, 1), Fraction(3, 256), Fraction(-3, 1024), Fraction(9, 1024), 2, 2),
        (ORDER_3, (0, 0, 1, 0), Fraction(93, 16384), Fraction(-147, 16384), Fraction(-27, 8192), 16, 8),
    )
    for partition, word, positive, negative, net, compatible, nonzero in cases:
        contributions = micro_reversal_contributions(MATRIX, partition, word)
        summary = cancellation_summary(contributions)
        assert summary.compatible_micro_paths == compatible
        assert summary.nonzero_micro_contributions == nonzero
        assert summary.positive_total == positive
        assert summary.negative_total == negative
        assert summary.net_delta == net
        assert macro_word_delta(MATRIX, partition, word) == net
        assert sum((row.delta for row in contributions), Fraction(0)) == net


def test_all_horizon_hidden_representative_has_exact_certificate():
    result = observed_time_reversal_equivalence(MATRIX, INFINITY)
    assert result.equivalent
    assert result.detection_horizon is None
    for horizon in (1, 2, 3):
        assert reversal_odd_pairs(observed_path_distribution(MATRIX, horizon, INFINITY)) == ()
