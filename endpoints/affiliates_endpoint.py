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
        self.response = requests.get(url=Urls.affiliates_url, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Создаем филиал")
    def create_affiliates_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.affiliates_url, headers=header, json=json, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаляем филиал")
    def delete_affiliates_api(self, affiliates_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.affiliates_url + affiliates_id, headers=header, verify=False)
        assert self.response.status_code == 204
        return self.response

    @allure.step("Получение id филиала по имени")
    def get_filial_id_by_name_api(self, name):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.affiliates_url, headers=header, verify=False)
        self.response_json = self.response.json()
        for filial in self.response_json:
            if filial['name'] == name:
                return filial['id']

    @testit.step("Удаление филиала по имени")
    @allure.step("Удаление филиала по имени")
    def delete_filial_by_name_api(self, name):
        filial_id = self.get_filial_id_by_name_api(name)
        payload = dict(
            name=name,
            address='Самара',
            employees=[]
        )
        self.change_filial(str(filial_id), payload)
        self.delete_affiliates_api(str(filial_id))

    @allure.step("Изменение филиала")
    def change_filial(self, affiliates_id, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.put(url=Urls.affiliates_url + affiliates_id, json=json, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаление филиала если он существует")
    def delete_filial_if_it_exist(self, name):
        filial_id = self.get_filial_id_by_name_api(name)
        if filial_id is None:
            pass
        else:
            payload = dict(
                name=name,
                address='Самара',
                employees=[]
            )
            self.change_filial(str(filial_id), payload)
            self.delete_affiliates_api(str(filial_id))

    @allure.step("Получаем названия всех филиалов")
    def get_all_affiliates_name(self):
        all_affiliates = self.get_all_affiliates_api().json()
        all_affiliates_name = []
        for affiliates in all_affiliates:
            all_affiliates_name.append(affiliates['name'])
        return all_affiliates_name