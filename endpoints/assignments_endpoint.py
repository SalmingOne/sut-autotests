import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class AssignmentEndpoint:
    response = None
    response_json = None

    @allure.step("Создаем назначение")
    def create_assignment_api(self, json):
        header = AuthEndpoint.get_header_token_api()
        self.response = requests.post(url=Urls.assignment_url, headers=header, json=json)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаляем назначение")
    def delete_assignment_api(self, assignment_id):
        header = AuthEndpoint.get_header_token_api()
        self.response = requests.delete(url=Urls.assignment_url + assignment_id, headers=header)
        self.response_json = self.response.json()
        assert self.response.status_code == 200
        return self.response

    @allure.step("Изменяем назначение")
    def put_assignment_api(self, json, assignment_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.put(url=Urls.assignment_url + f'{assignment_id}', headers=header, json=json)
        self.response_json = self.response.json()
        return self.response