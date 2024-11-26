import time
from datetime import datetime

import allure
import testit

from locators.production_calendar_page_locators import ProductionCalendarPageLocators
from pages.base_page import BasePage


class ProductionCalendarPage(BasePage):
    locators = ProductionCalendarPageLocators()

    @testit.step("Переход на страницу Производственный календарь")
    @allure.step("Переход на страницу Производственный календарь")
    def go_to_production_calendar_page(self):
        time.sleep(1)
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_MORE))
        self.element_is_visible(self.locators.TAB_PRODUCTION_CALENDAR).click()

    @testit.step("Проверка заголовков")
    @allure.step("Проверка заголовков")
    def check_title(self):
        all_titles = self.elements_are_visible(self.locators.TITLES)
        data = []
        for title in all_titles:
            data.append(title.text)
        assert 'Производственный календарь' in data, "Нет заголовка производственный календарь"
        assert 'Январь' or 'Июль' in data, "Нет заголовка с названием месяца"
        assert 'I квартал' or 'III квартал' in data, "Нет заголовка с номером квартала"
        assert datetime.now().strftime("III-IV кварталы %Y") or datetime.now().strftime("I-II кварталы %Y") in data, "Нет заголовка с текущим годом"

    @testit.step("Проверка наличия кнопок следующего и предыдущего периода")
    @allure.step("Проверка наличия кнопок следующего и предыдущего периода")
    def check_next_previous_buttons(self):
        assert self.element_is_displayed(self.locators.NEXT_PERIOD_BUTTON), "Нет кнопки следующего периода"
        assert self.element_is_displayed(self.locators.PREVIOUS_PERIOD_BUTTON), "Нет кнопки предыдущего периода"

    @testit.step("Проверка заголовков с днями недели")
    @allure.step("Проверка заголовков с днями недели")
    def check_week_title(self):
        all_titles = self.elements_are_visible(self.locators.WEEK_TITLES)
        data = []
        for title in all_titles:
            data.append(title.text)
        assert 'ПН' and 'ВТ' and 'СР' and 'ЧТ' and 'ПТ' and 'СБ' and 'ВС' in data, "Есть не все дни недели"

    @testit.step("Проверка строки с количеством рабочих часов")
    @allure.step("Проверка строки с количеством рабочих часов")
    def check_work_hours_title(self):
        assert 'Рабочие часы:' in self.elements_are_present(self.locators.WORK_HOUR_TITLES)[0].text,\
            "Нет строки Рабочие часы"

    @testit.step("Проверка цветов в легенде")
    @allure.step("Проверка цветов в легенде")
    def check_legend_colors(self):
        time.sleep(1)
        print(self.element_is_visible(self.locators.LEGEND_TODAY).value_of_css_property(
            'border'))
        assert self.element_is_visible(self.locators.LEGEND_TODAY).value_of_css_property(
            'border') == '1px solid rgb(46, 125, 50)', "Не корректный цвет текущего дня"
        assert self.element_is_visible(self.locators.LEGEND_HOLIDAY).value_of_css_property(
            'background-color') == 'rgba(198, 40, 40, 0.3)', "Не корректный цвет праздничного дня"
        assert self.element_is_visible(self.locators.LEGEND_WEEKEND).value_of_css_property(
            'background-color') == 'rgba(255, 207, 204, 0.5)', "Не корректный цвет выходного дня"
        assert self.element_is_visible(self.locators.LEGEND_PRE_HOLIDAY).value_of_css_property(
            'background-color') == 'rgba(255, 192, 140, 0.5)', "Не корректный цвет предпраздничного дня"

    @testit.step("Проверка цветов в календаре")
    @allure.step("Проверка цветов в календаре")
    def check_calendar_colors(self):
        assert self.elements_are_visible(self.locators.CALENDAR_TODAY)[0].value_of_css_property(
            'border') == '1px solid rgb(46, 125, 50)', "Не корректный цвет текущего дня"
        assert self.elements_are_visible(self.locators.CALENDAR_HOLIDAY)[0].value_of_css_property(
            'background-color') == 'rgba(198, 40, 40, 0.3)', "Не корректный цвет праздничного дня"
        assert self.elements_are_visible(self.locators.CALENDAR_WEEKEND)[0].value_of_css_property(
            'background-color') == 'rgba(255, 207, 204, 0.5)', "Не корректный цвет выходного дня"
        assert self.elements_are_visible(self.locators.CALENDAR_PRE_HOLIDAY)[0].value_of_css_property(
            'background-color') == 'rgba(255, 192, 140, 0.5)', "Не корректный цвет предпраздничного дня"

    @testit.step("Проверка информации о квартале")
    @allure.step("Проверка информации о квартале")
    def check_quarter_info(self):
        assert self.element_is_displayed(self.locators.QUARTER_CALENDAR_DAYS), "Нет количества календарных дней"
        assert self.element_is_displayed(self.locators.QUARTER_WORK_DAYS), "Нет количества рабочих дней"
        assert self.element_is_displayed(self.locators.QUARTER_HOLIDAY_DAYS), "Нет количества выходных и праздничных дней"
        assert self.element_is_displayed(self.locators.QUARTER_PRE_HOLIDAY_DAYS), "Нет количества предпраздничных дней"