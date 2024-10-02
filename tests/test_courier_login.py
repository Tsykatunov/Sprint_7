import requests
from conftest import base_url
from helpers import CourierCreate

class TestCourierLogin:
    def test_courier_login(self):
        login, password, first_name = CourierCreate.register_new_courier_and_return_login_password()
        courier_id = CourierCreate.login_courier(login, password)
        assert courier_id is not None

    def test_courier_login_invalid_login(self):
        login, password, first_name = CourierCreate.register_new_courier_and_return_login_password()
        response = requests.post(f"{base_url}/api/v1/courier/login", json={
            "login": login + "1",
            "password": password
        })
        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена"
        }

    def test_courier_login_invalid_password(self):
        login, password, first_name = CourierCreate.register_new_courier_and_return_login_password()
        response = requests.post(f"{base_url}/api/v1/courier/login", json={
            "login": login,
            "password": password + "1"
        })
        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена"
        }

    def test_courier_login_missing_password_field(self):
        login, password, first_name = CourierCreate.register_new_courier_and_return_login_password()
        response = requests.post(f"{base_url}/api/v1/courier/login", json={
            "login": login,
            "password": ""
        })
        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для входа"
        }

    def test_courier_login_missing_login_field(self):
        login, password, first_name = CourierCreate.register_new_courier_and_return_login_password()
        response = requests.post(f"{base_url}/api/v1/courier/login", json={
            "login": "",
            "password": password
        })
        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для входа"
        }