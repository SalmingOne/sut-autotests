import time

import allure
import pytest
import testit
import datetime

from endpoints.project_endpoint import ProjectEndpoint
from pages.all_project_page import AllProjectPage
from pages.labor_cost_page import LaborCostPage
from locators.labor_cost_page_locators import LaborCostPageLocators
from pages.user_page import UserPage


@allure.suite("Таблица трудозатрат")
class TestLaborCostPage:

    @testit.workItemIds(270)
    @testit.displayName("3.1.1.2 Заполнение таблицы Отчет трудозатрат")
    @pytest.mark.smoke
    @allure.title("id-270 3.1.1.2 Заполнение таблицы Отчет трудозатрат")
    def test_filing_labor_cost_report_table(self, project_with_assignment, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.choose_period("week")
        labor_cost_page.check_change_color_on_labor_cost_field()

    @testit.workItemIds(267)
    @testit.displayName("3.1.1.1 Просмотр таблицы трудозатрат.")
    @pytest.mark.smoke
    @allure.title("id-267 3.1.1.1 Просмотр таблицы трудозатрат.")
    def test_mapping_labor_cost_page(self, project_with_assignment, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(1)
        labor_cost_page.check_title()
        labor_cost_page.check_add_to_project_button()
        labor_cost_page.check_period_select()
        labor_cost_page.check_add_overtime_work_button()
        labor_cost_page.check_add_absense_button()
        labor_cost_page.check_filter()
        labor_cost_page.check_open_widget_button()
        labor_cost_page.check_month_picker()
        labor_cost_page.check_next_previous_buttons()
        all_head_list, day_in_month = labor_cost_page.check_tab_head()
        labor_cost_page.check_week_days_head()
        labor_cost_page.check_colors_of_days()
        labor_cost_page.check_have_selected_days()
        tooltip_on_code = labor_cost_page.check_tooltip_on_project_code()
        labor_cost_page.check_save_and_disable_buttons()
        labor_cost_page.go_to_filter_by_project_name()
        tooltip_on_project = labor_cost_page.check_tooltip_on_project_code()
        # Проверяем, что в таблице есть отсутствия. Если нет добавляем
        if labor_cost_page.check_absence_on_tab() == 0:
            zero_reason_day = labor_cost_page.get_numbers_days_reason("zero")
            labor_cost_page.add_absence(zero_reason_day[0], 'vacation')
        else:
            pass
        labor_cost_page.check_stateman_tabs_heads()
        labor_cost_page.check_previous_absense_checkbox()
        labor_cost_page.check_tooltip_on_download_file_text()
        labor_cost_page.delete_all_absence()
        assert tooltip_on_code in tooltip_on_project, "Тултип отображается без имени проекта"
        assert 'Проект' in all_head_list, "Нет столбца Проект"
        assert 'Итого' in all_head_list, "Нет столбца Итого"

    @testit.workItemIds(1461)
    @testit.displayName("3.1.1.2 Содержание модального окна указания причин списания.")
    @pytest.mark.smoke
    @allure.title("id-1461 3.1.1.2 Содержание модального окна указания причин списания.")
    def test_contents_modal_window_indicating_the_reasons(self, project_with_labor_reason, login, driver):
        # Проверяем наличие необходимых элементов на модальном окне
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_reason_window()
        labor_cost_page.check_title_reason_window()
        labor_cost_page.check_fields_reason_window()
        labor_cost_page.check_buttons_reason_window()
        labor_cost_page.close_reason_window()

    @testit.workItemIds(277)
    @testit.displayName("3.1.1.2 Удаление значений в таблице Отчет трудозатрат")
    @pytest.mark.regress
    @allure.title("id-277 3.1.1.2 Удаление значений в таблице Отчет трудозатрат")
    def test_delete_values_on_labor_cost_report_table(self, project_with_assignment, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.choose_period("week")
        labor_cost_page.check_delete_values_on_labor_cost_field()

    @testit.workItemIds(1464)
    @testit.displayName("Пустой ввод в поле Причина")
    @pytest.mark.regress
    @allure.title('id-1464 Пустой ввод в поле "Причина"')
    def test_empty_entry_in_the_reason_field(self, project_with_labor_reason, login, driver):
        labor_cost_page = LaborCostPage(driver)
        locators = LaborCostPageLocators()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_reason_window(project_with_labor_reason["name"])
        labor_cost_page.input_hours_into_form(6)
        assert labor_cost_page.element_is_clickable(locators.SAVE_WINDOW_BUTTON) == False, 'Кнопка "Сохранить" активна'

    @testit.workItemIds(1476)
    @testit.displayName("Ввод пробела в поле Причина")
    @pytest.mark.regress
    @pytest.mark.labor_reason("True")
    @allure.title('id-1476 Ввод пробела в поле Причина')
    def test_enter_whitespace_in_the_reason_field(self, project_with_labor_reason, login, driver):
        labor_cost_page = LaborCostPage(driver)
        locators = LaborCostPageLocators()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_reason_window(project_with_labor_reason["name"])
        labor_cost_page.input_hours_into_form(6)
        labor_cost_page.input_reason_into_form(" ")
        labor_cost_page.save_hours_and_reason()

        assert labor_cost_page.element_is_visible(
            locators.GOAL_REASON_FIELD_IS_REQUIRED), 'Отсутствует сообщение "Поле обязательно"'

    @testit.workItemIds(1477)
    @testit.displayName("Превышение допустимого количества символов в поле Причина (255 максимальное количество)")
    @pytest.mark.regress
    @allure.title('id-1477 Превышение допустимого количества символов в поле "Причина" (255 максимальное количество)')
    def test_enter_over_max_characters_in_the_reason_field(self, project_with_labor_reason, login, driver):
        labor_cost_page = LaborCostPage(driver)
        locators = LaborCostPageLocators()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_reason_window(project_with_labor_reason["name"])
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

    @testit.workItemIds(3165)
    @testit.displayName("3.1.1.5. Уведомление пользователей о несохраненных данных в разделе трудозатрат.")
    @pytest.mark.regress
    @allure.title("id-3165 3.1.1.5. Уведомление пользователей о несохраненных данных в разделе трудозатрат.")
    def test_notify_users_about_unsaved_data(self, project_with_assignment, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        value_after_input = labor_cost_page.input_unsaved_values_on_labor_cost_field()

        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()

        labor_cost_page.check_unsaved_data_window()
        labor_cost_page.go_to_labor_cost_page()
        value_after_return = labor_cost_page.get_values_on_labor_cost_field_to_check()

        assert value_after_input != value_after_return, "В ячейке сохранились списанные трудозатраты"

    @testit.workItemIds(535)
    @testit.displayName("3.1.2.1. Добавление больничного/отпуска.")
    @pytest.mark.regress
    @allure.title("id-535 3.1.2.1. Добавление больничного/отпуска.")
    def test_add_sick_leave_and_vacation(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(1)  # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() > 0:
            labor_cost_page.click_previous_checkbox()
            labor_cost_page.delete_all_absence()
        else:
            pass
        # Добавляем 4 разных отсутствия
        zero_reason_day = labor_cost_page.get_numbers_days_reason("zero")
        labor_cost_page.add_absence(zero_reason_day[0], 'vacation')
        labor_cost_page.add_absence(zero_reason_day[1], 'administrative_leave')
        labor_cost_page.add_absence(zero_reason_day[2], 'sick_leave')
        labor_cost_page.add_absence(zero_reason_day[3], 'maternity_leave')
        absense_count = labor_cost_page.check_absence_on_tab()
        # Удаляем все заявления
        labor_cost_page.click_previous_checkbox()
        deleted_count = labor_cost_page.delete_all_absence()
        assert absense_count == 4, "Добавились не все 4 отсутствия"
        assert deleted_count == 4, "Не все 4 отсутствия есть на странице заявлений"

    @testit.workItemIds(543)
    @testit.displayName("Добавление отсутствия на период, в котором есть отсутствия")
    @pytest.mark.regress
    @allure.title("id-543 Добавление отсутствия на период, в котором есть отсутствия")
    def test_add_absence_twice_for_period(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем что нет заявлений в таблице. И если есть удаляем
        time.sleep(1)  # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() > 0:
            labor_cost_page.click_previous_checkbox()
            labor_cost_page.delete_all_absence()
        else:
            pass
        # Добавляем отсутствия в один и тот же день
        zero_reason_day = labor_cost_page.get_numbers_days_reason("zero")
        labor_cost_page.add_absence(zero_reason_day[0], 'vacation')
        labor_cost_page.add_absence(zero_reason_day[0], 'sick_leave')
        labor_cost_page.check_outer_absence()
        time.sleep(0.2)  # Без ожидания скрипт срабатывает раньше чем пройдет анимация
        labor_cost_page.click_previous_checkbox()
        labor_cost_page.delete_all_absence()

    @testit.workItemIds(539)
    @testit.displayName("Добавление отсутствия на период, в котором есть списанные трудозатраты")
    @pytest.mark.regress
    @allure.title("id-539 Добавление отсутствия на период, в котором есть списанные трудозатраты")
    def test_add_absence_to_labor_reason(self, project_with_overtime_work, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.add_absence_to_reason_day()

    @testit.workItemIds(2759)
    @testit.displayName("3.1.3.1. Добавление переработки на проект на дату, в которую добавлено отсутствие.")
    @pytest.mark.regress
    @allure.title("id-2759 3.1.3.1. Добавление переработки на проект на дату, в которую добавлено отсутствие.")
    def test_add_overwork_to_absence(self, project_with_assignment, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(1)  # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() > 0:
            labor_cost_page.click_previous_checkbox()
            labor_cost_page.delete_all_absence()
        else:
            pass
        # Добавляем отсутствие
        zero_reason_day = labor_cost_page.get_numbers_days_reason("zero")
        labor_cost_page.add_absence(zero_reason_day[0], 'vacation')
        labor_cost_page.add_overtime_work(zero_reason_day[0], 4)
        error_text = labor_cost_page.get_mui_error_text()
        labor_cost_page.click_previous_checkbox()
        labor_cost_page.delete_all_absence()

        assert error_text == 'В выбранный день добавлено отсутствие, выберите другой день для добавления переработки', "Не появилось сообщение об ошибке"

    @testit.workItemIds(3634)
    @testit.displayName("Ввод пробела в поле Причина на проект с обязательным указанием причины списания")
    @pytest.mark.regress
    @allure.title("id-3634 Ввод пробела в поле Причина на проект с обязательным указанием причины списания")
    def test_add_space_in_reason_field(self, f_overtime_reason_requirement, project_with_assignment, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(1)  # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() > 0:
            labor_cost_page.click_previous_checkbox()
            labor_cost_page.delete_all_absence()
        else:
            pass
        zero_reason_day = labor_cost_page.get_numbers_days_reason("zero")
        error_text = labor_cost_page.check_overtime_work_space_in_reason_field(zero_reason_day[0], 5, ' ')
        time.sleep(2)
        assert error_text == 'Укажите причину переработки', "Не появилось сообщение об ошибке"

    @testit.workItemIds(2737)
    @testit.displayName("Пустой ввод в обязательные поля при добавлении переработки")
    @pytest.mark.regress
    @allure.title("id-2737 Пустой ввод в обязательные поля при добавлении переработки")
    def test_empty_enter(self, simple_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(1)  # Без ожидания скрипт срабатывает до загрузки страницы
        tooltip_text = labor_cost_page.check_disable_submit_button_and_tooltip()
        assert tooltip_text == 'Заполните все обязательные поля', "Не появился тултип об обязательности заполнения полей"

    @testit.workItemIds(2725)
    @testit.displayName("Добавление переработки на проект")
    @pytest.mark.regress
    @allure.title("id-2725 Добавление переработки на проект")
    def test_adding_processing_to_a_project(self, project_with_assignment, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        zero_reason_day = labor_cost_page.get_numbers_days_reason("zero")
        labor_cost_page.input_labor_reason_by_project("AutoTestProject", zero_reason_day[0] + 2, 6)
        labor_cost_page.add_overtime_work(zero_reason_day[0], 4, "AutoTestProject")
        time.sleep(0.5)
        project_day_cell_contents = labor_cost_page.get_project_day_cell_contents("AutoTestProject",
                                                                                  zero_reason_day[0] + 2)
        total_column = labor_cost_page.get_project_total("AutoTestProject")
        in_total_row = labor_cost_page.get_day_total_raw(zero_reason_day[0] + 1)
        labor_cost_page.save_labor_reason()
        labor_cost_page.check_project_reason_tab("AutoTestProject")
        alert_text = labor_cost_page.get_alert_message()
        assert 'Переработка успешно добавлена' in alert_text, "Не появилось сообщение о добавлении переработки"
        assert project_day_cell_contents == total_column, "Нет переработки в столице Итого"
        assert project_day_cell_contents == in_total_row, "Нет переработки в строке Итого"

    @testit.workItemIds(2710)
    @testit.displayName("Содержание дровера Добавление переработки")
    @pytest.mark.regress
    @allure.title("id-2710 Содержание дровера Добавление переработки")
    def test_content_drover_adding_overwork(self, f_overtime_reason_requirement, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.open_overtime_drover()
        labor_cost_page.check_fields_on_overtime_drover()

    @testit.workItemIds(1356)
    @testit.displayName("Редактирование отсутствий")
    @pytest.mark.regress
    @allure.title("id-1356 Редактирование отсутствий")
    def test_editing_absences(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем, что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(1)  # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() > 0:
            labor_cost_page.click_previous_checkbox()
            labor_cost_page.delete_all_absence()
        else:
            pass
        zero_reason_day = labor_cost_page.get_numbers_days_reason('zero')
        labor_cost_page.add_absence(zero_reason_day[1], 'vacation')
        labor_cost_page.click_previous_checkbox()
        labor_cost_page.open_kebab_redact()
        to_date = labor_cost_page.change_date_absense(zero_reason_day[0])
        time.sleep(0.5)  # Без ожидания не успевает прогрузиться
        start_date, end_date = labor_cost_page.check_data_absense()
        labor_cost_page.delete_all_absence()
        assert to_date == start_date, 'Измененная дата начала отсутствия не сохранилась'
        assert to_date == end_date, 'Измененная дата конца отсутствия не сохранилась'

    @testit.workItemIds(1359)
    @testit.displayName("Удаление отсутствий")
    @pytest.mark.regress
    @allure.title("id-1359 Удаление отсутствий")
    def test_delete_absences(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем, что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(0.5)  # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() > 0:
            labor_cost_page.click_previous_checkbox()
            labor_cost_page.delete_all_absence()
        else:
            pass
        zero_reason_day = labor_cost_page.get_numbers_days_reason('zero')
        labor_cost_page.add_absence(zero_reason_day[1], 'maternity_leave')
        labor_cost_page.click_previous_checkbox()
        start_date, end_date = labor_cost_page.check_data_absense()
        drawer_description_text = labor_cost_page.check_delete_absense()
        time.sleep(0.5)  # Без ожидания не успевает прогрузиться алерт
        alert_text = labor_cost_page.get_alert_message()
        assert start_date in drawer_description_text, "Даты начала отсутствия нет на дровере удаления"
        assert end_date in drawer_description_text, "Даты конца отсутствия нет на дровере удаления"
        assert 'Отсутствие успешно удалено' in alert_text, "Не появилось сообщение об удалении отсутствия"

    @testit.workItemIds(1361)
    @testit.displayName("Отмена удаления отсутствия")
    @pytest.mark.regress
    @allure.title("id-1361 Отмена удаления отсутствия")
    def test_cansel_delete_absences(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем, что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(0.5)  # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() > 0:
            labor_cost_page.click_previous_checkbox()
            labor_cost_page.delete_all_absence()
        else:
            pass
        zero_reason_day = labor_cost_page.get_numbers_days_reason('zero')
        labor_cost_page.add_absence(zero_reason_day[1], 'administrative_leave')
        labor_cost_page.click_previous_checkbox()
        start_date, end_date = labor_cost_page.check_data_absense()
        labor_cost_page.cansel_delete_absense()
        start_date_outer, end_date_outer = labor_cost_page.check_data_absense()
        labor_cost_page.delete_all_absence()
        assert start_date == start_date_outer, "Дата начала отсутствия изменилась или удалилось отсутствие"
        assert end_date == end_date_outer, "Дата конца отсутствия изменилась или удалилось отсутствие"

    @testit.workItemIds(547)
    @testit.displayName("Фильтр таблицы Отсутствие по времени. Прошедшие отсутствия.")
    @pytest.mark.regress
    @allure.title("id-547 Фильтр таблицы Отсутствие по времени. Прошедшие отсутствия.")
    def test_filter_past_absences(self, project_with_assignment, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем, что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        # Временное решение
        labor_cost_page.go_to_previous_period()
        time.sleep(1)  # Без ожидания скрипт срабатывает до загрузки страницы
        if labor_cost_page.check_absence_on_tab() == 0:
            zero_reason_day = labor_cost_page.get_numbers_days_reason('zero')
            labor_cost_page.add_absence(zero_reason_day[1], 'sick_leave', 'yeas')
        else:
            pass
        before = labor_cost_page.get_count_absense()
        labor_cost_page.click_previous_checkbox()
        after = labor_cost_page.get_count_absense()
        labor_cost_page.delete_all_absence()
        assert before != after, "Количество заявлений не изменилось после включения чекбокса прошедшие отсутствия"

    @testit.workItemIds(3383)
    @testit.displayName("3.1.3.1. Добавление переработки на проект, который завершен")
    @pytest.mark.regress
    @allure.title("id-3383 3.1.3.1. Добавление переработки на проект, который завершен")
    def test_adding_overtime_work_to_a_completed_project(self, finished_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_overtime_drover()
        labor_cost_page.check_adding_overtime_work_to_a_completed_project()

    @testit.workItemIds(258)
    @testit.displayName("1.3.1.7 Отмена добавления пользователем себя на проект")
    @pytest.mark.regress
    @allure.title("id-258 1.3.1.7 Отмена добавления пользователем себя на проект")
    def test_canceling_a_user_from_adding_himself_to_a_project(self, no_resources_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.press_add_to_project_button()
        labor_cost_page.field_adding_himself_to_a_project(no_resources_project["name"])
        labor_cost_page.press_cancel_button_adding_himself_to_a_project()
        assert not labor_cost_page.get_project_on_tab(no_resources_project["name"]), "Пользователь добавился на проект"

    @testit.workItemIds(259)
    @testit.displayName("1.3.1.7 Н. Обязательные поля не заполнены")
    @pytest.mark.regress
    @allure.title("id-259 1.3.1.7 Н. Обязательные поля не заполнены")
    def test_adding_himself_to_a_project_required_fields_are_not_filled(self, no_resources_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.press_add_to_project_button()
        labor_cost_page.check_clickable_save_button_in_adding_himself_to_a_project_drawer(no_resources_project["name"])

    @testit.workItemIds(11932)
    @testit.displayName("1.3.1.7 Проверка работы функционала Добавление себя на проект")
    @pytest.mark.regress
    @allure.title("id-11932 1.3.1.7 Проверка работы функционала Добавление себя на проект")
    def test_checking_the_functionality_adding_himself_to_a_project(self, no_resources_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        projects_on_tab = labor_cost_page.get_all_project_name_on_tab()
        project_endpoint = ProjectEndpoint()
        adding_himself, no_adding_himself = project_endpoint.get_name_projects_with_adding_himself_and_no_adding()
        labor_cost_page.press_add_to_project_button()
        projects_in_field = labor_cost_page.get_project_name_in_adding_himself_to_a_project_drawer()
        labor_cost_page.remove_project_on_tab(projects_on_tab, adding_himself)
        assert adding_himself == projects_in_field, \
            "В дропдауне отображаются не все проекты с самостоятельным добавлением"

    @testit.workItemIds(2783)
    @testit.displayName("3.1.3.2. Редактирование переработки на проекте с обязательным указанием причины списания")
    @pytest.mark.regress
    @allure.title("id-2783 3.1.3.2. Редактирование переработки на проекте с обязательным указанием причины списания")
    def test_edit_overwork_obligatory_reason(self, second_project, f_overtime_reason_requirement, login, driver):
        labor_cost_page = LaborCostPage(driver)
        today = labor_cost_page.get_date_list_from_today()
        labor_cost_page.add_overtime_work_without_file(today[0]-1, 2, second_project['name'])
        labor_cost_page.field_reason_overwork("Много работал")
        # +1 т.к. считает с первого столбца (Проект)
        project_day_cell_contents_before = labor_cost_page.get_project_day_cell_contents(second_project['name'], today[0]+1)
        total_column_before = labor_cost_page.get_project_total(second_project['name'])
        in_total_row_before = labor_cost_page.get_day_total_raw(today[0])
        # -1 иначе выбирает завтрашний день. Хотя при выводе print(today[0]) число верное
        labor_cost_page.open_overwork_drover_for_specific_day(today[0]-1, second_project['name'])
        labor_cost_page.check_data_from_drover(2, "Много работал")
        labor_cost_page.editing_overwork(5, 'Еще больше работал')
        project_day_cell_contents_after = labor_cost_page.get_project_day_cell_contents(second_project['name'], today[0]+1)
        total_column_after = labor_cost_page.get_project_total(second_project['name'])
        in_total_row_after = labor_cost_page.get_day_total_raw(today[0])
        assert project_day_cell_contents_after != project_day_cell_contents_before, 'Часы переработки не изменились'
        assert total_column_after != total_column_before, 'Часы переработки не изменились'
        assert in_total_row_after != in_total_row_before, 'Часы переработки не изменились'

    @testit.workItemIds(946)
    @testit.displayName("1.4.3. Списание часов трудозатрат на восстановленный из архива проект")
    @pytest.mark.regress
    @allure.title("id-946 1.4.3. Списание часов трудозатрат на восстановленный из архива проект")
    def test_writing_off_labor_hours_for_a_project_restored_from_the_archive(self, archive_project_with_assignment, login, driver):
        labor_cost_page = LaborCostPage(driver)
        projects_page = AllProjectPage(driver)
        projects_page.go_to_all_project_page()
        projects_page.check_archiving_a_project_on_tab(archive_project_with_assignment['name'])
        projects_page.unzipping_the_project(archive_project_with_assignment['name'])
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(2)
        today = labor_cost_page.get_date_list_from_today()
        labor_cost_page.input_labor_reason_by_project(archive_project_with_assignment['name'], today[0], 7)
        labor_cost_page.save_labor_reason()
        time.sleep(1)
        assert 'Трудозатраты сохранены' in labor_cost_page.get_alert_message(), "Трудозатраты не сохранились"

    @testit.workItemIds(11864)
    @testit.displayName("3.1.1.4 Просмотр таблицы Трудозатраты за неделю (с переключением периодов)")
    @pytest.mark.regress
    @allure.title("id-11864 3.1.1.4 Просмотр таблицы Трудозатраты за неделю (с переключением периодов)")
    def test_viewing_the_effort_table_for_a_week_with_period_switching(self, simple_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.choose_period("week")
        assert 'Проект' and 'Итого' in labor_cost_page.get_tab_header(), "В шапке столбцов нет Проект и Итого"
        assert 'пн' and 'вт' and 'ср' and 'чт' and 'пт' and 'сб' and 'вс' in labor_cost_page.get_tab_header_week_days(), \
            "В шапке столбцов нет названий дней недели"
        labor_cost_page.check_next_previous_buttons()
        assert labor_cost_page.get_month_or_week_on_tab() == str(datetime.date.today().isocalendar().week) + ' неделя', \
            "Отображается некорректный номер недели"
        assert labor_cost_page.get_week_dates() == ' ' + labor_cost_page.week_day(), \
            "Отображаются некорректные даты недели"
        labor_cost_page.check_filter()
        labor_cost_page.check_change_period_by_week()

    @testit.workItemIds(3377)
    @testit.displayName("3.1.3.2. Редактирование переработки на проекте с обязательным приложением файлов")
    @pytest.mark.regress
    @allure.title("id-3377 3.1.3.2. Редактирование переработки на проекте с обязательным приложением файлов")
    def test_edit_overwork_obligatory_file(self, project_with_attach_files, login, driver):
        labor_cost_page = LaborCostPage(driver)
        today = labor_cost_page.get_date_list_from_today()
        labor_cost_page.add_overtime_work_with_file(today[0] - 1, 2, project_with_attach_files['name'])
        # +1 т.к. считает с первого столбца (Проект)
        project_day_cell_contents_before = labor_cost_page.get_project_day_cell_contents(project_with_attach_files['name'],
                                                                                         today[0] + 1)
        total_column_before = labor_cost_page.get_project_total(project_with_attach_files['name'])
        in_total_row_before = labor_cost_page.get_day_total_raw(today[0])
        # -1 иначе выбирает завтрашний день. Хотя при выводе print(today[0]) число верное
        labor_cost_page.open_overwork_drover_for_specific_day(today[0] - 1, project_with_attach_files['name'])
        labor_cost_page.check_data_with_file_from_drover(2, "переработка.docx")
        labor_cost_page.editing_overwork_with_file(5)
        project_day_cell_contents_after = labor_cost_page.get_project_day_cell_contents(project_with_attach_files['name'],
                                                                                        today[0] + 1)
        total_column_after = labor_cost_page.get_project_total(project_with_attach_files['name'])
        in_total_row_after = labor_cost_page.get_day_total_raw(today[0])
        assert project_day_cell_contents_after != project_day_cell_contents_before, 'Часы переработки не изменились'
        assert total_column_after != total_column_before, 'Часы переработки не изменились'
        assert in_total_row_after != in_total_row_before, 'Часы переработки не изменились'

    @testit.workItemIds(3167)
    @testit.displayName("3.1.1.5. Отмена перехода на другую страницу без сохранения данных в разделе трудозатрат")
    @pytest.mark.regress
    @allure.title("id-3167 3.1.1.5. Отмена перехода на другую страницу без сохранения данных в разделе трудозатрат")
    def test_cancel_moving_without_saving_in_labor_cost(self, simple_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        user_page = UserPage(driver)
        today = labor_cost_page.get_date_list_from_today()
        labor_cost_page.input_labor_reason_by_project(simple_project['name'], today[1], 4)
        in_total_row_before = labor_cost_page.get_day_total_raw(today[0])
        user_page.go_to_user_page()
        time.sleep(1)
        labor_cost_page.cancel_moving_to_another_page()
        in_total_row_after = labor_cost_page.get_day_total_raw(today[0])
        assert in_total_row_after == in_total_row_before, 'Изменения не сохранились'