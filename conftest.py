import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from data.data import LOGIN, PASSWORD
from pages.all_project_page import AllProjectPage
from pages.authorization_page import AuthorizationPage
from pages.create_project_drawer_page import CreateProjectDrawerPage

IN_URL = 'http://10.7.2.3:43000/'


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
    authorization_page.authorization(LOGIN, PASSWORD)
    return login


@pytest.fixture
def project(login, driver):
    create_project_drawer_page = CreateProjectDrawerPage(driver)
    create_project_drawer_page.go_to_create_project_drawer_from_menu()
    create_project_drawer_page.create_project('no')
    yield project
    all_project_page = AllProjectPage(driver)
    all_project_page.go_to_all_project_page()
    all_project_page.delete_project()

