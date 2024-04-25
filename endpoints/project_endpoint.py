import allure
import requests

from data.urls import Urls

from endpoints.auth_endpoint import AuthEndpoint


class ProjectEndpoint:
    response = None
    response_json = None

    @allure.step("Создаем проект")
    def create_project_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.project_url, headers=header, json=json)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаляем проект")
    def delete_project_api(self, project_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.project_url + project_id, headers=header)
        assert self.response.status_code == 204
        return self.response

    @allure.step("Получаем все проекты")
    def get_all_project(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.project_url, headers=header)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получаем проект по имени")
    def get_project_id_by_name(self, name):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.project_url, headers=header)
        self.response_json = self.response.json()
        for project in self.response_json:
            if project['name'] == name:
                return project['id']

    @allure.step("Удаление проекта по имени")
    def delete_project_by_name_api(self, name):
        project_id = self.get_project_id_by_name(name)
        self.delete_project_api(str(project_id))