import time

import allure
import pytest
import testit

from pages.all_project_page import AllProjectPage
from pages.economy_page import EconomyPage
from pages.filial_page import FilialPage
from pages.project_card_page import ProjectCardPage
from pages.project_roles_page import ProjectRolesPage


class TestEconomyPage:

    @testit.workItemIds(3606)
    @testit.displayName("16.3.1.7. Удаление ставки привлечения")
    @pytest.mark.regress
    @allure.title("id-3606 16.3.1.7. Удаление ставки привлечения")
    def test_delete_attraction_rate(self, project_with_assignment, attraction_rate_by_user_to_delete, attraction_rate_by_slot_to_delete, attraction_rate_by_affiliate_to_delete, login, driver):
        economy_page = EconomyPage(driver)
        all_project_page = AllProjectPage(driver)
        project_card_page = ProjectCardPage(driver)
        project_roles_page = ProjectRolesPage(driver)
        filial_page = FilialPage(driver)
        economy_page.go_to_economy_page()
        attraction_rates_to_delete = [
            attraction_rate_by_user_to_delete[0],
            attraction_rate_by_slot_to_delete,
            attraction_rate_by_affiliate_to_delete[0]
        ]
        for attraction_rate in attraction_rates_to_delete:
            time.sleep(3)
            economy_page.open_kebab_menu(attraction_rate, 'Удалить')
            economy_page.check_modal_window(attraction_rate)
            economy_page.apply_deleting()
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_assignment[0]['name'])
        project_card_page.go_to_team_tab()
        project_card_page.go_to_redact_team()
        assert (attraction_rate not in project_card_page.get_attraction_rates_by_user(attraction_rate_by_user_to_delete[1]) for
                attraction_rate in attraction_rates_to_delete), 'Ставка привлечения отображается в выпадающем списке таба Команда'
        project_card_page.press_abort_button()
        project_roles_page.go_to_project_roles_page()
        project_roles_page.redact_project_role_by_name('Тестировщик')
        project_roles_page.get_attraction_rates_by_role()
        assert (
            attraction_rate not in project_roles_page.get_attraction_rates_by_role() for
            attraction_rate in attraction_rates_to_delete), 'Ставка привлечения отображается в выпадающем списке таба Проектные роли'
        project_card_page.action_esc()
        project_card_page.action_esc()
        filial_page.go_to_filial_page()
        filial_page.open_redact_filial(attraction_rate_by_affiliate_to_delete[1])
        assert (
            attraction_rate not in filial_page.get_attraction_rates_by_filial() for
            attraction_rate in attraction_rates_to_delete), 'Ставка привлечения отображается в выпадающем списке таба Филиалы'

    @testit.workItemIds(3607)
    @testit.displayName("16.3.1.7. Удаление ставки привлечения, если она используется хотя бы на одном проекте")
    @pytest.mark.regress
    @allure.title("id-3607 16.3.1.7. Удаление ставки привлечения, если она используется хотя бы на одном проекте")
    def test_delete_attraction_rate_with_project(self, attraction_rate_with_project, login, driver):
        economy_page = EconomyPage(driver)
        economy_page.go_to_economy_page()
        time.sleep(3)
        economy_page.open_kebab_menu(attraction_rate_with_project, 'Удалить')
        economy_page.apply_deleting()
        assert 'Вы не можете удалить эту ставку, так как она используется в расчете!' in economy_page.get_alert_message(), 'Нет предупреждения о невозможности удаления ставки привлечения'

