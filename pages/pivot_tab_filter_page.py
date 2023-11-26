import random

import allure
from locators.pivot_tab_filter_locators import PivotTabFilterPageLocators
from pages.base_page import BasePage


class PivotTabFilterPage(BasePage):
    locators = PivotTabFilterPageLocators()

    # Берем имена с выбранных чек-боксов и радио-кнопок
    @allure.step("Берем имена с выбранных чек-боксов и радио-кнопок")
    def get_checked_element_text(self):
        checked_element_list = self.elements_are_visible(self.locators.CHECKED_ELEMENTS_TEXT)
        data = []
        for element in checked_element_list:
            data.append(element.text)
        return data

    # Выбираем случайные чек-боксы и радиокнопки
    @allure.step("Выбираем случайные чек-боксы и радиокнопки")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ALL_CHECKBOXES_AND_RADIOBUTTON)
        count = 5
        while count != 0:
            item = item_list[random.randint(1, 11)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    # Нажимаем кнопку сбросить все
    @allure.step("Нажимаем кнопку сбросить все")
    def click_reset_button(self):
        self.element_is_visible(self.locators.RESET_ALL_BUTTON).click()
