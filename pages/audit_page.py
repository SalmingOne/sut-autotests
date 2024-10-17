import time
import platform

import allure
import testit
from selenium.webdriver import Keys

from locators.audit_page_locators import AuditPageLocators
from pages.base_page import BasePage


class AuditPage(BasePage):
    locators = AuditPageLocators()

    @testit.step("Переход на страницу Аудит")
    @allure.step("Переход на страницу Аудит")
    def go_to_audit_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.AUDIT_PAGE).click()

    @testit.step("Проверка заголовков столбцов")
    @allure.step("Проверка заголовков столбцов")
    def check_columns_headers(self):
        time.sleep(2)
        columns_headers = self.elements_are_visible(self.locators.AUDIT_TAB_COLUMN_TITLES)
        headers_text = []
        for element in columns_headers:
            headers_text.append(element.text)
        assert headers_text == ['Событие', 'Дата', 'Проект', 'Предыдущее значение', 'Новое значение', 'Пользователь',
                                'Ссылка', 'Системная роль', 'Инициатор', 'Устройство', 'IP', 'Статус', 'Уровень',
                                'Текст ошибки'], 'В таблице есть не все столбцы'

    @testit.step("Проверка кнопки сбросить все")
    @allure.step("Проверка кнопки сбросить все")
    def check_reset_all_button(self):
        assert self.element_is_displayed(self.locators.RESET_ALL_BUTTON), 'Нет кнопки сбросить все'

    @testit.step("Выбор интервала дат через датапикер")
    @allure.step("Выбор интервала дат через датапикер")
    def select_day_interval_in_datepicker(self, start_day, end_day):
        self.elements_are_visible(self.locators.FILTER_BUTTONS)[1].click()
        self.elements_are_visible(self.locators.DATETIMEPICKERS_ICONS)[0].click()
        self.element_is_visible(self.locators.get_day_by_number(start_day)).click()
        self.elements_are_visible(self.locators.DATETIMEPICKERS_ICONS)[1].click()
        if self.element_is_clickable(self.locators.get_day_by_number(end_day)):
            self.element_is_visible(self.locators.get_day_by_number(end_day)).click()
            return True
        return False

    @testit.step("Очистить поле")
    @allure.step("Очистить поле")
    def clear_date_field(self, field):
        field.click()
        if platform.system() == 'Windows':
            field.send_keys(Keys.CONTROL + 'a')
        else:
            field.send_keys(Keys.COMMAND + 'a')
        field.send_keys(Keys.BACK_SPACE)

    @testit.step("Ввести интервал дат вручную")
    @allure.step("Ввести интервал дат вручную")
    def input_date_manually(self, start_date, end_date):
        start_date_field = self.elements_are_visible(self.locators.DATE_FIELDS)[0]
        end_date_field = self.elements_are_visible(self.locators.DATE_FIELDS)[1]
        self.clear_date_field(start_date_field)
        self.clear_date_field(end_date_field)
        start_date_field.send_keys(start_date)
        end_date_field.send_keys(end_date)
        start_date_field_status = start_date_field.get_attribute('aria-invalid') == 'true'
        end_date_field_status = end_date_field.get_attribute('aria-invalid') == 'true'
        return start_date_field_status, end_date_field_status
