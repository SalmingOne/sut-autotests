import time

import allure
import testit

from locators.gantt_page_locators import GanttPageLocators
from pages.base_page import BasePage


class GanttPage(BasePage):
    locators = GanttPageLocators()

    @testit.step("Переход на вкладку Диаграмма Ганта")
    @allure.step("Переход на вкладку Диаграмма Ганта")
    def go_to_gantt_tab(self):
        self.element_is_visible(self.locators.GANTT_TAB).click()

    @testit.step("Добавление фазы")
    @allure.step("Добавление фазы")
    def add_phase(self, phase_name):
        self.element_is_visible(self.locators.EDIT_GANTT_BUTTON).click()
        self.element_is_visible(self.locators.CREATE_PHASE_OR_TASK_BUTTON).click()
        self.element_is_visible(self.locators.CREATE_PHASE_BUTTON).click()
        self.element_is_visible(self.locators.PHASE_NAME_FIELD).send_keys(phase_name)
        self.element_is_visible(self.locators.DRAWER_SUBMIT_BUTTON).click()

    @testit.step("Проверка даты начала и окончания")
    @allure.step("Проверка даты начала и окончания")
    def check_start_and_end_dates(self, phase_name):
        time.sleep(0.5)
        start_date = self.element_is_visible(self.locators.start_date(phase_name)).get_attribute('aria-label')
        end_date = self.element_is_visible(self.locators.end_date(phase_name)).get_attribute('aria-label')
        assert start_date and end_date == self.get_day_before(0), 'Длина фазы не равна текущему дню'

    @testit.step("Проверка статуса")
    @allure.step("Проверка статуса")
    def check_status(self, phase_name):
        self.element_is_visible(self.locators.CHECK_COLUMN_TAB).click()
        self.element_is_visible(self.locators.STATUS_COLUMN_CHECKBOX).click()
        self.action_esc()
        time.sleep(0.5)
        assert self.element_is_visible(self.locators.status(phase_name)).get_attribute('aria-label') == 'Планирование', \
            "Статус фазы не Планирование"
