import allure
import pytest
from data.data import LOGIN, PASSWORD
from pages.authorization_page import AuthorizationPage
from conftest import IN_URL


# @pytest.mark.smoke_test
@allure.suite("Страница авторизации")
class TestAuthorization:
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


class TestA:

    @pytest.mark.labor_reason("True")
    @pytest.mark.attach_files("True")
    @pytest.mark.project_status("ARCHIVED")
    def test_1(self, f_create_temp_project):
        code = 1
        test = f_create_temp_project
        assert test == 0