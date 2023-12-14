import time

import allure
import pytest

from pages.pivot_tab_filter_page import PivotTabFilterPage
from pages.pivot_tab_page import PivotTabPage


@allure.suite("Дровер фильтрации сводной таблицы по проектам")
class TestPivotTabFilterPage:

    #  id-1194 3.2.2.15.1 Реакция системы на нажатие кнопки "Сбросить все" на табе "По проектам".
    @pytest.mark.demo
    @allure.title("id-1194 3.2.2.15.1 Реакция системы на нажатие кнопки Сбросить все на табе По проектам.")
    def test_reset_all_button_on_filter(self, login, driver):
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(1)  # Без ожидания открывается фильтр на странице трудозатрат вместо сводной таблицы
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

#  id-1187 3.2.2.15.1 Содержание дропдауна с фильтрами при просмотре сводной таблицы "По проектам".
    @allure.title("id-1187 3.2.2.15.1 Содержание дропдауна с фильтрами при просмотре сводной таблицы  По проектам")
    def test_content_dropdown_filter(self, login, driver):
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(1)  # Без ожидания открывается фильтр на странице трудозатрат вместо сводной таблицы
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
