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

    @allure_testit_step("Удаление знания или навыка")
    def delete_skills_and_knowledge_api(self, skill_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.skills_del_url + skill_id, headers=header, verify=False)
        assert self.response.status_code == 200
        return self.response

    @allure_testit_step("Получение id знания или навыка по имени")
    def get_skills_and_knowledge_id_by_name_api(self, name):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.skills_url, headers=header, verify=False)
        self.response_json = self.response.json()
        for skill in self.response_json:
            if skill['name'] == name:
                return skill['id']

    @allure_testit_step("Удаление знания или навыка по имени")
    def delete_skills_and_knowledge_by_name_api(self, name):
        skill_id = self.get_skills_and_knowledge_id_by_name_api(name)
        self.delete_skills_and_knowledge_api(str(skill_id))
