import time

import allure
import testit
from selenium.webdriver import Keys

from locators.logging_page_locators import LoggingPageLocators
from pages.base_page import BasePage


class LoggingPage(BasePage):
    locators = LoggingPageLocators()

    @testit.step("Переход на страницу логирования")
    @allure.step("Переход на страницу логирования")
    def go_to_audit_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_AUDIT_TAB).click()

    @testit.step("Изменение настроек логирования")
    @allure.step("Изменение настроек логирования")
    def change_audit_setting(self, status=None, level=None, depth=None):
        time.sleep(0.5)  # Без ожидания не успевает прогрузиться страница
        self.element_is_visible(self.locators.AUDIT_STATUS_FIELD).click()
        self.element_is_visible(self.locators.set_choice(status)).click()
        self.element_is_visible(self.locators.AUDIT_LEVEL_FIELD).click()
        self.element_is_visible(self.locators.set_choice(level)).click()
        self.element_is_visible(self.locators.DEPTH_DATE_QUANTITY_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.DEPTH_DATE_QUANTITY_FIELD).send_keys('1')
        self.element_is_visible(self.locators.DEPTH_DATE_TYPE_FIELD).click()
        self.element_is_visible(self.locators.set_choice(depth)).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Получение текста модального окна")
    @allure.step("Получение текста модального окна")
    def get_modal_window(self):
        return self.element_is_visible(self.locators.DIALOG_TEXT).text

    @testit.step("Проверка кнопки отмены модального окна")
    @allure.step("Проверка кнопки отмены модального окна")
    def check_modal_abort_button(self):
        assert self.element_is_displayed(self.locators.DIALOG_ABORT_BUTTON)

    @testit.step("Подтверждение изменений в модальном окне")
    @allure.step("Подтверждение изменений в модальном окне")
    def submit_modal_dialog(self):
        self.element_is_visible(self.locators.DIALOG_SUBMIT_BUTTON).click()

    @testit.step("Получение текста сообщения системы")
    @allure.step("Получение текста сообщения системы")
    def get_alert_text(self):
        return self.element_is_visible(self.locators.ALERT_TEXT).text

    @testit.step("Проверка наличия пункта меню Аудит")
    @allure.step("Проверка наличия пункта меню Аудит")
    def check_audit_menu_item(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        return self.element_is_displayed(self.locators.AUDIT_PAGE, 1)

    @testit.step("Выключение логирования")
    @allure.step("Выключение логирования")
    def disabling_logging(self):
        time.sleep(0.5)  # Без ожидания не успевает прогрузиться страница
        self.element_is_visible(self.locators.AUDIT_STATUS_FIELD).click()
        self.element_is_visible(self.locators.set_choice('Выкл')).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка элементов на табе 'Аудит'")
    @allure.step("Проверка элементов на табе 'Аудит'")
    def check_elements_on_page(self):
        assert self.element_is_displayed(self.locators.AUDIT_STATUS_FIELD), "Дропдаун аудит не отображается"
        assert self.element_is_displayed(self.locators.AUDIT_LEVEL_FIELD), "Дропдаун уровень аудита не отображается"
        assert self.element_is_displayed(self.locators.DEPTH_DATE_QUANTITY_FIELD), "Поле глубина аудита не отображается"
        assert self.element_is_displayed(self.locators.DEPTH_DATE_TYPE_FIELD), "Дропдаун глубина аудита не отображается"
        assert self.element_is_displayed(self.locators.SUBMIT_BUTTON), "Кнопка сохранить не отображается"
        assert self.element_is_displayed(self.locators.ABORT_BUTTON), "Кнопка отменить не отображается"

    @testit.step("Проверка значений в выпадающих списках")
    @allure.step("Проверка значений в выпадающих списках")
    def check_elements_in_select(self):
        self.element_is_visible(self.locators.AUDIT_STATUS_FIELD).click()
        audit_status_elements = [element.text for element in self.elements_are_visible(self.locators.ELEMENTS_IN_SELECT)]
        self.element_is_visible(self.locators.AUDIT_LEVEL_FIELD).click()
        audit_level_elements = [element.text for element in self.elements_are_visible(self.locators.ELEMENTS_IN_SELECT)]
        self.element_is_visible(self.locators.DEPTH_DATE_TYPE_FIELD).click()
        depth_date_elements = [element.text for element in self.elements_are_visible(self.locators.ELEMENTS_IN_SELECT)]
        assert audit_status_elements == ["Вкл", "Выкл"], "В выпадающем списке аудита не все значения"
        assert audit_level_elements == ["Все", "Информационные", "Ошибка", "Фатальные"], "В выпадающем списке уровень аудита не все значения"
        assert depth_date_elements == ["День", "Неделя", "Месяц", "Год"], "В выпадающем списке глубина аудита не все значения"

    @testit.step("Проверка активны ли кнопки")
    @allure.step("Проверка активны ли кнопки")
    def buttons_are_enabled(self):
        assert self.element_is_clickable(self.locators.SUBMIT_BUTTON), 'Кнопка сохранить неактивна'
        assert self.element_is_clickable(self.locators.ABORT_BUTTON), 'Кнопка отменить неактивна'

    @testit.step("Проверка неактивны ли кнопки")
    @allure.step("Проверка неактивны ли кнопки")
    def buttons_are_disabled(self):
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON), 'Кнопка сохранить активна'
        assert not self.element_is_clickable(self.locators.ABORT_BUTTON), 'Кнопка отменить активна'

    @testit.step("Проверка активны ли поля")
    @allure.step("Проверка активны ли поля")
    def fields_are_enabled(self):
        assert self.element_is_visible(self.locators.AUDIT_LEVEL_FIELD), 'Поле уровень аудита неактивно'
        assert self.element_is_visible(self.locators.DEPTH_DATE_QUANTITY_FIELD), 'Поле количество неактивно'
        assert self.element_is_visible(self.locators.DEPTH_DATE_TYPE_FIELD), 'Поле глубина аудита неактивно'

    @testit.step("Изменение статуса аудита")
    @allure.step("Изменение статуса аудита")
    def change_audit_status(self, status):
        self.element_is_visible(self.locators.AUDIT_STATUS_FIELD).click()
        self.element_is_visible(self.locators.set_choice(status)).click()

    @testit.step("Отмена изменений в модальном окне")
    @allure.step("Отмена изменений в модальном окне")
    def abort_modal_dialog(self):
        self.element_is_present(self.locators.DIALOG_ABORT_BUTTON).click()

    @testit.step("Получение значений полей")
    @allure.step("Получение значений полей")
    def get_field_values(self):
        audit_status_field_value = self.element_is_visible(self.locators.AUDIT_STATUS_FIELD).get_attribute('value')
        audit_level_field_value =  self.element_is_visible(self.locators.AUDIT_LEVEL_FIELD).get_attribute('value')
        audit_depth_field_value = self.element_is_visible(self.locators.DEPTH_DATE_TYPE_FIELD).get_attribute('value')
        audit_depth_quantity_value = self.element_is_visible(self.locators.DEPTH_DATE_QUANTITY_FIELD).get_attribute('value').lstrip('0')
        return audit_status_field_value, audit_level_field_value, audit_depth_quantity_value, audit_depth_field_value

    @testit.step("Изменение настроек логирования с отменой")
    @allure.step("Изменение настроек логирования с отменой")
    def discard_audit_setting_changes(self, status=None, level=None, depth=None):
        self.element_is_visible(self.locators.AUDIT_STATUS_FIELD).click()
        self.element_is_visible(self.locators.set_choice(status)).click()
        self.element_is_visible(self.locators.AUDIT_LEVEL_FIELD).click()
        self.element_is_visible(self.locators.set_choice(level)).click()
        self.element_is_visible(self.locators.DEPTH_DATE_QUANTITY_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.DEPTH_DATE_QUANTITY_FIELD).send_keys('1')
        self.element_is_visible(self.locators.DEPTH_DATE_TYPE_FIELD).click()
        self.element_is_visible(self.locators.set_choice(depth)).click()
        self.element_is_visible(self.locators.ABORT_BUTTON).click()
