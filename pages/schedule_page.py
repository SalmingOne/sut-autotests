import time

import allure
import testit
from selenium.webdriver import Keys

from locators.schedule_page_locators import SchedulePageLocators
from pages.base_page import BasePage


class SchedulePage(BasePage):
    locators = SchedulePageLocators()

    @testit.step("Переход на страницу Режим работы")
    @allure.step("Переход на страницу Режим работы")
    def go_to_schedule_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_ACTIVITY))
        self.element_is_visible(self.locators.TAB_SCHEDULE).click()

    @testit.step("Открытие дровера редактирования графика конкретного дня")
    @allure.step("Открытие дровера редактирования графика конкретного дня")
    def open_editing_schedule_for_a_specific_day_drawer(self):
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        time.sleep(1)  # Без ожидания не всегда успевает прогрузиться страница
        self.elements_are_visible(self.locators.ALL_CHIPS_BUTTON)[0].click()

    @testit.step("Открытие дровера редактирования стандартного графика")
    @allure.step("Открытие дровера редактирования стандартного графика")
    def open_editing_schedule_for_a_standard_chart_drawer(self):
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        time.sleep(1)  # Без ожидания не всегда успевает прогрузиться страница
        self.elements_are_visible(self.locators.ALL_PLUS_BUTTON)[0].click()

    @testit.step("Получение заголовка дровера")
    @allure.step("Получение заголовка дровера")
    def get_drawer_title(self):
        return self.element_is_visible(self.locators.DRAWER_TITLE).text

    @testit.step("Получение заголовков полей дровера")
    @allure.step("Получение заголовков полей дровера")
    def get_drawer_fields_title(self):
        all_titles = self.elements_are_visible(self.locators.DRAWER_FIELDS_LABELS)
        data = []
        for title in all_titles:
            data.append(title.text)
        return data

    @testit.step("Проверка времени перерыва по умолчанию")
    @allure.step("Проверка времени перерыва по умолчанию")
    def check_break_time(self):
        assert self.element_is_visible(self.locators.START_BREAK).get_attribute('value') == '13:00', 'Не корректное время начала перерыва по умолчанию'
        assert self.element_is_visible(self.locators.END_BREAK).get_attribute('value') == '14:00', 'Не корректное время окончания перерыва по умолчанию'

    @testit.step("Проверка кнопки добавления перерыва")
    @allure.step("Проверка кнопки добавления перерыва")
    def check_add_break_button(self):
        for a in range(7):
            self.element_is_visible(self.locators.ADD_BREAK_BUTTON).click()
        assert self.element_is_clickable(self.locators.ADD_BREAK_BUTTON, 2) == False, 'Кнопка добавления перерыва не задизейблена'

    @testit.step("Проверка кнопки удаления перерыва")
    @allure.step("Проверка кнопки удаления перерыва")
    def check_break_delete_icon(self):
        assert len(self.elements_are_visible(self.locators.DELETE_BREAK_BUTTON)) == 7

    @testit.step("Проверка кнопок сохранить и отменить")
    @allure.step("Проверка кнопок сохранить и отменить")
    def check_submit_and_break_button(self):
        assert self.element_is_displayed(self.locators.DRAWER_SUBMIT_BUTTON), 'Нет кнопки сохранить'
        assert self.element_is_displayed(self.locators.DRAWER_BREAK_BUTTON), 'Нет кнопки отменить'

    @testit.step("Проверка наличия кнопки очистки дровера")
    @allure.step("Проверка наличия кнопки очистки дровера")
    def check_x_button(self):
        assert self.element_is_displayed(self.locators.CLEAR_ICON_IN_REDACT_DRAWER), 'Нет кнопки очистки дровера'

    @testit.step("Проверка наличия чекбоксов с днями недели и свича")
    @allure.step("Проверка наличия чекбоксов с днями недели и свича")
    def check_week_days_checkboxes_and_switch(self):
        assert len(self.elements_are_present(self.locators.WEEK_CHECKBOXES)) == 8, 'Нет чекбоксов с днями недели и свича'

    @testit.step("Открытие дровера взятия отгула")
    @allure.step("Открытие дровера взятия отгула")
    def open_take_off_drawer(self):
        self.element_is_visible(self.locators.TAKE_OFF_BUTTON).click()

    @testit.step("Проверка переключения по часам/полный день")
    @allure.step("Проверка переключения по часам/полный день")
    def check_switch_by_day(self):
        before = self.get_drawer_fields_title()
        self.element_is_visible(self.locators.SWITCH_BY_DAY).click()
        after = self.get_drawer_fields_title()
        assert 'Начало отгула' in before, 'Нет поля длительность отгула'
        assert 'Начало отгула' not in after, 'Есть поле длительность отгула при расчете по дням'

    @testit.step("Проверка полей дровера")
    @allure.step("Проверка полей дровера")
    def check_taking_time_off_fields(self):
        fields = self.get_drawer_fields_title()
        assert fields == ['Полный день', 'Дата отгула\u2009*', 'Начало отгула', 'Длительность', 'Окончание отгула',
                          'Дата отработки\u2009*', 'Начало отработки', 'Длительность', 'Окончание отработки'],\
            'В дровере есть не все поля'

    @testit.step("Проверка выбора даты отгула раньше сегодняшней")
    @allure.step("Проверка выбора даты отгула раньше сегодняшней")
    def check_disable_previous_date_on_date_picker(self):
        self.element_is_visible(self.locators.TAKE_OFF_DATA_PICKER).click()
        assert self.element_is_clickable(self.locators.THIS_DAY_PICKER), 'Нельзя выбрать текущую дату'
        assert not self.element_is_clickable(self.locators.DAY_BEFORE_THIS_DAY_PICKER, 2), 'Можно выбрать предыдущую дату'

    @testit.step("Проверка добавления и удаления даты отработки")
    @allure.step("Проверка добавления и удаления даты отработки")
    def check_add_and_delete_taking_time_off_buttons(self):
        self.element_is_visible(self.locators.ADD_TAKE_OFF_DATA_BUTTON).click()
        self.element_is_visible(self.locators.DELETE_BREAK_BUTTON).click()

    @testit.step("Проверка элемента с номером текущей недели")
    @allure.step("Проверка элемента с номером текущей недели")
    def check_number_week_displayed(self):
        assert self.element_is_displayed(self.locators.THIS_WEEK_NUMBER), 'Нет элемента с номером текущей недели'

    @testit.step("Проверка кнопок переключения периода и кнопки Сегодня")
    @allure.step("Проверка кнопок переключения периода и кнопки Сегодня")
    def check_switch_periods_and_this_day_button(self):
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        assert not self.element_is_clickable(self.locators.THIS_DAY_BUTTON, 2), "Кнопка Сегодня не задизейблена"

    @testit.step("Проверка кнопки редактирования")
    @allure.step("Проверка кнопки редактирования")
    def check_redact_button(self):
        assert self.element_is_displayed(self.locators.REDACT_BUTTON), 'Нет кнопки редактирования'

    @testit.step("Проверка кнопки добавления отгула")
    @allure.step("Проверка кнопки добавления отгула")
    def check_add_take_off_button(self):
        assert self.element_is_displayed(self.locators.TAKE_OFF_BUTTON), 'Нет кнопки добавления отгула'

    @testit.step("Проверка отображения рабочих часов")
    @allure.step("Проверка отображения рабочих часов")
    def check_hours_in_day_fields(self):
        assert len(self.elements_are_visible(self.locators.WORK_HOURS_IN_DAY)) == 24, 'Не над каждым днем отображаются рабочие часы'

    @testit.step("Переход на следующий период")
    @allure.step("Переход на следующий период")
    def go_to_next_period(self):
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()

    @testit.step("Получение текста с чипсы режима работы")
    @allure.step("Получение текста с чипсы режима работы")
    def get_text_on_chips(self, number_element):
        return self.elements_are_visible(self.locators.ALL_CHIPS_BUTTON)[number_element].text

    @testit.step("Начало редактирования")
    @allure.step("Начало редактирования")
    def press_redact_button(self):
        self.element_is_visible(self.locators.REDACT_BUTTON).click()

    @testit.step("Выбор чипсы для редактирования")
    @allure.step("Выбор чипсы для редактирования")
    def open_chips_to_edit(self, number_element):
        self.elements_are_visible(self.locators.ALL_CHIPS_BUTTON)[number_element].click()

    @testit.step("Редактирование начала работы и начала перерыва")
    @allure.step("Редактирование начала работы и начала перерыва")
    def editing_a_specific_day(self, start_work, start_break):
        self.element_is_visible(self.locators.START_WORK).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.START_WORK).send_keys(start_work)
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()
        self.element_is_visible(self.locators.START_BREAK).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.START_BREAK).send_keys(start_break)
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()
        self.element_is_visible(self.locators.DRAWER_SUBMIT_BUTTON).click()

    @testit.step("Проверка наличия модального окна первого запуска")
    @allure.step("Проверка наличия модального окна первого запуска")
    def check_text_on_modal(self):
        return self.element_is_displayed(self.locators.TEXT_IN_MODAL)

    @testit.step("Нажатие кнопки сохранить модального окна первого запуска")
    @allure.step("Нажатие кнопки сохранить модального окна первого запуска")
    def press_submit_button_in_modal(self):
        self.element_is_visible(self.locators.SUBMIT_IN_MODAL).click()
