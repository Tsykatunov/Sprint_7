import requests
import random
import string
import time

base_url = "https://qa-scooter.praktikum-services.ru"

class CourierCreate:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def register_new_courier_and_return_login_password():
        login = CourierCreate.generate_random_string(10)
        password = CourierCreate.generate_random_string(10)
        first_name = CourierCreate.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        try:
            response = requests.post(f"{base_url}/api/v1/courier", json=payload)
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            response = requests.post(f"{base_url}/api/v1/courier", json=payload)

        if response.status_code == 201:
            return login, password, first_name
        else:
            return None, None, None

    @staticmethod
    def login_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }

        try:
            response = requests.post(f"{base_url}/api/v1/courier/login", json=payload)
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            response = requests.post(f"{base_url}/api/v1/courier/login", json=payload)

        if response.status_code == 200:
            return response.json()["id"]
        else:
            return None

#Данные для создания заказа:
order_data = {
        "firstName": "Sheev",
        "lastName": "Palpatine",
        "address": "Galactic Senate",
        "metroStation": 53,
        "phone": "+9779809836",
        "rentTime": 2,
        "deliveryDate": "2024-10-05",
        "comment": "Я и есть ЗАКАЗ!",
        "color": []
    }