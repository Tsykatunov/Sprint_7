import requests

def test_get_orders(base_url):
    response = requests.get(f"{base_url}/api/v1/orders")
    assert response.status_code == 200
    orders = response.json()["orders"]
    assert isinstance(orders, list)
    assert len(orders) > 0

def test_get_orders_without_courier(base_url):
    courierId = 1
    response = requests.get(f"{base_url}/api/v1/orders?courierId={courierId}")
    assert response.status_code == 404
    assert response.json() == {
        "code": 404,
        "message": f"Курьер с идентификатором {courierId} не найден"}