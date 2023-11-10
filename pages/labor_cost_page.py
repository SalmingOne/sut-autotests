import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from locators.labor_cost_page_locators import LaborCostPageLocators
from pages.base_page import BasePage


class LaborCostPage(BasePage):
    locators = LaborCostPageLocators()

    # Переход на таблицу трудозатрат через меню
    @allure.title("Переход на таблицу трудозатрат через меню")
    def go_to_labor_cost_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_ACTIVITY))
        self.element_is_visible(self.locators.TAB_LABOR_COST_TABLE).click()

    # Проверка, что код проекта есть на странице
    @allure.title("Проверка, что код проекта есть на странице")
    def check_project_code_at_labor(self):
        check_code_at_labor = self.element_is_present(self.locators.CHECK_CODE_PROJECT).text
        print(check_code_at_labor)
        return check_code_at_labor

    # Проверка что кода проекта нет на странице
    @allure.title("Проверка что кода проекта нет на странице")
    def check_no_project_code_at_labor(self):
        try:
            check_code_at_labor = self.element_is_present(self.locators.CHECK_CODE_PROJECT).text
            print(check_code_at_labor)
            return check_code_at_labor
        except TimeoutException:
            return "no element on page"

    # Проверка что появляется окно указания причины списания
    @allure.title("Проверка что появляется окно указания причины списания ")
    def check_to_have_reason_fo_write(self):
        self.element_is_visible(self.locators.RANDOM_DAYS_BY_PROJECT).click()
        checked_text = self.element_is_visible(self.locators.CHECK_LABOR_REASON_FIELD).text
        self.element_is_visible(self.locators.BREAK_LABOR_REASON_WINDOW).click()
        assert checked_text == "Причина *", "Не открылось окно указания причины"

    # Ввод значения в клетку таблицы трудозатрат
    @allure.title("Ввод значения в клетку таблицы трудозатрат")
    def input_time(self, element, in_time):
        self.element_is_visible(element).click()
        self.element_is_visible(element).send_keys(in_time)
        self.element_is_visible(element).send_keys(Keys.RETURN)

    # Списываем трудозатраты за первый и последний (28) день месяца
    @allure.title("Списываем трудозатраты за первый и последний (28) день месяца")
    def input_work_by_month(self):
        first_day_time = 5
        last_day_time = 8
        previous_last_day_time = 6
        next_first_day_time = 3
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        self.input_time(self.locators.LAST_28_DAY_BY_PROJECT, last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        self.input_time(self.locators.LAST_28_DAY_BY_PROJECT, previous_last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()

        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, next_first_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()

        sum_in_month = first_day_time + last_day_time

        return sum_in_month

    # Очищаем все дни за месяц
    @allure.title("Очищаем все дни за месяц")
    def clear_month_work(self):
        all_day_list = self.elements_are_present(self.locators.ALL_DAYS_BY_PROJECT)
        for day in all_day_list:
            day.click()
            day.send_keys(Keys.BACK_SPACE)
            day.send_keys(Keys.BACK_SPACE)

    # Очищаем все дни за текущий, предидущий и следующи месяц
    @allure.title("Очищаем все дни за текущий, предидущий и следующи месяц")
    def three_mont_clear(self):
        self.clear_month_work()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        self.clear_month_work()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.clear_month_work()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()



