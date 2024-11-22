import allure
import requests
import testit

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class SkillsEndpoint:
    response = None
    response_json = None

    @allure.step("Получаем все Знания")
    def get_all_skills_api(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.skills_url, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Создаем Знание")
    def create_skills_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.skills_url, headers=header, json=json, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получаем количество Знаний")
    def return_len_skills(self):
        return len(self.get_all_skills_api().json())

    @allure.step("Удаляем Знание")
    def delete_skill_api(self, skill_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.skills_url + skill_id, headers=header, verify=False)
        assert self.response.status_code == 204
        return self.response

    @allure.step("Получение id знания по имени")
    def get_skill_id_by_name_api(self, name):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.skills_url, headers=header, verify=False)
        self.response_json = self.response.json()
        for skill in self.response_json:
            if skill['name'] == name:
                return skill['id']

    @allure.step("Удаление знания по имени")
    def delete_skill_by_name_api(self, name):
        skill_id = self.get_skill_id_by_name_api(name)
        self.delete_skill_api(str(skill_id))

    @allure.step("Проверка наличия знания")
    def check_skill_by_id(self, skill_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.skills_url + skill_id, headers=header, verify=False)
        if self.response.status_code == 200:
            return True
        else:
            return False

    @allure.step("Получение списка всех знаний")
    def get_all_skills_name_api(self):
        return [item['name'] for item in self.get_all_skills_api().json()]