import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint
from utils.concat_testit_allure_step import allure_testit_step


class SlotsEndpoint:
    response = None
    response_json = None

    @allure_testit_step("Создание слота на проекте")
    def create_slot(self, project_id, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(Urls.slots_url + f'?projectId={project_id}', json=json, headers=header, verify=False)
        return self.response
