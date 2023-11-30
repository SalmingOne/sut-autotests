import allure
import pytest
from time import sleep

from pages.all_project_page import AllProjectPage
from pages.create_project_drawer_page import CreateProjectDrawerPage
from pages.labor_cost_page import LaborCostPage
from webdriver_manager.chrome import ChromeDriverManager
from locators.labor_cost_page_locators import LaborCostPageLocators

@pytest.mark.this
@allure.suite("Поле \"Причина\"")
class TestReasonField:

    @allure.title("id 1464 Пустой ввод в поле \"Причина\"")
    def test_empty_entry_in_the_reson_field(self, login, driver: ChromeDriverManager ):
        
        drawer = CreateProjectDrawerPage(driver)
        drawer.go_to_create_project_drawer_from_menu()
        drawer.create_project("reason")

        labor_cost_page = LaborCostPage(driver)
        locators = LaborCostPageLocators()
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.click_onto_cell(locators.RANDOM_DAYS_BY_PROJECT)

        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.delete_project()

        if labor_cost_page.element_is_clickable(locators.SAVE_WINDOW_BUTTON):
            assert False, "Кнопка \"Сохранить\" активна"
        else:
            assert True