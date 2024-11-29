import time

import allure
import pytest
import testit

from data.data import USER_ID
from data.models.create_project_model import CreateProject
from endpoints.gantt_endpoint import GanttEndpoint
from endpoints.users_endpoint import UserEndpoint
from pages.all_project_page import AllProjectPage
from pages.gantt_page import GanttPage


@allure.suite("Диаграмма ганта")
class TestGanttPage:

    @testit.workItemIds(1296)
    @testit.displayName("14.2.1 Создание фазы")
    @pytest.mark.smoke
    @allure.title("id-1296 14.2.1 Создание фазы")
    def test_creating_a_phase(self, project_with_assignment, login, driver):
        gantt_page = GanttPage(driver)
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(CreateProject().name)
        gantt_page.go_to_gantt_tab()
        gantt_page.add_phase('Фаза 1')
        gantt_page.check_start_and_end_dates('Фаза 1')
        gantt_page.check_status('Фаза 1')

    @testit.workItemIds(3053)
    @testit.displayName('14.1.4 Реакция системы на включение\выключение свитча "Таблица"')
    @pytest.mark.regress
    @allure.title('id-3053 14.1.4 Реакция системы на включение\выключение свитча "Таблица"')
    def test_table_switch_on_off(self, project_with_completed_task, login, driver):
        gantt_page = GanttPage(driver)
        user_endpoint = UserEndpoint()
        user_name = user_endpoint.get_user_by_id(str(USER_ID)).json()['fullName']
        task_name = project_with_completed_task[2]
        start_date, end_date = [day.strftime("%d.%m") for day in gantt_page.get_current_week_start_end()]
        start_date = start_date if start_date != gantt_page.get_day_before_d_m(0) else gantt_page.get_day_before_d_m(1)
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_completed_task[0]['name'])
        gantt_page.go_to_gantt_tab()
        time.sleep(2)
        gantt_page.toggle_checkbox('Таблица')
        assert gantt_page.get_status_of_gantt_task(), "Диаграмма Ганта не отображается"
        assert gantt_page.get_status_of_checkbox('Таблица', 'Не активно'), "Чекбокс Таблица активен"
        time.sleep(2)
        assert {'number'} == gantt_page.get_columns_types(), 'Таблица содержит все столбцы'
        assert f'Задача: {task_name} | ({start_date} - {end_date})\nИсполнители: {user_name}' == gantt_page.get_tooltip_text(project_with_completed_task[2]), "Неверный текст тултипа"
        gantt_page.toggle_checkbox('Таблица')
        assert gantt_page.get_status_of_gantt_task(), "Диаграмма Ганта не отображается"
        assert gantt_page.get_status_of_checkbox('Таблица', 'Активно'), "Чекбокс Таблица не активен"
        assert {'planned_labor_costs', 'end_date', 'name', 'start_date', 'actions', 'number'} == gantt_page.get_columns_types(), "Таблица не содержит все столбцы"
        gantt_page.toggle_checkbox('Диаграмма')
        assert gantt_page.get_status_of_checkbox('Таблица', 'Активно'), "Чекбокс Таблица не активен"
        assert gantt_page.get_status_of_checkbox('Диаграмма', 'Не активно'), "Чекбокс Диаграмма активен"
        assert {'planned_labor_costs', 'end_date', 'name', 'start_date', 'actions', 'number'} == gantt_page.get_columns_types(), "Таблица не содержит все столбцы"
        assert not gantt_page.get_status_of_gantt_task(), "Диаграмма Ганта отображается"
        gantt_page.toggle_checkbox('Таблица')
        assert gantt_page.get_status_of_checkbox('Таблица', 'Не активно'), "Чекбокс Таблица активен"
        assert gantt_page.get_status_of_checkbox('Диаграмма', 'Активно'), "Чекбокс Диаграмма не активен"
        assert {'number'} == gantt_page.get_columns_types(), 'Таблица содержит все столбцы'
        assert gantt_page.get_status_of_gantt_task(), "Диаграмма Ганта не отображается"

    @testit.workItemIds(3057)
    @testit.displayName('14.1.4 Реакция системы на включение\выключение свитча "Диаграмма"')
    @pytest.mark.regress
    @allure.title('id-3057 14.1.4 Реакция системы на включение\выключение свитча "Диаграмма"')
    def test_diagram_switch_on_off(self, project_with_completed_task, login, driver):
        gantt_page = GanttPage(driver)
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_completed_task[0]['name'])
        gantt_page.go_to_gantt_tab()
        time.sleep(2)
        gantt_page.toggle_checkbox('Диаграмма')
        assert not gantt_page.get_status_of_gantt_task(), "Диаграмма Ганта отображается"
        assert gantt_page.get_status_of_checkbox('Диаграмма', 'Не активно'), "Чекбокс Диаграмма активен"
        assert {'planned_labor_costs', 'end_date', 'name', 'start_date', 'actions',
                'number'} == gantt_page.get_columns_types(), "Таблица не содержит все столбцы"
        time.sleep(2)
        gantt_page.toggle_checkbox('Диаграмма')
        assert gantt_page.get_status_of_gantt_task(), "Диаграмма Ганта не отображается"
        assert gantt_page.get_status_of_checkbox('Диаграмма', 'Активно'), "Чекбокс Диаграмма не активен"
        assert {'planned_labor_costs', 'end_date', 'name', 'start_date', 'actions',
                'number'} == gantt_page.get_columns_types(), "Таблица не содержит все столбцы"
        gantt_page.toggle_checkbox('Таблица')
        assert gantt_page.get_status_of_checkbox('Таблица', 'Не активно'), "Чекбокс Таблица активен"
        assert {'number'} == gantt_page.get_columns_types(), "Таблица содержит все столбцы"
        assert gantt_page.get_status_of_gantt_task(), "Диаграмма Ганта не отображается"
        gantt_page.toggle_checkbox('Диаграмма')
        assert gantt_page.get_status_of_checkbox('Диаграмма', 'Не активно'), "Чекбокс Диаграмма активен"
        assert gantt_page.get_status_of_checkbox('Таблица', 'Активно'), "Чекбокс Таблица не активен"
        assert {'planned_labor_costs', 'end_date', 'name', 'start_date', 'actions',
                'number'} == gantt_page.get_columns_types(), "Таблица не содержит все столбцы"
        assert not gantt_page.get_status_of_gantt_task(), "Диаграмма Ганта не отображается"

    @testit.workItemIds(3457)
    @testit.displayName('14.1.2 Реакция системы при нажатии на кнопку редактирования, если диаграмма редактируется другим пользователем')
    @pytest.mark.regress
    @allure.title('id-3457 14.1.2 Реакция системы при нажатии на кнопку редактирования, если диаграмма редактируется другим пользователем')
    def test_edit_locked_diagram(self, project_with_assignment, login, driver):
        gantt_page = GanttPage(driver)
        all_project_page = AllProjectPage(driver)
        gantt_endpoint = GanttEndpoint()
        gantt_endpoint.start_editing_by_other_user(project_with_assignment[0]['id'])
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_assignment[0]['name'])
        gantt_page.go_to_gantt_tab()
        time.sleep(2)
        gantt_page.edit_diagram()
        assert 'Проект уже редактируется другим пользователем' in gantt_page.get_errors_on_page(), 'Нет сообщения системы о редактировании диаграммы другим пользователем'

    @testit.workItemIds(3027)
    @testit.displayName('14.1.2 Сохранение редактирования диаграммы Ганта')
    @pytest.mark.regress
    @allure.title('id-3027 14.1.2 Сохранение редактирования диаграммы Ганта')
    def test_save_diagram_changes(self, project_with_assignment, login, driver):
        gantt_page = GanttPage(driver)
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_assignment[0]['name'])
        gantt_page.go_to_gantt_tab()
        time.sleep(2)
        gantt_page.edit_diagram()
        gantt_page.add_phase('Новолуние')
        gantt_page.save_changes()
        assert 'Новолуние' in gantt_page.get_phases_name(), 'Изменения не сохранены'
        assert gantt_page.get_status_of_gantt_task(), "Диаграмма Ганта не отображается"

    @testit.workItemIds(3028)
    @testit.displayName('14.1.2 Отмена редактирования диаграммы Ганта')
    @pytest.mark.regress
    @allure.title('id-3028 14.1.2 Отмена редактирования диаграммы Ганта')
    def test_discard_diagram_changes(self, project_with_assignment, login, driver):
        gantt_page = GanttPage(driver)
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_assignment[0]['name'])
        gantt_page.go_to_gantt_tab()
        time.sleep(2)
        gantt_page.edit_diagram()
        gantt_page.add_phase('Полнолуние')
        gantt_page.discard_changes(confirm=True)
        time.sleep(5)
        assert 'Полнолуние' not in gantt_page.get_phases_name(), "Изменения сохранены"
        assert gantt_page.get_status_of_gantt_task(), "Диаграмма Ганта не отображается"

    @testit.workItemIds(4303)
    @testit.displayName('14.1.2 Выбор кнопки "Отмена" в модальном окне отмены изменений')
    @pytest.mark.regress
    @allure.title('id-4303 14.1.2 Выбор кнопки "Отмена" в модальном окне отмены изменений')
    def test_discard_diagram_changes(self, project_with_assignment, login, driver):
        gantt_page = GanttPage(driver)
        all_project_page = AllProjectPage(driver)
        all_project_page.go_to_all_project_page()
        all_project_page.go_project_page(project_with_assignment[0]['name'])
        gantt_page.go_to_gantt_tab()
        time.sleep(2)
        gantt_page.edit_diagram()
        gantt_page.add_phase('Полнолуние')
        gantt_page.discard_changes(confirm=False)
        time.sleep(5)
        gantt_page.buttons_are_displayed()
        assert 'Полнолуние' in gantt_page.get_phases_name(), "Внесенные ранее изменения не отображаются"
        assert gantt_page.get_status_of_gantt_task(), "Диаграмма Ганта не отображается"