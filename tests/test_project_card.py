import time
from datetime import timedelta, datetime

import allure
import pytest
import testit

from data.data import PROJECT_NAME
from endpoints.project_roles_endpoint import ProjectRolesEndpoint
from endpoints.users_endpoint import UserEndpoint
from pages.all_project_page import AllProjectPage
from pages.gantt_page import GanttPage
from pages.project_card_page import ProjectCardPage


@allure.suite("Карточка проекта")
class TestProjectCard:

    @testit.workItemIds(3185)
    @testit.displayName("1.3.1 Сохранение изменений на вкладке Команда")
    @pytest.mark.smoke
    @allure.title("id-3185 1.3.1 Сохранение изменений на вкладке Команда")
    def test_save_changes_to_the_team_tab(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_team_tab()
        time.sleep(1)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        input_member = project_card_page.get_all_team_members()
        project_card_page.go_to_redact_team()
        time.sleep(1)
        member_before_redact = project_card_page.get_all_team_member_on_redact()
        project_card_page.add_new_member()
        time.sleep(1)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        member_after_redact = project_card_page.get_all_team_members()
        assert input_member[0] == member_before_redact[0], "Роль, ресурс и ставка изменились при нажатии кнопки редактирования"
        assert len(input_member) != len(member_after_redact), "Не добавился новый ресурс"

    @testit.workItemIds(11847)
    @testit.displayName("1.2.2 Содержание табов в карточке проекта.")
    @pytest.mark.regress
    @allure.title("id-11847 1.2.2 Содержание табов в карточке проекта.")
    def test_contents_of_tabs_in_the_project_card(self, project_with_overtime_work, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page = ProjectCardPage(driver)
        project_card_page.check_description_tab()

        project_card_page.go_to_project_hierarchy_tab()
        project_card_page.check_project_hierarchy_tab()

        gantt_page = GanttPage(driver)
        gantt_page.go_to_gantt_tab()
        gantt_page.check_gantt_tab()

        project_card_page.go_to_team_tab()
        project_card_page.check_team_tab()

        project_card_page.go_to_resource_plan_tab()
        project_card_page.check_resource_plan_tab()

        project_card_page.go_to_progress_tab()
        project_card_page.check_progress_tab()

    @testit.workItemIds(10134)
    @testit.displayName("1.2.9. Отображение таблицы Ресурсный план - по дням")
    @pytest.mark.regress
    @allure.title("id-10134 1.2.9. Отображение таблицы Ресурсный план - по дням")
    def test_displaying_the_resource_plan_table_by_day(self, project_with_assignment, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.chose_period('Месяц (по дням)')
        project_card_page.check_resource_plan_tab_title_format_day()
        project_card_page.check_resource_plan_tab_add_percent_button()

    @testit.workItemIds(10135)
    @testit.displayName("1.2.9. Отображение таблицы Ресурсный план - по месяцам")
    @pytest.mark.regress
    @allure.title("id-10135 1.2.9. Отображение таблицы Ресурсный план - по месяцам")
    def test_displaying_the_resource_plan_table_by_month(self, project_with_assignment, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.chose_period('Год')
        project_card_page.check_resource_plan_tab_title_format_month()
        project_card_page.check_resource_plan_tab_add_percent_button()

    @testit.workItemIds(12239)
    @testit.displayName("1.3.1.1. Содержание выпадающих списков Проектная роль и Ресурс")
    @pytest.mark.regress
    @allure.title("id-12239 1.3.1.1. Содержание выпадающих списков Проектная роль и Ресурс")
    def test_contents_of_the_project_role_and_resource_drop_down_lists(self, simple_project, create_work_user, login, driver):
        all_project_page = AllProjectPage(driver)
        project_card_page = ProjectCardPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page.go_to_team_tab()
        # Проверяем все роли и всех пользователей
        user_on_project = project_card_page.get_all_user_before_redact_team_tab()
        project_roles_endpoint = ProjectRolesEndpoint()
        project_roles_system = project_roles_endpoint.get_all_project_roles_name()
        project_card_page.go_to_redact_team()
        project_card_page.press_add_button()
        project_roles_ui = project_card_page.get_all_names_in_li_menu(0)
        user_endpoint = UserEndpoint()
        api_users = user_endpoint.get_names_all_users()
        api_users.remove(user_on_project)
        ui_users = project_card_page.get_all_names_in_li_menu(1)
        # Проверяем проектные роли при заполненном ресурсе
        project_card_page.field_resource_field(create_work_user)
        user_roles_api = user_endpoint.get_user_roles_by_name(create_work_user)
        user_roles_ui = project_card_page.get_all_names_in_li_menu(0)
        project_card_page.press_delete_icon()
        # Проверяем все ресурсы при заполненной проектной роли
        project_card_page.press_add_button()
        api_users_by_role = user_endpoint.get_users_by_project_role_name(user_roles_ui[0])
        project_card_page.field_roles_field(user_roles_ui[0])
        ui_users_by_role = project_card_page.get_all_names_in_li_menu(0)

        assert project_roles_system == project_roles_ui, ("Отображается выпадающий список не со всеми существующими "
                                                          "проектными ролями в системе")
        assert api_users == ui_users, ("Отображается выпадающий список не со всеми существующими "
                                       "пользователями системы которые не назначены на данный проект")
        assert user_roles_api == user_roles_ui, ("Отображается выпадающий список, содержащий не только те проектные"
                                                 " роли, которые доступны пользователю из поля Ресурс")
        assert api_users_by_role == ui_users_by_role, ("Отображается выпадающий список, содержащий не только "
                                                       "пользователей с выбранной проектной ролью")

    @testit.workItemIds(3186)
    @testit.displayName("1.3.1.12 Отмена сохранения изменений на вкладке Команда")
    @pytest.mark.regress
    @allure.title("id-3186 1.3.1.12 Отмена сохранения изменений на вкладке Команда")
    def test_cancel_save_changes_to_the_team_tab(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_team_tab()
        time.sleep(1)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        input_member = project_card_page.get_all_team_members()
        project_card_page.go_to_redact_team()
        time.sleep(1)
        member_before_redact = project_card_page.get_all_team_member_on_redact()
        project_card_page.field_add_new_member_string()
        project_card_page.press_abort_button()
        project_card_page.check_abort_add_resource_window()
        project_card_page.press_modal_submit_button()
        time.sleep(1)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        member_after_redact = project_card_page.get_all_team_members()
        assert input_member[0] == member_before_redact[0], "Роль, ресурс и ставка изменились при нажатии кнопки редактирования"
        assert len(input_member) == len(member_after_redact), "Добавился новый ресурс"

    @testit.workItemIds(54)
    @testit.displayName("1.3.2.1 Редактирование даты начала проекта")
    @pytest.mark.regress
    @allure.title("id-54 1.3.2.1 Редактирование даты начала проекта")
    def test_editing_the_project_start_date(self, project_with_assignment, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page = ProjectCardPage(driver)
        before_start_date = project_card_page.get_project_start_date()
        new_date = datetime.strptime(before_start_date, "%d.%m.%Y").date() - timedelta(1)
        project_card_page.change_start_date(new_date.strftime("%d.%m.%Y"))
        project_card_page.press_submit_button()
        after_start_date = project_card_page.get_project_start_date()

        assert project_card_page.get_alert_message() == 'Свойства проекта успешно изменены', \
            "Не появилось сообщение об изменении проекта"
        assert before_start_date != after_start_date, "Дата начала проекта не изменилась"
        assert after_start_date == new_date.strftime("%d.%m.%Y"), "Дата начала проекта не изменилась на указанную"
