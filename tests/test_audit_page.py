import time

import allure
import pytest
import testit

from pages.audit_page import AuditPage


@allure.suite("Страница аудит")
class TestAuditPage:
    @testit.workItemIds(1200)
    @testit.displayName("6.4.1 Содержание страницы Аудит")
    @pytest.mark.smoke
    @allure.title("id-1200 6.4.1 Содержание страницы Аудит")
    def test_view_audit_page(self, login, logging_on, driver):
        audit_page = AuditPage(driver)
        audit_page.go_to_audit_page()
        time.sleep(1)
        audit_page.check_columns_headers()
        audit_page.check_reset_all_button()

    @testit.workItemIds(1211)
    @testit.displayName('6.4.2 Реакция системы на ввод конечной даты раньше начальной при фильтрации по полю "Дата"')
    @pytest.mark.regress
    @allure.title('id-1211 6.4.2 Реакция системы на ввод конечной даты раньше начальной при фильтрации по полю "Дата"')
    def test_end_date_before_start_date_raises_validation_error(self,logging_on, login, driver):
        audit_page = AuditPage(driver)
        audit_page.go_to_audit_page()
        assert not audit_page.select_day_interval_in_datepicker(10,9), 'Есть возможность выбора конченой даты раньше начальной'
        assert (audit_page.input_date_manually('09.10.2024','08.10.2024')), 'Есть возможность ввода конченой даты раньше начальной'
