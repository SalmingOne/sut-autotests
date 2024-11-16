import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint

class AttractionRatesEndpoint:
    response = None
    response_json = None

    @allure.step("Создание ставки привлечения")
    def create_attraction_rate(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(Urls.attraction_rates_url, json=json, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаление ставки привлечения")
    def delete_attraction_rate(self, attraction_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(Urls.attraction_rates_url + attraction_id, headers=header, verify=False)
        assert self.response.status_code == 204
        return self.response

    @allure.step("Получение всех ставок привлечения")
    def get_attraction_rates(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(Urls.attraction_rates_url, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Изменить ставку привлечения")
    def change_attraction_rate(self, attraction_id, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.put(Urls.attraction_rates_url + attraction_id, json=json, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response
