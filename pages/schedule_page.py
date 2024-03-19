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

    @testit.step("Проверка заголовка дровера")
    @allure.step("Проверка заголовка дровера")
    def check_drawer_title(self):
        title = self.element_is_visible(self.locators.DRAWER_TITLE).text
        assert 'Редактирование графика' in title, 'В заголовке нет слов Редактирование графика'

    @testit.step("Проверка заголовков полей дровера")
    @allure.step("Проверка заголовков полей дровера")
    def check_drawer_fields_title(self):
        all_titles = self.elements_are_visible(self.locators.DRAWER_FIELDS_LABELS)
        data = []
        for title in all_titles:
            data.append(title.text)
        assert data == ['Начало рабочего дня', 'Длительность', 'Окончание рабочего дня', 'Начало перерыва',
                        'Длительность', 'Окончание перерыва'], 'В дровере есть не все поля'

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
