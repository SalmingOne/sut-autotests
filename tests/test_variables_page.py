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
