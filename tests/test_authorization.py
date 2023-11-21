import allure

from data.data import LOGIN, PASSWORD
from pages.authorization_page import AuthorizationPage
from conftest import IN_URL


#@pytest.mark.smoke_test
@allure.suite("Страница авторизации")
class TestAuthorization:
    # id-16 4.1 Авторизация в системе
    @allure.title("id-16  4.1 Авторизация в системе")
    def test_correct_authorization(self, driver):
        authorization_page = AuthorizationPage(driver, IN_URL)
        authorization_page.open()
        authorization_page.authorization(LOGIN, PASSWORD)
        authorization_page.check_authorization()
