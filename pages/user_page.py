import time

import allure
import testit
from selenium.webdriver import Keys

from locators.user_page_locators import UserPageLocators
from pages.base_page import BasePage


class UserPage(BasePage):
    locators = UserPageLocators()

    @testit.step("Проверяем есть ли пользователь в таблице")
    @allure.step("Проверяем есть ли пользователь в таблице")
    def check_user_is_not_in_table(self, last_name):
        time.sleep(1)
        self.elements_are_visible(self.locators.SEARCH_TAB_FIELDS)[1].send_keys(Keys.CONTROL + 'a')
        time.sleep(1)
        self.elements_are_visible(self.locators.SEARCH_TAB_FIELDS)[1].send_keys(Keys.BACK_SPACE)
        self.elements_are_visible(self.locators.SEARCH_TAB_FIELDS)[1].send_keys(f'{last_name}')
        return self.element_is_displayed(self.locators.USER_KEBABS)

    @testit.step("Переход на страницу Пользователи")
    @allure.step("Переход на страницу Пользователи")
    def go_to_user_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_ROLE).click()

    @testit.step("Переход на карточку пользователя")
    @allure.step("Переход на карточку пользователя")
    def go_to_user_card(self):
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.USER_FULL_INFO_BUTTON).click()

    @testit.step("Получаем заголовки карточки пользователя")
    @allure.step("Получаем заголовки карточки пользователя")
    def get_labels_on_user_card(self):
        all_label_elements = self.elements_are_visible(self.locators.USER_CARD_LABEL)
        labels = []
        for i in all_label_elements:
            labels.append(i.text)
        return labels

    @testit.step("Переход на вкладку проекты")
    @allure.step("Переход на вкладку проекты")
    def go_to_tab_projects(self):
        self.element_is_visible(self.locators.TAB_PROJECTS).click()

    @testit.step("Переход на вкладку контакты")
    @allure.step("Переход на вкладку контакты")
    def go_to_tab_contacts(self):
        self.element_is_visible(self.locators.TAB_CONTACTS).click()

    @testit.step("Проверка иконки очистки")
    @allure.step("Проверка иконки очистки")
    def check_clear_button(self):
        assert self.element_is_displayed(self.locators.CLEAR_BUTTON)

    @testit.step("Проверка заголовка корточки пользователя")
    @allure.step("Проверка заголовка корточки пользователя")
    def check_user_card_title(self):
        assert self.element_is_displayed(self.locators.USER_CARD_TITLE)

    @testit.step("Получаем статус пользователя")
    @allure.step("Получаем статус пользователя")
    def get_user_status(self):
        return self.element_is_visible(self.locators.USER_STATUS).text

    @testit.step("Уволить пользователя")
    @allure.step("Уволить пользователя")
    def fired_user(self):
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.FIRED_BUTTON).click()
        self.element_is_visible(self.locators.FIRED_ALERT_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.FIRED_ALERT_FIELD).send_keys(self.get_day_before(0))
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(2)  # Без ожидания не успевает срабатывать анимация

    @testit.step("Восстановить пользователя")
    @allure.step("Восстановить пользователя")
    def restore_user(self):
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.RESTORE_BUTTON).click()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация

    @testit.step("Проверка заголовка страницы Пользователи")
    @allure.step("Проверка заголовка страницы Пользователи")
    def check_user_page_title(self):
        assert self.element_is_displayed(self.locators.USER_PAGE_TITLE)

    @testit.step("Проверка кнопки фильтрации")
    @allure.step("Проверка кнопки фильтрации")
    def check_filter_button(self):
        assert self.element_is_displayed(self.locators.FILTER_BUTTON)

    @testit.step("Проверка кнопок добавления пользователя")
    @allure.step("Проверка кнопок добавления пользователя")
    def check_add_user_buttons(self):
        assert self.element_is_displayed(self.locators.ADD_LOCAL_USER_BUTTON)
        assert self.element_is_displayed(self.locators.ADD_FREEIPA_USER_BUTTON)

    @testit.step("Проверка заголовков столбцов")
    @allure.step("Проверка заголовков столбцов")
    def check_columns_headers(self):
        time.sleep(1)
        columns_headers = self.elements_are_visible(self.locators.COLUMNS_HEADERS)
        headers_text = []
        for element in columns_headers:
            headers_text.append(element.text)
        assert headers_text == ['Пользователь', 'Действия', 'Системная роль',
                                'Статус'], "В таблице недостаточно столбцов или есть лишние"

    @testit.step("Проверка наличия полей поиска")
    @allure.step("Проверка наличия полей поиска")
    def check_search_fields(self):
        assert len(self.elements_are_visible(
            self.locators.SEARCH_TAB_FIELDS)) == 3, "В таблице недостаточно полей поиска или есть лишние"

    @testit.step("Проверка наличия кнопок фильтрации")
    @allure.step("Проверка наличия кнопок фильтрации")
    def check_filter_tab_buttons(self):
        assert len(self.elements_are_visible(
            self.locators.TAB_FILTER_BUTTONS)) == 3, "В таблице недостаточно кнопок фильтрации или есть лишние"

    @testit.step("Берем заголовки элементов кебаб меню")
    @allure.step("Берем заголовки элементов кебаб меню")
    def get_kebab_menu_item(self):
        time.sleep(2)
        self.element_is_visible(self.locators.USER_KEBABS).click()
        menu_item = self.elements_are_visible(self.locators.KEBAB_MENU_ITEM)
        items_text = []
        for element in menu_item:
            items_text.append(element.text)
        self.action_esc()
        return items_text

    @testit.step("Получаем дату принятия на работу пользователя")
    @allure.step("Получаем дату принятия на работу пользователя")
    def get_the_hiring_date(self):
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        hiring_date = self.element_is_visible(self.locators.HIRING_DATA_INPUT).get_attribute('value')
        self.action_esc()
        return hiring_date

    @testit.step("Проверка на совпадения дат увольнения и принятия на работу")
    @allure.step("Проверка на совпадения дат увольнения и принятия на работу")
    def check_fired_data_on_date_picker(self, date):
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.FIRED_BUTTON).click()
        self.element_is_visible(self.locators.FIRED_ALERT_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.FIRED_ALERT_FIELD).send_keys(date)
        self.element_is_visible(self.locators.CALENDAR_BUTTON).click()
        assert not self.element_is_clickable(self.locators.DAY_BEFORE_SELECTED_DAY_PICKER,
                                             2), 'Можно выбрать дату приема на работу'

    @testit.step("Проверяем назначение системной роли на пользователя")
    @allure.step("Проверяем назначение системной роли на пользователя")
    def check_assigning_system_role_to_user(self):
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        user_before_add_role = self.element_is_visible(self.locators.USER_SYSTEM_ROLE_DISABLE_INDICATOR).get_attribute(
            'class')
        self.element_is_visible(self.locators.SYSTEM_ROLE_FIELD).click()
        add_role = self.elements_are_visible(self.locators.NOT_SELECTED_SYSTEM_ROLE)[0].get_attribute('aria-label')
        self.elements_are_visible(self.locators.NOT_SELECTED_SYSTEM_ROLE)[0].click()
        user_after_add_role = self.element_is_visible(self.locators.USER_SYSTEM_ROLE_DISABLE_INDICATOR).get_attribute(
            'class')
        self.element_is_visible(self.locators.delete_system_role_button(add_role)).click()
        assert 'Mui-disabled' in user_before_add_role, 'Роль Пользователь не задизейблена'
        assert 'Mui-disabled' not in user_after_add_role, 'Роль Пользователь задизейблена после добавления другой роли'

    @testit.step("Проверяем удаление единственной проектной роли")
    @allure.step("Проверяем удаление единственной проектной роли")
    def check_removing_a_single_project_role_from_a_user(self):
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация
        self.element_is_visible(self.locators.DELETE_PROJECT_ROLE_ICONS).click()
        assert not self.element_is_clickable(self.locators.SAVE_BUTTON, 1), 'Кнопка Сохранить не задизейбленна'
