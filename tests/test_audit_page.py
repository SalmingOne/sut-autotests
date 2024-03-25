import time

import allure
import pytest
import testit

from pages.audit_page import AuditPage


@allure.suite("Страница все проекты")
class TestAuditPage:
    @testit.workItemIds(1200)
    @testit.displayName("6.4.1 Содержание страницы Аудит")
    @pytest.mark.smoke
    @allure.title("id-1200 6.4.1 Содержание страницы Аудит")
    def test_view_audit_page(self, login, driver):
        audit_page = AuditPage(driver)
        audit_page.go_to_audit_page()
        audit_page.check_columns_headers()
        audit_page.check_reset_all_button()