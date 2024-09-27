import requests

def test_create_courier(base_url, valid_courier_data_for_register):
    response = requests.post(f"{base_url}/api/v1/courier", json=valid_courier_data_for_register)
    assert response.status_code == 201
    assert response.json() == {"ok": True}

def test_create_duplicate_courier(base_url, duplicate_courier_data):
    response = requests.post(f"{base_url}/api/v1/courier", json=duplicate_courier_data)
    assert response.status_code in [409]
    assert response.json() == {
        "code": 409,
        "message": "Этот логин уже используется. Попробуйте другой."}

def test_create_courier_missing_fields(base_url, missing_login_field_courier_data):
    response = requests.post(f"{base_url}/api/v1/courier", json=missing_login_field_courier_data)
    assert response.status_code == 400
    assert response.json() == {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи"}

def test_create_courier_existing_login(base_url, missing_password_field_courier_data):
    response = requests.post(f"{base_url}/api/v1/courier", json=missing_password_field_courier_data)
    assert response.status_code == 400
    assert response.json() == {
        "code": 400,
        "message": "Недостаточно данных для создания учетной записи"}

def test_delete_courier_after(base_url, valid_courier_data_for_register):
    login_data = {
        "login": valid_courier_data_for_register["login"],
        "password": valid_courier_data_for_register["password"]
    }
    courier_id = requests.post(f"{base_url}/api/v1/courier/login", json=login_data).json()["id"]
    requests.delete(f"{base_url}api/v1/courier/{courier_id}")