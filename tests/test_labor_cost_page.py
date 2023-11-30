import allure

from pages.labor_cost_page import LaborCostPage


@allure.suite("Таблица трудозатрат")
class TestLaborCostPage:

    #  id-270 3.1.1.2 Заполнение таблицы "Отчет трудозатрат".
    @allure.title("id-270 3.1.1.2 Заполнение таблицы Отчет трудозатрат")
    def test_filing_labor_cost_report_table(self, project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.choose_period("week")
        labor_cost_page.check_change_color_on_labor_cost_field()

    def test_mapping_labor_cost_page(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.check_title()
        labor_cost_page.check_period_select()
        labor_cost_page.check_add_to_project_button()
        count_add_overtime_work = labor_cost_page.get_number_last_month_day()
        assert count_add_overtime_work >= 28
        labor_cost_page.check_filter()

