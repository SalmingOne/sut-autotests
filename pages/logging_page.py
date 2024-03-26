import time

import allure
import testit
from selenium.webdriver import Keys

from locators.logging_page_locators import LoggingPageLocators
from pages.base_page import BasePage


class LoggingPage(BasePage):
    locators = LoggingPageLocators()

    @testit.step("Переход на страницу логирования")
    @allure.step("Переход на страницу логирования")
    def go_to_audit_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_AUDIT_TAB).click()

    @testit.step("Изменение настроек логирования")
    @allure.step("Изменение настроек логирования")
    def change_audit_setting(self, status=None, level=None, depth=None):
        time.sleep(0.5)  # Без ожидания не успевает прогрузиться страница
        self.element_is_visible(self.locators.AUDIT_STATUS_FIELD).click()
        self.element_is_visible(self.locators.set_choice(status)).click()
        self.element_is_visible(self.locators.AUDIT_LEVEL_FIELD).click()
        self.element_is_visible(self.locators.set_choice(level)).click()
        self.element_is_visible(self.locators.DEPTH_DATE_QUANTITY_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.DEPTH_DATE_QUANTITY_FIELD).send_keys('1')
        self.element_is_visible(self.locators.DEPTH_DATE_TYPE_FIELD).click()
        self.element_is_visible(self.locators.set_choice(depth)).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Получение текста модального окна")
    @allure.step("Получение текста модального окна")
    def get_modal_window(self):
        return self.element_is_visible(self.locators.DIALOG_TEXT).text

    @testit.step("Проверка кнопки отмены модального окна")
    @allure.step("Проверка кнопки отмены модального окна")
    def check_modal_abort_button(self):
        assert self.element_is_displayed(self.locators.DIALOG_ABORT_BUTTON)

    @testit.step("Подтверждение изменений в модальном окне")
    @allure.step("Подтверждение изменений в модальном окне")
    def submit_modal_dialog(self):
        self.element_is_visible(self.locators.DIALOG_SUBMIT_BUTTON).click()

    @testit.step("Получение текста сообщения системы")
    @allure.step("Получение текста сообщения системы")
    def get_alert_text(self):
        return self.element_is_visible(self.locators.ALERT_TEXT).text

    @testit.step("Проверка наличия пункта меню Аудит")
    @allure.step("Проверка наличия пункта меню Аудит")
    def check_audit_menu_item(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        return self.element_is_displayed(self.locators.AUDIT_PAGE, 1)

    @testit.step("Выключение логирования")
    @allure.step("Выключение логирования")
    def disabling_logging(self):
        time.sleep(0.5)  # Без ожидания не успевает прогрузиться страница
        self.element_is_visible(self.locators.AUDIT_STATUS_FIELD).click()
        self.element_is_visible(self.locators.set_choice('Выкл')).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
