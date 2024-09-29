import pytest

base_url = "https://qa-scooter.praktikum-services.ru"

#Данные для тестов регистрации курьера:
valid_courier_data_for_register = {
        "login": "Anakin",
        "password": "DarthVader",
        "firstName": "Any"
    }

missing_login_field_courier_data = {
        "login": "",
        "password": "DarthVader",
        "firstName": "Any"
    }

missing_password_field_courier_data = {
        "login": "Anakin",
        "password": "",
        "firstName": "Any"
    }

#Данные для тестов логина курьера:
valid_login_courier_data= {
        "login": "Anakin",
        "password": "DarthVader"
    }

login_invalid_courier_data_login = {
        "login": "Anakine",
        "password": "DarthVader"
    }

login_invalid_courier_data_password = {
        "login": "Anakin",
        "password": "DarthBane"
    }

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