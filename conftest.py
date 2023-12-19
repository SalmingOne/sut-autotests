import time

import pytest
import requests
from requests import Response
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from data.data import LOGIN, PASSWORD
from pages.all_project_page import AllProjectPage
from pages.authorization_page import AuthorizationPage
from pages.create_project_drawer_page import CreateProjectDrawerPage
from configuration.config_provider import ConfigProvider
from api_methods.project import ProjectApi

IN_URL = 'http://10.7.2.3:43091/'
config = ConfigProvider()


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


@pytest.fixture
def f_auth() -> dict:

    response = requests.post(
        url=config.get_auth_url(),
        json=config.get_admin_creds()
    )

    return {"Access": "Bearer " + response.json()["accessToken"]}


@pytest.fixture
def f_create_temp_project(request) -> Response:
    """ Создаёт временный проект удаляемый по окончанию теста """

    try:
        status = request.node.get_closest_marker("project_status").args[0]
    except AttributeError:
        status = "ACTIVE"
    try:
        laborReasons = bool(request.node.get_closest_marker("labor_reason"))
    except AttributeError:
        laborReasons = False
    try:
        mandatoryAttachFiles = bool(request.node.get_closest_marker("atach_files"))
    except AttributeError:
        mandatoryAttachFiles = False
    
    project_api = ProjectApi()
    response = project_api.create_project(
        status=status,
        laborReasons=laborReasons,
        mandatoryAttachFiles=mandatoryAttachFiles)
    yield response

    project_api.delete_project(response["id"])
