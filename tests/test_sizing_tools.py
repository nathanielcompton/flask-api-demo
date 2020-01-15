import pytest

from src.sizing_tools import find_best_fit


def test_single_item_too_heavy(load_too_heavy_single_item):
    with pytest.raises(ValueError) as e:
        find_best_fit(load_too_heavy_single_item)
        assert load_too_heavy_single_item[0]["weight"] in e
        assert load_too_heavy_single_item[0]["height"] not in e


def test_single_item_too_tall(load_too_tall_single_item):
    with pytest.raises(ValueError) as e:
        find_best_fit(load_too_tall_single_item)
        assert load_too_tall_single_item[0]["height"] in e
        assert load_too_tall_single_item[0]["weight"] not in e


def test_single_item_too_long(load_too_long_single_item):
    with pytest.raises(ValueError) as e:
        find_best_fit(load_too_long_single_item)
        assert load_too_long_single_item[0]["width"] in e
        assert load_too_long_single_item[0]["length"] not in e


def test_exceed_max_vehicle_constraints(load_exceeded_max_total_items):
    error_string = f"Items list total weight/vol exceeds largest Vehicle max"
    with pytest.raises(ValueError) as e:
        find_best_fit(load_exceeded_max_total_items)
        assert error_string in e
