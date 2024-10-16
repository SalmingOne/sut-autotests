import time

import allure
import pytest
import testit

from endpoints.affiliates_endpoint import AffiliatesEndpoint
from endpoints.project_roles_endpoint import ProjectRolesEndpoint
from pages.labor_cost_page import LaborCostPage
from pages.pivot_tab_filter_page import PivotTabFilterPage
from pages.pivot_tab_page import PivotTabPage


@allure.suite("Дровер фильтрации сводной таблицы")
class TestPivotTabFilterPage:

    @testit.workItemIds(1194)
    @testit.displayName("3.2.2.15.1 Реакция системы на нажатие кнопки Сбросить все на табе По проектам.")
    @pytest.mark.regress
    @allure.title("id-1194 3.2.2.15.1 Реакция системы на нажатие кнопки Сбросить все на табе По проектам.")
    def test_reset_all_button_on_filter(self, login, driver):
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(2)  # Без ожидания открывается фильтр на странице трудозатрат вместо сводной таблицы
        pivot_tab_page.open_filter()
        pivot_tab_filter_page = PivotTabFilterPage(driver)
        before_changes = pivot_tab_filter_page.get_element_text('checked')
        pivot_tab_filter_page.click_random_checkbox()
        outer_changes = pivot_tab_filter_page.get_element_text('checked')
        pivot_tab_filter_page.click_reset_button()
        outer_reset = pivot_tab_filter_page.get_element_text('checked')
        assert before_changes != outer_changes, "Настройки фильтров не изменились"
        assert outer_reset == ['Bсе проекты', 'Почасовая оплата', 'По окладу', 'Пользователи без филиалов',
                               'Показывать активность пользователя'], ("После сброса не все фильтры восстановились по "
                                                                       "умолчанию")

    @testit.workItemIds(1187)
    @testit.displayName("3.2.2.15.1 Содержание дропдауна с фильтрами при просмотре сводной таблицы  По проектам")
    @pytest.mark.regress
    @allure.title("id-1187 3.2.2.15.1 Содержание дропдауна с фильтрами при просмотре сводной таблицы  По проектам")
    def test_content_dropdown_filter(self, login, driver):
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(2)  # Без ожидания открывается фильтр на странице трудозатрат вместо сводной таблицы
        pivot_tab_page.open_filter()
        pivot_tab_filter_page = PivotTabFilterPage(driver)
        all_elements = pivot_tab_filter_page.get_element_text('all')
        pivot_tab_filter_page.open_filial_dropdown()
        filial_dropdown_elements = pivot_tab_filter_page.get_element_text('dropdown')
        pivot_tab_filter_page.open_filial_dropdown()
        pivot_tab_filter_page.open_integration_dropdown()
        integration_dropdown_elements = pivot_tab_filter_page.get_element_text('dropdown')
        assert all_elements == ['Неактивные пользователи', 'Неактивные проекты', 'Bсе проекты', 'Участник',
                                'Руководитель проекта', 'Мои проекты', 'Почасовая оплата', 'По окладу',
                                'Пользователи без филиалов', 'Активности по интеграциям', 'Показывать причины списания',
                                'Показывать активность пользователя'], "На дропдауне фильтрации сводной таблицы есть не все чек-боксы и радио-кнопки"
        assert 'Выбрать всё' in filial_dropdown_elements, "Нет кнопки выбрать все филиалы"
        assert integration_dropdown_elements == ['Выбрать все активности', 'Выбрать все активности Jira',
                                                 'Задача создана (Jira)', 'Добавлен комментарий (Jira)',
                                                 'Задача изменила статус (Jira)', 'Задача отредактирована (Jira)',
                                                 'Выбрать все активности Bitbucket', 'Commits (Bitbucket)',
                                                 'Pull requests (Bitbucket)', 'Code review (Bitbucket)',
                                                 'Выбрать все активности Confluence', 'Страница (Confluence)',
                                                 'Вложение (Confluence)', 'Комментарий (Confluence)',
                                                 'Страница-блог (Confluence)', 'Пространство (Confluence)',
                                                 'Не определено (Confluence)', 'Выбрать все активности Test IT',
                                                 'Создание (Test IT)', 'Прохождение тест кейсов (Test IT)',
                                                 'Выбрать все активности Gitlab', 'Code review (Gitlab)',
                                                 'Commits (Gitlab)', 'Закрыто issue (Gitlab)',
                                                 'Количество комментариев issue (Gitlab)', 'Открыто issue (Gitlab)',
                                                 'Merge requests (Gitlab)', 'Задач закрыто (Gitlab)',
                                                 'Задач открыто (Gitlab)'], "Не все интеграции есть в дропдауне интеграций"

    @testit.workItemIds(1163)
    @testit.displayName("3.2.2.15.2 Проверка сохранения фильтрации, выбранной пользователем на табе По пользователям")
    @pytest.mark.regress
    @allure.title("id-1163 3.2.2.15.2 Проверка сохранения фильтрации, выбранной пользователем на табе По пользователям")
    def test_checking_whether_filtering_selected_by_user_is_saved(self, login, driver):
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(1)
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.open_filter()
        pivot_tab_filter_page = PivotTabFilterPage(driver)
        before_changes = pivot_tab_filter_page.get_element_text('checked')
        pivot_tab_filter_page.click_random_checkbox()
        outer_changes = pivot_tab_filter_page.get_element_text('checked')
        pivot_tab_filter_page.press_submit_button()
        labor_cost_page = LaborCostPage(driver)
        labor_cost_page.go_to_labor_cost_page()
        pivot_tab_page.go_to_pivot_page_not_wait()
        time.sleep(3)
        pivot_tab_page.open_filter()
        outer_return = pivot_tab_filter_page.get_element_text('checked')
        assert before_changes != outer_changes, "Выбранные в фильтре чек-боксы не изменились"
        assert outer_changes == outer_return, \
            "При переходе на другую страницу и возвращение обратно не сохранились выбранные чекбоксы"

    @testit.workItemIds(1164)
    @testit.displayName("3.2.2.15.2 Содержание окна фильтра на табе По пользователям")
    @pytest.mark.regress
    @allure.title("id-1164 3.2.2.15.2 Содержание окна фильтра на табе По пользователям")
    def test_content_dropdown_filter_by_user(self, login, driver):
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(2)  # Без ожидания открывается фильтр на странице трудозатрат вместо сводной таблицы
        pivot_tab_page.go_to_by_user_tab()
        pivot_tab_page.open_filter()
        pivot_tab_filter_page = PivotTabFilterPage(driver)
        all_elements = pivot_tab_filter_page.get_element_text('all')
        checked_elements = pivot_tab_filter_page.get_element_text('checked')
        pivot_tab_filter_page.open_project_roles_dropdown()
        project_roles_dropdown = pivot_tab_filter_page.get_element_text('dropdown')
        # Дропдаун проектные роли
        project_roles_endpoint = ProjectRolesEndpoint()
        project_roles_system = project_roles_endpoint.get_all_project_roles_name()
        checked_in_roles = pivot_tab_filter_page.get_element_text('checked')
        pivot_tab_filter_page.action_esc()
        assert 'Выбрать все' in checked_in_roles, \
            "В дропдауне проектные роли кнопка Выбрать все не выбрана по умолчанию"
        project_roles_dropdown.remove('Выбрать все')
        assert project_roles_dropdown == project_roles_system, "В дропдауне есть не все проектные роли"
        # Дропдаун филиалы
        affiliates_endpoint = AffiliatesEndpoint()
        system_filial_name = affiliates_endpoint.get_all_affiliates_name()
        pivot_tab_filter_page.open_filial_dropdown()
        filial_dropdown_elements = pivot_tab_filter_page.get_element_text('dropdown')
        checked_in_filial = pivot_tab_filter_page.get_element_text('checked')
        assert 'Выбрать всё' in checked_in_filial, "В дропдауне филиалов кнопка Выбрать все не выбрана по умолчанию"
        filial_dropdown_elements.remove('Выбрать всё')
        assert filial_dropdown_elements == system_filial_name, "В дропдауне есть не все филиалы"
        pivot_tab_filter_page.action_esc()
        # Дропдаун интеграции
        pivot_tab_filter_page.check_integration_field_not_clickable()
        pivot_tab_filter_page.open_integration_dropdown()
        integration_dropdown_elements = pivot_tab_filter_page.get_element_text('dropdown')
        assert all_elements == ['Неактивные пользователи', 'Неактивные проекты', 'Пользователей с переработками',
                                'Пользователей с ежегодным отпуском', 'Пользователей с больничным',
                                'Пользователей с административным отпуском', 'Пользователей с декретным отпуском',
                                'Почасовая оплата', 'По окладу', 'Пользователи без филиалов',
                                'Активности по интеграциям', 'Показывать причины списания',
                                'Показывать активность пользователя'], "В дровере есть не все чекбоксы"
        assert checked_elements == ['Почасовая оплата', 'По окладу', 'Пользователи без филиалов',
                                    'Показывать активность пользователя'], \
            "Не все необходимые чекбоксы выбраны по умолчанию "
        assert integration_dropdown_elements == ['Выбрать все активности', 'Выбрать все активности Jira',
                                                 'Задача создана (Jira)', 'Добавлен комментарий (Jira)',
                                                 'Задача изменила статус (Jira)', 'Задача отредактирована (Jira)',
                                                 'Выбрать все активности Bitbucket', 'Commits (Bitbucket)',
                                                 'Pull requests (Bitbucket)', 'Code review (Bitbucket)',
                                                 'Выбрать все активности Confluence', 'Страница (Confluence)',
                                                 'Вложение (Confluence)', 'Комментарий (Confluence)',
                                                 'Страница-блог (Confluence)', 'Пространство (Confluence)',
                                                 'Не определено (Confluence)', 'Выбрать все активности Test IT',
                                                 'Создание (Test IT)', 'Прохождение тест кейсов (Test IT)',
                                                 'Выбрать все активности Gitlab', 'Code review (Gitlab)',
                                                 'Commits (Gitlab)', 'Закрыто issue (Gitlab)',
                                                 'Количество комментариев issue (Gitlab)', 'Открыто issue (Gitlab)',
                                                 'Merge requests (Gitlab)', 'Задач закрыто (Gitlab)',
                                                 'Задач открыто (Gitlab)'], \
            "Не все интеграции есть в дропдауне интеграций"
