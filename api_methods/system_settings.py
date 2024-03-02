import requests
import allure
from configuration.config_provider import ConfigProvider
from api_methods.auth import AuthApi
import enum

config = ConfigProvider()


class SystemSettingsApi:

    @allure.step('Включить чекбокс "Обязательно указание причин переработок"')
    def turn_on_required_overwork_reason(self):
        token = AuthApi().auth_to_token()
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.required_overtime_reason.value,
                            headers={"Access": "Bearer " + token},
                            json={'enabled': True})

    @allure.step('Выключить чекбокс "Обязательно указание причин переработок"')
    def turn_off_required_overwork_reason(self):
        token = AuthApi().auth_to_token()
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.required_overtime_reason.value,
                            headers={"Access": "Bearer " + token},
                            json={'enabled': False})

    @allure.step('Включить чекбокс "Показывать режим обучения для новых сотрудников"')
    def turn_on_show_onboarding(self):
        token = AuthApi().auth_to_token()
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.showing_onboarding.value,
                            headers={"Access": "Bearer " + token},
                            json={'enabled': True})

    @allure.step('Выключить чекбокс "Показывать режим обучения для новых сотрудников"')
    def turn_off_show_onboarding(self):
        token = AuthApi().auth_to_token()
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.showing_onboarding.value,
                            headers={"Access": "Bearer " + token},
                            json={'enabled': False})

    @allure.step('Включить чекбокс "Отправлять оповещения системы на почту"')
    def turn_on_notifications(self):
        token = AuthApi().auth_to_token()
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.sending_notifications.value,
                            headers={"Access": "Bearer " + token},
                            json={'enabled': True})

    @allure.step('Выключить чекбокс "Отправлять оповещения системы на почту"')
    def turn_off_notifications(self):
        token = AuthApi().auth_to_token()
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.sending_notifications.value,
                            headers={"Access": "Bearer " + token},
                            json={'enabled': False})


class SystemSettingsNames(enum.Enum):
    required_overtime_reason = 'OvertimeReason'
    showing_onboarding = 'ShowOnboarding'
    sending_notifications = 'SendNotifications'
