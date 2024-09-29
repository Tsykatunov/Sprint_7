import pytest
import requests
from conftest import base_url, order_data

@pytest.mark.parametrize("color", [
    ["BLACK"],
    ["GREY"],
    ["BLACK", "GREY"],
    []
])
def test_create_order_with_color(color):
    order_data["color"] = color
    response = requests.post(f"{base_url}/api/v1/orders", json=order_data)
    assert response.status_code == 201
    assert "track" in response.json()