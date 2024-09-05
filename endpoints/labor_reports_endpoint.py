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
        self.response = requests.post(url=Urls.labor_reports_url, headers=header, json=json, verify=False)
        return self.response

    @allure.step("Получаем трудозатраты проекта")
    def get_labor_reports_by_project_api(self, project_id, start_date, end_date):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.get(
            url=Urls.labor_reports_url + project_id + f'?startDate={start_date}&endDate={end_date}',
            headers=header,
            verify=False)
        labor_ids = []
        for a in self.response.json()["laborReports"]:
            labor_ids.append(a["id"])
        return labor_ids

    @allure.step("Изменение трудозатрат")
    def put_labor_reports(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.put(url=Urls.labor_reports_url, headers=header, json=json, verify=False)
        return self.response
