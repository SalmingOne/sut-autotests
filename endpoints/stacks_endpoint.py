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

    @allure_testit_step("Получение стека по id")
    def get_stack_by_id(self, stack_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.stacks_url + stack_id, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure_testit_step("Удаление стека по id если он существует")
    def delete_stack_if_it_exist(self, stack_id):
        if self.get_stack_by_id(str(stack_id)).status_code == 404:
            pass
        else:
            self.delete_stacks_api(str(stack_id))