def test_sanity_check(test_client):
    res = test_client.get("/sanity")
    assert res.status_code == 200
    assert res.data == b"This is a sanity check!"


def test_valid_items_returns_compact(test_client, load_valid_request_data):
    body = load_valid_request_data
    res = test_client.post("/vehicle_size", json=body)
    assert res.status_code == 200
    assert res.data == b"Compact"
