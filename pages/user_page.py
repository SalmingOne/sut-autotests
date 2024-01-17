import time

import allure
from selenium.webdriver import Keys

from locators.user_page_locators import UserPageLocators
from pages.base_page import BasePage


class UserPage(BasePage):
    locators = UserPageLocators()

    @allure.step("Проверяем есть ли пользователь в таблице")
    def check_user_is_not_in_table(self, last_name):
        time.sleep(1)
        self.elements_are_visible(self.locators.SEARCH_TAB_FIELDS)[1].send_keys(Keys.CONTROL + 'a')
        self.elements_are_visible(self.locators.SEARCH_TAB_FIELDS)[1].send_keys(Keys.BACK_SPACE)
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

    @allure.step("Проверка заголовка корточки пользователя")
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

    @allure.step("Проверка заголовка страницы Пользователи")
    def check_user_page_title(self):
        assert self.element_is_displayed(self.locators.USER_PAGE_TITLE)

    @allure.step("Проверка кнопки фильтрации")
    def check_filter_button(self):
        assert self.element_is_displayed(self.locators.FILTER_BUTTON)

    @allure.step("Проверка кнопок добавления пользователя")
    def check_add_user_buttons(self):
        assert self.element_is_displayed(self.locators.ADD_LOCAL_USER_BUTTON)
        assert self.element_is_displayed(self.locators.ADD_FREEIPA_USER_BUTTON)

    @allure.step("Проверка заголовков столбцов")
    def check_columns_headers(self):
        time.sleep(1)
        columns_headers = self.elements_are_visible(self.locators.COLUMNS_HEADERS)
        headers_text = []
        for element in columns_headers:
            headers_text.append(element.text)
        assert headers_text == ['Пользователь', 'Действия', 'Системная роль',
                                'Статус'], "В таблице недостаточно столбцов или есть лишние"

    @allure.step("Проверка наличия полей поиска")
    def check_search_fields(self):
        assert len(self.elements_are_visible(self.locators.SEARCH_TAB_FIELDS)) == 3, "В таблице недостаточно полей поиска или есть лишние"

    @allure.step("Проверка наличия кнопок фильтрации")
    def check_filter_tab_buttons(self):
        assert len(self.elements_are_visible(self.locators.TAB_FILTER_BUTTONS)) == 3, "В таблице недостаточно кнопок фильтрации или есть лишние"

    @allure.step("Берем заголовки элементов кебаб меню")
    def get_kebab_menu_item(self):
        self.element_is_visible(self.locators.USER_KEBABS).click()
        menu_item = self.elements_are_visible(self.locators.KEBAB_MENU_ITEM)
        items_text = []
        for element in menu_item:
            items_text.append(element.text)
        self.action_esc()
        return items_text
