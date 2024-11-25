import time
from enum import Enum, auto

from locators.economy_page_locators import EconomyPageLocators
from pages.base_page import BasePage
from utils.concat_testit_allure_step import allure_testit_step


class EconomyPage(BasePage):
    locators = EconomyPageLocators()

    class AttractionType(Enum):
        ByUser = auto()
        BySlot = auto()
        ByFilial = auto()

    @allure_testit_step('Переход на страницу Экономика')
    def go_to_economy_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.ECONOMY_PAGE).click()

    @allure_testit_step('Открыть кебаб-меню ставки привлечения')
    def open_kebab_menu(self, attraction_rate_name, action):
        self.element_is_visible(self.locators.get_kebab_menu_by_name(attraction_rate_name), 10).click()
        self.element_is_visible(self.locators.get_kebab_action(action)).click()

    @allure_testit_step('Подтвердить удаление в модальном окне')
    def apply_deleting(self):
        self.element_is_visible(self.locators.APPLY_MODAL_WINDOW_BUTTON).click()

    @allure_testit_step('Отменить удаление в модальном окне')
    def cancel_deleting(self):
        self.element_is_visible(self.locators.DISCARD_DELETING_BUTTON).click()

    @allure_testit_step('Проверка элементов в модальном окне подтверждения удаления ставки')
    def check_modal_window_delete(self, attraction_rate_name):
        assert self.element_is_displayed(self.locators.APPLY_MODAL_WINDOW_BUTTON), "Нет кнопки Подтвердить"
        assert self.element_is_displayed(self.locators.DISCARD_DELETING_BUTTON), 'Нет кнопки Отменить'
        assert f'Вы уверены, что хотите удалить выбранную ставку "{attraction_rate_name}"?' == self.element_is_visible(self.locators.DELETING_MODAL_WINDOW_TEXT).text, 'Некорекнтый текст описания'

    @allure_testit_step("Берем текст всех сообщений системы")
    def get_alert_message(self):
        all_alerts = self.elements_are_visible(self.locators.ALERT_TEXT)
        data = []
        for alert in all_alerts:
            data.append(alert.text)
        return data

    @allure_testit_step("Получить все ставки привлечения")
    def get_all_attraction_rates(self):
        return [element.text for element in self.elements_are_visible(self.locators.ATTRACTION_RATES)]

    @allure_testit_step("Настройки фильтра отображения")
    def click_checkbox_in_filter_attraction_rates(self, type: AttractionType = None):
        from selenium.common import ElementClickInterceptedException
        try:
            self.element_is_visible(self.locators.FILTER_ICON).click()
        except ElementClickInterceptedException:
            pass
        match type:
            case self.AttractionType.ByUser:
                self.elements_are_visible(self.locators.CHECKBOXES)[0].click()
            case self.AttractionType.BySlot:
                self.elements_are_visible(self.locators.CHECKBOXES)[1].click()
            case self.AttractionType.ByFilial:
                self.elements_are_visible(self.locators.CHECKBOXES)[2].click()
            case _:
                for element in self.elements_are_visible(self.locators.CHECKBOXES, 10):
                    element.click()

    @allure_testit_step("Получить типы, отображенные на странице")
    def get_all_attraction_rates_types(self):
        return set(element.text for element in self.elements_are_visible(self.locators.ATTRACTION_RATES_TYPES))

    @allure_testit_step("Открыть дровер создания ставки привлечения")
    def open_create_drawer(self):
        self.element_is_visible(self.locators.CREATE_ATTRACTION_RATE_BUTTON).click()

    @allure_testit_step("Заполнить обязательные поля")
    def fill_fields_in_drawer(self, attraction_rate_name, target_name, type: AttractionType, size):
        self.element_is_visible(self.locators.ATTRACTION_RATE_NAME_FIELD).send_keys(attraction_rate_name)
        self.element_is_visible(self.locators.ATTRACTION_RATE_TYPE_DROPDOWN).click()
        match type:
            case self.AttractionType.ByUser:
                self.elements_are_visible(self.locators.DRAWER_LI_ITEMS)[0].click()
            case self.AttractionType.BySlot:
                self.elements_are_visible(self.locators.DRAWER_LI_ITEMS)[1].click()
            case self.AttractionType.ByFilial:
                self.elements_are_visible(self.locators.DRAWER_LI_ITEMS)[2].click()
        self.element_is_visible(self.locators.ATTRACTION_RATE_TARGET_FIELD).send_keys(target_name)
        self.elements_are_visible(self.locators.DRAWER_LI_ITEMS)[0].click()
        self.action_esc()
        self.element_is_visible(self.locators.ATTRACTION_RATE_SIZE_FIELD).send_keys(size)

    @allure_testit_step("Заполнить поля компонентов")
    def fill_components_in_drawer(self, fot, additional_expense, profitability_ratio, tax):
        self.element_is_visible(self.locators.FOT_INPUT).send_keys(fot)
        if any([fot, additional_expense, profitability_ratio, tax]):
            assert self.element_is_visible(self.locators.ATTRACTION_RATE_SIZE_FIELD).get_attribute('disabled'), "Поле ставка не задизейблено"
        self.element_is_visible(self.locators.ADDITIONAL_EXPENSES_INPUT).send_keys(additional_expense)
        self.element_is_visible(self.locators.PROFITABILITY_RATIO_INPUT).send_keys(profitability_ratio)
        self.element_is_visible(self.locators.TAXES_INPUT).send_keys(tax)

    @allure_testit_step("Провести предварительны расчет")
    def pre_calculate(self, result = None):
        self.element_is_visible(self.locators.PRE_CALCULATION_BUTTON).click()
        # assert result == self.element_is_visible(self.locators.ATTRACTION_RATE_SIZE_FIELD).get_attribute('value')

    @allure_testit_step("Получить информацию о доступности кнопки Предварительный расчет")
    def pre_calculate_button_is_disabled(self):
        return self.element_is_visible(self.locators.PRE_CALCULATION_BUTTON).get_attribute('disabled')

    @allure_testit_step("Сохранить добавление\изменение ставки привлечения")
    def save_changes(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @allure_testit_step("Отменить добавление\изменение ставки привлечения")
    def discard_changes(self):
        self.element_is_visible(self.locators.DISCARD_BUTTON).click()
        assert self.element_is_displayed(self.locators.APPLY_MODAL_WINDOW_BUTTON), "Нет кнопки Подтвердить"
        assert self.element_is_displayed(self.locators.DISCARD_MODAL_WINDOW_BUTTON), 'Нет кнопки Отмена'
        assert self.element_is_displayed(self.locators.MODAL_WINDOW_TITLE), 'Нет название модального окна'
        assert self.element_is_displayed(self.locators.MODAL_WINDOW_SUBTITLE), "Нет текста модального окна"
        self.element_is_visible(self.locators.APPLY_MODAL_WINDOW_BUTTON).click()

    @allure_testit_step("Проверить даты создания и даты изменения")
    def check_dates(self, update_date, start_date, end_date = '', row_number = 0):
        assert update_date == self.elements_are_visible(self.locators.UPDATE_DATE)[row_number].text, 'Неправильная дата изменения'
        assert start_date == self.elements_are_visible(self.locators.START_DATE)[row_number].text, 'Неправильная дата создания'
        assert end_date == self.elements_are_visible(self.locators.END_DATE)[row_number].text, 'Неправильная дата окончания'

    @allure_testit_step("Проверить строки в истории изменений")
    def check_changes_window(self, update_date, start_date, end_date, size, status, row_number = 0):
        self.check_dates(update_date, start_date, end_date, row_number)
        assert size == float(self.elements_are_visible(self.locators.ATTRACTION_RATE_SIZE_MODAL_VIEW)[row_number].text), 'Не отображается размер ставки'
        assert status == self.elements_are_visible(self.locators.ATTRACTION_RATE_STATUS_MODAL_VIEW)[row_number].text, 'Не отображается статус ставки'

    @allure_testit_step("Проверить отображение ставки привлечения в таблице")
    def check_attraction_rate_row(self, attraction_rate_name, type, size):
        assert self.element_is_displayed(self.locators.get_attraction_rate(attraction_rate_name)), 'Не отображается название ставки'
        assert self.element_is_visible(self.locators.get_attraction_rate_type(attraction_rate_name)).text == type, 'Не отображается тип ставки'
        assert float(self.element_is_visible(self.locators.get_attraction_rate_size(attraction_rate_name)).text) == size, 'Не отображается размер ставки'


