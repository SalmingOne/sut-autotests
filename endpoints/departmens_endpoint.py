import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class DepartmentsEndpoint:
    response = None
    response_json = None

    @allure.step("Получаем все отделы")
    def get_all_departments(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.department_url, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получаем id всех отделов")
    def get_all_departments_id(self):
        all_departments = self.get_all_departments().json()
        departments_id = []
        for department in all_departments:
            departments_id.append(department['id'])
        return departments_id
