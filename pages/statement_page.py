import time

import allure
from selenium.common import TimeoutException

from locators.statement_page_locators import StatementPageLocators
from pages.base_page import BasePage


class StatementPage(BasePage):
    locators = StatementPageLocators()

    # Переходим на страницу заявлений
    @allure.step("Переходим на страницу заявлений")
    def go_to_statement_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_ACTIVITY))
        self.element_is_visible(self.locators.TAB_APPLICATION).click()

    # Удаляем все отсутствия на странице заявлений
    @allure.step("Удаляем все отсутствия на странице заявлений")
    def delete_all_absence(self):
        self.element_is_visible(self.locators.PREVIOUS_ABSENCE_CHECKBOX).click()
        count = 0
        for i in range(20):
            try:
                self.elements_are_present(self.locators.ALL_ABSENCE_KEBABS)[0].click()
                time.sleep(0.1)  # Без ожидания иногда не корректно выбираются пункты кебаба меню
                self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
                time.sleep(0.1)  # Без ожидания иногда не корректно выбираются пункты кебаба меню
                self.element_is_visible(self.locators.DEL_ACCEPT_BUTTON).click()
                count += 1
                time.sleep(0.5)  # Без ожидания иногда не корректно выбираются пункты кебаба меню
            except TimeoutException:
                break
        return count




