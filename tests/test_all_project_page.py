import time

import allure
import pytest
import testit

from data.data import USER_NAME
from endpoints.project_endpoint import ProjectEndpoint
from pages.all_project_page import AllProjectPage
from pages.create_local_user_drawer_page import CreateLocalUserDrawerPage
from pages.labor_cost_page import LaborCostPage
from pages.pivot_tab_page import PivotTabPage
from pages.project_card_page import ProjectCardPage
from pages.resource_plane_page import ResourcePlanePage
from pages.user_page import UserPage


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

    @testit.workItemIds(1474)
    @testit.displayName("1.4.1 Удаление проекта на который списаны трудозатраты")
    @pytest.mark.regress
    @allure.title("id-1474 1.4.1 Удаление проекта на который списаны трудозатраты")
    def test_deleting_a_project_for_which_labor_costs_have_been_written_off(self, project_with_work, login, driver):
        projects_page = AllProjectPage(driver)
        projects_page.go_to_all_project_page()
        projects_page.check_delete_project_with_work(project_with_work['name'])

    @testit.workItemIds(940)
    @testit.displayName("1.4.2. Архивация проекта")
    @pytest.mark.regress
    @allure.title("id-940 1.4.2. Архивация проекта")
    def test_archiving_a_project(self, simple_project, login, driver):
        projects_page = AllProjectPage(driver)
        projects_page.go_to_all_project_page()
        projects_page.archiving_a_project(simple_project['name'])
        message = projects_page.get_alert_message()
        assert message == ['Проект заархивирован']
        projects_page.check_archiving_a_project_on_tab(simple_project['name'])
        # Не произошел переход на страницу проекта
        project_card_page = ProjectCardPage(driver)
        project_card_page.check_resource_plan_tab_on_page()
        # Проект на странице трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        time.sleep(2)
        labor_cost_page.check_archive_project(simple_project['name'])
        time.sleep(1)
        # Проект на странице сводная таблица
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(2)
        pivot_tab_page.check_archive_project(simple_project['name'])
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.open_project_list()
        pivot_tab_page.check_project_color_on_user(simple_project['name'])
        # Проект на странице ресурсный план
        resource_plane = ResourcePlanePage(driver)
        resource_plane.go_to_resource_plane_page()
        resource_plane.check_archive_project(simple_project['code'])
        resource_plane.go_to_by_user_tab()
        resource_plane.open_project_list()
        resource_plane.check_project_color_on_user(simple_project['code'])
        # Проект на странице пользователя
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.check_user_is_not_in_table(USER_NAME)
        user_page.go_to_redact_user()
        create_local_user_page = CreateLocalUserDrawerPage(driver)
        time.sleep(2)
        create_local_user_page.go_to_tab_projects()
        project_list = create_local_user_page.get_project_and_roles_text()
        assert simple_project['name'] not in project_list, "Проект отображается в карточке пользователя"

    @testit.workItemIds(941)
    @testit.displayName("1.4.2. Отмена архивации проекта")
    @pytest.mark.regress
    @allure.title("id-941 1.4.2. Отмена архивации проекта")
    def test_cancel_archiving_a_project(self, simple_project, login, driver):
        projects_page = AllProjectPage(driver)
        projects_page.go_to_all_project_page()
        projects_page.cancel_archiving_a_project(simple_project['name'])
        time.sleep(2)
        assert projects_page.get_project_on_tab(simple_project['name']), "Проект отсутствует на странице"

    @testit.workItemIds(944)
    @testit.displayName("1.4.3. Разархивация проекта")
    @pytest.mark.regress
    @allure.title("id-944 1.4.3. Разархивация проекта")
    def test_unzipping_the_project(self, archive_project, login, driver):
        projects_page = AllProjectPage(driver)
        projects_page.go_to_all_project_page()
        projects_page.check_archiving_a_project_on_tab(archive_project['name'])
        projects_page.unzipping_the_project(archive_project['name'])
        message = projects_page.get_alert_message()
        assert message == ['Проект разархивирован'], "Не появилось сообщение об разархивации"
        time.sleep(1)
        assert projects_page.get_project_status(archive_project['name']) == 'Активный', "Статус проекта не Активный"
        # Проект на странице трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.check_add_hour_to_project()
        # Проект на странице пользователя
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.check_user_is_not_in_table(USER_NAME)
        user_page.go_to_redact_user()
        create_local_user_page = CreateLocalUserDrawerPage(driver)
        time.sleep(2)
        create_local_user_page.go_to_tab_projects()
        project_list = create_local_user_page.get_project_and_roles_text()
        assert archive_project['name'] in project_list, "Проект не отображается в карточке пользователя"

    @testit.workItemIds(947)
    @testit.displayName("1.4.3.  Отмена разархивации проекта")
    @pytest.mark.regress
    @allure.title("id-947 1.4.3.  Отмена разархивации проекта")
    def test_cansel_unzipping_the_project(self, archive_project, login, driver):
        projects_page = AllProjectPage(driver)
        projects_page.go_to_all_project_page()
        projects_page.check_archiving_a_project_on_tab(archive_project['name'])
        projects_page.cansel_unzipping_the_project(archive_project['name'])
        assert projects_page.get_project_status(archive_project['name']) == 'В архиве', "Статус проекта изменился"
