import requests
from conftest import base_url
from helpers import CourierCreate

class TestCourierCreate:
    def test_create_courier(self):
        login, password, first_name = CourierCreate.register_new_courier_and_return_login_password()
        assert login is not None
        assert password is not None
        assert first_name is not None

    def test_create_duplicate_courier(self):
        login, password, first_name = CourierCreate.register_new_courier_and_return_login_password()
        response = requests.post(f"{base_url}/api/v1/courier", json={
            "login": login,
            "password": password,
            "firstName": first_name
        })
        assert response.status_code == 409
        assert response.json() == {
            "code": 409,
            "message": "Этот логин уже используется. Попробуйте другой."
        }

    def test_create_courier_missing_login_field(self):
        response = requests.post(f"{base_url}/api/v1/courier", json={
            "password": CourierCreate.generate_random_string(10),
            "firstName": CourierCreate.generate_random_string(10)
        })
        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }

    def test_create_courier_missing_password_field(self):
        response = requests.post(f"{base_url}/api/v1/courier", json={
            "login": CourierCreate.generate_random_string(10),
            "firstName": CourierCreate.generate_random_string(10)
        })
        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }