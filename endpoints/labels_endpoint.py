import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class LabelsEndpoint:
    response = None
    response_json = None

    @allure.step("Создаем метку")
    def put_label_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.put(url=Urls.labels_url, headers=header, json=json, verify=False)
        self.response_json = self.response.json()
        return self.response