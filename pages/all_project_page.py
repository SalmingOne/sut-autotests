from locators.all_project_page_locators import AllProjectPageLocators
from pages.base_page import BasePage


class AllProjectPage(BasePage):
    locators = AllProjectPageLocators()

    def go_to_all_project_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_PROJECTS))
        self.element_is_visible(self.locators.TAB_ALL_PROJECTS).click()

    def check_project_name_at_all(self):
        check_name_at_all = self.element_is_present(self.locators.CHECK_NAME_PROJECT).text
        print(check_name_at_all)
        return check_name_at_all

    def delete_project(self):
        self.element_is_visible(self.locators.PROJECT_ACTION_BUTTON).click()
        self.element_is_visible(self.locators.PROJECT_DELETE_BUTTON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()






