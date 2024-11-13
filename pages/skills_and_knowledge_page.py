import time

import allure
import testit
from selenium.webdriver import Keys

from locators.skills_and_knowledge_page_locators import SkillsAndKnowledgePageLocators
from pages.base_page import BasePage
from utils.concat_testit_allure_step import allure_testit_step


class SkillsAndKnowledgePage(BasePage):
    locators = SkillsAndKnowledgePageLocators()

    @allure_testit_step('Переход на справочник Знания и навыки')
    def go_to_skills_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.REFERENCE_BOOKS).click()
        self.element_is_visible(self.locators.SKILLS_TAB).click()

    @allure_testit_step('Проверка наличия кнопки Добавить')
    def check_add_skills_button(self):
        assert self.element_is_displayed(self.locators.ADD_SKILLS_BUTTON), 'Нет кнопки Добавить'

    @allure_testit_step('Проверка заголовков столбцов таблицы')
    def check_columns_headers(self):
        time.sleep(2)
        headers_text = [element.text for element in self.elements_are_visible(self.locators.COLUMN_TITLES)]
        headers_text.append(self.element_is_visible(self.locators.COLUMN_ACTION_TITLE).text)
        assert headers_text == ['Название', 'Тип', 'Описание', 'Действия'], 'Заголовки столбцов таблицы не корректны'

    @allure_testit_step('Проверка пунктов кебаб меню')
    def check_kebab_menu_item(self):
        time.sleep(1)
        self.elements_are_visible(self.locators.KEBAB_MENU)[0].click()
        menu_item = self.elements_are_visible(self.locators.KEBAB_MENU_ITEM)
        items_text = []
        for element in menu_item:
            items_text.append(element.text)
        assert items_text == ['Редактировать', 'Удалить'], 'В кебаб меню есть не все пункты'

