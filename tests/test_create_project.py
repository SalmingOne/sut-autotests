from pages.all_project_page import AllProjectPage
from pages.create_project_drawer_page import CreateProjectDrawerPage
from pages.labor_cost_page import LaborCostPage
from pages.project_card_page import ProjectCardPage


# @pytest.mark.smoke_test
class TestCreateProject:
    # id-47 1.1.1 Создание нового проекта
    def test_create_project(self, login, driver):
        # Создаем прект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        project_name, project_code, project_data, project_worker = create_project_drawer_page.create_project('no')
        # Берем данные с карточки проекта
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_description_tab()
        output_project_name, output_project_code, output_project_status, output_project_begin_data, output_project_manager = project_card_page.get_project_description()
        assert project_name == output_project_name, "поле имя проекта не отобразилось в карточке проекта"
        assert project_code == output_project_code, "поле код проекта не отобразилось в карточке проекта"
        assert project_data == output_project_begin_data, "поле дата начала проекта не отобразилось в карточке проекта"
        assert project_worker == output_project_manager, "поле администратор не отобразилось в карточке проекта"
        # Берем имя поректа с старници все проекты
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        check_name_at_all = all_project_page.check_project_name_at_all()
        assert project_name == check_name_at_all, "имя созданного проекта отсутствует на странице все проекты"
        # Берем код проекта со страници трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        check_code_at_labor = labor_cost_page.check_project_code_at_labor()
        assert project_code == check_code_at_labor, "код созданного проекта отсутствует на странице трудозатрат"
        # Пока удаление проекта здесь, планирую позже включить его в фикстуру
        all_project_page.go_to_all_project_page()
        all_project_page.delete_project()

    # id-10157 1.1.1 Создание нового проекта в статусе черновик
    def test_create_project_draft(self, login, driver):
        # Создаем прект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        project_name, project_code, project_data, project_worker = create_project_drawer_page.create_project('draft')

        # Берем данные с карточки проекта
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_description_tab()
        output_project_name, output_project_code, output_project_status, output_project_begin_data, output_project_manager = project_card_page.get_project_description()
        assert project_name == output_project_name, "поле имя проекта не отобразилось в карточке проекта"
        assert project_code == output_project_code, "поле код проекта не отобразилось в карточке проекта"
        assert project_data == output_project_begin_data, "поле дата начала проекта не отобразилось в карточке проекта"
        assert project_worker == output_project_manager, "поле администратор не отобразилось в карточке проекта"

        # Берем код проекта со страници трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        check_code_at_labor = labor_cost_page.check_no_project_code_at_labor()
        assert check_code_at_labor == "no element on page", "проект присутствует на странице трудозатрат"

        # Берем имя поректа с старници все проекты
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()

        check_name_at_all = all_project_page.check_project_name_at_all()
        assert project_name == check_name_at_all, "имя созданного проекта отсутствует на странице все проекты"
        # Пока удаление проекта здесь, планирую позже включить его в фикстуру
        all_project_page.delete_project()

        # id-1469 1.1.1 Добавление нового проекта с обязательным указанием причины списания
    def test_create_project_reason(self, login, driver):
        # Создаем прект
        create_project_drawer_page = CreateProjectDrawerPage(driver)
        create_project_drawer_page.go_to_create_project_drawer_from_menu()
        project_name, project_code, project_data, project_worker = create_project_drawer_page.create_project('reason')

        # Берем данные с карточки проекта
        project_card_page = ProjectCardPage(driver)
        project_card_page.go_to_description_tab()
        output_project_name, output_project_code, output_project_status, output_project_begin_data, output_project_manager = project_card_page.get_project_description()
        assert project_name == output_project_name, "поле имя проекта не отобразилось в карточке проекта"
        assert project_code == output_project_code, "поле код проекта не отобразилось в карточке проекта"
        assert project_data == output_project_begin_data, "поле дата начала проекта не отобразилось в карточке проекта"
        assert project_worker == output_project_manager, "поле администратор не отобразилось в карточке проекта"

        # Берем код проекта со страници трудозатрат
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        labor_cost_page.check_to_have_reason_fo_write()
        # Берем имя поректа с старници все проекты
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        check_name_at_all = all_project_page.check_project_name_at_all()
        assert project_name == check_name_at_all, "имя созданного проекта отсутствует на странице все проекты"
        # Пока удаление проекта здесь, планирую позже включить его в фикстуру
        all_project_page.delete_project()
