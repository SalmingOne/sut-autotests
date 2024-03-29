import time

import allure
import testit

from locators.advanced_search_page_locators import AdvancedSearchPageLocators
from pages.base_page import BasePage


class AdvancedSearchPage(BasePage):
    locators = AdvancedSearchPageLocators()

    @testit.step("Переход на страницу расширенного поиска")
    @allure.step("Переход на страницу расширенного поиска")
    def go_advanced_search_page(self):
        self.element_is_visible(self.locators.COLLEAGUES_TAB).click()
        self.element_is_visible(self.locators.ALL_COLLEAGUES).click()
        time.sleep(1)
        self.element_is_visible(self.locators.TO_ADVANCED_SEARCH_BUTTON).click()

    @testit.step("Создание расширенного поиска")
    @allure.step("Создание расширенного поиска")
    def create_new_search(self):
        self.element_is_visible(self.locators.NEW_SEARCH_BUTTON).click()
        self.elements_are_visible(self.locators.OPEN_BUTTONS)[0].click()
        criterion_value = self.elements_are_visible(self.locators.LI_MENU_ITEM)[1].text
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[1].click()

        self.elements_are_visible(self.locators.OPEN_BUTTONS)[1].click()
        operator_value = self.elements_are_visible(self.locators.LI_MENU_ITEM)[1].text
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[1].click()
        time.sleep(1)
        self.elements_are_visible(self.locators.OPEN_BUTTONS)[2].click()
        condition_value = self.elements_are_visible(self.locators.LI_MENU_ITEM)[1].text
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[1].click()

        self.element_is_visible(self.locators.SAVE_SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.SEARCH_NAME_FIELD).send_keys('Авто-поиск')
        self.element_is_visible(self.locators.CHECK_ICON).click()
        return 'Авто-поиск', criterion_value, operator_value, condition_value[:-4]

    @testit.step("Получение названий сохраненных поисков")
    @allure.step("Получение названий сохраненных поисков")
    def get_search_chips_names(self):
        time.sleep(1)
        all_chips = self.elements_are_visible(self.locators.SEARCH_CHIPS)
        names = []
        for chips in all_chips:
            names.append(chips.text)
        return names

    @testit.step("Проверка тултипа")
    @allure.step("Проверка тултипа")
    def check_tooltip(self, name):
        self.action_move_to_element(self.element_is_visible(self.locators.chips_by_name(name)))
        tooltip_text = self.element_is_visible(self.locators.TOOLTIP).text
        assert name in tooltip_text, "В тултипе нет полного имени поиска"

    @testit.step("Удаление сохраненного поиска")
    @allure.step("Удаление сохраненного поиска")
    def get_chips_values_and_delete_search_chips(self, name):
        self.action_double_click(self.element_is_visible(self.locators.chips_by_name(name)))
        fields = self.elements_are_visible(self.locators.ALL_FIELDS)
        values = []
        for field in fields:
            values.append(field.get_attribute('value'))
        self.element_is_visible(self.locators.DELETE_SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)
        return values

