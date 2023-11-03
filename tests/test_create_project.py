from pages.create_project_drawer_page import CreateProjectDrawerPage


class TestCreateProject:
    def test_create_project(self,  login, driver):
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()



