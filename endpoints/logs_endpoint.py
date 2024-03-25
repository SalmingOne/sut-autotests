import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class LogsEndpoint:
    response = None
    response_json = None

    @allure.step("Получение настроек аудита")
    def get_logs_settings(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.logs_settings_url, headers=header)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Установка настроек аудита")
    def post_logs_settings(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.logs_settings_url, headers=header, json=json)
        return self.response