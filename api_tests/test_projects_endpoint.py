import time

import allure
import pytest
import testit

from data.data import PROJECT_NAME
from endpoints.project_endpoint import ProjectEndpoint
from pages.base_page import BasePage


@allure.suite("Projects endpoint")
class TestProjectEndpoint:
    testdata = [
        ('', PROJECT_NAME, '01.10.2022', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с пустым полем code'),
        (10, PROJECT_NAME, '01.10.2022', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с полем code отличным от string'),
        ("123456789011", PROJECT_NAME, '01.10.2022', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с полем code длиной более 11 символов'),
        ("ЦюZw-23", PROJECT_NAME, '01.10.2022', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         200, 'Нельзя изменить проект с корректным полем code'),
        ("-ЦюZw23", PROJECT_NAME, '01.10.2022', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с полем code начинающимся с -'),
        ("ЦюZw-23-", PROJECT_NAME, '01.10.2022', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с полем code заканчивающимся на -'),
        ("ATP", '', '01.10.2022', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с пустым полем name'),
        ("ATP", 11, '01.10.2022', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с полем name отличным от string'),
        ("ATP", ('a' * 101), '01.10.2022', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с полем name длиной более 100 символов'),
        ("ATP", PROJECT_NAME, '', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с пустым полем startDate'),
        ("ATP", PROJECT_NAME, 'дата', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с полем startDate отличным от формата datetime'),
        ("ATP", PROJECT_NAME, 23, '12.21.2029', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с полем startDate отличным от формата string'),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2022', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с полем startDate позже endDate'),
        ("ATP", PROJECT_NAME, '12.21.1223', '12.21.2029', 'ACTIVE', True, False, False, [], False,
         200, 'Нельзя изменить поле startDate на дату раньше 1900 года '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', '', True, False, False, [], False,
         400, 'Можно изменить проект с пустым полем status '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 17, True, False, False, [], False,
         400, 'Можно изменить проект с полем status отличным от string'),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', '', False, False, [], False,
         400, 'Можно изменить проект с пустым полем selfAdding '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', 45, False, False, [], False,
         400, 'Можно изменить проект с полем selfAdding отличным от boolean '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, '', False, [], False,
         400, 'Можно изменить проект с пустым полем laborReasons '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, 222, False, [], False,
         400, 'Можно изменить проект с полем laborReasons отличным от boolean '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, False, '', [], False,
         400, 'Можно изменить проект с пустым полем mandatoryAttachFiles '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, False, 65, [], False,
         400, 'Можно изменить проект с полем mandatoryAttachFiles отличным от boolean '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, False, False, [], '',
         400, 'Можно изменить проект с пустым полем automaticLaborReports '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, False, False, [], 21,
         400, 'Можно изменить проект с полем automaticLaborReports отличным от boolean '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, True, False, [], True,
         400,
         'Можно изменить проект с одновременным включением автоматического проставления трудозатрат и '
         'обязательного указания причины списания трудозатрат '),
        ("ATP", PROJECT_NAME, '12.21.2023', '', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с пустым полем endDate '),
        ("ATP", PROJECT_NAME, '12.21.2023', 'дата', 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с полем endDate отличным от формата datetime '),
        ("ATP", PROJECT_NAME, '12.21.2023', 33, 'ACTIVE', True, False, False, [], False,
         400, 'Можно изменить проект с полем endDate отличным от string '),
        ("ATP", PROJECT_NAME, '12.21.2023', 'дата', 'ACTIVE', True, False, False, None, False,
         400, 'Можно изменить проект с пустым полем resources '),
        ("ATP", PROJECT_NAME, '12.21.2023', 33, 'ACTIVE', True, False, False, 'не формат', False,
         400, 'Можно изменить проект с полем resources отличным от array ')
    ]

    @testit.workItemIds(65256)
    @testit.displayName("PUT /projects/{projectId} (Чек-лист)")
    @pytest.mark.api
    @allure.title("id-65256 PUT /projects/{projectId} (Чек-лист)")
    @pytest.mark.parametrize("code, name, start_date, end_date, status, self_adding, labor_reasons, "
                             "mandatory_attach_files, resources, auto_labor_reports, expected, error_text", testdata)
    def test_put_projects_check_list(self, simple_project, code, name, start_date, end_date, status, self_adding,
                                     labor_reasons, mandatory_attach_files, resources, auto_labor_reports,
                                     expected, error_text):
        project_endpoint = ProjectEndpoint()
        time.sleep(0.5)
        payload = dict(
            code=code,
            name=name,
            startDate=start_date,
            endDate=end_date,
            status=status,
            selfAdding=self_adding,
            laborReasons=labor_reasons,
            mandatoryAttachFiles=mandatory_attach_files,
            resources=resources,
            automaticLaborReports=auto_labor_reports
        )
        time.sleep(1)
        response = project_endpoint.change_project_api(str(simple_project['id']), payload)
        assert response.status_code == expected, error_text + '\n' + 'Запрос:\n' + str(
            payload) + '\n' + 'Ответ:\n' + str(response.json())

    testdata_2 = [
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, False, False, [], False, '', None, None, None,
         None, 400, 'Можно изменить проект с пустым полем description '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, False, False, [], False, 'не визивиг', None,
         None, None, None, 400, 'Можно изменить проект с полем description отличным от визивига'),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, False, False, [], False, 1, None, None, None,
         None, 400, 'Можно изменить проект с полем description отличным от string '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, False, False, [], False, None, '', None, None,
         None, 400, 'Можно изменить проект с пустым полем consumer '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, False, False, [], False, None, 24, None, None,
         None, 400, 'Можно изменить проект с полем consumer отличным от string '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, True, False, [], False, None, None, '', None,
         None, 400, 'Можно изменить проект с пустым полем laborReasonStartDate '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, True, False, [], False, None, None, 24, None,
         None, 400, 'Можно изменить проект с полем laborReasonStartDate отличным от string '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, True, False, [], False, None, None, 'дата',
         None, None, 400, 'Можно изменить проект с полем laborReasonStartDate отличным от datetime '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, True, False, [], False, None, None,
         BasePage(driver=None).get_day_before_m_d_y(-1), None, None, 400,
         'Можно изменить проект с полем laborReasonStartDate позднее текущей даты '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, True, False, [], False, None, None, None, '',
         None, 400, 'Можно изменить проект с пустым полем fileDescription '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, True, False, [], False, None, None, None, 24,
         None, 400, 'Можно изменить проект с полем fileDescription отличным от string '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, True, False, [], False, None, None, None,
         None, '', 400, 'Можно изменить проект с пустым полем imageField '),
        ("ATP", PROJECT_NAME, '12.21.2023', '12.21.2029', 'ACTIVE', True, True, False, [], False, None, None, None,
         None, 'строка', 400, 'Можно изменить проект с полем imageField отличным от number ')
    ]

    @testit.workItemIds(65256)
    @testit.displayName("PUT /projects/{projectId} (Чек-лист)")
    @pytest.mark.api
    @allure.title("id-65256 PUT /projects/{projectId} (Чек-лист)")
    @pytest.mark.parametrize("code, name, start_date, end_date, status, self_adding, labor_reasons, "
                             "mandatory_attach_files, resources, auto_labor_reports, description, consumer, "
                             "labor_reason_start_date, file_description, image_field, expected, error_text", testdata_2)
    def test_put_projects_check_list_2(self, simple_project, code, name, start_date, end_date, status, self_adding,
                                       labor_reasons, mandatory_attach_files, resources, auto_labor_reports,
                                       description, consumer, labor_reason_start_date, file_description, image_field,
                                       expected, error_text):
        project_endpoint = ProjectEndpoint()
        time.sleep(0.5)
        payload = dict(
            code=code,
            name=name,
            startDate=start_date,
            endDate=end_date,
            status=status,
            selfAdding=self_adding,
            laborReasons=labor_reasons,
            mandatoryAttachFiles=mandatory_attach_files,
            resources=resources,
            automaticLaborReports=auto_labor_reports,
            description=description,
            consumer=consumer,
            laborReasonStartDate=labor_reason_start_date,
            fileDescription=file_description,
            imageField=image_field
        )
        time.sleep(1)
        response = project_endpoint.change_project_api(str(simple_project['id']), payload)
        assert response.status_code == expected, error_text + '\n' + 'Запрос:\n' + str(
            payload) + '\n' + 'Ответ:\n' + str(response.json())
