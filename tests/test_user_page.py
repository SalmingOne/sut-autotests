import allure

from pages.create_local_user_drawer_page import CreateLocalUserDrawerPage
from pages.user_page import UserPage


@allure.suite("Пользователи")
class TestUsersPage:

    @allure.title("id-1382 4.3. Просмотр карточки пользователя в разделе Пользователи")
    def test_viewing_a_user_card_in_the_users_section(self, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        if not user_page.check_user_is_not_in_table('АвтоСПроектом'):
            create_local_user_page = CreateLocalUserDrawerPage(driver)
            create_local_user_page.go_to_create_local_user_drawer()
            create_local_user_page.field_required_fields('AutoTester1', 'АвтоСПроектом', 'auto_testt@mail.ru', 'yes')
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
        assert project_data == ['Проект', 'Роль в проекте', 'Руководитель проекта'], "Отсутствуют поля на вкладке проекты"
        assert contact_data == ['Телефон', 'Почта'], "Отсутствуют поля на вкладке контакты"

    @allure.title("id-134 4.8 Подтверждение восстановления пользователя")
    def test_user_recovery_confirmation(self, login, driver):
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        # Проверяем что есть нужный пользователь
        if not user_page.check_user_is_not_in_table('Автотестов'):
            create_local_user_page = CreateLocalUserDrawerPage(driver)
            create_local_user_page.field_required_fields('AutoTester', 'Автотестов', 'auto_test@mail.ru', 'yes')
        else:
            pass
        if user_page.get_user_status() == 'Уволeн':
            pass
        else:
            user_page.fired_user()
        # Проверяем восстановление пользователя
        user_page.restore_user()
        assert user_page.get_user_status() == 'Работает'
        # Увольняем пользователя после теста
        user_page.fired_user()

