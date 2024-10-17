import time

import allure
import pytest
import testit

from pages.holidays_reference_page import HolidaysReferencePage


@allure.suite("Справочник праздничных дней")
class TestHolidaysReferencePage:
    @testit.workItemIds(10459)
    @testit.displayName("6.1.5.3. Редактирование праздничного дня, если обязательное поле не заполнено")
    @pytest.mark.regress
    @allure.title("id-10459 6.1.5.3. Редактирование праздничного дня, если обязательное поле не заполнено")
    def test_edit_holiday_empty_required_field(self, create_holiday, login, driver):
        holidays_reference_page = HolidaysReferencePage(driver)
        holidays_reference_page.go_to_holidays_reference_page()
        time.sleep(1)
        holidays_reference_page.open_kebab_to_edit(create_holiday)
        holidays_reference_page.check_edit_with_empty_fields()
        time.sleep(1)

