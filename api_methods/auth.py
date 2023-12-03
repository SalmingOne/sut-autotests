import requests
import allure
from configuration.config_provider import ConfigProvider

config = ConfigProvider()

class AuthApi:
    """ Класс методов API авторизации\аутентификации"""

    @allure.step("Авторизация")
    def auth(self) -> None:

        response = requests.post(
            url=config.get_auth_url(),
            json=config.get_admin_creds()
        )
        if response.status_code == 200:
            config.set_token(response.json()["accessToken"])
        else:
            assert False, 'Авторизация не удалась, статус код: ' + str(response.status_code)

