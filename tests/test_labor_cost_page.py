import allure

from pages.all_project_page import AllProjectPage
from pages.create_project_drawer_page import CreateProjectDrawerPage
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
    @allure.title("id-1461 3.1.1.2 Содержание модального окна указания причин списания.")
    def test_contents_modal_window_indicating_the_reasons(self, login, driver):
        # Создаем проект с обязательным указанием причины списания
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        create_project_drawer_page.create_project('reason')
        # Проверяем наличие необходимых элементов на модальном окне
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_reason_window()
        labor_cost_page.check_title_reason_window()
        labor_cost_page.check_fields_reason_window()
        labor_cost_page.check_buttons_reason_window()
        labor_cost_page.close_reason_window()
        # Удаляем проект
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.delete_project()

    #  id-277 3.1.1.2 Удаление значений в таблице Отчет трудозатрат
    @allure.title("id-277 3.1.1.2 Удаление значений в таблице Отчет трудозатрат")
    def test_delete_values_on_labor_cost_report_table(self, project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.choose_period("week")
        labor_cost_page.check_delete_values_on_labor_cost_field()

    #  id-3165 3.1.1.5. Уведомление пользователей о несохраненных данных в разделе трудозатрат.
    @allure.title("id-3165 3.1.1.5. Уведомление пользователей о несохраненных данных в разделе трудозатрат.")
    def test_notify_users_about_unsaved_data(self, project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        value_after_input = labor_cost_page.input_unsaved_values_on_labor_cost_field()

        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()

        labor_cost_page.check_unsaved_data_window()
        labor_cost_page.go_to_labor_cost_page()
        value_after_return = labor_cost_page.get_values_on_labor_cost_field_to_check()

        assert value_after_input != value_after_return