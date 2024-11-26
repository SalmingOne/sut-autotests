import time

import allure
import testit

from data.data import USER_NAME
from locators.resource_plane_locators import ResourcePlaneLocators
from pages.base_page import BasePage


class ResourcePlanePage(BasePage):
    locators = ResourcePlaneLocators()

    @testit.step("Переход на страницу Ресурсный план")
    @allure.step("Переход на страницу Ресурсный план")
    def go_to_resource_plane_page(self):
        time.sleep(0.3)
        self.action_move_to_element(self.element_is_visible(self.locators.PLANING_MORE))
        self.element_is_visible(self.locators.TAB_RESOURCE_PLANE).click()

    @testit.step("Проверка отображения архивного проекта")
    @allure.step("Проверка отображения архивного проекта")
    def check_archive_project(self, project_code):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.NOT_ACTIV_PROJECT_CHECKBOX).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        self.action_move_to_element(self.element_is_visible(self.locators.project_color_on_project(project_code), 30))
        name_color = self.element_is_visible(self.locators.project_color_on_project(project_code)).value_of_css_property('color')
        assert name_color == 'rgba(0, 0, 0, 0.12)', "Цвет проекта не серый"

    @testit.step("Проверка отображения архивного проекта по пользователям")
    @allure.step("Проверка отображения архивного проекта по пользователям")
    def check_project_color_on_user(self, project_code):
        self.action_move_to_element(self.element_is_visible(self.locators.project_color_on_user(project_code)))
        name_color = self.element_is_visible(self.locators.project_color_on_user(project_code)).value_of_css_property('color')
        assert name_color == 'rgba(0, 0, 0, 0.12)', "Цвет проекта не серый"

    @testit.step("Переходим на отображение таблицы по пользователю")
    @allure.step("Переходим на отображение таблицы по пользователю")
    def go_to_by_user_tab(self):
        self.element_is_visible(self.locators.BY_USER_BUTTON).click()

    @testit.step("Открываем список проектов пользователя")
    @allure.step("Открываем список проектов пользователя")
    def open_project_list(self):
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(USER_NAME)
        self.element_is_visible(self.locators.OPEN_PROJECT_LIST).click()
