import time

import allure
import testit
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from locators.gantt_page_locators import GanttPageLocators
from pages.base_page import BasePage
from utils.concat_testit_allure_step import allure_testit_step


class GanttPage(BasePage):
    locators = GanttPageLocators()

    @testit.step("Переход на вкладку Диаграмма Ганта")
    @allure.step("Переход на вкладку Диаграмма Ганта")
    def go_to_gantt_tab(self):
        self.element_is_visible(self.locators.GANTT_TAB).click()

    @testit.step("Добавление фазы")
    @allure.step("Добавление фазы")
    def add_phase(self, phase_name, parent_name='', drawer_is_opened=False):
        if not drawer_is_opened:
            self.element_is_visible(self.locators.EDIT_GANTT_BUTTON).click()
            time.sleep(0.5)
            self.element_is_visible(self.locators.CREATE_PHASE_OR_TASK_BUTTON).click()
            self.element_is_visible(self.locators.CREATE_PHASE_BUTTON).click()
        if parent_name:
            parent_name_field = self.element_is_visible(self.locators.PARENT_PHASE_NAME)
            self.action_select_all_text(parent_name_field)
            parent_name_field.send_keys(parent_name)
            self.element_is_visible(self.locators.DROPDOWN_ITEMS).click()
        self.element_is_visible(self.locators.PHASE_NAME_FIELD).send_keys(phase_name)
        time.sleep(0.5)
        if self.element_is_clickable(self.locators.DRAWER_SUBMIT_BUTTON):
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
        return set(
            div.get_attribute('data-column-name') for element in self.elements_are_visible(self.locators.TABLE_ROWS) for
            div in element.find_elements(By.XPATH, './div'))

    @allure_testit_step('Получить статус чекбокса')
    def get_status_of_checkbox(self, checkbox_name, status):
        icon_testid = "CheckBoxIcon" if status == "Активно" else "CheckBoxOutlineBlankIcon"
        try:
            match checkbox_name:
                case 'Таблица':
                    self.elements_are_visible(self.locators.CHECKBOXES)[0].find_element(By.XPATH,
                                                                                        f'./*[@data-testid="{icon_testid}"]')
                case 'Диаграмма':
                    self.elements_are_visible(self.locators.CHECKBOXES)[1].find_element(By.XPATH,
                                                                                        f'./*[@data-testid="{icon_testid}"]')
                case _:
                    return None
            return True
        except TimeoutException:
            return False

    @allure_testit_step('Перейти в режим редактирования диаграммы')
    def edit_diagram(self):
        self.element_is_visible(self.locators.EDIT_GANTT_BUTTON).click()

    @allure_testit_step('Получить все сообщения системы')
    def get_errors_on_page(self):
        return self.get_all_alert_message(self.locators.ALERT_MESSAGE)

    @allure_testit_step('Получить названия фаз')
    def get_phases_name(self):
        try:
            return [element.text.split('\n')[1] for element in self.elements_are_visible(self.locators.PHASES_NAME)]
        except TimeoutException:
            return []

    @allure_testit_step('Получить названия задач')
    def get_task_name(self):
        try:
            return [element.text.split('\n')[1] for element in self.elements_are_visible(self.locators.TASKS_NAME)]
        except TimeoutException:
            return []

    @allure_testit_step('Получить номер задачи/фазы')
    def get_number_of_task_or_phase(self, name):
        return [element.text for element in
                self.elements_are_visible(self.locators.get_number_of_task_or_phase_by_name(name))]

    @allure_testit_step('Сохранить изменения в таблице')
    def save_changes(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @allure_testit_step('Отменить изменения в таблице')
    def discard_changes(self, confirm):
        self.element_is_visible(self.locators.DISCARD_BUTTON).click()
        time.sleep(1)
        if confirm:
            self.element_is_visible(self.locators.MODAL_SUBMIT_BUTTON).click()
        else:
            self.element_is_visible(self.locators.MODAL_ABORT_BUTTON).click()

    @allure_testit_step('Проверить отображение кнопок в режиме редактирования диаграммы Ганта')
    def buttons_are_displayed(self):
        assert self.element_is_displayed(
            self.locators.SUBMIT_BUTTON), "Кнопка Сохранить не отображается в режиме редактирования диаграммы Ганта"
        assert self.element_is_displayed(
            self.locators.DISCARD_BUTTON), "Кнопка Отменить не отображается в режиме редактирования диаграммы Ганта"

    @allure_testit_step('Получить сообщения ошибок валидации полей')
    def get_mui_error_messages(self):
        return [element.text for element in self.elements_are_visible(self.locators.MUI_ERROR)]

    # Потом возможно добавятся еще поля
    @allure_testit_step('Очистить обязательные поля')
    def clear_required_fields(self):
        element = self.element_is_visible(self.locators.PHASE_NAME_FIELD)
        self.action_select_all_text(element)
        element.send_keys(Keys.BACKSPACE)

    @allure_testit_step('Получить цвет рамки поля название')
    def get_field_border_color(self):
        return self.element_is_visible(self.locators.FIELD_BORDER).value_of_css_property('border-color')

    @allure_testit_step('Проверить отображение модального окна')
    def check_modal_window(self, message: str):
        assert message == self.element_is_visible(self.locators.MODAL_MESSAGE).text, "Неправильный текст сообщения"
        assert self.element_is_displayed(self.locators.MODAL_SUBMIT_BUTTON), "Нет кнопки подтверждения"
        assert self.element_is_displayed(self.locators.MODAL_ABORT_BUTTON), "Нет кнопки отмены"

    @allure_testit_step('Удаление или редактирование фазы/задачи')
    def modify_phase_or_task(self, phase_or_task_name, action, confirm=True):
        self.element_is_visible(self.locators.EDIT_GANTT_BUTTON).click()
        time.sleep(5)
        self.element_is_visible(self.locators.get_kebab_menu_by_name(phase_or_task_name)).click()
        match action:
            case 'Удалить':
                if self.element_is_visible(self.locators.LI_KEBAB_DELETE_BUTTON).get_attribute('aria-label'):
                    self.action_move_to_element(self.element_is_visible(self.locators.KEBAB_DELETE_BUTTON))
                    is_deleted = False
                    assert 'Нельзя удалить фазу/задачу, на задачи которой списаны часы' == self.element_is_visible(
                        self.locators.TOOLTIP).text, "Неверный текст тултипа"
                else:
                    self.element_is_visible(self.locators.KEBAB_DELETE_BUTTON).click()
                    is_deleted = True
                    try:
                        self.check_modal_window(f'Вы действительно хотите удалить фазу "{phase_or_task_name}"?')
                    except AssertionError:
                        self.check_modal_window(f'Вы действительно хотите удалить задачу "{phase_or_task_name}"?')
                if is_deleted:
                    button = self.element_is_visible(
                        self.locators.MODAL_SUBMIT_BUTTON) if confirm else self.element_is_visible(
                        self.locators.MODAL_ABORT_BUTTON)
                    button.click()
            case "Редактировать":
                self.element_is_visible(self.locators.KEBAB_EDIT_BUTTON).click()
                self.clear_required_fields()
                self.element_is_visible(self.locators.PHASE_NAME_FIELD).send_keys('Новое имя')
                self.element_is_visible(self.locators.DRAWER_SUBMIT_BUTTON).click()
                assert 'Новое имя' in self.get_phases_name(), "Изменения не сохранены"

    @allure_testit_step('Сменить статус фазы/задачи')
    def change_status(self, phase_or_task_name):
        self.element_is_visible(self.locators.get_kebab_menu_by_name(phase_or_task_name)).click()
        self.element_is_visible(self.locators.KEBAB_CHANGE_STATUS_BUTTON).click()

    #   Пока только открытие дровера

    @allure_testit_step('Проверить отображение элементов дровера изменения статуса')
    def check_drawer_items(self):
        assert self.element_is_displayed(self.locators.STATUS_FIELD), "Не отображается поле Статус"
        assert self.element_is_displayed(self.locators.DATE_FIELD), "Не отображается поле Дата изменения"
        assert self.get_day_before(0) == self.element_is_visible(self.locators.DATE_FIELD).get_attribute('value'), \
            "Дата изменения по умолчанию не сегодняшняя"
        assert self.element_is_displayed(self.locators.CHANGE_STATUS_DRAWER_SUBMIT_BUTTON), ("Не отображается кнопка "
                                                                                             "сохранения")
        assert self.element_is_displayed(self.locators.CHANGE_STATUS_DRAWER_DISCARD_BUTTON), ("Не отображается "
                                                                                              "кнопка отмены")
