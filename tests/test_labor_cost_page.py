import locale
import platform
import time

import allure
import pytest
import testit
import datetime

from endpoints.project_endpoint import ProjectEndpoint
from pages.all_project_page import AllProjectPage
from pages.labor_cost_page import LaborCostPage
from locators.labor_cost_page_locators import LaborCostPageLocators
from pages.project_card_page import ProjectCardPage
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
        labor_cost_page.click_previous_checkbox()
        if labor_cost_page.check_absence_on_tab() > 0:
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
        time.sleep(1)
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
        user_page.go_to_user_page_simple()
        time.sleep(1)
        labor_cost_page.cancel_moving_to_another_page()
        in_total_row_after = labor_cost_page.get_day_total_raw(today[0])
        assert in_total_row_after == in_total_row_before, 'Изменения не сохранились'

    @testit.workItemIds(11865)
    @testit.displayName("3.1.1.4 Просмотр таблицы Трудозатраты за месяц(с переключением периодов)")
    @pytest.mark.regress
    @allure.title("id-11865 3.1.1.4 Просмотр таблицы Трудозатраты за месяц (с переключением периодов)")
    def test_viewing_the_effort_table_for_a_month_with_period_switching(self, simple_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        assert 'Проект' and 'Итого' in labor_cost_page.get_tab_header(), "В шапке столбцов нет Проект и Итого"
        assert 'пн' and 'вт' and 'ср' and 'чт' and 'пт' and 'сб' and 'вс' in labor_cost_page.get_tab_header_week_days(), \
            "В шапке столбцов нет названий дней недели"
        labor_cost_page.check_next_previous_buttons()
        locale.setlocale(locale.LC_TIME, 'ru_RU')
        assert labor_cost_page.get_month_or_week_on_tab() == datetime.date.today().strftime('%B %Y'), \
            "Отображается некорректный месяц и год"
        labor_cost_page.check_filter()
        labor_cost_page.check_change_period_by_month()

    @testit.workItemIds(3381)
    @testit.displayName("3.1.3.1 Приложение к переработке файла с превышением размера")
    @pytest.mark.regress
    @allure.title("id-3381 3.1.3.1 Приложение к переработке файла с превышением размера")
    def test_add_oversized_file_to_overwork(self, project_with_attach_files, login, driver):
        labor_cost_page = LaborCostPage(driver)
        today = labor_cost_page.get_date_list_from_today()
        labor_cost_page.add_overwork_with_file_5mb(today[0] - 1, 2, project_with_attach_files['name'])

    @testit.workItemIds(3379)
    @testit.displayName("3.1.2.1 Добавление отсутствий из таблицы трудозатрат с обязательным приложением файлов.")
    @pytest.mark.regress
    @allure.title("id-3379 3.1.2.1 Добавление отсутствий из таблицы трудозатрат с обязательным приложением файлов.")
    def test_add_adding_absences_with_the_obligatory_attachment_of_files(self, project_with_attach_files, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем что нет заявлений в таблице. И если есть удаляем
        if labor_cost_page.check_absence_on_tab() > 0:
            labor_cost_page.click_previous_checkbox()
            labor_cost_page.delete_all_absence()
        else:
            pass
        absense_count_before = labor_cost_page.check_absence_on_tab()
        zero_reason_day = labor_cost_page.get_numbers_days_reason('zero')
        labor_cost_page.add_absence(zero_reason_day[0], 'sick_leave')
        time.sleep(1)
        assert labor_cost_page.get_alert_message() == ['Файл прикреплён', 'Больничный/отпуск успешно добавлен'], \
            "Не появились необходимые сообщения"
        absense_count_after = labor_cost_page.check_absence_on_tab()
        assert absense_count_before != absense_count_after, "Количество отсутствий не изменилось"
        labor_cost_page.click_previous_checkbox()
        assert labor_cost_page.check_text_on_page('Больничный'), "Отсутствия нет в разделе заявлений"
        assert labor_cost_page.check_text_on_page('Скачать файлы (1)'), "В разделе заявлений нет текста Скачать файл"
        labor_cost_page.delete_all_absence()

    @testit.workItemIds(1357)
    @testit.displayName("3.1.2.4. Редактирование отсутствий если выбранный период пересекается с другими отсутствиями")
    @pytest.mark.regress
    @allure.title("id-1357 3.1.2.4. Редактирование отсутствий если выбранный период пересекается с другими отсутствиями")
    def test_add_editing_absences_if_the_selected_period_overlaps_with_other_absences(self, project_with_attach_files, login,
                                                                         driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем что нет заявлений в таблице. И если есть удаляем
        if labor_cost_page.check_absence_on_tab() > 0:
            labor_cost_page.click_previous_checkbox()
            labor_cost_page.delete_all_absence()
        else:
            pass
        zero_reason_day = labor_cost_page.get_numbers_days_reason('zero')
        labor_cost_page.add_absence(zero_reason_day[-2], 'administrative_leave')
        labor_cost_page.add_absence(zero_reason_day[-3], 'sick_leave')
        time.sleep(1) # Не успевает прогрузиться
        labor_cost_page.check_editing_absences_if_the_selected_period_overlaps_with_other_absences(zero_reason_day[-3])
        labor_cost_page.click_previous_checkbox()
        labor_cost_page.delete_all_absence()

    @testit.workItemIds(2736)
    @testit.displayName("3.1.3.1. Добавление переработки на проект с обязательным указанием причины списания")
    @pytest.mark.regress
    @allure.title("id-2736 3.1.3.1. Добавление переработки на проект с обязательным указанием причины списания")
    def test_adding_processing_to_a_project_with_mandatory_indication_of_the_reason(self, project_with_labor_reason,
                                                                                    login, f_overtime_reason_requirement, driver):
        labor_cost_page = LaborCostPage(driver)
        zero_reason_day = labor_cost_page.get_numbers_days_reason("zero")
        labor_cost_page.add_overtime_work_without_file(zero_reason_day[-2], 3, project_with_labor_reason['name'])
        labor_cost_page.field_reason_overwork("Много работал")
        time.sleep(2)
        project_day_cell_contents = labor_cost_page.get_project_day_cell_contents(project_with_labor_reason['name'],
                                                                                  zero_reason_day[-2] + 2)
        total_column = labor_cost_page.get_project_total(project_with_labor_reason['name'])
        assert project_day_cell_contents == total_column == '0+3', "Переработка не отразилась в строке и столбце Итого"
        assert 'Переработка успешно добавлена' in labor_cost_page.get_alert_message(), \
            "Не появилось сообщение о добавлении переработки"
        reason, status = labor_cost_page.check_overtime_on_reason_tab(project_with_labor_reason['name'])
        assert reason == 'Много работал', "Не отобразился или отобразился некорректно текст причины переработки"
        assert status == 'На рассмотрении', "Не отобразился или отобразился некорректно статус причины переработки"

    @testit.workItemIds(10166)
    @testit.displayName("3.1.3.1 Отображение тултипа для поля загрузки файла при создании переработки")
    @pytest.mark.regress
    @allure.title("id-10166 3.1.3.1 Отображение тултипа для поля загрузки файла при создании переработки")
    def test_display_tooltip_for_file_upload_field_when_creating_a_rework(self, project_with_labor_reason, login, driver):
        labor_cost_page = LaborCostPage(driver)
        zero_reason_day = labor_cost_page.get_numbers_days_reason("zero")
        labor_cost_page.check_tooltip_overtime_work_file_field(zero_reason_day[-2], 3, project_with_labor_reason['name'])

    @testit.workItemIds(2784)
    @testit.displayName("3.1.3.2. Отмена редактирования переработок в таблице трудозатраты")
    @pytest.mark.regress
    @allure.title("id-2784 3.1.3.2. Отмена редактирования переработок в таблице трудозатраты")
    def test_cancel_editing_overtime_in_the_labor_costs_table(self, project_with_labor_reason, login, driver):
        labor_cost_page = LaborCostPage(driver)
        zero_reason_day = labor_cost_page.get_numbers_days_reason("zero")
        labor_cost_page.add_overtime_work_with_file(
            zero_reason_day[-2],
            2,
            project_with_labor_reason['name']
        )
        project_day_cell_contents_before = labor_cost_page.get_project_day_cell_contents(
            project_with_labor_reason['name'],
            zero_reason_day[-2] + 2
        )
        time.sleep(4)
        labor_cost_page.redact_overtime_on_reason_tab(project_with_labor_reason['name'])
        labor_cost_page.cancel_redact_overtime(7)
        project_day_cell_contents_after = labor_cost_page.get_project_day_cell_contents(
            project_with_labor_reason['name'],
            zero_reason_day[-2] + 2
        )
        assert project_day_cell_contents_before == project_day_cell_contents_after, "Переработка изменилась"

    @testit.workItemIds(12194)
    @testit.displayName("3.1.3.2. Редактирование даты переработки в таблице трудозатраты при заполненных трудозатратах")
    @pytest.mark.regress
    @allure.title("id-12194 3.1.3.2. Редактирование даты переработки в таблице трудозатраты при заполненных трудозатратах")
    def test_editing_date_when_labor_costs_are_filled(self, project_with_work_and_overtime_work, login, driver):
        labor_cost_page = LaborCostPage(driver)
        today = labor_cost_page.get_date_list_from_today()
        # Перенос переработки на день с трудозатратами
        labor_cost_page.change_overtime_work_date(project_with_work_and_overtime_work['name'], labor_cost_page.get_day_before(-1))
        time.sleep(1)
        work = labor_cost_page.get_project_day_cell_contents(
            project_with_work_and_overtime_work['name'],
            today[1] + 1
        )
        assert work == '6+3', "Переработка не перенеслась на день с трудозатратами или не корректно отображается"
        # Перенос переработки на день без трудозатрат
        labor_cost_page.change_overtime_work_date(project_with_work_and_overtime_work['name'],
                                                  labor_cost_page.get_day_before(-3))
        time.sleep(3)
        zero_work = labor_cost_page.get_project_day_cell_contents(
            project_with_work_and_overtime_work['name'],
            today[3] + 1
        )
        assert zero_work == '0+3', "Переработка не перенеслась на день без трудозатрат или не корректно отображается"
        # Перенос переработки с дня без трудозатрат
        labor_cost_page.change_overtime_work_date(project_with_work_and_overtime_work['name'],
                                                  labor_cost_page.get_day_before(-4))
        time.sleep(1)
        empty_work = labor_cost_page.get_project_day_cell_contents(
            project_with_work_and_overtime_work['name'],
            today[3] + 1
        )
        assert empty_work == '', "Трудозатраты отображаются не корректно после переноса переработки"
        # Перенос переработки на изначальный день
        labor_cost_page.change_overtime_work_date(project_with_work_and_overtime_work['name'],
                                                  labor_cost_page.get_day_before(-2))
        time.sleep(1)
        work_and_overtime = labor_cost_page.get_project_day_cell_contents(
            project_with_work_and_overtime_work['name'],
            today[2] + 1
        )
        assert work_and_overtime == '8+3', "Переработка отображается не корректно после переноса"

    @testit.workItemIds(11918)
    @testit.displayName("3.1.3.3 Редактирование переработки с обязательным приложением файлов")
    @pytest.mark.regress
    @allure.title("id-11918 3.1.3.3 Редактирование переработки с обязательным приложением файлов")
    def test_editing_processing_with_mandatory_file_attachment(self, project_with_attach_files, login, driver):
        labor_cost_page = LaborCostPage(driver)
        time.sleep(1)
        zero_reason_day = labor_cost_page.get_numbers_days_reason("zero")
        labor_cost_page.add_overtime_work_with_file(
            zero_reason_day[-2],
            2,
            project_with_attach_files['name']
        )
        labor_cost_page.redact_overtime_on_reason_tab(project_with_attach_files['name'])
        value_before = labor_cost_page.get_overtime_value_on_drawer()
        labor_cost_page.editing_overwork_with_file_from_tab(4)
        labor_cost_page.redact_overtime_on_reason_tab(project_with_attach_files['name'])
        time.sleep(1)
        value_after = labor_cost_page.get_overtime_value_on_drawer()
        assert value_before != value_after, "Значения в полях не изменились"
        assert '4' in value_after, "Не корректные значения в полях после редактирования переработки"

    @testit.workItemIds(11919)
    @testit.displayName("3.1.3.3. Н. Изменение данных на не валидные при редактировании переработок на проект из раздела Заявления")
    @pytest.mark.regress
    @allure.title("id-11919 3.1.3.3. Н. Изменение данных на не валидные при редактировании переработок на проект из раздела Заявления")
    def test_changing_data_to_invalid_when_editing_overtime_work(self, project_with_attach_files, login, driver):
        labor_cost_page = LaborCostPage(driver)
        time.sleep(1)
        zero_reason_day = labor_cost_page.get_numbers_days_reason("zero")
        labor_cost_page.add_overtime_work_with_file(
            zero_reason_day[-2],
            2,
            project_with_attach_files['name']
        )
        time.sleep(1)
        labor_cost_page.input_labor_reason_by_project(project_with_attach_files['name'], zero_reason_day[-2] + 2, 8)
        labor_cost_page.add_overtime_work_with_file(
            zero_reason_day[-3],
            4,
            project_with_attach_files['name']
        )
        time.sleep(5)
        labor_cost_page.redact_overtime_on_reason_tab(project_with_attach_files['name'])
        labor_cost_page.check_clear_required_field()
        labor_cost_page.redact_overtime_on_reason_tab(project_with_attach_files['name'])
        time.sleep(1)
        labor_cost_page.change_date_in_date_piker(zero_reason_day[-3])
        assert labor_cost_page.get_mui_error_text() == 'На выбранную дату и проект уже есть переработка', \
            "Не появилось сообщение о наложении переработок"
        labor_cost_page.redact_overtime_on_reason_tab(project_with_attach_files['name'])
        labor_cost_page.check_change_file_to_not_valid()
        labor_cost_page.redact_overtime_on_reason_tab(project_with_attach_files['name'])
        labor_cost_page.change_time_in_overtime_drawer(18)
        assert labor_cost_page.get_mui_error_text() == 'Сумма трудозатрат за день не может превышать 24 часа', \
            "Не появилось сообщение о превышении допустимого времени работы"

    @testit.workItemIds(11920)
    @testit.displayName("3.1.3.4. Удаление/отмена удаления переработок в блоке Причины")
    @pytest.mark.regress
    @allure.title("id-11920 3.1.3.4. Удаление/отмена удаления переработок в блоке Причины")
    def test_deleting_cancelling_deletion_in_the_reasons_block(self, project_with_overtime_work, login, driver):
        labor_cost_page = LaborCostPage(driver)
        time.sleep(1)
        labor_cost_page.check_break_delete_overtime_on_reason_tab(project_with_overtime_work['name'])
        time.sleep(1)
        labor_cost_page.delete_overtime_on_reason_tab(project_with_overtime_work['name'])
        assert labor_cost_page.get_alert_message() == ['Переработка удалена'], \
            "Не появилось сообщение об удалении системы"
        labor_cost_page.not_have_overtime_on_reason_tab_by_project(project_with_overtime_work['name'])

    @testit.workItemIds(3700)
    @testit.displayName("3.1.1.7 Реакция системы на выбор чекбокса 'Отображать причины отклонения'")
    @pytest.mark.regress
    @allure.title("id-3700 3.1.1.7 Реакция системы на выбор чекбокса 'Отображать причины отклонения'")
    def test_rejection_reasons_shown_on_checkbox_selection(self, project_with_rejected_labor_report, login, driver):
        project_name = project_with_rejected_labor_report[0]['name']
        number_day = project_with_rejected_labor_report[1]
        rejection_reason = project_with_rejected_labor_report[2]
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.click_rejection_reasons_checkbox()
        assert labor_cost_page.get_day_tooltip_text_in_project(project_name, number_day) == f'Причина отклонения: {rejection_reason}', 'Неверный текст тултипа с причиной отклонения'

    @testit.workItemIds(3723)
    @testit.displayName("3.1.1.7 Просмотр причины отклонения списаний трудозатрат через уведомления системы")
    @pytest.mark.regress
    @allure.title("id-3723 3.1.1.7 Просмотр причины отклонения списаний трудозатрат через уведомления системы")
    def test_labor_cost_rejection_notification(self, project_with_rejected_labor_report, login, driver):
        project_name = project_with_rejected_labor_report[0]['name']
        rejection_reason = project_with_rejected_labor_report[2]
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        start, end = [day.strftime('%d.%m') for day in labor_cost_page.get_current_week_start_end()]
        assert labor_cost_page.get_notification_text() == (f'Трудозатраты по {project_name} на {start}-{end} '
                                                           f'были отклонены. Причина: {rejection_reason}'), \
            'Неверный текст уведомления с причиной отклонения'

    @testit.workItemIds(3138)
    @testit.displayName("3.1.1.2 Заполнение трудозатрат по задаче со статусом Остановлено.")
    @pytest.mark.regress
    @allure.title("id-3138 3.1.1.2 Заполнение трудозатрат по задаче со статусом Остановлено.")
    def test_fill_labor_costs_for_stopped_task(self, project_with_stopped_task, login, driver):
        task_name = project_with_stopped_task[2]
        number_day = project_with_stopped_task[1]
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_tasks_list(project_with_stopped_task[0]['name'])
        assert labor_cost_page.get_status_of_field_task(task_name, number_day), 'Ячейка активна для ввода'

    @testit.workItemIds(3139)
    @testit.displayName("3.1.1.2 Заполнение трудозатрат по задаче со статусом Завершено.")
    @pytest.mark.regress
    @allure.title("id-3139 3.1.1.2 Заполнение трудозатрат по задаче со статусом Завершено.")
    def test_fill_labor_costs_for_completed_task(self, project_with_completed_task, login, driver):
        task_name = project_with_completed_task[2]
        number_day = project_with_completed_task[1]
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_tasks_list(project_with_completed_task[0]['name'])
        assert labor_cost_page.get_status_of_field_task(task_name, number_day), 'Ячейка активна для ввода'

    @testit.workItemIds(3724)
    @testit.displayName("3.1.1.7 Проверка отсутствия тултипа если чекбокс 'Отображать причины отклонения' не выбран.")
    @pytest.mark.regress
    @allure.title("id-3724 3.1.1.7 Проверка отсутствия тултипа если чекбокс 'Отображать причины отклонения' не выбран.")
    def test_no_tooltip_if_reason_checkbox_disabled(self, project_with_rejected_labor_report, login, driver):
        project_name = project_with_rejected_labor_report[0]['name']
        number_day = project_with_rejected_labor_report[1]
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        assert labor_cost_page.field_is_rejected(project_name, number_day), 'Трудозатраты не отклонены'
        assert not labor_cost_page.get_status_of_field_project(project_name,number_day), 'Ячейка неактивна для ввода'
        assert not labor_cost_page.tooltip_is_displayed(project_name, number_day), 'Тултип отображается'

    @testit.workItemIds(3160)
    @testit.displayName("3.1.1.3. Отображение неактивных проектов в таблице трудозатрат")
    @pytest.mark.regress
    @allure.title("id-3160 3.1.1.3. Отображение неактивных проектов в таблице трудозатрат")
    def test_show_inactive_projects_in_labor_cost_table(self, archive_project_with_assignment, second_project,  login, driver):
        project_name = archive_project_with_assignment['name']
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.check_filter()
        before_check = project_name not in labor_cost_page.get_all_project_name_on_tab()
        labor_cost_page.check_archive_project(project_name)
        time.sleep(0.5)
        after_check = project_name in labor_cost_page.get_all_project_name_on_tab()
        assert before_check and after_check, "Неактивный проект не отображается"

    @testit.workItemIds(3458)
    @testit.displayName("3.1.1.1 Отображение тултипа причины списания трудозатрат и переработки.")
    @pytest.mark.regress
    @allure.title("id-3458 3.1.1.1 Отображение тултипа причины списания трудозатрат и переработки.")
    def test_display_labor_cost_and_overtime_write_off_tooltip(self, f_overtime_reason_requirement, project_with_required_reasons_with_work_and_overtime_work, login, driver):
        project_name = project_with_required_reasons_with_work_and_overtime_work[0]['name']
        number_day = project_with_required_reasons_with_work_and_overtime_work[1]
        reason = project_with_required_reasons_with_work_and_overtime_work[2]
        hours = project_with_required_reasons_with_work_and_overtime_work[3]
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        assert labor_cost_page.get_day_tooltip_text_in_project(project_name, number_day) == f"{hours} + {hours}\nРабота на проекте: {reason}\nПричина переработки: {reason}", 'Неверный текст тултипа с причинами списаний'

    @testit.workItemIds(274)
    @testit.displayName('3.1.1.2 Отмена заполнение таблицы "Отчет трудозатрат".')
    @pytest.mark.regress
    @allure.title('id-274 3.1.1.2 Отмена заполнение таблицы "Отчет трудозатрат".')
    def test_cancel_labor_cost_fill(self, project_with_assignment, login, driver):
        project_name = project_with_assignment[0]['name']
        number_day = project_with_assignment[1]
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.input_labor_reason_by_project(project_name, number_day, 1)
        value_before_canceling = labor_cost_page.get_project_day_cell_contents(project_name, number_day)
        first_color = labor_cost_page.get_cell_color(project_name,number_day)
        labor_cost_page.cancel_editing_labor_cost()
        value_after_canceling = labor_cost_page.get_project_day_cell_contents(project_name, number_day)
        second_color = labor_cost_page.get_cell_color(project_name,number_day)
        assert first_color  == 'rgba(255, 251, 233, 1)', 'Цвет ячейки не желтый'
        assert second_color == 'rgba(0, 0, 0, 0)', 'Цвет ячейки не белый'
        assert value_before_canceling == '1', "Введенное значение не отображается в ячейке"
        assert value_after_canceling == '', "В ячейке сохранены изменения"

    @testit.workItemIds(3719)
    @testit.displayName('3.1.1.2 Заполнение таблицы "Трудозатраты" с переключением отображения Неделя/месяц.')
    @pytest.mark.regress
    @allure.title('id-3719 3.1.1.2 Заполнение таблицы "Трудозатраты" с переключением отображения Неделя/месяц.')
    def test_labor_cost_fill(self, project_with_assignment, second_project_with_assignment, login, driver):
        first_project_name = project_with_assignment[0]['name']
        second_project_name = second_project_with_assignment[0]['name']
        labor_cost_page = LaborCostPage(driver)
        try:
            number_day = int(labor_cost_page.get_day_before_ymd(1).split('-')[2]) + 1
            labor_cost_page.input_labor_reason_by_project(first_project_name, number_day, 12)
            time.sleep(2)
            assert labor_cost_page.get_cell_color(first_project_name,
                                                  number_day) == 'rgba(255, 251, 233, 1)', 'Цвет ячейки не желтый'
        except AssertionError as e:
            number_day = int(labor_cost_page.get_day_after_ymd(1).split('-')[2]) + 1
            labor_cost_page.input_labor_reason_by_project(first_project_name, number_day, 12)
            time.sleep(2)
            assert labor_cost_page.get_cell_color(first_project_name,
                                                  number_day) == 'rgba(255, 251, 233, 1)', 'Цвет ячейки не желтый'
        labor_cost_page.choose_period('week')
        try:
            number_day = labor_cost_page.get_number_day_week()
            labor_cost_page.input_labor_reason_by_project(second_project_name, number_day, 13)
            time.sleep(2)
            assert labor_cost_page.get_cell_color(second_project_name,
                                                  number_day) == 'rgba(255, 251, 233, 1)', 'Цвет ячейки не желтый'
        except AssertionError as e:
            number_day = labor_cost_page.get_number_day_week() + 2
            labor_cost_page.input_labor_reason_by_project(second_project_name, number_day, 13)
            time.sleep(2)
            assert labor_cost_page.get_cell_color(second_project_name,
                                                  number_day) == 'rgba(255, 251, 233, 1)', 'Цвет ячейки не желтый'
        time.sleep(2)
        assert (labor_cost_page.get_color_day_total_raw(number_day-1)
                == 'rgba(211, 47, 47, 1)'), 'Цвет текста не красный'
        labor_cost_page.save_labor_reason()
        assert not labor_cost_page.get_status_of_saving(), "Данные сохранены"
        assert ("Сумма часов не может превышать 24 за текущий день" in
                labor_cost_page.get_alert_message()), 'Нет сообщения об ошибке'
        assert int(labor_cost_page.get_day_total_raw(number_day-1)) == labor_cost_page.get_all_values_by_day(number_day), 'Неправильная сумма часов'

    @testit.workItemIds(11935)
    @testit.displayName('3.1.1.9. Редактирование/отмена редактирования списаний трудозатрат с причиной из раздела "Заявления"')
    @pytest.mark.regress
    @allure.title('id-11935 3.1.1.9. Редактирование/отмена редактирования списаний трудозатрат с причиной из раздела "Заявления"')
    def test_edit_cancel_reason_for_labor_cost_in_statements(self, project_with_added_labor_reason, login, driver):
        labor_cost_page = LaborCostPage(driver)
        time.sleep(2)
        labor_cost_page.redact_overtime_on_reason_tab(project_with_added_labor_reason['name'])
        source_data = labor_cost_page.get_labor_cost_value_on_drawer()
        labor_cost_page.redact_labor_cost(8, 'Первая причина это ты, а вторая все твои мечты')
        labor_cost_page.cancel_changes_labor_cost_drawer()
        labor_cost_page.redact_overtime_on_reason_tab(project_with_added_labor_reason['name'])
        labor_cost_page.check_values_on_reason_tab(project_with_added_labor_reason['name'], source_data[0], source_data[1])
        value_after_canceling = labor_cost_page.get_labor_cost_value_on_drawer()
        labor_cost_page.redact_labor_cost(8,'Третья это все твои слова, Я им не поверил едва. '
                                            'Четвёртая причина это ложь, Кто прав, кто виноват - не разберёшь,')
        labor_cost_page.save_changes_labor_cost_drawer()
        time.sleep(1)
        labor_cost_page.check_values_on_reason_tab(project_with_added_labor_reason['name'], '8',
                                                   'Третья это все твои слова, Я им не поверил едва. '
                                                   'Четвёртая причина это ложь, Кто прав, кто виноват - не разберёшь,')
        labor_cost_page.redact_overtime_on_reason_tab(project_with_added_labor_reason['name'])
        value_after_saving = labor_cost_page.get_labor_cost_value_on_drawer()
        assert value_after_canceling == source_data, 'Данные изменились при отмене'
        assert value_after_saving != source_data, 'Данные не изменились при сохранении'


    @testit.workItemIds(11936)
    @testit.displayName('3.1.1.9. Н. Изменение данных на невалидные при редактировании списаний трудозатрат с причиной из раздела "Заявления"')
    @pytest.mark.regress
    @allure.title('id-11936 3.1.1.9. Н. Изменение данных на невалидные при редактировании списаний трудозатрат с причиной из раздела "Заявления"')
    def test_invalid_data_for_labor_cost_on_editing(self, project_with_added_labor_reason, second_project_with_work, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.redact_overtime_on_reason_tab(project_with_added_labor_reason['name'])
        labor_cost_page.redact_labor_cost(hours='25')
        hours_over_24 = labor_cost_page.get_labor_cost_value_on_drawer()
        labor_cost_page.redact_labor_cost(hours='-5')
        hours_less_0 = labor_cost_page.get_labor_cost_value_on_drawer()
        labor_cost_page.redact_labor_cost(hours='24')
        labor_cost_page.save_changes_labor_cost_drawer()
        errors = labor_cost_page.get_alert_message()
        labor_cost_page.redact_overtime_on_reason_tab(project_with_added_labor_reason['name'])
        labor_cost_page.redact_labor_cost(hours=' ', reason=' ')
        assert not labor_cost_page.save_changes_labor_cost_drawer(), "Кнопка сохранения активна"
        assert 'Сумма часов не может превышать 24 за текущий день' in errors, "Нет сообщения об ошибке"
        assert hours_over_24 != '25', "Значение больше 24 отображается в поле"
        assert hours_less_0 != '-5', "Значение меньше 0 отображается в поле"

    @testit.workItemIds(3725)
    @testit.displayName('3.1.1.8 Внесение изменений в отклонённые списания трудозатрат по задачам на проекте с обязательным указанием причин списания.')
    @pytest.mark.regress
    @allure.title('id-3725 3.1.1.8 Внесение изменений в отклонённые списания трудозатрат по задачам на проекте с обязательным указанием причин списания.')
    def test_edit_task_rejected_labor_cost_with_required_reasons(self, project_with_rejected_task_labor_cost, login, driver):
        labor_cost_page = LaborCostPage(driver)
        project_card_page = ProjectCardPage(driver)
        first, last = project_card_page.get_current_week_start_end()
        project_name = project_with_rejected_task_labor_cost[0]['name']
        number_day = project_with_rejected_task_labor_cost[1]
        task_name = project_with_rejected_task_labor_cost[2]
        user_name = project_with_rejected_task_labor_cost[3]
        labor_cost_page.open_tasks_list(project_name)
        labor_cost_page.click_cell_in_labor_cost_table_by_task(task_name, number_day)
        labor_cost_page.check_labor_cost_drawer_view(labor_cost_page.get_day_after(0))
        assert ('3', 'Причина') == labor_cost_page.get_labor_cost_value_on_drawer(), 'В поле не отображаются ранее сохраненные значения'
        labor_cost_page.redact_labor_cost(hours=7, reason='Другая причина совсем непохожая на старую')
        labor_cost_page.save_changes_labor_cost_drawer()
        assert labor_cost_page.get_task_day_cell_contents(task_name, number_day) == '7', 'Значение не изменилось'
        assert not labor_cost_page.field_is_rejected(task_name, number_day), "Поле отображается отклоненным"
        labor_cost_page.save_labor_reason()
        driver.refresh()
        assert f'Пользователь {user_name} внёс изменения в трудозатраты на проекте {project_name} с {first.strftime('%d.%m.%Y')} по {last.strftime('%d.%m.%Y')}' == labor_cost_page.get_notification_text(), "Нет уведомления об изменениях"
        labor_cost_page.action_esc()
        labor_cost_page.go_to_project_card(project_name)
        project_card_page.go_to_progress_tab()
        project_card_page.check_wait_approved_reason_on_tab()

    @testit.workItemIds(3726)
    @testit.displayName('3.1.1.8. Отмена внесений изменений в отклонённые списания трудозатрат по проекту с обязательным указанием причин списания.')
    @pytest.mark.regress
    @allure.title('id-3726 3.1.1.8. Отмена внесений изменений в отклонённые списания трудозатрат по проекту с обязательным указанием причин списания.')
    def test_cancel_edit_task_rejected_labor_cost_with_required_reasons(self, project_with_rejected_task_labor_cost, login, driver):
        labor_cost_page = LaborCostPage(driver)
        project_name = project_with_rejected_task_labor_cost[0]['name']
        number_day = project_with_rejected_task_labor_cost[1]
        task_name = project_with_rejected_task_labor_cost[2]
        labor_cost_page.open_tasks_list(project_name)
        labor_cost_page.click_cell_in_labor_cost_table_by_task(task_name, number_day)
        labor_cost_page.redact_labor_cost(hours=7, reason='Из-за ретроградного Меркурия всё пошло не по плану')
        labor_cost_page.cancel_changes_labor_cost_drawer()
        assert labor_cost_page.get_task_day_cell_contents(task_name, number_day) == '3', "Значение в ячейке изменилось"
        assert labor_cost_page.field_is_rejected(task_name, number_day), "Поле отображается не отклоненным"

    @testit.workItemIds(3727)
    @testit.displayName('3.1.1.8 Внесение изменений в отклонённые списания трудозатрат по проекту.')
    @pytest.mark.regress
    @allure.title('id-3727 3.1.1.8 Внесение изменений в отклонённые списания трудозатрат по проекту.')
    def test_edit_rejected_labor_cost(self, project_with_rejected_labor_cost_without_reason, login, driver):
        labor_cost_page = LaborCostPage(driver)
        project_card_page = ProjectCardPage(driver)
        first, last = labor_cost_page.get_current_week_start_end()
        project_name = project_with_rejected_labor_cost_without_reason[0]['name']
        number_day = project_with_rejected_labor_cost_without_reason[1]
        user_name = project_with_rejected_labor_cost_without_reason[2]
        labor_cost_page.redact_labor_cost_table_by_project(project_name, number_day, 8)
        assert labor_cost_page.get_cell_color(project_name, int(number_day)) in ['rgba(255, 251, 233, 1)', 'rgba(255, 236, 229, 1)'], 'Цвет не желтый/красный(выходной)'
        labor_cost_page.save_labor_reason()
        assert labor_cost_page.get_project_day_cell_contents(project_name, number_day) == '8', 'Значение не изменилось'
        assert not labor_cost_page.field_is_rejected(project_name, number_day), "Поле отображается отклоненным"
        driver.refresh()
        assert f'Пользователь {user_name} внёс изменения в трудозатраты на проекте {project_name} с {first.strftime('%d.%m.%Y')} по {last.strftime('%d.%m.%Y')}' == labor_cost_page.get_notification_text(), "Нет уведомления об изменениях"
        labor_cost_page.action_esc()
        labor_cost_page.go_to_project_card(project_name)
        project_card_page.go_to_progress_tab()
        project_card_page.check_wait_approved_reason_on_tab()

    @testit.workItemIds(3728)
    @testit.displayName('3.1.1.8 Отмена внесений изменений в отклонённые списания трудозатрат по проекту.')
    @pytest.mark.regress
    @allure.title('id-3728 3.1.1.8 Отмена внесений изменений в отклонённые списания трудозатрат по проекту.')
    def test_cancel_edit_rejected_labor_cost(self, project_with_rejected_labor_cost_without_reason, login, driver):
        labor_cost_page = LaborCostPage(driver)
        project_name = project_with_rejected_labor_cost_without_reason[0]['name']
        number_day = project_with_rejected_labor_cost_without_reason[1]
        labor_cost_page.redact_labor_cost_table_by_project(project_name, number_day, 8)
        labor_cost_page.cancel_editing_labor_cost()
        assert labor_cost_page.get_project_day_cell_contents(project_name, number_day) == '3', 'Значение изменилось'
        assert labor_cost_page.field_is_rejected(project_name, number_day), "Поле отображается не отклоненным"

    @testit.workItemIds(3737)
    @testit.displayName('3.1.1.8 Внесение изменений в отклонённые списания трудозатрат по проекту с обязательным указанием причин списания.')
    @pytest.mark.regress
    @allure.title('id-3737 3.1.1.8 Внесение изменений в отклонённые списания трудозатрат по проекту с обязательным указанием причин списания.')
    def test_edit_rejected_labor_cost_with_required_reasons(self, project_with_rejected_labor_cost, login, driver):
        labor_cost_page = LaborCostPage(driver)
        project_card_page = ProjectCardPage(driver)
        first, last = labor_cost_page.get_current_week_start_end()
        project_name = project_with_rejected_labor_cost[0]['name']
        number_day = project_with_rejected_labor_cost[1]
        user_name = project_with_rejected_labor_cost[2]
        labor_cost_page.click_cell_in_labor_cost_table_by_project(project_name, number_day)
        labor_cost_page.check_labor_cost_drawer_view(labor_cost_page.get_day_after(1))
        assert ('3', 'Причина') == labor_cost_page.get_labor_cost_value_on_drawer(), 'В поле не отображаются ранее сохраненные значения'
        labor_cost_page.redact_labor_cost(hours=7, reason='Другая причина совсем непохожая на старую')
        labor_cost_page.save_changes_labor_cost_drawer()
        assert labor_cost_page.get_project_day_cell_contents(project_name, number_day) == '7', 'Значение не изменилось'
        assert not labor_cost_page.field_is_rejected(project_name, number_day), "Поле отображается отклоненным"
        labor_cost_page.save_labor_reason()
        driver.refresh()
        assert f'Пользователь {user_name} внёс изменения в трудозатраты на проекте {project_name} с {first.strftime('%d.%m.%Y')} по {last.strftime('%d.%m.%Y')}' == labor_cost_page.get_notification_text(), "Нет уведомления об изменениях"
        labor_cost_page.action_esc()
        labor_cost_page.go_to_project_card(project_name)
        project_card_page.go_to_progress_tab()
        project_card_page.check_wait_approved_reason_on_tab()
