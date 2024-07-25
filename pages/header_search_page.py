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

    @testit.step("Проверка сообщения Ничего не найдено")
    @allure.step("Проверка сообщения Ничего не найдено")
    def check_nothing_found_text(self):
        self.element_is_visible(self.locators.SEARCH_HEADER_FIELD).send_keys('ацывжы')
        assert self.element_is_visible(self.locators.NOTHING_FOUND_TEXT).text == 'Ничего не найдено', "Не появилось сообщение"

    @testit.step("Ввод пробела в поле поиска")
    @allure.step("Ввод пробела в поле поиска")
    def entering_a_space_in_the_header_search(self):
        self.element_is_visible(self.locators.SEARCH_HEADER_FIELD).send_keys(' ')


