import time

import allure
from selenium.webdriver.common.by import By

from locators.pivot_tab_page_locators import PivotTabPageLocators
from pages.base_page import BasePage


class PivotTabPage(BasePage):
    locators = PivotTabPageLocators()

    # Переходим на сводную таблицу через меню
    @allure.step("Переходим на сводную таблицу через меню")
    def go_to_pivot_page(self):
        self.element_is_visible(self.locators.ANALYTIC_MENU_BUTTON).click()
        self.element_is_visible(self.locators.PIVOT_TAB_BUTTON).click()

    # Выбираем отображаемый период
    @allure.step("Выбираем отображаемый период")
    def choose_period(self, period):
        time.sleep(1)
        self.element_is_visible(self.locators.PERIOD_SELECT_BUTTON).click()
        if period == "month":
            self.element_is_visible(self.locators.MONTH_PERIOD_SELECT).click()
        if period == "month_by_day":
            self.element_is_visible(self.locators.MONTH_BY_DAY_PERIOD_SELECT).click()
        if period == "week":
            self.element_is_visible(self.locators.WEEK_PERIOD_SELECT).click()

    # Берем id строки нужного проекта для дальнейшего поиска
    @allure.step("Берем id строки нужного проекта для дальнейшего поиска ")
    def get_row_id(self, tab):
        if tab == "project":
            row_id = self.element_is_visible(self.locators.GET_ROW_ID).get_attribute("row-id")
            return row_id
        if tab == "user":
            row_id = self.element_is_visible(self.locators.GET_ROW_ID_ON_USER).get_attribute("row-id")
            return row_id

    # Берем сумму списаных часов за период по проекту
    @allure.step("Берем сумму списаных часов за период по проекту")
    def get_sum_reason_on_project(self, period):
        row_id = self.get_row_id("project")
        if period == "month":
            PERIOD_SUM = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@aria-colindex="8"]/p')
            a = self.element_is_visible(PERIOD_SUM).text
            print(a)
            return a
        if period == "week":
            PERIOD_SUM = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@aria-colindex="10"]//p')
            a = self.element_is_visible(PERIOD_SUM).text
            print(a)
            return a

    # Берем сумму списаных часов за период по пользователю
    @allure.step("Берем сумму списаных часов за период по пользователю")
    def get_sum_reason_on_user(self, period):
        row_id = self.get_row_id("user")
        if period == "month":
            PERIOD_SUM = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@col-id="workdaysHoursSum"]/p')
            a = self.element_is_visible(PERIOD_SUM).text
            print(a)
            return a
        if period == "week":
            PERIOD_SUM = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@col-id="workdaysHoursSum"]/p')
            a = self.element_is_visible(PERIOD_SUM).text
            print(a)
            return a

    # Переходим на отображение таблицы по пользователю
    @allure.step("Переходим на отображение таблицы по пользователю")
    def go_to_by_user_tab(self):
        self.element_is_visible(self.locators.BY_USER_BUTTON).click()

    # Открываем списо проектов пользователя
    @allure.step("Открываем списо проектов пользователя")
    def open_project_list(self):
        self.element_is_visible(self.locators.OPEN_PROJECT_LIST).click()
