from pages.create_local_user_drawer_page import CreateLocalUserDrawerPage


class TestCreateLocalUser:
    def test_create_local_user_drawer(self, login, driver):
        create_local_user_page = CreateLocalUserDrawerPage(driver)
        create_local_user_page.go_to_create_local_user_drawer()
        create_local_user_page.check_names_text()
        create_local_user_page.check_placeholder_text()
        create_local_user_page.check_hour_pay_checkbox()

        create_local_user_page.go_to_tab_projects()
        create_local_user_page.check_add_project_button_and_fields()
        create_local_user_page.check_project_manager_checkbox()

        create_local_user_page.go_to_tab_contacts()
        create_local_user_page.check_names_on_contacts_text()

