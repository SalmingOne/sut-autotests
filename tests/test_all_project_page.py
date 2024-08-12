import allure
import pytest
import testit

from endpoints.project_endpoint import ProjectEndpoint
from pages.all_project_page import AllProjectPage


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
