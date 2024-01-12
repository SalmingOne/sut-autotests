import allure
from locators.user_page_locators import UserPageLocators
from pages.base_page import BasePage


class UserPage(BasePage):
    locators = UserPageLocators()

    @allure.step("Проверяем есть ли пользователь в таблице")
    def check_user_is_not_in_table(self, last_name):
        self.elements_are_visible(self.locators.SEARCH_TAB_FIELDS)[1].send_keys(f'{last_name}')
        return self.element_is_displayed(self.locators.USER_KEBABS)


