import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint
from utils.concat_testit_allure_step import allure_testit_step


class StatementFilesEndpoint:
    response = None
    response_json = None

    @allure_testit_step('Получение всех файлов заявлений')
    def get_all_statement_files(self):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(url=Urls.statement_files_url, headers=header, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure_testit_step('Получение всех типов заявлений в системе')
    def get_all_statement_files_types(self):
        return [element['type'] for element in self.get_all_statement_files().json()]

    @allure_testit_step('Добавление заявления')
    def post_statement_file(self, file_id, file_type):
        header = AuthEndpoint().get_header_token_api()
        payload = dict(fileIds=[file_id],
                       type=file_type)
        self.response = requests.post(url=Urls.statement_files_url, headers=header, json=payload, verify=False)
        self.response_json = self.response.json()
        return self.response
