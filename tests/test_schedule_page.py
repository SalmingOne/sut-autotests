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
        time.sleep(1)  # Без ожидания начинает выполнять тест на странице трудозатрат
        schedule_page.go_to_next_period()
        before_edit = schedule_page.get_text_on_chips(0)
        schedule_page.press_redact_button()
        schedule_page.open_chips_to_edit(0)
        schedule_page.editing_a_specific_day('07:00', '12:00')
        after_edit = schedule_page.get_text_on_chips(0)
        assert after_edit != before_edit, 'Изменения не сохранились'
        assert after_edit == '07:00 - 12:00', 'Не корректно сохранились изменения'
