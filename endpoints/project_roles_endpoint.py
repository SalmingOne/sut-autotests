import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class ProjectRolesEndpoint:
    response = None
    response_json = None

    @allure.step("Получаем все проектные роли")
    def get_all_project_roles(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.project_role_url, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получаем id всех проектных ролей")
    def get_all_project_roles_id(self):
        all_get_all_project_roles = self.get_all_project_roles().json()
        get_all_project_roles_id = []
        for role in all_get_all_project_roles:
            get_all_project_roles_id.append(role['id'])
        return get_all_project_roles_id

    @allure.step("Получаем названия всех проектных ролей")
    def get_all_project_roles_name(self):
        all_get_all_project_roles = self.get_all_project_roles().json()
        get_all_project_roles_name = []
        for role in all_get_all_project_roles:
            get_all_project_roles_name.append(role['name'])
        return get_all_project_roles_name

    @allure.step("Получаем данные о дате создания и обновления проектной роли")
    def get_info_about_project_role_dates(self, project_role_id):
        all_get_all_project_roles = self.get_all_project_roles().json()
        for role in all_get_all_project_roles:
            if role['id'] == project_role_id:
                data_list = [role['createdAt'], role['updatedAt']]
                return data_list

    @allure.step("Получаем название проектной роли по id")
    def get_name_project_role_by_id(self, project_role_id):
        all_get_all_project_roles = self.get_all_project_roles().json()
        for role in all_get_all_project_roles:
            if role['id'] == project_role_id:
                return role['name']