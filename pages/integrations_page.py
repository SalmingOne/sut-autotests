import time

import allure
import testit

from locators.integrations_page_locators import IntegrationsPageLocators
from pages.base_page import BasePage


class IntegrationsPage(BasePage):
    locators = IntegrationsPageLocators()

    @testit.step("Переход на страницу интеграций")
    @allure.step("Переход на страницу интеграций")
    def go_to_integrations_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.INTEGRATIONS_PAGE).click()

    @testit.step("Удаление всех интеграций jira")
    @allure.step("Удаление всех интеграций jira")
    def delete_all_jira_integration(self):
        if not self.element_is_clickable(self.locators.DELETE_ALL_JIRA_INTEGRATION, 1):
            pass
        else:
            self.element_is_visible(self.locators.DELETE_ALL_JIRA_INTEGRATION).click()
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Добавление интеграции jira")
    @allure.step("Добавление интеграции jira")
    def add_jira_integration(self, url, login, password):
        self.element_is_visible(self.locators.ADD_JIRA_INTEGRATION_BUTTON).click()
        self.element_is_visible(self.locators.URL_INPUT_FIELD).send_keys(url)
        self.element_is_visible(self.locators.LOGIN_INPUT_FIELD).send_keys(login)
        self.element_is_visible(self.locators.PASSWORD_INPUT_FIELD).send_keys(password)
        assert not self.element_is_clickable(self.locators.ADD_INTEGRATION_ON_MODAL, 1),\
            "Кнопка добавить интеграцию на модальном окне кликабельна"
        self.element_is_visible(self.locators.CHECK_ICON).click()

    @testit.step("Получение сообщений системы")
    @allure.step("Получение сообщений системы")
    def get_alert_message(self):
        time.sleep(1)
        all_alerts = self.elements_are_visible(self.locators.ALERT_MESSAGE)
        data = []
        for alert in all_alerts:
            data.append(alert.text)
        return data

    @testit.step("Проверка наличия иконки удаления")
    @allure.step("Проверка наличия иконки удаления")
    def check_delete_icon_on_modal_window(self):
        assert self.element_is_displayed(self.locators.DELETE_BUTTON_ON_MODAL), "Иконка удаления интеграции отсутствует"

    @testit.step("Проверка наличия иконки редактирования")
    @allure.step("Проверка наличия иконки редактирования")
    def check_edit_icon_on_modal_window(self):
        assert self.element_is_displayed(self.locators.EDIT_BUTTON_ON_MODAL), "Иконка редактирования интеграции отсутствует"

    @testit.step("Проверка отсутствия иконки с функционалом сохранения интеграции")
    @allure.step("Проверка отсутствия иконки с функционалом сохранения интеграции")
    def check_check_icon_on_modal_window(self):
        assert not self.element_is_displayed(self.locators.CHECK_ICON), "Иконка с функционалом сохранения интеграции присутствует"
