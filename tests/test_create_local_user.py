import allure

from pages.create_local_user_drawer_page import CreateLocalUserDrawerPage


@allure.suite("Дровер создания нового локального пользователя")
class TestCreateLocalUser:

    # id-280 4.2 Содержание дровера "Добавление нового пользователя" при создании локального пользователя
    @allure.title("id-280 4.2 Содержание дровера Добавление нового пользователя при создании локального пользователя")
    def test_create_local_user_drawer(self, login, driver):
        create_local_user_page = CreateLocalUserDrawerPage(driver)
        create_local_user_page.go_to_create_local_user_drawer()
        # Проверяем вкладку Личные данные
        create_local_user_page.check_names_text()
        create_local_user_page.check_placeholder_text()
        create_local_user_page.check_hour_pay_checkbox()
        # Проверяем вкладку Проекты
        create_local_user_page.go_to_tab_projects()
        create_local_user_page.check_add_project_button_and_fields()
        create_local_user_page.check_project_manager_checkbox()
        create_local_user_page.check_delete_project_button()
        # Проверяем вкладку Контакты
        create_local_user_page.go_to_tab_contacts()
        create_local_user_page.check_names_on_contacts_text()
        # Общие кнопки
        create_local_user_page.check_clear_icon_button()
        create_local_user_page.check_save_button()
        create_local_user_page.check_abort_button()
