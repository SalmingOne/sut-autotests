import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class SkillsEndpoint:
    response = None
    response_json = None

    @allure.step("Получаем все Знания")
    def get_all_skills_api(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.skills_url, headers=header)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Создаем Знание")
    def create_skills_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.skills_url, headers=header, json=json)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получаем количество Знаний")
    def return_len_skills(self):
        return len(self.get_all_skills_api().json())