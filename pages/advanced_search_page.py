import time

import allure
import testit
from selenium.common import TimeoutException
from selenium.webdriver import Keys

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
        try:
            condition_value = self.elements_are_visible(self.locators.LI_MENU_ITEM, 2)[1].text
            self.elements_are_visible(self.locators.LI_MENU_ITEM)[1].click()
        except TimeoutException:
            self.elements_are_visible(self.locators.OPEN_BUTTONS)[2].click()
            condition_value = self.elements_are_visible(self.locators.LI_MENU_ITEM)[1].text
            self.elements_are_visible(self.locators.LI_MENU_ITEM)[1].click()

        self.element_is_visible(self.locators.SAVE_SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.SEARCH_NAME_FIELD).send_keys('Авто-поиск')
        self.element_is_visible(self.locators.CHECK_ICON).click()
        return 'Авто-поиск', criterion_value, operator_value, condition_value.split('(')[0].rstrip()

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

    @testit.step("Получение значений всех полей")
    @allure.step("Получение значений всех полей")
    def get_all_fields(self):
        fields = self.elements_are_visible(self.locators.ALL_FIELDS)
        values = []
        for field in fields:
            values.append(field.get_attribute('value'))
        return values

    @testit.step("Удаление сохраненного поиска")
    @allure.step("Удаление сохраненного поиска")
    def get_chips_values_and_delete_search_chips(self, name):
        self.action_double_click(self.element_is_visible(self.locators.chips_by_name(name)))
        values = self.get_all_fields()
        self.element_is_visible(self.locators.DELETE_SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(2)
        return values

    @testit.step("Добавление строки в расширенном поиске")
    @allure.step("Добавление строки в расширенном поиске")
    def add_string_to_search(self):
        self.element_is_visible(self.locators.NEW_SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.KEBAB_MENU_BUTTON).click()
        self.element_is_visible(self.locators.ADD_RULES_BUTTON).click()

    @testit.step("Проверка переключателя с выбором оператора")
    @allure.step("Проверка переключателя с выбором оператора")
    def check_operator_selector_switch(self):
        assert self.element_is_displayed(self.locators.AND_SWITCH), "Нет селектора с оператором И"
        assert 'Mui-selected' in self.element_is_visible(self.locators.AND_SWITCH).get_attribute('class'), "Оператор И не выбран по умолчанию"
        assert self.element_is_displayed(self.locators.OR_SWITCH), "Нет селектора с оператором ИЛИ"

    @testit.step("Проверка наличия двух строк")
    @allure.step("Проверка наличия двух строк")
    def check_two_string(self):
        assert len(self.elements_are_visible(self.locators.CRITERION_FIELD)) == 2, "Не два поля Критерии"
        assert len(self.elements_are_visible(self.locators.RUL_FIELD)) == 2, "Не два поля Правила"
        assert len(self.elements_are_visible(self.locators.DELETE_ICON)) == 2, "Не две иконки удаления строки"

    @testit.step("Проверка удаления одной строки")
    @allure.step("Проверка удаления одной строки")
    def check_delete_string(self):
        self.elements_are_visible(self.locators.DELETE_ICON)[0].click()
        assert len(self.elements_are_visible(self.locators.CRITERION_FIELD)) == 1, "Не удалилась строка"
        assert not self.element_is_displayed(self.locators.DELETE_ICON, 1), "Осталась иконка удаления строки"

    @testit.step("Добавление группы поиска")
    @allure.step("Добавление группы поиска")
    def add_group_to_search(self):
        self.element_is_visible(self.locators.NEW_SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.KEBAB_MENU_BUTTON).click()
        self.element_is_visible(self.locators.ADD_GROUP_BUTTON).click()

    @testit.step("Проверка наличия второй группы поиска")
    @allure.step("Проверка наличия второй группы поиска")
    def check_add_block(self):
        assert len(self.elements_are_visible(self.locators.CRITERION_FIELD)) == 3, "Не три поля Критерии"
        assert len(self.elements_are_visible(self.locators.RUL_FIELD)) == 3, "Не три поля Правила"
        assert len(self.elements_are_visible(self.locators.DELETE_ICON)) == 3, "Не три иконки удаления строки"
        assert len(self.elements_are_visible(self.locators.AND_SWITCH)) == 2, "Нет второй группы"

    @testit.step("Получение текста элементов кебаб меню")
    @allure.step("Получение текста элементов кебаб меню")
    def get_kebab_menu_item_text(self, index_element):
        self.elements_are_visible(self.locators.KEBAB_MENU_BUTTON)[index_element].click()
        all_li = self.elements_are_visible(self.locators.MENU_ITEM_TEXT)
        data = []
        for li in all_li:
            data.append(li.text)
        return data

    @testit.step("Проверка текста элементов кебаб меню")
    @allure.step("Проверка текста элементов кебаб меню")
    def check_menu_item(self):
        assert self.get_kebab_menu_item_text(1) == ['Добавить правило', 'Добавить группу', 'Удалить группу'], "Не корректные пункты кебаб меню"

    @testit.step("Проверка удаления группы поиска")
    @allure.step("Проверка удаления группы поиска")
    def check_delete_group(self):
        self.element_is_visible(self.locators.DELETE_GROUP_BUTTON).click()
        assert len(self.elements_are_visible(self.locators.CRITERION_FIELD)) == 1, "Не удалилась группа"
        assert not self.element_is_displayed(self.locators.DELETE_ICON, 1), "Осталась иконка удаления строки\группы"

    @testit.step("Проверка отмены поиска")
    @allure.step("Проверка отмены поиска")
    def check_cancel_search(self):
        self.element_is_visible(self.locators.NEW_SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.ABORT_BUTTON).click()
        assert not self.element_is_displayed(self.locators.CRITERION_FIELD, 1), "Модальное окно новый поиск не закрылось"

    @testit.step("Получение текста всех операторов")
    @allure.step("Получение текста всех операторов")
    def get_operators(self):
        operators = self.elements_are_visible(self.locators.LI_MENU_ITEM)
        all_operators = []
        for operator in operators:
            all_operators.append(operator.get_attribute('aria-label'))
        return all_operators

    @testit.step("Проверка операторов числового типа поля и даты")
    @allure.step("Проверка операторов числового типа поля и даты")
    def check_numeric_and_date_field(self):
        self.element_is_visible(self.locators.NEW_SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.CRITERION_FIELD).send_keys('Дата рождения')
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        self.element_is_visible(self.locators.RUL_FIELD).click()
        assert self.get_operators() == ['Равно', 'Не равно', 'Меньше', 'Меньше или равно', 'Больше', 'Больше или равно', 'Пусто', 'Не пусто'], \
            "Не корректные операторы сравнения при выборе числового типа поля"

    @testit.step("Проверка операторов поля с типом тождество")
    @allure.step("Проверка операторов поля с типом тождество")
    def check_identity_field(self):
        self.element_is_visible(self.locators.NEW_SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.CRITERION_FIELD).send_keys('Пол')
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        self.element_is_visible(self.locators.RUL_FIELD).click()
        assert self.get_operators() == ['Равно', 'Не равно', 'Пусто', 'Не пусто'], "Не корректные операторы сравнения"

    @testit.step("Проверка кнопки сбросить все")
    @allure.step("Проверка кнопки сбросить все")
    def check_resetting_values_in_a_modal_search_window(self):
        self.element_is_visible(self.locators.NEW_SEARCH_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.KEBAB_MENU_BUTTON).click()
        self.element_is_visible(self.locators.ADD_RULES_BUTTON).click()
        self.elements_are_visible(self.locators.CRITERION_FIELD)[1].send_keys('Должность')
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        all_fields_before = self.get_all_fields()
        self.element_is_visible(self.locators.RESET_ALL_BUTTON).click()
        all_fields_after = self.get_all_fields()
        assert all_fields_before != all_fields_after, "Не удалилось правило"
        assert all_fields_after == ['', 'Равно'], "Отображается не одна строка поиска (по умолчанию)"

    @testit.step("Получение текста тултипа")
    @allure.step("Получение текста тултипа")
    def get_tooltip(self, locator):
        self.action_move_to_element(self.element_is_visible(locator))
        tooltip_text = self.element_is_visible(self.locators.TOOLTIP).text
        return tooltip_text

    @testit.step("Проверка правила Пусто")
    @allure.step("Проверка правила Пусто")
    def check_selecting_the_rule_empty_or_not_empty(self):
        self.element_is_visible(self.locators.NEW_SEARCH_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.CRITERION_FIELD).send_keys('Статус')
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        self.element_is_visible(self.locators.RUL_FIELD).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.RUL_FIELD).send_keys('Пусто')
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        tooltip = self.get_tooltip(self.locators.STATUS_VALUE_FIELD)
        assert tooltip == 'Выбранное правило не предполагает заполнение данного поля', "Не отображается тултип"
        assert not self.element_is_clickable(self.locators.STATUS_VALUE_FIELD, 1), "Поле Значение не задизейблено"

    @testit.step("Проверка наличия чипсы сохраненного поиска")
    @allure.step("Проверка наличия чипсы сохраненного поиска")
    def check_search_chips(self):
        assert self.element_is_displayed(self.locators.SEARCH_CHIPS), "Нет чипсы сохраненного поиска"

    @testit.step("Проверка наличия кнопки новый поиск")
    @allure.step("Проверка наличия кнопки новый поиск")
    def check_new_search(self):
        assert self.element_is_displayed(self.locators.NEW_SEARCH_BUTTON), "Нет кнопки новый поиск"

    @testit.step("Проверка наличия кнопки экспорта в эксель")
    @allure.step("Проверка наличия кнопки экспорта в эксель")
    def check_export_to_exel_button(self):
        assert self.element_is_displayed(self.locators.EXPORT_TO_EXEL_BUTTON), "Нет кнопки экспорта в эксель"

    @testit.step("Проверка заголовков столбцов таблицы")
    @allure.step("Проверка заголовков столбцов таблицы")
    def check_column_titles(self):
        all_titles = self.elements_are_visible(self.locators.COLUMNS_TITLES)
        columns_texts = []
        for a in all_titles:
            columns_texts.append(a.text)
        assert columns_texts == ['Фото', 'ФИО', 'Отдел', 'Должность', 'Статус'], "Есть не все столбцы"

    @testit.step("Проверка кнопки сбросить поиск")
    @allure.step("Проверка кнопки сбросить поиск")
    def check_break_search_button(self, name):
        assert not self.element_is_clickable(self.locators.BREAK_SEARCH_BUTTON), "Кнопка кликабельна до выбора поиска"
        self.element_is_visible(self.locators.chips_by_name(name)).click()
        assert self.element_is_clickable(self.locators.BREAK_SEARCH_BUTTON), "Кнопка не кликабельна после выбора поиска"

    @testit.step("Проверка изменения сохраненного поиска")
    @allure.step("Проверка изменения сохраненного поиска")
    def check_editing_search(self, name):
        time.sleep(2)
        self.action_double_click(self.element_is_visible(self.locators.chips_by_name(name)))
        values_before = self.get_all_fields()
        self.element_is_visible(self.locators.CRITERION_FIELD).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.CRITERION_FIELD).send_keys('Отдел')
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        self.element_is_visible(self.locators.RUL_FIELD).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.RUL_FIELD).send_keys('Не равно')
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        self.elements_are_visible(self.locators.OPEN_BUTTONS)[2].click()
        try:
            self.elements_are_visible(self.locators.LI_MENU_ITEM, 1)[1].click()
        except TimeoutException:
            self.elements_are_visible(self.locators.OPEN_BUTTONS)[2].click()
            self.elements_are_visible(self.locators.LI_MENU_ITEM)[1].click()

        values_after = self.get_all_fields()
        self.element_is_visible(self.locators.SAVE_SEARCH_BUTTON).click()
        assert values_before != values_after, "Поиск не изменился"

    @testit.step("Берем текст сообщения системы")
    @allure.step("Берем текст сообщения системы")
    def get_massage(self):
        return self.element_is_visible(self.locators.ALERT_MESSAGE).text

    @testit.step("Проверка кнопки Найти")
    @allure.step("Проверка кнопки Найти")
    def check_search_button(self):
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        assert not self.element_is_displayed(self.locators.RESET_ALL_BUTTON, 1), "Модальное окно не закрылось"

    @testit.step("Проверка отмены сохранения изменения поиска")
    @allure.step("Проверка отмены сохранения изменения поиска")
    def check_cancel_edition_search(self, name):
        time.sleep(2)
        self.action_double_click(self.element_is_visible(self.locators.chips_by_name(name)))
        values_before = self.get_all_fields()
        self.element_is_visible(self.locators.CRITERION_FIELD).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.CRITERION_FIELD).send_keys('Отдел')
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        self.element_is_visible(self.locators.RUL_FIELD).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.RUL_FIELD).send_keys('Не равно')
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        self.elements_are_visible(self.locators.OPEN_BUTTONS)[2].click()
        try:
            self.elements_are_visible(self.locators.LI_MENU_ITEM, 1)[1].click()
        except TimeoutException:
            self.elements_are_visible(self.locators.OPEN_BUTTONS)[2].click()
            self.elements_are_visible(self.locators.LI_MENU_ITEM)[1].click()

        values_after = self.get_all_fields()
        self.element_is_visible(self.locators.ABORT_BUTTON).click()
        assert not self.element_is_displayed(self.locators.RESET_ALL_BUTTON, 1), "Модальное окно не закрылось"
        assert values_before != values_after, "Изменения не внесены"
        return values_before

    @testit.step("Проверка поиска после отмены сохранения изменения")
    @allure.step("Проверка поиска после отмены сохранения изменения")
    def check_search_not_change(self, name):
        self.action_double_click(self.element_is_visible(self.locators.chips_by_name(name)))
        return self.get_all_fields()

    @testit.step("Проверка наличия чипсы поиска на странице")
    @allure.step("Проверка наличия чипсы поиска на странице")
    def check_chips_on_page(self, name):
        return self.element_is_displayed(self.locators.chips_by_name(name), 1)
