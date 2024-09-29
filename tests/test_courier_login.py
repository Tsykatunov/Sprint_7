import requests
from conftest import base_url, valid_courier_data_for_register, valid_login_courier_data, \
    login_invalid_courier_data_login, login_invalid_courier_data_password


def test_courier_login():
    requests.post(f"{base_url}/api/v1/courier", json=valid_courier_data_for_register)
    response = requests.post(f"{base_url}/api/v1/courier/login", json=valid_login_courier_data)
    assert response.status_code == 200
    assert "id" in response.json()

def test_courier_login_invalid_credentials_login():
    response = requests.post(f"{base_url}/api/v1/courier/login", json=login_invalid_courier_data_login)
    assert response.status_code == 404
    assert response.json() == {
        "code": 404,
        "message": "Учетная запись не найдена"}

def test_courier_login_invalid_credentials_password():
    response = requests.post(f"{base_url}/api/v1/courier/login", json=login_invalid_courier_data_password)
    assert response.status_code == 404
    assert response.json() == {
        "code": 404,
        "message": "Учетная запись не найдена"}

def test_courier_login_missing_password_field():
    missing_field_data = {
        "login": valid_courier_data_for_register["login"],
        "password": ""
    }
    response = requests.post(f"{base_url}/api/v1/courier/login", json=missing_field_data)
    assert response.status_code == 400
    assert response.json() == {
        "code": 400,
        "message": "Недостаточно данных для входа"}

def test_courier_login_missing_login_field():
    missing_field_data = {
        "login": "",
        "password": valid_courier_data_for_register["password"]
    }
    response = requests.post(f"{base_url}/api/v1/courier/login", json=missing_field_data)
    assert response.status_code == 400
    assert response.json() == {
        "code": 400,
        "message": "Недостаточно данных для входа"}

def test_delete_courier_after():
    login_data = {
        "login": valid_courier_data_for_register["login"],
        "password": valid_courier_data_for_register["password"]
    }
    courier_id = requests.post(f"{base_url}/api/v1/courier/login", json=login_data).json()["id"]
    delete_courier = requests.delete(f"{base_url}/api/v1/courier/{courier_id}")
    assert delete_courier.status_code == 200
    assert delete_courier.json() == {"ok": True}