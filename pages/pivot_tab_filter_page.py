import random

import allure
import testit

from locators.pivot_tab_filter_locators import PivotTabFilterPageLocators
from pages.base_page import BasePage


class PivotTabFilterPage(BasePage):
    locators = PivotTabFilterPageLocators()

    @testit.step("Берем текст с разных элементов")
    @allure.step("Берем текст с разных элементов")
    def get_element_text(self, element):
        if element == 'checked':
            element_list = self.elements_are_visible(self.locators.CHECKED_ELEMENTS_TEXT)
        elif element == 'all':
            element_list = self.elements_are_visible(self.locators.ALL_CHECKBOXES_AND_RADIOBUTTON_TEXT)
        elif element == 'dropdown':
            element_list = self.elements_are_visible(self.locators.ELEMENTS_DROPDOWN_TEXT)
        data = []
        for element in element_list:
            self.go_to_element(element)
            data.append(element.text)
        return data

    @testit.step("Выбираем случайные чек-боксы и радиокнопки")
    @allure.step("Выбираем случайные чек-боксы и радиокнопки")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ALL_CHECKBOXES_AND_RADIOBUTTON)
        for i in range(1, 6):
            item = item_list[random.randint(1, 11)]
            self.go_to_element(item)
            item.click()

    @testit.step("Нажимаем кнопку сбросить все")
    @allure.step("Нажимаем кнопку сбросить все")
    def click_reset_button(self):
        self.element_is_visible(self.locators.RESET_ALL_BUTTON).click()

    @testit.step("Раскрываем дропдаун филиалов")
    @allure.step("Раскрываем дропдаун филиалов")
    def open_filial_dropdown(self):
        self.element_is_visible(self.locators.OPEN_FILIAL_DROPDOWN).click()

    @testit.step("Раскрываем дропдаун интеграций")
    @allure.step("Раскрываем дропдаун интеграций")
    def open_integration_dropdown(self):
        self.element_is_visible(self.locators.INTEGRATION_CHECKBOX).click()
        self.element_is_visible(self.locators.OPEN_INTEGRATION_DROPDOWN).click()

    @testit.step("Нажатие кнопки сохранить")
    @allure.step("Нажатие кнопки сохранить")
    def press_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
