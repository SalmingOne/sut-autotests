import time

import allure
import pytest
import testit

from data.data import LOGIN, PASSWORD
from pages.authorization_page import AuthorizationPage
from conftest import IN_URL


@allure.suite("Страница авторизации")
class TestAuthorization:

    @testit.workItemIds(16)
    @testit.displayName("Авторизация в системе")
    @pytest.mark.smoke
    @allure.title("id-16  4.1 Авторизация в системе")
    def test_correct_authorization(self, driver):
        authorization_page = AuthorizationPage(driver, IN_URL)
        authorization_page.open()
        authorization_page.authorization(LOGIN, PASSWORD)
        authorization_page.check_authorization()

    @testit.workItemIds(901)
    @testit.displayName("4.1 Вход с вводом символов в разном регистре")
    @pytest.mark.regress
    @allure.title("id-901  4.1 Вход с вводом символов в разном регистре")
    def test_correct_mixed_authorization(self, driver):
        authorization_page = AuthorizationPage(driver, IN_URL)
        authorization_page.open()
        authorization_page.authorization("ADMin", PASSWORD)
        authorization_page.check_authorization()

    @testit.workItemIds(1378)
    @testit.displayName("4.10. Выход пользователя из системы")
    @pytest.mark.smoke
    @allure.title("id-1378  4.10. Выход пользователя из системы")
    def test_user_logout(self, login, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.logout()
        authorization_page.check_logout()
