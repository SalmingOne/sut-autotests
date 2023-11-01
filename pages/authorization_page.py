import time

from locators.authorization_locators import AuthorizationPageLocators
from pages.base_page import BasePage


class AuthorizationPage(BasePage):
    locators = AuthorizationPageLocators()

    def authorization(self, login, password):
        self.element_is_visible(self.locators.LOGIN_FIELD).send_keys(login)
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(password)
        self.element_is_visible(self.locators.IN_BUTTON).click()
        time.sleep(5)
