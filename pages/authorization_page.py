import allure
from locators.authorization_locators import AuthorizationPageLocators
from pages.base_page import BasePage


class AuthorizationPage(BasePage):
    locators = AuthorizationPageLocators()

    @allure.step("Авторизация в системе")
    def authorization(self, login, password):
        self.element_is_visible(self.locators.LOGIN_FIELD).send_keys(login)
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(password)
        self.element_is_visible(self.locators.IN_BUTTON).click()

    @allure.step("Проверка что пользователь авторизовался")
    def check_authorization(self):
        assert self.element_is_visible(self.locators.ACTIVITY_CHECK).text == "Активность", "Пользователь не авторизовался"

    @allure.step("Выход пользователя из системы")
    def logout(self):
        self.element_is_visible(self.locators.PROFILE_BUTTON).click()
        self.element_is_visible(self.locators.OUT_BUTTON).click()

    @allure.step("Выход пользователя из системы")
    def check_logout(self):
        assert self.element_is_displayed(self.locators.LOGIN_FIELD), "Пользователь не вышел из системы"
