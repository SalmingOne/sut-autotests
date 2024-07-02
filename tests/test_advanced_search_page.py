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

    @testit.workItemIds(10096)
    @testit.displayName("10.3.1. Сброс значений в модальном окне поиска")
    @pytest.mark.regress
    @allure.title("id-10096 10.3.1. Сброс значений в модальном окне поиска")
    def test_resetting_values_in_a_modal_search_window(self, login, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        time.sleep(3)
        advanced_search_page.check_resetting_values_in_a_modal_search_window()

    @testit.workItemIds(10127)
    @testit.displayName("10.3.1. Выбор правила Пусто или Не пусто")
    @pytest.mark.regress
    @allure.title("id-10127 10.3.1. Выбор правила Пусто или Не пусто")
    def test_selecting_the_rule_empty_or_not_empty(self, login, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.check_selecting_the_rule_empty_or_not_empty()

    @testit.workItemIds(3235)
    @testit.displayName("10.3.3. Просмотр страницы Расширенный поиск")
    @pytest.mark.regress
    @allure.title("id-3235 10.3.3. Просмотр страницы Расширенный поиск")
    def test_view_page_advanced_search(self, login, create_advanced_search, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.check_search_chips()
        advanced_search_page.check_new_search()
        advanced_search_page.check_export_to_exel_button()
        advanced_search_page.check_column_titles()
        advanced_search_page.check_break_search_button(create_advanced_search)

    @testit.workItemIds(3237)
    @testit.displayName("10.3.4. Редактирование сохраненного поиска")
    @pytest.mark.regress
    @allure.title("id-3237 10.3.4. Редактирование сохраненного поиска")
    def test_editing_a_saved_search(self, login, create_advanced_search, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        time.sleep(0.5)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.check_editing_search(create_advanced_search)
        message = advanced_search_page.get_massage()
        advanced_search_page.check_search_button()
        assert message == 'Поиск "Автопоиск" сохранен', "Не появилось уведомление об успешном сохранении изменении"

    @testit.workItemIds(3238)
    @testit.displayName("10.3.4. Отмена редактирования сохраненного поиска")
    @pytest.mark.regress
    @allure.title("id-3238 10.3.4. Отмена редактирования сохраненного поиска")
    def test_cansel_editing_a_saved_search(self, login, create_advanced_search, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        time.sleep(0.5)
        advanced_search_page.go_advanced_search_page()
        before = advanced_search_page.check_cancel_edition_search(create_advanced_search)
        after = advanced_search_page.check_search_not_change(create_advanced_search)
        assert before == after, "Изменения сохранились"

    @testit.workItemIds(3242)
    @testit.displayName("10.3.5. Удаление сохраненного поиска")
    @pytest.mark.regress
    @allure.title("id-3242 10.3.5. Удаление сохраненного поиска")
    def test_deleting_a_saved_search(self, login, advanced_search_to_delete, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        time.sleep(1)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.get_chips_values_and_delete_search_chips(advanced_search_to_delete)
        message = advanced_search_page.get_massage()
        assert not advanced_search_page.check_chips_on_page(advanced_search_page), "Чипса сохраненного поиска не удалилась"
        assert message == 'Сохраненный поиск "Для удаления" удален', "Не появилось уведомление об удалении поиска"

    @testit.workItemIds(3249)
    @testit.displayName("10.3.6 Отмена сохранения расширенного поиска")
    @pytest.mark.regress
    @allure.title("id-3249 10.3.6 Отмена сохранения расширенного поиска")
    def test_cancel_saving_advanced_search(self, login, driver):
        advanced_search_page = AdvancedSearchPage(driver)
        time.sleep(1)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.check_cancel_saving()
