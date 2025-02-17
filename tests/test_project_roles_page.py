
import allure
import pytest
import testit

from pages.project_roles_page import ProjectRolesPage


@allure.suite("Проектные роли")
class TestProjectsRolesPage:

    @testit.workItemIds(1284)
    @testit.displayName("6.1.1.1. Создание новой проектной роли.")
    @pytest.mark.smoke
    @allure.title("id-1284 6.1.1.1. Создание новой проектной роли.")
    def test_create_new_project_role(self, login, driver):
        project_roles_page = ProjectRolesPage(driver)
        project_roles_page.go_to_project_roles_page()
        # Если роль уже есть, то удаляем ее
        if project_roles_page.check_role_name_on_tab('Тестировщик автоматизатор'):
            project_roles_page.delete_project_role('Тестировщик автоматизатор')
        else:
            pass

        project_roles_page.open_create_role_drawer()
        project_roles_page.check_max_size_role_name()
        project_roles_page.check_color_on_color_input()
        project_roles_page.salary_rate_not_clickable()
        project_roles_page.manger_role_checkbox_is_present()
        project_roles_page.field_role_name('Тестировщик автоматизатор')
        project_roles_page.field_first_attraction_rate()
        project_roles_page.abort_button_is_present()
        project_roles_page.clear_drawer_button_is_present()
        project_roles_page.submit_create_role()
        assert project_roles_page.check_role_name_on_tab('Тестировщик автоматизатор')
        # Удаляем созданную роль
        project_roles_page.delete_project_role('Тестировщик автоматизатор')

    @testit.workItemIds(1446)
    @testit.displayName("6.1.1.1 Пустой ввод при создании проектной роли")
    @pytest.mark.regress
    @allure.title("id-1446 6.1.1.1 Пустой ввод при создании проектной роли")
    def test_blank_input_when_create_a_project_role(self, login, driver):
        project_roles_page = ProjectRolesPage(driver)
        project_roles_page.go_to_project_roles_page()
        project_roles_page.open_create_role_drawer()
        project_roles_page.submit_button_not_clickable()

    @testit.workItemIds(1285)
    @testit.displayName("6.1.1.2. Просмотр справочника проектные роли(в системе есть проектные роли)")
    @pytest.mark.smoke
    @allure.title("id-1285 6.1.1.2. Просмотр справочника проектные роли(в системе есть проектные роли)")
    def test_view_project_roles_tab(self, login, driver):
        project_roles_page = ProjectRolesPage(driver)
        project_roles_page.go_to_project_roles_page()
        project_roles_page.create_role_button_is_present()
        project_roles_page.check_roles_tab_headers()
        project_roles_page.check_search_fields()
        project_roles_page.check_filter_icons()
        project_roles_page.check_kebab_menu_items()

    @testit.workItemIds(1445)
    @testit.displayName("6.1.1.1 Дублирование уникальных полей")
    @pytest.mark.regress
    @allure.title("id-1445 6.1.1.1 Дублирование уникальных полей")
    def test_duplicate_unique_fields(self, login, driver):
        project_roles_page = ProjectRolesPage(driver)
        project_roles_page.go_to_project_roles_page()
        project_roles_page.open_create_role_drawer()
        project_roles_page.field_first_attraction_rate()
        project_roles_page.field_role_name('Аналитик')
        project_roles_page.submit_create_role()
        project_roles_page.check_uniqueness_project_role_name()
