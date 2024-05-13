import requests
import allure

import enum

from data.urls import Urls
from endpoints.auth_endpoint import AuthEndpoint


class SystemSettingsApi:

    @allure.step('Включить чекбокс "Обязательно указание причин переработок"')
    def turn_on_required_overwork_reason(self):
        header = AuthEndpoint().get_header_token_api()
        return requests.put(url=Urls.system_settings_url + SystemSettingsNames.required_overtime_reason.value,
                            headers=header,
                            json={'enabled': True})

    @allure.step('Выключить чекбокс "Обязательно указание причин переработок"')
    def turn_off_required_overwork_reason(self):
        header = AuthEndpoint().get_header_token_api()
        return requests.put(url=Urls.system_settings_url + SystemSettingsNames.required_overtime_reason.value,
                            headers=header,
                            json={'enabled': False})

    @allure.step('Включить чекбокс "Показывать режим обучения для новых сотрудников"')
    def turn_on_show_onboarding(self):
        header = AuthEndpoint().get_header_token_api()
        return requests.put(url=Urls.system_settings_url + SystemSettingsNames.showing_onboarding.value,
                            headers=header,
                            json={'enabled': True})

    @allure.step('Выключить чекбокс "Показывать режим обучения для новых сотрудников"')
    def turn_off_show_onboarding(self):
        header = AuthEndpoint().get_header_token_api()
        return requests.put(url=Urls.system_settings_url + SystemSettingsNames.showing_onboarding.value,
                            headers=header,
                            json={'enabled': False})

    @allure.step('Включить чекбокс "Отправлять оповещения системы на почту"')
    def turn_on_notifications(self):
        header = AuthEndpoint().get_header_token_api()
        return requests.put(url=Urls.system_settings_url + SystemSettingsNames.sending_notifications.value,
                            headers=header,
                            json={'enabled': True})

    @allure.step('Выключить чекбокс "Отправлять оповещения системы на почту"')
    def turn_off_notifications(self):
        header = AuthEndpoint().get_header_token_api()
        return requests.put(url=Urls.system_settings_url + SystemSettingsNames.sending_notifications.value,
                            headers=header,
                            json={'enabled': False})


class SystemSettingsNames(enum.Enum):
    required_overtime_reason = 'OvertimeReason'
    showing_onboarding = 'ShowOnboarding'
    sending_notifications = 'SendNotifications'
