from locators.user_page_locators import UserPageLocators
from pages.base_page import BasePage


class UserPage(BasePage):
    locators = UserPageLocators()

    def check_user_last_name(self, last_name):
        self.go_to_element(self.locators.user_by_name(last_name))
        print(self.element_is_displayed(self.locators.user_by_name(last_name)))
        return self.element_is_displayed(self.locators.user_by_name(last_name))
