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
    def test_go_to_user_from_search(self, login, driver):
        header_search_page = HeaderSearchPage(driver)
        header_search_page.select_search_field_header()
        header_search_page.check_tooltip_in_header_search()

