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
        self.element_is_visible(self.locators.APPLY_DELETING_BUTTON).click()

    @allure_testit_step('Отменить удаление в модальном окне')
    def cancel_deleting(self):
        self.element_is_visible(self.locators.DISCARD_DELETING_BUTTON).click()

    @allure_testit_step('Проверка элементов в модальном окне подтверждения удаления ставки')
    def check_modal_window(self, attraction_rate_name):
        assert self.element_is_displayed(self.locators.APPLY_DELETING_BUTTON), "Нет кнопки Подтвердить"
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

