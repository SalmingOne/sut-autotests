import allure
import requests
from data.models.auth_model import AuthModels
from data.urls import Urls


class AuthEndpoint:
    response = None
    response_json = None

    @allure.step("Авторизуемся")
    def auth_api(self, json):
        self.response = requests.post(url=Urls.auth_url, json=json, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получаем токен")
    def get_header_token_api(self):
        payload = AuthModels.AuthRequestModel.Model().model_dump()
        self.response = requests.post(url=Urls.auth_url, json=payload, verify=False)
        self.response_json = self.response.json()
        return {"Access": "Bearer " + self.response_json['accessToken']}
