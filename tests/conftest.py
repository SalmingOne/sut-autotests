import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.authorization_page import AuthorizationPage

IN_URL = 'http://10.7.2.3:38221/'


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    authorization_page = AuthorizationPage(driver, IN_URL)
    authorization_page.open()
    authorization_page.authorization('admin', 'password')
    return login
