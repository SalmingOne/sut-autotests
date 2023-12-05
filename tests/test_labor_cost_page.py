import allure
import pytest
from time import sleep

from pages.all_project_page import AllProjectPage
from pages.create_project_drawer_page import CreateProjectDrawerPage
from pages.labor_cost_page import LaborCostPage
from webdriver_manager.chrome import ChromeDriverManager
from locators.labor_cost_page_locators import LaborCostPageLocators


@allure.suite("Поле \"Причина\"")
class TestReasonField:

    @pytest.mark.labor_reason("True")
    @allure.title("id 1464 Пустой ввод в поле \"Причина\"")
    def test_empty_entry_in_the_reson_field(self, driver, login, f_create_temp_project):

        labor_cost_page = LaborCostPage(driver)
        locators = LaborCostPageLocators()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.input_hours_into_form(locators.get_random_day_by_project(f_create_temp_project["name"]), 6)

        if labor_cost_page.element_is_clickable(locators.SAVE_WINDOW_BUTTON):
            assert False, "Кнопка \"Сохранить\" активна"
        else:
            assert True