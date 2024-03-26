import time

import allure
import testit

from locators.skills_page_locators import SkillsPageLocators
from pages.base_page import BasePage


class SkillsPage(BasePage):
    locators = SkillsPageLocators()

    @testit.step("Переход на справочник Знания")
    @allure.step("Переход на справочник Знания")
    def go_to_skills_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.REFERENCE_BOOKS).click()
        self.element_is_visible(self.locators.SKILLS_TAB).click()

    @testit.step("Проверка кнопки добавить знание")
    @allure.step("Проверка кнопки добавить знание")
    def check_add_skills_button(self):
        assert self.element_is_displayed(self.locators.ADD_SKILLS_BUTTON), 'Нет кнопки проверить знания'

    @testit.step("Проверка заголовков столбцов таблицы")
    @allure.step("Проверка заголовков столбцов таблицы")
    def check_columns_headers(self):
        time.sleep(1)
        columns_headers = self.elements_are_visible(self.locators.AUDIT_TAB_COLUMN_TITLES)
        headers_text = []
        for element in columns_headers:
            headers_text.append(element.text)
        assert headers_text == ['Знания', 'Группы знаний', 'Действия'], 'В таблице есть не все столбцы'

    @testit.step("Проверка пунктов кебаб меню")
    @allure.step("Проверка пунктов кебаб меню")
    def check_kebab_menu_item(self):
        time.sleep(1)
        self.elements_are_visible(self.locators.KEBAB_MENU)[0].click()
        menu_item = self.elements_are_visible(self.locators.KEBAB_MENU_ITEM)
        items_text = []
        for element in menu_item:
            items_text.append(element.text)
        assert items_text == ['Редактировать', 'Удалить'], 'В кебаб меню есть не все пункты'
