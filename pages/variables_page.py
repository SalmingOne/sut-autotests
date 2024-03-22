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
                        'Значение переменной', 'Шаблоны', 'Действия', 'Название поля', 'Название переменной'],\
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

