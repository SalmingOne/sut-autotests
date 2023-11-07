from pages.create_project_drawer_page import CreateProjectDrawerPage
from pages.labor_cost_page import LaborCostPage


class TestPivotPage:

    # 3.2.2.1 Проверка правильности подсчета трудозатрат за месяц при отображении "Сводной таблицы" "За месяц-по дням".
    def test_correct_month_summ_on_pivot_for_month_by_day(self, driver):
        # Создаем прект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        create_project_drawer_page.create_project('no')
        #
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
