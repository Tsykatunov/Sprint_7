import pytest

@pytest.fixture
def base_url():
    return "https://qa-scooter.praktikum-services.ru/"

#Данные для тестов регистрации курьера:
@pytest.fixture
def valid_courier_data_for_register():
    return {
        "login": "Anakin",
        "password": "DarthVader",
        "firstName": "Any"
    }

@pytest.fixture
def duplicate_courier_data(valid_courier_data_for_register):
    return valid_courier_data_for_register

@pytest.fixture
def missing_login_field_courier_data():
    return {
        "login": "",
        "password": "DarthVader",
        "firstName": "Any"
    }

@pytest.fixture
def missing_password_field_courier_data():
    return {
        "login": "Anakin",
        "password": "",
        "firstName": "Any"
    }

#Данные для тестов логина курьера:

@pytest.fixture
def valid_login_courier_data():
    return {
        "login": "Anakin",
        "password": "DarthVader"
    }

@pytest.fixture
def login_invalid_courier_data_login():
    return {
        "login": "Anakine",
        "password": "DarthVader"
    }

@pytest.fixture
def login_invalid_courier_data_password():
    return {
        "login": "Anakin",
        "password": "DarthBane"
    }

#Данные для создания заказа:
@pytest.fixture
def order_data():
    return {
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