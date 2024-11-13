import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint
from utils.concat_testit_allure_step import allure_testit_step


class SkillsAndKnowledgeEndpoint:
    response = None
    response_json = None

    @allure_testit_step('Получаем все Знания и Навыки')
    def get_all_skills_and_knowledge_api(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.skills_url, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure_testit_step('Создаем Знания или Навык')
    def create_skills_and_knowledge_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.skills_url, headers=header, json=json, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure_testit_step('Получаем количество Знаний или Навыков')
    def return_len_skills_and_knowledge(self):
        return len(self.get_all_skills_and_knowledge_api().json())
