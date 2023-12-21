import time
import allure
from pages.labor_cost_page import LaborCostPage
from pages.statement_page import StatementPage


@allure.suite("Заявления")
class TestStatementPage:
    @allure.title("id-1356 Редактирование отсутствий")
    def test_editing_absences(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        statement_page = StatementPage(driver)
        # Проверяем что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(1)  # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() > 0:
            statement_page.go_to_statement_page()
            statement_page.click_previous_checkbox()
            statement_page.delete_all_absence()
        else:
            pass
        labor_cost_page.go_to_labor_cost_page()
        zero_reason_day = labor_cost_page.get_numbers_days_reason('zero')
        labor_cost_page.add_absence(1, 'vacation')
        statement_page.go_to_statement_page()
        statement_page.click_previous_checkbox()
        statement_page.open_kebab_redact()
        to_date = statement_page.change_date_absense(zero_reason_day[0])
        time.sleep(0.5)
        start_date, end_date = statement_page.check_data_absense()
        statement_page.delete_all_absence()
        assert to_date == start_date, "После редактирования дата начала отсутствия не изменилась"
        assert to_date == end_date, "После редактирования дата конца отсутствия не изменилась"
