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
        self.action_triple_click(self.element_is_visible(self.locators.USER_SEARCH_FIELD))
        time.sleep(1)
        self.element_is_visible(self.locators.USER_SEARCH_FIELD).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.USER_SEARCH_FIELD).send_keys(f'{last_name}')
        return self.element_is_displayed(self.locators.USER_KEBABS, 3)

    @testit.step("Переход на страницу Пользователи")
    @allure.step("Переход на страницу Пользователи")
    def go_to_user_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_ROLE).click()
        self.elements_are_visible(self.locators.USER_KEBABS, 10)

    @testit.step("Переход на страницу Пользователи без ожидания появления таблицы")
    @allure.step("Переход на страницу Пользователи без ожидания появления таблицы")
    def go_to_user_page_simple(self):
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
        time.sleep(1)
        return self.element_is_visible(self.locators.USER_STATUS).text

    @testit.step("Уволить пользователя")
    @allure.step("Уволить пользователя")
    def fired_user(self):
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.FIRED_BUTTON).click()
        self.action_double_click(self.element_is_visible(self.locators.FIRED_ALERT_FIELD))
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
        self.action_double_click(self.element_is_visible(self.locators.FIRED_ALERT_FIELD))
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
        time.sleep(4)
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
        time.sleep(2)  # Без ожидания не успевает срабатывать анимация
        self.element_is_visible(self.locators.DELETE_PROJECT_ROLE_ICONS).click()
        assert not self.element_is_clickable(self.locators.SAVE_BUTTON, 1), 'Кнопка Сохранить не задизейбленна'

    @testit.step("Редактирование пользователя")
    @allure.step("Редактирование пользователя")
    def go_to_redact_user(self):
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.REDACT_BUTTON).click()

    @testit.step("Нажатие кнопки фильтрации")
    @allure.step("Нажатие кнопки фильтрации")
    def press_filter_button(self):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()

    @testit.step("Нажатие чекбокса Почасовая оплата")
    @allure.step("Нажатие чекбокса Почасовая оплата")
    def press_hourly_wage_checkbox(self):
        self.element_is_visible(self.locators.HOUR_WAGE_CHECKBOX).click()

    @testit.step("Нажатие чекбокса По окладу")
    @allure.step("Нажатие чекбокса По окладу")
    def press_by_salary_checkbox(self):
        self.element_is_visible(self.locators.BY_SALARY_CHECKBOX).click()

    @testit.step("Проверка наличия картинки Данные отсутствуют")
    @allure.step("Проверка наличия картинки Данные отсутствуют")
    def check_no_data_image(self):
        assert self.element_is_displayed(self.locators.NO_DATA_IMAGE), "Нет картинки Данные отсутствуют"

    @testit.step("Получение текста выбранных чекбоксов")
    @allure.step("Получение текста выбранных чекбоксов")
    def get_checked_checkboxes_text(self):
        element_list = self.elements_are_visible(self.locators.CHECKED_CHECKBOXES_TEXT)
        data = []
        for element in element_list:
            self.go_to_element(element)
            data.append(element.text)
        return data

    @testit.step("Открытие дровера редактирования пользователя")
    @allure.step("Открытие дровера редактирования пользователя")
    def open_redact_drawer(self):
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация
        self.element_is_visible(self.locators.USER_KEBABS).click()
        self.element_is_visible(self.locators.REDACT_BUTTON).click()

    @testit.step("Проверка кликабельности предыдущего дня в датапикере")
    @allure.step("Проверка кликабельности предыдущего дня в датапикере")
    def check_clickable_previous_day(self):
        self.element_is_visible(self.locators.DISMISSAL_DATA_DATA_PICKER).click()
        assert not self.element_is_clickable(self.locators.DAY_BEFORE_SELECTED_DAY_PICKER,
                                             2), 'Можно выбрать дату приема на работу'

    @testit.step("Нажатие кнопки отмены в дровере")
    @allure.step("Нажатие кнопки отмены в дровере")
    def press_cancel_button(self):
        self.element_is_visible(self.locators.ABORT_BUTTON).click()

    @testit.step("Нажатие кнопки следующего дня в датапикере")
    @allure.step("Нажатие кнопки следующего дня в датапикере")
    def press_next_day_button_in_data_picker(self):
        self.element_is_visible(self.locators.DAY_AFTER_THIS_DAY_PICKER).click()

    @testit.step("Нажатие кнопки сохранения в дровере")
    @allure.step("Нажатие кнопки сохранения в дровере")
    def press_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Берем текст сообщения системы")
    @allure.step("Берем текст сообщения системы")
    def get_alert_message(self):
        self.elements_are_visible(self.locators.ALERT_TEXT, 15)
        all_messages = self.elements_are_visible(self.locators.ALERT_TEXT)
        data = []
        for message in all_messages:
            data.append(message.text)
        return data

    @testit.step("Проверка наличия пункта Восстановить в кебаб меню")
    @allure.step("Проверка наличия пункта Восстановить в кебаб меню")
    def check_restore_menu_item(self):
        time.sleep(1)  # Без ожидания не успевает срабатывать анимация
        self.element_is_visible(self.locators.USER_KEBABS).click()
        assert self.element_is_displayed(self.locators.RESTORE_BUTTON)

    @testit.step("Проверка корректности даты увольнения")
    @allure.step("Проверка корректности даты увольнения")
    def check_data_fired_in_drawer(self):
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        assert self.element_is_visible(self.locators.DISMISSAL_DATA).get_attribute('value') == self.get_day_before(-1), \
            "Дата увольнения не следующий день"

