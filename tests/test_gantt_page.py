import time

import allure
import pytest
import testit

from data.models.create_project_model import CreateProject
from pages.all_project_page import AllProjectPage
from pages.gantt_page import GanttPage


@allure.suite("Диаграмма ганта")
class TestGanttPage:

    @testit.workItemIds(1296)
    @testit.displayName("14.2.1 Создание фазы")
    @pytest.mark.smoke
    @allure.title("id-1296 14.2.1 Создание фазы")
    def test_creating_a_phase(self, project_with_assignment, login, driver):
        gantt_page = GanttPage(driver)
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(CreateProject().name)
        gantt_page.go_to_gantt_tab()
        gantt_page.add_phase('Фаза 1')
        gantt_page.check_start_and_end_dates('Фаза 1')
        gantt_page.check_status('Фаза 1')

