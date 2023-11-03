import time

from selenium.webdriver import Keys

from locators.create_project_drawer_locators import CreateProjectDrawerLocators
from pages.base_page import BasePage


class CreateProjectDrawerPage(BasePage):
    locators = CreateProjectDrawerLocators()

    def go_to_create_project_drawer_from_menu(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_PROJECTS))
        self.element_is_visible(self.locators.TAB_CREATE_PROJECT).click()
        # time.sleep(3)

    def create_project(self):
        self.element_is_visible(self.locators.PROJECT_NAME_FIELD).send_keys('AutoTestProject')
        self.element_is_visible(self.locators.PROJECT_CODE_FIELD).send_keys('ATP')
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).click()
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys('01.10.2023')
        self.element_is_visible(self.locators.PROJECT_RECOURSE_FIELD).send_keys('АДМИНИСТРАТОР АДМИНИСТРАТОР')
        time.sleep(3)
        self.element_is_visible(self.locators.CHOSE_RECOURSE).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
