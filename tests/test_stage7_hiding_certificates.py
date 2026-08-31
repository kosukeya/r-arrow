from fractions import Fraction

from r_arrow.arrow_memory import arrow_filter_state_for_word
from r_arrow.benchmarks import higher_order_hidden_arrow_four_state, reversible_four_cycle
from r_arrow.coarse_grain import partition_label, set_partitions
from r_arrow.equivalence import observed_time_reversal_equivalence, time_reversed_transition
from r_arrow.reversal_symmetry import (
    linear_intertwiner_certificate,
    minimal_scalar_realization,
    permutation_reversal_certificates,
    reduced_state_for_word,
)
from r_arrow.stage7 import REPRESENTATIVE_HIDDEN, stage7_hiding_certificates


def _hidden_and_finite_partitions():
    matrix = higher_order_hidden_arrow_four_state()
    hidden = []
    finite = []
    for partition in set_partitions(4):
        result = observed_time_reversal_equivalence(matrix, partition)
        (hidden if result.equivalent else finite).append(partition)
    return tuple(hidden), tuple(finite)


def test_frozen_stage4_split_is_preserved():
    hidden, finite = _hidden_and_finite_partitions()
    assert len(hidden) == 7
    assert len(finite) == 8


def test_primary_witness_has_no_observation_preserving_permutation_certificate():
    matrix = higher_order_hidden_arrow_four_state()
    for partition in set_partitions(4):
        assert permutation_reversal_certificates(matrix, partition) == ()


def test_all_hidden_primary_partitions_have_exact_linear_intertwiners():
    matrix = higher_order_hidden_arrow_four_state()
    hidden, _ = _hidden_and_finite_partitions()
    ranks = []
    for partition in hidden:
        certificate = linear_intertwiner_certificate(matrix, partition)
        assert certificate is not None
        assert certificate.rank in {1, 2}
        assert certificate.is_identity
        ranks.append(certificate.rank)
    assert set(ranks) == {1, 2}


def test_finite_arrow_partitions_have_no_equality_intertwiner():
    matrix = higher_order_hidden_arrow_four_state()
    _, finite = _hidden_and_finite_partitions()
    for partition in finite:
        assert linear_intertwiner_certificate(matrix, partition) is None


def test_reversible_control_has_identity_permutation_certificate_for_every_partition():
    matrix = reversible_four_cycle()
    for partition in set_partitions(4):
        certificates = permutation_reversal_certificates(matrix, partition)
        assert certificates
        assert any(certificate.cycle_notation == "identity" for certificate in certificates)


def test_representative_hidden_rows_differ_but_reduced_states_pair_exactly():
    matrix = higher_order_hidden_arrow_four_state()
    reverse = time_reversed_transition(matrix)
    partition = REPRESENTATIVE_HIDDEN
    prefix = (0,)

    filter_state = arrow_filter_state_for_word(matrix, partition, prefix)
    assert filter_state.forward_row != filter_state.reverse_row
    assert filter_state.forward_likelihood == filter_state.reverse_likelihood == Fraction(1, 2)

    forward = minimal_scalar_realization(matrix, partition)
    backward = minimal_scalar_realization(reverse, partition)
    certificate = linear_intertwiner_certificate(matrix, partition)
    assert certificate is not None
    assert certificate.rank == 2

    forward_state = reduced_state_for_word(forward, prefix)
    reverse_state = reduced_state_for_word(backward, prefix)
    mapped = tuple(
        sum(
            forward_state[i] * certificate.intertwiner[i][j]
            for i in range(certificate.rank)
        )
        for j in range(certificate.rank)
    )
    assert mapped == reverse_state
    assert forward_state == reverse_state


def test_complete_taxonomy_is_8_finite_and_7_linear_only():
    artifact = stage7_hiding_certificates()
    assert artifact["certificate_class_counts"] == {"finite_arrow": 8, "linear_only": 7}
    assert artifact["all_horizon_hidden_count"] == 7
    assert artifact["finite_arrow_count"] == 8
    assert artifact["reversible_control_identity_permutation_all"] is True

    hidden_rows = [row for row in artifact["rows"] if row["all_horizon_reversible"]]
    assert {row["certificate_class"] for row in hidden_rows} == {"linear_only"}
    assert all(row["permutation_certificate_count"] == 0 for row in hidden_rows)
    assert all(row["linear_certificate"] is not None for row in hidden_rows)


def test_hidden_labels_match_stage6_family():
    artifact = stage7_hiding_certificates()
    hidden_labels = {
        row["label"] for row in artifact["rows"] if row["all_horizon_reversible"]
    }
    assert hidden_labels == {
        "02|1|3",
        "0|123",
        "012|3",
        "013|2",
        "02|13",
        "023|1",
        "0123",
    }


def test_representative_is_expected_partition():
    assert partition_label(REPRESENTATIVE_HIDDEN, 4) == "02|1|3"
