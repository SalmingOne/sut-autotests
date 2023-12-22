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
        # Проверяем, что нет заявлений в таблице. И если есть удаляем
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
        time.sleep(0.5)  # Без ожидания не успевает прогрузиться
        start_date, end_date = statement_page.check_data_absense()
        statement_page.delete_all_absence()
        assert to_date == start_date, 'Измененная дата начала отсутствия не сохранилась'
        assert to_date == end_date, 'Измененная дата конца отсутствия не сохранилась'

    @allure.title("id-1359 Удаление отсутствий")
    def test_delete_absences(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        statement_page = StatementPage(driver)
        # Проверяем, что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(0.5)  # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() > 0:
            statement_page.go_to_statement_page()
            statement_page.click_previous_checkbox()
            statement_page.delete_all_absence()
        else:
            pass
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.add_absence(1, 'vacation')
        statement_page.go_to_statement_page()
        statement_page.click_previous_checkbox()
        start_date, end_date = statement_page.check_data_absense()
        drawer_description_text = statement_page.check_delete_absense()
        time.sleep(0.5)  # Без ожидания не успевает прогрузиться аллерт
        allert_text = statement_page.get_allert_message()
        assert start_date in drawer_description_text, "Даты начала отсутствия нет на дровере удаления"
        assert end_date in drawer_description_text, "Даты конца отсутствия нет на дровере удаления"
        assert 'Отсутствие успешно удалено' in allert_text, "Не появилось сообщение об удалении отсутствия"

    @allure.title("id-1361 Отмена удаления отсутствия")
    def test_cansel_delete_absences(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        statement_page = StatementPage(driver)
        # Проверяем, что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(0.5)  # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() > 0:
            statement_page.go_to_statement_page()
            statement_page.click_previous_checkbox()
            statement_page.delete_all_absence()
        else:
            pass
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.add_absence(1, 'vacation')
        statement_page.go_to_statement_page()
        statement_page.click_previous_checkbox()
        start_date, end_date = statement_page.check_data_absense()
        statement_page.cansel_delete_absense()
        start_date_outer, end_date_outer = statement_page.check_data_absense()
        statement_page.delete_all_absence()
        assert start_date == start_date_outer, "Дата начала отсутствия изменилась или удалилось отсутствие"
        assert end_date == end_date_outer, "Дата конца отсутствия изменилась или удалилось отсутствие"
