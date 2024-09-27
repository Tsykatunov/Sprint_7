import pytest
import requests

@pytest.mark.parametrize("color", [
    ["BLACK"],
    ["GREY"],
    ["BLACK", "GREY"],
    []
])
def test_create_order_with_color(base_url, order_data, color):
    order_data["color"] = color
    response = requests.post(f"{base_url}/api/v1/orders", json=order_data)
    assert response.status_code == 201
    assert "track" in response.json()