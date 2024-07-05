import time

import allure
import testit
from selenium.webdriver import Keys

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

    @testit.step("Сортируем знания по имени")
    @allure.step("Сортируем знания по имени")
    def sort_skills(self):
        self.element_is_visible(self.locators.SORT_SKILLS_BUTTON).click()
        time.sleep(1)

    @testit.step("Открытие дровера редактирования знания по имени")
    @allure.step("Открытие дровера редактирования знания по имени")
    def redact_skill_by_name(self, name):
        self.element_is_visible(self.locators.kebab_by_skill_name(name)).click()
        self.element_is_visible(self.locators.KEBABS_REDACT_MENU_ITEM).click()

    @testit.step("Проверка превышения максимальной длины имени знания")
    @allure.step("Проверка превышения максимальной длины имени знания")
    def check_max_name_field(self):
        text = 'Loremipsumdolorsitametconsectetueradipiscingelitseddiaaaaaaaaaaaa'
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(text)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        error = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_visible(self.locators.BREAK_BUTTON).click()
        assert error == 'Максимальное количество символов: 64', 'Не появилось сообщение о превышении максимума символов'

    @testit.step("Изменение названия знания")
    @allure.step("Изменение названия знания")
    def change_the_skill(self, new_name):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(new_name)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка знания на табе Знания")
    @allure.step("Проверка знания на табе Знания")
    def check_skill_name_on_page(self, name):
        return self.element_is_displayed(self.locators.text_on_page(name), 1)

    @testit.step("Проверка знания в дровере добавления значений в справочниках Группы знаний")
    @allure.step("Проверка знания в дровере добавления значений в справочниках Группы знаний")
    def check_skill_name_on_tag_tab(self, name):
        self.element_is_visible(self.locators.TAG_TAB).click()
        time.sleep(1)
        self.element_is_visible(self.locators.ADD_SKILLS_BUTTON).click()
        self.element_is_visible(self.locators.ARROW_DOWN).click()
        assert self.element_is_displayed(self.locators.text_on_page(name)),\
            "Не сохранились изменения в дровере добавления значений в справочниках Группы знаний"

    @testit.step("Переход на вкладку Знания")
    @allure.step("Переход на вкладку Знания")
    def go_to_skill_tab(self):
        self.element_is_visible(self.locators.SKILLS_TAB).click()

    @testit.step("Проверка наличия Группы знаний на вкладке Знания")
    @allure.step("Проверка наличия Группы знаний на вкладке Знания")
    def check_tag_on_skill_tab(self, skill_name, tag_name):
        self.element_is_visible(self.locators.arrow_by_skill_name(skill_name)).click()
        assert self.element_is_displayed(self.locators.text_on_page(tag_name)), "Группы знаний нет на вкладке Знания"

    @testit.step("Добавление Знания")
    @allure.step("Добавление Знания")
    def create_skill(self, name, tag_name, second_tag_name=None):
        self.element_is_visible(self.locators.ADD_SKILLS_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.TAG_FIELD).click()
        self.element_is_visible(self.locators.check_li_item_by_text(tag_name)).click()
        if second_tag_name is None:
            pass
        else:
            self.element_is_visible(self.locators.check_li_item_by_text(second_tag_name)).click()
        tags_count = len(self.elements_are_visible(self.locators.CANSEL_ICON))
        self.action_esc()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return tags_count

    @testit.step("Отмена добавления Знания")
    @allure.step("Отмена добавления Знания")
    def check_cancel_add_skill(self, name):
        self.element_is_visible(self.locators.ADD_SKILLS_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.BREAK_BUTTON).click()

    @testit.step("Проверка кнопки сохранить при пустом вводе")
    @allure.step("Проверка кнопки сохранить при пустом вводе")
    def check_empty_filling_in_the_required_fields(self):
        self.element_is_visible(self.locators.ADD_SKILLS_BUTTON).click()
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 1), "Кнопка сохранения не задизейблена"
        self.element_is_visible(self.locators.NAME_FIELD).send_keys("Имя")
        assert self.element_is_clickable(self.locators.SUBMIT_BUTTON, 1), "Кнопка сохранения задизейблена"

    @testit.step("Добавление Знания с неуникальным именем")
    @allure.step("Добавление Знания с неуникальным именем")
    def check_add_skill_not_unique_name(self, name):
        self.element_is_visible(self.locators.ADD_SKILLS_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        error = self.element_is_visible(self.locators.MUI_ERROR).text
        alert = self.get_alert_message()
        assert error == 'Укажите уникальноe название знания', "Не появилось сообщение с предупреждением"
        assert alert == ['Значение уже добавлено'], "Не появился тост с предупреждением"

    @testit.step("Берем текст всех сообщений системы")
    @allure.step("Берем текст всех сообщений системы")
    def get_alert_message(self):
        all_alerts = self.elements_are_visible(self.locators.ALERT_TEXT)
        data = []
        for alert in all_alerts:
            data.append(alert.text)
        return data

    @testit.step("Проверка максимально длины полей дровера")
    @allure.step("Проверка максимально длины полей дровера")
    def check_drawer_fields_max_length(self):
        self.element_is_visible(self.locators.ADD_SKILLS_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys('a'*65)
        self.element_is_visible(self.locators.TAG_FIELD).click()
        error = self.element_is_visible(self.locators.MUI_ERROR).text
        assert error == 'Максимальное количество символов: 64', "Не корректное сообщение об ошибке"
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys('a' * 64)
        self.element_is_visible(self.locators.TAG_FIELD).click()
        assert not self.element_is_displayed(self.locators.MUI_ERROR, 1), "Появилось сообщение об ошибке при корректной длине"
        self.element_is_visible(self.locators.TAG_FIELD).send_keys('a'*129)
        assert self.element_is_displayed(self.locators.MAX_LENGTH_PRESENTATION, 1), "Не появилось сообщение о превышении длины"
        self.element_is_visible(self.locators.NAME_FIELD).click()
        self.element_is_visible(self.locators.TAG_FIELD).send_keys('a' * 128)
        assert not self.element_is_displayed(self.locators.MAX_LENGTH_PRESENTATION, 1), "Появилось сообщение об ошибке при корректной длине"

    @testit.step("Получение текста ошибки")
    @allure.step("Получение текста ошибки")
    def get_error(self):
        return self.element_is_visible(self.locators.MUI_ERROR).text

    @testit.step("Редактирование без заполнения обязательных полей")
    @allure.step("Редактирование без заполнения обязательных полей")
    def check_redact_with_empty_fields(self):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.TAG_FIELD).click()

    @testit.step("Редактирование с превышением максимальной длины полей")
    @allure.step("Редактирование с превышением максимальной длины полей")
    def check_drawer_fields_max_length_when_redact(self):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys('a' * 65)
        self.element_is_visible(self.locators.TAG_FIELD).click()
        error = self.element_is_visible(self.locators.MUI_ERROR).text
        assert error == 'Максимальное количество символов: 64', "Не корректное сообщение об ошибке"
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys('a' * 64)
        self.element_is_visible(self.locators.TAG_FIELD).click()
        assert not self.element_is_displayed(self.locators.MUI_ERROR,
                                             1), "Появилось сообщение об ошибке при корректной длине"
        self.element_is_visible(self.locators.TAG_FIELD).send_keys('a' * 129)
        assert self.element_is_displayed(self.locators.MAX_LENGTH_PRESENTATION,
                                         1), "Не появилось сообщение о превышении длины"
        self.element_is_visible(self.locators.NAME_FIELD).click()
        self.element_is_visible(self.locators.TAG_FIELD).send_keys('a' * 128)
        assert not self.element_is_displayed(self.locators.MAX_LENGTH_PRESENTATION,
                                             1), "Появилось сообщение об ошибке при корректной длине"

    @testit.step("Отмена редактирования Знания")
    @allure.step("Отмена редактирования Знания")
    def check_cancel_redact_skill(self, name):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.BREAK_BUTTON).click()
