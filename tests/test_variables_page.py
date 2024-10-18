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
    def test_creating_a_variable_with_a_non_unique_fields(self, variable_not_unique, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        variables_page.create_variable(
            variable_not_unique[0],
            variable_not_unique[1],
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
        value_before_delete = variables_page.get_value_from_column('Автотест', '6')
        variables_page.check_template_is_empty()
        # уходим из шаблонов, чтобы проверить что он удалился
        variables_page.go_to_variables_page()
        variables_page.check_template_file_delete()
        value_after_delete = variables_page.get_value_from_column('Автотест', '6')
        assert value_before_delete != value_after_delete, 'Шаблон не удален из переменной'
        variables_page.delete_add_variable('Автотест', '7')

    @testit.workItemIds(3166)
    @testit.displayName("6.3.1.3 Отмена создания переменной")
    @pytest.mark.regress
    @allure.title("id-3166 6.3.1.3 Отмена создания переменной")
    def test_cancel_variable_creation(self, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        count_before = variables_page.get_count_of_variables()
        variables_page.cancel_variable_creation(
            'Поле переменной',
            'Имя переменной',
            'Значение переменной')
        count_after = variables_page.get_count_of_variables()
        assert count_before == count_after, 'Переменная создана'

    @testit.workItemIds(3163)
    @testit.displayName("6.3.1.1. Отмена удаления шаблона заявления в системе")
    @pytest.mark.regress
    @allure.title("id-3163 6.3.1.1. Отмена удаления шаблона заявления в системе")
    def test_cancel_delete_template_application(self, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        variables_page.check_template_is_not_empty()
        assert variables_page.cancel_template_deletion(), "Шаблон удален"
        variables_page.delete_file_if_used('шаблон.docx')

    @testit.workItemIds(3229)
    @testit.displayName("6.3.1.1. Попытка загрузить шаблон заявления с неподдерживаемым форматом в систему")
    @pytest.mark.regress
    @allure.title("id-3229 6.3.1.1. Попытка загрузить шаблон заявления с неподдерживаемым форматом в систему")
    def test_add_template_application_incorrect_format(self, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        variables_page.check_template_is_empty()
        variables_page.add_incorrect_template_file()

    @testit.workItemIds(1279)
    @testit.displayName("6.3.1.1. Редактирование переменной в таблице переменных")
    @pytest.mark.regress
    @allure.title("id-1279 6.3.1.1. Редактирование переменной в таблице переменных")
    def test_add_editing_variable(self, variable_for_edit, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        variables_page.click_editing_add_variable('Для редактирования', '7')
        time.sleep(5)
        variables_page.editing_variable('Отредактировано')
        # без рефреша не видит новое название
        driver.refresh()
        field_name = variables_page.get_value_from_column("Отредактировано", '1')
        variable_name = variables_page.get_value_from_column("Отредактировано", '2')
        variable_value = variables_page.get_value_from_column("Отредактировано", '5')
        assert field_name == "Отредактировано", 'Название поля не изменилось'
        assert variable_name == "Отредактировано", 'Название переменной не изменилось'
        assert variable_value == "Отредактировано", 'Значение переменной не изменилось'

    @testit.workItemIds(1280)
    @testit.displayName("6.3.1.5 Удаление/отмена удаления переменной из таблицы переменных")
    @pytest.mark.regress
    @allure.title("id-1280 6.3.1.5 Удаление/отмена удаления переменной из таблицы переменных")
    def test_delete_and_cancel_deletion_variable(self, variable_for_delete, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        count_variables = variables_page.get_count_of_variables()
        variables_page.cancel_variable_deletion(variable_for_delete[0])
        driver.refresh()
        count_variables_after_cancel_deletion = variables_page.get_count_of_variables()
        variables_page.delete_variable(variable_for_delete[0])
        driver.refresh()
        count_variables_after_delete = variables_page.get_count_of_variables()
        assert count_variables == count_variables_after_cancel_deletion, "Переменная удалена"
        assert (count_variables - 1) == count_variables_after_delete, "Переменная не удалена"

    @testit.workItemIds(3168)
    @testit.displayName("6.3.1.4 Редактирование переменной в таблице переменных, если заполнены не все поля уникальными значениями")
    @pytest.mark.regress
    @allure.title("id-3168 6.3.1.4 Редактирование переменной в таблице переменных, если заполнены не все поля уникальными значениями")
    def test_edit_variable_to_not_unique(self, variable_for_edit, variable_not_unique, login, driver):
        variables_page = VariablesPage(driver)
        variables_page.go_to_variables_page()
        variables_page.click_editing_add_variable(variable_for_edit['name'], '7')
        variables_page.editing_variable(variable_not_unique['name'])
        variables_page.check_warning_text('Переменная с таким названием поля уже создана в системе', 'Переменная с таким названием уже создана в системе')