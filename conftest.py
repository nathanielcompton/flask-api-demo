import sys
import pytest

from src import app

sys.path.append("path")

"""
IMO, a single test fixture file can function in a similar manner as a `settings.py`,
allowing for centralized editing of fixtures, and easier/simpler test readability.
"""


@pytest.fixture
def test_client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def load_valid_request_data():
    return [
        {"length": 5.9, "width": 1.8, "height": 3.0, "weight": 12.2, "quantity": 1},
        {"length": 3.9, "width": 4.8, "height": 3.0, "weight": 10.2, "quantity": 2},
    ]


@pytest.fixture(scope="module")
def load_invalid_request_key():
    return [
        {"invalid_key": 5.9, "width": 1.8, "height": 3.0, "weight": 12.2, "quantity": 1}
    ]


@pytest.fixture(scope="module")
def load_invalid_request_value_type():
    return [
        {
            "length": "invalid_type",
            "width": 1.8,
            "height": 3.0,
            "weight": 12.2,
            "quantity": 1,
        }
    ]


@pytest.fixture(scope="module")
def load_invalid_request_negative_value():
    return [
        {"length": -5.9, "width": 1.8, "height": 3.0, "weight": 12.2, "quantity": 1},
    ]


@pytest.fixture(scope="module")
def load_too_heavy_single_item():
    return [
        {"length": 5.9, "width": 1.8, "height": 3.0, "weight": 999.2, "quantity": 1},
    ]


@pytest.fixture(scope="module")
def load_too_long_single_item():
    return [
        {"length": 5.9, "width": 500.8, "height": 3.0, "weight": 999.2, "quantity": 1},
    ]


@pytest.fixture(scope="module")
def load_too_tall_single_item():
    return [
        {"length": 5.9, "width": 1.8, "height": 999.0, "weight": 12.2, "quantity": 1},
    ]


@pytest.fixture(scope="module")
def load_exceeded_max_total_items():
    return [
        {"length": 50.0, "width": 50.0, "height": 50.0, "weight": 50.0, "quantity": 500},
    ]
