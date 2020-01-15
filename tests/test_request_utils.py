import pytest

from src.request_utils import validate_request


def test_valid_keys_and_values(load_valid_request_data):
    assert load_valid_request_data == validate_request(load_valid_request_data)


def test_request_format_invalid_key(load_invalid_request_key):
    with pytest.raises(KeyError) as e:
        validate_request(load_invalid_request_key)
        assert load_invalid_request_key[0] in e


def test_request_invalid_key_type(load_invalid_request_value_type):
    with pytest.raises(ValueError) as e:
        validate_request(load_invalid_request_value_type)
        assert load_invalid_request_value_type[0] in e


def test_request_negative_size_value(load_invalid_request_negative_value):
    with pytest.raises(ValueError) as e:
        validate_request(load_invalid_request_negative_value)
        assert load_invalid_request_negative_value[0] in e
