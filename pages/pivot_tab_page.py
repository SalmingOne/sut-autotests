import time

import allure
from selenium.webdriver.common.by import By

from locators.pivot_tab_page_locators import PivotTabPageLocators
from pages.base_page import BasePage


class PivotTabPage(BasePage):
    locators = PivotTabPageLocators()

    @allure.step("Переходим на сводную таблицу через меню")
    def go_to_pivot_page(self):
        self.element_is_visible(self.locators.ANALYTIC_MENU_BUTTON).click()
        self.element_is_visible(self.locators.PIVOT_TAB_BUTTON).click()

    @allure.step("Выбираем отображаемый период")
    def choose_period(self, period):
        time.sleep(1)
        self.element_is_visible(self.locators.PERIOD_SELECT_BUTTON).click()
        if period == "month":
            self.element_is_visible(self.locators.MONTH_PERIOD_SELECT).click()
        elif period == "month_by_day":
            self.element_is_visible(self.locators.MONTH_BY_DAY_PERIOD_SELECT).click()
        elif period == "week":
            self.element_is_visible(self.locators.WEEK_PERIOD_SELECT).click()
        elif period == "year":
            self.element_is_visible(self.locators.YEAR_PERIOD_SELECT).click()

    @allure.step("Берем id строки нужного проекта для дальнейшего поиска ")
    def get_row_id(self, tab):
        if tab == "project":
            row_id = self.element_is_visible(self.locators.GET_ROW_ID).get_attribute("row-id")
            return row_id
        elif tab == "user":
            row_id = self.element_is_visible(self.locators.GET_ROW_ID_ON_USER).get_attribute("row-id")
            return row_id

    @allure.step("Берем сумму списанных часов за период по проекту")
    def get_sum_reason_on_project(self, period):
        row_id = self.get_row_id("project")
        if period == "month":
            period_sum = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@aria-colindex="8"]/p')
            a = self.element_is_visible(period_sum).text
            print(a)
            return a
        elif period == "week":
            period_sum = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@aria-colindex="10"]//p')
            a = self.element_is_visible(period_sum).text
            print(a)
            return a
        elif period == "year":
            period_sum = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@aria-colindex="15"]//p')
            a = self.element_is_visible(period_sum).text
            print(a)
            return a

    @allure.step("Берем сумму списанных часов за период по пользователю")
    def get_sum_reason_on_user(self):
        row_id = self.get_row_id("user")
        period_sum = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@col-id="workdaysHoursSum"]/p')
        a = self.element_is_visible(period_sum).text
        print(a)
        return a

    @allure.step("Переходим на отображение таблицы по пользователю")
    def go_to_by_user_tab(self):
        self.element_is_visible(self.locators.BY_USER_BUTTON).click()

    @allure.step("Открываем список проектов пользователя")
    def open_project_list(self):
        self.element_is_visible(self.locators.OPEN_PROJECT_LIST).click()

    @allure.step("Открываем дровер фильтрации (отображение)")
    def open_filter(self):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()
