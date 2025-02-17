import time

import allure
import testit

from locators.vacation_schedule_locators import VacationSchedulePageLocators
from pages.base_page import BasePage


class VacationSchedulePage(BasePage):
    locators = VacationSchedulePageLocators()

    @testit.step("Переходим на страницу График отпусков")
    @allure.step("Переходим на страницу График отпусков")
    def go_to_vacation_schedule_page(self):
        time.sleep(0.3)
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_MORE))
        self.element_is_visible(self.locators.TAB_VACATION_SCHEDULE).click()

    @testit.step("Есть шапка таблицы и в ней 12 или больше недель")
    @allure.step("Есть шапка таблицы и в ней 12 или больше недель")
    def check_header_and_week_in_header(self):
        assert len(self.elements_are_visible(
            self.locators.WEEKS_IN_VACATION_SCHEDULE_HEADER)) >= 12, "В шапке графика отпусков меньше 12 недель"
        assert self.element_is_displayed(self.locators.VACATION_SCHEDULE_HEADER), "Нет шапки таблицы"

    @testit.step("Есть тултип с номером недели")
    @allure.step("Есть тултип с номером недели")
    def check_tooltip(self):
        time.sleep(0.5)
        self.action_move_to_element(self.element_is_visible(self.locators.FIRST_WEEK_IN_VACATION_SCHEDULE_HEADER))
        self.action_move_to_element(self.element_is_visible(self.locators.VACATION_SCHEDULE_HEADER))
        assert 'Неделя №' in self.element_is_visible(self.locators.TOOLTIP).text, "В тултипе не отображается номер недели"

    @testit.step("Текущая неделя выделена цветом")
    @allure.step("Текущая неделя выделена цветом")
    def check_color_this_week(self):
        color_this_week = self.element_is_visible(self.locators.TODAY_WEEK).value_of_css_property('color')
        assert color_this_week == 'rgba(25, 118, 210, 1)', "Текущая неделя не выделена синим цветом"

    @testit.step("Есть стрелки для перемещения по кварталам")
    @allure.step("Есть стрелки для перемещения по кварталам")
    def check_arrows(self):
        assert self.element_is_displayed(self.locators.NEXT_PERIOD_BUTTON), "Нет стрелки перехода на следующий период"
        assert self.element_is_displayed(self.locators.PREVIOUS_PERIOD_BUTTON), "Нет стрелки перехода на предыдущий период"

    @testit.step("Есть кнопка сегодня")
    @allure.step("Есть кнопка сегодня")
    def check_this_day_button(self):
        assert self.element_is_displayed(self.locators.THIS_DAY_BUTTON), "Нет кнопки Сегодня"

    @testit.step("Есть фильтр Отображение с полями и чекбоксом")
    @allure.step("Есть фильтр Отображение с полями и чекбоксом")
    def check_filter_drover(self):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()
        checkbox_text = self.element_is_visible(self.locators.CHECKBOX_ON_FILTER).text
        fields = self.elements_are_visible(self.locators.FILTER_INPUT_PLACEHOLDERS)
        placeholders = []
        for i in fields:
            placeholders.append(i.get_attribute("placeholder"))
        assert placeholders == ['Отфильтровать по проекту', 'Поиск сотрудника...'], "Нет полей фильтрации по проекту и сотруднику"
        assert checkbox_text == 'Показывать только пользователей с отпусками', "Нет чекбокса пользователи с отпусками"
        self.action_esc()

    @testit.step("Есть строки с Именами пользователей")
    @allure.step("Есть строки с Именами пользователей")
    def check_user_rows(self):
        assert self.element_is_displayed(self.locators.ALL_USER_NAMES), "Нет строк с пользователями"

    @testit.step("Есть строки с проектными ролями")
    @allure.step("Есть строки с проектными ролями")
    def check_roles_rows(self):
        assert self.element_is_displayed(self.locators.ALL_PROJECTS_ROLES), "Нет строк с проектными ролями"
