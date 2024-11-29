import time

import allure
import pytest
import testit

from endpoints.users_endpoint import UserEndpoint
from pages.labor_cost_page import LaborCostPage
from pages.user_page import UserPage
from pages.user_profile_page import UserProfilePage
from pages.colleagues_page import ColleaguesPage


@allure.suite("Пользователи")
class TestUsersPage:

    @testit.workItemIds(1382)
    @testit.displayName("4.3. Просмотр карточки пользователя в разделе Пользователи")
    @pytest.mark.regress
    @allure.title("id-1382 4.3. Просмотр карточки пользователя в разделе Пользователи")
    def test_viewing_a_user_card_in_the_users_section(self, create_work_user, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.check_user_is_not_in_table('АвтоСПроектом')
        user_page.go_to_user_card()
        user_page.check_user_card_title()
        user_page.check_clear_button()
        personal_data = user_page.get_labels_on_user_card()
        user_page.go_to_tab_contacts()
        contact_data = user_page.get_labels_on_user_card()
        assert personal_data == ['Логин', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Пол',
                                 'Дата принятия на работу', 'Дата увольнения', 'Проектная роль', 'Системная роль',
                                 'Подразделение', 'Должность', 'Филиал', 'Дополнительная информация',
                                 'Почасовая оплата'], "Отсутствуют некоторые персональные данные"
        assert contact_data == ['Телефон', 'Почта'], "Отсутствуют поля на вкладке контакты"

    @testit.workItemIds(134)
    @testit.displayName("4.8 Подтверждение восстановления пользователя")
    @pytest.mark.regress
    @allure.title("id-134 4.8 Подтверждение восстановления пользователя")
    def test_user_recovery_confirmation(self, create_fired_user, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.check_user_is_not_in_table('Автотестов')
        # Проверяем восстановление пользователя
        user_page.restore_user()
        time.sleep(2)
        assert user_page.get_user_status() == 'Работает', "Пользователь не восстановлен"
        # Увольняем пользователя после теста
        user_page.fired_user()

    @testit.workItemIds(30)
    @testit.displayName("4.9 Содержание страницы Пользователи")
    @pytest.mark.smoke
    @allure.title("id-30 4.9 Содержание страницы Пользователи")
    def test_contents_of_the_users_page(self, create_work_user, create_fired_user, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.check_user_page_title()
        user_page.check_add_user_buttons()
        user_page.check_columns_headers()
        user_page.check_filter_button()
        user_page.check_search_fields()
        user_page.check_filter_tab_buttons()
        user_page.check_user_is_not_in_table('Автотестов')
        fired_kebab_menu = user_page.get_kebab_menu_item()

        user_page.check_user_is_not_in_table('АвтоСПроектом')
        work_kebab_menu = user_page.get_kebab_menu_item()
        assert fired_kebab_menu == ['Полная информация', 'Редактировать',
                                    'Восстановить'], "Есть не все элементы в кебаб меню"
        assert work_kebab_menu == ['Полная информация', 'Редактировать', 'Уволить'], "Есть не все элементы в кебаб меню"

    @testit.workItemIds(129)
    @testit.displayName("4.6 Выбрать Дату увольнения раньше Даты принятия на работу")
    @pytest.mark.regress
    @allure.title("id-129 4.6 Выбрать Дату увольнения раньше Даты принятия на работу")
    def test_select_the_dismissal_date_before_the_hiring_date(self, create_work_user, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.check_user_is_not_in_table('АвтоСПроектом')
        hiring_date = user_page.get_the_hiring_date()
        # Проводим тест
        user_page.check_fired_data_on_date_picker(hiring_date)

    @testit.workItemIds(482)
    @testit.displayName("7.1.1 Назначение системной роли пользователю")
    @pytest.mark.smoke
    @allure.title("id-482 7.1.1 Назначение системной роли пользователю")
    def test_assigning_a_system_role_to_a_user(self, create_work_user, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.check_user_is_not_in_table('АвтоСПроектом')
        # Проводим тест
        user_page.check_assigning_system_role_to_user()

    @testit.workItemIds(1376)
    @testit.displayName("4.13 Удаление единственной проектной роли у пользователя")
    @pytest.mark.smoke
    @allure.title("id-1376 4.13 Удаление единственной проектной роли у пользователя")
    def test_removing_a_single_project_role_from_a_user(self, create_user_with_one_project_role_and_no_assignments, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.check_user_is_not_in_table(create_user_with_one_project_role_and_no_assignments)
        user_page.check_removing_a_single_project_role_from_a_user()

    @testit.workItemIds(2061)
    @testit.displayName("4.9.1.1 Фильтрация пользователей по фильтру Почасовая оплата")
    @pytest.mark.smoke
    @allure.title("id-2061 4.9.1.1 Фильтрация пользователей по фильтру Почасовая оплата")
    def test_filtering_users_by_the_hourly_wage_filter(self, create_hourly_wage_user, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.press_filter_button()
        user_page.press_by_salary_checkbox()
        user_page.press_hourly_wage_checkbox()
        user_page.check_no_data_image()

        user_page.press_hourly_wage_checkbox()
        before_checkboxes = user_page.get_checked_checkboxes_text()
        user_page.action_esc()
        assert user_page.check_user_is_not_in_table(create_hourly_wage_user), \
            "На странице не отображается пользователь с почасовой оплатой"

        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        user_page.go_to_user_page()
        user_page.press_filter_button()
        after_checkboxes = user_page.get_checked_checkboxes_text()
        assert before_checkboxes == after_checkboxes, \
            "Настройки фильтрации не сохранились при переходе на другую страницу"

    @testit.workItemIds(2063)
    @testit.displayName("4.9.1.1 Изменение значения фильтра в блоке заработной платы")
    @pytest.mark.smoke
    @allure.title("id-2063 4.9.1.1 Изменение значения фильтра в блоке заработной платы")
    def test_changing_the_filter_value_in_the_salary_block(self, create_hourly_wage_user, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.press_filter_button()
        user_page.press_by_salary_checkbox()
        user_page.press_hourly_wage_checkbox()
        before_checkboxes = user_page.get_checked_checkboxes_text()
        user_page.check_no_data_image()
        user_page.action_esc()
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        user_page.go_to_user_page_simple()
        user_page.press_filter_button()
        after_checkboxes = user_page.get_checked_checkboxes_text()
        assert before_checkboxes == after_checkboxes, \
            "Настройки фильтрации не сохранились при переходе на другую страницу"

    @testit.workItemIds(11854)
    @testit.displayName("4.6 Запланированное увольнение пользователя / отмена увольнения")
    @pytest.mark.regress
    @allure.title("id-11854 4.6 Запланированное увольнение пользователя / отмена увольнения")
    def test_planned_user_termination_cancellation_of_termination(self, add_all_statement_files,
                                                                  create_user_with_one_project_role_and_no_assignments,
                                                                  login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.check_user_is_not_in_table(create_user_with_one_project_role_and_no_assignments)
        user_page.go_to_redact_user()
        user_page.check_clickable_previous_day()
        user_page.action_esc()
        user_page.press_cancel_button()
        user_page.go_to_redact_user()
        user_page.check_clickable_previous_day()
        user_page.press_next_day_button_in_data_picker()
        user_page.press_submit_button()
        message = user_page.get_alert_message()
        time.sleep(2)
        user_page.check_restore_menu_item()
        user_page.check_data_fired_in_drawer()
        time.sleep(1)
        user_page.press_cancel_button()
        # Восстановление пользователя
        user_page.restore_user()
        assert message == ['Пользователь изменен'], "Нет сообщения об изменении пользователя"

    @testit.workItemIds(483)
    @testit.displayName("7.1.1 Снятие системной роли с пользователя")
    @pytest.mark.regress
    @allure.title("id-483 7.1.1 Снятие системной роли с пользователя")
    def test_removing_system_role_from_user(self, create_system_role,
                                            create_user_with_two_system_role, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_page.check_delete_system_role_from_user(create_user_with_two_system_role,
                                                     create_system_role['name'])
        # Удаленная роль была с правами просмотра чужих резюме
        # Проверяем, может ли пользователь посмотреть чужое резюме
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user(create_user_with_two_system_role)
        time.sleep(1)
        colleagues_page.go_to_watch_the_user_eyes()
        colleagues_page.go_colleagues_page()
        colleagues_page.check_user_name_link()
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_resume_tab()
        user_profile_page.check_resume_tab_unavailable_without_rights()
