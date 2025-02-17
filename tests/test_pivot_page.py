import time

import allure
import pytest
import testit

from endpoints.users_endpoint import UserEndpoint
from pages.labor_cost_page import LaborCostPage
from pages.pivot_tab_page import PivotTabPage


@allure.suite("Сводная таблица")
class TestPivotPage:

    @testit.workItemIds(3104)
    @testit.displayName("3.2.2.1 Проверка правильности подсчета трудозатрат за месяц при отображении Сводной таблицы За месяц-по неделям")
    @pytest.mark.smoke
    @allure.title("id-3104 3.2.2.1 Проверка правильности подсчета трудозатрат за месяц при отображении Сводной таблицы За месяц-по неделям")
    def test_correct_month_summ_on_pivot_for_month_by_week(self, project_with_assignment, login, driver):
        # Заполняем таблицу трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(1)
        sum_in_month = labor_cost_page.input_work_by_month()
        # Берем сумму на сводной таблице проектов за месяц по неделям
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        pivot_tab_page.choose_period("month")
        time.sleep(1)
        sum_on_project = pivot_tab_page.get_sum_reason_on_project("month")
        # Берем сумму на сводной таблице пользователей за месяц по неделям
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.open_project_list()
        sum_on_user = pivot_tab_page.get_sum_reason_on_user()
        assert str(sum_in_month) == sum_on_project
        assert str(sum_in_month) == sum_on_user

    @testit.workItemIds(3105)
    @testit.displayName("3.2.2.1 Проверка правильности подсчета трудозатрат за месяц при отображении Сводной таблицы За месяц-по неделям")
    @pytest.mark.smoke
    @allure.title("id-3105 3.2.2.1 Проверка правильности подсчета трудозатрат за неделю при отображении Сводной таблицы За неделю")
    def test_correct_week_summ_on_pivot_for_week(self, project_with_assignment, login, driver):
        # Заполняем таблицу трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.choose_period("week")
        sum_in_week = labor_cost_page.input_work_by_week()
        # Берем сумму на сводной таблице проектов за неделю
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        pivot_tab_page.choose_period("week")
        sum_on_project = pivot_tab_page.get_sum_reason_on_project("week")
        # Берем сумму на сводной таблице пользователей за месяц по неделям
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.open_project_list()
        sum_on_user = pivot_tab_page.get_sum_reason_on_user()
        assert str(sum_in_week) == sum_on_project
        assert str(sum_in_week) == sum_on_user

    @testit.workItemIds(3106)
    @testit.displayName("3.2.2.1 Проверка правильности подсчета трудозатрат за год при отображении Сводной таблицы За год")
    @pytest.mark.smoke
    @allure.title(
        "id-3106 3.2.2.1 Проверка правильности подсчета трудозатрат за год при отображении Сводной таблицы За год")
    def test_correct_summ_on_pivot_for_year(self, project_with_assignment, login, driver):
        # Заполняем таблицу трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        sum_in_year = labor_cost_page.input_work_by_year()
        # Берем сумму на сводной таблице проектов за неделю
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(1)
        pivot_tab_page.choose_period("year")
        sum_on_project = pivot_tab_page.get_sum_reason_on_project("year")
        # Берем сумму на сводной таблице пользователей за месяц по неделям
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.open_project_list()
        sum_on_user = pivot_tab_page.get_sum_reason_on_user()
        assert str(sum_in_year) == sum_on_project
        assert str(sum_in_year) == sum_on_user

    @testit.workItemIds(1181)
    @testit.displayName("3.2.2.11. Отображение переработок в сводной таблице трудозатрат")
    @pytest.mark.smoke
    @allure.title("id-1181 3.2.2.11. Отображение переработок в сводной таблице трудозатрат")
    def test_displaying_overwork_on_pivot_page(self, project_with_overtime_work, login, driver):
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(1)
        pivot_tab_page.check_overwork_by_project()
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.open_project_list()
        pivot_tab_page.check_overwork_by_user()

    @testit.workItemIds(928)
    @testit.displayName("3.2.2.4. Выбор формата ресурсов отображения значений трудозатрат в сводной таблице по пользователю")
    @pytest.mark.regress
    @allure.title("id-928 3.2.2.4. Выбор формата ресурсов отображения значений трудозатрат в сводной таблице по пользователю")
    def test_select_the_resource_format_for_displaying_in_pivot_page(self, simple_project, login, driver):
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(1)
        pivot_tab_page.choose_period("week")
        assert pivot_tab_page.get_first_column_title() == 'Проект', "Название первого столбца не Проект"
        pivot_tab_page.check_tab_column_titles_by_project()
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.check_chose_period_list()
        pivot_tab_page.check_export_buttons()
        pivot_tab_page.check_next_previous_buttons()
        pivot_tab_page.check_filter_icon()
        assert pivot_tab_page.get_first_column_title() == 'Пользователь', "Название первого столбца не Пользователь"
        time.sleep(2)
        pivot_tab_page.check_tab_column_titles_by_user()

    @testit.workItemIds(11832)
    @testit.displayName("3.2.2.18 Экспорт в JSON, если не заполнены обязательные поля")
    @pytest.mark.regress
    @allure.title("id-11832 3.2.2.18 Экспорт в JSON, если не заполнены обязательные поля")
    def test_export_to_json_if_required_fields_are_left_blank(self, simple_project, login, driver):
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(1)
        pivot_tab_page.press_export_to_json_button()
        assert not pivot_tab_page.get_clickable_save_button(), "Кнопка сохранения не задизейблена"
