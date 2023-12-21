import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from locators.statement_page_locators import StatementPageLocators
from pages.base_page import BasePage


class StatementPage(BasePage):
    locators = StatementPageLocators()

    @allure.step("Переходим на страницу заявлений")
    def go_to_statement_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_ACTIVITY))
        self.element_is_visible(self.locators.TAB_APPLICATION).click()

    @allure.step("Удаляем все отсутствия на странице заявлений")
    def delete_all_absence(self):
        count = 0
        for i in range(20):
            try:
                self.elements_are_visible(self.locators.ALL_ABSENCE_KEBABS)[0].click()
                time.sleep(0.1)  # Без ожидания иногда не корректно выбираются пункты кебаба меню
                self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
                time.sleep(0.1)  # Без ожидания иногда не корректно выбираются пункты кебаба меню
                self.element_is_visible(self.locators.DEL_ACCEPT_BUTTON).click()
                count += 1
                time.sleep(0.5)  # Без ожидания иногда не корректно выбираются пункты кебаб меню
            except TimeoutException:
                break
        return count

    @allure.step("Ставим чекбокс предыдущих отсутствий")
    def click_previous_checkbox(self):
        self.element_is_visible(self.locators.PREVIOUS_ABSENCE_CHECKBOX).click()

    @allure.step("Открываем кебаб меню для редактирования")
    def open_kebab_redact(self):
        self.elements_are_visible(self.locators.ALL_ABSENCE_KEBABS)[0].click()
        self.element_is_visible(self.locators.KEBABS_REDACT_MENU_ITEM).click()

    @allure.step("Изменяем дату в отсутствии")
    def change_date_absense(self, day_number):
        time.sleep(0.5)  # Ожидание нужно для прогрузки анимации
        input_day = self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[0].get_attribute('value')
        if day_number >= 9:
            insert_day = str(day_number + 1)
        elif day_number <= 8:
            insert_day = '0' + str(day_number + 1)
        output_day = insert_day + input_day[2:10]
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[0].click()
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[0].send_keys(Keys.CONTROL + 'a')
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[0].send_keys(Keys.BACK_SPACE)
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[0].send_keys(output_day)
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[1].click()
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[1].send_keys(Keys.CONTROL + 'a')
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[1].send_keys(Keys.BACK_SPACE)
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[1].send_keys(output_day)
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[1].send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.DRAWER_SAVE_BUTTON).click()
        return output_day

    @allure.step("Берем дату начала и окончания отсутствия из таблицы")
    def check_data_absense(self):
        start_date = self.elements_are_visible(self.locators.ABSENCE_START_DATE_ON_TAB)[0].text
        end_date = self.elements_are_visible(self.locators.ABSENCE_END_DATE_ON_TAB)[0].text
        return start_date, end_date

    @allure.step("Проверяем удаление заявления")
    def check_delete_absense(self):
        self.elements_are_visible(self.locators.ALL_ABSENCE_KEBABS)[0].click()
        self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
        description_text = self.element_is_visible(self.locators.DRAWER_DESCRIPTION_TEXT).text
        self.element_is_visible(self.locators.DEL_ACCEPT_BUTTON).click()
        return description_text

    @allure.step("Берем текст сообщения системы")
    def get_allert_message(self):
        all_alerts = self.elements_are_visible(self.locators.ALLERT_TEXT)
        data = []
        for allert in all_alerts:
            data.append(allert.text)
        return data
