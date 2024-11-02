import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint
from utils.concat_testit_allure_step import allure_testit_step


class PersonalQualityEndpoint:
    response = None
    response_json = None

    @allure_testit_step('Создание персонального качества')
    def create_personal_quality_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.personal_quality_url, headers=header, json=json, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure_testit_step('Удаление персонального качества')
    def delete_personal_quality_api(self, personal_quality_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.personal_quality_url + personal_quality_id, headers=header, verify=False)
        assert self.response.status_code == 204
        return self.response
