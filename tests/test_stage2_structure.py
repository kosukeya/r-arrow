from fractions import Fraction

from r_arrow.benchmarks import biased_four_cycle
from r_arrow.coarse_grain import is_strongly_lumpable, observed_path_distribution


def test_adjacent_pair_merge_preserves_oriented_one_step_macro_cycle() -> None:
    matrix = biased_four_cycle()
    partition = ((0, 1), (2,), (3,))  # 01|2|3
    observed = observed_path_distribution(matrix, 1, partition)

    # Macro cycle A={0,1} -> B={2} -> C={3} -> A retains net current 1/16.
    assert observed[(0, 1)] - observed[(1, 0)] == Fraction(1, 16)
    assert observed[(1, 2)] - observed[(2, 1)] == Fraction(1, 16)
    assert observed[(2, 0)] - observed[(0, 2)] == Fraction(1, 16)
    assert not is_strongly_lumpable(matrix, partition)


def test_opposite_pair_merge_balances_one_step_macro_fluxes() -> None:
    matrix = biased_four_cycle()
    partition = ((0, 2), (1,), (3,))  # 02|1|3
    observed = observed_path_distribution(matrix, 1, partition)

    assert observed[(0, 1)] == observed[(1, 0)] == Fraction(3, 16)
    assert observed[(0, 2)] == observed[(2, 0)] == Fraction(3, 16)
    assert observed.get((1, 2), Fraction(0)) == observed.get((2, 1), Fraction(0)) == 0
    # Non-lumpability alone therefore does not imply an observable arrow.
    assert not is_strongly_lumpable(matrix, partition)
