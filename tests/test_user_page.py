import time

import allure
import pytest
import testit

from endpoints.users_endpoint import UserEndpoint
from pages.create_local_user_drawer_page import CreateLocalUserDrawerPage
from pages.user_page import UserPage


@allure.suite("Пользователи")
class TestUsersPage:

    @testit.workItemIds(1382)
    @testit.displayName("4.3. Просмотр карточки пользователя в разделе Пользователи")
    @pytest.mark.regress
    @allure.title("id-1382 4.3. Просмотр карточки пользователя в разделе Пользователи")
    def test_viewing_a_user_card_in_the_users_section(self, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        if not user_page.check_user_is_not_in_table('АвтоСПроектом'):
            create_local_user_page = CreateLocalUserDrawerPage(driver)
            create_local_user_page.go_to_create_local_user_drawer()
            create_local_user_page.field_required_fields('AutoTester1', 'АвтоСПроектом', 'auto_testt@mail.rruu', 'yes')
        else:
            pass
        user_page.go_to_user_card()
        user_page.check_user_card_title()
        user_page.check_clear_button()
        personal_data = user_page.get_labels_on_user_card()
        user_page.go_to_tab_projects()
        project_data = user_page.get_labels_on_user_card()
        user_page.go_to_tab_contacts()
        contact_data = user_page.get_labels_on_user_card()
        assert personal_data == ['Логин', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Пол',
                                 'Дата принятия на работу', 'Дата увольнения', 'Проектная роль', 'Системная роль',
                                 'Подразделение', 'Должность', 'Филиал', 'Дополнительная информация',
                                 'Почасовая оплата'], "Отсутствуют некоторые персональные данные"
        assert 'Проект' and 'Роль в проекте' and 'Руководитель проекта' in project_data, "Отсутствуют поля на вкладке проекты"
        assert contact_data == ['Телефон', 'Почта'], "Отсутствуют поля на вкладке контакты"

    @testit.workItemIds(134)
    @testit.displayName("4.8 Подтверждение восстановления пользователя")
    @pytest.mark.regress
    @allure.title("id-134 4.8 Подтверждение восстановления пользователя")
    def test_user_recovery_confirmation(self, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        # Проверяем, что есть нужный пользователь
        if not user_page.check_user_is_not_in_table('Автотестов'):
            create_local_user_page = CreateLocalUserDrawerPage(driver)
            create_local_user_page.go_to_create_local_user_drawer()
            create_local_user_page.field_required_fields('AutoTester', 'Автотестов', 'auto_test@mail.ruru', 'yes')
        else:
            pass
        if user_page.get_user_status() == 'Уволeн':
            pass
        else:
            user_page.fired_user()
        # Проверяем восстановление пользователя
        user_page.restore_user()
        assert user_page.get_user_status() == 'Работает', "Пользователь не восстановлен"
        # Увольняем пользователя после теста
        user_page.fired_user()

    @testit.workItemIds(30)
    @testit.displayName("4.9 Содержание страницы Пользователи")
    @pytest.mark.smoke
    @allure.title("id-30 4.9 Содержание страницы Пользователи")
    def test_contents_of_the_users_page(self, login, driver):
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
        assert fired_kebab_menu == ['Полная информация', 'Редактировать', 'Восстановить'], "Есть не все элементы в кебаб меню"
        assert work_kebab_menu == ['Полная информация', 'Редактировать', 'Уволить'], "Есть не все элементы в кебаб меню"

    @testit.workItemIds(129)
    @testit.displayName("4.6 Выбрать Дату увольнения раньше Даты принятия на работу")
    @pytest.mark.regress
    @allure.title("id-129 4.6 Выбрать Дату увольнения раньше Даты принятия на работу")
    def test_select_the_dismissal_date_before_the_hiring_date(self, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        # Проверяем, что есть нужный пользователь
        if not user_page.check_user_is_not_in_table('АвтоСПроектом'):
            create_local_user_page = CreateLocalUserDrawerPage(driver)
            create_local_user_page.go_to_create_local_user_drawer()
            create_local_user_page.field_required_fields('AutoTester1', 'АвтоСПроектом', 'auto_testt@mail.rruu', 'yes')
        else:
            pass
        # Ставим пользователю текущий день как дату принятия на работу
        user_page.set_the_hiring_date_on_this_day()
        # Проводим тест
        user_page.check_fired_data_on_date_picker()

    @testit.workItemIds(482)
    @testit.displayName("7.1.1 Назначение системной роли пользователю")
    @pytest.mark.smoke
    @allure.title("id-482 7.1.1 Назначение системной роли пользователю")
    def test_assigning_a_system_role_to_a_user(self, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        # Проверяем, что есть нужный пользователь
        if not user_page.check_user_is_not_in_table('АвтоСПроектом'):
            create_local_user_page = CreateLocalUserDrawerPage(driver)
            create_local_user_page.go_to_create_local_user_drawer()
            create_local_user_page.field_required_fields('AutoTester1', 'АвтоСПроектом', 'auto_testt@mail.rruu', 'yes')
        else:
            pass
        # Проводим тест
        user_page.check_assigning_system_role_to_user()

    @testit.workItemIds(1376)
    @testit.displayName("4.13 Удаление единственной проектной роли у пользователя")
    @pytest.mark.smoke
    @allure.title("id-1376 4.13 Удаление единственной проектной роли у пользователя")
    def test_removing_a_single_project_role_from_a_user(self, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        user_endpoint = UserEndpoint()
        users = user_endpoint.get_users_whit_one_project_role_and_no_assignments()
        user_page.check_user_is_not_in_table(users[0])
        user_page.check_removing_a_single_project_role_from_a_user()
