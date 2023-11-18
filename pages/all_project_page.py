import time

import allure

from locators.all_project_page_locators import AllProjectPageLocators
from pages.base_page import BasePage


class AllProjectPage(BasePage):
    locators = AllProjectPageLocators()

    # Переходим через меню на страницу все проекты
    @allure.step("Переходим через меню на страницу все проекты")
    def go_to_all_project_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_PROJECTS))
        self.element_is_visible(self.locators.TAB_ALL_PROJECTS).click()

    # Проверяем, что имя проекта есть на странице
    @allure.step("Проверяем, что имя проекта есть на странице")
    def check_project_name_at_all(self):
        check_name_at_all = self.element_is_present(self.locators.CHECK_NAME_PROJECT).text
        return check_name_at_all

    # Получаем статус проекта
    @allure.step("Получаем статус проекта")
    def get_project_status_at_all(self):
        project_status_at_all = self.element_is_present(self.locators.PROJECT_STATUS_TEXT).text
        return project_status_at_all

    # Удаляем проект
    @allure.step("Удаляем проект")
    def delete_project(self):
        self.element_is_visible(self.locators.PROJECT_ACTION_BUTTON).click()
        self.element_is_visible(self.locators.PROJECT_DELETE_BUTTON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)#Если не поставить явное ожидание драйвер закроется раньше чем удалится проект

    # Включаем фильтр проект во всех стаусах
    @allure.step("Включаем фильтр проект во всех стаусах")
    def see_all_status_project(self):
        self.element_is_visible(self.locators.STATUS_FILTER_BUTTON).click()
        self.element_is_visible(self.locators.MARK_ALL_STATUS).click()