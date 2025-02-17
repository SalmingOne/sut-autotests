import time
from datetime import timedelta, datetime

import allure
import pytest
import testit

from data.data import PROJECT_NAME
from endpoints.project_roles_endpoint import ProjectRolesEndpoint
from endpoints.busy_percentages_endpoint import BusyPercentagesEndpoint
from endpoints.users_endpoint import UserEndpoint
from pages.all_project_page import AllProjectPage
from pages.colleagues_page import ColleaguesPage
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
        time.sleep(2)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        input_member = project_card_page.get_all_team_members()
        project_card_page.go_to_redact_team()
        time.sleep(1)
        member_before_redact = project_card_page.get_all_team_member_on_redact()
        project_card_page.add_new_member()
        time.sleep(2)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        member_after_redact = project_card_page.get_all_team_members()
        assert input_member[0] == member_before_redact[0], "Роль, ресурс и ставка изменились при нажатии кнопки редактирования"
        assert len(input_member) != len(member_after_redact), "Не добавился новый ресурс"

    @testit.workItemIds(11847)
    @testit.displayName("1.2.2 Содержание табов в карточке проекта.")
    @pytest.mark.regress
    @allure.title("id-11847 1.2.2 Содержание табов в карточке проекта.")
    def test_contents_of_tabs_in_the_project_card(self, project_with_three_overtime_work, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        time.sleep(2)
        project_card_page = ProjectCardPage(driver)
        project_card_page.check_description_tab()

        gantt_page = GanttPage(driver)
        gantt_page.go_to_gantt_tab()
        gantt_page.check_gantt_tab()

        project_card_page.go_to_team_tab()
        project_card_page.check_team_tab()
        time.sleep(2)
        # Переход на ресурсный план может положить стенд, пока закомментировал
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
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page = ProjectCardPage(driver)
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
        ui_users_by_role = project_card_page.get_all_names_in_li_menu(1)

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
        time.sleep(1)
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_team_tab()
        time.sleep(2)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
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

    @testit.workItemIds(78)
    @testit.displayName("1.3.2.1 Пустой ввод в поле Код проекта")
    @pytest.mark.regress
    @allure.title("id-78 1.3.2.1 Пустой ввод в поле Код проекта")
    def test_blank_entry_in_the_project_code_field(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page = ProjectCardPage(driver)
        project_card_page.clear_code_field()
        assert project_card_page.get_mui_error() == 'Поле обязательно', \
            "Не отображается подсказка об обязательности поля"
        assert project_card_page.get_code_field_color() == 'rgb(211, 47, 47)', "Поле код не выделяется красным"

    @testit.workItemIds(80)
    @testit.displayName("1.3.2.1 Редактирование значения поля Названия проекта на уже имеющееся в системе")
    @pytest.mark.regress
    @allure.title("id-80 1.3.2.1 Редактирование значения поля Названия проекта на уже имеющееся в системе")
    def test_editing_the_project_name_to_already_available_in_the_system(self, simple_project, second_project, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.change_project_name(second_project['name'])
        assert project_card_page.get_mui_error() == 'Указанное название проекта уже используется в системе', \
            "Не появилось сообщение о существовании проекта с данным именем"
        assert project_card_page.get_name_field_color() == 'rgb(211, 47, 47)', "Поле имя проекта не выделяется красным"

    @testit.workItemIds(81)
    @testit.displayName("1.3.2.1 Редактирование значения поля Код проекта на уже имеющееся в системе")
    @pytest.mark.regress
    @allure.title("id-81 1.3.2.1 Редактирование значения поля Код проекта на уже имеющееся в системе")
    def test_editing_the_project_code_to_already_available_in_the_system(self, simple_project, second_project, login,
                                                                         driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.change_project_code(second_project['code'])
        assert project_card_page.get_mui_error() == 'Указанный код проекта уже используется в системе', \
            "Не появилось сообщение о существовании проекта с данным кодом"
        assert project_card_page.get_code_field_color() == 'rgb(211, 47, 47)', "Поле код проекта не выделяется красным"

    @testit.workItemIds(143)
    @testit.displayName("1.3.2.1 Пустой ввод в поле Название проекта")
    @pytest.mark.regress
    @allure.title("id-143 1.3.2.1 Пустой ввод в поле Название проекта")
    def test_blank_entry_in_the_project_name_field(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.clear_name_field()
        assert project_card_page.get_mui_error() == 'Поле обязательно', \
            "Не отображается подсказка об обязательности поля"
        assert project_card_page.get_name_field_color() == 'rgb(211, 47, 47)', "Поле имя проекта не выделяется красным"

    @testit.workItemIds(145)
    @testit.displayName("1.3.2.1 Пустой ввод в поле Дата начала")
    @pytest.mark.regress
    @allure.title("id-145 1.3.2.1 Пустой ввод в поле Дата начала")
    def test_blank_entry_in_the_start_project_date_field(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.clear_start_project_date_field()
        assert project_card_page.get_mui_error() == 'Поле обязательно', \
            "Не отображается подсказка об обязательности поля"
        assert project_card_page.get_start_project_date_field_color() == 'rgb(211, 47, 47)', \
            "Поле дата начала проекта не выделяется красным"

    @testit.workItemIds(313)
    @testit.displayName("1.3.2.3 Удаление чипса с руководителем проекта")
    @pytest.mark.regress
    @allure.title("id-313 1.3.2.3 Удаление чипса с руководителем проекта")
    def test_chip_removal_with_project_manager(self, project_with_assignment_not_current_manager, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_assignment_not_current_manager['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.remove_manager_chips()
        message = project_card_page.get_alert_message()
        time.sleep(1)
        project_card_page.check_manager_label()
        project_card_page.go_to_team_tab()
        time.sleep(1)
        project_card_page.check_text_on_page('АвтоСПроектом')
        # Пока закомментировал выяснения причины проблемы
        #colleagues_page = ColleaguesPage(driver)
        #time.sleep(1)
        #colleagues_page.go_colleagues_page()
        #colleagues_page.search_user('АвтоСПроектом')
        #colleagues_page.go_to_watch_the_user_eyes()
        #all_project_page.go_to_all_project_page()
        #all_project_page.go_project_page(project_with_assignment_not_current_manager['name'])
        #project_card_page.check_resource_plan_tab_on_page()
        #project_card_page.check_text_on_page('Нет данных')
        assert message == 'Свойства проекта успешно изменены'

    @testit.workItemIds(286)
    @testit.displayName("1.3.2.2 Назначение руководителя проекта при редактировании свойств проекта")
    @pytest.mark.regress
    @allure.title("id-286 1.3.2.2 Назначение руководителя проекта при редактировании свойств проекта")
    def test_assigning_a_project_manager_when_editing_project_properties(self, project_with_two_resources, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(1)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_two_resources['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.check_manager_label()
        project_card_page.go_to_team_tab()
        time.sleep(2)
        before_add_manager_time_tab = project_card_page.get_all_team_members()
        project_card_page.go_to_description_tab()
        # Добавление первого менеджера
        first_manager = project_card_page.add_manager(0)
        assert project_card_page.get_all_manger() == [first_manager], "Менеджер не добавился"
        project_card_page.press_submit_button()
        time.sleep(0.5)
        assert project_card_page.get_alert_message() == 'Свойства проекта успешно изменены', \
            "Нет сообщения об изменении проекта"
        project_card_page.check_manager_can_not_delete_himself()
        # Добавление второго менеджера
        second_manager = project_card_page.add_manager(1)
        assert project_card_page.get_all_manger() == [first_manager, second_manager], "Менеджер не добавился"
        project_card_page.press_submit_button()
        time.sleep(2)
        project_card_page.go_to_team_tab()
        time.sleep(2)
        after_add_manager_time_tab = project_card_page.get_all_team_members()
        assert sorted(before_add_manager_time_tab) == sorted(after_add_manager_time_tab), \
            "Изменились проектные роли выбранных менеджеров"

    @testit.workItemIds(3956)
    @testit.displayName("1.3.3.6. Отображение пустой таблицы")
    @pytest.mark.regress
    @allure.title("id-3956 1.3.3.6. Отображение пустой таблицы")
    def test_displaying_an_empty_progress_table(self, project_with_overtime_work, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(1)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_overtime_work['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_progress_tab()
        project_card_page.open_filter()
        project_card_page.press_choose_all_checkbox()
        project_card_page.check_no_checked_checkboxes()
        project_card_page.press_apply_button()
        project_card_page.check_text_on_page('Нет данных')

    @testit.workItemIds(12567)
    @testit.displayName("1.3.3.6. Чек-лист. Фильтрация таблицы по статусу согласованности трудозатрат")
    @pytest.mark.regress
    @allure.title("id-12567 1.3.3.6. Чек-лист. Фильтрация таблицы по статусу согласованности трудозатрат")
    def test_filtering_a_table_by_work_reconciliation_status(self, project_with_three_overtime_work, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(1)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_three_overtime_work['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_progress_tab()
        project_card_page.open_filter()
        project_card_page.press_choose_all_checkbox()
        project_card_page.check_no_checked_checkboxes()
        project_card_page.press_apply_button()
        project_card_page.check_text_on_page('Нет данных')
        project_card_page.open_filter()
        project_card_page.press_wait_approved_checkbox()
        project_card_page.press_apply_button()
        time.sleep(1)
        project_card_page.check_wait_approved_reason_on_tab()
        project_card_page.go_to_next_period()
        project_card_page.open_filter()
        project_card_page.press_wait_approved_checkbox()
        project_card_page.press_approved_checkbox()
        project_card_page.press_apply_button()
        time.sleep(1)
        project_card_page.check_approved_reason_on_tab()
        project_card_page.go_to_next_period()
        project_card_page.open_filter()
        project_card_page.press_approved_checkbox()
        project_card_page.press_rejected_checkbox()
        project_card_page.press_apply_button()
        time.sleep(1)
        project_card_page.check_rejected_on_tab()

    @testit.workItemIds(3736)
    @testit.displayName("1.3.3.3. Отклонение списаний, если не заполнены обязательные поля")
    @pytest.mark.regress
    @allure.title("id-3736 1.3.3.3. Отклонение списаний, если не заполнены обязательные поля")
    def test_rejection_labor_reason_if_required_fields_are_not_filled(self, project_with_three_overtime_work, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(1)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_three_overtime_work['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_progress_tab()
        project_card_page.press_clear_icon()
        assert not project_card_page.check_dialog_submit_button_clickable(), \
            "Кнопка сохранить кликабельна до заполнения обязательных полей"
        project_card_page.field_modal_reason_field('Нужно больше работать')
        assert project_card_page.check_dialog_submit_button_clickable(), \
            "Кнопка сохранить не кликабельна после заполнения обязательных полей"

    @testit.workItemIds(3799)
    @testit.displayName("1.3.3.3. Отмена отклонения в модальном окне Отклонение")
    @pytest.mark.regress
    @allure.title("id-3799 1.3.3.3. Отмена отклонения в модальном окне Отклонение")
    def test_cancel_a_deviation_in_the_decline_modal_window(self, project_with_three_overtime_work, login,
                                                                      driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(1)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_three_overtime_work['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_progress_tab()
        project_card_page.check_wait_approved_reason_on_tab()
        project_card_page.press_clear_icon()
        project_card_page.field_modal_reason_field('Нужно больше работать')
        project_card_page.press_cell_with_labor_reason_by_text('3 + 3')
        project_card_page.press_dialog_abort_button()
        project_card_page.check_wait_approved_reason_on_tab()

    @testit.workItemIds(3800)
    @testit.displayName("1.3.3.3. Отмена отклонения списаний на табе Ход выполнения")
    @pytest.mark.regress
    @allure.title("id-3800 1.3.3.3. Отмена отклонения списаний на табе Ход выполнения")
    def test_cancel_the_rejection_of_write_the_progress_tab(self, project_with_three_overtime_work, login,
                                                            driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(1)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_three_overtime_work['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_progress_tab()
        project_card_page.check_wait_approved_reason_on_tab()
        project_card_page.press_clear_icon()
        project_card_page.field_modal_reason_field('Нужно больше работать')
        project_card_page.press_cell_with_labor_reason_by_text('3 + 3')
        project_card_page.press_dialog_submit_button()
        project_card_page.check_rejected_on_tab()
        project_card_page.press_abort_button()
        project_card_page.check_wait_approved_reason_on_tab()

    @testit.workItemIds(3803)
    @testit.displayName("1.3.3.4. Отмена подтверждения списаний трудозатрат и переработок")
    @pytest.mark.regress
    @allure.title("id-3803 1.3.3.4. Отмена подтверждения списаний трудозатрат и переработок")
    def test_cancel_of_confirmation_of_write_offs_of_labor_costs_and_overtime(self, project_with_three_overtime_work,
                                                                              login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(1)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_three_overtime_work['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_progress_tab()
        project_card_page.check_wait_approved_reason_on_tab()
        project_card_page.press_done_icon()
        project_card_page.check_approved_reason_on_tab()
        project_card_page.press_abort_button()
        project_card_page.check_wait_approved_reason_on_tab()

    @testit.workItemIds(3730)
    @testit.displayName("1.3.3.2 Отображение тултипов при просмотре таблицы Трудозатраты")
    @pytest.mark.regress
    @allure.title("id-3730 1.3.3.2 Отображение тултипов при просмотре таблицы Трудозатраты")
    def test_displaying_tooltips_when_viewing_the_labour_costs_table(self, project_with_three_overtime_work,
                                                                              login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(1)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_three_overtime_work['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_progress_tab()
        project_card_page.go_to_next_period()
        project_card_page.go_to_next_period()
        time.sleep(1)
        assert project_card_page.get_tooltip_text_reject_labor_cost() == 'Сотрудник не работал в этот день', \
            "Отсутствует тултип с причиной отклонения списания"
        assert project_card_page.get_integrations_tooltip_text('3 + 3') == ['Jira:', 'Confluence:', 'Bitbucket:', 'Testit:', 'GitLab:'], \
            "В тултипе указаны не все интеграции"
        assert project_card_page.get_tooltip_text_on_approval_status() == 'Причина отклонения: У нас не перерабатывают', \
            "Отсутствует тултип с причиной отклонения переработки"
        
    @testit.workItemIds(915)
    @testit.displayName('2.1.1.1. Содержание дровера "Добавление процента занятости" ')
    @pytest.mark.regress
    @allure.title('id-915 2.1.1.1. Содержание дровера "Добавление процента занятости" ')
    def test_drover_content_adding_percentage_occupancy(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.change_radiobutton_percent()
        project_card_page.press_add_employment_button()
        project_card_page.check_drover_resource_plan_tab()

    @testit.workItemIds(417)
    @testit.displayName('2.1.1.1. Отмена добавления периода привлечения (дровер)')
    @pytest.mark.regress
    @allure.title('id-417 2.1.1.1. Отмена добавления периода привлечения (дровер)')
    def test_drover_cancel_adding_attraction_period(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.change_radiobutton_percent()
        # Получаем отображение таблицы "Ресурсный план" до изменений
        table_before = project_card_page.displaying_table_resource_plan()
        project_card_page.press_add_employment_button()
        project_card_page.set_period_and_employment()
        project_card_page.press_cancel_in_drover()
        # Получаем отображение таблицы "Ресурсный план" после изменений
        table_after = project_card_page.displaying_table_resource_plan()
        # Проверяем что таблица не изменяется
        assert table_before == table_after, "Данные в таблице изменились после отмены внесения"

    @testit.workItemIds(419)
    @testit.displayName('2.1.1.1. Отмена сохранения внесенных изменений в таблицу "Ресурсный план"')
    @pytest.mark.regress
    @allure.title('id-419 2.1.1.1. Отмена сохранения внесенных изменений в таблицу "Ресурсный план"')
    def test_cancel_saving_changes_resource_plan_table(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.change_radiobutton_percent()
        # Получаем отображение таблицы "Ресурсный план" до изменений
        table_before = project_card_page.displaying_table_resource_plan()
        project_card_page.press_add_employment_button()
        project_card_page.set_period_and_employment()
        project_card_page.press_save_in_drover()
        # Получаем отображение таблицы "Ресурсный план" после изменений
        table_after = project_card_page.displaying_table_resource_plan()
        # Проверяем что таблица изменяется
        assert table_before != table_after, "Выбранный в дровере период привлечения не отображается в таблице 'Ресурсный план'"
        project_card_page.press_break_button()
        # Получаем отображение таблицы "Ресурсный план" после отмены сохранения
        table_after_cancel = project_card_page.displaying_table_resource_plan()
        # Проверяем что таблица вернулась к изначальному состоянию
        assert table_before == table_after_cancel, \
            "Выбранный в дровере период привлечения после отмены не исчезает из таблицы 'Ресурсный план'"

    @testit.workItemIds(384)
    @testit.displayName('2.1.1.2. Отображение заливки ячеек при выборе процента привлечения ресурса')
    @pytest.mark.regress
    @allure.title('id-384 2.1.1.2. Отображение заливки ячеек при выборе процента привлечения ресурса')
    def test_displaying_cell_fill_percentage_resource_attraction(self, project_with_two_resources, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        time.sleep(1)
        all_project_page.go_project_page(project_with_two_resources['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.change_radiobutton_percent()
        time.sleep(1)
        project_card_page.checking_cell_default_value()
        project_card_page.checking_cell_dropdown_list_values()
        project_card_page.checking_color_cell()

    @testit.workItemIds(481)
    @testit.displayName('2.1.1.2. Отмена редактирования процента занятости')
    @pytest.mark.regress
    @allure.title('id-481 2.1.1.2. Отмена редактирования процента занятости')
    def test_cancel_editing_percentage_employment(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.change_radiobutton_percent()
        # Получаем отображение таблицы "Ресурсный план" до изменений
        table_before = project_card_page.displaying_table_resource_plan()
        project_card_page.change_table_resource_plan()
        # Получаем отображение таблицы "Ресурсный план" после изменений
        table_after = project_card_page.displaying_table_resource_plan()
        assert table_before != table_after, "Внесенные изменения не отображаются"
        project_card_page.press_break_button()
        # Получаем отображение таблицы "Ресурсный план" после отмены сохранения
        table_after_cancel = project_card_page.displaying_table_resource_plan()
        # Проверяем что таблица не изменяется
        assert table_before == table_after_cancel, "Данные в таблице изменились после отмены внесения"

    @testit.workItemIds(11798)
    @testit.displayName('2.1.1.2.1. Отмена редактирования часов занятости')
    @pytest.mark.regress
    @allure.title('id-11798 2.1.1.2.1. Отмена редактирования часов занятости')
    def test_cancel_editing_hours_employment(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        # Получаем отображение таблицы "Ресурсный план" до изменений
        table_before = project_card_page.displaying_table_resource_plan()
        project_card_page.change_table_resource_plan()
        # Получаем отображение таблицы "Ресурсный план" после изменений
        table_after = project_card_page.displaying_table_resource_plan()
        assert table_before != table_after, "Внесенные изменения не отображаются"
        project_card_page.press_break_button()
        # Получаем отображение таблицы "Ресурсный план" после отмены сохранения
        table_after_cancel = project_card_page.displaying_table_resource_plan()
        # Проверяем что таблица не изменяется
        assert table_before == table_after_cancel, "Данные в таблице изменились после отмены внесения"

    @testit.workItemIds(11787)
    @testit.displayName("2.1.1.1. Просмотр таблицы 'Ресурсный план' при отсутствии ресурсов")
    @pytest.mark.regress
    @allure.title("id-11787 2.1.1.1. Просмотр таблицы 'Ресурсный план' при отсутствии ресурсов")
    def test_viewing_resource_plan_tab_without_resources(self,  no_resources_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(no_resources_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab_not_wait()
        project_card_page.check_resource_plan_tab_without_resources()

    @testit.workItemIds(1955)
    @testit.displayName('2.1.2.2 Переключение временных интервалов')
    @pytest.mark.regress
    @allure.title('id-1955 2.1.2.2 Переключение временных интервалов')
    def test_switching_time_intervals(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.switching_time_intervals('quarter')
        project_card_page.chose_period('Месяц (по дням)')
        project_card_page.switching_time_intervals('month')
        project_card_page.chose_period('Год')
        project_card_page.switching_time_intervals('year')

    @testit.workItemIds(11794)
    @testit.displayName('2.1.1.1.1. Отмена добавление периодов привлечения и почасовой занятости для ресурса (дровер)')
    @pytest.mark.regress
    @allure.title('id-11794 2.1.1.1.1. Отмена добавление периодов привлечения и почасовой занятости для ресурса (дровер)')
    def test_cancel_adding_periods_hour_employment_driver(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        # Получаем отображение таблицы "Ресурсный план" до изменений
        table_before = project_card_page.displaying_table_resource_plan()
        project_card_page.press_add_employment_button()
        project_card_page.set_period_and_employment()
        project_card_page.press_cancel_in_drover()
        # Получаем отображение таблицы "Ресурсный план" после изменений
        table_after = project_card_page.displaying_table_resource_plan()
        # Проверяем что таблица не изменяется
        assert table_before == table_after, "Данные в таблице изменились после отмены внесения"
    
    @testit.workItemIds(444)
    @testit.displayName('2.1.1.1 Обзор дат за границами проекта в выпадающем календаре')
    @pytest.mark.regress
    @allure.title('id-444 2.1.1.1 Обзор дат за границами проекта в выпадающем календаре')
    def test_overview_dates_outside_boundary_project_drop_down_calendar(self, short_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(short_project['name'])
        project_card_page = ProjectCardPage(driver)
        start_date = project_card_page.get_project_start_date()
        end_date = project_card_page.get_project_end_date()
        project_card_page.go_to_resource_plan_tab()
        project_card_page.change_radiobutton_percent()
        project_card_page.press_add_employment_button()
        project_card_page.press_start_date_in_drover()
        project_card_page.check_dropdown_calendar()
        project_card_page.check_dates_outside_project_boundaries(start_date, end_date)

    @testit.workItemIds(1956)
    @testit.displayName('2.1.2.2 Уведомление о несохраненных данных в ячейках при переходе в другой раздел')
    @pytest.mark.regress
    @allure.title('id-1956 2.1.2.2 Уведомление о несохраненных данных в ячейках при переходе в другой раздел')
    def test_message_unsaved_data_in_cells_when_navigation(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        time.sleep(1)
        # Получаем отображение таблицы "Ресурсный план" до изменений
        table_before = project_card_page.displaying_table_resource_plan()
        project_card_page.change_table_resource_plan()
        # Получаем отображение таблицы "Ресурсный план" после изменений
        table_after = project_card_page.displaying_table_resource_plan()
        assert table_before != table_after, "Внесенные изменения не отображаются"
        project_card_page.go_to_description_tab()
        project_card_page.check_abort_add_resource_window()

    @testit.workItemIds(433)
    @testit.displayName('2.1.1.1. Добавление процента занятости для ресурса')
    @pytest.mark.regress
    @allure.title('id-433 2.1.1.1. Добавление процента занятости для ресурса')
    def test_adding_busy_percentage_for_resource(self, simple_project, project_with_planned_resources, login, driver):
        start_date = str(project_with_planned_resources[0])
        end_date = str(project_with_planned_resources[1])
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.change_radiobutton_percent()
        project_card_page.press_add_employment_button()
        project_card_page.set_period_and_busy(start_date, end_date, 4)
        project_card_page.press_save_in_drover()
        # Получаем отображение таблицы "Ресурсный план" до сохранения
        table_before = project_card_page.displaying_table_resource_plan()
        # Получаем процент привлечения на фронте
        percentage_ui = project_card_page.get_busy(start_date)
        project_card_page.press_submit_button()
        # Получаем отображение таблицы "Ресурсный план" после сохранения
        table_after = project_card_page.displaying_table_resource_plan()
        # Получаем busy_percentages после сохранения
        busy_percentages_endpoint = BusyPercentagesEndpoint()
        busy_percentages_api = busy_percentages_endpoint.get_busy_percentages_api(simple_project['id'])
        percentage_api = [entry['percentage'] for entry in busy_percentages_api]
        assert percentage_ui == '50%'
        assert percentage_api == [50, 50, 50, 50, 50], "Внесенные изменения не сохранились в БД"
        assert table_before == table_after, "Данные в таблице не сохранились"
    
    @testit.workItemIds(11791)
    @testit.displayName('2.1.1.1. Превышение процента занятости для ресурса')
    @pytest.mark.regress
    @allure.title('id-11791 2.1.1.1. Превышение процента занятости для ресурса')
    def test_overoccupancy_percentage_for_resource(self, simple_project, project_with_planned_resources, login, driver):
        start_date = str(project_with_planned_resources[0])
        end_date = str(project_with_planned_resources[1])
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.change_radiobutton_percent()
        project_card_page.press_add_employment_button()
        project_card_page.set_period_and_busy(start_date, end_date, 8)
        project_card_page.press_save_in_drover()
        project_card_page.check_color_cell()
        save_button = project_card_page.check_save_button_is_clickable()
        assert not save_button, "Кнопка Сохранить кликабельна"

    @testit.workItemIds(11788)
    @testit.displayName('2.1.1.1.1. Добавление периодов привлечения и почасовой занятости для ресурса')
    @pytest.mark.regress
    @allure.title('id-11788 2.1.1.1.1. Добавление периодов привлечения и почасовой занятости для ресурса')
    def test_adding_busy_hours_for_resource(self, simple_project, project_with_planned_resources, login, driver):
        start_date = str(project_with_planned_resources[0])
        end_date = str(project_with_planned_resources[1])
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.press_add_employment_button()
        project_card_page.set_period_and_busy(start_date, end_date, 4)
        project_card_page.press_save_in_drover()
        # Получаем отображение таблицы "Ресурсный план" до сохранения
        table_before = project_card_page.displaying_table_resource_plan()
        # Получаем процент привлечения на фронте
        percentage_ui = project_card_page.get_busy(start_date)
        project_card_page.press_submit_button()
        # Получаем отображение таблицы "Ресурсный план" после сохранения
        table_after = project_card_page.displaying_table_resource_plan()
        # Получаем busy_hours после сохранения
        busy_percentages_endpoint = BusyPercentagesEndpoint()
        busy_percentages_api = busy_percentages_endpoint.get_busy_percentages_api(simple_project['id'])
        percentage_api = [entry['percentage'] for entry in busy_percentages_api]
        assert percentage_ui == '20'
        assert percentage_api == [50, 50, 50, 50, 50], "Внесенные изменения не сохранились в БД"
        assert table_before == table_after, "Данные в таблице не сохранились"
    
    @testit.workItemIds(11792)
    @testit.displayName('2.1.1.1.1. Превышение суммы почасовой занятости для ресурса')
    @pytest.mark.regress
    @allure.title('id-11792 2.1.1.1.1. Превышение суммы почасовой занятости для ресурса')
    def test_overoccupancy_hours_for_resource(self, simple_project, project_with_planned_resources, login, driver):
        start_date = str(project_with_planned_resources[0])
        end_date = str(project_with_planned_resources[1])
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.press_add_employment_button()
        project_card_page.set_period_and_busy(start_date, end_date, 8)
        project_card_page.press_save_in_drover()
        project_card_page.check_color_cell('hours')
        save_button = project_card_page.check_save_button_is_clickable()
        assert not save_button, "Кнопка Сохранить кликабельна"

    @testit.workItemIds(11795)
    @testit.displayName('2.1.1.1.1. Отмена добавления периодов привлечения и почасовой занятости для ресурса (таблица)')
    @pytest.mark.regress
    @allure.title('id-11795 2.1.1.1.1. Отмена добавления периодов привлечения и почасовой занятости для ресурса (таблица)')
    def test_cancel_adding_busy_hours_for_resource(self, simple_project, project_with_planned_resources, login, driver):
        start_date = str(project_with_planned_resources[0])
        end_date = str(project_with_planned_resources[1])
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        # Получаем отображение таблицы "Ресурсный план" до внесения изменений
        table_before = project_card_page.displaying_table_resource_plan()
        project_card_page.press_add_employment_button()
        project_card_page.set_period_and_busy(start_date, end_date, 4)
        project_card_page.press_save_in_drover()
        # Получаем отображение таблицы "Ресурсный план" после внесения изменений
        table_after = project_card_page.displaying_table_resource_plan()
        assert table_before != table_after, 'Внесенные изменения не отображаются'
        project_card_page.press_break_button()
        # Получаем отображение таблицы "Ресурсный план" после отмены сохранения
        table_after_break = project_card_page.displaying_table_resource_plan()
        assert table_before == table_after_break, "Данные в таблице сохранились после отмены"
    
    @testit.workItemIds(554)
    @testit.displayName('2.1.2.3. Сохранение данных при переключении временных периодов')
    @pytest.mark.regress
    @allure.title('id-554 2.1.2.3. Сохранение данных при переключении временных периодов')
    def test_saving_data_when_switching_time_periods(self, project_with_two_resources, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_two_resources['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.change_table_resource_plan()
        value = project_card_page.get_value_cell()
        project_card_page.switching_time_intervals('quarter')
        value_after_switching = project_card_page.get_value_cell()
        assert value == value_after_switching, 'Данные после переключения интервалов не сохранились'
        project_card_page.press_submit_button()
        message = project_card_page.get_alert_message()
        value_after_submit = project_card_page.get_value_cell()
        assert value == value_after_submit, 'Данные после сохранения не сохранились'
        assert message == 'Данные сохранены', 'Нет сообщения об успешном сохранении данных'

    @testit.workItemIds(1968)
    @testit.displayName('2.1.2.3.Отмена сохранения данных на фронте в таблице ресурсный план \
                        при переключении временных периодов')
    @pytest.mark.regress
    @allure.title('id-1968 2.1.2.3.Отмена сохранения данных на фронте в таблице ресурсный план \
                  при переключении временных периодов')
    def test_cancel_saving_data_when_switching_time_periods(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.change_table_resource_plan()
        value = project_card_page.get_value_cell()
        project_card_page.switching_time_intervals('quarter')
        value_after_switching = project_card_page.get_value_cell()
        assert value == value_after_switching, 'Данные после переключения интервалов не сохранились'
        project_card_page.press_break_button()
        value_after_break = project_card_page.get_value_cell()
        assert value != value_after_break, 'Данные в таблице сохранились после отмены'
    
    @testit.workItemIds(11826)
    @testit.displayName('2.1.2.4 Переключение режима отображения трудозатрат проценты/часы')
    @pytest.mark.regress
    @allure.title('id-11826 2.1.2.4 Переключение режима отображения трудозатрат проценты/часы')
    def test_switch_display_mode_of_labor_costs_percentage_hours(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.press_add_employment_button()
        start_date, end_date = project_card_page.get_full_work_week()
        project_card_page.set_period_and_busy(start_date.strftime("%d.%m.%Y"), end_date.strftime("%d.%m.%Y"))
        project_card_page.press_save_in_drover()
        list_hours = project_card_page.displaying_table_resource_plan()
        index = list_hours.index("40")
        project_card_page.change_radiobutton_percent()
        list_percentage = project_card_page.displaying_table_resource_plan()
        assert list_percentage[index] == "100%", 'Трудозатраты в таблице не перевелись из часов в проценты '
        project_card_page.change_radiobutton_hour()
        list_hours_after = project_card_page.displaying_table_resource_plan()
        assert list_hours == list_hours_after, 'Трудозатраты в таблице не перевелись из процентов в часы '
    
    @testit.workItemIds(11781)
    @testit.displayName('2.1.2.2 Отображение часов при заполнении таблицы во временном интервале "Квартал"')
    @pytest.mark.regress
    @allure.title('id-11781 2.1.2.2 Отображение часов при заполнении таблицы во временном интервале "Квартал"')
    def test_displaying_hours_when_table_full_in_quarter(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.press_add_employment_button()
        start_date, end_date = project_card_page.get_current_month_start_end()
        project_card_page.set_period_and_busy(start_date.strftime("%d.%m.%Y"), end_date.strftime("%d.%m.%Y"))
        project_card_page.press_save_in_drover()
        list_quarter = project_card_page.displaying_table_resource_plan()
        project_card_page.chose_period('Месяц (по дням)')
        list_month = project_card_page.displaying_table_resource_plan()
        list_quarter = [int(x) for x in list_quarter if x != '-' and x != '0']
        list_week = project_card_page.converting_list_hours_day_to_list_week(list_month)
        assert list_quarter == list_week, 'Сумма часов по дням за неделю не равна значению часов в неделю'
        project_card_page.chose_period('Год')
        list_year = project_card_page.displaying_table_resource_plan()
        assert sum([int(x) for x in list_year if x != '-']) == sum([int(x) for x in list_month if x != '-']), \
            'Сумма часов по дням за месяц не равна значению часов в месяц'
    
    @testit.workItemIds(11783)
    @testit.displayName('2.1.2.2 Отображение часов при заполнении таблицы во временном интервале "Месяц(по дням)"')
    @pytest.mark.regress
    @allure.title('id-11783 2.1.2.2 Отображение часов при заполнении таблицы во временном интервале "Месяц(по дням)"')
    def test_displaying_hours_when_table_full_in_month(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.chose_period('Месяц (по дням)')
        project_card_page.press_add_employment_button()
        start_date, end_date = project_card_page.get_current_month_start_end()
        project_card_page.set_period_and_busy(start_date.strftime("%d.%m.%Y"), end_date.strftime("%d.%m.%Y"))
        project_card_page.press_save_in_drover()
        list_month = project_card_page.displaying_table_resource_plan()
        project_card_page.chose_period('Квартал')
        list_week = project_card_page.converting_list_hours_day_to_list_week(list_month)
        list_quarter = project_card_page.displaying_table_resource_plan()
        list_quarter = [int(x) for x in list_quarter if x != '-' and x != '0']
        assert list_quarter == list_week, 'Сумма часов по дням за неделю не равна значению часов в неделю'
        project_card_page.chose_period('Год')
        list_year = project_card_page.displaying_table_resource_plan()
        assert sum([int(x) for x in list_year if x != '-']) == sum([int(x) for x in list_month if x != '-']), \
            'Сумма часов по дням за месяц не равна значению часов в месяц'

    @testit.workItemIds(11785)
    @testit.displayName('2.1.2.2 Отображение часов при заполнении таблицы во временном интервале "Год"')
    @pytest.mark.regress
    @allure.title('id-11785 2.1.2.2 Отображение часов при заполнении таблицы во временном интервале "Год"')
    def test_displaying_hours_when_table_full_in_year(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(simple_project['name'])
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.chose_period('Год')
        project_card_page.press_add_employment_button()
        start_date, end_date = project_card_page.get_current_month_start_end()
        project_card_page.set_period_and_busy(start_date.strftime("%d.%m.%Y"), end_date.strftime("%d.%m.%Y"))
        project_card_page.press_save_in_drover()
        list_year = project_card_page.displaying_table_resource_plan()
        project_card_page.chose_period('Квартал')
        list_quarter = project_card_page.displaying_table_resource_plan()
        list_quarter = [int(x) for x in list_quarter if x != '-' and x != '0']
        project_card_page.chose_period('Месяц (по дням)')
        list_month = project_card_page.displaying_table_resource_plan()
        list_week = project_card_page.converting_list_hours_day_to_list_week(list_month)
        assert list_quarter == list_week, 'Сумма часов по дням за неделю не равна значению часов в неделю'
        assert sum([int(x) for x in list_year if x != '-']) == sum([int(x) for x in list_month if x != '-']), \
            'Сумма часов по дням за месяц не равна значению часов в месяц'


    @testit.workItemIds(140)
    @testit.displayName("1.3.2.1 Подтверждение изменения даты начала проекта с выхождением запланированных \
                        периодов привлечения за дату начала проекта.")
    @pytest.mark.regress
    @allure.title("id-140 1.3.2.1 Подтверждение изменения даты начала проекта с выхождением запланированных \
                  периодов привлечения за дату начала проекта.")
    def test_confirmation_change_start_date_project_with_out_boundary_planned_resources\
        (self, project_with_planned_resources, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_planned_resources[2]['name'])
        project_card_page = ProjectCardPage(driver)
        before_start_date = project_card_page.get_project_start_date()
        before_end_date = project_card_page.get_project_end_date()
        new_start_date = (datetime.strptime(before_start_date, "%d.%m.%Y").date() + timedelta(1)).strftime("%d.%m.%Y")
        project_card_page.change_start_date(new_start_date)
        project_card_page.press_submit_button()
        project_card_page.check_project_boundaries_modal_window()
        project_card_page.press_modal_submit_button()
        message = project_card_page.get_alert_message()
        after_start_date = project_card_page.get_project_start_date()
        project_card_page.check_project_start_date_in_title(new_start_date)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.press_add_employment_button()
        project_card_page.press_start_date_in_drover()
        project_card_page.check_dates_outside_project_boundaries(new_start_date, before_end_date)
        assert message == 'Свойства проекта успешно изменены', "Не появилось сообщение об изменении проекта"
        assert before_start_date != after_start_date, "Дата начала проекта не изменилась"
        assert after_start_date == new_start_date, "Дата начала проекта не изменилась на указанную"

    @testit.workItemIds(142)
    @testit.displayName("1.3.2.1 Отмена редактирования даты начала проекта с выхождением запланированных \
                        периодов привлечения за дату начала проекта.")
    @pytest.mark.regress
    @allure.title("id-142 1.3.2.1 Отмена редактирования даты начала проекта с выхождением запланированных \
                  периодов привлечения за дату начала проекта.")
    def test_cancel_editing_start_date_project_with_out_boundary_planned_resources\
        (self, project_with_planned_resources, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_planned_resources[2]['name'])
        project_card_page = ProjectCardPage(driver)
        before_start_date = project_card_page.get_project_start_date()
        new_start_date = (datetime.strptime(before_start_date, \
                                            "%d.%m.%Y").date() + timedelta(1)).strftime("%d.%m.%Y")
        project_card_page.change_start_date(new_start_date)
        project_card_page.press_submit_button()
        project_card_page.check_project_boundaries_modal_window()
        project_card_page.press_modal_abort_button()
        after_start_date = project_card_page.get_project_start_date()
        save_button = project_card_page.check_save_button_is_clickable()
        assert save_button, "Кнопка Сохранить не кликабельна"
        assert before_start_date != after_start_date, 'Дата начала проекта не изменилась'
        project_card_page.press_break_button()
        after_break_start_date = project_card_page.get_project_start_date()

        save_button = project_card_page.check_save_button_is_clickable()
        assert not save_button, "Кнопка Сохранить кликабельна"
        assert after_break_start_date == before_start_date, \
            'Дата начала проекта не вернулась к исходной после отмены'

    @testit.workItemIds(66683)
    @testit.displayName("1.3.2.5. Назначение приоритета проекта на табе 'Описание'")
    @pytest.mark.regress
    @allure.title("id-66683 1.3.2.5. Назначение приоритета проекта на табе 'Описание'")
    def test_assigning_project_priority_on_description_tab(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page = ProjectCardPage(driver)
        priority_before = project_card_page.get_priority_on_description_tab()
        project_card_page.check_description_tab_priority_field()
        project_card_page.select_priority()
        project_card_page.press_break_button()
        priority_after_break = project_card_page.get_priority_on_description_tab()
        project_card_page.select_priority()
        project_card_page.press_submit_button()
        priority_after_submit = project_card_page.get_priority_on_description_tab()
        message = project_card_page.get_alert_message()
        assert priority_before == priority_after_break == '', \
            "Поле с приоритетом не очистилось после отмены"
        assert priority_before != priority_after_submit, \
            "Поле с приоритетом не поменялось после сохранения"
        assert message == 'Свойства проекта успешно изменены', \
            "Не появилось сообщение об изменении проекта"

    @testit.workItemIds(74)
    @testit.displayName("1.3.2.1 Подтверждение изменения даты окончания проекта с выхождением "
                        "запланированных периодов привлечения за дату окончания проекта.")
    @pytest.mark.regress
    @allure.title("id-74 1.3.2.1 Подтверждение изменения даты окончания проекта с выхождением "
                  "запланированных периодов привлечения за дату окончания проекта.")
    def test_confirmation_change_end_date_project_with_out_boundary_planned_resources \
                    (self, project_with_planned_resources, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_planned_resources[2]['name'])
        project_card_page = ProjectCardPage(driver)
        before_start_date = project_card_page.get_project_start_date()
        before_end_date = project_card_page.get_project_end_date()
        new_end_date = (datetime.strptime(before_end_date,
                                          "%d.%m.%Y").date() + timedelta(-1)).strftime("%d.%m.%Y")
        project_card_page.change_end_date(new_end_date)
        project_card_page.press_submit_button()
        project_card_page.check_project_boundaries_modal_window()
        project_card_page.press_modal_submit_button()
        message = project_card_page.get_alert_message()
        after_end_date = project_card_page.get_project_end_date()
        project_card_page.check_project_end_date_in_title(new_end_date)
        project_card_page.go_to_resource_plan_tab()
        project_card_page.press_add_employment_button()
        project_card_page.press_end_date_in_drover()
        time.sleep(2) # без этого ожидания не успевает поменяться дата в датапикере
        project_card_page.check_dates_outside_project_boundaries(before_start_date, new_end_date)
        assert message == 'Свойства проекта успешно изменены', "Не появилось сообщение об изменении проекта"
        assert before_end_date != after_end_date, "Дата начала проекта не изменилась"
        assert after_end_date == new_end_date, "Дата начала проекта не изменилась на указанную"

    @testit.workItemIds(67938)
    @testit.displayName("1.3.2.6 (Чек-лист) Возможные переходы из одного статуса в другой в карточке проекта")
    @pytest.mark.regress
    @allure.title("id-67938 1.3.2.6 (Чек-лист) Возможные переходы из одного статуса в другой в карточке проекта")
    def test_possible_transition_from_one_status_to_another_in_project_card(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page = ProjectCardPage(driver)
        assert project_card_page.get_available_status_on_description_tab() == ['В архиве', 'Черновик'], \
            'Дровер содержит статусы, не соответствующие проекту со статусом "Активен"'
        project_card_page.change_status_project('Черновик')
        all_project_page.go_to_all_project_page()
        all_project_page.see_all_status_project()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        assert project_card_page.get_available_status_on_description_tab() == ['Активный'], \
            'Дровер содержит статусы, не соответствующие проекту со статусом "Черновик"'
        project_card_page.change_status_project('Активный')
        project_card_page.change_status_project('В архиве')
        all_project_page.go_to_all_project_page()
        all_project_page.see_all_status_project()
        all_project_page.check_archive_project_is_not_clickable(f"{PROJECT_NAME}")
