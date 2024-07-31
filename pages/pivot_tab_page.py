import time

import allure
import testit
from selenium.webdriver.common.by import By

from locators.pivot_tab_page_locators import PivotTabPageLocators
from pages.base_page import BasePage
from data.models.create_project_model import CreateProject


class PivotTabPage(BasePage):
    locators = PivotTabPageLocators()

    @testit.step("Переходим на сводную таблицу через меню")
    @allure.step("Переходим на сводную таблицу через меню")
    def go_to_pivot_page(self):
        time.sleep(1)
        self.element_is_visible(self.locators.ANALYTIC_MENU_BUTTON).click()
        self.element_is_visible(self.locators.PIVOT_TAB_BUTTON).click()

    @testit.step("Выбираем отображаемый период")
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

    @testit.step("Берем id строки нужного проекта для дальнейшего поиска")
    @allure.step("Берем id строки нужного проекта для дальнейшего поиска")
    def get_row_id(self, tab):
        if tab == "project":
            row_id = self.element_is_visible(self.locators.GET_ROW_ID).get_attribute("row-id")
            return row_id
        elif tab == "user":
            row_id = self.element_is_visible(self.locators.GET_ROW_ID_ON_USER).get_attribute("row-id")
            return row_id

    @testit.step("Берем сумму списанных часов за период по проекту")
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

    @testit.step("Берем сумму списанных часов за период по пользователю")
    @allure.step("Берем сумму списанных часов за период по пользователю")
    def get_sum_reason_on_user(self):
        row_id = self.get_row_id("user")
        period_sum = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@col-id="workdaysHoursSum"]/p')
        a = self.element_is_visible(period_sum).text
        print(a)
        return a

    @testit.step("Переходим на отображение таблицы по пользователю")
    @allure.step("Переходим на отображение таблицы по пользователю")
    def go_to_by_user_tab(self):
        self.element_is_visible(self.locators.BY_USER_BUTTON).click()

    @testit.step("Открываем список проектов пользователя")
    @allure.step("Открываем список проектов пользователя")
    def open_project_list(self):
        self.element_is_visible(self.locators.OPEN_PROJECT_LIST).click()

    @testit.step("Открываем дровер фильтрации (отображение)")
    @allure.step("Открываем дровер фильтрации (отображение)")
    def open_filter(self):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()

    @testit.step("Берем aria-colindex текущего столбца")
    @allure.step("Берем aria-colindex текущего столбца")
    def get_today_col_index(self):
        return self.element_is_visible(self.locators.HEADER_TODAY).get_attribute('aria-colindex')

    @testit.step("Проверяем отображение переработок в таблице по проектам")
    @allure.step("Проверяем отображение переработок в таблице по проектам")
    def check_overwork_by_project(self):
        row_id = self.element_is_visible(self.locators.get_row_id_on_project(CreateProject().name)).get_attribute("row-id")
        col_index = self.get_today_col_index()
        this_period = self.element_is_visible(self.locators.intersection_field(row_id, col_index)).text
        end_month = self.element_is_visible(self.locators.intersection_field(row_id, 8)).text
        assert this_period == end_month, 'Переработки не отразились в итоговом столбце '
        assert this_period == '3 + 3', 'Переработки не отразились в текущем столбце'

    @testit.step("Проверяем отображение переработок в таблице по пользователям")
    @allure.step("Проверяем отображение переработок в таблице по пользователям")
    def check_overwork_by_user(self):
        row_id = self.element_is_visible(self.locators.get_row_id_on_user(CreateProject().name)).get_attribute("row-id")
        col_index = self.get_today_col_index()
        this_period = self.element_is_visible(self.locators.intersection_field(row_id, col_index)).text
        end_month = self.element_is_visible(self.locators.intersection_field(row_id, 8)).text
        assert this_period == end_month, 'Переработки не отразились в итоговом столбце '
        assert this_period == '3 + 3', 'Переработки не отразились в текущем столбце'

