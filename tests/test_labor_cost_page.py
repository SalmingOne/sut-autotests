import time

import allure
import pytest
import testit

from pages.all_project_page import AllProjectPage
from pages.labor_cost_page import LaborCostPage
from locators.labor_cost_page_locators import LaborCostPageLocators



@allure.suite("Таблица трудозатрат")
class TestLaborCostPage:

    @testit.workItemIds(270)
    @testit.displayName("3.1.1.2 Заполнение таблицы Отчет трудозатрат")
    @allure.title("id-270 3.1.1.2 Заполнение таблицы Отчет трудозатрат")
    def test_filing_labor_cost_report_table(self, f_create_temp_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.choose_period("week")
        labor_cost_page.check_change_color_on_labor_cost_field()

    @testit.workItemIds(267)
    @testit.displayName("3.1.1.1 Просмотр таблицы трудозатрат.")
    @allure.title("id-267 3.1.1.1 Просмотр таблицы трудозатрат.")
    def test_mapping_labor_cost_page(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.check_title()
        labor_cost_page.check_add_to_project_button()
        labor_cost_page.check_period_select()
        labor_cost_page.check_add_overtime_work_button()
        labor_cost_page.check_add_absense_button()
        #labor_cost_page.check_filter()
        labor_cost_page.check_open_widget_button()
        labor_cost_page.check_month_picker()
        #labor_cost_page.check_next_previous_buttons()
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
        assert tooltip_on_code in tooltip_on_project, "Тултип отображается без имени проекта"
        assert 'Проект' in all_head_list, "Нет столбца Проект"
        assert 'Итого' in all_head_list, "Нет столбца Итого"

    @testit.workItemIds(1461)
    @testit.displayName("3.1.1.2 Содержание модального окна указания причин списания.")
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

    @testit.workItemIds(277)
    @testit.displayName("3.1.1.2 Удаление значений в таблице Отчет трудозатрат")
    @allure.title("id-277 3.1.1.2 Удаление значений в таблице Отчет трудозатрат")
    def test_delete_values_on_labor_cost_report_table(self, f_create_temp_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.choose_period("week")
        labor_cost_page.check_delete_values_on_labor_cost_field()

    @testit.workItemIds(1464)
    @testit.displayName("Пустой ввод в поле Причина")
    @pytest.mark.labor_reason("True")
    @allure.title('id-1464 Пустой ввод в поле "Причина"')
    def test_empty_entry_in_the_reason_field(self, f_create_temp_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        locators = LaborCostPageLocators()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_reason_window(f_create_temp_project["name"])
        labor_cost_page.input_hours_into_form(6)

        assert labor_cost_page.element_is_clickable(locators.SAVE_WINDOW_BUTTON) == False, 'Кнопка "Сохранить" активна'

    @testit.workItemIds(1476)
    @testit.displayName("Ввод пробела в поле Причина")
    @pytest.mark.labor_reason("True")
    @allure.title('id-1476 Ввод пробела в поле Причина')
    def test_enter_whitespace_in_the_reason_field(self, f_create_temp_project, login, driver):
        labor_cost_page = LaborCostPage(driver)
        locators = LaborCostPageLocators()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.open_reason_window(f_create_temp_project["name"])
        labor_cost_page.input_hours_into_form(6)
        labor_cost_page.input_reason_into_form(" ")
        labor_cost_page.save_hours_and_reason()

        assert labor_cost_page.element_is_visible(
            locators.GOAL_REASON_FIELD_IS_REQUIRED), 'Отсутствует сообщение "Поле обязательно"'

    @testit.workItemIds(1477)
    @testit.displayName("Превышение допустимого количества символов в поле Причина (255 максимальное количество)")
    @pytest.mark.labor_reason("True")
    @allure.title('id-1477 Превышение допустимого количества символов в поле "Причина" (255 максимальное количество)')
    def test_enter_over_max_characters_in_the_reason_field(self, f_create_temp_project, login, driver):
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

    @testit.workItemIds(3165)
    @testit.displayName("3.1.1.5. Уведомление пользователей о несохраненных данных в разделе трудозатрат.")
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

    @testit.workItemIds(535)
    @testit.displayName("3.1.2.1. Добавление больничного/отпуска.")
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
    @allure.title("id-539 Добавление отсутствия на период, в котором есть списанные трудозатраты")
    def test_add_absence_to_labor_reason(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.add_absence_to_reason_day()

    @testit.workItemIds(2759)
    @testit.displayName("3.1.3.1. Добавление переработки на проект на дату, в которую добавлено отсутствие.")
    @allure.title("id-2759 3.1.3.1. Добавление переработки на проект на дату, в которую добавлено отсутствие.")
    def test_add_overwork_to_absence(self, login, driver):
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
    @allure.title("id-3634 Ввод пробела в поле Причина на проект с обязательным указанием причины списания")
    def test_add_space_in_reason_field(self, f_overtime_reason_requirement, login, driver):
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

    # Женя заведет баг, нужно ждать как баг решится
    @testit.workItemIds(2737)
    @testit.displayName("Пустой ввод в обязательные поля при добавлении переработки")
    @allure.title("id-2737 Пустой ввод в обязательные поля при добавлении переработки")
    def test_empty_enter(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(1)  # Без ожидания скрипт срабатывает до загрузки страницы
        tooltip_text = labor_cost_page.check_disable_submit_button_and_tooltip()
        assert tooltip_text == 'Заполните все обязательные поля', "Не появился тултип об обязательности заполнения полей"

    @testit.workItemIds(2725)
    @testit.displayName("Добавление переработки на проект")
    @allure.title("id-2725 Добавление переработки на проект")
    def test_adding_processing_to_a_project(self, f_create_temp_project, login, driver):
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
    @allure.title("id-2710 Содержание дровера Добавление переработки")
    def test_content_drover_adding_overwork(self, f_overtime_reason_requirement, login, driver):
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.open_overtime_drover()
        labor_cost_page.check_fields_on_overtime_drover()

    @testit.workItemIds(1356)
    @testit.displayName("Редактирование отсутствий")
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
    @allure.title("id-547 Фильтр таблицы Отсутствие по времени. Прошедшие отсутствия.")
    def test_filter_past_absences(self, login, driver):
        labor_cost_page = LaborCostPage(driver)
        # Проверяем, что нет заявлений в таблице. И если есть удаляем
        labor_cost_page.go_to_labor_cost_page()
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
