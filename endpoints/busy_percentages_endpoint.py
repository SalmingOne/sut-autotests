import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class BusyPercentagesEndpoint:
    response = None
    response_json = None

    @allure.step("Получение процента занятости для проекта")
    def get_busy_percentages_api(self, id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.busy_percentages_url + f'tasks/{id}', headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response_json   
    
    @allure.step("Создаем проценты занятости")
    def create_busy_percentages_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.busy_percentages_url, headers=header, json=json, verify=False)
        return self.response