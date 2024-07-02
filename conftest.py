import pytest
import requests
from requests import Response
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from api_methods.departmens import DepartmentsApi
from api_methods.position import PositionsApi
from api_methods.project_roles import ProjectRolesApi
from data.data import LOGIN, PASSWORD, USER_ID
from data.models.create_project_model import CreateProject
from data.urls import Urls
from endpoints.affiliates_endpoint import AffiliatesEndpoint
from endpoints.assignments_endpoint import AssignmentEndpoint
from endpoints.auth_endpoint import AuthEndpoint
from endpoints.labor_reports_endpoint import LaborReportEndpoint
from endpoints.logs_endpoint import LogsEndpoint
from endpoints.project_endpoint import ProjectEndpoint
from endpoints.search_profile_endpoint import SearchProfileEndpoint
from endpoints.skills_endpoint import SkillsEndpoint
from endpoints.tags_endpoint import TagsEndpoint
from endpoints.users_endpoint import UserEndpoint
from endpoints.variables_endpoint import VariablesEndpoint
from pages.authorization_page import AuthorizationPage
from pages.base_page import BasePage
from api_methods.system_settings import SystemSettingsApi


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    authorization_page = AuthorizationPage(driver, Urls.base_url)
    authorization_page.open()
    authorization_page.authorization(LOGIN, PASSWORD)
    return login


@pytest.fixture()
def simple_project():
    project_endpoint = ProjectEndpoint()
    payload = CreateProject().model_dump()
    response = project_endpoint.create_project_api(json=payload)
    yield response.json()
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def project_with_labor_reason():
    project_endpoint = ProjectEndpoint()
    payload = CreateProject(
        laborReasons=True
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    payload = dict(projectRoleId=1,
                   projectId=response.json()["id"],
                   slotId=response.json()["slots"][0]["assignments"][0]['slotId'],
                   userId=USER_ID,
                   isProjectManager=True,
                   startDate=CreateProject().startDate
                   )
    assignment_endpoint = AssignmentEndpoint()
    assignment_endpoint.put_assignment_api(
        json=payload,
        assignment_id=str(response.json()["slots"][0]["assignments"][0]["id"])
    )
    yield response.json()
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def project_with_attach_files():
    project_endpoint = ProjectEndpoint()
    payload = CreateProject(
        mandatoryAttachFiles=True
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    yield response.json()
    project_endpoint.delete_project_api(str(response.json()['id']))


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


@pytest.fixture(scope='session')
def script():
    project_roles = ProjectRolesApi()
    header = AuthEndpoint().get_header_token_api()
    logs_endpoint = LogsEndpoint()
    payload = dict(status=True, level="ALL", depthDateQuantity=0, depthDateType="YEAR")
    logs_endpoint.post_logs_settings(json=payload)
    if project_roles.get_project_roles_api(header) == 0:
        project_roles.post_project_roles_api(header)
    else:
        pass
    departments = DepartmentsApi()
    if departments.get_departments_api(header) == 0:
        departments.post_department_api(header)
    else:
        pass
    positions = PositionsApi()
    if positions.get_positions_api(header) == 0:
        positions.post_positions_api(header)
    else:
        pass
    filial_endpoint = AffiliatesEndpoint()
    if len(filial_endpoint.get_all_affiliates_api().json()) == 0:
        payload = dict(name="Саратовский филиал", address='г. Саратов')
        filial_endpoint.create_affiliates_api(json=payload)
    else:
        pass


@pytest.fixture()
def finished_project():
    project_endpoint = ProjectEndpoint()
    payload = CreateProject(
        endDate=BasePage(driver=None).get_day_before_m_d_y(1)
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)

    yield
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def project_with_overtime_work():
    labor_report_endpoint = LaborReportEndpoint()
    project_endpoint = ProjectEndpoint()
    payload = CreateProject().model_dump()
    res = project_endpoint.create_project_api(json=payload)
    project_id = res.json()['id']
    payload = [dict(
        date=BasePage(driver=None).get_day_before_m_d_y(0),
        projectId=project_id,
        overtimeWork=3,
        hours=3,
        type="DEFAULT",
        userId=USER_ID
    )]
    labor_report_endpoint.post_labor_report_api(json=payload)
    yield
    project_endpoint.delete_project_api(str(project_id))


@pytest.fixture()
def variables():
    variables_endpoints = VariablesEndpoint()
    payload = dict(name='Не уникальное имя', systemName='Не уникальное системное имя')
    response = variables_endpoints.create_variables_api(json=payload)
    yield payload['name'], payload['systemName']
    variables_endpoints.delete_variables_api(str(response.json()['id']))


@pytest.fixture()
def logging_off():
    logs_endpoint = LogsEndpoint()
    payload = dict(status=False, level="ALL", depthDateQuantity=0, depthDateType="YEAR")
    logs_endpoint.post_logs_settings(json=payload)


@pytest.fixture()
def logging_on():
    logs_endpoint = LogsEndpoint()
    payload = dict(status=True, level="ALL", depthDateQuantity=0, depthDateType="YEAR")
    logs_endpoint.post_logs_settings(json=payload)


@pytest.fixture()
def skills():
    skills_endpoint = SkillsEndpoint()
    if skills_endpoint.return_len_skills() >= 2:
        pass
    else:
        payload = dict(name='Selenium', tags=[])
        skills_endpoint.create_skills_api(json=payload)
        payload = dict(name='Pytest', tags=[])
        skills_endpoint.create_skills_api(json=payload)


@pytest.fixture()
def create_skill():
    skills_endpoint = SkillsEndpoint()
    payload = dict(name='ABCD', tags=[])
    response = skills_endpoint.create_skills_api(json=payload)
    yield payload['name']
    skills_endpoint.delete_skill_api(str(response.json()['id']))


@pytest.fixture()
def project_with_assignment():
    assignment_endpoint = AssignmentEndpoint()
    project_endpoint = ProjectEndpoint()
    payload = CreateProject().model_dump()
    response = project_endpoint.create_project_api(json=payload)
    payload = dict(projectRoleId=1,
                   projectId=response.json()["id"],
                   slotId=response.json()["slots"][0]["assignments"][0]['slotId'],
                   userId=USER_ID,
                   isProjectManager=True,
                   startDate=CreateProject().startDate
                   )
    assignment_endpoint.put_assignment_api(
        json=payload,
        assignment_id=str(response.json()["slots"][0]["assignments"][0]["id"])
    )
    yield
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def create_tag():
    tags_endpoint = TagsEndpoint()
    payload = dict(name='ABSENT', skills=[])
    response = tags_endpoint.create_tag_api(json=payload)
    yield payload['name']
    tags_endpoint.delete_tag_api(str(response.json()['id']))


@pytest.fixture()
def create_filial():
    filial_endpoint = AffiliatesEndpoint()
    payload = dict(name='Для редактирования', address='г. Москва')
    response = filial_endpoint.create_affiliates_api(json=payload)
    yield payload['name']
    filial_endpoint.delete_affiliates_api(str(response.json()['id']))


@pytest.fixture()
def create_work_user():
    user_endpoint = UserEndpoint()
    project_endpoint = ProjectEndpoint()
    first_project_id = project_endpoint.get_all_project().json()[0]['id']
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    payload = dict(username="AutoTester1",
                   name="Автомат",
                   secondName="АвтоСПроектом",
                   gender="MALE",
                   phone="",
                   email="auto_testt@mail.rruu",
                   hourlyWage=False,
                   startWorkDate="2024-04-11",
                   userAssignments=[dict(
                       projectId=first_project_id,
                       projectRoleId=1,
                       isProjectManager=False
                   )
                   ],
                   projectRoleIds=[1],
                   postId=1,
                   departmentId=1,
                   systemRoleIds=[1]
                   )
    if user_id is None:
        response = user_endpoint.create_user_api(json=payload)
        print(response.status_code)
    else:
        response = user_endpoint.change_user(user_id=str(user_id), json=payload)
        print(response.status_code)


@pytest.fixture()
def create_fired_user():
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_test@mail.ruru')
    payload = dict(username="AutoTester",
                   name="Автомат",
                   secondName="Автотестов",
                   gender="MALE",
                   phone="",
                   email="auto_test@mail.ruru",
                   hourlyWage=False,
                   startWorkDate="2024-04-11",
                   dismissalDate="2024-05-11",
                   userAssignments=[],
                   projectRoleIds=[1],
                   postId=1,
                   departmentId=1,
                   systemRoleIds=[1]
                   )
    if user_id is None:
        response = user_endpoint.create_user_api(json=payload)
        print(response.status_code)
    else:
        response = user_endpoint.change_user(user_id=str(user_id), json=payload)
        print(response.status_code)


@pytest.fixture(scope='session', autouse=True)
def write_user_creds_file():
    user_endpoint = UserEndpoint()
    user_endpoint.write_user_id_and_name_to_file(LOGIN)


@pytest.fixture()
def create_advanced_search():
    advanced_search = SearchProfileEndpoint()
    payload = dict(
        userId=USER_ID,
        title='Автопоиск',
        query="{\"rules\":[{\"field\":\"status\",\"value\":\"WORK\",\"operator\":\"in\"}],\"combinator\":\"and\"}"
    )
    response = advanced_search.create_advanced_search_api(json=payload)
    yield payload['title']
    advanced_search.delete_advanced_search_api(str(response.json()['id']))


@pytest.fixture()
def advanced_search_to_delete():
    advanced_search = SearchProfileEndpoint()
    payload = dict(
        userId=USER_ID,
        title='Для удаления',
        query="{\"rules\":[{\"field\":\"status\",\"value\":\"WORK\",\"operator\":\"in\"}],\"combinator\":\"and\"}"
    )
    advanced_search.create_advanced_search_api(json=payload)
    yield payload['title']
