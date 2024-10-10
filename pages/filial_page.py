import time

import allure
import testit
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from locators.filial_page_locators import FilialPageLocators
from pages.base_page import BasePage


class FilialPage(BasePage):
    locators = FilialPageLocators()

    @testit.step("Переход на справочник Филиалы")
    @allure.step("Переход на справочник Филиалы")
    def go_to_filial_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.REFERENCE_BOOKS).click()
        self.element_is_visible(self.locators.FILIAL_TAB).click()
        self.element_is_visible(self.locators.KEBAB_MENU, 15)

    @testit.step("Открытие дровера добавления филиала")
    @allure.step("Открытие дровера добавления филиала")
    def open_add_filial_drawer(self):
        self.element_is_visible(self.locators.ADD_FILIAL_BUTTON).click()

    @testit.step("Проверка ограничения в 255 символов для поля")
    @allure.step("Проверка ограничения в 255 символов для поля")
    def check_255_symbol_in_field(self, locator):
        bed_value = ('Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt'
                     ' ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci'
                     ' tation ullamcorper suscipit lobortis nisl ut aliquip ex ea co')
        self.element_is_visible(locator).send_keys(bed_value)
        self.element_is_visible(self.locators.EMAIL_FIELD).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_visible(locator).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(locator).send_keys('1')
        self.element_is_visible(self.locators.EMAIL_FIELD).click()
        assert error_text == 'Максимальное количество символов: 255', \
            "Не появилось сообщение о превышении максимального количества символов"

    @testit.step("Проверка всех полей с ограничением в 255 символов")
    @allure.step("Проверка всех полей с ограничением в 255 символов")
    def check_max_lait(self):
        fields = [self.locators.NAME_FIELD, self.locators.ADDRESS_FIELD]
        for field in fields:
            self.check_255_symbol_in_field(field)

    @testit.step("Проверка полей Сотрудники и Директор")
    @allure.step("Проверка полей Сотрудники и Директор")
    def check_employees_and_director_fields(self):
        self.element_is_visible(self.locators.EMPLOYEES_FIELD).click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[1].click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[2].click()
        self.action_esc()
        self.element_is_visible(self.locators.DIRECTOR_FIELD).click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[0].click()

    @testit.step("Проверка кнопки Сохранить")
    @allure.step("Проверка кнопки Сохранить")
    def check_clickable_save_button(self):
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 1), "Кнопка Сохранить не задизейблена"

    @testit.step("Проверка поля Родительский филиал")
    @allure.step("Проверка поля Родительский филиал")
    def check_affiliate_field(self):
        assert self.element_is_displayed(self.locators.AFFILIATE_FIELD), "Нет поля Родительский филиал"

    @testit.step("Проверка полей Ставки привлечения и Размер ставки")
    @allure.step("Проверка полей Ставки привлечения и Размер ставки")
    def check_attraction_rate(self):
        size_before = self.element_is_visible(self.locators.ATTRACTION_RATE_SIZE_FIELD).get_attribute('value')
        self.element_is_visible(self.locators.ATTRACTION_RATE_FIELD).click()
        try:
            self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[0].click()
            size_after = self.element_is_visible(self.locators.ATTRACTION_RATE_SIZE_FIELD).get_attribute('value')
            assert size_before == '', "Поле размер ставки не пустое"
            assert size_after != size_before, "Поле размер ставки не изменилось после выбора ставки привлечения"
            assert not self.element_is_clickable(self.locators.ATTRACTION_RATE_SIZE_FIELD, 0.5), \
                "Поле размер ставки не задизейблено"
        except TimeoutException:
            print('В системе нет ставок привлечения с типом по филиалу')

    @testit.step("Проверка поля Телефон")
    @allure.step("Проверка поля Телефон")
    def check_phone_field(self):
        assert self.element_is_displayed(self.locators.PHONE_FIELD), "Нет поля Телефон"
        assert self.element_is_visible(self.locators.PHONE_FIELD).get_attribute('placeholder') == '+7(###)### ## ##',\
            "В поле Телефон нет плейсходера"

    @testit.step("Проверка поля Email")
    @allure.step("Проверка поля Email")
    def check_email_field(self):
        assert self.element_is_displayed(self.locators.AFFILIATE_FIELD), "Нет поля Email"

    @testit.step("Нажатие кнопки Отменить")
    @allure.step("Нажатие кнопки Отменить")
    def press_abort_button(self):
        self.element_is_visible(self.locators.ABORT_BUTTON).click()

    @testit.step("Добавление филиала")
    @allure.step("Добавление филиала")
    def add_filial(self, name, address, phone, email):
        self.element_is_visible(self.locators.ADD_FILIAL_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.ADDRESS_FIELD).send_keys(address)
        self.check_employees_and_director_fields()
        self.element_is_visible(self.locators.AFFILIATE_FIELD).click()
        try:
            self.elements_are_visible(self.locators.DROPDOWN_ITEMS, 2)[0].click()
        except TimeoutException:
            print('Нет родительских филиалов')
        self.element_is_visible(self.locators.PHONE_FIELD).send_keys(phone)
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка наличия филиала в таблице")
    @allure.step("Проверка наличия филиала в таблице")
    def check_filial_on_tab(self, name):
        return self.element_is_displayed(self.locators.text_on_page(name))

    @testit.step("Получаем адрес филиала")
    @allure.step("Получаем адрес филиала")
    def get_address_on_tab(self, name):
        return self.element_is_visible(self.locators.address_by_filial_name(name)).text

    @testit.step("Изменение адреса филиала")
    @allure.step("Изменение адреса филиала")
    def change_filial_address(self, name, new_address):
        self.element_is_visible(self.locators.kebab_by_filial_name(name)).click()
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        self.element_is_visible(self.locators.ADDRESS_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.ADDRESS_FIELD).send_keys(new_address)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Удаление филиала")
    @allure.step("Удаление филиала")
    def delete_filial(self, name):
        self.element_is_visible(self.locators.kebab_by_filial_name(name)).click()
        time.sleep(1)
        self.element_is_visible(self.locators.KEBAB_DELETE_BUTTON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Назначение случайных пользователей в филиал")
    @allure.step("Назначение случайных пользователей в филиал")
    def add_first_user_to_filial(self, filial_name):
        self.element_is_visible(self.locators.kebab_by_filial_name(filial_name)).click()
        time.sleep(1)
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        self.element_is_visible(self.locators.EMPLOYEES_FIELD).click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[1].click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[2].click()
        self.action_esc()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Получение пользователей назначенных на филиал")
    @allure.step("Получение пользователей назначенных на филиал")
    def get_employees_in_field(self):
        all_chips = self.elements_are_visible(self.locators.EMPLOYEES_CHIPS)
        data = []
        for chips in all_chips:
            data.append(chips.text)
        return data

    @testit.step("Проверка удаления пользователя из филиала")
    @allure.step("Проверка удаления пользователя из филиала")
    def check_removing_user_from_filial(self, filial_name):
        time.sleep(1)
        self.element_is_visible(self.locators.kebab_by_filial_name(filial_name)).click()
        time.sleep(2)
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        employees_before = self.get_employees_in_field()
        self.elements_are_visible(self.locators.EMPLOYEES_CHIPS_DELETE_ICON)[0].click()
        employees_after = self.get_employees_in_field()
        assert employees_before != employees_after, 'Пользователь не удалился из поля'

    @testit.step("Удаление всех ресурсов с филиала")
    @allure.step("Удаление всех ресурсов с филиала")
    def delete_all_resources_from_filial(self, name):
        self.element_is_visible(self.locators.kebab_by_filial_name(name)).click()
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        self.element_is_visible(self.locators.DIRECTOR_FIELD).click()
        self.element_is_visible(self.locators.CLEAR_DIRECTOR_FIELD_BUTTON).click()
        all_employs = self.elements_are_visible(self.locators.EMPLOYEES_CHIPS_DELETE_ICON)
        while len(all_employs) > 0:
            try:
                self.elements_are_visible(self.locators.EMPLOYEES_CHIPS_DELETE_ICON, 1)[0].click()
            except TimeoutException:
                break
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка заголовков колонок таблицы")
    @allure.step("Проверка заголовков колонок таблицы")
    def check_table_column_headings(self):
        assert self.element_is_displayed(self.locators.NAME_HEADING), 'Некорректный заголовок столбца Название'
        assert self.element_is_displayed(self.locators.ADDRESS_HEADING), 'Некорректный заголовок столбца Адрес'
        assert self.element_is_displayed(self.locators.PARENT_FILIAL_HEADING), 'Некорректный заголовок столбца Родительский филиал'
        assert self.element_is_displayed(self.locators.ACTIONS_HEADING), 'Некорректный заголовок столбца Действия'

    @testit.step("Проверка заголовков колонок таблицы")
    @allure.step("Проверка заголовков колонок таблицы")
    def check_buttons_on_tab_filial(self):
        self.element_is_visible(self.locators.KEBAB_MENU).click()
        assert self.element_is_displayed(self.locators.REDACT_BUTTON), 'Нет Редактирования'
        assert self.element_is_displayed(self.locators.KEBAB_VIEW_FULL_INFO_BUTTON), 'Нет Просмотра полной информации'
        assert self.element_is_displayed(self.locators.KEBAB_DELETE_BUTTON), 'Нет Удаления'
        assert self.element_is_displayed(self.locators.ADD_FILIAL_BUTTON), 'Нет кнопки Создать филиал'
