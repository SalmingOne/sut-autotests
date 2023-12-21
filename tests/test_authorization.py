import time

import allure
import pytest
from data.data import LOGIN, PASSWORD
from pages.authorization_page import AuthorizationPage
from conftest import IN_URL


@allure.suite("Страница авторизации")
class TestAuthorization:
    @pytest.mark.tryfirst
    def test_for_token(self, f_create_temp_project, f_auth, driver):
        time.sleep(0.2)  # ожидание для перезаписи токена
        print('прошел тест для получения токена')

    # id-16 4.1 Авторизация в системе
    @allure.title("id-16  4.1 Авторизация в системе")
    def test_correct_authorization(self, driver):
        authorization_page = AuthorizationPage(driver, IN_URL)
        authorization_page.open()
        authorization_page.authorization(LOGIN, PASSWORD)
        authorization_page.check_authorization()

    # id-901 4.1 Вход с вводом символов в разном регистре
    @allure.title("id-901  4.1 Вход с вводом символов в разном регистре")
    def test_correct_mixed_authorization(self, driver):
        authorization_page = AuthorizationPage(driver, IN_URL)
        authorization_page.open()
        authorization_page.authorization("ADMin", PASSWORD)
        authorization_page.check_authorization()
