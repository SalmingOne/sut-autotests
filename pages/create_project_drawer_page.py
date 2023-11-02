from locators.create_project_drawer_locators import CreateProjectDrawerLocators
from pages.base_page import BasePage


class CreateProjectDrawerPage(BasePage):
    locators = CreateProjectDrawerLocators()

    def go_to_create_project_drawer_from_menu(self):
        self.go_to_element(self.locators.TAB_PROJECTS)
        self.element_is_visible(self.locators.TAB_CREATE_PROJECT).click()
