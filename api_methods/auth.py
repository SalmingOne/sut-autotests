import time

import requests
import allure
from configuration.config_provider import ConfigProvider

config = ConfigProvider()


# Класс методов API авторизации\\аутентификации
class AuthApi:

    @allure.step("Авторизация")
    def auth(self):

        response = requests.post(
            url=config.get_auth_url(),
            json=config.get_admin_creds()
        )
        print(response.status_code)

        if response.status_code == 200:
            config.set_token(response.json()["accessToken"])
            time.sleep(1)
        else:
            assert False, 'Авторизация не удалась, статус код: ' + \
                          str(response.status_code)
