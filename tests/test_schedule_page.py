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
        schedule_page.check_drawer_title()
        schedule_page.check_drawer_fields_title()
        schedule_page.check_break_time()
        schedule_page.check_add_break_button()
        schedule_page.check_break_delete_icon()
        schedule_page.check_submit_and_break_button()



