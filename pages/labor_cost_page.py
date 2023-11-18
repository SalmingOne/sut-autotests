import time

import allure
from selenium.common import TimeoutException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from data.data import PROJECT_NAME
from locators.labor_cost_page_locators import LaborCostPageLocators
from pages.base_page import BasePage


class LaborCostPage(BasePage):
    locators = LaborCostPageLocators()

    # Переход на таблицу трудозатрат через меню
    @allure.step("Переход на таблицу трудозатрат через меню")
    def go_to_labor_cost_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_ACTIVITY))
        self.element_is_visible(self.locators.TAB_LABOR_COST_TABLE).click()

    # Проверка, что код проекта есть на странице
    @allure.step("Проверка, что код проекта есть на странице")
    def check_project_code_at_labor(self):
        check_code_at_labor = self.element_is_present(self.locators.CHECK_CODE_PROJECT).text
        #print(check_code_at_labor)
        return check_code_at_labor

    # Проверка что кода проекта нет на странице
    @allure.step("Проверка что кода проекта нет на странице")
    def check_no_project_code_at_labor(self):
        try:
            check_code_at_labor = self.element_is_present(self.locators.CHECK_CODE_PROJECT).text
            #print(check_code_at_labor)
            return check_code_at_labor
        except TimeoutException:
            return "no element on page"

    # Проверка что появляется окно указания причины списания
    @allure.step("Проверка что появляется окно указания причины списания ")
    def check_to_have_reason_fo_write(self):
        self.element_is_visible(self.locators.RANDOM_DAYS_BY_PROJECT).click()
        checked_text = self.element_is_visible(self.locators.CHECK_LABOR_REASON_FIELD).text
        self.element_is_visible(self.locators.BREAK_LABOR_REASON_WINDOW).click()
        assert checked_text == "Причина *", "Не открылось окно указания причины"

    # Ввод значения в клетку таблицы трудозатрат
    @allure.step("Ввод значения в клетку таблицы трудозатрат")
    def input_time(self, element, in_time):
        self.element_is_visible(element).click()
        self.element_is_visible(element).send_keys(in_time)
        self.element_is_visible(element).send_keys(Keys.RETURN)

    # Узнаем сколько дней в конкретном месяце, что бы потом вставить значение в последний день
    @allure.step("Узнаем сколько дней в конкретном месяце, что бы потом вставить значение в последний день")
    def get_number_last_month_day(self):
        all_day_list = self.elements_are_visible(self.locators.ALL_DAY_NUMBER)
        numbers = []
        for day in all_day_list:
            day_number = day.text
            numbers.append(day_number)
        # print(numbers)
        # print(len(numbers)-5)
        return len(numbers) - 5

    # Списываем трудозатраты за первый и последний (28) день месяца
    @allure.step("Списываем трудозатраты за первый и последний (28) день месяца")
    def input_work_by_month(self):
        first_day_time = 5
        last_day_time = 8
        previous_last_day_time = 6
        next_first_day_time = 3
        # Заполняем текущий месяц
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        last_day_number = self.get_number_last_month_day() + 1
        last_day_locator = (
            By.XPATH,
            f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[{last_day_number}]//input')
        self.input_time(last_day_locator, last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        # Переходим на предыдущий месяц и запоняем его
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        last_day_number = self.get_number_last_month_day() + 1
        last_day_locator = (
            By.XPATH,
            f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[{last_day_number}]//input')
        self.input_time(last_day_locator, previous_last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        # Переходим на текущий а потом следующий месяц и запоняем его
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, next_first_day_time)
        try:
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
        except ElementClickInterceptedException:
            pass
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()

        sum_in_month = first_day_time + last_day_time
        return sum_in_month

    # Очищаем все дни за месяц
    @allure.step("Очищаем все дни за месяц")
    def clear_month_work(self):
        all_day_list = self.elements_are_present(self.locators.ALL_DAYS_BY_PROJECT)
        for day in all_day_list:
            day.click()
            try:
                day.send_keys(Keys.BACK_SPACE)
                day.send_keys(Keys.BACK_SPACE)
            except ElementNotInteractableException:
                pass

    # Очищаем все дни за текущий, предидущий и следующи месяц
    @allure.step("Очищаем все дни за текущий, предидущий и следующи месяц")
    def three_mont_clear(self):
        self.clear_month_work()
        try:
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
        except ElementClickInterceptedException:
            pass
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        # self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        self.clear_month_work()
        try:
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
        except ElementClickInterceptedException:
            pass
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.clear_month_work()
        try:
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
        except ElementClickInterceptedException:
            pass
        time.sleep(1)  # Без этого ожидания не подтверждаются изменения в последнем месяце

    # Списываем трудозатраты за первый и последний день недели
    @allure.step("Списываем трудозатраты за первый и последний день недели")
    def input_work_by_week(self):
        first_day_time = 7
        last_day_time = 11
        previous_last_day_time = 8
        next_first_day_time = 2
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        self.input_time(self.locators.LAST_7_DAY_BY_PROJECT, last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        self.input_time(self.locators.LAST_7_DAY_BY_PROJECT, previous_last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()

        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, next_first_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()

        sum_in_week = first_day_time + last_day_time
        return sum_in_week

    # Выбираем отображаемый период
    @allure.step("Выбираем отображаемый период")
    def choose_period(self, period):
        time.sleep(1)
        self.element_is_visible(self.locators.PERIOD_SELECT_BUTTON).click()
        if period == "month":
            self.element_is_visible(self.locators.MONTH_PERIOD_SELECT).click()
        if period == "week":
            self.element_is_visible(self.locators.WEEK_PERIOD_SELECT).click()
