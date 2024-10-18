import time

import allure
import pytest
import testit

from pages.production_calendar_page import ProductionCalendarPage


@allure.suite("Производственный календарь")
class TestProductionCalendarPage:

    @testit.workItemIds(3902)
    @testit.displayName("5.1. Просмотр производственного календаря")
    @pytest.mark.regress
    @allure.title("id-3902 5.1. Просмотр производственного календаря")
    def test_view_your_production_calendar(self, login, driver):
        production_calendar_page = ProductionCalendarPage(driver)
        production_calendar_page.go_to_production_calendar_page()
        time.sleep(2)
        production_calendar_page.check_title()
        production_calendar_page.check_next_previous_buttons()
        production_calendar_page.check_week_title()
        production_calendar_page.check_work_hours_title()
        production_calendar_page.check_legend_colors()
        production_calendar_page.check_calendar_colors()
        production_calendar_page.check_quarter_info()
