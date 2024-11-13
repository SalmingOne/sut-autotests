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

    @allure_testit_step('Проверка наличия знания или навыка')
    def check_skill_name_on_page(self, name):
        return self.element_is_displayed(self.locators.skill_name_on_page(name))

    @allure_testit_step('Проверка полей дровера добавления знания или навыка')
    def check_drawer_fields(self):
        assert self.element_is_displayed(self.locators.text_on_page('Добавление навыка/знания'))
        name_error = self.check_max_field_length(
            self.locators.NAME_FIELD,
            64,
            self.locators.text_on_page('Добавление навыка/знания')
        )
        assert name_error == 'Превышено допустимое количество символов: 64', "Не соблюдена максимальная длина поля Имя"
        self.element_is_visible(self.locators.TYPE_FIELD).click()
        menu_items = [item.text for item in self.elements_are_visible(self.locators.LI_MENU_ITEM)]
        assert menu_items == ['Навык', 'Знание'], "В дропдауне Тип доступны не все значения"
        name_error = self.check_max_field_length(
            self.locators.DESCRIPTION_FIELD,
            1000,
            self.locators.text_on_page('Добавление навыка/знания')
        )
        assert name_error == 'Превышено допустимое количество символов: 1000', \
            "Не соблюдена максимальная длина поля Описание"
        assert self.element_is_displayed(self.locators.SUBMIT_BUTTON), "Отсутствует кнопка Добавить"
        assert self.element_is_displayed(self.locators.BREAK_BUTTON), "Отсутствует кнопка Отменить"

    @allure_testit_step('Проверка максимальной длины поля')
    def check_max_field_length(self, locator, max_length, locator_to_click):
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys('A' * (max_length + 1))
        self.element_is_visible(locator_to_click).click()
        error = self.element_is_visible(self.locators.MUI_ERROR).text
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys('AAA')
        self.element_is_visible(locator_to_click).click()
        return error

    @allure_testit_step('Нажатие кнопки добавления знания или навыка')
    def press_add_skill_button(self):
        time.sleep(0.5)
        self.element_is_visible(self.locators.ADD_SKILLS_BUTTON).click()

    @allure_testit_step('Нажатие кнопки Добавить')
    def press_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @allure_testit_step('Получение имени и описания знания или навыка')
    def get_name_and_description_values(self):
        name = self.element_is_visible(self.locators.NAME_FIELD).get_attribute('value')
        description = self.element_is_visible(self.locators.DESCRIPTION_FIELD).get_attribute('value')
        return [name, description]



