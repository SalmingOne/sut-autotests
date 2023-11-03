import time

from pages.create_project_drawer_page import CreateProjectDrawerPage
from pages.project_cart_page import ProjectCardPage
from tests import conftest


class TestCreateProject:
    # id-47 1.1.1 Создание нового проекта
    def test_create_project(self, login, driver):
        create_project_drawer_page = CreateProjectDrawerPage(driver)

        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        project_name, project_code, project_data, project_worker = create_project_drawer_page.create_project()

        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_description_tab()
        time.sleep(3)





