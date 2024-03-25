import allure
import requests

from data.urls import Urls

from endpoints.auth_endpoint import AuthEndpoint


class VariablesEndpoint:
    response = None
    response_json = None

    @allure.step("Получаем все переменные")
    def get_all_variables(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.variables_url, headers=header)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Создаем переменную")
    def create_variables_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.variables_url, headers=header, json=json)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаляем переменную")
    def delete_variables_api(self, variables_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.variables_url + variables_id, headers=header)
        assert self.response.status_code == 204
        return self.response
