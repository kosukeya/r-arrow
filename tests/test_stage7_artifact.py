import json
from pathlib import Path

from r_arrow.stage7 import stage7_hiding_certificates


ROOT = Path(__file__).resolve().parents[1]


def test_stage7_json_artifact_matches_executable_summary():
    artifact = json.loads((ROOT / "results/stage7_hiding_certificates.json").read_text())
    generated = stage7_hiding_certificates()

    assert artifact["stage"] == generated["stage"] == 7
    assert artifact["model"] == generated["model"]
    assert artifact["partition_count"] == generated["partition_count"] == 15
    assert artifact["all_horizon_hidden_count"] == generated["all_horizon_hidden_count"] == 7
    assert artifact["finite_arrow_count"] == generated["finite_arrow_count"] == 8
    assert artifact["certificate_class_counts"] == generated["certificate_class_counts"]

    rows = generated["rows"]
    assert artifact["primary_permutation_certificate_total"] == sum(
        row["permutation_certificate_count"] for row in rows
    )

    hidden_rows = [row for row in rows if row["all_horizon_reversible"]]
    assert artifact["hidden_linear_certificate_count"] == sum(
        row["linear_certificate"] is not None for row in hidden_rows
    )

    rank_counts = {}
    for row in hidden_rows:
        rank = str(row["linear_certificate"]["rank"])
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    assert artifact["hidden_linear_rank_counts"] == rank_counts

    assert artifact["hidden_identity_intertwiner_count"] == sum(
        row["linear_certificate"]["is_identity_in_reduced_coordinates"]
        for row in hidden_rows
    )
    assert (
        artifact["reversible_control_identity_permutation_all"]
        == generated["reversible_control_identity_permutation_all"]
        is True
    )

    representative = generated["representative_linear_explanation"]
    frozen = artifact["representative"]
    assert frozen["partition"] == representative["partition"]
    assert frozen["prefix"] == representative["prefix"]
    assert frozen["forward_hidden_predictive_row"] == representative["forward_hidden_predictive_row"]
    assert frozen["reverse_hidden_predictive_row"] == representative["reverse_hidden_predictive_row"]
    assert frozen["word_probability"] == representative["forward_word_probability"]
    assert representative["forward_word_probability"] == representative["reverse_word_probability"]
    assert frozen["reduced_rank"] == representative["reduced_rank"]
    assert frozen["reduced_forward_state"] == representative["reduced_forward_state"]
    assert frozen["reduced_reverse_state"] == representative["reduced_reverse_state"]
    assert frozen["intertwiner"] == representative["intertwiner"]
