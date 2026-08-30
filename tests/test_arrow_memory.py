from fractions import Fraction

from r_arrow.arrow_memory import (
    arrow_filter_state_for_word,
    filter_matches_direct_word_probability,
    likelihood_ratio_insufficiency_witness,
    linear_memory_profile,
)
from r_arrow.benchmarks import higher_order_hidden_arrow_four_state, reversible_four_cycle


MATRIX = higher_order_hidden_arrow_four_state()


def test_recursive_filter_reproduces_stage3_order3_witness() -> None:
    partition = ((0, 1), (2, 3))
    word = (0, 0, 1, 0)
    assert filter_matches_direct_word_probability(MATRIX, partition, word)
    state = arrow_filter_state_for_word(MATRIX, partition, word)
    assert state.forward_likelihood == Fraction(55, 1024)
    assert state.reverse_likelihood == Fraction(467, 8192)
    assert state.likelihood_ratio == Fraction(440, 467)


def test_current_likelihood_ratio_is_not_recursive_state_order1() -> None:
    witness = likelihood_ratio_insufficiency_witness(
        MATRIX, ((0,), (1, 2), (3,)), max_prefix_symbols=3
    )
    assert witness is not None
    assert witness.prefix_a == (1,)
    assert witness.prefix_b == (0,)
    assert witness.current_ratio == 1
    assert witness.extension_symbol == 0
    assert witness.updated_ratio_a == Fraction(8, 11)
    assert witness.updated_ratio_b == 1


def test_current_likelihood_ratio_is_not_recursive_state_order2() -> None:
    witness = likelihood_ratio_insufficiency_witness(
        MATRIX, ((0,), (1,), (2, 3)), max_prefix_symbols=3
    )
    assert witness is not None
    assert witness.prefix_a == (0, 2)
    assert witness.prefix_b == (0,)
    assert witness.current_ratio == 1
    assert witness.extension_symbol == 1
    assert witness.updated_ratio_a == Fraction(32, 23)
    assert witness.updated_ratio_b == 1


def test_current_likelihood_ratio_is_not_recursive_state_order3() -> None:
    witness = likelihood_ratio_insufficiency_witness(
        MATRIX, ((0, 1), (2, 3)), max_prefix_symbols=3
    )
    assert witness is not None
    assert witness.prefix_a == (0, 0, 1)
    assert witness.prefix_b == (0,)
    assert witness.current_ratio == 1
    assert witness.extension_symbol == 0
    assert witness.updated_ratio_a == Fraction(440, 467)
    assert witness.updated_ratio_b == 1


def test_linear_memory_profiles_separate_depth_from_rank() -> None:
    order1 = linear_memory_profile(MATRIX, ((0,), (1, 2), (3,)))
    order1_lower_rank = linear_memory_profile(MATRIX, ((0,), (1, 3), (2,)))
    order2 = linear_memory_profile(MATRIX, ((0,), (1,), (2, 3)))
    order3 = linear_memory_profile(MATRIX, ((0, 1), (2, 3)))
    hidden = linear_memory_profile(MATRIX, ((0, 2), (1,), (3,)))

    assert (order1.forward_rank, order1.reverse_rank) == (3, 3)
    assert (order1.joint_forward_reverse_rank, order1.reversal_contrast_rank) == (6, 6)
    assert (order1_lower_rank.joint_forward_reverse_rank, order1_lower_rank.reversal_contrast_rank) == (4, 4)
    assert (order2.joint_forward_reverse_rank, order2.reversal_contrast_rank) == (6, 6)
    assert (order3.joint_forward_reverse_rank, order3.reversal_contrast_rank) == (6, 6)
    assert (hidden.forward_rank, hidden.reverse_rank) == (2, 2)
    assert hidden.joint_forward_reverse_rank == 2
    assert hidden.reversal_contrast_rank == 0


def test_reversible_control_has_zero_contrast_rank() -> None:
    profile = linear_memory_profile(reversible_four_cycle(), ((0,), (1, 2), (3,)))
    assert profile.reversal_contrast_rank == 0
