import time

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
        assert self.element_is_displayed(self.locators.text_on_page('Добавление навыка/знания')), \
            "Нет заголовка дровера добавления навыка/знания"
        name_error = self.check_max_field_length(
            self.locators.NAME_FIELD,
            64,
            self.locators.NAME_FIELD_COLOR,
            self.locators.text_on_page('Добавление навыка/знания'),
            'AAA'
        )
        assert name_error == 'Превышено допустимое количество символов: 64', "Не соблюдена максимальная длина поля Имя"
        self.element_is_visible(self.locators.TYPE_FIELD).click()
        menu_items = [item.text for item in self.elements_are_visible(self.locators.LI_MENU_ITEM)]
        assert menu_items == ['Навык', 'Знание'], "В дропдауне Тип доступны не все значения"
        name_error = self.check_max_field_length(
            self.locators.DESCRIPTION_FIELD,
            1000,
            self.locators.DESCRIPTION_FIELD_COLOR,
            self.locators.text_on_page('Добавление навыка/знания'),
            'AAA'
        )
        assert name_error == 'Превышено допустимое количество символов: 1000', \
            "Не соблюдена максимальная длина поля Описание"
        assert self.element_is_displayed(self.locators.SUBMIT_BUTTON), "Отсутствует кнопка Добавить"
        assert self.element_is_displayed(self.locators.BREAK_BUTTON), "Отсутствует кнопка Отменить"

    @allure_testit_step('Проверка максимальной длины поля')
    def check_max_field_length(self, locator, max_length, locator_to_color, locator_to_click, new_value):
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys('A' * (max_length + 1))
        self.element_is_visible(locator_to_click).click()
        error = self.element_is_visible(self.locators.MUI_ERROR).text
        name_field_color = self.element_is_present(locator_to_color).value_of_css_property('border-color')
        assert name_field_color == 'rgb(211, 47, 47)', "Цвет поля Название не красный"
        time.sleep(1)
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 2), \
            "Кнопка Добавить активна при не корректном заполнении поля"
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys(new_value)
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

    @allure_testit_step('Проверка ответа при не заполнении обязательных полей')
    def check_empty_mandatory_fields(self):
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 2), \
            "Кнопка Добавить активна до заполнения обязательных полей"
        # Поле Название
        self.element_is_visible(self.locators.NAME_FIELD).click()
        self.element_is_visible(self.locators.text_on_page('Добавление навыка/знания')).click()
        assert self.element_is_visible(self.locators.MUI_ERROR).text == 'Поле обязательно', \
            "Нет сообщения об обязательности поля Название"
        name_field_color = self.element_is_present(self.locators.NAME_FIELD_COLOR).value_of_css_property('border-color')
        assert name_field_color == 'rgb(211, 47, 47)', "Цвет поля Название не красный"
        self.element_is_visible(self.locators.NAME_FIELD).send_keys('Имя')
        # Кнопка добавить после заполнения обязательных полей
        self.element_is_visible(self.locators.text_on_page('Добавление навыка/знания')).click()
        assert self.element_is_clickable(self.locators.SUBMIT_BUTTON, 2), \
            "Кнопка Добавить не активна после заполнения обязательных полей"
        # Поле Тип
        self.action_select_all_text(self.element_is_visible(self.locators.TYPE_FIELD))
        self.element_is_visible(self.locators.TYPE_FIELD).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.text_on_page('Добавление навыка/знания')).click()
        assert self.element_is_visible(self.locators.MUI_ERROR).text == 'Поле обязательно', \
            "Нет сообщения об обязательности поля Тип"
        type_field_color = self.element_is_present(self.locators.TYPE_FIELD_COLOR).value_of_css_property('border-color')
        assert type_field_color == 'rgb(211, 47, 47)', "Цвет поля Тип не красный"
        self.element_is_visible(self.locators.BREAK_BUTTON).click()

    @allure_testit_step('Проверка отклика при совпадении имени навыка/знания')
    def check_skill_same_name(self, name):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.text_on_page('Добавление навыка/знания')).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 2), \
            "Кнопка Добавить активна при не корректном заполнении полей"
        assert self.element_is_visible(self.locators.MUI_ERROR).text == 'Навык/Знание с данным названием уже существует', \
            "Нет сообщения о совпадении имен"
        name_field_color = self.element_is_present(self.locators.NAME_FIELD_COLOR).value_of_css_property('border-color')
        assert name_field_color == 'rgb(211, 47, 47)', "Цвет поля Название не красный"
        self.element_is_visible(self.locators.BREAK_BUTTON).click()

    @allure_testit_step('Проверка ответа при превышении количества допустимых символов')
    def check_exceeded_characters_in_fields(self):
        name_error = self.check_max_field_length(
            self.locators.NAME_FIELD,
            64,
            self.locators.NAME_FIELD_COLOR,
            self.locators.text_on_page('Добавление навыка/знания'),
            'AAA'
        )
        assert name_error == 'Превышено допустимое количество символов: 64', "Не соблюдена максимальная длина поля Имя"
        name_error = self.check_max_field_length(
            self.locators.DESCRIPTION_FIELD,
            1000,
            self.locators.DESCRIPTION_FIELD_COLOR,
            self.locators.text_on_page('Добавление навыка/знания'),
            'AAA'
        )
        assert name_error == 'Превышено допустимое количество символов: 1000', \
            "Не соблюдена максимальная длина поля Описание"

    @allure_testit_step('Открытие дровера редактирования знания или навыка')
    def open_skill_to_redact(self, skill_name):
        self.element_is_visible(self.locators.kebab_by_skill_name(skill_name)).click()
        self.element_is_visible(self.locators.KEBABS_REDACT_MENU_ITEM).click()

    @allure_testit_step('Проверка полей дровера редактирования знания/навыка и изменение значений полей')
    def check_redact_drawer_fields(self, new_name, new_description):
        assert self.element_is_displayed(self.locators.text_on_page('Редактирование навыка/знания')), \
            "Нет заголовка дровера добавления навыка/знания"
        name_error = self.check_max_field_length(
            self.locators.NAME_FIELD,
            64,
            self.locators.NAME_FIELD_COLOR,
            self.locators.text_on_page('Редактирование навыка/знания'),
            new_name
        )
        assert name_error == 'Превышено допустимое количество символов: 64', "Не соблюдена максимальная длина поля Имя"
        self.element_is_visible(self.locators.TYPE_FIELD).click()
        menu_items = [item.text for item in self.elements_are_visible(self.locators.LI_MENU_ITEM)]
        assert menu_items == ['Навык', 'Знание'], "В дропдауне Тип доступны не все значения"
        name_error = self.check_max_field_length(
            self.locators.DESCRIPTION_FIELD,
            1000,
            self.locators.DESCRIPTION_FIELD_COLOR,
            self.locators.text_on_page('Редактирование навыка/знания'),
            new_description
        )
        assert name_error == 'Превышено допустимое количество символов: 1000', \
            "Не соблюдена максимальная длина поля Описание"
        assert self.element_is_displayed(self.locators.SUBMIT_BUTTON), "Отсутствует кнопка Добавить"
        assert self.element_is_displayed(self.locators.BREAK_BUTTON), "Отсутствует кнопка Отменить"

