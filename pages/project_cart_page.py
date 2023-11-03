from locators.project_cart_locators import ProjectCardLocators
from pages.base_page import BasePage


class ProjectCardPage(BasePage):
    locators = ProjectCardLocators()

    def go_to_description_tab(self):
        self.element_is_visible(self.locators.DESCRIPTION_TAB).click()

    def get_project_name(self):


