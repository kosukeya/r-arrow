import csv
from pathlib import Path

from r_arrow.stage4 import stage4_frontier


def test_stage4_csv_matches_executable_frontier() -> None:
    artifact_path = Path(__file__).resolve().parents[1] / "results" / "stage4_detection_frontier.csv"
    with artifact_path.open(newline="", encoding="utf-8") as handle:
        artifact_rows = list(csv.DictReader(handle))

    frontier = stage4_frontier()
    executable = {(row["model"], row["label"]): row for row in frontier["rows"]}
    assert len(artifact_rows) == frontier["row_count"] == 45
    assert set(executable) == {(row["model"], row["label"]) for row in artifact_rows}

    for artifact in artifact_rows:
        row = executable[(artifact["model"], artifact["label"])]
        expected_horizon = "infinity" if row["L_arrow"] is None else str(row["L_arrow"])
        expected_word = "" if row["witness_word"] is None else "".join(str(symbol) for symbol in row["witness_word"])
        assert artifact["macro_states"] == str(row["macro_states"])
        assert artifact["L_arrow"] == expected_horizon
        assert artifact["all_horizon_reversible"] == str(row["all_horizon_reversible"]).lower()
        assert artifact["witness_word"] == expected_word
        assert artifact["witness_forward_probability"] == (row["witness_forward_probability"] or "")
        assert artifact["witness_reverse_probability"] == (row["witness_reverse_probability"] or "")
        assert artifact["reachable_dimension"] == str(row["reachable_dimension"])
