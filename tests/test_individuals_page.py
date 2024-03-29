import time

import allure
import pytest
import testit

from pages.individuals_page import IndividualsPage


@allure.suite("Справочник Физические лица")
class TestIndividualsPage:
    @testit.workItemIds(11908)
    @testit.displayName("9.1.2. Заполнение справочника/отмена заполнения ")
    @pytest.mark.smoke
    @allure.title("id-11908 9.1.2. Заполнение справочника/отмена заполнения ")
    def test_completing_the_directory_and_cancelling_filling(self, login, driver):
        individuals_page = IndividualsPage(driver)
        individuals_page.go_to_individuals_page()
        time.sleep(1)
        individuals_page.open_add_drawer()
        individuals_page.check_max_lait()
        individuals_page.check_email()
        individuals_page.check_date_pikers()
        individuals_page.check_clickable_submit_button()
        individuals_page.check_role_dropdown()
        individuals_page.check_document_type_dropdown()
        individuals_page.check_bic_bank()
        individuals_page.press_abort_button()
        individuals_page.create_individual('Автор',
                                           'Романов',
                                           '123456789',
                                           '9876543',
                                           'abs@abs.abs')
        individuals_page.check_individual_on_tab('Романов Автор')
        individuals_page.delete_individual()
