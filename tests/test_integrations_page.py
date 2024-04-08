import os
import time

import allure
import pytest
import testit

from data.data import LOGIN, PASSWORD
from pages.integrations_page import IntegrationsPage


@allure.suite("Страница интеграций")
class TestIntegrationsPage:

    @testit.workItemIds(1001)
    @testit.displayName("12.1.1 Добавление не валидной интеграции")
    @pytest.mark.smoke
    @allure.title("id-1001 12.1.1 Добавление не валидной интеграции")
    def test_adding_not_valid_integration(self, login, driver):
        integration_page = IntegrationsPage(driver)
        integration_page.go_to_integrations_page()
        integration_page.delete_all_jira_integration()
        integration_page.add_jira_integration('https://jira.moskit.pro', LOGIN, PASSWORD)
        time.sleep(1)  # Необходимо время для прогрузки анимации
        message = integration_page.get_alert_message()
        time.sleep(1)  # Необходимо время для прогрузки анимации
        integration_page.check_check_icon_on_modal_window()
        integration_page.check_delete_icon_on_modal_window()
        integration_page.check_edit_icon_on_modal_window()
        assert 'Настройки интеграции сохранены. Интеграция не готова к использованию. Измените настройки интеграции.' in message, 'Нет сообщения о неготовности интеграции'

    @testit.workItemIds(1000)
    @testit.displayName("12.1.1 Добавление валидной интеграции")
    @pytest.mark.smoke
    @allure.title("id-1000 12.1.1 Добавление валидной интеграции")
    def test_adding_valid_integration(self, login, driver):
        integration_page = IntegrationsPage(driver)
        integration_page.go_to_integrations_page()
        integration_page.delete_all_jira_integration()
        integration_page.add_jira_integration('https://jira.moskit.pro',
                                              os.getenv('INTEGRATION_LOGIN'),
                                              os.getenv('INTEGRATION_PASSWORD'))
        time.sleep(1)  # Необходимо время для прогрузки анимации
        message = integration_page.get_alert_message()
        time.sleep(1)  # Необходимо время для прогрузки анимации
        integration_page.check_check_icon_on_modal_window()
        integration_page.check_delete_icon_on_modal_window()
        integration_page.check_edit_icon_on_modal_window()
        integration_page.delete_integration_from_modal()
        time.sleep(1)
        assert 'Настройки интеграции сохранены. Интеграция готова к использованию.' in message,\
            'Нет сообщения о готовности интеграции'

    @testit.workItemIds(994)
    @testit.displayName("12.1.1 Содержание подраздела Интеграции с интеграциями")
    @pytest.mark.smoke
    @allure.title("id-994 12.1.1 Содержание подраздела Интеграции с интеграциями")
    def test_contents_of_integrations_page(self, login, driver):
        integration_page = IntegrationsPage(driver)
        integration_page.go_to_integrations_page()
        integration_page.check_integration_titles()
        integration_page.check_delete_and_add_buttons()
        integration_page.check_edit_buttons()