import time

import allure
import pytest
import testit
from selenium.common import TimeoutException

from data.data import USER_NAME
from endpoints.project_endpoint import ProjectEndpoint
from pages.all_project_page import AllProjectPage
from pages.create_project_drawer_page import CreateProjectDrawerPage
from pages.labor_cost_page import LaborCostPage
from pages.project_card_page import ProjectCardPage


@allure.suite("Создание проекта")
class TestCreateProject:
    @testit.workItemIds(47)
    @testit.displayName("1.1.1 Создание нового проекта")
    @pytest.mark.smoke
    @allure.title("id-47 1.1.1 Создание нового проекта")
    def test_create_project(self, login, driver):
        # Создаем проект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        project_name, project_code, project_data, project_worker = create_project_drawer_page.create_project(
            "AutoTestProject1",
            'ATP1',
            USER_NAME,
            'no',
            '01.10.2022'
        )
        create_project_drawer_page.check_created_project()
        # Берем данные с карточки проекта
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_description_tab()
        output_project_name, output_project_code, output_project_status, output_project_begin_data, output_project_manager = project_card_page.get_project_description()
        assert project_name == output_project_name, "поле имя проекта не отобразилось в карточке проекта"
        assert project_code == output_project_code, "поле код проекта не отобразилось в карточке проекта"
        assert project_data == output_project_begin_data, "поле дата начала проекта не отобразилось в карточке проекта"
        assert project_worker in output_project_manager, "поле администратор не отобразилось в карточке проекта"
        # Берем имя проекта со страницы все проекты
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        check_name_at_all = all_project_page.check_project_name_at_all("AutoTestProject1")
        assert project_name == check_name_at_all, "имя созданного проекта отсутствует на странице все проекты"
        # Берем код проекта со страницы трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        check_code_at_labor = labor_cost_page.check_project_code_at_labor('ATP1')
        assert project_code == check_code_at_labor, "код созданного проекта отсутствует на странице трудозатрат"
        # Удаляем проект
        project_endpoint = ProjectEndpoint()
        project_endpoint.delete_project_by_name_api("AutoTestProject1")

    @testit.workItemIds(10157)
    @testit.displayName("1.1.1 Создание нового проекта в статусе черновик")
    @pytest.mark.smoke
    @allure.title("id-10157 1.1.1 Создание нового проекта в статусе черновик")
    def test_create_project_draft(self, login, driver):
        # Создаем проект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        project_name, project_code, project_data, project_worker = create_project_drawer_page.create_project(
            "AutoTestProjectDraft",
            'ATPD',
            USER_NAME,
            'draft',
            '01.10.2022'
        )
        create_project_drawer_page.check_created_project()
        # Берем данные с карточки проекта
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_description_tab()
        output_project_name, output_project_code, output_project_status, output_project_begin_data, output_project_manager = project_card_page.get_project_description()
        assert project_name == output_project_name, "поле имя проекта не отобразилось в карточке проекта"
        assert project_code == output_project_code, "поле код проекта не отобразилось в карточке проекта"
        assert project_data == output_project_begin_data, "поле дата начала проекта не отобразилось в карточке проекта"
        assert project_worker in output_project_manager, "поле администратор не отобразилось в карточке проекта"

        # Берем код проекта со страницы трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        check_code_at_labor = labor_cost_page.check_no_project_code_at_labor('ATPD')
        assert check_code_at_labor == "no element on page", "проект присутствует на странице трудозатрат"

        # Берем имя проекта со страницы все проекты
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        try:
            check_name_at_all = all_project_page.check_project_name_at_all('AutoTestProjectDraft')
        except TimeoutException:
            all_project_page.see_all_status_project()
            check_name_at_all = all_project_page.check_project_name_at_all('AutoTestProjectDraft')
        assert project_name == check_name_at_all, "имя созданного проекта отсутствует на странице все проекты"
        # Удаляем проект
        project_endpoint = ProjectEndpoint()
        project_endpoint.delete_project_by_name_api("AutoTestProjectDraft")

    @testit.workItemIds(1469)
    @testit.displayName("1.1.1 Добавление нового проекта с обязательным указанием причины списания")
    @pytest.mark.smoke
    @allure.title("id-1469 1.1.1 Добавление нового проекта с обязательным указанием причины списания")
    def test_create_project_reason(self, login, driver):
        # Создаем проект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        project_name, project_code, project_data, project_worker = create_project_drawer_page.create_project(
            "AutoTestProjectReason",
            'ATPR',
            USER_NAME,
            'reason',
            '01.10.2022')
        create_project_drawer_page.check_created_project()
        # Берем данные с карточки проекта
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_description_tab()
        output_project_name, output_project_code, output_project_status, output_project_begin_data, output_project_manager = project_card_page.get_project_description()
        assert project_name == output_project_name, "поле имя проекта не отобразилось в карточке проекта"
        assert project_code == output_project_code, "поле код проекта не отобразилось в карточке проекта"
        assert project_data == output_project_begin_data, "поле дата начала проекта не отобразилось в карточке проекта"
        assert project_worker in output_project_manager, "поле администратор не отобразилось в карточке проекта"

        # Берем код проекта со страницы трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.check_to_have_reason_fo_write('AutoTestProjectReason')
        # Берем имя проекта со страницы все проекты
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        check_name_at_all = all_project_page.check_project_name_at_all('AutoTestProjectReason')
        assert project_name == check_name_at_all, "имя созданного проекта отсутствует на странице все проекты"
        # Удаляем проект
        project_endpoint = ProjectEndpoint()
        project_endpoint.delete_project_by_name_api("AutoTestProjectReason")

    @testit.workItemIds(48)
    @testit.displayName("1.1.1 Создание проекта с неуникальным названием")
    @pytest.mark.smoke
    @allure.title("id-48 1.1.1 Создание проекта с неуникальным названием")
    def test_creating_a_project_with_non_unique_name(self, simple_project, login, driver):
        # Создаем проект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        create_project_drawer_page.create_project(
            "AutoTestProject",
            'AUTO',
            USER_NAME,
            'no',
            '01.10.2022'
        )
        error = create_project_drawer_page.get_mui_error_text()
        assert error == 'Указанное название проекта уже используется в системе', 'Не появилась ошибка о неуникальном названии проекта'

    @testit.workItemIds(1470)
    @testit.displayName("1.1.1 Создание проекта с неуникальным кодом")
    @pytest.mark.smoke
    @allure.title("id-1470 1.1.1 Создание проекта с неуникальным кодом")
    def test_creating_a_project_with_non_unique_code(self, simple_project, login, driver):
        # Создаем проект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        create_project_drawer_page.create_project(
            "TestProject",
            'ATP',
            USER_NAME,
            'no',
            '01.10.2022'
        )
        error = create_project_drawer_page.get_mui_error_text()
        assert error == 'Указанный код проекта уже используется в системе', 'Не появилась ошибка о неуникальном коде проекта'

    @testit.workItemIds(3134)
    @testit.displayName("1.1.1 Создание проекта с указанием даты окончания проекта раньше даты начала")
    @pytest.mark.smoke
    @allure.title("id-3134 1.1.1 Создание проекта с указанием даты окончания проекта раньше даты начала")
    def test_entering_an_end_date_before_the_project_start_date(self, login, driver):
        # Создаем проект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        create_project_drawer_page.create_project(
            "AutoTestProject",
            'ATP',
            USER_NAME,
            'no',
            '01.10.2022',
            '01.09.2022'
        )
        error = create_project_drawer_page.get_mui_error_text()
        assert error == 'Дата окончания проекта не должна быть раньше даты начала', 'Не появилась ошибка о несоответствии даты начала и окончания проекта'

    @testit.workItemIds(3135)
    @testit.displayName("1.1.1 Н. Ввод недопустимых символов в поле Название проекта")
    @pytest.mark.regress
    @allure.title("id-3135 1.1.1 Н. Ввод недопустимых символов в поле Название проекта")
    def test_entering_invalid_characters_in_the_project_name_field(self, login, driver):
        # Создаем проект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        create_project_drawer_page.create_project(
            "AutoTestProject)(,",
            'ATP',
            USER_NAME,
            'no',
            '01.10.2022'
        )
        error = create_project_drawer_page.get_mui_error_text()
        assert error == 'Значение в поле содержит недопустимые символы', 'Не появилась ошибка о недопустимых символах'

    @testit.workItemIds(3133)
    @testit.displayName("1.1.1 Н. Ввод недопустимых символов в поле Код проекта")
    @pytest.mark.regress
    @allure.title("id-3133 1.1.1 Н. Ввод недопустимых символов в поле Код проекта")
    def test_entering_invalid_characters_in_the_project_code_field(self, login, driver):
        # Создаем проект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        create_project_drawer_page.create_project(
            "AutoTestProject",
            'ATP)(,',
            USER_NAME,
            'no',
            '01.10.2022'
        )
        error = create_project_drawer_page.get_mui_error_text()
        assert error == 'Значение в поле содержит недопустимые символы', 'Не появилась ошибка о недопустимых символах'

    @testit.workItemIds(3131)
    @testit.displayName("1.1.1 Н. Превышение допустимого количества символов в поле Название проекта")
    @pytest.mark.regress
    @allure.title("id-3131 1.1.1 Н. Превышение допустимого количества символов в поле Название проекта")
    def test_exceeding_the_allowed_number_of_characters_in_the_project_name_field(self, login, driver):
        # Создаем проект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        create_project_drawer_page.create_project(
            "Lorem ipsum dolor sit amet consectetuer adipiscing elit sed diam nonummy nibh euismod tincidunt utttt",
            'ATP',
            USER_NAME,
            'no',
            '01.10.2022'
        )
        error = create_project_drawer_page.get_mui_error_text()
        assert error == 'Максимальное количество символов: 100', 'Не появилась ошибка о превышении максимального количества символов'

    @testit.workItemIds(3132)
    @testit.displayName("1.1.1 Н. Превышение допустимого количества символов в поле Код проекта")
    @pytest.mark.regress
    @allure.title("id-3132 1.1.1 Н. Превышение допустимого количества символов в поле Код проекта")
    def test_exceeding_the_allowed_number_of_characters_in_the_project_code_field(self, login, driver):
        # Создаем проект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        create_project_drawer_page.create_project(
            "AutoTestProject",
            'AutoTestPro',
            USER_NAME,
            'no',
            '01.10.2022'
        )
        error = create_project_drawer_page.get_mui_error_text()
        assert error == 'Максимальное количество символов: 10', 'Не появилась ошибка о превышении максимального количества символов'

    @testit.workItemIds(284)
    @testit.displayName("1.3.2.2 Назначение руководителя проекта при создании проекта")
    @pytest.mark.regress
    @allure.title("id-284 1.3.2.2 Назначение руководителя проекта при создании проекта")
    def test_appointment_of_a_project_manager_when_creating_a_project(self, login, driver):
        # Создаем проект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        create_project_drawer_page.create_project(
            "AutoTestProject",
            'AutoTest',
            USER_NAME,
            'no',
            '01.10.2022'
        )
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_description_tab()
        description_list = project_card_page.get_project_description()
        # Удаляем проект
        project_endpoint = ProjectEndpoint()
        project_endpoint.delete_project_by_name_api("AutoTestProject")
        assert USER_NAME in description_list[4], \
            "Выбранный руководитель проекта не отображается в поле Руководитель проекта"
