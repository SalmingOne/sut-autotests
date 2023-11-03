import time

from pages.create_project_drawer_page import CreateProjectDrawerPage
from tests import conftest


class TestCreateProject:
    # id-47 1.1.1 Создание нового проекта
    def test_create_project(self, login, driver):
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        time.sleep(3)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()



