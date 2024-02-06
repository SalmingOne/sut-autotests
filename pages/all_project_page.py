import time

import allure
import testit
from selenium.webdriver.common.by import By

from locators.all_project_page_locators import AllProjectPageLocators
from pages.base_page import BasePage


class AllProjectPage(BasePage):
    locators = AllProjectPageLocators()

    @testit.step("Переходим через меню на страницу все проекты")
    @allure.step("Переходим через меню на страницу все проекты")
    def go_to_all_project_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_PROJECTS))
        self.element_is_visible(self.locators.TAB_ALL_PROJECTS).click()

    @testit.step("Проверяем, что имя проекта есть на странице")
    @allure.step("Проверяем, что имя проекта есть на странице")
    def check_project_name_at_all(self):
        check_name_at_all = self.element_is_present(self.locators.CHECK_NAME_PROJECT).text
        return check_name_at_all

    @testit.step("Получаем статус проекта")
    @allure.step("Получаем статус проекта")
    def get_project_status_at_all(self):
        project_status_at_all = self.element_is_present(self.locators.PROJECT_STATUS_TEXT).text
        return project_status_at_all

    @testit.step("Удаляем проект")
    @allure.step("Удаляем проект")
    def delete_project(self):

        self.element_is_visible(self.locators.PROJECT_ACTION_BUTTON).click()
        self.element_is_visible(self.locators.PROJECT_DELETE_BUTTON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)  # Если не поставить явное ожидание драйвер закроется раньше чем, удалится проект

    @testit.step("Включаем фильтр проект во всех статусах")
    @allure.step("Включаем фильтр проект во всех статусах")
    def see_all_status_project(self):
        time.sleep(1)
        self.element_is_visible(self.locators.STATUS_FILTER_BUTTON).click()
        self.element_is_visible(self.locators.MARK_ALL_STATUS).click()
        time.sleep(2)
        self.action_esc()
        time.sleep(1)

    @testit.step("Переходим на страницу проекта по имени")
    @allure.step("Переходим на страницу проекта по имени")
    def go_project_page(self, name):
        project_title = (By.XPATH, f'//div[@col-id="name"]//div[text()="{name}"]')
        self.element_is_visible(project_title).click()