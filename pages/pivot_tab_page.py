import time

from selenium.webdriver.common.by import By

from locators.pivot_tab_page_locators import PivotTabPageLocators
from pages.base_page import BasePage


class PivotTabPage(BasePage):
    locators = PivotTabPageLocators()

    def go_to_pivot_page(self):
        self.element_is_visible(self.locators.ANALYTIC_MENU_BUTTON).click()
        self.element_is_visible(self.locators.PIVOT_TAB_BUTTON).click()

    def choose_period(self, period):
        time.sleep(1)
        self.element_is_visible(self.locators.PERIOD_SELECT_BUTTON).click()
        if period == "month":
            self.element_is_visible(self.locators.MONTH_PERIOD_SELECT).click()
        if period == "month_by_day":
            self.element_is_visible(self.locators.MONTH_BY_DAY_PERIOD_SELECT).click()
        if period == "week":
            self.element_is_visible(self.locators.WEEK_PERIOD_SELECT).click()

    def get_row_id(self):
        row_id = self.element_is_visible(self.locators.GET_ROW_ID).get_attribute("row-id")
        return row_id

    def get_sum_reason(self, period):
        row_id = self.get_row_id()
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
