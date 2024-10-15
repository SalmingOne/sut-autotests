import time

import allure
import testit
from selenium.webdriver.common.by import By

from locators.pivot_tab_page_locators import PivotTabPageLocators
from pages.base_page import BasePage
from data.models.create_project_model import CreateProject


class PivotTabPage(BasePage):
    locators = PivotTabPageLocators()

    @testit.step("Переходим на сводную таблицу через меню")
    @allure.step("Переходим на сводную таблицу через меню")
    def go_to_pivot_page(self):
        time.sleep(1)
        self.element_is_visible(self.locators.ANALYTIC_MENU_BUTTON).click()
        self.element_is_visible(self.locators.PIVOT_TAB_BUTTON).click()
        self.element_is_visible(self.locators.ICON_TREE_CLOSED, 15)

    @testit.step("Выбираем отображаемый период")
    @allure.step("Выбираем отображаемый период")
    def choose_period(self, period):
        time.sleep(1)
        self.element_is_visible(self.locators.PERIOD_SELECT_BUTTON).click()
        if period == "month":
            self.element_is_visible(self.locators.MONTH_PERIOD_SELECT).click()
        elif period == "month_by_day":
            self.element_is_visible(self.locators.MONTH_BY_DAY_PERIOD_SELECT).click()
        elif period == "week":
            self.element_is_visible(self.locators.WEEK_PERIOD_SELECT).click()
        elif period == "year":
            self.element_is_visible(self.locators.YEAR_PERIOD_SELECT).click()

    @testit.step("Берем id строки нужного проекта для дальнейшего поиска")
    @allure.step("Берем id строки нужного проекта для дальнейшего поиска")
    def get_row_id(self, tab):
        if tab == "project":
            row_id = self.element_is_visible(self.locators.GET_ROW_ID).get_attribute("row-id")
            return row_id
        elif tab == "user":
            row_id = self.element_is_visible(self.locators.GET_ROW_ID_ON_USER).get_attribute("row-id")
            return row_id

    @testit.step("Берем сумму списанных часов за период по проекту")
    @allure.step("Берем сумму списанных часов за период по проекту")
    def get_sum_reason_on_project(self, period):
        row_id = self.get_row_id("project")
        if period == "month":
            period_sum = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@aria-colindex="8"]/p')
            a = self.element_is_visible(period_sum).text
            print(a)
            return a
        elif period == "week":
            period_sum = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@aria-colindex="10"]//p')
            a = self.element_is_visible(period_sum).text
            print(a)
            return a
        elif period == "year":
            period_sum = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@aria-colindex="15"]//p')
            a = self.element_is_visible(period_sum).text
            print(a)
            return a

    @testit.step("Берем сумму списанных часов за период по пользователю")
    @allure.step("Берем сумму списанных часов за период по пользователю")
    def get_sum_reason_on_user(self):
        row_id = self.get_row_id("user")
        period_sum = (By.XPATH, f'//div[@row-id="{row_id}"]//div[@col-id="workdaysHoursSum"]/p')
        a = self.element_is_visible(period_sum).text
        print(a)
        return a

    @testit.step("Переходим на отображение таблицы по пользователю")
    @allure.step("Переходим на отображение таблицы по пользователю")
    def go_to_by_user_tab(self):
        self.element_is_visible(self.locators.BY_USER_BUTTON).click()
        self.element_is_visible(self.locators.ICON_TREE_CLOSED, 15)

    @testit.step("Переходим на отображение таблицы по проектам")
    @allure.step("Переходим на отображение таблицы по проектам")
    def go_to_by_project_tab(self):
        self.element_is_visible(self.locators.BY_PROJECT_BUTTON).click()
        self.element_is_visible(self.locators.ICON_TREE_CLOSED, 15)

    @testit.step("Открываем список проектов пользователя")
    @allure.step("Открываем список проектов пользователя")
    def open_project_list(self):
        self.element_is_visible(self.locators.OPEN_PROJECT_LIST).click()

    @testit.step("Открываем дровер фильтрации (отображение)")
    @allure.step("Открываем дровер фильтрации (отображение)")
    def open_filter(self):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()

    @testit.step("Берем aria-colindex текущего столбца")
    @allure.step("Берем aria-colindex текущего столбца")
    def get_today_col_index(self):
        return self.element_is_visible(self.locators.HEADER_TODAY).get_attribute('aria-colindex')

    @testit.step("Проверяем отображение переработок в таблице по проектам")
    @allure.step("Проверяем отображение переработок в таблице по проектам")
    def check_overwork_by_project(self):
        row_id = self.element_is_visible(self.locators.get_row_id_on_project(CreateProject().name)).get_attribute("row-id")
        col_index = self.get_today_col_index()
        this_period = self.element_is_visible(self.locators.intersection_field(row_id, col_index)).text
        end_month = self.element_is_visible(self.locators.intersection_field(row_id, 8)).text
        assert this_period == end_month, 'Переработки не отразились в итоговом столбце '
        assert this_period == '3 + 3', 'Переработки не отразились в текущем столбце'

    @testit.step("Проверяем отображение переработок в таблице по пользователям")
    @allure.step("Проверяем отображение переработок в таблице по пользователям")
    def check_overwork_by_user(self):
        row_id = self.element_is_visible(self.locators.get_row_id_on_user(CreateProject().name)).get_attribute("row-id")
        col_index = self.get_today_col_index()
        this_period = self.element_is_visible(self.locators.intersection_field(row_id, col_index)).text
        end_month = self.element_is_visible(self.locators.intersection_field(row_id, 8)).text
        assert this_period == end_month, 'Переработки не отразились в итоговом столбце '
        assert this_period == '3 + 3', 'Переработки не отразились в текущем столбце'

    @testit.step("Проверка отображения архивного проекта в таблице по проектам")
    @allure.step("Проверка отображения архивного проекта в таблице по проектам")
    def check_archive_project(self, project_name):
        self.element_is_visible(self.locators.FILTER_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.NOT_ACTIV_PROJECT_CHECKBOX).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        self.action_move_to_element(self.element_is_visible(self.locators.check_name_project_color(project_name)))
        name_color = self.element_is_visible(self.locators.check_name_project_color(project_name)).value_of_css_property('color')
        assert name_color == 'rgba(0, 0, 0, 0.4)', "Цвет проекта не серый"

    @testit.step("Проверка отображения архивного проекта в таблице по пользователям")
    @allure.step("Проверка отображения архивного проекта в таблице по пользователям")
    def check_project_color_on_user(self, project_name):
        self.action_move_to_element(self.element_is_visible(self.locators.project_color_on_user(project_name)))
        name_color = self.element_is_visible(
            self.locators.project_color_on_user(project_name)).value_of_css_property('color')
        assert name_color == 'rgba(0, 0, 0, 0.4)', "Цвет проекта не серый"

    @testit.step("Проверка списка выбора периодов")
    @allure.step("Проверка списка выбора периодов")
    def check_chose_period_list(self):
        self.element_is_visible(self.locators.CHOSE_PERIOD_BUTTON).click()
        assert self.get_text_menu_items() == ['Неделя', 'Месяц (по дням)', 'Месяц (по неделям)', 'Год'], \
            "Не корректный список выбора периодов"

    @testit.step("Получение выпадающего списка")
    @allure.step("Получение выпадающего списка")
    def get_text_menu_items(self):
        time.sleep(0.5)
        text = [element.text for element in self.elements_are_present(self.locators.LI_MENU_ITEM)]
        self.action_esc()
        return text

    @testit.step("Проверка наличия кнопок экспорта")
    @allure.step("Проверка наличия кнопок экспорта")
    def check_export_buttons(self):
        assert self.element_is_displayed(self.locators.EXPORT_TO_JSON_BUTTON), "Нет кнопки экспорта в JSON"
        assert self.element_is_displayed(self.locators.EXPORT_TO_EXEL_BUTTON), "Нет кнопки экспорта в EXEL"

    @testit.step("Проверка наличия иконки фильтрации")
    @allure.step("Проверка наличия иконки фильтрации")
    def check_filter_icon(self):
        assert self.element_is_displayed(self.locators.FILTER_BUTTON), "Нет иконки фильтрации"

    @testit.step("Проверка наличия блока переключения периодов")
    @allure.step("Проверка наличия блока переключения периодов")
    def check_next_previous_buttons(self):
        assert self.element_is_displayed(
            self.locators.NEXT_PERIOD_BUTTON), "Нет кнопки переключения на следующий период"
        assert self.element_is_displayed(
            self.locators.PREVIOUS_PERIOD_BUTTON), "Нет кнопки переключения на предыдущий период"
        assert self.element_is_displayed(self.locators.THIS_DAY_BUTTON), "Нет кнопки Сегодня"

    @testit.step("Получение заголовка первого столбца страницы")
    @allure.step("Получение заголовка первого столбца страницы")
    def get_first_column_title(self):
        return self.element_is_visible(self.locators.TAB_TITLE).text

    @testit.step("Проверка заголовков сводной таблицы по пользователям")
    @allure.step("Проверка заголовков сводной таблицы по пользователям")
    def check_tab_column_titles_by_user(self):
        week_days = [element.text for element in self.elements_are_present(self.locators.TAB_HEADER_WEEK_TEXT)]
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.HORIZONTAL_SCROLL), 110, 0)
        time.sleep(1)
        title_sum = [element.text for element in self.elements_are_present(self.locators.COLUMN_TITLES)]
        assert 'Сумма' and 'Сумма От' and 'Сумма Б' and 'Сумма А' and 'Сумма Д' and 'Итог + переработки' in title_sum, \
            "Есть не все заголовки столбцов в таблице"
        assert 'пн' and 'вт' and 'ср' and 'чт' and 'пт' and 'сб' and 'вс' in week_days, \
            "Есть не все дни недели в заголовках столбцов таблицы"

    @testit.step("Проверка заголовков сводной таблицы по проектам")
    @allure.step("Проверка заголовков сводной таблицы по проектам")
    def check_tab_column_titles_by_project(self):
        week_days = [element.text for element in self.elements_are_present(self.locators.TAB_HEADER_WEEK_TEXT)]
        time.sleep(1)
        title_sum = [element.text for element in self.elements_are_present(self.locators.COLUMN_TITLES)]
        assert 'Сумма' in title_sum, "Нет столбца сумма в таблице"
        assert 'пн' and 'вт' and 'ср' and 'чт' and 'пт' and 'сб' and 'вс' in week_days, \
            "Есть не все дни недели в заголовках столбцов таблицы"

    @testit.step("Нажатие кнопки Экспорт в JSON")
    @allure.step("Нажатие кнопки Экспорт в JSON")
    def press_export_to_json_button(self):
        self.element_is_visible(self.locators.EXPORT_TO_JSON_BUTTON).click()

    @testit.step("Получение кликабельности кнопки Сохранить")
    @allure.step("Получение кликабельности кнопки Сохранить")
    def get_clickable_save_button(self):
        return self.element_is_clickable(self.locators.SUBMIT_BUTTON, 3)
