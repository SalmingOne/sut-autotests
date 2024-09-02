import time

import allure
import pytest
import testit

from pages.schedule_page import SchedulePage


@allure.suite("Режим работы")
class TestSchedulePage:

    @testit.workItemIds(11603)
    @testit.displayName("10.2.1.3 Отображение дровера Редактирование графика конкретного дня")
    @pytest.mark.smoke
    @allure.title("id-11603 10.2.1.3 Отображение дровера Редактирование графика конкретного дня")
    def test_displaying_schedule_for_a_specific_day(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        schedule_page.open_editing_schedule_for_a_specific_day_drawer()
        title = schedule_page.get_drawer_title()
        fields = schedule_page.get_drawer_fields_title()
        schedule_page.check_break_time()
        schedule_page.check_add_break_button()
        schedule_page.check_break_delete_icon()
        schedule_page.check_submit_and_break_button()

        assert 'Редактирование графика' in title, 'В заголовке нет слов Редактирование графика'
        assert fields == ['Начало рабочего дня', 'Длительность', 'Окончание рабочего дня', 'Начало перерыва',
                          'Длительность', 'Окончание перерыва'], 'В дровере есть не все поля'

    @testit.workItemIds(11653)
    @testit.displayName("10.2.1.2. Отображение дровера Редактирование стандартного графика")
    @pytest.mark.smoke
    @allure.title("id-11653 10.2.1.2. Отображение дровера Редактирование стандартного графика")
    def test_displaying_schedule_for_a_standard_chart(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        schedule_page.open_editing_schedule_for_a_standard_chart_drawer()
        schedule_page.check_x_button()
        schedule_page.check_week_days_checkboxes_and_switch()
        title = schedule_page.get_drawer_title()
        fields = schedule_page.get_drawer_fields_title()
        schedule_page.check_break_time()
        schedule_page.check_add_break_button()
        schedule_page.check_break_delete_icon()
        schedule_page.check_submit_and_break_button()

        assert title == 'Редактирование стандартного графика', 'Отсутствует или не корректный заголовок дровера'
        assert fields == ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС', "Индивидуальный график для каждого дня",
                          'Начало рабочего дня', 'Длительность', 'Окончание рабочего дня', 'Начало перерыва',
                          'Длительность', 'Окончание перерыва'], 'В дровере есть не все поля'

    @testit.workItemIds(11629)
    @testit.displayName("10.2.1.7 Отображение дровера Взятие отгула")
    @pytest.mark.smoke
    @allure.title("id-11629 10.2.1.7 Отображение дровера Взятие отгула")
    def test_displaying_the_taking_time_off_driver(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        schedule_page.open_take_off_drawer()
        schedule_page.check_taking_time_off_fields()
        schedule_page.check_disable_previous_date_on_date_picker()
        schedule_page.check_switch_by_day()
        schedule_page.check_add_and_delete_taking_time_off_buttons()
        schedule_page.check_submit_and_break_button()

    @testit.workItemIds(2262)
    @testit.displayName("10.2.1.1. Отображение страницы Режим работы")
    @pytest.mark.smoke
    @allure.title("id-2262 10.2.1.1. Отображение страницы Режим работы")
    def test_displaying_the_schedule_page(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        schedule_page.check_number_week_displayed()
        schedule_page.check_switch_periods_and_this_day_button()
        schedule_page.check_redact_button()
        schedule_page.check_add_take_off_button()
        schedule_page.check_hours_in_day_fields()

    @testit.workItemIds(11592)
    @testit.displayName("10.2.1.3 Редактирование конкретного дня")
    @pytest.mark.smoke
    @allure.title("id-11592 10.2.1.3 Редактирование конкретного дня")
    def test_editing_a_specific_day(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        time.sleep(1)  # Без ожидания начинает выполнять тест на странице трудозатрат
        schedule_page.go_to_next_period()
        before_edit = schedule_page.get_text_on_chips(0)
        schedule_page.press_redact_button()
        schedule_page.open_chips_to_edit(0)
        schedule_page.editing_a_specific_day('07:00', '12:00')
        after_edit = schedule_page.get_text_on_chips(0)
        assert after_edit != before_edit, 'Изменения не сохранились'
        assert after_edit == '07:00 - 12:00', 'Не корректно сохранились изменения'

    @testit.workItemIds(11661)
    @testit.displayName("10.2.1.2. Снятие выбора со всех чекбоксов дней недели")
    @pytest.mark.smoke
    @allure.title("id-11661 10.2.1.2. Снятие выбора со всех чекбоксов дней недели")
    def test_unselecting_all_weekday_checkboxes(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        schedule_page.open_editing_schedule_for_a_standard_chart_drawer()
        schedule_page.unselecting_all_weekday_checkboxes()
        schedule_page.press_submit_button_in_drawer()
        errors = schedule_page.get_all_errors_in_checkboxes()
        assert errors == ['Хотя бы один день недели должен быть выбран'], \
            "Не появилось сообщение о необходимости выбрать чекбокс"

    @testit.workItemIds(11600)
    @testit.displayName("10.2.1.2. Добавление дополнительного перерыва")
    @pytest.mark.regress
    @allure.title("id-11600 10.2.1.2. Добавление дополнительного перерыва")
    def test_adding_second_break(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        first_day_chips = schedule_page.get_first_day_chips_text()
        schedule_page.open_editing_schedule_for_a_standard_chart_drawer()
        schedule_page.check_add_one_break()
        schedule_page.change_second_break()
        schedule_page.press_submit_button_in_drawer()
        first_day_chips_redacted = schedule_page.get_first_day_chips_text()
        schedule_page.press_save_button_in_page()
        first_day_chips_saved = schedule_page.get_first_day_chips_text()
        # Возвращаем первоначальные значения
        schedule_page.return_before_values()
        assert first_day_chips_redacted == ('09:00 - 13:00', '15:00 - 19:00'), "Значения в графике не изменились на заданные"
        assert first_day_chips_redacted != first_day_chips, "График не изменился"
        assert first_day_chips_redacted == first_day_chips_saved, "График не сохранился"

    @testit.workItemIds(11664)
    @testit.displayName("10.2.1.2. Редактирование стандартного рабочего графика")
    @pytest.mark.regress
    @allure.title("id-11664 10.2.1.2. Редактирование стандартного рабочего графика")
    def test_editing_a_standard_work_schedule(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        first_day_chips = schedule_page.get_first_day_chips_text()
        schedule_page.open_editing_schedule_for_a_standard_chart_drawer()
        schedule_page.change_end_work_time()
        schedule_page.press_submit_button_in_drawer()
        first_day_chips_redacted = schedule_page.get_first_day_chips_text()
        schedule_page.press_save_button_in_page()
        first_day_chips_saved = schedule_page.get_first_day_chips_text()
        # Возвращаем первоначальные значения
        schedule_page.return_end_work_time()
        schedule_page.check_change_all_days()
        assert first_day_chips_redacted == ('09:00 - 13:00', '14:00 - 18:30'), "Значения в графике не изменились на заданные"
        assert first_day_chips_redacted != first_day_chips, "График не изменился"
        assert first_day_chips_redacted == first_day_chips_saved, "График не сохранился"

    @testit.workItemIds(2265)
    @testit.displayName("10.2.1.2. Отмена редактирования стандартного рабочего графика")
    @pytest.mark.regress
    @allure.title("id-2265 10.2.1.2. Отмена редактирования стандартного рабочего графика")
    def test_cancel_editing_of_a_standard_work_schedule(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        before_chips_text = schedule_page.get_all_chips_text()
        schedule_page.open_editing_schedule_for_a_standard_chart_drawer()
        schedule_page.change_end_work_time()
        schedule_page.press_cancel_button()
        after_chips_text = schedule_page.get_all_chips_text()
        assert before_chips_text == after_chips_text, "Стандартный график изменился"

    @testit.workItemIds(2264)
    @testit.displayName("10.2.1.2. Редактирование стандартного рабочего графика индивидуально для каждого дня")
    @pytest.mark.regress
    @allure.title("id-2264 10.2.1.2. Редактирование стандартного рабочего графика индивидуально для каждого дня")
    def test_editing_the_standard_work_schedule_individually_for_each_day(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        schedule_page.open_editing_schedule_for_a_standard_chart_drawer()
        schedule_page.check_no_individual_tabs()
        schedule_page.press_individual_switch()
        schedule_page.match_checked_checkboxes_and_individual_tabs_text()
        schedule_page.change_end_work_time()
        schedule_page.press_submit_button_in_drawer()
        schedule_page.press_save_button_in_page()
        first_day_chips = schedule_page.get_first_day_chips_text()
        second_day_chips = schedule_page.get_second_day_chips_text()
        # Возвращаем первоначальные значения
        schedule_page.return_end_work_time()
        assert first_day_chips == ('09:00 - 13:00', '14:00 - 18:30'), "Значения в графике не изменились на заданные"
        assert first_day_chips != second_day_chips, "День не отредактировался индивидуально"

    @testit.workItemIds(11607)
    @testit.displayName("10.2.1.3 Отмена редактирования конкретного дня")
    @pytest.mark.regress
    @allure.title("id-11607 10.2.1.3 Отмена редактирования конкретного дня")
    def test_cancel_editing_of_a_specific_day(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        first_day_chips_before = schedule_page.get_first_day_chips_text()
        schedule_page.press_redact_button()
        schedule_page.redact_next_week_day()
        schedule_page.change_end_work_time()
        schedule_page.press_cancel_button()
        first_day_chips_after = schedule_page.get_first_day_chips_text()
        assert first_day_chips_after == first_day_chips_before, "В календаре произошли изменения"

    @testit.workItemIds(11602)
    @testit.displayName("10.2.1.2. Указание перерыва раньше начала/позже конца рабочего дня")
    @pytest.mark.regress
    @allure.title("id-11602 10.2.1.2. Указание перерыва раньше начала/позже конца рабочего дня")
    def test_add_break_before_or_after_working_day(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        schedule_page.open_editing_schedule_for_a_standard_chart_drawer()
        schedule_page.add_break_before_working_day()
        schedule_page.press_cancel_button()
        schedule_page.reopen_editing_schedule_for_a_standard_chart_drawer()
        schedule_page.add_break_after_working_day()

    @testit.workItemIds(11658)
    @testit.displayName("10.2.1.3. Перенос перерыва за час до окончания РД/до начала РД")
    @pytest.mark.regress
    @allure.title("id-11658 10.2.1.3. Перенос перерыва за час до окончания РД/до начала РД")
    def test_add_break_for_hour_before_end_or_after_start_working_day(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        schedule_page.open_editing_schedule_for_a_standard_chart_drawer()
        schedule_page.check_add_break_in_start_work_time()
        schedule_page.press_cancel_button()
        schedule_page.reopen_editing_schedule_for_a_standard_chart_drawer()
        schedule_page.check_add_break_for_hour_before_end_work_time()

    @testit.workItemIds(11591)
    @testit.displayName("10.2.1.3 Выбор менее 8 часов в день (фултайм)")
    @pytest.mark.regress
    @allure.title("id-11591 10.2.1.3 Выбор менее 8 часов в день (фултайм)")
    def test_choice_of_less_than_eight_hours_a_day_full_time(self, login, driver):
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        schedule_page.press_redact_button()
        schedule_page.redact_next_week_day()
        schedule_page.editing_a_specific_day('11:00', '12:00')
        assert schedule_page.get_massage() == 'Ваш рабочий день должен составлять не менее 8 часов', \
            "Не появилось сообщения о недостаточном количестве часов"
