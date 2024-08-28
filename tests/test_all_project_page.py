import time

import allure
import pytest
import testit

from endpoints.project_endpoint import ProjectEndpoint
from pages.all_project_page import AllProjectPage
from pages.labor_cost_page import LaborCostPage
from pages.pivot_tab_page import PivotTabPage


@allure.suite("Страница все проекты")
class TestProjectPage:
    @testit.workItemIds(949)
    @testit.displayName("1.2.1. Просмотр страницы всех проектов системы")
    @pytest.mark.smoke
    @allure.title("id-949 1.2.1. Просмотр страницы всех проектов системы")
    def test_view_all_projects_page(self, login, driver):
        projects_page = AllProjectPage(driver)
        projects_page.go_to_all_project_page()
        projects_page.check_all_projects_tab_menu_item()
        projects_page.check_title()
        projects_page.check_create_project_button()
        projects_page.check_only_my_projects_checkbox()
        projects_page.check_tab_column_titles()
        projects_page.check_action_menu_items()

    @testit.workItemIds(3144)
    @testit.displayName("1.2.1. Просмотр своих проектов")
    @pytest.mark.regress
    @allure.title("id-3144 1.2.1. Просмотр своих проектов")
    def test_view_your_projects(self, login, driver):
        projects_page = AllProjectPage(driver)
        projects_page.go_to_all_project_page()
        project_endpoint = ProjectEndpoint()
        api_project_user_names = project_endpoint.get_project_name_for_current_user()
        names_before = projects_page.get_all_project_names_on_page()
        projects_page.press_only_my_projects_checkbox()
        names_after = projects_page.get_all_project_names_on_page()
        assert sorted(names_after) != sorted(names_before), "Не исчезли проекты на которые не назначен пользователь"
        assert sorted(api_project_user_names) == sorted(names_after), \
            "Отображены не все проекты на которые назначен пользователь"

    @testit.workItemIds(1473)
    @testit.displayName("1.4.1 Удаление проекта на который НЕ списаны трудозатраты")
    @pytest.mark.regress
    @allure.title("id-1473 1.4.1 Удаление проекта на который НЕ списаны трудозатраты")
    def test_deleting_a_project_for_which_labor_are_not_written_off(self, simple_project_to_delete, login, driver):
        projects_page = AllProjectPage(driver)
        projects_page.go_to_all_project_page()
        projects_page.check_delete_project(simple_project_to_delete['name'])
        message = projects_page.get_alert_message()
        assert not projects_page.get_project_on_tab(simple_project_to_delete['name']), \
            "Проект отображается в таблице Все проекты"
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(1)
        project_names = labor_cost_page.get_all_project_name_on_tab()
        assert simple_project_to_delete['name'] not in project_names, "Проект отображается в таблице Трудозатраты"
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        assert not projects_page.get_project_on_tab(simple_project_to_delete['name']), \
            "Проект отображается в Сводной таблице"
        assert message == ['Проект удален'], "Отсутствует сообщение об удалении проекта"
