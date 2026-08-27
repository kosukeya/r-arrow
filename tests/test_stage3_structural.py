from fractions import Fraction

from r_arrow.benchmarks import biased_four_cycle, higher_order_hidden_arrow_four_state
from r_arrow.coarse_grain import declared_partitions, observed_arrow_strength, observed_path_distribution
from r_arrow.markov import stationary_distribution
from r_arrow.structural import (
    first_asymmetric_horizon,
    macro_flux_is_symmetric,
    observed_paths_are_reversal_symmetric,
    one_step_arrow_visible_by_flux,
    stationary_macro_flux,
)


ADJACENT = ((0, 1), (2,), (3,))
OPPOSITE = ((0, 2), (1,), (3,))
BINARY_HIDDEN = ((0, 1), (2, 3))


def test_stage2_one_step_census_is_exactly_classified_by_macro_flux_symmetry():
    matrix = biased_four_cycle()
    for partition in declared_partitions(4):
        visible_by_flux = one_step_arrow_visible_by_flux(matrix, partition)
        visible_by_kl = observed_arrow_strength(matrix, 1, partition) > 1e-12
        assert visible_by_flux == visible_by_kl


def test_stage2_adjacent_and_opposite_merges_have_different_macro_flux_structure():
    matrix = biased_four_cycle()

    adjacent = stationary_macro_flux(matrix, ADJACENT)
    opposite = stationary_macro_flux(matrix, OPPOSITE)

    assert not macro_flux_is_symmetric(adjacent)
    assert macro_flux_is_symmetric(opposite)

    # Adjacent merge retains an oriented three-cycle current of magnitude 1/16.
    assert adjacent[0][1] - adjacent[1][0] == Fraction(1, 16)
    assert adjacent[1][2] - adjacent[2][1] == Fraction(1, 16)
    assert adjacent[2][0] - adjacent[0][2] == Fraction(1, 16)

    # Opposite merge balances the observable A-B and A-C fluxes exactly.
    assert opposite[0][1] == opposite[1][0] == Fraction(3, 16)
    assert opposite[0][2] == opposite[2][0] == Fraction(3, 16)


def test_stage3_hidden_arrow_benchmark_has_uniform_stationary_distribution_and_positive_support():
    matrix = higher_order_hidden_arrow_four_state()
    assert stationary_distribution(matrix) == (Fraction(1, 4),) * 4
    assert all(value > 0 for row in matrix for value in row)


def test_stage3_hidden_arrow_has_symmetric_one_step_macro_flux():
    matrix = higher_order_hidden_arrow_four_state()
    flux = stationary_macro_flux(matrix, BINARY_HIDDEN)

    assert flux == (
        (Fraction(1, 4), Fraction(1, 4)),
        (Fraction(1, 4), Fraction(1, 4)),
    )
    assert macro_flux_is_symmetric(flux)
    assert not one_step_arrow_visible_by_flux(matrix, BINARY_HIDDEN)
    assert observed_arrow_strength(matrix, 1, BINARY_HIDDEN) == 0.0


def test_stage3_binary_hidden_arrow_first_appears_at_L3():
    matrix = higher_order_hidden_arrow_four_state()

    assert observed_paths_are_reversal_symmetric(matrix, 1, BINARY_HIDDEN)
    assert observed_paths_are_reversal_symmetric(matrix, 2, BINARY_HIDDEN)
    assert not observed_paths_are_reversal_symmetric(matrix, 3, BINARY_HIDDEN)
    assert not observed_paths_are_reversal_symmetric(matrix, 4, BINARY_HIDDEN)
    assert first_asymmetric_horizon(matrix, BINARY_HIDDEN, (1, 2, 3, 4)) == 3

    assert observed_arrow_strength(matrix, 1, BINARY_HIDDEN) == 0.0
    assert observed_arrow_strength(matrix, 2, BINARY_HIDDEN) == 0.0
    assert observed_arrow_strength(matrix, 3, BINARY_HIDDEN) > 0.0
    assert observed_arrow_strength(matrix, 4, BINARY_HIDDEN) > 0.0


def test_stage3_L3_asymmetry_has_exact_path_probability_witness():
    matrix = higher_order_hidden_arrow_four_state()
    observed = observed_path_distribution(matrix, 3, BINARY_HIDDEN)

    forward = (0, 0, 1, 0)
    reverse = tuple(reversed(forward))

    assert observed[forward] == Fraction(55, 1024)
    assert observed[reverse] == Fraction(467, 8192)
    assert observed[forward] - observed[reverse] == Fraction(-27, 8192)
