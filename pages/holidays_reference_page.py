import allure
import testit
from selenium.webdriver import Keys

from locators.holidays_reference_page_locators import HolidaysReferencePageLocators
from pages.base_page import BasePage


class HolidaysReferencePage(BasePage):
    locators = HolidaysReferencePageLocators()

    @testit.step("Переход на справочник праздничные дни")
    @allure.step("Переход на справочник праздничные дни")
    def go_to_holidays_reference_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.REFERENCE_BOOKS).click()
        self.element_is_visible(self.locators.HOLIDAYS_TAB).click()

    @testit.step("Открываем кебаб меню для редактирования")
    @allure.step("Открываем кебаб меню для редактирования")
    def open_kebab_to_edit(self, name):
        self.element_is_visible(self.locators.kebab_by_holiday_name(name)).click()
        self.element_is_visible(self.locators.KEBAB_EDIT_BUTTON).click()

    @testit.step("Создание праздничного дня")
    @allure.step("Создание праздничного дня")
    def create_holiday(self, name, date):
        self.element_is_visible(self.locators.ADD_HOLIDAY_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.DATE_FIELD).send_keys(date)
        self.element_is_visible(self.locators.TYPE_DROPDOWN).click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[0].click()
        self.element_is_visible(self.locators.PRIORITY_DROPDOWN).click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[0].click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Редактирование праздничного дня, если обязательное поле не заполнено")
    @allure.step("Редактирование праздничного дня, если обязательное поле не заполнено")
    def check_edit_with_empty_fields(self):
        self.element_is_visible(self.locators.PRIORITY_DROPDOWN).click()
        self.element_is_visible(self.locators.CLEAR_PRIORITY_DROPDOWN_BUTTON).click()
        self.element_is_visible(self.locators.TYPE_DROPDOWN).click()
        self.element_is_visible(self.locators.CLEAR_TYPE_DROPDOWN_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.DATE_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.DATE_FIELD).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.DESCRIPTION_FIELD).click()
        assert self.element_is_displayed(self.locators.GOAL_REASON_FIELD_IS_REQUIRED), 'Отсутствует сообщение "Поле обязательно"'
        self.element_is_visible(self.locators.CANCEL_BUTTON).click()

    @testit.step("Удаление праздничного дня")
    @allure.step("Удаление праздничного дня")
    def delete_holiday(self, name):
        self.element_is_visible(self.locators.kebab_by_holiday_name(name)).click()
        self.element_is_visible(self.locators.KEBAB_DELETE_BUTTON).click()
        self.element_is_visible(self.locators.MODAL_SUBMIT_BUTTON).click()

    @testit.step("Получение значений полей в дровере изменения праздничного дня")
    @allure.step("Получение значений полей в дровере изменения праздничного дня")
    def get_holiday_field_values(self):
        name = self.element_is_visible(self.locators.NAME_FIELD).get_attribute('value')
        date = self.element_is_visible(self.locators.DATE_FIELD).get_attribute('value')
        type = self.element_is_visible(self.locators.TYPE_VALUE).get_attribute('value')
        priority = self.element_is_visible(self.locators.PRIORITY_VALUE).get_attribute('value')
        description = self.element_is_visible(self.locators.DESCRIPTION_FIELD).text
        return name, date, type, priority, description

    @testit.step("Изменение полей в дровере изменения праздничного дня")
    @allure.step("Изменение полей в дровере изменения праздничного дня")
    def change_holiday_field_values(self, name, date, description):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.DATE_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.DATE_FIELD).send_keys(date)
        self.element_is_visible(self.locators.DESCRIPTION_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.DESCRIPTION_FIELD).send_keys(description)

    @testit.step("Нажатие кнопки отмены")
    @allure.step("Нажатие кнопки отмены")
    def press_abort_button(self):
        self.element_is_visible(self.locators.CANCEL_BUTTON).click()
