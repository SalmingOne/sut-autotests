import time

import allure
import testit

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
        time.sleep(1)
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
