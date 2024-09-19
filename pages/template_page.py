import time
import os

import allure
import testit
from selenium.webdriver import Keys
from selenium.common.exceptions import TimeoutException

from locators.template_locators import TemplatePageLocators
from pages.base_page import BasePage


class TemplatePage(BasePage):
    locators = TemplatePageLocators()

    @testit.step("Переход на страницу Шаблоны")
    @allure.step("Переход на страницу Шаблоны")
    def go_to_template_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM).click()
        self.element_is_visible(self.locators.TEMPLATE_TAB).click()

    @testit.step("Проверка что нет загруженных шаблонов")
    @allure.step("Проверка что нет загруженных шаблонов")
    def check_template_is_empty(self):
        while self.element_is_displayed(self.locators.DELETE_ICON):
            self.element_is_visible(self.locators.DELETE_ICON).click()
            time.sleep(1)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            time.sleep(1)
        else:
            pass

    @testit.step("Добавление файла")
    @allure.step("Добавление файла")
    def add_file(self, name, text):
        file = open(os.path.abspath(rf'../{name}'), 'w+')
        file.write(f'{text}')
        file.close()

    @testit.step("Удаление файла")
    @allure.step("Удаление файла")
    def delete_file(self, name):
        os.remove(rf'../{name}')

    @testit.step("Добавление шаблона в валидном формате")
    @allure.step("Добавление шаблона в валидном формате")
    def add_template_file(self):
        self.add_file('шаблон.docx', 'Шаблон')
        self.element_is_present(self.locators.ADD_DOC, 2).send_keys(os.path.abspath(r'../шаблон.docx'))

    @testit.step("Проверка что шаблон добавлен")
    @allure.step("Проверка что шаблон добавлен")
    def check_template_file(self):
        assert self.element_is_displayed(self.locators.check_text('шаблон.docx')), "Файл не добавился"
        self.delete_file('шаблон.docx')

    @testit.step("Создание переменной")
    @allure.step("Создание переменной")
    def add_variable(self, name, text):
        self.element_is_visible(self.locators.CREATE_VARIABLE).click()
        self.element_is_visible(self.locators.FIELD_NAME).send_keys(name)
        self.element_is_visible(self.locators.VARIABLE_NAME).send_keys(text)
        self.element_is_visible(self.locators.VARIABLE_VALUE).send_keys(text)
        self.element_is_visible(self.locators.TEMPLATE_WITH_VARIABLE).click()
        time.sleep(1)
        self.element_is_visible(self.locators.TEMPLATE_VALUE).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)

    @testit.step("Получить значение ячейки в столбце Шаблоны")
    @allure.step("Получить значение ячейки в столбце Шаблоны")
    def get_value_from_column_template(self, variable_name, column_number):
        try:
            self.element_is_visible(self.locators.get_value_from_column(variable_name, column_number))
            return self.element_is_visible(self.locators.get_value_from_column(variable_name, column_number)).text
        except TimeoutException:
            return 'Пусто'

    @testit.step("Проверка что шаблон удален")
    @allure.step("Проверка что шаблон удален")
    def check_template_file_delete(self):
        assert self.element_is_not_visible(self.locators.check_text('шаблон.docx')), "Файл не удален"
        self.delete_file('шаблон.docx')

    @testit.step("Удаление добавленной переменной")
    @allure.step("Удаление добавленной переменной")
    def delete_add_variable(self, variable_name, column_number):
        self.element_is_visible(self.locators.get_value_from_column(variable_name, column_number)).click()
        time.sleep(1)
        self.element_is_visible(self.locators.DELETE).click()
        time.sleep(1)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()