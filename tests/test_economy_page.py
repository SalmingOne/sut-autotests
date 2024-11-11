import time

import allure
import pytest
import testit

from pages.all_project_page import AllProjectPage
from pages.economy_page import EconomyPage
from pages.project_card_page import ProjectCardPage


class TestEconomyPage:

    @testit.workItemIds(3606)
    @testit.displayName("16.3.1.7. Удаление ставки привлечения")
    @pytest.mark.regress
    @allure.title("id-3606 16.3.1.7. Удаление ставки привлечения")
    def test_delete_attraction_rate(self, attraction_rate_to_delete, project_with_assignment, login, driver):
        economy_page = EconomyPage(driver)
        economy_page.go_to_economy_page()
        all_project_page = AllProjectPage(driver)
        project_card_page = ProjectCardPage(driver)
        economy_page.open_kebab_menu(attraction_rate_to_delete[0], 'Удалить')
        economy_page.check_modal_window(attraction_rate_to_delete[0])
        economy_page.apply_deleting()
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_assignment[0]['name'])
        project_card_page.go_to_team_tab()
        project_card_page.go_to_redact_team()
        assert attraction_rate_to_delete[0] not in project_card_page.get_attraction_rates_by_user(attraction_rate_to_delete[1]), 'Ставка привлечения отображается в выпадающем списке'