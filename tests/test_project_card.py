import time

import allure
import pytest
import testit

from data.data import PROJECT_NAME
from pages.all_project_page import AllProjectPage
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
        time.sleep(1)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        input_member = project_card_page.get_all_team_members()
        project_card_page.go_to_redact_team()
        time.sleep(1)
        member_before_redact = project_card_page.get_all_team_member_on_redact()
        project_card_page.add_new_member()
        time.sleep(1)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        member_after_redact = project_card_page.get_all_team_members()
        assert input_member[0] == member_before_redact[0], "Роль, ресурс и ставка изменились при нажатии кнопки редактирования"
        assert len(input_member) != len(member_after_redact), "Не добавился новый ресурс"

    @testit.workItemIds(11847)
    @testit.displayName("1.2.2 Содержание табов в карточке проекта.")
    @pytest.mark.regress
    @allure.title("id-11847 1.2.2 Содержание табов в карточке проекта.")
    def test_contents_of_tabs_in_the_project_card(self, project_with_assignment, login, driver):
        all_project_page = AllProjectPage(driver)
        time.sleep(0.5)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        time.sleep(2)
        project_card_page = ProjectCardPage(driver)
        project_card_page.check_description_tab()

        project_card_page.go_to_project_hierarchy_tab()
        project_card_page.check_project_hierarchy_tab()

        gantt_page = GanttPage(driver)
        gantt_page.go_to_gantt_tab()
        gantt_page.check_gantt_tab()

        project_card_page.go_to_team_tab()
        project_card_page.check_team_tab()

        project_card_page.go_to_resource_plan_tab()
        project_card_page.check_resource_plan_tab()


        time.sleep(3)
