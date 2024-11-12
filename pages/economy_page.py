import time

from locators.economy_page_locators import EconomyPageLocators
from pages.base_page import BasePage
from utils.concat_testit_allure_step import allure_testit_step


class EconomyPage(BasePage):
    locators = EconomyPageLocators()

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