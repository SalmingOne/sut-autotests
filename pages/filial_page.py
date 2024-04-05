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
        self.element_is_visible(self.locators.ATTRACTION_RATE_FIELD).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_visible(locator).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(locator).send_keys('1')
        self.element_is_visible(self.locators.ATTRACTION_RATE_FIELD).click()
        assert error_text == 'Максимальное количество символов: 255', \
            "Не появилось сообщение о превышении максимального количества символов"

    @testit.step("Проверка всех полей с ограничением в 255 символов")
    @allure.step("Проверка всех полей с ограничением в 255 символов")
    def check_max_lait(self):
        fields = [self.locators.NAME_FIELD, self.locators.ADDRESS_FIELD, ]
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
        print(size_before)
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
        self.check_attraction_rate()
        self.element_is_visible(self.locators.PHONE_FIELD).send_keys(phone)
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка наличия филиала в таблице")
    @allure.step("Проверка наличия филиала в таблице")
    def check_filial_on_tab(self, name):
        assert self.element_is_displayed(self.locators.text_on_page(name)), "Филиала нет в таблице"


