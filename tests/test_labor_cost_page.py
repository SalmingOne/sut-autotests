import time

import allure
import pytest


from pages.all_project_page import AllProjectPage
from pages.labor_cost_page import LaborCostPage
from locators.labor_cost_page_locators import LaborCostPageLocators
from pages.statement_page import StatementPage


@allure.suite("Таблица трудозатрат")
class TestLaborCostPage:

    #  id-270 3.1.1.2 Заполнение таблицы "Отчет трудозатрат".
    @allure.title("id-270 3.1.1.2 Заполнение таблицы Отчет трудозатрат")
    def test_filing_labor_cost_report_table(self, f_create_temp_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.choose_period("week")
        labor_cost_page.check_change_color_on_labor_cost_field()

    #  id-267 3.1.1.1 Просмотр таблицы трудозатрат.
    @allure.title("id-267 3.1.1.1 Просмотр таблицы трудозатрат.")
    def test_mapping_labor_cost_page(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.check_title()
        labor_cost_page.check_period_select()
        labor_cost_page.check_add_to_project_button()
        count_add_overtime_work = labor_cost_page.get_number_last_month_day()
        first_column, all_day = labor_cost_page.check_tab_head()
        labor_cost_page.check_filter()
        labor_cost_page.check_open_widget_button()
        labor_cost_page.check_month_picker()
        labor_cost_page.check_next_previous_buttons()
        labor_cost_page.check_week_days_head()
        labor_cost_page.check_colors_of_days()
        labor_cost_page.check_have_selected_days()
        tooltip_on_code = labor_cost_page.check_tooltip_on_project_code()
        labor_cost_page.check_save_and_disable_buttons()
        labor_cost_page.go_to_filter_by_project_name()
        tooltip_on_project = labor_cost_page.check_tooltip_on_project_code()

        assert tooltip_on_code in tooltip_on_project, "Тултип отображается без имени проекта"
        assert 'Проект' in first_column, "Нет столбца Проект"
        assert count_add_overtime_work == all_day, "Количество кнопок переработки не равно количеству дней"

    #  id-1461 3.1.1.2 Содержание модального окна указания причин списания.
    @pytest.mark.labor_reason("True")
    @allure.title("id-1461 3.1.1.2 Содержание модального окна указания причин списания.")
    def test_contents_modal_window_indicating_the_reasons(self, f_create_temp_project, login, driver):
        # Проверяем наличие необходимых элементов на модальном окне
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_reason_window()
        labor_cost_page.check_title_reason_window()
        labor_cost_page.check_fields_reason_window()
        labor_cost_page.check_buttons_reason_window()
        labor_cost_page.close_reason_window()

    #  id-277 3.1.1.2 Удаление значений в таблице Отчет трудозатрат
    @allure.title("id-277 3.1.1.2 Удаление значений в таблице Отчет трудозатрат")
    def test_delete_values_on_labor_cost_report_table(self, f_create_temp_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.choose_period("week")
        labor_cost_page.check_delete_values_on_labor_cost_field()

    @pytest.mark.labor_reason("True")
    @allure.title('id-1464 Пустой ввод в поле "Причина"')
    def test_empty_entry_in_the_reason_field(self, driver, login, f_create_temp_project):
        labor_cost_page = LaborCostPage(driver)
        locators = LaborCostPageLocators()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_reason_window(f_create_temp_project["name"])
        labor_cost_page.input_hours_into_form(6)

        assert labor_cost_page.element_is_clickable(locators.SAVE_WINDOW_BUTTON) == False, 'Кнопка "Сохранить" активна'

    @pytest.mark.labor_reason("True")
    @allure.title('id-1476 Ввод пробела в поле "Причина"')
    def test_enter_whitespace_in_the_reason_field(self, driver, login, f_create_temp_project):
        labor_cost_page = LaborCostPage(driver)
        locators = LaborCostPageLocators()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_reason_window(f_create_temp_project["name"])
        labor_cost_page.input_hours_into_form(6)
        labor_cost_page.input_reason_into_form(" ")
        labor_cost_page.save_hours_and_reason()

        assert labor_cost_page.element_is_visible(
            locators.GOAL_REASON_FIELD_IS_REQUIRED), 'Отсутствует сообщение "Поле обязательно"'

    @pytest.mark.labor_reason("True")
    @allure.title('id-1477 Превышение допустимого количества символов в поле "Причина" (255 максимальное количество)')
    def test_enter_over_max_characters_in_the_reason_field(self, driver, login, f_create_temp_project):
        labor_cost_page = LaborCostPage(driver)
        locators = LaborCostPageLocators()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_reason_window(f_create_temp_project["name"])
        labor_cost_page.input_hours_into_form(6)
        labor_cost_page.input_reason_into_form("12345678901234567890123456789012345678901234567890"
                                               "12345678901234567890123456789012345678901234567890"
                                               "12345678901234567890123456789012345678901234567890"
                                               "12345678901234567890123456789012345678901234567890"
                                               "12345678901234567890123456789012345678901234567890"
                                               "123456")
        labor_cost_page.save_hours_and_reason()

        assert labor_cost_page.element_is_visible(
            locators.GOAL_NUMBER_OF_CHARACTERS_OVER_MAX), 'Отсутствует сообщение "Максимальное количество символов: 255"'

    #  id-3165 3.1.1.5. Уведомление пользователей о несохраненных данных в разделе трудозатрат.
    @allure.title("id-3165 3.1.1.5. Уведомление пользователей о несохраненных данных в разделе трудозатрат.")
    def test_notify_users_about_unsaved_data(self, f_create_temp_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        value_after_input = labor_cost_page.input_unsaved_values_on_labor_cost_field()

        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()

        labor_cost_page.check_unsaved_data_window()
        labor_cost_page.go_to_labor_cost_page()
        value_after_return = labor_cost_page.get_values_on_labor_cost_field_to_check()

        assert value_after_input != value_after_return, "В ячейке сохранились списанные трудозатраты"

    #  id-535 3.1.2.1. Добавление больничного/отпуска.
    @allure.title("id-535 3.1.2.1. Добавление больничного/отпуска.")
    def test_add_sick_leave_and_vacation(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        statement_page = StatementPage(driver)
        # Проверяем что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(1) # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() > 0:
            statement_page.go_to_statement_page()
            statement_page.delete_all_absence()
        else:
            pass
        # Добавляем 4 разных отсутствия
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.add_absence(0, 'vacation')
        labor_cost_page.add_absence(1, 'administrative_leave')
        labor_cost_page.add_absence(2, 'sick_leave')
        labor_cost_page.add_absence(3, 'maternity_leave')
        absense_count = labor_cost_page.check_absence_on_tab()
        # Удаляем все заявления
        statement_page.go_to_statement_page()
        deleted_count = statement_page.delete_all_absence()
        assert absense_count == 4, "Добавились не все 4 отсутствия"
        assert deleted_count == 4, "Не все 4 отсутсвия есть на странице заявлений"
