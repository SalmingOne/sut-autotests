import time

import allure
import pytest
import testit

from pages.header_search_page import HeaderSearchPage


@allure.suite("Поиск в хедере")
class TestHeaderSearchPage:
    @testit.workItemIds(3696)
    @testit.displayName("10.12.1. Отображение тултипа при незаполненной строке поиска")
    @pytest.mark.regress
    @allure.title("id-3696 10.12.1. Отображение тултипа при незаполненной строке поиска")
    def test_displaying_tooltip_in_header_search(self, login, driver):
        header_search_page = HeaderSearchPage(driver)
        header_search_page.select_search_field_header()
        header_search_page.check_tooltip_in_header_search()

    @testit.workItemIds(3669)
    @testit.displayName("10.12.1. Данные по запросу через строку поиска отсутствуют")
    @pytest.mark.regress
    @allure.title("id-3669 10.12.1. Данные по запросу через строку поиска отсутствуют")
    def test_displaying_no_data_in_the_header_search(self, login, driver):
        header_search_page = HeaderSearchPage(driver)
        header_search_page.select_search_field_header()
        header_search_page.check_nothing_found_text()

    @testit.workItemIds(4286)
    @testit.displayName("10.12.1. Ввод пробела в строку поиска")
    @pytest.mark.regress
    @allure.title("id-4286 10.12.1. Ввод пробела в строку поиска")
    def test_entering_a_space_in_the_header_search(self, login, driver):
        header_search_page = HeaderSearchPage(driver)
        header_search_page.select_search_field_header()
        header_search_page.entering_a_space_in_the_header_search()
        header_search_page.check_tooltip_in_header_search()

    @testit.workItemIds(3664)
    @testit.displayName("10.12.1. Перейти на страницу пользователя из результатов поиска")
    @pytest.mark.regress
    @allure.title("id-3664 10.12.1. Перейти на страницу пользователя из результатов поиска")
    def test_go_to_user_from_header_search(self, login, driver):
        header_search_page = HeaderSearchPage(driver)
        header_search_page.select_search_field_header()
        header_search_page.entering_2_letters_in_header_search()
        header_search_page.check_dropdown_not_visible()
        header_search_page.entering_3th_letter_in_header_search()
        time.sleep(2)           #прогружается список
        header_search_page.check_projects_in_dropdown_2_or_less()
        header_search_page.check_users_in_dropdown_2_or_less()
        header_search_page.go_to_quick_search_page()
        header_search_page.quick_search_page()
        header_search_page.check_users_in_alphabetical_order()
        header_search_page.check_projects_in_chronological_order()
        header_search_page.go_to_user_page_from_quick_search()
        time.sleep(3)           #прогружается страница
        driver.switch_to.window(driver.window_handles[1])
        header_search_page.check_page_after_redirect()


