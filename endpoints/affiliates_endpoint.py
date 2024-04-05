import allure
import requests
import testit

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class AffiliatesEndpoint:
    response = None
    response_json = None

    @allure.step("Получаем все филиалы")
    def get_all_affiliates_api(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.affiliates_url, headers=header)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Создаем филиал")
    def create_affiliates_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.affiliates_url, headers=header, json=json)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаляем филиал")
    def delete_affiliates_api(self, affiliates_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.affiliates_url + affiliates_id, headers=header)
        assert self.response.status_code == 204
        return self.response

    @allure.step("Получение id филиала по имени")
    def get_filial_id_by_name_api(self, name):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.affiliates_url, headers=header)
        self.response_json = self.response.json()
        for filial in self.response_json:
            if filial['name'] == name:
                return filial['id']

    @testit.step("Удаление филиала по имени")
    @allure.step("Удаление филиала по имени")
    def delete_filial_by_name_api(self, name):
        filial_id = self.get_filial_id_by_name_api(name)
        self.delete_affiliates_api(str(filial_id))