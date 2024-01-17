import time

import allure
from locators.user_page_locators import UserPageLocators
from pages.base_page import BasePage


class UserPage(BasePage):
    locators = UserPageLocators()

    @allure.step("Проверяем есть ли пользователь в таблице")
    def check_user_is_not_in_table(self, last_name):
        time.sleep(1)
        self.elements_are_visible(self.locators.SEARCH_TAB_FIELDS)[1].send_keys(f'{last_name}')
        return self.element_is_displayed(self.locators.USER_KEBABS)

    @allure.step("Переход на страницу Пользователи")
    def go_to_user_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_ROLE).click()

    @allure.step("Переход на карточку пользователя")
    def go_to_user_card(self):
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.USER_FULL_INFO_BUTTON).click()

    @allure.step("Получаем заголовки")
    def get_labels_on_user_card(self):
        all_label_elements = self.elements_are_visible(self.locators.USER_CARD_LABEL)
        labels = []
        for i in all_label_elements:
            labels.append(i.text)
        return labels

    @allure.step("Переход на вкладку проекты")
    def go_to_tab_projects(self):
        self.element_is_visible(self.locators.TAB_PROJECTS).click()

    @allure.step("Переход на вкладку контакты")
    def go_to_tab_contacts(self):
        self.element_is_visible(self.locators.TAB_CONTACTS).click()

    @allure.step("Проверка иконки очистки")
    def check_clear_button(self):
        assert self.element_is_displayed(self.locators.CLEAR_BUTTON)

    @allure.step("Проверка заголовка")
    def check_user_card_title(self):
        assert self.element_is_displayed(self.locators.USER_CARD_TITLE)

    @allure.step("Получаем статус пользователя")
    def get_user_status(self):
        return self.element_is_visible(self.locators.USER_STATUS).text

    @allure.step("Уволить пользователя")
    def fired_user(self):
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.FIRED_BUTTON).click()
        self.element_is_visible(self.locators.CALENDAR_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_PICKER).click()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация

    @allure.step("Восстановить пользователя")
    def restore_user(self):
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.RESTORE_BUTTON).click()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация

