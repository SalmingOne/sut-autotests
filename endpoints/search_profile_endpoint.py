import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class SearchProfileEndpoint:
    response = None
    response_json = None

    @allure.step("Создаем Расширенный поиск")
    def create_advanced_search_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.create_advanced_search_url, headers=header, json=json, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаляем Расширенный поиск")
    def delete_advanced_search_api(self, search_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.advanced_search_url + search_id, headers=header, verify=False)
        assert self.response.status_code == 204
        return self.response

    @allure.step("Проверяем наличие расширенного поиска")
    def check_advanced_search_by_id(self, user_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.advanced_search_url + user_id, headers=header, verify=False)
        self.response_json = self.response.json()
        print(self.response.status_code)
        print(self.response.json())
        if not self.response.json():
            return False
        else:
            return True
