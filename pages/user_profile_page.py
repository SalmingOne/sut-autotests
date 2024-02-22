import time

import allure
import testit

from locators.user_profile_page_locators import UserProfilePageLocators
from pages.base_page import BasePage


class UserProfilePage(BasePage):
    locators = UserProfilePageLocators()

    @testit.step("Переходим в профиль пользователя")
    @allure.step("Переходим в профиль пользователя")
    def go_to_user_profile(self):
        self.element_is_visible(self.locators.PROFILE_BUTTON).click()
        self.element_is_visible(self.locators.MY_PROFILE_MENU_ITEM).click()

    @testit.step("Переходим на вкладку образование")
    @allure.step("Переходим на вкладку образование")
    def go_to_education_tab(self):
        self.element_is_visible(self.locators.EDUCATION_TAB_BUTTON).click()

    @testit.step("Переходим на вкладку Сертификаты")
    @allure.step("Переходим на вкладку Сертификаты")
    def go_to_certificate_tab(self):
        self.element_is_visible(self.locators.CERTIFICATE_TAB_BUTTON).click()

    @testit.step("Переходим на вкладку Опыт работы")
    @allure.step("Переходим на вкладку Опыт работы")
    def go_to_experience_tab(self):
        self.element_is_visible(self.locators.EXPERIENCES_TAB_BUTTON).click()

    @testit.step("Нажимаем кнопку редактировать")
    @allure.step("Нажимаем кнопку редактировать")
    def press_redact_button(self):
        time.sleep(1)  # Без этого ожидания не всегда нажимается кнопка
        self.element_is_visible(self.locators.REDACT_BUTTON).click()

    @testit.step("Нажимаем иконку добавления нового диплома")
    @allure.step("Нажимаем иконку добавления нового диплома")
    def press_add_icon_button(self):
        self.action_move_to_element(self.element_is_visible(self.locators.ADD_ICON))
        self.element_is_visible(self.locators.ADD_ICON).click()

    @testit.step("Нажимаем кнопку сохранения")
    @allure.step("Нажимаем кнопку сохранения")
    def press_save_button(self):
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

    @testit.step("Берем текст сообщения системы")
    @allure.step("Берем текст сообщения системы")
    def get_alert_message(self):
        return self.element_is_visible(self.locators.ALERT_TEXT).text

    @testit.step("Берем цвет вкладки Образование")
    @allure.step("Берем цвет вкладки Образование")
    def get_education_tab_color(self):
        return self.element_is_visible(self.locators.EDUCATION_TAB_BUTTON).value_of_css_property('background-color')

    @testit.step("Берем цвет вкладки Сертификаты")
    @allure.step("Берем цвет вкладки Сертификаты")
    def get_certificate_tab_color(self):
        return self.element_is_visible(self.locators.CERTIFICATE_TAB_BUTTON).value_of_css_property('background-color')

    @testit.step("Берем цвет вкладки Опыт работы")
    @allure.step("Берем цвет вкладки Опыт работы")
    def get_experience_tab_color(self):
        return self.element_is_visible(self.locators.EXPERIENCES_TAB_BUTTON).value_of_css_property('background-color')

    @testit.step("Берем текст ошибок с незаполненных обязательных полей")
    @allure.step("Берем текст ошибок с незаполненных обязательных полей")
    def get_mui_errors_text(self):
        error_messages = self.elements_are_visible(self.locators.MUI_ERROR)
        data = []
        for message in error_messages:
            data.append(message.text)
        return data
