import math

import pytest

from r_arrow.benchmarks import biased_three_cycle, reversible_three_cycle
from r_arrow.irreversibility import arrow_strength, biased_cycle_analytic_arrow


@pytest.mark.parametrize("horizon", [1, 2, 3, 4])
def test_reversible_control_has_zero_arrow(horizon):
    assert arrow_strength(reversible_three_cycle(), horizon) == pytest.approx(0.0, abs=1e-15)


@pytest.mark.parametrize("horizon", [1, 2, 3, 4])
def test_biased_cycle_matches_analytic_oracle(horizon):
    measured = arrow_strength(biased_three_cycle(), horizon)
    expected = biased_cycle_analytic_arrow(horizon)
    assert measured > 0.0
    assert measured == pytest.approx(expected, rel=1e-13, abs=1e-15)
    assert expected == pytest.approx((horizon / 4.0) * math.log(2.0), rel=0, abs=1e-15)


def test_biased_arrow_grows_linearly_over_frozen_horizons():
    values = [arrow_strength(biased_three_cycle(), horizon) for horizon in (1, 2, 3, 4)]
    unit = values[0]
    assert values == pytest.approx([horizon * unit for horizon in (1, 2, 3, 4)], rel=1e-13)


def test_arrow_strength_is_nonnegative_for_both_frozen_models():
    for matrix in (reversible_three_cycle(), biased_three_cycle()):
        for horizon in (1, 2, 3, 4):
            assert arrow_strength(matrix, horizon) >= -1e-15
