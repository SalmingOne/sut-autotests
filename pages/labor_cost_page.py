import os
import time

import allure
from selenium.common import TimeoutException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from data.data import PROJECT_NAME
from locators.labor_cost_page_locators import LaborCostPageLocators
from pages.base_page import BasePage


class LaborCostPage(BasePage):
    locators = LaborCostPageLocators()

    @allure.step("Переход на таблицу трудозатрат через меню")
    def go_to_labor_cost_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_ACTIVITY))
        self.element_is_visible(self.locators.TAB_LABOR_COST_TABLE).click()

    @allure.step("Проверка, что код проекта есть на странице")
    def check_project_code_at_labor(self):
        check_code_at_labor = self.element_is_present(self.locators.CHECK_CODE_PROJECT).text
        return check_code_at_labor

    @allure.step("Проверка что кода проекта нет на странице")
    def check_no_project_code_at_labor(self):
        try:
            return self.element_is_present(self.locators.CHECK_CODE_PROJECT).text
        except TimeoutException:
            return "no element on page"

    @allure.step("Проверка что появляется окно указания причины списания ")
    def check_to_have_reason_fo_write(self):
        self.element_is_visible(self.locators.RANDOM_DAYS_BY_PROJECT).click()
        checked_text = self.element_is_visible(self.locators.CHECK_LABOR_REASON_FIELD).text
        self.element_is_visible(self.locators.BREAK_LABOR_REASON_WINDOW).click()
        assert checked_text == "Причина *", "Не открылось окно указания причины"

    @allure.step("Ввод значения в клетку таблицы трудозатрат")
    def input_time(self, element, in_time):
        self.element_is_visible(element).click()
        self.element_is_visible(element).send_keys(in_time)
        self.element_is_visible(element).send_keys(Keys.RETURN)

    @allure.step("Ввод значения часов трудозатрат в модальном окне при обязательном указании причин трудозатрат")
    def input_hours_into_form(self, hours):
        self.element_is_visible(self.locators.INPUT_HOUR_FIELD).send_keys(hours)

    @allure.step("Ввод причины трудозатрат в модальном окне при обязательном указании причин трудозатрат")
    def input_reason_into_form(self, reason):
        self.element_is_visible(self.locators.INPUT_REASON_DESCRIPTION_FIELD).send_keys(reason)

    @allure.step("Узнаем сколько дней в конкретном месяце, что бы потом вставить значение в последний день")
    def get_number_last_month_day(self):
        all_day_list = self.elements_are_present(self.locators.ADD_OVERTIME_WORK_BUTTON)
        numbers = []
        for day in all_day_list:
            numbers.append(day.text)
        return len(numbers)

    @allure.step("Списываем трудозатраты за первый и последний день месяца")
    def input_work_by_month(self):
        first_day_time = 5  # Первый день текущего периода
        last_day_time = 8  # Первый день текущего периода
        previous_last_day_time = 6  # Первый день предыдущего периода
        next_first_day_time = 3  # Первый день следующего периода
        # Заполняем текущий месяц
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        last_day_number = self.get_number_last_month_day() + 1
        last_day_locator = (
            By.XPATH,
            f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[{last_day_number}]//input')
        self.input_time(last_day_locator, last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        # Переходим на предыдущий месяц и заполняем его
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        last_day_number = self.get_number_last_month_day() + 1
        last_day_locator = (
            By.XPATH,
            f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[{last_day_number}]//input')
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

    @allure.step("Выбираем отображаемый период")
    def choose_period(self, period):
        time.sleep(1)
        self.element_is_visible(self.locators.PERIOD_SELECT_BUTTON).click()
        if period == "month":
            self.element_is_visible(self.locators.MONTH_PERIOD_SELECT).click()
        elif period == "week":
            self.element_is_visible(self.locators.WEEK_PERIOD_SELECT).click()

    @allure.step("Выбираем месяц в датапикере")
    def choose_month_picker(self, month_name):  # имя месяца указывать точно как на экране(с точкой)
        self.element_is_visible(self.locators.MONTH_DATEPICKER).click()
        month = month_name
        month_locator = (By.XPATH, f'//button[text()="{month}"]')
        self.element_is_visible(month_locator).click()

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
        # Заполняем последний день предыдущего года
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        last_day_number = self.get_number_last_month_day() + 1
        last_day_locator = (
            By.XPATH,
            f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[{last_day_number}]//input')
        self.input_time(last_day_locator, previous_last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        # Заполняем последний день текущего года
        self.choose_month_picker('дек.')
        last_day_number = self.get_number_last_month_day() + 1
        last_day_locator = (
            By.XPATH,
            f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[{last_day_number}]//input')
        self.input_time(last_day_locator, last_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        # Заполняем первый день следующего года
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, next_first_day_time)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        return first_day_time + last_day_time

    @allure.step("Проверяем цвет поля при списании трудозатрат")
    def check_change_color_on_labor_cost_field(self):
        first_day_time = 4
        # Списываем затраты и берем цвета ячейки
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        color_before_save = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT_COLOR).value_of_css_property(
            'background-color')
        reason_in_field = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).get_attribute('placeholder')
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(1)  # Без этого ожидания не успевает прогрузиться белый цвет
        color_after_save = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT_COLOR).value_of_css_property(
            'background-color')
        reason_in_field_after_save = self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).get_attribute(
            'placeholder')
        # Удаляем списания по проекту
        self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).click()
        self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(1)  # Без этого ожидания не успевают сохраниться изменения и не удаляется проект
        assert color_before_save == 'rgba(255, 251, 233, 1)', "После списания трудозатрат цвет ячейки не жёлтый"
        assert color_after_save == 'rgba(0, 0, 0, 0)', "После сохранения списания цвет не белый"
        assert reason_in_field == str(first_day_time), "Количество часов списания не равно введенному значению"
        assert reason_in_field_after_save == str(first_day_time), "Списание не сохранено"

    @allure.step("Проверяем наличие заголовка Трудозатраты")
    def check_title(self):
        assert self.element_is_displayed(self.locators.TITLE_PAGE), "Заголовок страницы Трудозатраты отсутствует"

    @allure.step("Проверяем наличие выбора периода")
    def check_period_select(self):
        self.element_is_visible(self.locators.PERIOD_SELECT_BUTTON).click()
        menu_title_list = self.elements_are_visible(self.locators.PERIOD_MENU_ITEM)
        data = []
        for title in menu_title_list:
            data.append(title.text)
        self.action_esc()
        assert data == ['Месяц (по дням)', 'Неделя'], "Не все периоды отображены для выбора"

    @allure.step("Проверяем наличие кнопки добавления себя на проект")
    def check_add_to_project_button(self):
        assert self.element_is_displayed(self.locators.ADD_TO_PROJECT_BUTTON), "Нет кнопки добавления себя на проект"

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

    @allure.step("Проверяем наличие кнопки открытия виджетов")
    def check_open_widget_button(self):
        assert self.element_is_displayed(self.locators.OPEN_WIDGET_BUTTON), "Кнопки открытия виджетов нет на странице"

    @allure.step("Проверяем наличие кнопки выбора месяца")
    def check_month_picker(self):
        assert self.element_is_displayed(self.locators.MONTH_DATEPICKER), "Нет кнопки выбора месяца"

    @allure.step("Проверяем наличие кнопок следующего и предыдущего периода")
    def check_next_previous_buttons(self):
        assert self.element_is_displayed(self.locators.NEXT_PERIOD_BUTTON), "Нет кнопки следующего периода"
        assert self.element_is_displayed(self.locators.PREVIOUS_PERIOD_BUTTON), "Нет кнопки предыдущего периода"

    @allure.step("Проверяем наличие всех дней и Итого недели в шапке таблицы")
    def check_tab_head(self):
        all_day_list = self.elements_are_present(self.locators.ALL_DAY_NUMBER)
        numbers = []
        for day in all_day_list:
            numbers.append(day.text)
        assert 'Итого' in numbers, "Итого нет в заголовке"
        return numbers, len(numbers) - 5

    @allure.step("Проверяем наличие всех дней недели в шапке таблицы")
    def check_week_days_head(self):
        all_day_list = self.elements_are_present(self.locators.SEVEN_DAY_ON_HEAD)
        numbers = []
        for day in all_day_list:
            numbers.append(day.text)
        day_week = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
        for a in day_week:
            assert a in numbers, "Дня недели нет в заголовке"

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

    @allure.step("Проверяем наличие выбранных дней при наведении на ячейку таблицы")
    def check_have_selected_days(self):
        if self.element_is_displayed(self.locators.PROJECT_STRING):
            day_list = self.elements_are_visible(self.locators.ALL_DAY_COLORS)
            self.action_move_to_element(day_list[5])
            assert self.element_is_displayed(self.locators.SELECTED_DAYS), ("При наведении на ячейку таблицы на "
                                                                            "странице нет выбранных дней")
        else:
            pass

    @allure.step("Проверяем наличие тултипа при наведении на код проекта")
    def check_tooltip_on_project_code(self):
        if self.element_is_displayed(self.locators.PROJECT_STRING):
            project_list = self.elements_are_visible(self.locators.PROJECT_TITLE)
            self.action_move_to_element(project_list[0])
            assert self.element_is_displayed(self.locators.TOOLTIP), "При наведении на код проекта не появляется тултип"
            return self.element_is_visible(self.locators.TOOLTIP).text
        else:
            pass

    @allure.step("Проверяем наличие кнопок сохранения и отмены")
    def check_save_and_disable_buttons(self):
        assert self.element_is_displayed(self.locators.SAVE_BUTTON)
        assert self.element_is_displayed(self.locators.DISABLE_BUTTON)

    @allure.step("Переходим на отображение по имени проекта")
    def go_to_filter_by_project_name(self):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()
        self.element_is_visible(self.locators.FILTER_BY_PROJECT_NAME).click()
        self.action_esc()

    @allure.step("Открываем модальное окно указания причины списания")
    def open_reason_window(self, project_name=None):
        if project_name == None:
            self.element_is_visible(self.locators.RANDOM_DAYS_BY_PROJECT).click()
        else:
            self.element_is_visible(self.locators.get_random_day_by_project(project_name)).click()

    @allure.step("Нажать Сохранить в модальном окне указание часов и причины списания трудозатрат")
    def save_hours_and_reason(self):
        self.element_is_visible(self.locators.SAVE_LABOR_REASON_WINDOW_BUTTON).click()

    @allure.step("Проверяем наличие заголовка на модальном окне указания причины списания")
    def check_title_reason_window(self):
        assert self.element_is_displayed(self.locators.TITLE_MODAL_REASON_WINDOW)

    @allure.step("Проверяем наличие полей на модальном окне указания причины списания")
    def check_fields_reason_window(self):
        assert self.element_is_displayed(self.locators.INPUT_REASON_TIME_FIELD)
        assert self.element_is_displayed(self.locators.INPUT_REASON_DESCRIPTION_FIELD)

    @allure.step("Проверяем наличие кнопок на модальном окне указания причины списания")
    def check_buttons_reason_window(self):
        assert self.element_is_displayed(self.locators.SAVE_LABOR_REASON_WINDOW_BUTTON)
        assert self.element_is_displayed(self.locators.BREAK_LABOR_REASON_WINDOW)

    @allure.step("Закрываем модальное окно указания причины списания")
    def close_reason_window(self):
        self.element_is_visible(self.locators.BREAK_LABOR_REASON_WINDOW).click()

    @allure.step("Проверяем цвет поля при списании трудозатрат")
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

    @allure.step("Вводим в поле не сохраненные трудозатраты")
    def input_unsaved_values_on_labor_cost_field(self):
        first_day_time = 18
        self.input_time(self.locators.FIRST_DAY_BY_PROJECT, first_day_time)
        return str(first_day_time)

    @allure.step("Проверяем наличие элементов на окне уведомления о не сохраненных данных")
    def check_unsaved_data_window(self):
        assert self.element_is_displayed(self.locators.UNSAVED_WINDOW_TITLE)
        assert self.element_is_displayed(self.locators.UNSAVED_WINDOW_ACCEPT_BUTTON)
        assert self.element_is_displayed(self.locators.UNSAVED_WINDOW_ABORT_BUTTON)
        self.element_is_visible(self.locators.UNSAVED_WINDOW_ACCEPT_BUTTON).click()

    @allure.step("Берем текст в поле после возвращения на страницу трудозатрат")
    def get_values_on_labor_cost_field_to_check(self):
        return self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).text

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
            return [i for i, data in enumerate(data) if data == '0']

    @allure.step("Открываем дровер добавления отсутствия")
    def open_add_absence_drawer(self, number_day):
        all_head_days = self.elements_are_present(self.locators.ADD_OVERTIME_WORK_BUTTON_FIELD)
        self.action_move_to_element(all_head_days[number_day])
        all_overtime_buttons = self.elements_are_present(self.locators.ADD_OVERTIME_WORK_BUTTON)
        all_overtime_buttons[number_day].click()

    @allure.step("Добавляем отсутствие")
    def add_absence(self, number_empty_day, absence_tipe):
        days_zero_reason = self.get_numbers_days_reason("zero")
        self.open_add_absence_drawer(days_zero_reason[number_empty_day])
        if absence_tipe == 'vacation':
            self.field_absence_drawer(self.locators.VACATION)
        elif absence_tipe == 'administrative_leave':
            self.field_absence_drawer(self.locators.ADMINISTRATIVE_LEAVE)
        elif absence_tipe == 'sick_leave':
            self.field_absence_drawer(self.locators.SICK_LEAVE)
        elif absence_tipe == 'maternity_leave':
            self.field_absence_drawer(self.locators.MATERNITY_LEAVE)
        elif absence_tipe == 'overtime_work':
            return self.field_overtime_work_drawer(self.locators.OVERTIME_WORK)

    @allure.step("Заполняем поля дровера добавления отсутствий")
    def field_absence_drawer(self, locator):
        self.element_is_visible(self.locators.OPEN_ABSENCE_CHOOSE_BUTTON).click()
        self.element_is_visible(locator).click()
        this_day_text = self.element_is_visible(self.locators.BEGIN_LEAVE_DATA_INPUT).get_attribute('value')
        self.element_is_visible(self.locators.END_LEAVE_DATA_INPUT).send_keys(this_day_text)
        self.element_is_present(self.locators.FILE_INPUT).send_keys(os.path.abspath(r'../data/административный.docx'))
        self.element_is_visible(self.locators.DRAWER_SAVE_BUTTON).click()
        time.sleep(1.5)

    @allure.step("Проверяем наличие всех отсутствий в таблице")
    def check_absence_on_tab(self):
        all_day_list = self.elements_are_present(self.locators.ALL_DAYS_VALUE)
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

    @allure.step("Проверяем наличие сообщения о наложении отсутствий")
    def check_outer_absence(self):
        assert self.element_is_displayed(self.locators.HAVE_OUTER_LEAVE), "Сообщение о наложении отсутствий отсутствует"
        self.element_is_visible(self.locators.DRAWER_ABORT_BUTTON).click()

    @allure.step("Добавляем отсутствие в день где списаны трудозатраты и проверяем сообщение о наложении")
    def add_absence_to_reason_day(self):
        days_have_reason = self.get_numbers_days_reason("have")
        self.open_add_absence_drawer(days_have_reason[0])
        self.field_absence_drawer(self.locators.ADMINISTRATIVE_LEAVE)
        assert self.element_is_displayed(
            self.locators.HAVE_REASON), "Сообщение о наложении отсутствия на трудозатраты не появилось"
        self.element_is_visible(self.locators.DRAWER_ABORT_BUTTON).click()

    @allure.step("Переходим на предыдущий период")
    def go_to_previous_period(self):
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()

    @allure.step("Заполняем поля дровера переработки")
    def field_overtime_work_drawer(self, locator):
        self.element_is_visible(self.locators.OPEN_ABSENCE_CHOOSE_BUTTON).click()
        self.element_is_visible(locator).click()
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys('2')
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT).click()
        self.elements_are_visible(self.locators.ALL_PROJECT_ON_DRAWER_INPUT)[0].click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(os.path.abspath(r'../data/административный.docx'))
        self.action_move_to_element(self.element_is_present(self.locators.DRAWER_SAVE_BUTTON))
        self.element_is_present(self.locators.DRAWER_SAVE_BUTTON).click()
        output_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_present(self.locators.DRAWER_ABORT_BUTTON).click()
        time.sleep(1.5)
        return output_text

    @allure.step("Проверяем добавление пробела в поле обязательного указания переработки")
    def check_overtime_work_space_in_reason_field(self, number_empty_day, reason):
        days_zero_reason = self.get_numbers_days_reason("zero")
        self.open_add_absence_drawer(days_zero_reason[number_empty_day])
        self.element_is_visible(self.locators.OPEN_ABSENCE_CHOOSE_BUTTON).click()
        self.element_is_visible(self.locators.OVERTIME_WORK).click()
        time.sleep(0.5)  # Без этого ожидания не успевает прогрузиться
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys('4')
        self.element_is_visible(self.locators.OVERTIME_WORK_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.PROJECT_NAME_DRAWER_INPUT).click()
        self.elements_are_visible(self.locators.ALL_PROJECT_ON_DRAWER_INPUT)[0].click()
        self.element_is_visible(self.locators.OVERTIME_REASON_INPUT).send_keys(reason)
        self.element_is_present(self.locators.FILE_INPUT).send_keys(os.path.abspath(r'../data/административный.docx'))
        self.action_move_to_element(self.element_is_present(self.locators.DRAWER_SAVE_BUTTON))
        self.element_is_present(self.locators.DRAWER_SAVE_BUTTON).click()
        output_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_present(self.locators.DRAWER_ABORT_BUTTON).click()
        time.sleep(1.5)
        return output_text
