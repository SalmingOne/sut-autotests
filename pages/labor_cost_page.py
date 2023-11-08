import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from locators.labor_cost_page_locators import LaborCostPageLocators
from pages.base_page import BasePage


class LaborCostPage(BasePage):
    locators = LaborCostPageLocators()

    # Переход на таблицу трудозатрат через меню
    def go_to_labor_cost_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_ACTIVITY))
        self.element_is_visible(self.locators.TAB_LABOR_COST_TABLE).click()

    # Проверка, что код проекта есть на странице
    def check_project_code_at_labor(self):
        check_code_at_labor = self.element_is_present(self.locators.CHECK_CODE_PROJECT).text
        print(check_code_at_labor)
        return check_code_at_labor

    # Проверка что кода проекта нет на странице
    def check_no_project_code_at_labor(self):
        try:
            check_code_at_labor = self.element_is_present(self.locators.CHECK_CODE_PROJECT).text
            print(check_code_at_labor)
            return check_code_at_labor
        except TimeoutException:
            return "no element on page"

    # Проверка что появляется окно указания причины спмсания обязательн
    def check_to_have_reason_fo_write(self):
        self.element_is_visible(self.locators.RANDOM_DAYS_BY_PROJECT).click()
        checked_text = self.element_is_visible(self.locators.CHECK_LABOR_REASON_FIELD).text
        self.element_is_visible(self.locators.BREAK_LABOR_REASON_WINDOW).click()
        assert checked_text == "Причина *", "Не открылось окно указания причины"

    # Ввод значения в клетку таблицы трудозатрат
    def input_time(self, element, in_time):
        self.element_is_visible(element).click()
        self.element_is_visible(element).send_keys(in_time)
        self.element_is_visible(element).send_keys(Keys.RETURN)

    # Списываем трудозатраты за первый и последний (28) день месяца
    def input_work_by_month(self):
        first_day_time = 5
        last_day_time = 8
        previous_last_day_time = 6
        next_first_day_time = 3
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        self.input_time(self.locators.LAST_28_DAY_BY_PROJECT, last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
