import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class ResumeEndpoint:
    response = None
    response_json = None

    @allure.step("Создаем резюме")
    def create_resume_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.resume_url, headers=header, json=json)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаляем резюме")
    def delete_resume_api(self, resume_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.resume_url + resume_id, headers=header)
        assert self.response.status_code == 204
        return self.response
