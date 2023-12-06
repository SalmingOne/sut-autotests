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

    # Переход на таблицу трудозатрат через меню
    @allure.step("Переход на таблицу трудозатрат через меню")
    def go_to_labor_cost_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_ACTIVITY))
        self.element_is_visible(self.locators.TAB_LABOR_COST_TABLE).click()

    # Проверка, что код проекта есть на странице
    @allure.step("Проверка, что код проекта есть на странице")
    def check_project_code_at_labor(self):
        check_code_at_labor = self.element_is_present(self.locators.CHECK_CODE_PROJECT).text
        return check_code_at_labor

    # Проверка что кода проекта нет на странице
    @allure.step("Проверка что кода проекта нет на странице")
    def check_no_project_code_at_labor(self):
        try:
            return self.element_is_present(self.locators.CHECK_CODE_PROJECT).text
        except TimeoutException:
            return "no element on page"

    # Проверка что появляется окно указания причины списания
    @allure.step("Проверка что появляется окно указания причины списания ")
    def check_to_have_reason_fo_write(self):
        self.element_is_visible(self.locators.RANDOM_DAYS_BY_PROJECT).click()
        checked_text = self.element_is_visible(self.locators.CHECK_LABOR_REASON_FIELD).text
        self.element_is_visible(self.locators.BREAK_LABOR_REASON_WINDOW).click()
        assert checked_text == "Причина *", "Не открылось окно указания причины"

    # Ввод значения в клетку таблицы трудозатрат
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

    # Узнаем сколько дней в конкретном месяце, что бы потом вставить значение в последний день
    @allure.step("Узнаем сколько дней в конкретном месяце, что бы потом вставить значение в последний день")
    def get_number_last_month_day(self):
        all_day_list = self.elements_are_present(self.locators.ADD_OVERTIME_WORK_BUTTON)
        numbers = []
        for day in all_day_list:
            numbers.append(day.text)
        return len(numbers)

    # Списываем трудозатраты за первый и последний день месяца
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

    # Очищаем все дни за месяц
    @allure.step("Очищаем все дни за месяц")
    def clear_month_work(self):
        all_day_list = self.elements_are_present(self.locators.ALL_DAYS_BY_PROJECT)
        for day in all_day_list:
            day.click()
            try:
                day.send_keys(Keys.BACK_SPACE)
                day.send_keys(Keys.BACK_SPACE)
            except ElementNotInteractableException:
                pass

    # Очищаем все дни за текущий, предыдущий и следующий месяц
    @allure.step("Очищаем все дни за текущий, предыдущий и следующий месяц")
    def three_mont_clear(self):
        self.clear_month_work()
        try:
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
        except ElementClickInterceptedException:
            pass
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        self.clear_month_work()
        try:
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
        except ElementClickInterceptedException:
            pass
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.clear_month_work()
        try:
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
        except ElementClickInterceptedException:
            pass
        time.sleep(1)  # Без этого ожидания не подтверждаются изменения в последнем месяце

    # Списываем трудозатраты за первый и последний день недели
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

    # Выбираем отображаемый период
    @allure.step("Выбираем отображаемый период")
    def choose_period(self, period):
        time.sleep(1)
        self.element_is_visible(self.locators.PERIOD_SELECT_BUTTON).click()
        if period == "month":
            self.element_is_visible(self.locators.MONTH_PERIOD_SELECT).click()
        elif period == "week":
            self.element_is_visible(self.locators.WEEK_PERIOD_SELECT).click()

    # Выбираем месяц в датапикере
    @allure.step("Выбираем месяц в датапикере")
    def choose_month_picker(self, month_name):  # имя месяца указывать точно как на экране(с точкой)
        self.element_is_visible(self.locators.MONTH_DATEPICKER).click()
        month = month_name
        month_locator = (By.XPATH, f'//button[text()="{month}"]')
        self.element_is_visible(month_locator).click()

    # Списываем трудозатраты за первый и последний день года
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

    # Удаляем списания за первые и последние месяцы года
    @allure.step("Удаляем списания за первые и последние месяцы года")
    def clear_work_by_year(self):
        self.choose_month_picker('янв.')
        self.clear_month_work()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        self.clear_month_work()
        self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).click()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()

        self.choose_month_picker('дек.')
        self.clear_month_work()
        self.element_is_visible(self.locators.FIRST_DAY_BY_PROJECT).click()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.clear_month_work()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()

    # Проверяем цвет поля при списании трудозатрат
    @allure.step("Проверяем цвет поля при списании трудозатрат")
    def check_change_color_on_labor_cost_field(self):
        first_day_time = 14
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

    # Проверяем наличие заголовка Трудозатраты
    @allure.step("Проверяем наличие заголовка Трудозатраты")
    def check_title(self):
        assert self.element_is_displayed(self.locators.TITLE_PAGE), "Заголовок страницы Трудозатраты отсутствует"

    # Проверяем наличие выбора периода
    @allure.step("Проверяем наличие выбора периода")
    def check_period_select(self):
        self.element_is_visible(self.locators.PERIOD_SELECT_BUTTON).click()
        menu_title_list = self.elements_are_visible(self.locators.PERIOD_MENU_ITEM)
        data = []
        for title in menu_title_list:
            data.append(title.text)
        self.action_esc()
        assert data == ['Месяц (по дням)', 'Неделя'], "Не все периоды отображены для выбора"

    # Проверяем наличие кнопки добавления себя на проект
    @allure.step("Проверяем наличие кнопки добавления себя на проект")
    def check_add_to_project_button(self):
        assert self.element_is_displayed(self.locators.ADD_TO_PROJECT_BUTTON), "Нет кнопки добавления себя на проект"

    # Проверяем наличие всех параметров фильтрации
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

    # Проверяем наличие кнопки открытия виджетов
    @allure.step("Проверяем наличие кнопки открытия виджетов")
    def check_open_widget_button(self):
        assert self.element_is_displayed(self.locators.OPEN_WIDGET_BUTTON), "Кнопки открытия виджетов нет на странице"

    # Проверяем наличие кнопки выбора месяца
    @allure.step("Проверяем наличие кнопки выбора месяца")
    def check_month_picker(self):
        assert self.element_is_displayed(self.locators.MONTH_DATEPICKER), "Нет кнопки выбора месяца"

    # Проверяем наличие кнопок следующего и предыдущего периода
    @allure.step("Проверяем наличие кнопок следующего и предыдущего периода")
    def check_next_previous_buttons(self):
        assert self.element_is_displayed(self.locators.NEXT_PERIOD_BUTTON), "Нет кнопки следующего периода"
        assert self.element_is_displayed(self.locators.PREVIOUS_PERIOD_BUTTON), "Нет кнопки предыдущего периода"

    # Проверяем наличие Итого в шапке таблицы
    @allure.step("Проверяем наличие всех дней недели в шапке таблицы")
    def check_tab_head(self):
        all_day_list = self.elements_are_visible(self.locators.ALL_DAY_NUMBER)
        numbers = []
        for day in all_day_list:
            numbers.append(day.text)
        assert 'Итого' in numbers, "Итого нет в заголовке"
        return numbers, len(numbers) - 5

    # Проверяем наличие всех дней недели в шапке таблицы
    @allure.step("Проверяем наличие всех дней недели в шапке таблицы")
    def check_week_days_head(self):
        all_day_list = self.elements_are_present(self.locators.SEVEN_DAY_ON_HEAD)
        numbers = []
        for day in all_day_list:
            numbers.append(day.text)
        day_week = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
        for a in day_week:
            assert a in numbers, "Дня недели нет в заголовке"

    # Проверяем наличие красного и белого цвета ячеек в таблице
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

    # Проверяем наличие выбранных дней при наведении на ячейку таблицы
    @allure.step("Проверяем наличие выбранных дней при наведении на ячейку таблицы")
    def check_have_selected_days(self):
        if self.element_is_displayed(self.locators.PROJECT_STRING):
            day_list = self.elements_are_visible(self.locators.ALL_DAY_COLORS)
            self.action_move_to_element(day_list[5])
            assert self.element_is_displayed(self.locators.SELECTED_DAYS), ("При наведении на ячейку таблицы на "
                                                                            "странице нет выбранных дней")
        else:
            pass

    # Проверяем наличие тултипа при наведении на код проекта
    @allure.step("Проверяем наличие тултипа при наведении на код проекта")
    def check_tooltip_on_project_code(self):
        if self.element_is_displayed(self.locators.PROJECT_STRING):
            project_list = self.elements_are_visible(self.locators.PROJECT_TITLE)
            self.action_move_to_element(project_list[0])
            assert self.element_is_displayed(self.locators.TOOLTIP), "При наведении на код проекта не появляется тултип"
            return self.element_is_visible(self.locators.TOOLTIP).text
        else:
            pass

    # Проверяем наличие кнопок сохранения и отмены
    @allure.step("Проверяем наличие кнопок сохранения и отмены")
    def check_save_and_disable_buttons(self):
        assert self.element_is_displayed(self.locators.SAVE_BUTTON)
        assert self.element_is_displayed(self.locators.DISABLE_BUTTON)

    # Переходим на отображение по имени проекта
    @allure.step("Переходим на отображение по имени проекта")
    def go_to_filter_by_project_name(self):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()
        self.element_is_visible(self.locators.FILTER_BY_PROJECT_NAME).click()
        self.action_esc()

    # Открываем модальное окно указания причины списания
    @allure.step("Открываем модальное окно указания причины списания")
    def open_reason_window(self, project_name = None):
        if project_name == None:
            self.element_is_visible(self.locators.RANDOM_DAYS_BY_PROJECT).click()
        else:
            self.element_is_visible(self.locators.get_random_day_by_project(project_name)).click()
    
    @allure.step("Нажать Сохранить в модальном окне указание часов и причины списания трудозатрат")
    def save_hours_and_reason (self):
        self.element_is_visible(self.locators.SAVE_LABOR_REASON_WINDOW_BUTTON).click()

    # Проверяем наличие заголовка на модальном окне указания причины списания
    @allure.step("Проверяем наличие заголовка на модальном окне указания причины списания")
    def check_title_reason_window(self):
        assert self.element_is_displayed(self.locators.TITLE_MODAL_REASON_WINDOW)

    # Проверяем наличие полей на модальном окне указания причины списания
    @allure.step("Проверяем наличие полей на модальном окне указания причины списания")
    def check_fields_reason_window(self):
        assert self.element_is_displayed(self.locators.INPUT_REASON_TIME_FIELD)
        assert self.element_is_displayed(self.locators.INPUT_REASON_DESCRIPTION_FIELD)

    # Проверяем наличие кнопок на модальном окне указания причины списания
    @allure.step("Проверяем наличие кнопок на модальном окне указания причины списания")
    def check_buttons_reason_window(self):
        assert self.element_is_displayed(self.locators.SAVE_LABOR_REASON_WINDOW_BUTTON)
        assert self.element_is_displayed(self.locators.BREAK_LABOR_REASON_WINDOW)

    # Закрываем модальное окно указания причины списания
    @allure.step("Закрываем модальное окно указания причины списания")
    def close_reason_window(self):
        self.element_is_visible(self.locators.BREAK_LABOR_REASON_WINDOW).click()

    # Проверяем цвет поля при удалении списания трудозатрат
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
