from pages.create_project_drawer_page import CreateProjectDrawerPage
from pages.labor_cost_page import LaborCostPage
from pages.pivot_tab_page import PivotTabPage


class TestPivotPage:

    # id-3103 3.2.2.1 Проверка правильности подсчета трудозатрат за месяц при отображении "Сводной таблицы" "За месяц-по дням".
    #def test_correct_month_summ_on_pivot_for_month_by_day(self, login, driver):
        # Создаем прект
        #create_project_drawer_page = CreateProjectDrawerPage(driver)
        #create_project_drawer_page.go_to_create_project_drawer_from_menu()
        #create_project_drawer_page.create_project('no')
        # Заполняем таблицу трудозатрат
        #labor_cost_page = LaborCostPage(driver)
        #labor_cost_page.go_to_labor_cost_page()
        #sum_in_month = labor_cost_page.input_work_by_month()
        #print(sum_in_month)
        #
        #pivot_tab_page = PivotTabPage(driver)
        #pivot_tab_page.go_to_pivot_page()
        #pivot_moth_sum = pivot_tab_page.get_month_sum_reason()
        #print(pivot_moth_sum)

    # id-3104 3.2.2.1 Проверка правильности подсчета трудозатрат за месяц при отображении "Сводной таблицы" "За месяц-по неделям".
    def test_correct_month_summ_on_pivot_for_month_by_week(self, login, driver):
        # Создаем прект
        # create_project_drawer_page = CreateProjectDrawerPage(driver)
        # create_project_drawer_page.go_to_create_project_drawer_from_menu()
        # create_project_drawer_page.create_project('no')
        # Заполняем таблицу трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        sum_in_month = labor_cost_page.input_work_by_month()
        print(sum_in_month)
        # Берем сумму на сводной таблице проектов за месяц по неделям
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        pivot_tab_page.choose_period("month")
        sum_on_project = pivot_tab_page.get_sum_reason_on_project("month")
        assert str(sum_in_month) == sum_on_project
        # Берем сумму на сводной таблице пользователей за месяц по неделям
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.open_project_list()
        sum_on_user = pivot_tab_page.get_sum_reason_on_user("month")
        assert str(sum_in_month) == sum_on_user
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.three_mont_clear()

# id-3105 3.2.2.1 Проверка правильности подсчета трудозатрат за неделю при отображении "Сводной таблицы" "За неделю".
    def test_correct_week_summ_on_pivot_for_week(self, login, driver):
        # Создаем прект
        # create_project_drawer_page = CreateProjectDrawerPage(driver)
        # create_project_drawer_page.go_to_create_project_drawer_from_menu()
        # create_project_drawer_page.create_project('no')
        # Заполняем таблицу трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        #sum_in_month = labor_cost_page.input_work_by_month()
        #print(sum_in_month)
        # Берем сумму на сводной таблице проектов за месяц по неделям
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        #pivot_tab_page.choose_period("month")
        #sum_on_project = pivot_tab_page.get_sum_reason_on_project("month")
        #assert str(sum_in_month) == sum_on_project
        # Берем сумму на сводной таблице пользователей за месяц по неделям
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.open_project_list()
        #sum_on_user = pivot_tab_page.get_sum_reason_on_user("month")
        #assert str(sum_in_month) == sum_on_user
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.three_mont_clear()
