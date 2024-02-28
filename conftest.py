import pytest
import requests
from requests import Response
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from api_methods.affiliates import AffiliatesApi
from api_methods.auth import AuthApi
from api_methods.departmens import DepartmentsApi
from api_methods.position import PositionsApi
from api_methods.project_roles import ProjectRolesApi
from data.data import LOGIN, PASSWORD
from pages.all_project_page import AllProjectPage
from pages.authorization_page import AuthorizationPage
from pages.create_project_drawer_page import CreateProjectDrawerPage
from configuration.config_provider import ConfigProvider
from api_methods.project import ProjectApi
from api_methods.system_settings import SystemSettingsApi

IN_URL = 'http://10.7.2.3:32901/'
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
        mandatoryAttachFiles = bool(request.node.get_closest_marker("attach_files"))
    except AttributeError:
        mandatoryAttachFiles = False

    project_api = ProjectApi()
    response = project_api.create_project(
        status=status,
        laborReasons=laborReasons,
        mandatoryAttachFiles=mandatoryAttachFiles)
    yield response

    project_api.delete_project(response["id"])


@pytest.fixture
def f_overtime_reason_requirement():
    sys_settings = SystemSettingsApi()
    sys_settings.turn_on_required_overwork_reason()
    yield
    sys_settings.turn_off_required_overwork_reason()


@pytest.fixture
def f_show_onboarding():
    sys_settings = SystemSettingsApi()
    sys_settings.turn_on_show_onboarding()
    yield
    sys_settings.turn_off_show_onboarding()


@pytest.fixture
def f_notifications():
    sys_settings = SystemSettingsApi()
    sys_settings.turn_on_notifications()
    yield
    sys_settings.turn_off_notifications()


@pytest.fixture
def token_auth():
    auth_api = AuthApi()
    x = auth_api.auth_to_token()
    print(x)


@pytest.fixture(scope='session', autouse=True)
def script():
    project_roles = ProjectRolesApi()
    token = AuthApi().auth_to_token()
    if project_roles.get_project_roles_api(token) == 0:
        project_roles.post_project_roles_api(token)
    else:
        pass
    departments = DepartmentsApi()
    if departments.get_departments_api(token) == 0:
        departments.post_department_api(token)
    else:
        pass
    positions = PositionsApi()
    if positions.get_positions_api(token) == 0:
        positions.post_positions_api(token)
    else:
        pass
    affiliates = AffiliatesApi()
    if affiliates.get_affiliates_api(token) == 0:
        affiliates.post_affiliates_api(token)
    else:
        pass


