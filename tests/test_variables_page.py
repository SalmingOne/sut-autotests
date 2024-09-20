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

    @testit.workItemIds(3164)
    @testit.displayName("6.3.1.3 Создание переменной в таблице переменных, если уникальные поля НЕ уникальны")
    @pytest.mark.smoke
    @allure.title("id-3164 6.3.1.3 Создание переменной в таблице переменных, если уникальные поля НЕ уникальны")
    def test_creating_a_variable_with_a_non_unique_fields(self, variables, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        variables_page.create_variable(
            variables[0],
            variables[1],
            'Значение переменной'
        )
        errors = variables_page.get_mui_errors_text()
        assert errors == ['Переменная с таким названием поля уже создана в системе',
                          'Переменная с таким названием уже создана в системе'],\
            'Не появились сообщения о неуникальных полях'

    @testit.workItemIds(1274)
    @testit.displayName("6.3.1.1. Загрузка шаблонов заявлений в систему")
    @pytest.mark.smoke
    @allure.title("id-1274 6.3.1.1. Загрузка шаблонов заявлений в систему")
    def test_add_template_application(self, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        variables_page.check_template_is_empty()
        variables_page.add_template_file()
        # уходим из шаблонов, чтобы проверить что он сохранился
        variables_page.go_to_variables_page()
        variables_page.check_template_file()

    @testit.workItemIds(1276)
    @testit.displayName("6.3.1.1. Удаление шаблонов заявлений в системе")
    @pytest.mark.smoke
    @allure.title("id-1276 6.3.1.1. Удаление шаблонов заявлений в системе")
    def test_delete_template_application(self, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        variables_page.check_template_is_empty()
        variables_page.add_template_file()
        variables_page.add_variable_with_template('Автотест', 'Автотекст')
        value_before_delete = variables_page.get_value_from_column_template('Автотест', '6')
        variables_page.check_template_is_empty()
        # уходим из шаблонов, чтобы проверить что он удалился
        variables_page.go_to_variables_page()
        variables_page.check_template_file_delete()
        value_after_delete = variables_page.get_value_from_column_template('Автотест', '6')
        assert value_before_delete != value_after_delete, 'Шаблон не удален из переменной'
        variables_page.delete_add_variable('Автотест', '7')