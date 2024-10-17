import allure
import testit
import time
import os

from selenium.webdriver import Keys
from selenium.common.exceptions import TimeoutException

from locators.variables_page_locators import VariablesPageLocators
from pages.base_page import BasePage


class VariablesPage(BasePage):
    locators = VariablesPageLocators()

    @testit.step("Переход на таблицу переменных")
    @allure.step("Переход на таблицу переменных")
    def go_to_variables_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_AUDIT_TAB).click()
        self.element_is_visible(self.locators.TEMPLATES_TAB).click()

    @testit.step("Проверка кнопки создать переменную")
    @allure.step("Проверка кнопки создать переменную")
    def check_add_variable_button(self):
        assert self.element_is_displayed(self.locators.ADD_VARIABLE_BUTTON), 'Нет кнопки создать переменную'

    @testit.step("Проверка заголовков столбцов таблицы")
    @allure.step("Проверка заголовков столбцов таблицы")
    def check_variables_tab_columns_headers(self):
        headers = self.elements_are_visible(self.locators.COLUMNS_HEADERS)
        data = []
        for head in headers:
            data.append(head.text)
        assert data == ['Переменные', 'Запрашивать значение у пользователя', 'Хранить значение поля',
                        'Значение переменной', 'Шаблоны', 'Действия', 'Название поля', 'Название переменной'], \
            'Есть не все заголовки'

    @testit.step("Проверка пунктов кебаб меню")
    @allure.step("Проверка пунктов кебаб меню")
    def check_menu_items_in_actions(self):
        self.elements_are_visible(self.locators.ALL_SEARCH_FIELDS)[3].send_keys('Системная переменная')
        self.elements_are_visible(self.locators.ALL_KEBABS)[0].click()
        system_variable_menu = self.element_is_visible(self.locators.KEBAB_MENU_ITEM).text
        self.action_esc()
        self.elements_are_visible(self.locators.ALL_SEARCH_FIELDS)[3].send_keys(Keys.CONTROL + 'a')
        self.elements_are_visible(self.locators.ALL_SEARCH_FIELDS)[3].send_keys('Задаётся пользователем')
        self.elements_are_visible(self.locators.ALL_KEBABS)[0].click()
        menu_items = self.elements_are_visible(self.locators.KEBAB_MENU_ITEM)
        data = []
        for item in menu_items:
            data.append(item.text)
        assert system_variable_menu == 'Редактировать', 'Не корректное меню у системных переменных'
        assert data == ['Редактировать', 'Удалить'], 'Не корректное меню у переменных задаваемых пользователями'

    @testit.step("Создание переменной")
    @allure.step("Создание переменной")
    def create_variable(self, field_name, variable_name, variable_value):
        self.element_is_visible(self.locators.ADD_VARIABLE_BUTTON).click()
        self.element_is_visible(self.locators.FIELD_NAME_INPUT).send_keys(field_name)
        self.element_is_visible(self.locators.VARIABLE_NAME_INPUT).send_keys(variable_name)
        self.element_is_visible(self.locators.VARIABLE_VALUE_INPUT).send_keys(variable_value)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Берем текст всех сообщений системы")
    @allure.step("Берем текст всех сообщений системы")
    def get_alert_message(self):
        all_alerts = self.elements_are_visible(self.locators.ALERT_TEXT)
        data = []
        for alert in all_alerts:
            data.append(alert.text)
        return data

    @testit.step("Удаление переменной")
    @allure.step("Удаление переменной")
    def delete_variable(self, variable_mame):
        self.elements_are_visible(self.locators.ALL_SEARCH_FIELDS)[6].send_keys(variable_mame)
        self.elements_are_visible(self.locators.ALL_KEBABS)[0].click()
        self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
        self.element_is_visible(self.locators.DEL_ACCEPT_BUTTON).click()

    @testit.step("Проверка остальных полей")
    @allure.step("Проверка остальных полей")
    def check_rest_fields(self):
        self.element_is_visible(self.locators.ADD_VARIABLE_BUTTON).click()
        # Проверка чекбокса Хранить значение поля
        assert not self.element_is_clickable(self.locators.SAVE_VALUE_CHECKBOX, 1), 'Чекбокс хранить значение поля кликабелен'
        # Проверка работы чекбокса Запрашивать значение у пользователя
        self.element_is_visible(self.locators.ASK_VALUE_CHECKBOX).click()
        assert not self.element_is_clickable(self.locators.VARIABLE_VALUE_INPUT, 1), 'Поле значение переменной не задизейбленно'
        # Проверка поля Шаблоны
        self.element_is_visible(self.locators.TEMPLATES_INPUT_FIELD).click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS_NOT_SELECTED)[0].click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS_NOT_SELECTED)[0].click()
        self.element_is_visible(self.locators.TEMPLATES_INPUT_FIELD).click()
        assert len(self.elements_are_visible(self.locators.CHIPS_IN_TEMPLATES_INPUT_FIELD)) == 2, 'Добавились не все шаблоны'
        self.element_is_visible(self.locators.ABORT_BUTTON).click()

    @testit.step("Получение текста ошибок")
    @allure.step("Получение текста ошибок")
    def get_mui_errors_text(self):
        error_messages = self.elements_are_visible(self.locators.MUI_ERROR)
        data = []
        for message in error_messages:
            data.append(message.text)
        return data

    @testit.step("Проверка что нет загруженных шаблонов")
    @allure.step("Проверка что нет загруженных шаблонов")
    def check_template_is_empty(self):
        while self.element_is_displayed(self.locators.DELETE_ICON):
            self.element_is_visible(self.locators.DELETE_ICON).click()
            time.sleep(1)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            time.sleep(1)
        else:
            pass

    @testit.step("Добавление файла")
    @allure.step("Добавление файла")
    def add_file(self, name, text):
        file = open(os.path.abspath(rf'../{name}'), 'w+')
        file.write(f'{text}')
        file.close()

    @testit.step("Удаление файла")
    @allure.step("Удаление файла")
    def delete_file(self, name):
        os.remove(rf'../{name}')

    @testit.step("Добавление шаблона в валидном формате")
    @allure.step("Добавление шаблона в валидном формате")
    def add_template_file(self):
        self.add_file('шаблон.docx', 'Шаблон')
        self.element_is_present(self.locators.ADD_DOC, 2).send_keys(os.path.abspath(r'../шаблон.docx'))

    @testit.step("Проверка что шаблон добавлен")
    @allure.step("Проверка что шаблон добавлен")
    def check_template_file(self):
        assert self.element_is_displayed(self.locators.check_text('шаблон.docx')), "Файл не добавился"
        self.delete_file('шаблон.docx')

    @testit.step("Создание переменной с шаблоном")
    @allure.step("Создание переменной с шаблоном")
    def add_variable_with_template(self, name, text):
        self.element_is_visible(self.locators.ADD_VARIABLE_BUTTON).click()
        self.element_is_visible(self.locators.FIELD_NAME_INPUT).send_keys(name)
        self.element_is_visible(self.locators.VARIABLE_NAME_INPUT).send_keys(text)
        self.element_is_visible(self.locators.VARIABLE_VALUE_INPUT).send_keys(text)
        self.element_is_visible(self.locators.TEMPLATE_WITH_VARIABLE).click()
        time.sleep(1)
        self.element_is_visible(self.locators.TEMPLATE_VALUE).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)

    @testit.step("Получить значение ячейки в указанном столбце")
    @allure.step("Получить значение ячейки в указанном столбце")
    def get_value_from_column(self, variable_name, column_number):
        try:
            self.element_is_visible(self.locators.get_value_from_column(variable_name, column_number))
            return self.element_is_visible(self.locators.get_value_from_column(variable_name, column_number)).text
        except TimeoutException:
            return 'Пусто'

    @testit.step("Проверка что шаблон удален")
    @allure.step("Проверка что шаблон удален")
    def check_template_file_delete(self):
        assert self.element_is_not_visible(self.locators.check_text('шаблон.docx')), "Файл не удален"
        self.delete_file('шаблон.docx')

    @testit.step("Удаление добавленной переменной")
    @allure.step("Удаление добавленной переменной")
    def delete_add_variable(self, variable_name, column_number):
        self.element_is_visible(self.locators.get_value_from_column(variable_name, column_number)).click()
        time.sleep(1)
        self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
        time.sleep(1)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Получить кол-во переменных на странице")
    @allure.step("Получить кол-во переменных на странице")
    def get_count_of_variables(self):
        return len(self.elements_are_visible(self.locators.ALL_KEBABS))

    @testit.step("Отмена создания переменной")
    @allure.step("Отмена создания переменной")
    def cancel_variable_creation(self, field_name, variable_mame, variable_value):
        self.element_is_visible(self.locators.ADD_VARIABLE_BUTTON).click()
        self.element_is_visible(self.locators.FIELD_NAME_INPUT).send_keys(field_name)
        self.element_is_visible(self.locators.VARIABLE_NAME_INPUT).send_keys(variable_mame)
        self.element_is_visible(self.locators.VARIABLE_VALUE_INPUT).send_keys(variable_value)
        self.element_is_visible(self.locators.ABORT_BUTTON).click()

    @testit.step("Отмена удаления шаблона")
    @testit.step("Отмена удаления шаблона")
    def cancel_template_deletion(self):
        self.element_is_present(self.locators.DELETE_ICON).click()
        self.element_is_visible(self.locators.ABORT_BUTTON).click()
        return self.element_is_displayed(self.locators.DELETE_ICON)

    @testit.step("Проверка что есть хотя бы один загруженный шаблон")
    @testit.step("Проверка что есть хотя бы один загруженный шаблон")
    def check_template_is_not_empty(self):
        if self.element_is_displayed(self.locators.DELETE_ICON):
            pass
        else:
            self.add_template_file()

    @testit.step("Добавление шаблона в невалидном формате")
    @allure.step("Добавление шаблона в невалидном формате")
    def add_incorrect_template_file(self):
        self.add_file('Некорректный шаблон.pdf', 'Некорректный шаблон')
        self.element_is_present(self.locators.ADD_DOC, 2).send_keys(os.path.abspath(r'../Некорректный шаблон.pdf'))
        assert self.element_is_visible(self.locators.ALERT_INCORRECT_TEMPLATE), "Сообщения с предупреждением нет"
        self.delete_file('Некорректный шаблон.pdf')

    @testit.step("Нажать кнопку редактирования добавленной переменной")
    @allure.step("Нажать кнопку редактирования добавленной переменной")
    def click_editing_add_variable(self, variable_name, column_number):
        self.element_is_visible(self.locators.get_value_from_column(variable_name, column_number)).click()
        self.element_is_visible(self.locators.KEBABS_EDIT_MENU_ITEM).click()

    @testit.step("Редактирование переменной")
    @allure.step("Редактирование переменной")
    def editing_variable(self, new_name):
        self.element_is_visible(self.locators.FIELD_NAME_INPUT).send_keys(Keys.CONTROL + 'a', new_name)
        self.element_is_visible(self.locators.VARIABLE_NAME_INPUT).send_keys(Keys.CONTROL + 'a', new_name)
        self.element_is_visible(self.locators.VARIABLE_VALUE_INPUT).send_keys(Keys.CONTROL + 'a', new_name)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Отмена удаления переменной")
    @allure.step("Отмена удаления переменной")
    def cancel_variable_deletion(self, variable_mame):
        self.elements_are_visible(self.locators.ALL_SEARCH_FIELDS)[6].send_keys(variable_mame)
        self.elements_are_visible(self.locators.ALL_KEBABS)[0].click()
        self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
        self.element_is_visible(self.locators.CANCEL_ACCEPT_BUTTON).click()
        self.elements_are_visible(self.locators.ALL_SEARCH_FIELDS)[6].clear()
