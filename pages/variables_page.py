import allure
import testit
from selenium.webdriver import Keys

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
    def create_variable(self, field_name, variable_mame, variable_value):
        self.element_is_visible(self.locators.ADD_VARIABLE_BUTTON).click()
        self.element_is_visible(self.locators.FIELD_NAME_INPUT).send_keys(field_name)
        self.element_is_visible(self.locators.VARIABLE_NAME_INPUT).send_keys(variable_mame)
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




