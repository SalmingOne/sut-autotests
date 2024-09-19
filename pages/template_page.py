import time
import os

import allure
import testit
from selenium.webdriver import Keys

from locators.template_locators import TemplatePageLocators
from pages.labor_cost_page import LaborCostPage
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

    @testit.step("Проверка что шаблон удален")
    @allure.step("Проверка что шаблон удален")
    def check_template_file_delete(self):
        assert self.element_is_not_visible(self.locators.check_text('шаблон.docx')), "Файл не удален"
        self.delete_file('шаблон.docx')