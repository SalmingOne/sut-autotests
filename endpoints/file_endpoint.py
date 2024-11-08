import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint
from utils.concat_testit_allure_step import allure_testit_step


class FilesEndpoint:
    response = None
    response_json = None

    @allure_testit_step('Загрузка файла')
    def post_file(self, files):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.files_application_template_url, headers=header, files=files, verify=False)
        self.response_json = self.response.json()
        return self.response
