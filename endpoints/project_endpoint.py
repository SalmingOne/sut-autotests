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
        self.response = requests.post(url=Urls.project_url, headers=header, json=json, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаляем проект")
    def delete_project_api(self, project_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.project_url + project_id, headers=header, verify=False)
        assert self.response.status_code == 204
        return self.response

    @allure.step("Получаем все проекты")
    def get_all_project(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.project_url, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получаем проект по имени")
    def get_project_id_by_name(self, name):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.project_url, headers=header, verify=False)
        self.response_json = self.response.json()
        for project in self.response_json:
            if project['name'] == name:
                return project['id']

    @allure.step("Удаление проекта по имени")
    def delete_project_by_name_api(self, name):
        project_id = self.get_project_id_by_name(name)
        self.delete_project_api(str(project_id))

    @allure.step("Получаем дату старта проекта по имени")
    def get_project_start_date_by_name(self, name):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.project_url, headers=header, verify=False)
        self.response_json = self.response.json()
        for project in self.response_json:
            if project['name'] == name:
                return project['startDate']

    @allure.step("Получаем все имена проектов на которые назначен пользователь")
    def get_project_name_for_current_user(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.project_for_current_user_url, headers=header, verify=False)
        self.response_json = self.response.json()
        project_names = []
        for project in self.response_json:
            project_names.append(project['name'])
        return project_names

    @allure.step("Получаем два списка с проектами с самостоятельным добавлением и без")
    def get_name_projects_with_adding_himself_and_no_adding(self):
        all_projects_json = self.get_all_project().json()
        adding_himself = []
        no_adding_himself = []
        for project in all_projects_json:
            if project['selfAdding'] is True:
                adding_himself.append(project["name"])
            else:
                no_adding_himself.append(project["name"])
        return adding_himself, no_adding_himself

    @allure.step("Проверяем наличие проекта")
    def check_project_by_id(self, project_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.project_url + project_id, headers=header, verify=False)
        self.response_json = self.response.json()
        if self.response.status_code == 200:
            return True
        else:
            return False

    @allure.step("Удаление проекта если он существует")
    def delete_project_if_it_exist(self, project_name):
        if self.get_project_id_by_name(project_name) is None:
            pass
        else:
            self.delete_project_by_name_api(project_name)