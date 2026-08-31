"""Executable Stage 7 structural hiding-certificate synthesis."""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from typing import Any

from .arrow_memory import arrow_filter_state_for_word
from .benchmarks import higher_order_hidden_arrow_four_state, reversible_four_cycle
from .coarse_grain import Partition, partition_label, set_partitions
from .equivalence import observed_time_reversal_equivalence, time_reversed_transition
from .reversal_symmetry import (
    linear_intertwiner_certificate,
    minimal_scalar_realization,
    permutation_reversal_certificates,
    reduced_state_for_word,
)

REPRESENTATIVE_HIDDEN: Partition = ((0, 2), (1,), (3,))


def _fraction(value: Fraction) -> str:
    return str(value)


def _word(value: tuple[int, ...]) -> list[int]:
    return list(value)


def _matrix(value: tuple[tuple[Fraction, ...], ...]) -> list[list[str]]:
    return [[_fraction(entry) for entry in row] for row in value]


def _row_record(matrix: Any, partition: Partition) -> dict[str, Any]:
    label = partition_label(partition, 4)
    equivalence = observed_time_reversal_equivalence(matrix, partition)
    permutation_certificates = permutation_reversal_certificates(matrix, partition)
    linear_certificate = linear_intertwiner_certificate(matrix, partition)

    if not equivalence.equivalent:
        if permutation_certificates:
            raise AssertionError("a valid permutation certificate would force all-horizon equivalence")
        if linear_certificate is not None:
            raise AssertionError("finite-arrow observation must not receive an equality intertwiner")
        certificate_class = "finite_arrow"
    elif permutation_certificates:
        certificate_class = "permutation"
    elif linear_certificate is not None:
        certificate_class = "linear_only"
    else:
        certificate_class = "unresolved"

    return {
        "label": label,
        "partition": [list(block) for block in partition],
        "L_arrow": equivalence.detection_horizon,
        "all_horizon_reversible": equivalence.equivalent,
        "certificate_class": certificate_class,
        "permutation_certificate_count": len(permutation_certificates),
        "permutation_certificates": [
            {
                "permutation": list(certificate.permutation),
                "cycle_notation": certificate.cycle_notation,
            }
            for certificate in permutation_certificates
        ],
        "linear_certificate": None
        if linear_certificate is None
        else {
            "rank": linear_certificate.rank,
            "intertwiner": _matrix(linear_certificate.intertwiner),
            "prefix_basis_words": [_word(word) for word in linear_certificate.prefix_basis_words],
            "is_identity_in_reduced_coordinates": linear_certificate.is_identity,
        },
    }


def _representative_linear_explanation(matrix: Any) -> dict[str, Any]:
    partition = REPRESENTATIVE_HIDDEN
    prefix = (0,)
    filter_state = arrow_filter_state_for_word(matrix, partition, prefix)
    reverse_matrix = time_reversed_transition(matrix)
    forward_realization = minimal_scalar_realization(matrix, partition)
    reverse_realization = minimal_scalar_realization(reverse_matrix, partition)
    certificate = linear_intertwiner_certificate(matrix, partition)
    if certificate is None:
        raise AssertionError("representative hidden observation must have a linear certificate")

    reduced_forward = reduced_state_for_word(forward_realization, prefix)
    reduced_reverse = reduced_state_for_word(reverse_realization, prefix)
    mapped_forward = tuple(
        sum(
            (
                reduced_forward[i] * certificate.intertwiner[i][j]
                for i in range(certificate.rank)
            ),
            Fraction(0),
        )
        for j in range(certificate.rank)
    )
    if mapped_forward != reduced_reverse:
        raise AssertionError("intertwiner must pair representative reduced states")

    return {
        "partition": partition_label(partition, 4),
        "prefix": list(prefix),
        "forward_hidden_predictive_row": [_fraction(value) for value in filter_state.forward_row],
        "reverse_hidden_predictive_row": [_fraction(value) for value in filter_state.reverse_row],
        "hidden_rows_differ": filter_state.forward_row != filter_state.reverse_row,
        "forward_word_probability": _fraction(filter_state.forward_likelihood),
        "reverse_word_probability": _fraction(filter_state.reverse_likelihood),
        "reduced_rank": certificate.rank,
        "reduced_forward_state": [_fraction(value) for value in reduced_forward],
        "reduced_reverse_state": [_fraction(value) for value in reduced_reverse],
        "intertwiner": _matrix(certificate.intertwiner),
        "reduced_states_match_under_intertwiner": mapped_forward == reduced_reverse,
        "interpretation": "forward/reverse hidden predictive rows differ, but their observable minimal coordinates are exactly paired by the linear intertwiner",
    }


def stage7_hiding_certificates() -> dict[str, Any]:
    """Return the complete bounded Stage 7 certificate taxonomy."""

    matrix = higher_order_hidden_arrow_four_state()
    partitions = tuple(set_partitions(4))
    rows = [_row_record(matrix, partition) for partition in partitions]
    class_counts = Counter(row["certificate_class"] for row in rows)

    hidden_rows = [row for row in rows if row["all_horizon_reversible"]]
    finite_rows = [row for row in rows if not row["all_horizon_reversible"]]
    if len(hidden_rows) != 7 or len(finite_rows) != 8:
        raise AssertionError("Stage 7 must preserve the frozen Stage 4 detection split")

    reversible_control_rows = [_row_record(reversible_four_cycle(), partition) for partition in partitions]
    if any(row["certificate_class"] != "permutation" for row in reversible_control_rows):
        raise AssertionError("reversible control must admit an observation-preserving permutation certificate")
    if any(
        not any(certificate["cycle_notation"] == "identity" for certificate in row["permutation_certificates"])
        for row in reversible_control_rows
    ):
        raise AssertionError("identity permutation must certify every reversible-control observation")

    return {
        "stage": 7,
        "model": "higher_order_hidden_arrow_four_state",
        "partition_count": len(partitions),
        "all_horizon_hidden_count": len(hidden_rows),
        "finite_arrow_count": len(finite_rows),
        "certificate_class_counts": dict(sorted(class_counts.items())),
        "rows": rows,
        "representative_linear_explanation": _representative_linear_explanation(matrix),
        "reversible_control_partition_count": len(reversible_control_rows),
        "reversible_control_identity_permutation_all": True,
        "interpretation_guard": "linear-only equality is an observable representation certificate, not a literal hidden-state relabeling or microscopic reversibility claim",
    }


def main() -> None:
    print(json.dumps(stage7_hiding_certificates(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
