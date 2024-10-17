import allure
import requests

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class CalendarEndpoint:
    response = None
    response_json = None

    @allure.step("Создание дня для справочника праздничных дней")
    def create_holiday_api(self, json):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.post(url=Urls.calendar_url + 'holidays', headers=header, json=json, verify=False)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Удаление дня из справочника праздничных дней")
    def delete_holiday_api(self, calendar_id):
        header = AuthEndpoint().get_header_token_api()
        self.response = requests.delete(url=Urls.calendar_url + calendar_id, headers=header, verify=False)
        assert self.response.status_code == 204
        return self.response