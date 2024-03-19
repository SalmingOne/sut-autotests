import time

import allure
import testit

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
        assert self.element_is_displayed(self.locators.CLEAR_ICON), 'Нет кнопки очистки дровера'

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
        assert 'Начало рабочего дня' in before, 'Нет поля длительность отгула'
        assert 'Начало рабочего дня' not in after, 'Есть поле длительность отгула при расчете по дням'

    @testit.step("Проверка полей дровера")
    @allure.step("Проверка полей дровера")
    def check_taking_time_off_fields(self):
        fields = self.get_drawer_fields_title()
        assert fields == ['Полный день', 'Дата отгула\u2009*', 'Начало рабочего дня', 'Длительность',
                          'Окончание рабочего дня', 'Дата отработки\u2009*', 'Начало отработки',
                          'Длительность', 'Окончание отработки'], 'В дровере есть не все поля'

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


