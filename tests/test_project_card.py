import time

import allure

from pages.project_card_page import ProjectCardPage


@allure.suite("Карточка проекта")
class TestProjectCard:

    # id-3185 1.3.1 Сохранение изменений на вкладке "Команда"
    @allure.title("id-3185 1.3.1 Сохранение изменений на вкладке Команда")
    def test_save_changes_to_the_team_tab(self, project, login, driver):
        project_card_page = ProjectCardPage(driver)
        time.sleep(1)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        input_member = project_card_page.get_first_team_member()
        project_card_page.go_to_redact_team()
        member_before_redact = project_card_page.get_first_team_member_on_redact()
        project_card_page.change_first_team_member()
        time.sleep(1)  # Без этого ожидания иногда не успевает прогрузиться проектная роль
        member_after_redact = project_card_page.get_first_team_member()
        assert input_member == member_before_redact, "Роль, ресурс и ставка изменились при нажатии кнопки редактирования"
        assert input_member != member_after_redact, "Роль, ресурс или ставка не изменились после редактирования"
