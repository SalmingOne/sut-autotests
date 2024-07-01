import time

import allure
import pytest
import testit

from pages.advanced_search_page import AdvancedSearchPage


@allure.suite("Страница расширенного поиска")
class TestAdvancedSearchPage:
    @testit.workItemIds(3248)
    @testit.displayName("10.3.6 Сохранение расширенного поиска")
    @pytest.mark.smoke
    @allure.title("id-3248 10.3.6 Сохранение расширенного поиска")
    def test_saving_advanced_search(self, login, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        time.sleep(2)
        search_name, criterion_value, operator_value, condition_value = advanced_search_page.create_new_search()
        chips_names = advanced_search_page.get_search_chips_names()
        advanced_search_page.check_tooltip(search_name)
        fields_values = advanced_search_page.get_chips_values_and_delete_search_chips('Авто-поиск')
        assert search_name.upper() in chips_names, "Имени поиска нет на чипсах"
        assert criterion_value and operator_value and condition_value in fields_values, "Параметры поиска некорректно сохранились"

    @testit.workItemIds(1173)
    @testit.displayName("10.3.1. Добавление и удаление строки поиска")
    @pytest.mark.regress
    @allure.title("id-1173 10.3.1. Добавление и удаление строки поиска")
    def test_adding_or_removing_advanced_search_string(self, login, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.add_string_to_search()
        advanced_search_page.check_operator_selector_switch()
        advanced_search_page.check_two_string()
        advanced_search_page.check_delete_string()

    @testit.workItemIds(1131)
    @testit.displayName("10.3.1. Добавление и удаление группы поиска")
    @pytest.mark.regress
    @allure.title("id-1131 10.3.1. Добавление и удаление группы поиска")
    def test_adding_or_removing_search_group(self, login, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.add_group_to_search()
        advanced_search_page.check_add_block()
        advanced_search_page.check_menu_item()
        advanced_search_page.check_delete_group()

    @testit.workItemIds(3206)
    @testit.displayName("10.3.1. Отмена поиска")
    @pytest.mark.regress
    @allure.title("id-3206 10.3.1. Отмена поиска")
    def test_cancel_search(self, login, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page. check_cancel_search()

    @testit.workItemIds(1137)
    @testit.displayName("10.3.1.  Операторы сравнения для поиска сотрудников (числовой тип поля)")
    @pytest.mark.regress
    @allure.title("id-1137 10.3.1.  Операторы сравнения для поиска сотрудников (числовой тип поля)")
    def test_comparison_operators_for_employee_searches_numeric_field_type(self, login, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.check_numeric_and_date_field()

    @testit.workItemIds(1138)
    @testit.displayName("10.3.1. Операторы сравнения для поиска сотрудников (дата)")
    @pytest.mark.regress
    @allure.title("id-1138 10.3.1. Операторы сравнения для поиска сотрудников (дата)")
    def test_comparison_operators_for_employee_searches_date_type(self, login, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.check_numeric_and_date_field()

    @testit.workItemIds(1139)
    @testit.displayName("10.3.1.  Операторы сравнения для поиска сотрудников (тождество)")
    @pytest.mark.regress
    @allure.title("id-1139 10.3.1.  Операторы сравнения для поиска сотрудников (тождество)")
    def test_comparison_operators_for_employee_searches_identity_type(self, login, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.check_identity_field()

    @testit.workItemIds(10094)
    @testit.displayName("10.3.1. Сброс значений в модальном окне поиска")
    @pytest.mark.regress
    @allure.title("id-10094 10.3.1. Сброс значений в модальном окне поиска")
    def test_resetting_values_in_a_modal_search_window(self, login, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        time.sleep(3)
        advanced_search_page.check_resetting_values_in_a_modal_search_window()

