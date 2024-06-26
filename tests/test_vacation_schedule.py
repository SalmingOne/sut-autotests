import time

import allure
import pytest
import testit

from pages.vacation_schedule_page import VacationSchedulePage


@allure.suite("График отпусков")
class TestVacationSchedulePage:

    @testit.workItemIds(505)
    @testit.displayName("Отображение страницы График отпусков")
    @pytest.mark.regress
    @allure.title("id-505 Отображение страницы График отпусков")
    def test_displaying_the_vacation_schedule_page(self, login, driver):
        vacation_schedule_page = VacationSchedulePage(driver)
        vacation_schedule_page.go_to_vacation_schedule_page()
        vacation_schedule_page.check_tooltip()
        vacation_schedule_page.check_color_this_week()
        vacation_schedule_page.check_arrows()
        vacation_schedule_page.check_header_and_week_in_header()
        vacation_schedule_page.check_this_day_button()
        time.sleep(0.5)
        vacation_schedule_page.check_filter_drover()
        vacation_schedule_page.check_user_rows()
        vacation_schedule_page.check_roles_rows()