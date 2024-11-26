import time

import allure
import testit
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from utils.concat_testit_allure_step import allure_testit_step

from locators.gantt_page_locators import GanttPageLocators
from pages.base_page import BasePage


class GanttPage(BasePage):
    locators = GanttPageLocators()

    @testit.step("Переход на вкладку Диаграмма Ганта")
    @allure.step("Переход на вкладку Диаграмма Ганта")
    def go_to_gantt_tab(self):
        self.element_is_visible(self.locators.GANTT_TAB).click()

    @testit.step("Добавление фазы")
    @allure.step("Добавление фазы")
    def add_phase(self, phase_name):
        self.element_is_visible(self.locators.EDIT_GANTT_BUTTON).click()
        time.sleep(0.5)
        self.element_is_visible(self.locators.CREATE_PHASE_OR_TASK_BUTTON).click()
        self.element_is_visible(self.locators.CREATE_PHASE_BUTTON).click()
        self.element_is_visible(self.locators.PHASE_NAME_FIELD).send_keys(phase_name)
        self.element_is_visible(self.locators.DRAWER_SUBMIT_BUTTON).click()

    @testit.step("Проверка даты начала и окончания")
    @allure.step("Проверка даты начала и окончания")
    def check_start_and_end_dates(self, phase_name):
        time.sleep(0.5)
        start_date = self.element_is_visible(self.locators.start_date(phase_name)).get_attribute('aria-label')
        end_date = self.element_is_visible(self.locators.end_date(phase_name)).get_attribute('aria-label')
        assert start_date and end_date == self.get_day_before(0), 'Длина фазы не равна текущему дню'

    @testit.step("Проверка статуса")
    @allure.step("Проверка статуса")
    def check_status(self, phase_name):
        self.element_is_visible(self.locators.CHECK_COLUMN_TAB).click()
        self.element_is_visible(self.locators.STATUS_COLUMN_CHECKBOX).click()
        self.action_esc()
        time.sleep(0.5)
        assert self.element_is_visible(self.locators.status(phase_name)).get_attribute('aria-label') == 'Планирование', \
            "Статус фазы не Планирование"

    @testit.step("Проверка вкладки Диаграмма Ганта")
    @allure.step("Проверка вкладки Диаграмма Ганта")
    def check_gantt_tab(self):
        self.check_gantt_tab_calendar()
        self.check_gantt_project_live_line()
        self.check_gantt_today_marker_and_button()
        self.check_gantt_grid()
        self.check_gantt_tune_icon()
        self.check_default_period()
        self.check_chose_period_list()
        self.check_gantt_base_plan_button()
        assert self.get_column_header() == ['№', 'Фазы и задачи', 'Начало', 'Окончание', 'План. трудозатраты (Ч.)',
                                            'Действия'], "Есть не все заголовки по умолчанию"
        self.check_fields_filter()

    @testit.step("Проверка наличия таблицы Календарь")
    @allure.step("Проверка наличия таблицы Календарь")
    def check_gantt_tab_calendar(self):
        assert self.element_is_displayed(self.locators.CALENDAR), "Нет таблицы Календарь"

    @testit.step("Проверка наличия линии жизни проекта")
    @allure.step("Проверка наличия линии жизни проекта")
    def check_gantt_project_live_line(self):
        assert self.element_is_displayed(self.locators.PROJECT_LIVE_LINE), "Нет линии жизни проекта"

    @testit.step("Проверка наличия кнопки и линии Сегодня")
    @allure.step("Проверка наличия кнопки и линии Сегодня")
    def check_gantt_today_marker_and_button(self):
        self.element_is_visible(self.locators.TODAY_BUTTON).click()
        assert self.element_is_displayed(self.locators.TODAY_MARKER), "Нет линии отмечающей сегодняшний день"

    @testit.step("Проверка наличия таблицы задач и фаз")
    @allure.step("Проверка наличия таблицы задач и фаз")
    def check_gantt_grid(self):
        assert self.element_is_displayed(self.locators.GANTT_GRID), "Нет таблицы задач и фаз"

    @testit.step("Проверка кнопки Фильтр")
    @allure.step("Проверка кнопки Фильтр")
    def check_gantt_tune_icon(self):
        assert self.element_is_displayed(self.locators.TUNE_ICON), "Нет иконки Фильтр"

    @testit.step("Проверка кнопки создания базового плана")
    @allure.step("Проверка кнопки создания базового плана")
    def check_gantt_base_plan_button(self):
        assert self.element_is_displayed(self.locators.BASE_PLAN_BUTTON), "Нет кнопки создания базового плана"

    @testit.step("Проверка периода выбранного по умолчанию")
    @allure.step("Проверка периода выбранного по умолчанию")
    def check_default_period(self):
        assert self.element_is_visible(self.locators.CHOSE_PERIOD_BUTTON).text == 'День', \
            "По умолчанию выбран период не День"

    @testit.step("Проверка списка выбора периодов")
    @allure.step("Проверка списка выбора периодов")
    def check_chose_period_list(self):
        self.element_is_visible(self.locators.CHOSE_PERIOD_BUTTON).click()
        all_items = self.elements_are_visible(self.locators.LI_MENU_ITEM)
        text = []
        for item in all_items:
            text.append(item.text)
        self.action_esc()
        assert text == ['Год', 'Месяц', 'Неделя', 'День'], "Можно выбрать не все периоды"

    @testit.step("Получение заголовков таблицы фаз")
    @allure.step("Получение заголовков таблицы фаз")
    def get_column_header(self):
        time.sleep(1)
        all_headers = self.elements_are_visible(self.locators.COLUMN_HEADER)
        header_text = []
        for header in all_headers:
            header_text.append(header.text)
        return header_text

    @testit.step("Проверка чекбоксов выбора полей")
    @allure.step("Проверка чекбоксов выбора полей")
    def check_fields_filter(self):
        self.element_is_visible(self.locators.FIELDS_FILTER).click()
        assert self.get_all_checkboxes_text() == ['Таблица', 'Диаграмма', 'Слоты/исполнители', 'Начало', 'Окончание',
                                                  'Факт. начало', 'Факт. окончание', 'План. трудозатраты (Ч.)',
                                                  'План. длительность задач (Д.)', 'Затраченное время (Ч.)', 'Статус'], \
            "Есть не все чекбоксы"
        self.action_esc()

    @testit.step("Получение текста всех чекбоксов")
    @allure.step("Получение текста всех чекбоксов")
    def get_all_checkboxes_text(self):
        all_checkboxes = self.elements_are_visible(self.locators.CHECKBOXES_TEXT)
        checkboxes_text = []
        for checkbox in all_checkboxes:
            checkboxes_text.append(checkbox.text)
        return checkboxes_text

    @allure_testit_step('Включить/выключить чекбокс')
    def toggle_checkbox(self, checkbox_name):
        match checkbox_name:
            case 'Таблица':
                self.elements_are_visible(self.locators.CHECKBOXES)[0].click()
            case 'Диаграмма':
                self.elements_are_visible(self.locators.CHECKBOXES)[1].click()

    @allure_testit_step('Получить текст тултипа')
    def get_tooltip_text(self, task):
        self.action_move_to_element(self.element_is_visible(self.locators.get_task(task)))
        return self.element_is_visible(self.locators.GANTT_TOOLTIP).text

    @allure_testit_step('Получить статус отображения диаграммы Ганта')
    def get_status_of_gantt_task(self):
        return self.element_is_displayed(self.locators.GANT_TASK)

    @allure_testit_step('Получить типы столбцов таблицы')
    def get_columns_types(self):
        return set(div.get_attribute('data-column-name') for element in self.elements_are_visible(self.locators.TABLE_ROWS) for div in element.find_elements(By.XPATH, './div'))

    @allure_testit_step('Получить статус чекбокса')
    def get_status_of_checkbox(self, checkbox_name, status):
        icon_testid = "CheckBoxIcon" if status == "Активно" else "CheckBoxOutlineBlankIcon"
        try:
            match checkbox_name:
                case 'Таблица':
                    self.elements_are_visible(self.locators.CHECKBOXES)[0].find_element(By.XPATH, f'./*[@data-testid="{icon_testid}"]')
                case 'Диаграмма':
                    self.elements_are_visible(self.locators.CHECKBOXES)[1].find_element(By.XPATH, f'./*[@data-testid="{icon_testid}"]')
                case _:
                    return None
            return True
        except TimeoutException:
            return False

