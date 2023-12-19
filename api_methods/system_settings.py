import requests
import allure
from configuration.config_provider import ConfigProvider
from api_methods.auth import AuthApi
import enum

config = ConfigProvider()


class SystemSettingsApi:

    def __init__(self):
        auth = AuthApi()
        auth.auth()

    @allure.step('Включить чекбокс "Обязательно указание причин переработок"')
    def turn_on_required_overwork_reason(self):
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.required_overtime_reason.value,
                            headers=config.get_token_as_dict_for_headers(),
                            json={'enabled': True})

    @allure.step('Выключить чекбокс "Обязательно указание причин переработок"')
    def turn_off_required_overwork_reason(self):
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.required_overtime_reason.value,
                            headers=config.get_token_as_dict_for_headers(),
                            json={'enabled': False})

    @allure.step('Включить чекбокс "Показывать режим обучения для новых сотрудников"')
    def turn_on_show_onboarding(self):
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.showing_onboarding.value,
                            headers=config.get_token_as_dict_for_headers(),
                            json={'enabled': True})

    @allure.step('Выключить чекбокс "Показывать режим обучения для новых сотрудников"')
    def turn_off_show_onboarding(self):
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.showing_onboarding.value,
                            headers=config.get_token_as_dict_for_headers(),
                            json={'enabled': False})

    @allure.step('Включить чекбокс "Отправлять оповещения системы на почту"')
    def turn_on_notifications(self):
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.sending_notifications.value,
                            headers=config.get_token_as_dict_for_headers(),
                            json={'enabled': True})

    @allure.step('Выключить чекбокс "Отправлять оповещения системы на почту"')
    def turn_off_notifications(self):
        return requests.put(url=config.get_system_settings_url() + SystemSettingsNames.sending_notifications.value,
                            headers=config.get_token_as_dict_for_headers(),
                            json={'enabled': False})


class SystemSettingsNames(enum.Enum):
    required_overtime_reason = 'OvertimeReason'
    showing_onboarding = 'ShowOnboarding'
    sending_notifications = 'SendNotifications'
