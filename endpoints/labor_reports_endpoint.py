import allure
import requests

from data.urls import Urls

from endpoints.auth_endpoint import AuthEndpoint


class LaborReportEndpoint:
    response = None
    response_json = None

    @allure.step("Списываем трудозатраты")
    def post_labor_report_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.labor_reports_url, headers=header, json=json)
        return self.response
