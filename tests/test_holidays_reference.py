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

    @testit.workItemIds(10461)
    @testit.displayName("6.1.5.3. Отмена редактирования праздничного дня")
    @pytest.mark.regress
    @allure.title("id-10461 6.1.5.3. Отмена редактирования праздничного дня")
    def test_cancel_editing_a_holiday(self, create_holiday, login, driver):
        holidays_reference_page = HolidaysReferencePage(driver)
        holidays_reference_page.go_to_holidays_reference_page()
        time.sleep(1)
        holidays_reference_page.open_kebab_to_edit(create_holiday)
        before = holidays_reference_page.get_holiday_field_values()
        holidays_reference_page.change_holiday_field_values(
            'Новое имя',
            '20.01.2060',
            'Новое описание',
        )
        after_change = holidays_reference_page.get_holiday_field_values()
        holidays_reference_page.press_abort_button()
        holidays_reference_page.open_kebab_to_edit(create_holiday)
        after_abort = holidays_reference_page.get_holiday_field_values()
        assert before != after_change, "Данные в дровере не изменились"
        assert after_abort == before, "Данные сохранились после отмены сохранения"
