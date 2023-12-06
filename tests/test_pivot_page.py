import allure
import pytest

from conftest import project
from pages.labor_cost_page import LaborCostPage
from pages.pivot_tab_page import PivotTabPage


@pytest.mark.usefixtures('project')
@allure.suite("Сводная таблица")
class TestPivotPage:

    # id-3103 3.2.2.1 Проверка правильности подсчета трудозатрат за месяц при отображении "Сводной таблицы" "За
    # месяц-по дням".

    # id-3104 3.2.2.1 Проверка правильности подсчета трудозатрат за месяц при отображении "Сводной таблицы" "За
    # месяц-по неделям".
    @allure.title(
        "id-3104 3.2.2.1 Проверка правильности подсчета трудозатрат за месяц при отображении Сводной таблицы За месяц-по неделям")
    def test_correct_month_summ_on_pivot_for_month_by_week(self, login, driver):
        # Заполняем таблицу трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        sum_in_month = labor_cost_page.input_work_by_month()
        # Берем сумму на сводной таблице проектов за месяц по неделям
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        pivot_tab_page.choose_period("month")
        sum_on_project = pivot_tab_page.get_sum_reason_on_project("month")
        # Берем сумму на сводной таблице пользователей за месяц по неделям
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.open_project_list()
        sum_on_user = pivot_tab_page.get_sum_reason_on_user()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.three_mont_clear()
        assert str(sum_in_month) == sum_on_project
        assert str(sum_in_month) == sum_on_user

    # id-3105 3.2.2.1 Проверка правильности подсчета трудозатрат за неделю при отображении "Сводной таблицы" "За
    # неделю".
    @allure.title(
        "id-3105 3.2.2.1 Проверка правильности подсчета трудозатрат за неделю при отображении Сводной таблицы За неделю")
    def test_correct_week_summ_on_pivot_for_week(self, login, driver):
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
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.choose_period("week")
        labor_cost_page.three_mont_clear()
        assert str(sum_in_week) == sum_on_project
        assert str(sum_in_week) == sum_on_user

    # id-3106 3.2.2.1 Проверка правильности подсчета трудозатрат за год при отображении "Сводной таблицы" "За год"
    @allure.title(
        "id-3106 3.2.2.1 Проверка правильности подсчета трудозатрат за год при отображении Сводной таблицы За год")
    def test_correct_summ_on_pivot_for_year(self, login, driver):
        # Заполняем таблицу трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        sum_in_year = labor_cost_page.input_work_by_year()
        # Берем сумму на сводной таблице проектов за неделю
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        pivot_tab_page.choose_period("year")
        sum_on_project = pivot_tab_page.get_sum_reason_on_project("year")
        # Берем сумму на сводной таблице пользователей за месяц по неделям
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.open_project_list()
        sum_on_user = pivot_tab_page.get_sum_reason_on_user()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.clear_work_by_year()
        assert str(sum_in_year) == sum_on_project
        assert str(sum_in_year) == sum_on_user
