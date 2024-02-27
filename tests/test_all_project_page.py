import allure
import pytest
import testit

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