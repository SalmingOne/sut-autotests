import time

import allure
import pytest
import testit

from data.data import PROJECT_NAME
from pages.all_project_page import AllProjectPage
from pages.project_card_page import ProjectCardPage


@allure.suite("Карточка проекта")
class TestProjectCard:

    @testit.workItemIds(3185)
    @testit.displayName("1.3.1 Сохранение изменений на вкладке Команда")
    @pytest.mark.smoke
    @allure.title("id-3185 1.3.1 Сохранение изменений на вкладке Команда")
    def test_save_changes_to_the_team_tab(self, simple_project, login, driver):
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(f"{PROJECT_NAME}")
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_team_tab()
        time.sleep(1)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        input_member = project_card_page.get_first_team_member()
        project_card_page.go_to_redact_team()
        member_before_redact = project_card_page.get_first_team_member_on_redact()
        project_card_page.change_first_team_member()
        time.sleep(1)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        member_after_redact = project_card_page.get_first_team_member()
        assert input_member == member_before_redact, "Роль, ресурс и ставка изменились при нажатии кнопки редактирования"
        assert input_member != member_after_redact, "Роль, ресурс или ставка не изменились после редактирования"
