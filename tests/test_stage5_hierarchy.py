from fractions import Fraction

from r_arrow.stage5 import stage5_hierarchy


def _row_by_label(result, label):
    return next(row for row in result["rows"] if row["label"] == label)


def _rep_by_name(result, name):
    return next(row for row in result["representatives"] if row["name"] == name)


def test_stage5_reproduces_frozen_detection_classes():
    result = stage5_hierarchy()
    assert result["stage"] == 5
    assert result["state_count"] == 4
    assert result["partition_count"] == 15
    assert result["detection_class_summary"] == {"1": 4, "2": 2, "3": 2, "infinity": 7}

    expected = {
        "0|1|2|3": 1,
        "0|1|23": 2,
        "0|12|3": 1,
        "0|13|2": 1,
        "01|2|3": 1,
        "02|1|3": None,
        "03|1|2": 2,
        "0|123": None,
        "01|23": 3,
        "012|3": None,
        "013|2": None,
        "02|13": None,
        "023|1": None,
        "03|12": 3,
        "0123": None,
    }
    assert {row["label"]: row["L_arrow"] for row in result["rows"]} == expected


def test_first_detection_odd_statistics_are_exact():
    result = stage5_hierarchy()
    expected = {
        "0|1|2|3": (3, "9/64"),
        "0|1|23": (3, "27/1024"),
        "0|12|3": (3, "9/64"),
        "0|13|2": (3, "9/64"),
        "01|2|3": (3, "9/64"),
        "03|1|2": (3, "27/1024"),
        "01|23": (4, "27/2048"),
        "03|12": (4, "27/4096"),
    }
    for label, (pair_count, mass) in expected.items():
        row = _row_by_label(result, label)
        assert row["first_detection_odd_pair_count"] == pair_count
        assert row["first_detection_odd_mass"] == mass
        assert row["all_lower_orders_zero"] is True

    for label in {"02|1|3", "0|123", "012|3", "013|2", "02|13", "023|1", "0123"}:
        row = _row_by_label(result, label)
        assert row["all_horizon_reversible"] is True
        assert row["first_detection_odd_pair_count"] is None
        assert row["first_detection_odd_mass"] is None


def test_representative_temporal_order_profiles_and_cancellation():
    result = stage5_hierarchy()

    order1 = _rep_by_name(result, "order_1_direct")
    order2 = _rep_by_name(result, "order_2_hidden")
    order3 = _rep_by_name(result, "order_3_hidden")
    hidden = _rep_by_name(result, "all_horizon_hidden")

    assert order1["label"] == "0|12|3" and order1["L_arrow"] == 1
    assert order2["label"] == "0|1|23" and order2["L_arrow"] == 2
    assert order3["label"] == "01|23" and order3["L_arrow"] == 3
    assert hidden["label"] == "02|1|3" and hidden["L_arrow"] is None and hidden["all_horizon_reversible"]

    assert [entry["odd_pair_count"] for entry in order2["odd_profile_L1_to_L3"]][:2] == [0, 3]
    assert [entry["odd_pair_count"] for entry in order3["odd_profile_L1_to_L3"]] == [0, 0, 4]
    assert [entry["odd_pair_count"] for entry in hidden["odd_profile_L1_to_L3"]] == [0, 0, 0]

    assert order1["cancellation"]["summary"]["net_delta"] == "3/64"
    assert order1["cancellation"]["summary"]["cancelled_mass"] == "0"
    assert order2["cancellation"]["summary"]["net_delta"] == "9/1024"
    assert order2["cancellation"]["summary"]["cancelled_mass"] == "3/1024"
    assert order3["cancellation"]["summary"]["net_delta"] == "-27/8192"
    assert order3["cancellation"]["summary"]["cancelled_mass"] == "93/16384"
    assert hidden["cancellation"] is None


def test_temporal_order_is_not_same_as_first_detection_magnitude():
    result = stage5_hierarchy()
    a = _row_by_label(result, "01|23")
    b = _row_by_label(result, "03|12")
    assert a["L_arrow"] == b["L_arrow"] == 3
    assert Fraction(a["first_detection_odd_mass"]) == 2 * Fraction(b["first_detection_odd_mass"])
