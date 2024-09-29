import requests
from conftest import base_url, missing_login_field_courier_data, valid_courier_data_for_register, \
    missing_password_field_courier_data


def test_create_courier():
    response = requests.post(f"{base_url}/api/v1/courier", json=valid_courier_data_for_register)
    assert response.status_code == 201
    assert response.json() == {"ok": True}

def test_create_duplicate_courier():
    response = requests.post(f"{base_url}/api/v1/courier", json=valid_courier_data_for_register)
    assert response.status_code in [409]
    assert response.json() == {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой."}

def test_create_courier_missing_fields():
    response = requests.post(f"{base_url}/api/v1/courier", json=missing_login_field_courier_data)
    assert response.status_code == 400
    assert response.json() == {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи"}

def test_create_courier_existing_login():
    response = requests.post(f"{base_url}/api/v1/courier", json=missing_password_field_courier_data)
    assert response.status_code == 400
    assert response.json() == {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи"}

def test_delete_courier_after():
    login_data = {
        "login": valid_courier_data_for_register["login"],
        "password": valid_courier_data_for_register["password"]
    }
    courier_id = requests.post(f"{base_url}/api/v1/courier/login", json=login_data).json()["id"]
    delete_courier = requests.delete(f"{base_url}/api/v1/courier/{courier_id}")
    assert delete_courier.status_code == 200
    assert delete_courier.json() == {"ok": True}