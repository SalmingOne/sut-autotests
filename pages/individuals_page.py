import time

import allure
import testit
from selenium.webdriver import Keys

from locators.individuals_page_locators import IndividualsPageLocators
from pages.base_page import BasePage


class IndividualsPage(BasePage):
    locators = IndividualsPageLocators()

    @testit.step("Переход на справочник Физические лица")
    @allure.step("Переход на справочник Физические лица")
    def go_to_individuals_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.REFERENCE_BOOKS).click()
        self.element_is_visible(self.locators.INDIVIDUALS_TAB).click()

    @testit.step("Открытие дровера добавления Физического лица")
    @allure.step("Открытие дровера добавления Физического лица")
    def open_add_drawer(self):
        self.element_is_visible(self.locators.ADD_INDIVIDUALS_BUTTON).click()

    @testit.step("Проверка ограничения в 255 символов для поля")
    @allure.step("Проверка ограничения в 255 символов для поля")
    def check_255_symbol_in_field(self, locator):
        bed_value = ('Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt'
                     ' ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci'
                     ' tation ullamcorper suscipit lobortis nisl ut aliquip ex ea co')
        self.element_is_visible(locator).send_keys(bed_value)
        self.element_is_visible(self.locators.ROLE_DROPDOWN).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_visible(locator).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(locator).send_keys('1')
        self.element_is_visible(self.locators.ROLE_DROPDOWN).click()
        assert error_text == 'Максимальное количество символов: 255',\
            "Не появилось сообщение о превышении максимального количества символов"

    @testit.step("Проверка всех полей с ограничением в 255 символов")
    @allure.step("Проверка всех полей с ограничением в 255 символов")
    def check_max_lait(self):
        fields = [self.locators.NAME_FIELD, self.locators.SECOND_NAME_FIELD, self.locators.TIRD_NAME_FIELD,
                  self.locators.INN_FIELD, self.locators.ADDRESS_FIELD, self.locators.PHONE_FIELD,
                  self.locators.DOCUMENT_NAME_FIELD, self.locators.DOCUMENT_SECOND_NAME_FIELD,
                  self.locators.DOCUMENT_TIRD_NAME_FIELD, self.locators.SERIES_FIELD, self.locators.NUMBER_FIELD,
                  self.locators.AUTHORITY_FIELD, self.locators.BANK_NAME_FIELD, self.locators.BANK_INN_FIELD,
                  self.locators.BANK_ACCOUNT_FIELD, self.locators.BANK_CORRESPONDENT_ACCOUNT_FIELD]
        for field in fields:
            self.check_255_symbol_in_field(field)

    @testit.step("Проверка поля email")
    @allure.step("Проверка поля email")
    def check_email(self):
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys('2')
        self.element_is_visible(self.locators.ROLE_DROPDOWN).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys('abs@abs.abs')
        self.element_is_visible(self.locators.ROLE_DROPDOWN).click()
        assert error_text == 'Некорректный email-адрес', "Не появилось сообщение о некорректном email"

    @testit.step("Проверка дата-пикеров в дровере")
    @allure.step("Проверка дата-пикеров в дровере")
    def check_date_pikers(self):
        assert len(self.elements_are_visible(self.locators.DATE_PIKERS)) == 2, "В дровере не два дата-пикера"

    @testit.step("Получение значений дропдауна")
    @allure.step("Получение значений дропдауна")
    def get_dropdown_items(self):
        dropdown_items = self.elements_are_visible(self.locators.DROPDOWN_ITEMS)
        names = []
        for item in dropdown_items:
            names.append(item.text)
        return names

    @testit.step("Проверка дропдауна Роль")
    @allure.step("Проверка дропдауна Роль")
    def check_role_dropdown(self):
        self.element_is_visible(self.locators.NAME_FIELD).click()
        self.element_is_visible(self.locators.ROLE_DROPDOWN).click()
        assert self.get_dropdown_items() == ['Сотрудник', 'Заказчик', 'Субподрядчик'], "Не корректный список ролей"
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[0].click()

    @testit.step("Проверка дропдауна Тип документа")
    @allure.step("Проверка дропдауна Тип документа")
    def check_document_type_dropdown(self):
        self.element_is_visible(self.locators.DOCUMENT_TYPE_DROPDOWN).click()
        assert self.get_dropdown_items() == ['Паспорт РФ', 'РВП лица без гражданства', 'ВНЖ лица без гражданства',
                                             'Паспорт иностранного гражданства',
                                             'Иной документ, удостоверяющий личность'], "Не корректный список документов"
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[0].click()

    @testit.step("Проверка поля бик банка")
    @allure.step("Проверка поля бик банка")
    def check_bic_bank(self):
        self.element_is_visible(self.locators.BANK_BIC_FIELD).send_keys('1234567890')
        self.element_is_visible(self.locators.NAME_FIELD).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_visible(self.locators.BANK_BIC_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.BANK_BIC_FIELD).send_keys('123456789')
        self.element_is_visible(self.locators.NAME_FIELD).click()
        assert error_text == 'Максимальное количество символов: 9', "Нет ошибки о превышении символов"

    @testit.step("Проверка кнопки сохранить до заполнения обязательных полей")
    @allure.step("Проверка кнопки сохранить до заполнения обязательных полей")
    def check_clickable_submit_button(self):
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON), "Кнопка сохранить не задизейблена"

    @testit.step("Проверка кнопки отмены")
    @allure.step("Проверка кнопки отмены")
    def press_abort_button(self):
        self.element_is_visible(self.locators.ABORT_BUTTON).click()

    @testit.step("Создание физического лица")
    @allure.step("Создание физического лица")
    def create_individual(self, name, second_name, inn, phone, email):
        self.element_is_visible(self.locators.ADD_INDIVIDUALS_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.SECOND_NAME_FIELD).send_keys(second_name)
        self.element_is_visible(self.locators.INN_FIELD).send_keys(inn)
        self.element_is_visible(self.locators.PHONE_FIELD).send_keys(phone)
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
        self.element_is_visible(self.locators.ROLE_DROPDOWN).click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[0].click()
        self.element_is_visible(self.locators.INN_FIELD).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка наличия физического лица в таблице")
    @allure.step("Проверка наличия физического лица в таблице")
    def check_individual_on_tab(self, full_name):
        time.sleep(1)
        self.elements_are_visible(self.locators.SEARCH_TAB_FIELDS)[1].send_keys(Keys.CONTROL + 'a')
        time.sleep(1)
        self.elements_are_visible(self.locators.SEARCH_TAB_FIELDS)[1].send_keys(Keys.BACK_SPACE)
        self.elements_are_visible(self.locators.SEARCH_TAB_FIELDS)[1].send_keys(f'{full_name}')
        assert self.element_is_displayed(self.locators.KEBABS), "Физического лица нет в таблице"

    @testit.step("Удаление физического лица")
    @allure.step("Удаление физического лица")
    def delete_individual(self):
        self.element_is_visible(self.locators.KEBABS).click()
        self.element_is_visible(self.locators.DELETE_BUTTON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)
