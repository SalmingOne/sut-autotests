import time

import allure
import testit
from selenium.webdriver import Keys

from locators.header_search_locators import HeaderSearchLocators
from pages.base_page import BasePage


class HeaderSearchPage(BasePage):
    locators = HeaderSearchLocators()

    @testit.step("Выбор поля Поиск в хедере")
    @allure.step("Выбор поля Поиск в хедере")
    def select_search_field_header(self):
        self.element_is_visible(self.locators.SEARCH_HEADER_FIELD).click()

    @testit.step("Проверка тултипа поля Поиск в хедере")
    @allure.step("Проверка тултипа поля Поиск в хедере")
    def check_tooltip_in_header_search(self):
        self.element_is_visible(self.locators.SEARCH_HEADER_FIELD).send_keys(Keys.RETURN)
        assert self.element_is_visible(self.locators.TOOLTIP).text == 'Введите значение для поиска', "Не появился тултип или его текст не корректен"


