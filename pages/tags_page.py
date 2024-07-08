import time

import allure
import testit
from selenium.webdriver import Keys

from locators.tags_page_locators import TagsPageLocators
from pages.base_page import BasePage


class TagsPage(BasePage):
    locators = TagsPageLocators()

    @testit.step("Переход на справочник группы знаний")
    @allure.step("Переход на справочник группы знаний")
    def go_to_tags_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.REFERENCE_BOOKS).click()
        self.element_is_visible(self.locators.TAG_TAB).click()

    @testit.step("Нажатие кнопки добавить группу знаний")
    @allure.step("Нажатие кнопки добавить группу знаний")
    def press_add_tag_button(self):
        self.element_is_visible(self.locators.ADD_TAG_BUTTON).click()

    @testit.step("Проверка поля Имя дровера добавления группы знаний")
    @allure.step("Проверка поля Имя дровера добавления группы знаний")
    def check_name_field(self):
        bad_value = ('Loremipsumdolorsitametconsectetueradipiscingelitseddiamnonummynibheuismodtinciduntutlaoreetdoloremagnaaliquam12345678901234567890')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(bad_value)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_visible(self.locators.ABORT_BUTTON).click()
        assert error_text == 'Максимальное количество символов: 128',\
            "Не появилось сообщение о превышении максимального количества символов"

    @testit.step("Добавление группы знаний")
    @allure.step("Добавление группы знаний")
    def create_tag(self, name, skill_name):
        self.element_is_visible(self.locators.ADD_TAG_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.SKILL_FIELD).click()
        self.element_is_visible(self.locators.check_li_item_by_text(skill_name)).click()
        self.action_esc()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Сортируем группы знаний по имени")
    @allure.step("Сортируем группы знаний по имени")
    def sort_tags(self):
        self.element_is_visible(self.locators.SORT_TAGS_BUTTON).click()

    @testit.step("Переход на вкладку группы знаний")
    @allure.step("Переход на вкладку группы знаний")
    def go_to_tag_tab(self):
        self.element_is_visible(self.locators.TAG_TAB).click()

    @testit.step("Проверка наличия группы знаний на вкладке группы знаний")
    @allure.step("Проверка наличия группы знаний на вкладке группы знаний")
    def check_tag_on_tag_tab(self, name):
        assert self.element_is_displayed(self.locators.text_on_page(name)),\
            "Имени группы знаний нет на вкладке группы знаний"

    @testit.step("Изменение группы знаний")
    @allure.step("Изменение группы знаний")
    def edit_tag(self, name_before, name, skill_name):
        self.element_is_visible(self.locators.kebab_by_tag_name(name_before)).click()
        self.element_is_visible(self.locators.KEBABS_REDACT_MENU_ITEM).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.SKILL_FIELD).click()
        self.element_is_visible(self.locators.check_li_item_by_text(skill_name)).click()
        self.action_esc()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка кнопки добавления группы знаний")
    @allure.step("Проверка кнопки добавления группы знаний")
    def check_add_teg_button(self):
        assert self.element_is_displayed(self.locators.ADD_TAG_BUTTON), "Нет кнопки добавления группы знаний"

    @testit.step("Проверка заголовков столбцов таблицы")
    @allure.step("Проверка заголовков столбцов таблицы")
    def check_columns_headers(self):
        time.sleep(1)
        columns_headers = self.elements_are_visible(self.locators.COLUMN_TITLES)
        headers_text = []
        for element in columns_headers:
            headers_text.append(element.text)
        assert headers_text == ['Группы знаний', 'Знания', 'Действия'], 'В таблице есть не все столбцы'

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

    @testit.step("Добавление группы знаний с двумя скилами")
    @allure.step("Добавление группы знаний с двумя скилами")
    def check_create_tag_with_two_skills(self, name, skill_name, second_skill_name):
        self.element_is_visible(self.locators.ADD_TAG_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.SKILL_FIELD).click()
        self.element_is_visible(self.locators.check_li_item_by_text(skill_name)).click()
        self.element_is_visible(self.locators.check_li_item_by_text(second_skill_name)).click()
        self.action_esc()
        assert len(self.elements_are_visible(self.locators.CANSEL_ICON)) == 2, "В поле не два скила"
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка отмены добавления группы знаний")
    @allure.step("Проверка отмены добавления группы знаний")
    def check_cancel_adding_tag(self, name):
        self.element_is_visible(self.locators.ADD_TAG_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.ABORT_BUTTON).click()
        self.sort_tags()
        assert not self.element_is_displayed(self.locators.text_on_page(name), 1), "Группа знаний сохранилась"

    @testit.step("Проверка добавления Группы знаний без заполнения обязательных полей")
    @allure.step("Проверка добавления Группы знаний без заполнения обязательных полей")
    def check_adding_tag_without_filling_in_a_required_field(self):
        self.element_is_visible(self.locators.ADD_TAG_BUTTON).click()
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 1), "Кнопка сохранения не задизейблена"
        self.element_is_visible(self.locators.NAME_FIELD).send_keys("Имя")
        assert self.element_is_clickable(self.locators.SUBMIT_BUTTON, 1), "Кнопка сохранения задизейблена"

    @testit.step("Берем текст всех сообщений системы")
    @allure.step("Берем текст всех сообщений системы")
    def get_alert_message(self):
        all_alerts = self.elements_are_visible(self.locators.ALERT_TEXT)
        data = []
        for alert in all_alerts:
            data.append(alert.text)
        return data

    @testit.step("Добавление Группы знаний с неуникальным именем")
    @allure.step("Добавление Группы знаний с неуникальным именем")
    def check_add_tag_not_unique_name(self, name):
        self.element_is_visible(self.locators.ADD_TAG_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        error = self.element_is_visible(self.locators.MUI_ERROR).text
        alert = self.get_alert_message()
        assert error == 'Укажите уникальноe название группы знаний', "Не появилось сообщение с предупреждением"
        assert alert == ['Группа уже добавлена'], "Не появился тост с предупреждением"

    @testit.step("Проверка максимально длины полей дровера")
    @allure.step("Проверка максимально длины полей дровера")
    def check_drawer_fields_max_length(self):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys('a' * 129)
        self.element_is_visible(self.locators.SKILL_FIELD).click()
        error = self.element_is_visible(self.locators.MUI_ERROR).text
        assert error == 'Максимальное количество символов: 128', "Не корректное сообщение об ошибке"
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys('a' * 128)
        self.element_is_visible(self.locators.SKILL_FIELD).click()
        assert not self.element_is_displayed(self.locators.MUI_ERROR,
                                             1), "Появилось сообщение об ошибке при корректной длине"
        self.element_is_visible(self.locators.SKILL_FIELD).send_keys('a' * 65)
        assert self.element_is_displayed(self.locators.MAX_LENGTH_PRESENTATION,
                                         1), "Не появилось сообщение о превышении длины"
        self.element_is_visible(self.locators.NAME_FIELD).click()
        self.element_is_visible(self.locators.SKILL_FIELD).send_keys('a' * 64)
        assert not self.element_is_displayed(self.locators.MAX_LENGTH_PRESENTATION,
                                             1), "Появилось сообщение об ошибке при корректной длине"

    @testit.step("Редактирование Группы знаний по имени")
    @allure.step("Редактирование Группы знаний по имени")
    def redact_tag_by_name(self, name):
        self.element_is_visible(self.locators.kebab_by_tag_name(name)).click()
        self.element_is_visible(self.locators.KEBABS_REDACT_MENU_ITEM).click()

    @testit.step("Проверка ввода не уникального имени при редактирование Группы")
    @allure.step("Проверка ввода не уникального имени при редактирование Группы")
    def check_redact_tag_no_unique_name(self, name):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Получение текста ошибки")
    @allure.step("Получение текста ошибки")
    def get_error(self):
        return self.element_is_visible(self.locators.MUI_ERROR).text

    @testit.step("Проверка редактирования с пустым вводом в поле имя")
    @allure.step("Проверка редактирования с пустым вводом в поле имя")
    def check_redact_tag_empty_field(self):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.SKILL_FIELD).click()
        assert self.get_error() == 'Поле обязательно', "Не появилось сообщение с предупреждением"

    @testit.step("Проверка отмены редактирования")
    @allure.step("Проверка отмены редактирования")
    def check_cancel_editing_tag(self, new_name):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(new_name)
        self.element_is_visible(self.locators.ABORT_BUTTON).click()
        assert not self.element_is_displayed(self.locators.text_on_page(new_name), 1), "Группа знаний изменилась"


