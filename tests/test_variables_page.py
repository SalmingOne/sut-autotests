import time

import allure
import pytest
import testit

from pages.variables_page import VariablesPage


@allure.suite("Таблица переменных")
class TestVariablesPage:

    @testit.workItemIds(1277)
    @testit.displayName("6.3.1.2 Просмотр таблицы переменных")
    @pytest.mark.smoke
    @allure.title("id-1277 6.3.1.2 Просмотр таблицы переменных")
    def test_displaying_the_variables_page(self, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        variables_page.check_add_variable_button()
        variables_page.check_variables_tab_columns_headers()
        variables_page.check_menu_items_in_actions()

    @testit.workItemIds(1278)
    @testit.displayName("6.3.1.3 Создание переменной в таблице переменных")
    @pytest.mark.smoke
    @allure.title("id-1278 6.3.1.3 Создание переменной в таблице переменных")
    def test_create_a_variable(self, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        variables_page.create_variable(
            'Поле переменной',
            'Имя переменной',
            'Значение переменной'
        )
        message = variables_page.get_alert_message()
        variables_page.delete_variable('Имя переменной')
        variables_page.check_rest_fields()
        assert message == ['Переменная успешно добавлена'], 'Не появилось сообщение о добавлении переменной'
