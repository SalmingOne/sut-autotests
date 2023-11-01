from pages.authorization_page import AuthorizationPage


class TestAuthorization:
    def test_correct_authorization(self, driver):
        authorization_page = AuthorizationPage(driver, ' http://10.7.2.3:46041/')
        authorization_page.open()
        authorization_page.authorization('admin', 'password')
