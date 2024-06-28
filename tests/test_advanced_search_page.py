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
