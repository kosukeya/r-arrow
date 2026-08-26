from fractions import Fraction

import pytest

from r_arrow.benchmarks import biased_three_cycle, reversible_three_cycle
from r_arrow.markov import (
    detailed_balance_holds,
    probability_current,
    stationary_distribution,
    validate_transition_matrix,
)


def test_transition_matrix_validation_rejects_bad_rows():
    with pytest.raises(ValueError):
        validate_transition_matrix([[Fraction(1, 2), Fraction(1, 2)], [Fraction(1, 3), Fraction(1, 3)]])


def test_stage1_stationary_distributions_are_uniform():
    expected = (Fraction(1, 3),) * 3
    assert stationary_distribution(biased_three_cycle()) == expected
    assert stationary_distribution(reversible_three_cycle()) == expected


def test_biased_cycle_has_exact_clockwise_current():
    current = probability_current(biased_three_cycle())
    assert current[0][1] == Fraction(1, 12)
    assert current[1][2] == Fraction(1, 12)
    assert current[2][0] == Fraction(1, 12)
    assert current[1][0] == Fraction(-1, 12)
    assert current[2][1] == Fraction(-1, 12)
    assert current[0][2] == Fraction(-1, 12)
    assert not detailed_balance_holds(biased_three_cycle())


def test_reversible_control_has_zero_current_and_detailed_balance():
    current = probability_current(reversible_three_cycle())
    assert all(value == 0 for row in current for value in row)
    assert detailed_balance_holds(reversible_three_cycle())
