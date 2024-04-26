import time

import requests
import allure
from configuration.config_provider import ConfigProvider
from data.data import LOGIN, PASSWORD

config = ConfigProvider()


# Класс методов API авторизации\\аутентификации
class AuthApi:

    @allure.step("Авторизация")
    def auth(self):

        response = requests.post(
            url=config.get_auth_url(),
            json=config.get_admin_creds()
        )

        if response.status_code == 200:
            config.set_token(response.json()["accessToken"])
        else:
            assert False, 'Авторизация не удалась, статус код: ' + \
                          str(response.status_code)

    @allure.step("Авторизация токена")
    def auth_to_token(self):

        response = requests.post(
            url=config.get_auth_url(),
            json=dict(login=LOGIN, password=PASSWORD)
        )

        if response.status_code == 200:
            config.set_token(response.json()["accessToken"])
            return response.json()["accessToken"]
        else:
            assert False, 'Авторизация не удалась, статус код: ' + \
                          str(response.status_code)