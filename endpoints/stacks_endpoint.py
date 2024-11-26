import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint
from utils.concat_testit_allure_step import allure_testit_step


class StacksEndpoint:
    response = None
    response_json = None

    @allure_testit_step("Создание стека")
    def create_stacks_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(Urls.stacks_url, json=json, headers=header, verify=False)
        return self.response

    @allure_testit_step("Удаление стека")
    def delete_stacks_api(self, stack_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.stacks_url + stack_id, headers=header, verify=False)
        assert self.response.status_code == 200
        return self.response
