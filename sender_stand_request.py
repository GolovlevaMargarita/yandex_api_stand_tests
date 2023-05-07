import configuration
import requests
import data

def get_kit_body(name):
    current_name = data.kit_body.copy()
    current_name["name"] = name
    return current_name
def get_auth_token():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, headers=data.headers, json=data.user_body);
    return response.json()['authToken'];
def get_kits(authToken, kit_data):
    global data;
    headers = data.headers.copy();
    headers["Authorization"] = "Bearer " + authToken;

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_MAIN_KITS_PATH, headers=headers, json=kit_data);

# authToken = get_auth_token();
#
# kits_response = get_kits(authToken);
# kits = kits_response.json();
#
# print(kits);

# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов




