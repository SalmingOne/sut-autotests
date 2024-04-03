import allure
import requests
import testit

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class TagsEndpoint:
    response = None
    response_json = None

    @allure.step("Получаем все группы знаний")
    def get_all_tags_api(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.tags_url, headers=header)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Создаем группу знаний")
    def create_tag_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.tags_url, headers=header, json=json)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаление группу знаний")
    def delete_tag_api(self, tag_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.tags_url + tag_id, headers=header)
        assert self.response.status_code == 204
        return self.response

    @allure.step("Получение id группы знаний по имени")
    def get_tag_id_by_name_api(self, name):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.tags_url, headers=header)
        self.response_json = self.response.json()
        for tag in self.response_json:
            if tag['name'] == name:
                return tag['id']

    @testit.step("Удаление группы знаний по имени")
    @allure.step("Удаление группы знаний по имени")
    def delete_tag_by_name_api(self, name):
        tag_id = self.get_tag_id_by_name_api(name)
        self.delete_tag_api(str(tag_id))
