import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from data.data import LOGIN, PASSWORD, USER_ID, USER_NAME, PROJECT_NAME
from data.models.create_project_model import CreateProject
from data.urls import Urls
from endpoints.affiliates_endpoint import AffiliatesEndpoint
from endpoints.assignments_endpoint import AssignmentEndpoint
from endpoints.departmens_endpoint import DepartmentsEndpoint
from endpoints.gantt_endpoint import GanttEndpoint
from endpoints.labor_reports_endpoint import LaborReportEndpoint
from endpoints.logs_endpoint import LogsEndpoint
from endpoints.posts_endpoint import PostsEndpoint
from endpoints.project_endpoint import ProjectEndpoint
from endpoints.project_roles_endpoint import ProjectRolesEndpoint
from endpoints.resume_endpoint import ResumeEndpoint
from endpoints.search_profile_endpoint import SearchProfileEndpoint
from endpoints.skills_endpoint import SkillsEndpoint
from endpoints.system_roles_endpoint import SystemRolesEndpoint

from endpoints.users_endpoint import UserEndpoint
from endpoints.calendar_endpoint import CalendarEndpoint
from endpoints.variables_endpoint import VariablesEndpoint
from pages.authorization_page import AuthorizationPage
from pages.base_page import BasePage
from api_methods.system_settings import SystemSettingsApi


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    # Раскомментировать при запуске втемную
    #options.add_argument("--headless")
    #options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=ChromeService(), options=options)
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
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject().model_dump()
    response = project_endpoint.create_project_api(json=payload)
    yield response.json()
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def archive_project():
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        status='ARCHIVED'
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    yield response.json()
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def simple_project_to_delete():
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject().model_dump()
    response = project_endpoint.create_project_api(json=payload)
    yield response.json()
    if project_endpoint.check_project_by_id(str(response.json()['id'])):
        project_endpoint.delete_project_api(str(response.json()['id']))
    else:
        pass


@pytest.fixture()
def second_project():
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist('SecondProject')
    payload = CreateProject(
        code='SECP',
        name='SecondProject'
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    yield response.json()
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def no_resources_project():
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        resources=[]
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    yield response.json()
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def project_with_labor_reason():
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    project_endpoint = ProjectEndpoint()
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        laborReasons=True,
        resources=[dict(
            projectRoleId=1,
            userId=user_id,
            isProjectManager=True
        )
        ]
    ).model_dump()
    res = project_endpoint.create_project_api(json=payload)
    payload = dict(projectRoleId=1,
                   projectId=res.json()["id"],
                   userId=USER_ID,
                   isProjectManager=True,
                   startDate=CreateProject().startDate
                   )
    assignment_endpoint = AssignmentEndpoint()
    assignment_endpoint.create_assignment_api(json=payload)
    yield res.json()
    project_endpoint.delete_project_api(str(res.json()['id']))


@pytest.fixture()
def project_with_attach_files():
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        mandatoryAttachFiles=True
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    yield response.json()
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def project_with_two_resources(create_work_user):
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    payload = CreateProject(
        resources=[
            dict(
                projectRoleId=3,
                userId=USER_ID,
                isProjectManager=False
            ),
            dict(
                projectRoleId=3,
                userId=user_id,
                isProjectManager=False
            )
        ]
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


@pytest.fixture()
def finished_project():
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        endDate=BasePage(driver=None).get_day_before_m_d_y(1)
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    yield
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def short_project():
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    start_date = BasePage(driver=None).get_day_before_m_d_y(0)
    end_date = BasePage(driver=None).get_day_before_m_d_y(-15)
    start_date = BasePage(driver=None).check_and_replace_start_date(start_date)
    payload = CreateProject(
        startDate=start_date,
        endDate=end_date
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    yield response.json()
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def project_with_overtime_work():
    labor_report_endpoint = LaborReportEndpoint()
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    project_endpoint = ProjectEndpoint()
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        resources=[dict(
            projectRoleId=1,
            userId=user_id,
            isProjectManager=True
        )
        ]
    ).model_dump()
    res = project_endpoint.create_project_api(json=payload)
    payload = dict(projectRoleId=1,
                   projectId=res.json()["id"],
                   userId=USER_ID,
                   isProjectManager=True,
                   startDate=CreateProject().startDate
                   )
    assignment_endpoint = AssignmentEndpoint()
    assignment_endpoint.create_assignment_api(json=payload)

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
    yield res.json()
    project_endpoint.delete_project_api(str(project_id))


@pytest.fixture()
def project_with_rejected_labor_report():
    labor_report_endpoint = LaborReportEndpoint()
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        resources=[dict(
            projectRoleId=1,
            userId=USER_ID,
            isProjectManager=True
        )]
    ).model_dump()
    res = project_endpoint.create_project_api(json=payload)
    payload = [
        dict(
            hours=3,
            date=BasePage(driver=None).get_day_after_ymd(0),
            type="OTW",
            userId=USER_ID,
            projectId=res.json()["id"],
        )
    ]
    labor_report_endpoint.post_labor_report_api(json=payload)
    rejection_reason = 'Просто так'
    ids = labor_report_endpoint.get_labor_reports_by_project_api(str(res.json()["id"]),
                                                                 BasePage(driver=None).get_day_before_ymd(1),
                                                                 BasePage(driver=None).get_day_before_ymd(0))
    payload = [
        dict(
            ids=ids,
            rejectionReason=rejection_reason,
            approvalStatus='REJECTED',
        )
    ]
    number_day = BasePage(driver=None).get_day_after_ymd(1).split('-')[2]
    labor_report_endpoint.put_labor_reports(json=payload)
    yield res.json(), number_day, rejection_reason
    project_endpoint.delete_project_api(str(res.json()["id"]))

@pytest.fixture()
def project_with_stopped_task():
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        resources=[dict(
            projectRoleId=1,
            userId=USER_ID,
            isProjectManager=True
        )]
    ).model_dump()
    res = project_endpoint.create_project_api(json=payload)
    project_id = res.json()['id']
    gantt_endpoint = GanttEndpoint()
    gantt_endpoint.start_editing(project_id)

    start_date, end_date = [day.strftime("%m.%d.%Y") for day in BasePage(driver=None).get_current_week_start_end()]
    payload = dict(
        stages=[
                dict(
                name='Auto',
                id=1
            )
        ],
        tasks=[
            dict(
                name='Auto',
                id=1,
                parentId=1,
                slotsTasks=[
                    dict(
                        employmentPercentage=12.5,
                        endDate=end_date,
                        id=1,
                        slotId=res.json()['slots'][0]['id'],
                        startDate=start_date
                    )
                ],
            startDate=start_date,
            endDate=end_date
            )
        ],
        links=[]
    )
    gantt_endpoint.create_task(project_id, json=payload)

    tasks = gantt_endpoint.get_all_tasks(project_id).json()
    parentId = tasks[0]['parentId']
    taskId = tasks[0]['id']
    taskName = tasks[0]['name']

    payload = dict(
                status="IN_PROGRESS",
                changeDate=start_date
        )

    gantt_endpoint.change_stage_status(parentId, payload)
    gantt_endpoint.change_task_status(taskId, payload)

    payload = dict(
        status="STOPPED",
        changeDate=start_date
    )
    gantt_endpoint.change_task_status(taskId, payload)
    number_day = BasePage(driver=None).get_day_after_ymd(1).split('-')[2]

    yield res.json(), number_day, taskName
    project_endpoint.delete_project_api(str(project_id))

@pytest.fixture()
def delete_created_project():
    yield
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_by_name_api("AutoTestProject1")


@pytest.fixture()
def delete_created_draft_project():
    yield
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_by_name_api("AutoTestProjectDraft")


@pytest.fixture()
def delete_created_reason_project():
    yield
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_by_name_api("AutoTestProjectReason")


@pytest.fixture()
def project_with_work_and_overtime_work():
    labor_report_endpoint = LaborReportEndpoint()
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject().model_dump()
    res = project_endpoint.create_project_api(json=payload)
    project_id = res.json()['id']
    payload = [
        dict(
            date=BasePage(driver=None).get_day_before_m_d_y(-1),
            projectId=project_id,
            hours=6,
            type="DEFAULT",
            userId=USER_ID
        ),
        dict(
            date=BasePage(driver=None).get_day_before_m_d_y(-2),
            projectId=project_id,
            overtimeWork=3,
            hours=8,
            type="DEFAULT",
            userId=USER_ID
        )
    ]
    labor_report_endpoint.post_labor_report_api(json=payload)
    yield res.json()
    project_endpoint.delete_project_api(str(project_id))


@pytest.fixture()
def project_with_three_overtime_work():
    labor_report_endpoint = LaborReportEndpoint()
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject().model_dump()
    res = project_endpoint.create_project_api(json=payload)
    project_id = res.json()['id']
    payload = [
        dict(
            date=BasePage(driver=None).get_day_before_m_d_y(0),
            projectId=project_id,
            overtimeWork=3,
            hours=3,
            type="OTW",
            userId=USER_ID
        )
    ]
    labor_report_endpoint.post_labor_report_api(json=payload)
    payload = [
        dict(
            date=BasePage(driver=None).get_day_before_m_d_y(-7),
            projectId=project_id,
            overtimeWork=3,
            hours=3,
            type="OTW",
            userId=USER_ID
        )
    ]
    labor_report_endpoint.post_labor_report_api(json=payload)
    payload = [
        dict(
            date=BasePage(driver=None).get_day_before_m_d_y(-14),
            projectId=project_id,
            overtimeWork=3,
            hours=3,
            type="OTW",
            userId=USER_ID,
            overtimeApprovalStatus="REJECTED",
            overtimeRejectionReason="У нас не перерабатывают"

        )
    ]
    labor_report_endpoint.post_labor_report_api(json=payload)
    labor_ids = sorted(labor_report_endpoint.get_labor_reports_by_project_api(str(project_id),
                                                                       BasePage(driver=None).get_day_before_ymd(1),
                                                                       BasePage(driver=None).get_day_before_ymd(-30)))
    payload = [
        dict(
            ids=[labor_ids[1]],
            approvalStatus="APPROVED"
        ),
        dict(
            ids=[labor_ids[2]],
            rejectionReason="Сотрудник не работал в этот день",
            approvalStatus="REJECTED",
            overtimeApprovalStatus="REJECTED",
            overtimeRejectionReason="У нас не перерабатывают"

        )
    ]
    a = labor_report_endpoint.put_labor_reports(json=payload)
    yield res.json()
    project_endpoint.delete_project_api(str(project_id))


@pytest.fixture()
def project_with_work():
    labor_report_endpoint = LaborReportEndpoint()
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject().model_dump()
    res = project_endpoint.create_project_api(json=payload)
    project_id = res.json()['id']
    payload = [dict(
        date=BasePage(driver=None).get_day_before_m_d_y(0),
        projectId=project_id,
        hours=3,
        type="DEFAULT",
        userId=USER_ID
    )]
    labor_report_endpoint.post_labor_report_api(json=payload)
    yield res.json()
    project_endpoint.delete_project_api(str(project_id))


@pytest.fixture()
def variable_not_unique():
    variables_endpoints = VariablesEndpoint()
    payload = dict(name='Не уникальное имя', systemName='Не уникальное системное имя')
    response = variables_endpoints.create_variables_api(json=payload)
    yield payload['name'], payload['systemName']
    variables_endpoints.delete_variables_api(str(response.json()['id']))


@pytest.fixture()
def variable_for_edit():
    variables_endpoints = VariablesEndpoint()
    payload = dict(name='Для редактирования', systemName='Для редактирования', value='Для редактирования')
    response = variables_endpoints.create_variables_api(json=payload)
    yield payload['name'], payload['systemName'], payload['value']
    variables_endpoints.delete_variables_api(str(response.json()['id']))

@pytest.fixture()
def variable_for_delete():
    variables_endpoints = VariablesEndpoint()
    payload = dict(name='Для удаления', systemName='Для удаления', value='Для удаления')
    response = variables_endpoints.create_variables_api(json=payload)
    yield payload['name'], payload['systemName'], payload['value']
    if any(variable["name"] == payload["name"] for variable in variables_endpoints.get_all_variables().json()):
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
def create_second_skill():
    skills_endpoint = SkillsEndpoint()
    payload = dict(name='AABBCCDD', tags=[])
    response = skills_endpoint.create_skills_api(json=payload)
    yield payload['name']
    skills_endpoint.delete_skill_api(str(response.json()['id']))


@pytest.fixture()
def create_skill_to_delete():
    skills_endpoint = SkillsEndpoint()
    payload = dict(name='ABCD', tags=[])
    response = skills_endpoint.create_skills_api(json=payload)
    yield payload['name']
    if skills_endpoint.check_skill_by_id(str(response.json()['id'])):
        skills_endpoint.delete_skill_api(str(response.json()['id']))
    else:
        pass


@pytest.fixture()
def project_with_assignment():
    project_endpoint = ProjectEndpoint()
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        resources=[dict(
            projectRoleId=1,
            userId=user_id,
            isProjectManager=True
        )
        ]
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    payload = dict(projectRoleId=1,
                   projectId=response.json()["id"],
                   userId=USER_ID,
                   isProjectManager=True,
                   startDate=CreateProject().startDate
                   )
    assignment_endpoint = AssignmentEndpoint()
    assignment_endpoint.create_assignment_api(json=payload)
    yield
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def archive_project_with_assignment():
    project_endpoint = ProjectEndpoint()
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        status='ARCHIVED',
        resources=[dict(
            projectRoleId=1,
            userId=user_id,
            isProjectManager=True
        )
        ]
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    payload = dict(projectRoleId=1,
                   projectId=response.json()["id"],
                   userId=USER_ID,
                   isProjectManager=True,
                   startDate=CreateProject().startDate
                   )
    assignment_endpoint = AssignmentEndpoint()
    assignment_endpoint.create_assignment_api(json=payload)
    yield response.json()
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def project_with_assignment_not_current_manager(create_work_user):
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    payload = CreateProject(
        resources=[dict(
            projectRoleId=1,
            userId=user_id,
            isProjectManager=True
        )
        ]
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    yield response.json()
    project_endpoint.delete_project_api(str(response.json()['id']))


@pytest.fixture()
def create_filial():
    filial_endpoint = AffiliatesEndpoint()
    payload = dict(name='Для редактирования', address='г. Москва')
    response = filial_endpoint.create_affiliates_api(json=payload)
    yield payload['name']
    filial_endpoint.delete_affiliates_api(str(response.json()['id']))


@pytest.fixture()
def create_filial_to_delete():
    filial_endpoint = AffiliatesEndpoint()
    payload = dict(name='Для удаления', address='г. Москва')
    response = filial_endpoint.create_affiliates_api(json=payload)
    yield
    filial_endpoint.delete_filial_if_it_exist('Для удаления')


@pytest.fixture()
def delete_filial_after():
    yield
    filial_endpoint = AffiliatesEndpoint()
    filial_endpoint.delete_filial_by_name_api('Центральный филиал')


@pytest.fixture()
def create_work_user():
    user_endpoint = UserEndpoint()
    project_endpoint = ProjectEndpoint()
    department_endpoint = DepartmentsEndpoint()
    post_endpoint = PostsEndpoint()
    project_roles_endpoint = ProjectRolesEndpoint()
    system_roles_endpoint = SystemRolesEndpoint()
    first_system_role_id = system_roles_endpoint.get_user_system_role_id()
    first_project_role_id = project_roles_endpoint.get_all_project_roles_id()[1]
    first_post_id = post_endpoint.get_all_posts_id()[1]
    first_department_id = department_endpoint.get_all_departments_id()[1]
    first_project_id = project_endpoint.get_all_project().json()[3]['id']
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
                       projectRoleId=first_project_role_id,
                       isProjectManager=False
                   )
                   ],

                   projectRoleIds=[first_project_role_id],
                   postId=first_post_id,
                   departmentId=first_department_id,
                   systemRoleIds=[first_system_role_id]
                   )
    if user_id is None:
        response = user_endpoint.create_user_api(json=payload)
        print(response.status_code)
    else:
        response = user_endpoint.change_user(user_id=str(user_id), json=payload)
        print(response.status_code)
    return payload["secondName"]


@pytest.fixture()
def create_fired_user():
    user_endpoint = UserEndpoint()
    department_endpoint = DepartmentsEndpoint()
    post_endpoint = PostsEndpoint()
    project_roles_endpoint = ProjectRolesEndpoint()
    system_roles_endpoint = SystemRolesEndpoint()
    first_system_role_id = system_roles_endpoint.get_all_system_roles_id()[0]
    first_project_role_id = project_roles_endpoint.get_all_project_roles_id()[1]
    first_post_id = post_endpoint.get_all_posts_id()[0]
    first_department_id = department_endpoint.get_all_departments_id()[1]
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
                   projectRoleIds=[first_project_role_id],
                   postId=first_post_id,
                   departmentId=first_department_id,
                   systemRoleIds=[first_system_role_id]
                   )
    if user_id is None:
        response = user_endpoint.create_user_api(json=payload)
        print(response.status_code)
    else:
        response = user_endpoint.change_user(user_id=str(user_id), json=payload)
        print(response.status_code)


@pytest.fixture()
def create_user_whit_one_project_role_and_no_assignments():
    user_endpoint = UserEndpoint()
    department_endpoint = DepartmentsEndpoint()
    post_endpoint = PostsEndpoint()
    project_roles_endpoint = ProjectRolesEndpoint()
    system_roles_endpoint = SystemRolesEndpoint()
    first_system_role_id = system_roles_endpoint.get_all_system_roles_id()[0]
    first_project_role_id = project_roles_endpoint.get_all_project_roles_id()[1]
    first_post_id = post_endpoint.get_all_posts_id()[0]
    first_department_id = department_endpoint.get_all_departments_id()[1]
    user_id = user_endpoint.get_user_id_by_email('no_assignments@mail.ruru')
    payload = dict(username="AnotAssignment",
                   name="Анет",
                   secondName="Аназначения",
                   gender="MALE",
                   phone="",
                   email="no_assignments@mail.ruru",
                   hourlyWage=False,
                   startWorkDate=BasePage(driver=None).get_day_before_ymd(1),
                   dismissalDate=None,
                   userAssignments=[],
                   projectRoleIds=[first_project_role_id],
                   postId=first_post_id,
                   departmentId=first_department_id,
                   systemRoleIds=[first_system_role_id]
                   )
    if user_id is None:
        response = user_endpoint.create_user_api(json=payload)
        print(response.status_code)
    else:
        response = user_endpoint.change_user(user_id=str(user_id), json=payload)
        print(response.status_code)
    return payload["secondName"] + ' ' + payload["name"]


@pytest.fixture()
def create_hourly_wage_user():
    user_endpoint = UserEndpoint()
    project_endpoint = ProjectEndpoint()
    department_endpoint = DepartmentsEndpoint()
    post_endpoint = PostsEndpoint()
    project_roles_endpoint = ProjectRolesEndpoint()
    system_roles_endpoint = SystemRolesEndpoint()
    first_system_role_id = system_roles_endpoint.get_all_system_roles_id()[0]
    first_project_role_id = project_roles_endpoint.get_all_project_roles_id()[1]
    first_post_id = post_endpoint.get_all_posts_id()[0]
    first_department_id = department_endpoint.get_all_departments_id()[1]
    first_project_id = project_endpoint.get_all_project().json()[0]['id']
    user_id = user_endpoint.get_user_id_by_email('auto_testt_hourly@mail.rruu')
    payload = dict(username="AutoTestHourly",
                   name="Анисий",
                   secondName="Апочасовая",
                   gender="MALE",
                   phone="",
                   email="auto_testt_hourly@mail.rruu",
                   hourlyWage=True,
                   startWorkDate="2024-04-11",
                   userAssignments=[dict(
                       projectId=first_project_id,
                       projectRoleId=first_project_role_id,
                       isProjectManager=False
                   )
                   ],
                   projectRoleIds=[first_project_role_id],
                   postId=first_post_id,
                   departmentId=first_department_id,
                   systemRoleIds=[first_system_role_id]
                   )
    if user_id is None:
        response = user_endpoint.create_user_api(json=payload)
        print(response.status_code)
    else:
        response = user_endpoint.change_user(user_id=str(user_id), json=payload)
        print(response.status_code)
    return payload["secondName"]


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
    response = advanced_search.create_advanced_search_api(json=payload)
    yield payload['title']
    if advanced_search.check_advanced_search_by_id(str(USER_ID)):
        advanced_search.delete_advanced_search_api(str(response.json()['id']))
    else:
        pass


@pytest.fixture()
def create_resume():
    resume_endpoint = ResumeEndpoint()
    payload = dict(
        userId=USER_ID,
        title='резюме для авто',
        version=1,
        data=dict(
            fullName=USER_NAME,
            post='Автоматизатор',
            experienceDate=BasePage(driver=None).get_day_before_m_d_y(2)
        )
    )
    response = resume_endpoint.create_resume_api(json=payload)
    yield payload['title']
    resume_endpoint.delete_resume_api(str(response.json()['id']))


@pytest.fixture()
def create_resume_to_delete():
    resume_endpoint = ResumeEndpoint()
    payload = dict(
        userId=USER_ID,
        title='резюме для удаления',
        version=1,
        data=dict(
            fullName=USER_NAME,
            post='Автоматизатор',
            experienceDate=BasePage(driver=None).get_day_before_m_d_y(2)
        )
    )
    response = resume_endpoint.create_resume_api(json=payload)
    yield payload['title']
    if resume_endpoint.check_resume_by_id(str(response.json()['id'])):
        resume_endpoint.delete_resume_api(str(response.json()['id']))
    else:
        pass


@pytest.fixture()
def create_second_resume():
    resume_endpoint = ResumeEndpoint()
    payload = dict(
        userId=USER_ID,
        title='Второе резюме',
        version=1,
        data=dict(
            fullName=USER_NAME,
            post='Автоматизатор',
            experienceDate=BasePage(driver=None).get_day_before_m_d_y(2)
        )
    )
    response = resume_endpoint.create_resume_api(json=payload)
    yield payload['title']
    resume_endpoint.delete_resume_api(str(response.json()['id']))

@pytest.fixture()
def create_holiday():
    calendar_endpoint = CalendarEndpoint()
    payload = dict(
        name='Праздник3',
        startDate='12.12.2055',
        type="PREHOLIDAY",
        source="USER",
        description=None,
        annuality=False
    )
    response = calendar_endpoint.create_holiday_api(json=payload)
    yield payload['name']
    calendar_endpoint.delete_holiday_api(str(response.json()['id']))


@pytest.fixture()
def create_second_holiday():
    calendar_endpoint = CalendarEndpoint()
    payload = dict(
        name='Грустный праздник',
        startDate='10.12.2055',
        type="HOLIDAY",
        source="SYSTEM",
        description=None,
        annuality=False
    )
    response = calendar_endpoint.create_holiday_api(json=payload)
    yield payload
    calendar_endpoint.delete_holiday_api(str(response.json()['id']))


@pytest.fixture()
def create_filial_with_director():
    filial_endpoint = AffiliatesEndpoint()
    user_endpoint = UserEndpoint()
    project_roles_endpoint = ProjectRolesEndpoint()
    director_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    first_project_role_id = project_roles_endpoint.get_all_project_roles_id()[1]
    dates_of_project_role = project_roles_endpoint.get_info_about_project_role_dates(first_project_role_id)
    project_role_name = project_roles_endpoint.get_name_project_role_by_id(first_project_role_id)
    dates_of_user = user_endpoint.get_user_dates_by_id(director_id)
    payload = dict(name='Филиал с директором',
                   address='г. Рязань',
                   directorId=director_id,
                   employees=[dict(
                       id=director_id,
                       createdAt=dates_of_user[0],
                       updatedAt=dates_of_user[1],
                       username="AutoTester1",
                       name="Автомат",
                       secondName="АвтоСПроектом",
                       gender="MALE",
                       fullName='АвтоСПроектом Автомат',
                       email="auto_testt@mail.rruu",
                       hourlyWage=False,
                       type='local',
                       projectRoles=[dict(
                           id=first_project_role_id,
                           createdAt=dates_of_project_role[0],
                           updatedAt=dates_of_project_role[1],
                           name=project_role_name,
                           leadership=False)
                       ])
                   ])
    response = filial_endpoint.create_affiliates_api(json=payload)
    print(response.status_code)
    yield payload['name']
    filial_endpoint.delete_filial_if_it_exist('Филиал с директором') #Иначе пропадает пользователь
