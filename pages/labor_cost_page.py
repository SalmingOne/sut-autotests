import os
import time
import datetime
import random

import allure
import testit
from selenium.common import TimeoutException, ElementClickInterceptedException, InvalidArgumentException, \
    StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from data.data import PROJECT_NAME
from data.models.create_project_model import CreateProject
from locators.labor_cost_page_locators import LaborCostPageLocators
from pages.base_page import BasePage
from utils.concat_testit_allure_step import allure_testit_step


class LaborCostPage(BasePage):
    locators = LaborCostPageLocators()

    @testit.step("Переход на таблицу трудозатрат через меню")
    @allure.step("Переход на таблицу трудозатрат через меню")
    def go_to_labor_cost_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_ACTIVITY))
        self.element_is_visible(self.locators.TAB_LABOR_COST_TABLE).click()

    @testit.step("Проверка, что код проекта есть на странице")
    @allure.step("Проверка, что код проекта есть на странице")
    def check_project_code_at_labor(self, project_code):
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        check_code_at_labor = self.element_is_present(self.locators.check_code_project(project_code)).text
        return check_code_at_labor

    @testit.step("Проверка, что кода проекта нет на странице")
    @allure.step("Проверка, что кода проекта нет на странице")
    def check_no_project_code_at_labor(self, project_code):
        try:
            return self.element_is_present(self.locators.check_code_project(project_code)).text
        except TimeoutException:
            return "no element on page"

    @testit.step("Проверка что появляется окно указания причины списания")
    @allure.step("Проверка что появляется окно указания причины списания")
    def check_to_have_reason_fo_write(self, project_name):
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.element_is_visible(self.locators.get_random_day_by_project(project_name)).click()
        assert self.element_is_displayed(self.locators.LABOR_REASON_FIELD), "Не открылось окно указания причины"
        self.element_is_visible(self.locators.BREAK_LABOR_REASON_WINDOW).click()


    @testit.step("Ввод значения в клетку таблицы трудозатрат")
    @allure.step("Ввод значения в клетку таблицы трудозатрат")
    def input_time(self, element, in_time):
        self.element_is_visible(element).click()
        self.element_is_visible(element).send_keys(in_time)
        self.element_is_visible(element).send_keys(Keys.RETURN)

    @testit.step("Ввод значения в клетку таблицы трудозатрат нужного проекта")
    @allure.step("Ввод значения в клетку таблицы трудозатрат нужного проекта")
    def input_labor_reason_by_project(self, project_name, number_day, reason_time):
        self.input_time(self.locators.get_day_by_project(project_name, number_day), reason_time)

    @testit.step("Ввод значения часов трудозатрат в модальном окне при обязательном указании причин трудозатрат")
    @allure.step("Ввод значения часов трудозатрат в модальном окне при обязательном указании причин трудозатрат")
    def input_hours_into_form(self, hours):
        self.element_is_visible(self.locators.INPUT_HOUR_FIELD).send_keys(hours)

    @testit.step("Ввод причины трудозатрат в модальном окне при обязательном указании причин трудозатрат")
    @allure.step("Ввод причины трудозатрат в модальном окне при обязательном указании причин трудозатрат")
    def input_reason_into_form(self, reason):
        self.element_is_visible(self.locators.INPUT_REASON_DESCRIPTION_FIELD).send_keys(reason)

    @testit.step("Списываем трудозатраты за первый и последний день месяца")
    @allure.step("Списываем трудозатраты за первый и последний день месяца")
    def input_work_by_month(self):
        first_day_time = 5  # Первый день текущего периода
        last_day_time = 8  # Первый день текущего периода
        previous_last_day_time = 6  # Первый день предыдущего периода
        next_first_day_time = 3  # Первый день следующего периода
        # Заполняем текущий месяц
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        x, y = self.check_tab_head()
        last_day_number = y + 1
        last_day_locator = (
            By.XPATH,
            f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div[{last_day_number}]//input')
        time.sleep(1)
        self.input_time(last_day_locator, last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        # Переходим на предыдущий месяц и заполняем его
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        x, y = self.check_tab_head()
        last_day_number = y + 1
        last_day_locator = (
            By.XPATH,
            f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div[{last_day_number}]//input')
        self.input_time(last_day_locator, previous_last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        # Переходим на текущий, а потом следующий месяц и заполняем его
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, next_first_day_time)
        try:
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
        except ElementClickInterceptedException:
            pass
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()

        return first_day_time + last_day_time

    @testit.step("Списываем трудозатраты за первый и последний день недели")
    @allure.step("Списываем трудозатраты за первый и последний день недели")
    def input_work_by_week(self):
        first_day_time = 7
        last_day_time = 11
        previous_last_day_time = 8
        next_first_day_time = 2
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        self.input_time(self.locators.LAST_7_DAY_BY_PROJECT, last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        self.input_time(self.locators.LAST_7_DAY_BY_PROJECT, previous_last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()

        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, next_first_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()

        return first_day_time + last_day_time

    @testit.step("Выбираем отображаемый период")
    @allure.step("Выбираем отображаемый период")
    def choose_period(self, period):
        time.sleep(1)
        self.element_is_visible(self.locators.PERIOD_SELECT_BUTTON).click()
        if period == "month":
            self.element_is_visible(self.locators.MONTH_PERIOD_SELECT).click()
        elif period == "week":
            self.element_is_visible(self.locators.WEEK_PERIOD_SELECT).click()

    @testit.step("Выбираем месяц в датапикере")
    @allure.step("Выбираем месяц в датапикере")
    def choose_month_picker(self, month_name):  # имя месяца указывать точно как на экране(с точкой)
        self.element_is_visible(self.locators.MONTH_DATEPICKER).click()
        month = month_name
        month_locator = (By.XPATH, f'//button[text()="{month}"]')
        self.element_is_visible(month_locator).click()

    @testit.step("Списываем трудозатраты за первый и последний день года")
    @allure.step("Списываем трудозатраты за первый и последний день года")
    def input_work_by_year(self):
        first_day_time = 10
        last_day_time = 12
        previous_last_day_time = 9
        next_first_day_time = 4
        # Заполняем первый день года
        self.choose_month_picker('янв.')
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(2)  # Без задержки часто не корректно выбирается месяц
        # Заполняем последний день предыдущего года
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        x, y = self.check_tab_head()
        last_day_number = y + 1
        last_day_locator = (
            By.XPATH,
            f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div[{last_day_number}]//input')
        self.input_time(last_day_locator, previous_last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        time.sleep(2)  # Без задержки часто не корректно выбирается месяц
        # Заполняем последний день текущего года
        self.choose_month_picker('дек.')
        x, y = self.check_tab_head()
        last_day_number = y + 1
        last_day_locator = (
            By.XPATH,
            f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div[{last_day_number}]//input')
        self.input_time(last_day_locator, last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(2)  # Без задержки часто не корректно выбирается месяц
        # Заполняем первый день следующего года
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, next_first_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        return first_day_time + last_day_time

    @testit.step("Проверяем цвет поля при списании трудозатрат")
    @allure.step("Проверяем цвет поля при списании трудозатрат")
    def check_change_color_on_labor_cost_field(self):
        first_day_time = 4
        # Списываем затраты и берем цвета ячейки
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        color_before_save = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT_COLOR).value_of_css_property(
            'background-color')
        reason_in_field = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).get_attribute('placeholder')
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(2)  # Без этого ожидания не успевает прогрузиться белый цвет
        color_after_save = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT_COLOR).value_of_css_property(
            'background-color')
        reason_in_field_after_save = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).get_attribute(
            'placeholder')
        assert color_before_save == 'rgba(255, 251, 233, 1)', "После списания трудозатрат цвет ячейки не жёлтый"
        assert color_after_save == 'rgba(0, 0, 0, 0)', "После сохранения списания цвет не белый"
        assert reason_in_field == str(first_day_time), "Количество часов списания не равно введенному значению"
        assert reason_in_field_after_save == str(first_day_time), "Списание не сохранено"

    @testit.step("Проверяем наличие заголовка Трудозатраты")
    @allure.step("Проверяем наличие заголовка Трудозатраты")
    def check_title(self):
        assert self.element_is_displayed(self.locators.TITLE_PAGE), "Заголовок страницы Трудозатраты отсутствует"

    @testit.step("Проверяем наличие выбора периода")
    @allure.step("Проверяем наличие выбора периода")
    def check_period_select(self):
        self.element_is_visible(self.locators.PERIOD_SELECT_BUTTON).click()
        menu_title_list = self.elements_are_visible(self.locators.PERIOD_MENU_ITEM)
        data = []
        for title in menu_title_list:
            data.append(title.text)
        self.action_esc()
        assert data == ['Месяц (по дням)', 'Неделя'], "Не все периоды отображены для выбора"

    @testit.step("Проверяем наличие кнопки добавления себя на проект")
    @allure.step("Проверяем наличие кнопки добавления себя на проект")
    def check_add_to_project_button(self):
        assert self.element_is_displayed(self.locators.ADD_TO_PROJECT_BUTTON), "Нет кнопки добавления себя на проект"

    @testit.step("Проверяем наличие кнопки добавления переработки")
    @allure.step("Проверяем наличие кнопки добавления переработки")
    def check_add_overtime_work_button(self):
        assert self.element_is_displayed(self.locators.ADD_OVERTIME_WORK_BUTTON), "Нет кнопки добавления переработки"

    @testit.step("Проверяем наличие кнопки добавления отсутствия")
    @allure.step("Проверяем наличие кнопки добавления отсутствия")
    def check_add_absense_button(self):
        assert self.element_is_displayed(self.locators.ADD_ABSENSE_BUTTON), "Нет кнопки добавления отсутствия"

    @testit.step("Проверяем наличие всех параметров фильтрации")
    @allure.step("Проверяем наличие всех параметров фильтрации")
    def check_filter(self):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()
        filter_elements_list = self.elements_are_visible(self.locators.ELEMENTS_ON_FILTER)
        data = []
        for element in filter_elements_list:
            data.append(element.text)
        self.action_esc()
        assert data == ['Код проекта', 'Название проекта', 'Отображать неактивные проекты',
                        'Отображать причины отклонения'], "Отсутствуют элементы в меню фильтрации"

    @testit.step("Проверяем наличие кнопки открытия виджетов")
    @allure.step("Проверяем наличие кнопки открытия виджетов")
    def check_open_widget_button(self):
        assert self.element_is_displayed(self.locators.OPEN_WIDGET_BUTTON), "Кнопки открытия виджетов нет на странице"

    @testit.step("Проверяем наличие кнопки выбора месяца")
    @allure.step("Проверяем наличие кнопки выбора месяца")
    def check_month_picker(self):
        assert self.element_is_displayed(self.locators.MONTH_DATEPICKER), "Нет кнопки выбора месяца"

    @testit.step("Проверяем наличие кнопок следующего и предыдущего периода")
    @allure.step("Проверяем наличие кнопок следующего и предыдущего периода")
    def check_next_previous_buttons(self):
        assert self.element_is_displayed(self.locators.NEXT_PERIOD_BUTTON), "Нет кнопки следующего периода"
        assert self.element_is_displayed(self.locators.PREVIOUS_PERIOD_BUTTON), "Нет кнопки предыдущего периода"

    @testit.step("Возвращаем шапку таблицы трудозатрат и номер последнего дня")
    @allure.step("Возвращаем шапку таблицы трудозатрат и номер последнего дня")
    def check_tab_head(self):
        all_day_list = self.elements_are_present(self.locators.ALL_DAY_NUMBER)
        numbers = []
        for day in all_day_list:
            numbers.append(day.text)
        return numbers, int(numbers[numbers.index('Итого') - 1])

    @testit.step("Проверяем наличие всех дней недели в шапке таблицы")
    @allure.step("Проверяем наличие всех дней недели в шапке таблицы")
    def check_week_days_head(self):
        all_day_list = self.elements_are_present(self.locators.SEVEN_DAY_ON_HEAD)
        numbers = []
        for day in all_day_list:
            numbers.append(day.text)
        day_week = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
        for a in day_week:
            assert a in numbers, "Дня недели нет в заголовке"

    @testit.step("Проверяем наличие красного и белого цвета ячеек в таблице")
    @allure.step("Проверяем наличие красного и белого цвета ячеек в таблице")
    def check_colors_of_days(self):
        if self.element_is_displayed(self.locators.PROJECT_STRING):
            day_list = self.elements_are_visible(self.locators.ALL_DAY_COLORS)
            data = []
            for element in day_list:
                data.append(element.value_of_css_property('background-color'))
            color_list = ['rgba(0, 0, 0, 0)', 'rgba(255, 236, 229, 1)']
            for a in color_list:
                assert a in data, "В таблице нет ячеек красного или белого цвета"
        else:
            pass

    @testit.step("Проверяем наличие выбранных дней при наведении на ячейку таблицы")
    @allure.step("Проверяем наличие выбранных дней при наведении на ячейку таблицы")
    def check_have_selected_days(self):
        if self.element_is_displayed(self.locators.PROJECT_STRING):
            day_list = self.elements_are_visible(self.locators.ALL_DAY_COLORS)
            self.action_move_to_element(day_list[5])
            assert self.element_is_displayed(self.locators.SELECTED_DAYS), ("При наведении на ячейку таблицы на "
                                                                            "странице нет выбранных дней")
        else:
            pass

    @testit.step("Проверяем наличие тултипа при наведении на код проекта")
    @allure.step("Проверяем наличие тултипа при наведении на код проекта")
    def check_tooltip_on_project_code(self):
        if self.element_is_displayed(self.locators.PROJECT_STRING):
            project_list = self.elements_are_visible(self.locators.PROJECT_TITLE)
            self.action_move_to_element(project_list[0])
            assert self.element_is_displayed(self.locators.TOOLTIP), "При наведении на код проекта не появляется тултип"
            return self.element_is_visible(self.locators.TOOLTIP).text
        else:
            pass

    @testit.step("Проверяем наличие кнопок сохранения и отмены")
    @allure.step("Проверяем наличие кнопок сохранения и отмены")
    def check_save_and_disable_buttons(self):
        assert self.element_is_displayed(self.locators.SAVE_BUTTON)
        assert self.element_is_displayed(self.locators.DISABLE_BUTTON)

    @testit.step("Переходим на отображение по имени проекта")
    @allure.step("Переходим на отображение по имени проекта")
    def go_to_filter_by_project_name(self):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()
        self.element_is_visible(self.locators.FILTER_BY_PROJECT_NAME).click()
        self.action_esc()

    @testit.step("Проверяем наличие заголовков в таблицах блока Заявления")
    @allure.step("Проверяем наличие заголовков в таблицах блока Заявления")
    def check_stateman_tabs_heads(self):
        self.element_is_visible(self.locators.PREVIOUS_ABSENCE_CHECKBOX).click()
        all_column = self.elements_are_present(self.locators.STATEMENT_TABS_HEADERS)
        column_names = []
        for name in all_column:
            column_names.append(name.text)
        x = list(set(column_names) - set(['Дата начала', 'Дата окончания', 'Вид отсутствия', 'Действия', 'Файлы', 'Дата',
                                          'Кол-во часов', 'Причина', 'Статус согласования', 'Файлы', 'Тип',
                                          'Проект', 'Действия']))
        assert x == [], "Есть не все столбцы таблиц заявлений"

    @testit.step("Проверяем наличие чекбокса отображения предыдущих отсутствий")
    @allure.step("Проверяем наличие чекбокса отображения предыдущих отсутствий")
    def check_previous_absense_checkbox(self):
        assert self.element_is_displayed(
            self.locators.NEXT_PERIOD_BUTTON), "Нет чекбокса отображения предыдущих отсутствий"

    @testit.step("Проверяем наличие тултипа при наведении на надпись скачать файл")
    @allure.step("Проверяем наличие тултипа при наведении на надпись скачать файл")
    def check_tooltip_on_download_file_text(self):
        if self.element_is_displayed(self.locators.DOWNLOAD_FILE_TEXT):
            download_file_list = self.elements_are_visible(self.locators.DOWNLOAD_FILE_TEXT)
            self.action_move_to_element(download_file_list[0])
            assert self.element_is_displayed(
                self.locators.TOOLTIP), "При наведении на надпись скачать файл не появляется тултип"
        else:
            pass

    @testit.step("Открываем модальное окно указания причины списания")
    @allure.step("Открываем модальное окно указания причины списания")
    def open_reason_window(self, project_name=None):
        if project_name == None:
            self.element_is_visible(self.locators.RANDOM_DAYS_BY_PROJECT).click()
        else:
            self.element_is_visible(self.locators.get_random_day_by_project(project_name)).click()

    @testit.step("Нажать Сохранить в модальном окне указание часов и причины списания трудозатрат")
    @allure.step("Нажать Сохранить в модальном окне указание часов и причины списания трудозатрат")
    def save_hours_and_reason(self):
        self.element_is_visible(self.locators.SAVE_LABOR_REASON_WINDOW_BUTTON).click()

    @testit.step("Проверяем наличие заголовка на модальном окне указания причины списания")
    @allure.step("Проверяем наличие заголовка на модальном окне указания причины списания")
    def check_title_reason_window(self):
        assert self.element_is_displayed(self.locators.TITLE_MODAL_REASON_WINDOW)

    @testit.step("Проверяем наличие полей на модальном окне указания причины списания")
    @allure.step("Проверяем наличие полей на модальном окне указания причины списания")
    def check_fields_reason_window(self):
        assert self.element_is_displayed(self.locators.INPUT_REASON_TIME_FIELD)
        assert self.element_is_displayed(self.locators.INPUT_REASON_DESCRIPTION_FIELD)

    @testit.step("Проверяем наличие кнопок на модальном окне указания причины списания")
    @allure.step("Проверяем наличие кнопок на модальном окне указания причины списания")
    def check_buttons_reason_window(self):
        assert self.element_is_displayed(self.locators.SAVE_LABOR_REASON_WINDOW_BUTTON)
        assert self.element_is_displayed(self.locators.BREAK_LABOR_REASON_WINDOW)

    @testit.step("Закрываем модальное окно указания причины списания")
    @allure.step("Закрываем модальное окно указания причины списания")
    def close_reason_window(self):
        self.element_is_visible(self.locators.BREAK_LABOR_REASON_WINDOW).click()

    @testit.step("Проверяем цвет поля при удалении трудозатрат")
    @allure.step("Проверяем цвет поля при удалении трудозатрат")
    def check_delete_values_on_labor_cost_field(self):
        first_day_time = 10
        # Списываем затраты и берем цвета ячейки
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        reason_in_field = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).get_attribute('placeholder')
        time.sleep(1)  # Без этого ожидания не корректно удаляется значение в ячейке
        # Удаляем списания по проекту
        self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).click()
        self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).send_keys(Keys.RETURN)
        color_before_save = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT_COLOR).value_of_css_property(
            'background-color')
        reason_in_field_after_delete = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).get_attribute(
            'placeholder')
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(1)  # Без этого ожидания не успевает прогрузиться белый цвет
        color_after_save = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT_COLOR).value_of_css_property(
            'background-color')

        assert color_before_save == 'rgba(255, 251, 233, 1)', "После удаления списания цвет ячейки не жёлтый"
        assert color_after_save == 'rgba(0, 0, 0, 0)', "После сохранения удаления списания цвет не белый"
        assert reason_in_field_after_delete != reason_in_field, "Списание не удалено"

    @testit.step("Вводим в поле не сохраненные трудозатраты")
    @allure.step("Вводим в поле не сохраненные трудозатраты")
    def input_unsaved_values_on_labor_cost_field(self):
        first_day_time = 18
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        return str(first_day_time)

    @testit.step("Проверяем наличие элементов на окне уведомления о не сохраненных данных")
    @allure.step("Проверяем наличие элементов на окне уведомления о не сохраненных данных")
    def check_unsaved_data_window(self):
        assert self.element_is_displayed(self.locators.UNSAVED_WINDOW_TITLE)
        assert self.element_is_displayed(self.locators.UNSAVED_WINDOW_ACCEPT_BUTTON)
        assert self.element_is_displayed(self.locators.UNSAVED_WINDOW_ABORT_BUTTON)
        self.element_is_visible(self.locators.UNSAVED_WINDOW_ACCEPT_BUTTON).click()

    @testit.step("Берем текст в поле после возвращения на страницу трудозатрат")
    @allure.step("Берем текст в поле после возвращения на страницу трудозатрат")
    def get_values_on_labor_cost_field_to_check(self):
        return self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).text

    @testit.step("Получаем номера всех дней где не было списано трудозатрат")
    @allure.step("Получаем номера всех дней где не было списано трудозатрат")
    def get_numbers_days_reason(self, have_reason):
        in_total_list = self.elements_are_visible(self.locators.ALL_IN_TOTAL)
        data = []
        for i in in_total_list:
            data.append(i.text)
        data.remove('Итого')
        if have_reason == 'have':
            return [i for i, data in enumerate(data) if data != '0']
        elif have_reason == 'zero':
            return list(set([i for i, data in enumerate(data) if data == '0']) - set(self.get_absence_day_numbers()))

    @testit.step("Добавляем отсутствие")
    @allure.step("Добавляем отсутствие")
    def add_absence(self, number_day_element, absence_tipe, previous_month=None):
        self.element_is_visible(self.locators.ADD_ABSENSE_BUTTON).click()
        self.element_is_visible(self.locators.OPEN_ABSENCE_CHOOSE_BUTTON).click()
        if absence_tipe == 'vacation':
            self.element_is_visible(self.locators.VACATION).click()
        elif absence_tipe == 'administrative_leave':
            self.element_is_visible(self.locators.ADMINISTRATIVE_LEAVE).click()
        elif absence_tipe == 'sick_leave':
            self.element_is_visible(self.locators.SICK_LEAVE).click()
        elif absence_tipe == 'maternity_leave':
            self.element_is_visible(self.locators.MATERNITY_LEAVE).click()
        # Проставить нужную дату в начале
        self.element_is_visible(self.locators.BEGIN_LEAVE_DATA_PICKER_BUTTON).click()
        if previous_month == 'yeas':
            self.element_is_visible(self.locators.PREVIOUS_MONTH_IN_DATA_PICKER).click()
        else:
            pass
        self.elements_are_visible(self.locators.ALL_DATA_IN_DATA_PICKER)[number_day_element].click()
        this_day_text = self.element_is_visible(self.locators.BEGIN_LEAVE_DATA_INPUT).get_attribute('value')
        self.element_is_visible(self.locators.END_LEAVE_DATA_INPUT).send_keys(this_day_text)
        time.sleep(1.5)
        self.element_is_visible(self.locators.END_LEAVE_DATA_INPUT).send_keys(Keys.RETURN)
        try:
            self.add_file('отсутствие.docx', 'Отсутствие')
            self.element_is_present(self.locators.FILE_INPUT, 2).send_keys(os.path.abspath(r'../отсутствие.docx'))
            assert self.element_is_displayed(self.locators.check_text('отсутствие.docx')), "Файл не добавился"
        except TimeoutException:
            self.element_is_visible(self.locators.BEGIN_LEAVE_DATA_INPUT).click()
        self.element_is_visible(self.locators.DRAWER_SAVE_BUTTON).click()
        time.sleep(1.5)
        self.delete_file('отсутствие.docx')

    @testit.step("Проверяем наличие всех отсутствий в таблице")
    @allure.step("Проверяем наличие всех отсутствий в таблице")
    def check_absence_on_tab(self):
        project_name = self.elements_are_visible(self.locators.ALL_PROJECT_NAMES)[0].get_attribute(
            'aria-label')
        all_day_list = self.elements_are_present(self.locators.all_day_by_project(project_name))
        all_day_value = []
        for day in all_day_list:
            all_day_value.append(day.get_attribute('placeholder'))
        count = 0
        absences_title = ['От', 'А', 'Б', 'Д']
        for a in absences_title:
            try:
                assert a in all_day_value, "В таблице присутствуют не все отсутствия"
                count += 1
            except AssertionError:
                pass
        return count

    @testit.step("Получаем номера дней в которые были отсутствия")
    @allure.step("Получаем номера дней в которые были отсутствия")
    def get_absence_day_numbers(self):
        project_name = self.elements_are_visible(self.locators.ALL_PROJECT_NAMES)[0].get_attribute(
            'aria-label')
        all_day_list = self.elements_are_present(self.locators.all_day_by_project(project_name))
        all_day_value = []
        for day in all_day_list:
            all_day_value.append(day.get_attribute('placeholder'))
        data = [i for i, all_day_value in enumerate(all_day_value) if
                all_day_value == 'Б' or all_day_value == 'От' or all_day_value == 'А' or all_day_value == 'Д']
        return data

    @testit.step("Проверяем наличие сообщения о наложении отсутствий")
    @allure.step("Проверяем наличие сообщения о наложении отсутствий")
    def check_outer_absence(self):
        assert self.element_is_displayed(self.locators.HAVE_OUTER_LEAVE), "Сообщение о наложении отсутствий отсутствует"
        self.element_is_visible(self.locators.DRAWER_ABORT_BUTTON).click()

    @testit.step("Добавляем отсутствие в день где списаны трудозатраты и проверяем сообщение о наложении")
    @allure.step("Добавляем отсутствие в день где списаны трудозатраты и проверяем сообщение о наложении")
    def add_absence_to_reason_day(self):
        days_have_reason = self.get_numbers_days_reason("have")
        self.add_absence(days_have_reason[0], 'sick_leave')
        self.element_is_visible(self.locators.SAVE_WINDOW_BUTTON).click()
        assert self.element_is_displayed(
            self.locators.HAVE_REASON), "Сообщение о наложении отсутствия на трудозатраты не появилось"
        self.element_is_visible(self.locators.DRAWER_ABORT_BUTTON).click()

    @allure.step("Переходим на предыдущий период")
    def go_to_previous_period(self):
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()

    @testit.step("Добавляем переработку")
    @allure.step("Добавляем переработку")
    def add_overtime_work(self, number_day_element, overtime_work_hours, project_mame=None):
        self.element_is_visible(self.locators.ADD_OVERTIME_WORK_BUTTON).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_PICKER).click()
        self.elements_are_visible(self.locators.ALL_DATA_IN_DATA_PICKER)[number_day_element].click()

        self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        if project_mame is not None:
            self.element_is_visible(self.locators.chose_project_on_overtime_work_drawer(project_mame)).click()
        else:
            self.elements_are_visible(self.locators.ALL_PROJECT_ON_DRAWER_INPUT)[0].click()
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(overtime_work_hours)
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(Keys.RETURN)
        try:
            self.add_file('отсутствие.docx', 'Отсутствие')
            self.element_is_present(self.locators.FILE_INPUT, 2).send_keys(os.path.abspath(r'../отсутствие.docx'))
        except TimeoutException:
            pass
        self.action_move_to_element(self.element_is_present(self.locators.OVERTIME_WORK_SAVE_BUTTON))
        self.element_is_present(self.locators.OVERTIME_WORK_SAVE_BUTTON).click()
        time.sleep(1)
        self.delete_file('отсутствие.docx')

    @testit.step("Получаем текст ошибки")
    @allure.step("Получаем текст ошибки")
    def get_mui_error_text(self):
        output_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_present(self.locators.DRAWER_ABORT_BUTTON).click()
        return output_text

    @testit.step("Проверяем добавление пробела в поле обязательного указания переработки")
    @allure.step("Проверяем добавление пробела в поле обязательного указания переработки")
    def check_overtime_work_space_in_reason_field(self, number_day_element, overtime_work_hours, reason):
        self.element_is_visible(self.locators.ADD_OVERTIME_WORK_BUTTON).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_PICKER).click()
        self.elements_are_visible(self.locators.ALL_DATA_IN_DATA_PICKER)[number_day_element].click()
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(overtime_work_hours)
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.elements_are_visible(self.locators.ALL_PROJECT_ON_DRAWER_INPUT)[0].click()

        self.element_is_visible(self.locators.OVERTIME_REASON_INPUT).send_keys(reason)
        try:
            self.add_file('отсутствие.docx', 'Отсутствие')
            self.element_is_present(self.locators.FILE_INPUT, 2).send_keys(os.path.abspath(r'../отсутствие.docx'))
        except TimeoutException:
            pass
        self.action_move_to_element(self.element_is_present(self.locators.OVERTIME_WORK_SAVE_BUTTON))
        self.element_is_present(self.locators.OVERTIME_WORK_SAVE_BUTTON).click()
        output_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_present(self.locators.DRAWER_ABORT_BUTTON).click()
        self.delete_file('отсутствие.docx')
        return output_text

    @testit.step("Проверяем, что кнопка сохранения задизейблена и возвращаем текст тултипа")
    @allure.step("Проверяем, что кнопка сохранения задизейблена и возвращаем текст тултипа")
    def check_disable_submit_button_and_tooltip(self):
        self.element_is_visible(self.locators.ADD_OVERTIME_WORK_BUTTON).click()
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_PICKER).click()
        self.elements_are_visible(self.locators.ALL_DATA_IN_DATA_PICKER)[1].click()
        self.action_move_to_element(self.element_is_present(self.locators.OVERTIME_WORK_SAVE_BUTTON_DISABLE))
        return self.element_is_visible(self.locators.TOOLTIP).text

    @testit.step("Берем текст всех сообщений системы")
    @allure.step("Берем текст всех сообщений системы")
    def get_alert_message(self):
        all_alerts = self.elements_are_visible(self.locators.ALERT_TEXT)
        data = []
        for alert in all_alerts:
            data.append(alert.text)
        return data

    @testit.step("Берем значение из клетки в таблице трудозатрат")
    @allure.step("Берем значение из клетки в таблице трудозатрат")
    def get_project_day_cell_contents(self, project_name, number_day):
        time.sleep(1)
        return self.element_is_visible(self.locators.get_day_by_project(project_name, number_day)).get_attribute(
            'placeholder')

    @testit.step("Берем значение из столбца Итого проекта")
    @allure.step("Берем значение из столбца Итого проекта")
    def get_project_total(self, project_name):
        return self.element_is_visible(self.locators.total_by_project(project_name)).text

    @testit.step("Берем значение из строки Итого проекта")
    @allure.step("Берем значение из строки Итого проекта")
    def get_day_total_raw(self, number_day):
        return self.elements_are_visible(self.locators.ALL_IN_TOTAL)[number_day].text

    @testit.step("Сохраняем трудозатраты")
    @allure.step("Сохраняем трудозатраты")
    def save_labor_reason(self):
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

    @testit.step("Проверяем что переработка появилась в таблице Причины")
    @allure.step("Проверяем что переработка появилась в таблице Причины")
    def check_project_reason_tab(self, project_name):
        assert self.element_is_displayed(self.locators.check_projeck_on_reason_tab(project_name))

    @testit.step("Открываем дровер добавления переработки")
    @allure.step("Открываем дровер добавления переработки")
    def open_overtime_drover(self):
        self.action_move_to_element(self.element_is_visible(self.locators.ADD_OVERTIME_WORK_BUTTON))
        self.element_is_visible(self.locators.ADD_OVERTIME_WORK_BUTTON).click()

    @testit.step("Проверяем наличие полей на дровере переработки")
    @allure.step("Проверяем наличие полей на дровере переработки")
    def check_fields_on_overtime_drover(self):
        assert self.element_is_displayed(self.locators.BEGIN_LEAVE_DATA_INPUT), "Отсутствует поле даты переработки"
        assert self.element_is_displayed(
            self.locators.PROJECT_NAME_DRAWER_INPUT), "Отсутствует поле проекта переработки"
        assert self.element_is_displayed(self.locators.CHECK_TASK_FIELD), "Отсутствует поле задачи переработки"
        assert self.element_is_displayed(self.locators.OVERTIME_WORK_INPUT), "Отсутствует поле времени переработки"
        assert self.element_is_displayed(
            self.locators.DRAWER_ABORT_BUTTON), "Отсутствует кнопка отмены дровера переработки"
        assert self.element_is_displayed(
            self.locators.OVERTIME_REASON_INPUT), "Отсутствует поле описания причины переработки"
        self.action_move_to_element(self.element_is_visible(self.locators.OVERTIME_WORK_SAVE_BUTTON_DISABLE))
        assert self.element_is_displayed(
            self.locators.OVERTIME_WORK_SAVE_BUTTON_DISABLE), "Отсутствует кнопка сохранения дровера переработки"

    @testit.step("Удаляем все отсутствия на странице заявлений")
    @allure.step("Удаляем все отсутствия на странице заявлений")
    def delete_all_absence(self):
        count = 0
        for i in range(20):
            try:
                self.action_move_to_element(self.element_is_visible(self.locators.REASON_TAB_TITLE))
                self.elements_are_visible(self.locators.ALL_ABSENCE_KEBABS)[0].click()
                time.sleep(0.1)  # Без ожидания иногда не корректно выбираются пункты кебаба меню
                self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
                time.sleep(0.1)  # Без ожидания иногда не корректно выбираются пункты кебаба меню
                self.element_is_visible(self.locators.DEL_ACCEPT_BUTTON).click()
                count += 1
                time.sleep(1)  # Без ожидания иногда не корректно выбираются пункты кебаб меню
            except StaleElementReferenceException:
                break
            except ElementClickInterceptedException:
                break
            except TimeoutException:
                break
        return count

    @testit.step("Ставим чекбокс предыдущих отсутствий")
    @allure.step("Ставим чекбокс предыдущих отсутствий")
    def click_previous_checkbox(self):
        if self.element_is_displayed(self.locators.CHECKED_PREVIOUS_ABSENCE_CHECKBOX):
            pass
        else:
            self.element_is_visible(self.locators.PREVIOUS_ABSENCE_CHECKBOX).click()

    @testit.step("Открываем кебаб меню для редактирования")
    @allure.step("Открываем кебаб меню для редактирования")
    def open_kebab_redact(self):
        self.action_move_to_element(self.element_is_visible(self.locators.REASON_TAB_TITLE))
        self.elements_are_visible(self.locators.ALL_ABSENCE_KEBABS)[0].click()
        self.element_is_visible(self.locators.KEBABS_REDACT_MENU_ITEM).click()

    @testit.step("Изменяем дату в отсутствии")
    @allure.step("Изменяем дату в отсутствии")
    def change_date_absense(self, day_number):
        time.sleep(0.5)  # Ожидание нужно для прогрузки анимации
        input_day = self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[0].get_attribute('value')
        if day_number >= 9:
            insert_day = str(day_number + 1)
        elif day_number <= 8:
            insert_day = '0' + str(day_number + 1)
        output_day = insert_day + input_day[2:10]
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[0].click()
        self.action_triple_click(self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[0])
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[0].send_keys(output_day)
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[1].click()
        self.action_triple_click(self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[1])
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[1].send_keys(output_day)
        self.elements_are_visible(self.locators.FIRST_AND_LAST_ABSENCE_DAY)[1].send_keys(Keys.RETURN)
        return output_day

    @testit.step("Берем дату начала и окончания отсутствия из таблицы")
    @allure.step("Берем дату начала и окончания отсутствия из таблицы")
    def check_data_absense(self):
        start_date = self.elements_are_visible(self.locators.ABSENCE_START_DATE_ON_TAB)[0].text
        end_date = self.elements_are_visible(self.locators.ABSENCE_END_DATE_ON_TAB)[0].text
        return start_date, end_date

    @testit.step("Проверяем удаление заявления")
    @allure.step("Проверяем удаление заявления")
    def check_delete_absense(self):
        self.elements_are_visible(self.locators.ALL_ABSENCE_KEBABS)[0].click()
        self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
        description_text = self.element_is_visible(self.locators.DRAWER_DESCRIPTION_TEXT).text
        self.element_is_visible(self.locators.DEL_ACCEPT_BUTTON).click()
        return description_text

    @testit.step("Проверяем отмену удаления заявления")
    @allure.step("Проверяем отмену удаления заявления")
    def cansel_delete_absense(self):
        self.elements_are_visible(self.locators.ALL_ABSENCE_KEBABS)[0].click()
        self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
        self.element_is_visible(self.locators.DEL_CANSEL_BUTTON).click()

    @testit.step("Берем количество заявлений")
    @allure.step("Берем количество заявлений")
    def get_count_absense(self):
        try:
            return len(self.elements_are_visible(self.locators.ALL_ABSENCE_KEBABS))
        except TimeoutException:
            return 0

    @testit.step("Проверяем добавление переработки на завершенный проект")
    @allure.step("Проверяем добавление переработки на завершенный проект")
    def check_adding_overtime_work_to_a_completed_project(self):
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_INPUT).send_keys(self.get_day_before(2))
        self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.chose_project_on_overtime_work_drawer(CreateProject().name)).click()
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys('1')
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(Keys.RETURN)
        try:
            self.add_file('отсутствие.docx', 'Отсутствие')
            self.element_is_present(self.locators.FILE_INPUT, 2).send_keys(os.path.abspath(r'../отсутствие.docx'))
        except TimeoutException:
            pass
        self.action_triple_click(self.element_is_visible(self.locators.OVERTIME_WORK_DATA_INPUT))
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_INPUT).send_keys(self.get_day_before(0))
        attribute = self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT_FIELD).get_attribute("value")
        self.delete_file('отсутствие.docx')
        assert attribute == '', 'Поле проект не очистилось'
        assert not self.element_is_clickable(self.locators.OVERTIME_WORK_SAVE_BUTTON,
                                             1), 'Кнопка применить не задизейблена'

    @testit.step("Добавление файла")
    @allure.step("Добавление файла")
    def add_file(self, name, text):
        file = open(os.path.abspath(rf'../{name}'), 'w+')
        file.write(f'{text}')
        file.close()

    @testit.step("Удаление файла")
    @allure.step("Удаление файла")
    def delete_file(self, name):
        os.remove(rf'../{name}')

    @testit.step("Нажатие кнопки добавления себя на проект")
    @allure.step("Нажатие кнопки добавления себя на проект")
    def press_add_to_project_button(self):
        self.element_is_visible(self.locators.ADD_TO_PROJECT_BUTTON).click()

    @testit.step("Заполнение полей дровера добавления себя на проект")
    @allure.step("Заполнение полей дровера добавления себя на проект")
    def field_adding_himself_to_a_project(self, project_name):
        self.element_is_visible(self.locators.ADD_TO_PROJECT_PROJECT_FIELD).send_keys(project_name)
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()
        self.element_is_visible(self.locators.ADD_TO_PROJECT_ROLE_FIELD).click()
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()

    @testit.step("Нажатие кнопки отмены в дровере добавления себя на проект")
    @allure.step("Нажатие кнопки отмены в дровере добавления себя на проект")
    def press_cancel_button_adding_himself_to_a_project(self):
        self.element_is_visible(self.locators.ADD_TO_PROJECT_CANCEL).click()

    @testit.step("Получение отображения проекта в таблице трудозатрат")
    @allure.step("Получение отображения проекта в таблице трудозатрат")
    def get_project_on_tab(self, project_name):
        return self.element_is_displayed(self.locators.check_projeck_on_reason_tab(project_name), 2)

    @testit.step("Проверка кликабельности кнопки сохранить")
    @allure.step("Проверка кликабельности кнопки сохранить")
    def check_clickable_save_button_in_adding_himself_to_a_project_drawer(self, project_name):
        assert not self.element_is_clickable(self.locators.ADD_TO_PROJECT_SAVE, 1), \
            "Кнопка сохранить кликабельна до заполнения обязательных полей"
        self.element_is_visible(self.locators.ADD_TO_PROJECT_PROJECT_FIELD).send_keys(project_name)
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()
        assert not self.element_is_clickable(self.locators.ADD_TO_PROJECT_SAVE, 1), \
            "Кнопка сохранить кликабельна после заполнения имени проекта"
        self.element_is_visible(self.locators.ADD_TO_PROJECT_ROLE_FIELD).click()
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        assert self.element_is_clickable(self.locators.ADD_TO_PROJECT_SAVE, 1), \
            "Кнопка сохранить не кликабельна после заполнения обязательных полей"

    @testit.step("Получение имен проектов доступных в дровере самостоятельного добавления на проект")
    @allure.step("Получение имен проектов доступных в дровере самостоятельного добавления на проект")
    def get_project_name_in_adding_himself_to_a_project_drawer(self):
        self.element_is_visible(self.locators.ADD_TO_PROJECT_PROJECT_FIELD).click()
        return self.get_li_menu_items()

    @testit.step("Получение списка элементов дротдауна")
    @allure.step("Получение списка элементов дротдауна")
    def get_li_menu_items(self):
        all_items = self.elements_are_visible(self.locators.LI_MENU_ITEM)
        text = []
        for item in all_items:
            text.append(item.get_attribute('aria-label'))
        return text

    @testit.step("Получение списка проектов отображенных на странице трудозатрат")
    @allure.step("Получение списка проектов отображенных на странице трудозатрат")
    def get_all_project_name_on_tab(self):
        all_items = self.elements_are_visible(self.locators.ALL_PROJECT_NAMES)
        text = []
        for item in all_items:
            text.append(item.get_attribute('aria-label'))
        return text

    @testit.step("Удаление из списка проектов на которые назначен пользователь")
    @allure.step("Удаление из списка проектов на которые назначен пользователь")
    def remove_project_on_tab(self, project_on_tad, adding_himself):
        for project in project_on_tad:
            if project in adding_himself:
                adding_himself.remove(project)

    @testit.step("Нажатие кнопки сохранения в дровере добавления себя на проект")
    @allure.step("Нажатие кнопки сохранения в дровере добавления себя на проект")
    def press_save_button_adding_himself_to_a_project(self):
        self.element_is_visible(self.locators.ADD_TO_PROJECT_SAVE).click()

    @testit.step("Заполняем поле причина переработки")
    @allure.step("Заполняем поле причина переработки")
    def field_reason_overwork(self, reason):
        self.element_is_visible(self.locators.CHECK_LABOR_REASON_FIELD).send_keys(reason)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

    @testit.step("Нажать Применить в дровере добавления переработки")
    @allure.step("Нажать Применить в дровере добавления переработки")
    def submit_labor_reason(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка что данные сохранились в дровере")
    @allure.step("Проверка что данные сохранились в дровере")
    def check_data_from_drover(self, overtime, reason):
        assert self.element_is_displayed(self.locators.check_value(overtime)), 'Переработка не сохранилась'
        assert self.element_is_displayed(self.locators.check_text(reason)), 'Причина не сохранилась'

    @testit.step("Открыть дровер добавления переработки за конкретный день")
    @allure.step("Открыть дровер добавления переработки за конкретный день")
    def open_overwork_drover_for_specific_day(self, number_day_element, project_mame):
        self.element_is_visible(self.locators.ADD_OVERTIME_WORK_BUTTON).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_PICKER).click()
        self.elements_are_visible(self.locators.ALL_DATA_IN_DATA_PICKER)[number_day_element].click()
        self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.chose_project_on_overtime_work_drawer(project_mame)).click()

    @testit.step("Редактирование переработки")
    @allure.step("Редактирование переработки")
    def editing_overwork(self, number, reason):
        self.action_triple_click(self.element_is_visible(self.locators.CHECK_LABOR_REASON_FIELD))
        self.element_is_visible(self.locators.CHECK_LABOR_REASON_FIELD).send_keys(reason)
        time.sleep(1)
        self.action_triple_click(self.element_is_visible(self.locators.OVERTIME_WORK_INPUT))
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(number)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

    @testit.step("Добавить переработку без файла")
    @allure.step("Добавить переработку без файла")
    def add_overtime_work_without_file(self, number_day_element, overtime_work_hours, project_mame):
        self.element_is_visible(self.locators.ADD_OVERTIME_WORK_BUTTON).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_PICKER).click()
        self.elements_are_visible(self.locators.ALL_DATA_IN_DATA_PICKER)[number_day_element].click()
        self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.chose_project_on_overtime_work_drawer(project_mame)).click()
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(overtime_work_hours)
        time.sleep(1)

    @testit.step("Получение списка дат начиная с сегодняшней")
    @allure.step("Получение списка дат начиная с сегодняшней")
    def get_date_list_from_today(self):
        today = int(self.element_is_visible(self.locators.TODAY).text)
        data_list = []
        for i in range(today):
            data_list.append(i)
        in_total_list = self.elements_are_visible(self.locators.ALL_IN_TOTAL)
        data = []
        for i in in_total_list:
            data.append(i.text)
        data.remove('Итого')
        return list(set([i for i, data in enumerate(data)]) - set(data_list))

    @testit.step("Проверка отображения архивного проекта")
    @allure.step("Проверка отображения архивного проекта")
    def check_archive_project(self, project_name):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()
        self.element_is_visible(self.locators.NOT_ACTIV_PROJECT_CHECKBOX).click()
        self.action_esc()
        time.sleep(1)
        self.action_move_to_element(self.element_is_visible(self.locators.check_name_project_color(project_name)))
        name_color = self.element_is_visible(self.locators.check_name_project_color(project_name)).value_of_css_property('color')
        assert name_color == 'rgba(0, 0, 0, 0.26)', "Цвет проекта не серый"

    @testit.step("Добавление трудозатрат")
    @allure.step("Добавление трудозатрат")
    def check_add_hour_to_project(self):
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, 5)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(1)

    @testit.step("Получение заголовка таблицы")
    @allure.step("Получение заголовка таблицы")
    def get_tab_header(self):
        all_day_list = self.elements_are_present(self.locators.TAB_HEADER_TEXT)
        numbers = []
        for day in all_day_list:
            numbers.append(day.text)
        return numbers

    @testit.step("Получение заголовка таблицы с днями недели")
    @allure.step("Получение заголовка таблицы с днями недели")
    def get_tab_header_week_days(self):
        all_day_list = self.elements_are_present(self.locators.TAB_HEADER_WEEK_TEXT)
        numbers = []
        for day in all_day_list:
            numbers.append(day.text)
        return numbers

    @testit.step("Получение начала и конца текущей недели")
    @allure.step("Получение начала и конца текущей недели")
    def week_day(self):
        date = datetime.date.today()
        monday = self.get_day_before(date.weekday())
        sunday = self.get_day_before(-6 + date.weekday())
        return f'({monday} – {sunday})'

    @testit.step("Получение названия месяца или номера недели")
    @allure.step("Получение названия месяца или номера недели")
    def get_month_or_week_on_tab(self):
        return self.element_is_visible(self.locators.MONTH_DATEPICKER_TEXT).text

    @testit.step("Получение начала и конца текущей недели с таблицы трудозатрат")
    @allure.step("Получение начала и конца текущей недели с таблицы трудозатрат")
    def get_week_dates(self):
        return self.element_is_visible(self.locators.WEEK_DATEPICKER_TEXT).text

    @testit.step("Проверка перехода по периодам при отображении по неделе")
    @allure.step("Проверка перехода по периодам при отображении по неделе")
    def check_change_period_by_week(self):
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        assert self.get_month_or_week_on_tab() == str(datetime.date.today().isocalendar().week + 1) + ' неделя', \
            "В таблице не отображаются даты следующей недели"
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        assert self.get_month_or_week_on_tab() == str(datetime.date.today().isocalendar().week) + ' неделя', \
            "В таблице не отображаются даты текущей недели"
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        assert self.get_month_or_week_on_tab() == str(datetime.date.today().isocalendar().week - 1) + ' неделя', \
            "В таблице не отображаются даты предыдущей недели"

    @testit.step("Добавить переработку с файлом")
    @allure.step("Добавить переработку с файлом")
    def add_overtime_work_with_file(self, number_day_element, overtime_work_hours, project_mame):
        self.element_is_visible(self.locators.ADD_OVERTIME_WORK_BUTTON).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_PICKER).click()
        self.elements_are_visible(self.locators.ALL_DATA_IN_DATA_PICKER)[number_day_element].click()
        self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.chose_project_on_overtime_work_drawer(project_mame)).click()
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(overtime_work_hours)
        self.add_file('переработка.docx', 'Переработка')
        self.element_is_present(self.locators.FILE_INPUT, 2).send_keys(os.path.abspath(r'../переработка.docx'))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.delete_file('переработка.docx')

    @testit.step("Проверка что данные с файлом сохранились в дровере")
    @allure.step("Проверка что данные с файлом сохранились в дровере")
    def check_data_with_file_from_drover(self, overtime, file_name):
        assert self.element_is_displayed(self.locators.check_value(overtime)), 'Переработка не сохранилась'
        assert self.element_is_displayed(self.locators.check_text(file_name)), 'Файл не сохранился'

    @testit.step("Редактирование переработки с файлом")
    @allure.step("Редактирование переработки с файлом")
    def editing_overwork_with_file(self, number):
        self.action_triple_click(self.element_is_visible(self.locators.OVERTIME_WORK_INPUT))
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(number)
        time.sleep(1)
        self.element_is_visible(self.locators.DELETE_ICON).click()
        self.element_is_visible(self.locators.SUBMIT_DELETE_BUTTON).click()
        time.sleep(1)
        self.add_file('переработка2.docx', 'Переработка2')
        self.element_is_present(self.locators.FILE_INPUT, 2).send_keys(os.path.abspath(r'../переработка2.docx'))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.delete_file('переработка2.docx')

    @testit.step("Отмена перехода на другую страницу со страницы трудозатрат")
    @allure.step("Отмена перехода на другую страницу со страницы трудозатрат")
    def cancel_moving_to_another_page(self):
        self.element_is_visible(self.locators.UNSAVED_WINDOW_ABORT_BUTTON).click()

    @testit.step("Проверка перехода по периодам при отображении по месяцу")
    @allure.step("Проверка перехода по периодам при отображении по месяцу")
    def check_change_period_by_month(self):
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        assert self.get_month_or_week_on_tab() == str(
            (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%B %Y')), \
            "В таблице не отображаются даты следующего месяца"
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        assert self.get_month_or_week_on_tab() == str(
            (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%B %Y')), \
            "В таблице не отображаются даты текущего месяца"
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        assert self.get_month_or_week_on_tab() == str(
            (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%B %Y')), \
            "В таблице не отображаются даты предыдущего месяца"

    @testit.step("Добавление файла более 5 мб")
    @allure.step("Добавление файла более 5 мб")
    def add_file_5_mb(self, name):
        file = open(os.path.abspath(rf'../{name}'), 'w+')
        file.write('ппппппппппппппппппппппппп'*215000)
        file.close()

    @testit.step("Добавление переработки с файлом более 5 мб")
    @allure.step("Добавление переработки с файлом более 5 мб")
    def add_overwork_with_file_5mb(self, number_day_element, overtime_work_hours, project_mame):
        self.element_is_visible(self.locators.ADD_OVERTIME_WORK_BUTTON).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_PICKER).click()
        self.elements_are_visible(self.locators.ALL_DATA_IN_DATA_PICKER)[number_day_element].click()
        self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.chose_project_on_overtime_work_drawer(project_mame)).click()
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(overtime_work_hours)
        self.add_file_5_mb('переработка 5мб.docx')
        self.element_is_present(self.locators.FILE_INPUT, 2).send_keys(os.path.abspath(r'../переработка 5мб.docx'))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        assert self.element_is_displayed(self.locators.check_text('Суммарный размер файлов не должен превышать 5МБ')), 'Сообщения с предупреждением нет'
        self.delete_file('переработка 5мб.docx')

    @testit.step("Проверка наличия текста на странице")
    @allure.step("Проверка наличия текста на странице")
    def check_text_on_page(self, text):
        return self.element_is_displayed(self.locators.check_text(text), 2)

    @testit.step("Проверка редактирования отсутствий с пересечением с другими отсутствиями")
    @allure.step("Проверка редактирования отсутствий с пересечением с другими отсутствиями")
    def check_editing_absences_if_the_selected_period_overlaps_with_other_absences(self, number_day_element):
        self.elements_are_visible(self.locators.ALL_ABSENCE_KEBABS)[0].click()
        self.element_is_visible(self.locators.KEBABS_REDACT_MENU_ITEM).click()
        self.element_is_visible(self.locators.BEGIN_LEAVE_DATA_PICKER_BUTTON).click()
        self.elements_are_visible(self.locators.ALL_DATA_IN_DATA_PICKER)[number_day_element].click()
        self.element_is_visible(self.locators.REDACT_DRAWER_SAVE_BUTTON).click()
        assert self.element_is_displayed(self.locators.check_text('Наложение отсутствий, выберите другие даты')), \
            "Нет сообщения о наложении дат"
        self.element_is_visible(self.locators.DRAWER_ABORT_BUTTON).click()

    @testit.step("Получение причины и статуса переработки проекта")
    @allure.step("Получение причины и статуса переработки проекта")
    def check_overtime_on_reason_tab(self, project_name):
        self.action_move_to_element(self.element_is_visible(self.locators.OVERTIME_WORK_PROJECTS_SEARCH_FIELD))
        self.element_is_visible(self.locators.OVERTIME_WORK_PROJECTS_SEARCH_FIELD).send_keys(project_name)
        reason_text = self.element_is_visible(self.locators.ALL_OVERTIME_WORK_REASONS).text
        status_text = self.element_is_visible(self.locators.ALL_OVERTIME_WORK_STATUSES).text
        return reason_text, status_text

    @testit.step("Проверка тултипа загрузки файла при добавлении переработки")
    @allure.step("Проверка тултипа загрузки файла при добавлении переработки")
    def check_tooltip_overtime_work_file_field(self, number_day_element, overtime_work_hours, project_mame):
        self.element_is_visible(self.locators.ADD_OVERTIME_WORK_BUTTON).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_PICKER).click()
        self.elements_are_visible(self.locators.ALL_DATA_IN_DATA_PICKER)[number_day_element].click()
        self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.chose_project_on_overtime_work_drawer(project_mame)).click()
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(overtime_work_hours)
        assert 'Приложите документ о подтверждении ' in self.element_is_visible(self.locators.TOOLTIP).text, \
            "Не появился тултип с описанием файла"

    @testit.step("Переход в дровер редактирования переработки")
    @allure.step("Переход в дровер редактирования переработки")
    def redact_overtime_on_reason_tab(self, project_name):
        self.element_is_not_visible(self.locators.ALERT_TEXT, 10)
        self.action_move_to_element(self.element_is_visible(self.locators.OVERTIME_WORK_PROJECTS_SEARCH_FIELD))
        self.element_is_visible(self.locators.OVERTIME_WORK_PROJECTS_SEARCH_FIELD).send_keys(project_name)
        time.sleep(0.5)
        self.element_is_visible(self.locators.ALL_OVERTIME_WORK_KEBABS).click()
        self.element_is_visible(self.locators.KEBABS_REDACT_MENU_ITEM).click()

    @testit.step("Отмена редактирования переработки")
    @allure.step("Отмена редактирования переработки")
    def cancel_redact_overtime(self, overtime_work_hours):
        self.action_triple_click(self.element_is_visible(self.locators.OVERTIME_WORK_INPUT))
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(overtime_work_hours)
        self.element_is_visible(self.locators.DRAWER_ABORT_BUTTON).click()

    @testit.step("Изменение даты переработки")
    @allure.step("Изменение даты переработки")
    def change_overtime_work_date(self, project_name, new_date):
        self.redact_overtime_on_reason_tab(project_name)
        self.action_triple_click(self.element_is_visible(self.locators.OVERTIME_WORK_DATA_INPUT))
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_INPUT).send_keys(new_date)
        time.sleep(1)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        self.element_is_not_visible(self.locators.ALERT_TEXT, 10)

    @testit.step("Редактирование переработки с файлом через дровер")
    @allure.step("Редактирование переработки с файлом через дровер")
    def editing_overwork_with_file_from_tab(self, number):
        self.action_triple_click(self.element_is_visible(self.locators.OVERTIME_WORK_INPUT))
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(number)
        time.sleep(1)
        self.element_is_visible(self.locators.DELETE_ICON).click()
        self.element_is_visible(self.locators.SUBMIT_DELETE_BUTTON).click()
        time.sleep(1)
        self.add_file('переработка2.docx', 'Переработка2')
        self.element_is_present(self.locators.FILE_INPUT).send_keys(os.path.abspath(r'../переработка2.docx'))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(0.5)
        self.delete_file('переработка2.docx')

    @testit.step("Получение значений полей из дровера редактирования переработки")
    @allure.step("Получение значений полей из дровера редактирования переработки")
    def get_overtime_value_on_drawer(self):
        date = self.element_is_visible(self.locators.OVERTIME_WORK_DATA_INPUT).get_attribute('value')
        hours = self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).get_attribute('value')
        project = self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT_FIELD).get_attribute('value')
        file_name = self.elements_are_visible(self.locators.ADD_FILES_TEXT)[0].text
        return date, hours, project, file_name

    @testit.step("Проверка очистки обязательного поля при редактирования")
    @allure.step("Проверка очистки обязательного поля при редактирования")
    def check_clear_required_field(self):
        fields_locators = [self.locators.OVERTIME_WORK_DATA_INPUT, self.locators.OVERTIME_WORK_INPUT, self.locators.PROJECT_NAME_DRAWER_INPUT_FIELD]
        random_field = fields_locators[random.randint(0, 2)]
        self.action_triple_click(self.element_is_visible(random_field))
        self.element_is_visible(random_field).send_keys(Keys.BACKSPACE)
        self.element_is_visible(self.locators.check_text('Редактирование переработки')).click()
        assert self.element_is_visible(self.locators.MUI_ERROR).text == 'Поле обязательно',\
            "Не появилось сообщение об обязательности поля"
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 2), "Кнопка сохранить кликабельна"
        self.element_is_visible(self.locators.CLEAR_ICON).click()

    @testit.step("Изменение даты в датапикере")
    @allure.step("Изменение даты в датапикере")
    def change_date_in_date_piker(self, number_day_element):
        self.element_is_visible(self.locators.OVERTIME_WORK_DATA_PICKER).click()
        self.elements_are_visible(self.locators.ALL_DATA_IN_DATA_PICKER)[number_day_element].click()

    @testit.step("Проверка изменения файла на превышающий 5 мб")
    @allure.step("Проверка изменения файла на превышающий 5 мб")
    def check_change_file_to_not_valid(self):
        self.element_is_visible(self.locators.DELETE_ICON).click()
        self.element_is_visible(self.locators.SUBMIT_DELETE_BUTTON).click()
        time.sleep(1)
        self.add_file_5_mb('переработка 5мб.docx')
        self.element_is_present(self.locators.FILE_INPUT, 2).send_keys(os.path.abspath(r'../переработка 5мб.docx'))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        assert self.element_is_displayed(self.locators.check_text(
            'Суммарный размер файлов не должен превышать 5МБ')), 'Нет сообщения о превышении размера файла'
        self.delete_file('переработка 5мб.docx')
        self.element_is_visible(self.locators.CLEAR_ICON).click()

    @testit.step("Проверка изменения файла на превышающий 5 мб")
    @allure.step("Проверка изменения файла на превышающий 5 мб")
    def change_time_in_overtime_drawer(self, new_time):
        self.action_triple_click(self.element_is_visible(self.locators.OVERTIME_WORK_INPUT))
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(new_time)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Удаление переработки")
    @allure.step("Удаление переработки")
    def delete_overtime_on_reason_tab(self, project_name):
        self.element_is_not_visible(self.locators.ALERT_TEXT, 10)
        self.action_move_to_element(self.element_is_visible(self.locators.OVERTIME_WORK_PROJECTS_SEARCH_FIELD))
        self.element_is_visible(self.locators.OVERTIME_WORK_PROJECTS_SEARCH_FIELD).send_keys(project_name)
        time.sleep(0.5)
        self.element_is_visible(self.locators.ALL_OVERTIME_WORK_KEBABS).click()
        self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
        self.element_is_visible(self.locators.DEL_ACCEPT_BUTTON).click()

    @testit.step("Проверка отмены удаления переработки")
    @allure.step("Проверка отмены удаления переработки")
    def check_break_delete_overtime_on_reason_tab(self, project_name):
        self.element_is_not_visible(self.locators.ALERT_TEXT, 10)
        self.action_move_to_element(self.element_is_visible(self.locators.OVERTIME_WORK_PROJECTS_SEARCH_FIELD))
        self.element_is_visible(self.locators.OVERTIME_WORK_PROJECTS_SEARCH_FIELD).send_keys(project_name)
        time.sleep(0.5)
        self.element_is_visible(self.locators.ALL_OVERTIME_WORK_KEBABS).click()
        self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
        assert self.element_is_visible(
            self.locators.DRAWER_DESCRIPTION_TEXT).text == 'Вы уверены, что хотите удалить переработку?', \
            "Текст в модальном окне не корректен или отсутствует"
        self.element_is_visible(self.locators.DEL_CANSEL_BUTTON).click()

    @testit.step("Проверка отсутствия переработок на проекте")
    @allure.step("Проверка отсутствия переработок на проекте")
    def not_have_overtime_on_reason_tab_by_project(self, project_name):
        self.element_is_not_visible(self.locators.ALERT_TEXT, 10)
        self.action_move_to_element(self.element_is_visible(self.locators.OVERTIME_WORK_PROJECTS_SEARCH_FIELD))
        self.element_is_visible(self.locators.OVERTIME_WORK_PROJECTS_SEARCH_FIELD).send_keys(project_name)
        assert not self.element_is_displayed(self.locators.ALL_OVERTIME_WORK_KEBABS, 2), \
            "На проекте есть переработки"

    @allure_testit_step('Выбор чекбокса "Отображать причины отклонения"')
    def click_rejection_reasons_checkbox(self):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()
        self.element_is_visible(self.locators.REJECTED_REASON_CHECKBOX).click()
        self.action_esc()

    @allure_testit_step('Выбор чекбокса "Отображать неактивные проекты"')
    def click_not_active_project_checkbox(self):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()
        self.element_is_visible(self.locators.NOT_ACTIV_PROJECT_CHECKBOX).click()
        self.action_esc()

    @allure_testit_step('Получение текста тултипа дня проекта')
    def get_day_tooltip_text_in_project(self, project_name, number_day):
        self.action_move_to_element(self.element_is_visible(self.locators.get_day_by_project(project_name, number_day)))
        tooltip_text = self.element_is_visible(self.locators.TOOLTIP).text
        return tooltip_text

    @allure_testit_step('Проверка отображения тултипа')
    def tooltip_is_displayed(self, project_name, number_day):
        self.action_move_to_element(self.element_is_visible(self.locators.get_day_by_project(project_name, number_day)))
        return self.element_is_displayed(self.locators.TOOLTIP)

    @allure_testit_step('Проверка отклонения трудозатрат')
    def field_is_rejected(self, task_name, number_day):
        return 'rejected' in self.element_is_visible(self.locators.get_day_by_project(task_name, number_day)).find_element(By.XPATH, "..").get_attribute("class")

    @allure_testit_step('Получение информации о возможности ввода в ячейку задачи')
    def get_status_of_field_task(self, task_name, number_day):
        return self.element_is_visible(self.locators.get_day_by_task(task_name, number_day)).get_attribute('disabled')

    @allure_testit_step('Получение информации о возможности ввода в ячейку проекта')
    def get_status_of_field_project(self, project_name, number_day):
        return self.element_is_visible(self.locators.get_day_by_project(project_name, number_day)).get_attribute('disabled')

    @allure_testit_step('Получение текста уведомления')
    def get_notification_text(self, notification_id = 0):
        self.element_is_visible(self.locators.NOTIFICATIONS_ICON).click()
        self.elements_are_visible(self.locators.NOTIFICATIONS_SUMMARY_BUTTON,30)[notification_id].click()
        return self.element_is_visible(self.locators.NOTIFICATIONS_SUMMARY).text

    @allure_testit_step("Открыть список задачи")
    def open_tasks_list(self):
        self.elements_are_visible(self.locators.OPEN_TASKS_LIST_BUTTON)[0].click()

    @allure_testit_step("Получить цвет ячейки")
    def get_cell_color(self, project_name, number_day):
        return (self.element_is_visible(self.locators.check_day_color_by_project(project_name, number_day)).
                value_of_css_property('background-color'))

    @allure_testit_step("Отмена редактирования таблицы трудозатрат")
    def cancel_editing_labor_cost(self):
        self.element_is_visible(self.locators.DISABLE_BUTTON).click()
