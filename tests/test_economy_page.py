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
    def test_delete_attraction_rate(self, project_with_tester_assignment, attraction_rate_by_user_to_delete, attraction_rate_by_slot_to_delete, attraction_rate_by_affiliate_to_delete, login, driver):
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
            economy_page.check_modal_window_delete(attraction_rate)
            economy_page.apply_deleting()
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_tester_assignment[0]['name'])
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

    @testit.workItemIds(3608)
    @testit.displayName("16.3.1.7. Отмена удаления ставки привлечения, если она НЕ используется на проектах")
    @pytest.mark.regress
    @allure.title("id-3608 16.3.1.7. Отмена удаления ставки привлечения, если она НЕ используется на проектах")
    def test_cancel_attraction_rate_delete(self, attraction_rate_by_user_to_delete, login, driver):
        economy_page = EconomyPage(driver)
        economy_page.go_to_economy_page()
        time.sleep(3)
        economy_page.open_kebab_menu(attraction_rate_by_user_to_delete[0], 'Удалить')
        economy_page.check_modal_window_delete(attraction_rate_by_user_to_delete[0])
        economy_page.cancel_deleting()
        assert attraction_rate_by_user_to_delete[0] in economy_page.get_all_attraction_rates(), 'Ставка привлечения удалена'

    @testit.workItemIds(10119)
    @testit.displayName('16.3.1.3. Фильтрация таблицы "Ставки привлечения" через "Отображение"')
    @pytest.mark.regress
    @allure.title('id-10119 16.3.1.3. Фильтрация таблицы "Ставки привлечения" через "Отображение"')
    def test_filter_attraction_rates(self, attraction_rate_by_user_to_delete, attraction_rate_by_slot_to_delete, attraction_rate_by_affiliate_to_delete, login, driver):
        economy_page = EconomyPage(driver)
        economy_page.go_to_economy_page()
        time.sleep(3)
        economy_page.click_checkbox_in_filter_attraction_rates()
        economy_page.click_checkbox_in_filter_attraction_rates(economy_page.AttractionType.ByUser)
        assert {'По человеку'} == economy_page.get_all_attraction_rates_types(), 'Неправильная работа фильтра'
        economy_page.click_checkbox_in_filter_attraction_rates(economy_page.AttractionType.ByFilial)
        assert {'По человеку', 'По филиалу'} == economy_page.get_all_attraction_rates_types(), 'Неправильная работа фильтра'
        economy_page.click_checkbox_in_filter_attraction_rates(economy_page.AttractionType.BySlot)
        assert {'По человеку', 'По филиалу', 'По слоту'} == economy_page.get_all_attraction_rates_types(), 'Неправильная работа фильтра'

    @testit.workItemIds(3579)
    @testit.displayName('16.3.1.5.1. Создание новой ставки привлечения с типом слота "Филиал" без использования компонентов')
    @pytest.mark.regress
    @allure.title('id-3579 16.3.1.5.1. Создание новой ставки привлечения с типом слота "Филиал" без использования компонентов')
    def test_create_attraction_rate_type_filial(self, project_with_assignment, create_filial_with_added_user, login, driver,
                                              delete_filial_and_attraction_rate):
        try:
            economy_page = EconomyPage(driver)
            all_project_page = AllProjectPage(driver)
            project_card_page = ProjectCardPage(driver)
            filial_page = FilialPage(driver)
            economy_page.go_to_economy_page()
            time.sleep(5)
            economy_page.open_create_drawer()
            economy_page.fill_fields_in_drawer('Ставка', create_filial_with_added_user[0]['name'], economy_page.AttractionType.ByFilial, 100)
            economy_page.save_changes()
            economy_page.check_attraction_rate_row('Ставка', 'По филиалу', 100)
            economy_page.open_kebab_menu('Ставка', 'История ставки')
            economy_page.check_dates(economy_page.get_day_before(0), economy_page.get_day_before(0))
            economy_page.action_esc()
            all_project_page.go_to_all_project_page()
            all_project_page.go_project_page(project_with_assignment[0]['name'])
            project_card_page.go_to_team_tab()
            project_card_page.go_to_redact_team()
            assert 'Ставка' in project_card_page.get_attraction_rates_by_user(create_filial_with_added_user[1]) , 'Ставка привлечения не отображается в выпадающем списке таба Команда'
            project_card_page.press_abort_button()
            filial_page.go_to_filial_page()
            filial_page.open_redact_filial(create_filial_with_added_user[0]['name'])
            assert 'Ставка' in filial_page.get_attraction_rates_by_filial(), 'Ставка привлечения не отображается в выпадающем списке таба Филиалы'
            delete_filial_and_attraction_rate('Ставка', create_filial_with_added_user[0]['name'])
        except:
            delete_filial_and_attraction_rate('Ставка', create_filial_with_added_user[0]['name'])
            raise

    @testit.workItemIds(3580)
    @testit.displayName('16.3.1.5.1. Создание ставки привлечения с типом ставки  "Человек" без использования компонентов')
    @pytest.mark.regress
    @allure.title('id-3580 16.3.1.5.1. Создание ставки привлечения с типом ставки  "Человек" без использования компонентов')
    def test_create_attraction_rate_type_user(self, project_with_assignment, login, driver, delete_attraction_rate):
        try:
            economy_page = EconomyPage(driver)
            all_project_page = AllProjectPage(driver)
            project_card_page = ProjectCardPage(driver)
            economy_page.go_to_economy_page()
            time.sleep(5)
            economy_page.open_create_drawer()
            economy_page.fill_fields_in_drawer('Ставка', project_with_assignment[2] , economy_page.AttractionType.ByUser, 100)
            economy_page.save_changes()
            economy_page.check_attraction_rate_row('Ставка', 'По человеку', 100)
            economy_page.open_kebab_menu('Ставка', 'История ставки')
            economy_page.check_dates(economy_page.get_day_before(0), economy_page.get_day_before(0))
            economy_page.action_esc()
            all_project_page.go_to_all_project_page()
            all_project_page.go_project_page(project_with_assignment[0]['name'])
            project_card_page.go_to_team_tab()
            project_card_page.go_to_redact_team()
            assert 'Ставка' in project_card_page.get_attraction_rates_by_user(project_with_assignment[2]) , 'Ставка привлечения не отображается в выпадающем списке таба Команда'
            delete_attraction_rate('Ставка')
        except:
            delete_attraction_rate('Ставка')
            raise

    @testit.workItemIds(3610)
    @testit.displayName(
        '16.3.1.5.1. Создание ставки привлечения с типом ставки  "Слот" без использования компонентов')
    @pytest.mark.regress
    @allure.title(
        'id-3610 16.3.1.5.1. Создание ставки привлечения с типом ставки  "Слот" без использования компонентов')
    def test_create_attraction_rate_type_slot(self, project_with_tester_assignment, login, driver, delete_attraction_rate):
        try:
            economy_page = EconomyPage(driver)
            all_project_page = AllProjectPage(driver)
            project_card_page = ProjectCardPage(driver)
            economy_page.go_to_economy_page()
            time.sleep(5)
            economy_page.open_create_drawer()
            economy_page.fill_fields_in_drawer('Ставка', 'Тестировщик', economy_page.AttractionType.BySlot,
                                               100)
            economy_page.save_changes()
            economy_page.check_attraction_rate_row('Ставка', 'По слоту', 100)
            economy_page.open_kebab_menu('Ставка', 'История ставки')
            economy_page.check_dates(economy_page.get_day_before(0), economy_page.get_day_before(0))
            economy_page.action_esc()
            all_project_page.go_to_all_project_page()
            all_project_page.go_project_page(project_with_tester_assignment[0]['name'])
            project_card_page.go_to_team_tab()
            project_card_page.go_to_redact_team()
            assert 'Ставка' in project_card_page.get_attraction_rates_by_user(
                project_with_tester_assignment[2]), 'Ставка привлечения не отображается в выпадающем списке таба Команда'
            delete_attraction_rate('Ставка')
        except:
            delete_attraction_rate('Ставка')
            raise

    @testit.workItemIds(3639)
    @testit.displayName('16.3.1.5.1. Отмена создания ставки привлечения в конструкторе')
    @pytest.mark.regress
    @allure.title('id-3639 16.3.1.5.1. Отмена создания ставки привлечения в конструкторе')
    def test_cancel_create_attraction_rate(self, login, driver, ):
        economy_page = EconomyPage(driver)
        economy_page.go_to_economy_page()
        time.sleep(5)
        economy_page.open_create_drawer()
        economy_page.fill_fields_in_drawer('Ставка', 'Тестировщик', economy_page.AttractionType.BySlot,
                                           100)
        economy_page.discard_changes()

    @testit.workItemIds(4307)
    @testit.displayName('16.3.1.8. Просмотр истории изменения для новой ставки из таблицы')
    @pytest.mark.regress
    @allure.title('id-4307 16.3.1.8. Просмотр истории изменения для новой ставки из таблицы')
    def test_view_change_history_for_new_attraction_rate(self, attraction_rate_by_user_to_delete, login, driver, ):
        economy_page = EconomyPage(driver)
        economy_page.go_to_economy_page()
        time.sleep(5)
        economy_page.open_kebab_menu(attraction_rate_by_user_to_delete[0], 'История ставки')
        today = economy_page.get_day_before(0)
        economy_page.check_changes_window(today, today,'', 100, "действует")

