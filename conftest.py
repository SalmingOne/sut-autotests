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
from endpoints.file_endpoint import FilesEndpoint
from endpoints.labels_endpoint import LabelsEndpoint
from endpoints.gantt_endpoint import GanttEndpoint
from endpoints.labor_reports_endpoint import LaborReportEndpoint
from endpoints.logs_endpoint import LogsEndpoint
from endpoints.personal_quality_endpoint import PersonalQualityEndpoint
from endpoints.posts_endpoint import PostsEndpoint
from endpoints.project_endpoint import ProjectEndpoint
from endpoints.project_roles_endpoint import ProjectRolesEndpoint
from endpoints.resume_endpoint import ResumeEndpoint
from endpoints.search_profile_endpoint import SearchProfileEndpoint
from endpoints.skills_and_knowledge_endpoint import SkillsAndKnowledgeEndpoint
from endpoints.slots_endpoint import SlotsEndpoint
from endpoints.statement_files_endpoint import StatementFilesEndpoint
from endpoints.system_roles_endpoint import SystemRolesEndpoint
from endpoints.attraction_rates_endpoint import AttractionRatesEndpoint
from endpoints.users_endpoint import UserEndpoint
from endpoints.calendar_endpoint import CalendarEndpoint
from endpoints.variables_endpoint import VariablesEndpoint
from endpoints.busy_percentages_endpoint import BusyPercentagesEndpoint
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
    driver.implicitly_wait(10)
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
def simple_project_with_description():
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        description='Длинное описание проекта'
    ).model_dump()
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
def project_with_required_reasons_with_work_and_overtime_work():
    labor_report_endpoint = LaborReportEndpoint()
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    payload = CreateProject(
        laborReasons=True
    ).model_dump()
    res = project_endpoint.create_project_api(json=payload)
    project_id = res.json()['id']
    hours = 6
    reason = "Просто так"
    payload = [
        dict(
            date=BasePage(driver=None).get_day_before_m_d_y(0),
            projectId=project_id,
            overtimeWork=hours,
            hours=hours,
            type="DEFAULT",
            userId=USER_ID,
            reason=reason,
            overtimeReason=reason
        )
    ]
    labor_report_endpoint.post_labor_report_api(json=payload)
    number_day = BasePage(driver=None).get_day_after_ymd(1).split('-')[2]
    yield res.json(), number_day, reason, hours
    project_endpoint.delete_project_api(str(project_id))


@pytest.fixture()
def second_project_with_work():
    labor_report_endpoint = LaborReportEndpoint()
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist('SecondProject')
    project_endpoint = ProjectEndpoint()
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    project_endpoint.delete_project_if_it_exist('SecondProject')
    payload = CreateProject(
        name='SecondProject',
        code='SECP',
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
    hours = 3
    payload = [
        dict(
            date=BasePage(driver=None).get_day_before_m_d_y(0),
            projectId=project_id,
            hours=hours,
            type="DEFAULT",
            userId=USER_ID,
        )
    ]
    labor_report_endpoint.post_labor_report_api(json=payload)
    yield res.json()
    project_endpoint.delete_project_api(str(res.json()['id']))


@pytest.fixture()
def project_with_added_labor_reason():
    labor_report_endpoint = LaborReportEndpoint()
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
    project_id = res.json()['id']
    hours = 6
    reason = "Просто так"
    payload = [
        dict(
            date=BasePage(driver=None).get_day_before_m_d_y(0),
            projectId=project_id,
            hours=hours,
            type="DEFAULT",
            userId=USER_ID,
            reason=reason,
        )
    ]
    labor_report_endpoint.post_labor_report_api(json=payload)
    yield res.json()
    project_endpoint.delete_project_api(str(res.json()['id']))
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
    start_date = start_date if start_date != BasePage(driver=None).get_day_before_m_d_y(0) else BasePage(driver=None).get_day_before_m_d_y(1)
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
def project_with_completed_task():
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
    start_date = start_date if start_date != BasePage(driver=None).get_day_before_m_d_y(0) else BasePage(driver=None).get_day_before_m_d_y(1)
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
        status="COMPLETED",
        changeDate=start_date
    )
    gantt_endpoint.change_task_status(taskId, payload)
    number_day = BasePage(driver=None).get_day_after_ymd(1).split('-')[2]

    yield res.json(), number_day, taskName
    project_endpoint.delete_project_api(str(project_id))

@pytest.fixture()
def project_with_rejected_task_labor_cost():
    labor_report_endpoint = LaborReportEndpoint()
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    user_endpoint = UserEndpoint()
    user_name = user_endpoint.get_user_by_id(str(USER_ID)).json()['fullName']
    payload = CreateProject(
        laborReasons=True,
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
    start_date = start_date if start_date != BasePage(driver=None).get_day_before_m_d_y(0) else BasePage(
        driver=None).get_day_before_m_d_y(1)
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

    payload = [
        dict(
            hours=3,
            date=BasePage(driver=None).get_day_after_ymd(0),
            reason="Причина",
            userId=USER_ID,
            type='DEFAULT',
            projectId=res.json()["id"],
            taskId=taskId,
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
    labor_report_endpoint.put_labor_reports(json=payload)
    number_day = BasePage(driver=None).get_day_after_ymd(1).split('-')[2]
    yield res.json(), number_day, taskName, user_name
    project_endpoint.delete_project_api(str(project_id))

@pytest.fixture()
def project_with_rejected_labor_cost():
    labor_report_endpoint = LaborReportEndpoint()
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    user_endpoint = UserEndpoint()
    user_name = user_endpoint.get_user_by_id(str(USER_ID)).json()['fullName']
    payload = CreateProject(
        laborReasons=True,
        resources=[dict(
            projectRoleId=1,
            userId=USER_ID,
            isProjectManager=True
        )]
    ).model_dump()
    res = project_endpoint.create_project_api(json=payload)
    project_id = res.json()['id']

    payload = [
        dict(
            hours=3,
            date=BasePage(driver=None).get_day_after_ymd(1),
            reason="Причина",
            userId=USER_ID,
            type='DEFAULT',
            projectId=res.json()["id"],
        )
    ]

    labor_report_endpoint.post_labor_report_api(json=payload)
    rejection_reason = 'Просто так'
    ids = labor_report_endpoint.get_labor_reports_by_project_api(str(res.json()["id"]),
                                                                 BasePage(driver=None).get_day_after_ymd(0),
                                                                 BasePage(driver=None).get_day_after_ymd(2))
    payload = [
        dict(
            ids=ids,
            rejectionReason=rejection_reason,
            approvalStatus='REJECTED',
        )
    ]
    labor_report_endpoint.put_labor_reports(json=payload)
    number_day = BasePage(driver=None).get_day_after_ymd(2).split('-')[2]
    yield res.json(), number_day, user_name
    project_endpoint.delete_project_api(str(project_id))

@pytest.fixture()
def project_with_rejected_labor_cost_without_reason():
    labor_report_endpoint = LaborReportEndpoint()
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist(PROJECT_NAME)
    user_endpoint = UserEndpoint()
    user_name = user_endpoint.get_user_by_id(str(USER_ID)).json()['fullName']
    payload = CreateProject(
        resources=[dict(
            projectRoleId=1,
            userId=USER_ID,
            isProjectManager=True
        )]
    ).model_dump()
    res = project_endpoint.create_project_api(json=payload)
    project_id = res.json()['id']

    payload = [
        dict(
            hours=3,
            date=BasePage(driver=None).get_day_after_ymd(1),
            reason="Причина",
            userId=USER_ID,
            type='DEFAULT',
            projectId=res.json()["id"],
        )
    ]

    labor_report_endpoint.post_labor_report_api(json=payload)
    rejection_reason = 'Просто так'
    ids = labor_report_endpoint.get_labor_reports_by_project_api(str(res.json()["id"]),
                                                                 BasePage(driver=None).get_day_after_ymd(0),
                                                                 BasePage(driver=None).get_day_after_ymd(2))
    payload = [
        dict(
            ids=ids,
            rejectionReason=rejection_reason,
            approvalStatus='REJECTED',
        )
    ]
    labor_report_endpoint.put_labor_reports(json=payload)
    number_day = BasePage(driver=None).get_day_after_ymd(2).split('-')[2]
    yield res.json(), number_day, user_name
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
    payload = dict(name='Не уникальное имя', systemName='Не уникальное имя')
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
def skills_and_knowledge():
    skills_and_knowledge_endpoint = SkillsAndKnowledgeEndpoint()
    if skills_and_knowledge_endpoint.return_len_skills_and_knowledge() >= 2:
        pass
    else:
        payload = dict(name='Selenium', type='skill')
        skills_and_knowledge_endpoint.create_skills_and_knowledge_api(json=payload)
        payload = dict(name='Pytest', type='knowledge')
        skills_and_knowledge_endpoint.create_skills_and_knowledge_api(json=payload)


@pytest.fixture()
def create_skill():
    skills_and_knowledge_endpoint = SkillsAndKnowledgeEndpoint()
    payload = dict(name='Ловить мух', type='skill')
    response = skills_and_knowledge_endpoint.create_skills_and_knowledge_api(json=payload)
    yield response.json()
    skills_and_knowledge_endpoint.delete_skills_and_knowledge_api(str(response.json()['id']))


@pytest.fixture()
def project_with_assignment():
    project_endpoint = ProjectEndpoint()
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    user_name = user_endpoint.get_user_by_id(str(USER_ID)).json()['fullName']
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
    number_day = BasePage(driver=None).get_day_after_ymd(0).split('-')[2]
    number_day = number_day if number_day != '1' else BasePage(driver=None).get_day_after(1).split('.')[0]
    yield response.json(), number_day, user_name
    project_endpoint.delete_project_api(str(response.json()['id']))

@pytest.fixture()
def project_with_tester_assignment():
    project_endpoint = ProjectEndpoint()
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    user_name = user_endpoint.get_user_by_id(str(USER_ID)).json()['fullName']
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
    payload = dict(projectRoleId=6,
                   projectId=response.json()["id"],
                   userId=USER_ID,
                   isProjectManager=True,
                   startDate=CreateProject().startDate
                   )
    assignment_endpoint = AssignmentEndpoint()
    assignment_endpoint.create_assignment_api(json=payload)
    number_day = BasePage(driver=None).get_day_after_ymd(0).split('-')[2]
    number_day = number_day if number_day != '1' else BasePage(driver=None).get_day_after(1).split('.')[0]
    yield response.json(), number_day, user_name
    project_endpoint.delete_project_api(str(response.json()['id']))

@pytest.fixture()
def project_with_assignment_and_no_end_date():
    project_endpoint = ProjectEndpoint()
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    project_endpoint.delete_project_if_it_exist('No End')
    payload = CreateProject(
        name='No End',
        code='Noe',
        endDate=None,
        resources=[dict(
            projectRoleId=2,
            userId=user_id,
            isProjectManager=True
        )
        ]
    ).model_dump()
    response = project_endpoint.create_project_api(json=payload)
    payload = dict(projectRoleId=2,
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
def second_project_with_assignment():
    project_endpoint = ProjectEndpoint()
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    project_endpoint.delete_project_if_it_exist('SECP')
    payload = CreateProject(
        code='SECP',
        name='SecondProject',
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
    number_day = BasePage(driver=None).get_day_after_ymd(0).split('-')[2]
    number_day = number_day if number_day != '1' else BasePage(driver=None).get_day_after(1).split('.')[0]
    yield response.json(), number_day
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
    first_system_role_id = system_roles_endpoint.get_user_system_role_id('Пользователь')
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
    return payload["secondName"]


@pytest.fixture()
def create_next_week_fired_user():
    user_endpoint = UserEndpoint()
    department_endpoint = DepartmentsEndpoint()
    post_endpoint = PostsEndpoint()
    project_roles_endpoint = ProjectRolesEndpoint()
    system_roles_endpoint = SystemRolesEndpoint()
    first_system_role_id = system_roles_endpoint.get_all_system_roles_id()[0]
    first_project_role_id = project_roles_endpoint.get_all_project_roles_id()[1]
    first_post_id = post_endpoint.get_all_posts_id()[0]
    first_department_id = department_endpoint.get_all_departments_id()[1]
    user_id = user_endpoint.get_user_id_by_email('next_week_test@mail.ruru')
    payload = dict(username="AutNext",
                   name="Аскоро",
                   secondName="Ауволят",
                   gender="MALE",
                   phone="",
                   email="next_week_test@mail.ruru",
                   hourlyWage=False,
                   startWorkDate="2024-04-11",
                   dismissalDate=BasePage(driver=None).get_day_before_ymd(-7),
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
    return payload["secondName"]


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

@pytest.fixture()
def project_with_planned_resources():
    project_endpoint = ProjectEndpoint()
    project_endpoint.delete_project_if_it_exist('PlannedResourcesProject')
    start_date, end_date = [day for day in BasePage(driver=None).get_full_work_week()]
    start_date_pr = start_date.strftime("%m.%d.%Y")
    end_date_pr = end_date.strftime("%m.%d.%Y")
    start_date_dr = start_date.strftime("%d.%m.%Y")
    end_date_dr = end_date.strftime("%d.%m.%Y")
    payload = CreateProject(
        code='PRP',
        name='PlannedResourcesProject',
        startDate=start_date_pr,
        endDate=end_date_pr,
        resources=[dict(
            projectRoleId=1,
            userId=USER_ID,
            isProjectManager=True)
        ]
        ).model_dump()
    res = project_endpoint.create_project_api(json=payload)
    project_id = res.json()["id"]
    slot_id = res.json()["slots"][0]['id']
    payload = [dict(
        hours = 4,
        slotId = slot_id,
        projectId = project_id,
        projectRoleId = 1,
        userId = USER_ID,
        startOf = start_date_pr,
        endOf = end_date_pr
    )]
    busy_percentages_endpoint = BusyPercentagesEndpoint()
    busy_percentages_endpoint.create_busy_percentages_api(json=payload)
    yield start_date_dr, end_date_dr, res.json()
    project_endpoint.delete_project_api(str(res.json()['id']))


@pytest.fixture()
def put_label_to_auto_user(project_with_two_resources):
    user_endpoint = UserEndpoint()
    labels_endpoint = LabelsEndpoint()
    auto_user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    auto_user_profile_id = user_endpoint.get_user_profile_id_by_user_id(str(auto_user_id))
    user_profile_id = user_endpoint.get_user_profile_id_by_user_id(str(USER_ID))
    payload = dict(
        authorProfileId=user_profile_id,
        receiverProfileId=auto_user_profile_id,
        labels=[
            dict(
                mark=True,
                comment='Хорошо работает',
                projectId=project_with_two_resources['id']
            )
        ]
    )
    labels_endpoint.put_label_api(json=payload)


@pytest.fixture()
def create_resume_to_autotest_user():
    resume_endpoint = ResumeEndpoint()
    user_endpoint = UserEndpoint()
    user_id = user_endpoint.get_user_id_by_email('auto_testt@mail.rruu')
    payload = dict(
        userId=user_id,
        title='резюме для авто',
        version=1,
        data=dict(
            fullName='Авто Авто',
            post='Автоматизатор',
            experienceDate=BasePage(driver=None).get_day_before_m_d_y(2)
        )
    )
    response = resume_endpoint.create_resume_api(json=payload)
    yield payload['title']
    resume_endpoint.delete_resume_api(str(response.json()['id']))


@pytest.fixture()
def create_personal_quality():
    persona_quality_endpoint = PersonalQualityEndpoint()
    payload = dict(name='АААличное')
    response = persona_quality_endpoint.create_personal_quality_api(json=payload)
    yield response.json()
    persona_quality_endpoint.delete_personal_quality_api(str(response.json()['id']))


@pytest.fixture()
def create_second_personal_quality():
    persona_quality_endpoint = PersonalQualityEndpoint()
    payload = dict(name='АААкачество')
    response = persona_quality_endpoint.create_personal_quality_api(json=payload)
    yield response.json()
    persona_quality_endpoint.delete_personal_quality_api(str(response.json()['id']))


@pytest.fixture()
def add_all_statement_files():
    statement_files_endpoint = StatementFilesEndpoint()
    files_endpoint = FilesEndpoint()
    all_type_file = statement_files_endpoint.get_all_statement_files_types()
    if 'DIS' not in all_type_file:
        fp = open('../data/files/увольнение.docx', 'rb')
        files = {'file': fp}
        add_file = files_endpoint.post_file(files)
        statement_files_endpoint.post_statement_file(add_file.json()['id'], 'DIS')
    if 'ADM' not in all_type_file:
        fp = open('../data/files/административный.docx', 'rb')
        files = {'file': fp}
        add_file = files_endpoint.post_file(files)
        statement_files_endpoint.post_statement_file(add_file.json()['id'], 'ADM')
    if 'MAT' not in all_type_file:
        fp = open('../data/files/декретный отпуск.docx', 'rb')
        files = {'file': fp}
        add_file = files_endpoint.post_file(files)
        statement_files_endpoint.post_statement_file(add_file.json()['id'], 'MAT')
    if 'VAC' not in all_type_file:
        fp = open('../data/files/ежегодный.docx', 'rb')
        files = {'file': fp}
        add_file = files_endpoint.post_file(files)
        statement_files_endpoint.post_statement_file(add_file.json()['id'], 'VAC')


@pytest.fixture()
def attraction_rate_by_user_to_delete():
    user_endpoint = UserEndpoint()
    user_name = user_endpoint.get_user_by_id(str(USER_ID)).json()['fullName']
    attraction_rate_endpoint = AttractionRatesEndpoint()
    payload = dict(
        name='По пользователю',
        type='ByUser',
        size='100',
        dateActionAttractionRateFrom=BasePage(driver=None).get_day_before_y_m_d(0),
        targetIds=[
            USER_ID
        ]
    )
    res = attraction_rate_endpoint.create_attraction_rate(payload)
    yield res.json()['name'], user_name
    if res.json()['id'] in [item['id'] for item in attraction_rate_endpoint.get_attraction_rates().json()]:
        attraction_rate_endpoint.delete_attraction_rate(str(res.json()['id']))
    else:
        pass

@pytest.fixture()
def attraction_rate_by_slot_to_delete():
    user_endpoint = UserEndpoint()
    user_name = user_endpoint.get_user_by_id(str(USER_ID)).json()['fullName']
    attraction_rate_endpoint = AttractionRatesEndpoint()
    payload = dict(
        name='По cлоту',
        type='BySlot',
        size='100',
        dateActionAttractionRateFrom=BasePage(driver=None).get_day_before_y_m_d(0),
        targetIds=[
            6  # ID роли Тестировщик
        ]
    )
    res = attraction_rate_endpoint.create_attraction_rate(payload)
    yield res.json()['name']
    if res.json()['id'] in [item['id'] for item in attraction_rate_endpoint.get_attraction_rates().json()]:
        attraction_rate_endpoint.delete_attraction_rate(str(res.json()['id']))
    else:
        pass

@pytest.fixture()
def attraction_rate_by_affiliate_to_delete():
    filial_endpoint = AffiliatesEndpoint()
    payload = dict(name='Авто', address='г. Москва')
    response = filial_endpoint.create_affiliates_api(json=payload)
    attraction_rate_endpoint = AttractionRatesEndpoint()
    payload = dict(
        name='По ЮЛ',
        type='ByAffiliate',
        size='100',
        dateActionAttractionRateFrom=BasePage(driver=None).get_day_before_y_m_d(0),
        targetIds=[
            response.json()['id']
        ]
    )
    res = attraction_rate_endpoint.create_attraction_rate(payload)
    yield res.json()['name'], response.json()['name']
    filial_endpoint.delete_affiliates_api(str(response.json()['id']))
    if res.json()['id'] in [item['id'] for item in attraction_rate_endpoint.get_attraction_rates().json()]:
        attraction_rate_endpoint.delete_attraction_rate(str(res.json()['id']))
    else:
        pass

@pytest.fixture()
def attraction_rate_with_project():
    slots_endpoint = SlotsEndpoint()
    attraction_rate_endpoint = AttractionRatesEndpoint()
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
    payload = dict(
        name='По cлоту',
        type='BySlot',
        size='100',
        dateActionAttractionRateFrom=BasePage(driver=None).get_day_before_y_m_d(0),
        targetIds=[
            6  # ID роли Тестировщик
        ]
    )
    res = attraction_rate_endpoint.create_attraction_rate(payload)
    payload = [
            dict(
                projectRoleId=6,
                attractionRateId=res.json()['id'],
                disabled=False,
                assignments=[
                    dict(
                        userId=USER_ID
                    )
                ]
        )
    ]
    slots_endpoint.create_slot(response.json()['id'], payload)
    yield res.json()['name']
    project_endpoint.delete_project_api(str(response.json()['id']))
    attraction_rate_endpoint.delete_attraction_rate(str(res.json()['id']))

@pytest.fixture()
def create_filial_with_added_user():
    filial_endpoint = AffiliatesEndpoint()
    user_endpoint = UserEndpoint()
    user = user_endpoint.get_user_by_id(str(USER_ID)).json()
    payload = dict(name='Крутой филиал', address='г. Москва', employees=[user])
    response = filial_endpoint.create_affiliates_api(json=payload)
    yield response.json(), user['fullName']

@pytest.fixture()
def delete_filial_and_attraction_rate():
    def _delete_filial_and_attraction_rate(rate_name, filial_name):
        attraction_rate_endpoint = AttractionRatesEndpoint()
        filial_endpoint = AffiliatesEndpoint()
        filial_endpoint.delete_filial_by_name_api(filial_name)
        for rate in attraction_rate_endpoint.get_attraction_rates().json():
            if rate['name'] == rate_name:
                attraction_rate_endpoint.delete_attraction_rate(str(rate['id']))
    return _delete_filial_and_attraction_rate

@pytest.fixture()
def delete_attraction_rate():

    def _delete_attraction_rate(rate_name):
        attraction_rate_endpoint = AttractionRatesEndpoint()
        filial_endpoint = AffiliatesEndpoint()
        for rate in attraction_rate_endpoint.get_attraction_rates().json():
            if rate['name'] == rate_name:
                attraction_rate_endpoint.delete_attraction_rate(str(rate['id']))
    return _delete_attraction_rate


@pytest.fixture()
def changed_attraction_rate():
    user_endpoint = UserEndpoint()
    user_name = user_endpoint.get_user_by_id(str(USER_ID)).json()['fullName']
    attraction_rate_endpoint = AttractionRatesEndpoint()
    payload = dict(
        name='По пользователю',
        type='ByUser',
        size='100',
        dateActionAttractionRateFrom=BasePage(driver=None).get_day_before_y_m_d(0),
        targetIds=[
            USER_ID
        ]
    )
    res = attraction_rate_endpoint.create_attraction_rate(payload)
    payload = dict(
        dateActionAttractionRateFrom=BasePage(driver=None).get_day_before_y_m_d(0),
        size='1000',
    )
    response = attraction_rate_endpoint.change_attraction_rate(str(res.json()['id']), payload)
    yield res.json()['name'], user_name
    items = [item['id'] for item in attraction_rate_endpoint.get_attraction_rates().json()]
    if response.json()['id'] in items:
        attraction_rate_endpoint.delete_attraction_rate(str(response.json()['id']))
        attraction_rate_endpoint.delete_attraction_rate(str(response.json()['id'] - 1))
    else:
        pass