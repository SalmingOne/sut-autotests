import time
from datetime import datetime

import allure
import testit
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import Keys

from locators.project_card_locators import ProjectCardLocators
from pages.base_page import BasePage


class ProjectCardPage(BasePage):
    locators = ProjectCardLocators()

    @testit.step("Переход на вкладку описание проекта")
    @allure.step("Переход на вкладку описание проекта")
    def go_to_description_tab(self):
        self.element_is_visible(self.locators.DESCRIPTION_TAB).click()
        time.sleep(1)

    @testit.step("Получаем имя автора проекта")
    @allure.step("Получаем имя автора проекта")
    def get_project_autor_name(self):
        output_autor_name = self.element_is_visible(self.locators.AUTOR_NAME).text
        return output_autor_name

    @testit.step("Получаем значения полей вкладки описание проекта")
    @allure.step("Получаем значения полей вкладки описание проекта")
    def get_project_description(self):
        output_project_name = self.element_is_visible(self.locators.NAME_FIELD).get_attribute("defaultValue")
        output_project_code = self.element_is_visible(self.locators.CODE_FIELD).get_attribute("defaultValue")
        output_project_status = self.element_is_visible(self.locators.STATUS_FIELD).get_attribute("value")
        output_project_begin_data = self.element_is_visible(self.locators.BEGIN_DATA_FIELD).get_attribute("value")
        output_project_manager = self.element_is_visible(self.locators.MANAGER_LABEL).text
        return output_project_name, output_project_code, output_project_status, output_project_begin_data, output_project_manager

    @testit.step("Получаем роли, ресурсы и ставки команды до редактирования")
    @allure.step("Получаем роли, ресурсы и ставки команды до редактирования")
    def get_all_team_members(self):
        member_list = self.elements_are_present(self.locators.ALL_MEMBERS_TEXT)
        data = []
        for member in member_list:
            data.append(member.text)
        return data

    @testit.step("Получаем роль, ресурс и ставку на первой строке команды в режиме редактирования")
    @allure.step("Получаем роль, ресурс и ставку на первой строке команды в режиме редактирования")
    def get_first_team_member_on_redact(self):
        member_list = self.elements_are_present(self.locators.FIRST_MEMBER_TEXT_ON_REDACT)
        data = []
        for member in member_list:
            data.append(member.get_attribute("value"))
        return data

    @testit.step("Переходим в режим редактирования команды")
    @allure.step("Переходим в режим редактирования команды")
    def go_to_redact_team(self):
        self.element_is_visible(self.locators.REDACT_BUTTON).click()

    @testit.step("Меняем роль, ресурс и ставку на первой строке команды")
    @allure.step("Меняем роль, ресурс и ставку на первой строке команды")
    def change_first_team_member(self):
        member_list = self.elements_are_present(self.locators.FIRST_MEMBER_TEXT_ON_REDACT)
        for member in member_list:
            try:
                member.click()
                self.element_is_visible(self.locators.FIRST_NOT_CHOOSE).click()
            except StaleElementReferenceException:
                pass
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

    @testit.step("Переход на вкладку команды проекта")
    @allure.step("Переход на вкладку команды проекта")
    def go_to_team_tab(self):
        self.element_is_visible(self.locators.TEAM_TAB).click()

    @testit.step("Получаем роли, ресурсы и ставки команды в режиме редактирования")
    @allure.step("Получаем роли, ресурсы и ставки команды в режиме редактирования")
    def get_all_team_member_on_redact(self):
        member_list = self.elements_are_present(self.locators.ALL_MEMBERS_TEXT_ON_REDACT)
        data = []
        for member in member_list:
            data.append(member.get_attribute("value"))
        return data

    @testit.step("Добавляем новый ресурс")
    @allure.step("Добавляем новый ресурс")
    def add_new_member(self):
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        self.elements_are_present(self.locators.FIRST_MEMBER_TEXT_ON_REDACT)[0].click()
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()
        self.elements_are_present(self.locators.FIRST_MEMBER_TEXT_ON_REDACT)[0].click()
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

    @testit.step("Проверка вкладки Описание")
    @allure.step("Проверка вкладки Описание")
    def check_description_tab(self):
        self.check_description_tab_title()
        self.check_description_tab_name_field()
        self.check_description_tab_code_field()
        self.check_description_tab_status_field()
        self.check_description_tab_manager_field()
        self.check_description_tab_start_field()
        self.check_description_tab_end_field()
        self.check_description_tab_description_field()
        self.check_description_tab_file_description_field()
        self.check_description_tab_save_button()
        self.check_description_tab_break_button()
        assert self.get_all_checkboxes_text() == ['Обязательно указание причины списания трудозатрат',
                                                  'Обязательно приложение файлов при переработках и отсутствиях',
                                                  'Самостоятельное добавление',
                                                  'Автоматическое проставление трудозатрат'], ("Не все чекбоксы на "
                                                                                               "вкладке Описание")

    @testit.step("Проверка заголовка вкладки Описание")
    @allure.step("Проверка заголовка вкладки Описание")
    def check_description_tab_title(self):
        assert self.element_is_displayed(self.locators.DESCRIPTION_TAB_TITLE), "Нет заголовка вкладки Описание"

    @testit.step("Проверка наличия поля Имя на вкладке Описание")
    @allure.step("Проверка наличия поля Имя на вкладке Описание")
    def check_description_tab_name_field(self):
        assert self.element_is_displayed(self.locators.NAME_FIELD), "Нет поля Имя"

    @testit.step("Проверка наличия поля Код на вкладке Описание")
    @allure.step("Проверка наличия поля Код на вкладке Описание")
    def check_description_tab_code_field(self):
        assert self.element_is_displayed(self.locators.CODE_FIELD), "Нет поля Код"

    @testit.step("Проверка наличия поля Статус на вкладке Описание")
    @allure.step("Проверка наличия поля Статус на вкладке Описание")
    def check_description_tab_status_field(self):
        assert self.element_is_displayed(self.locators.STATUS_FIELD), "Нет поля Статус"

    @testit.step("Проверка наличия поля Руководитель на вкладке Описание")
    @allure.step("Проверка наличия поля Руководитель на вкладке Описание")
    def check_description_tab_manager_field(self):
        assert self.element_is_displayed(self.locators.MANAGER_FIELD), "Нет поля Руководитель"

    @testit.step("Проверка наличия поля Дата начала на вкладке Описание")
    @allure.step("Проверка наличия поля Дата начала на вкладке Описание")
    def check_description_tab_start_field(self):
        assert self.element_is_displayed(self.locators.BEGIN_DATA_FIELD), "Нет поля Дата начала"

    @testit.step("Проверка наличия поля Дата окончания на вкладке Описание")
    @allure.step("Проверка наличия поля Дата окончания на вкладке Описание")
    def check_description_tab_end_field(self):
        assert self.element_is_displayed(self.locators.END_DATA_FIELD), "Нет поля Дата окончания"

    @testit.step("Проверка наличия поля Описание на вкладке Описание")
    @allure.step("Проверка наличия поля Описание на вкладке Описание")
    def check_description_tab_description_field(self):
        assert self.element_is_displayed(self.locators.DESCRIPTION_FIELD), "Нет поля Описание"

    @testit.step("Проверка наличия поля Описание файла на вкладке Описание")
    @allure.step("Проверка наличия поля Описание файла на вкладке Описание")
    def check_description_tab_file_description_field(self):
        assert self.element_is_displayed(self.locators.FILE_DESCRIPTION_FIELD), "Нет поля Описание файла"

    @testit.step("Проверка наличия кнопки Сохранить на вкладке Описание")
    @allure.step("Проверка наличия кнопки Сохранить на вкладке Описание")
    def check_description_tab_save_button(self):
        assert self.element_is_displayed(self.locators.SAVE_BUTTON), "Нет кнопки Сохранить"

    @testit.step("Проверка наличия кнопки Отмена на вкладке Описание")
    @allure.step("Проверка наличия кнопки Отмена на вкладке Описание")
    def check_description_tab_break_button(self):
        assert self.element_is_displayed(self.locators.BREAK_BUTTON), "Нет кнопки Отмена"

    @testit.step("Получение текста всех чекбоксов")
    @allure.step("Получение текста всех чекбоксов")
    def get_all_checkboxes_text(self):
        all_checkboxes = self.elements_are_visible(self.locators.CHECKBOXES_TEXT)
        checkboxes_text = []
        for checkbox in all_checkboxes:
            checkboxes_text.append(checkbox.text)
        return checkboxes_text

    @testit.step("Переход на вкладку Проектная иерархия")
    @allure.step("Переход на вкладку Проектная иерархия")
    def go_to_project_hierarchy_tab(self):
        self.element_is_visible(self.locators.PROJECT_HIERARCHY_TAB).click()

    @testit.step("Проверка вкладки Проектная иерархия")
    @allure.step("Проверка вкладки ППроектная иерархия")
    def check_project_hierarchy_tab(self):
        time.sleep(1)
        self.check_project_hierarchy_tab_title()
        self.check_project_hierarchy_tab_switch()
        self.check_project_hierarchy_tab_scope_field()
        self.check_project_hierarchy_tab_centre_icon()
        self.check_project_hierarchy_tab_project_node()
        self.check_project_hierarchy_tab_source_icon()

    @testit.step("Проверка заголовка вкладки Проектная иерархия")
    @allure.step("Проверка заголовка вкладки Проектная иерархия")
    def check_project_hierarchy_tab_title(self):
        assert self.element_is_displayed(self.locators.PROJECT_HIERARCHY_TAB_TITLE), "Нет заголовка вкладки Проектная иерархия"

    @testit.step("Проверка Свитча включения/выключения легенды вкладки Проектная иерархия")
    @allure.step("Проверка Свитча включения/выключения легенды вкладки Проектная иерархия")
    def check_project_hierarchy_tab_switch(self):
        assert self.element_is_displayed(self.locators.LEGEND_SWITCH), "Нет Свитча включения/выключения легенды"

    @testit.step("Проверка поля выбора масштаба вкладки Проектная иерархия")
    @allure.step("Проверка поля выбора масштаба вкладки Проектная иерархия")
    def check_project_hierarchy_tab_scope_field(self):
        assert self.element_is_displayed(self.locators.SCOPE_FIELD), "Нет поля выбора масштаба"

    @testit.step("Проверка наличия кнопки возврата к центу вкладки Проектная иерархия")
    @allure.step("Проверка наличия кнопки возврата к центу вкладки Проектная иерархия")
    def check_project_hierarchy_tab_centre_icon(self):
        assert self.element_is_displayed(self.locators.CENTER_FOCUS_ICON), "Нет кнопки возврата к центу"

    @testit.step("Проверка наличия плитки проект вкладки Проектная иерархия")
    @allure.step("Проверка наличия плитки проект вкладки Проектная иерархия")
    def check_project_hierarchy_tab_project_node(self):
        assert self.element_is_displayed(self.locators.PROJECT_NODE_ICON), "Нет плитки проект"

    @testit.step("Проверка наличия плитки ресурс вкладки Проектная иерархия")
    @allure.step("Проверка наличия плитки ресурс вкладки Проектная иерархия")
    def check_project_hierarchy_tab_source_icon(self):
        assert self.element_is_displayed(self.locators.SOURCE_ICON), "Нет плитки ресурс"

    @testit.step("Проверка вкладки Команда")
    @allure.step("Проверка вкладки Команда")
    def check_team_tab(self):
        time.sleep(1)
        self.check_team_tab_redact_button()
        self.check_team_tab_to_excel_button()
        self.check_team_tab_filter_button()
        self.check_team_tab_number_of_recourses()
        self.check_team_tab_next_previous_buttons()
        self.check_team_tab_titles()

    @testit.step("Проверка наличия кнопки Редактировать вкладки Команда")
    @allure.step("Проверка наличия кнопки Редактировать вкладки Команда")
    def check_team_tab_redact_button(self):
        assert self.element_is_displayed(self.locators.REDACT_BUTTON), "Нет кнопки Редактировать"

    @testit.step("Проверка наличия кнопки экспорта в excel вкладки Команда")
    @allure.step("Проверка наличия кнопки экспорта в excel вкладки Команда")
    def check_team_tab_to_excel_button(self):
        assert self.element_is_displayed(self.locators.TO_EXCEL_BUTTON), "Нет кнопки экспорта в excel"

    @testit.step("Проверка наличия кнопки фильтрации вкладки Команда")
    @allure.step("Проверка наличия кнопки фильтрации вкладки Команда")
    def check_team_tab_filter_button(self):
        assert self.element_is_displayed(self.locators.TEAM_TAB_FILTER_BUTTON), "Нет кнопки фильтрации"

    @testit.step("Проверка наличия поля количества ресурсов вкладки Команда")
    @allure.step("Проверка наличия поля количества ресурсов вкладки Команда")
    def check_team_tab_number_of_recourses(self):
        assert self.element_is_displayed(self.locators.NUMBER_OF_RECOURSES), "Нет поля количества ресурсов"

    @testit.step("Проверка наличия блока переключения периодов")
    @allure.step("Проверка наличия блока переключения периодов")
    def check_team_tab_next_previous_buttons(self):
        assert self.element_is_displayed(self.locators.NEXT_PERIOD_BUTTON), "Нет кнопки переключения на следующий период"
        assert self.element_is_displayed(self.locators.PREVIOUS_PERIOD_BUTTON), "Нет кнопки переключения на предыдущий период"
        assert self.element_is_displayed(self.locators.THIS_DAY_BUTTON), "Нет кнопки Сегодня"

    @testit.step("Проверка заголовков вкладки Команда")
    @allure.step("Проверка заголовков вкладки Команда")
    def check_team_tab_titles(self):
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        all_titles = self.elements_are_visible(self.locators.TEAM_TAB_TITLES)
        titles_text = []
        for titles in all_titles:
            titles_text.append(titles.text)
        self.element_is_visible(self.locators.ABORT_BUTTON).click()
        assert titles_text == ['Ресурс', 'Ставка привлечения', 'Дата назначения пользователя на слот',
                               'Дата снятия пользователя со слота', 'Проектная роль', 'Действия'], "Не корректные заголовки таблицы"

    @testit.step("Переход на вкладку Ресурсный план")
    @allure.step("Переход на вкладку Ресурсный план")
    def go_to_resource_plan_tab(self):
        self.element_is_visible(self.locators.RESOURCE_PLAN_TAB).click()

    @testit.step("Проверка вкладки Ресурсный план")
    @allure.step("Проверка вкладки Ресурсный план")
    def check_resource_plan_tab(self):
        self.check_default_period()
        self.check_team_tab_next_previous_buttons()
        self.check_chose_period_list()
        self.check_resource_plan_tab_radiogroup()
        self.check_default_radiogroup()
        self.check_resource_plan_tab_save_and_break_buttons()
        self.check_resource_plan_tab_add_percent_button()
        self.check_resource_plan_tab_header_tooltip()

    @testit.step("Проверка периода выбранного по умолчанию")
    @allure.step("Проверка периода выбранного по умолчанию")
    def check_default_period(self):
        try:
            assert self.element_is_visible(self.locators.CHOSE_PERIOD_BUTTON).text == 'Квартал', \
                "По умолчанию выбран период не Квартал"
        except TimeoutException:
            self.go_to_resource_plan_tab()
            assert self.element_is_visible(self.locators.CHOSE_PERIOD_BUTTON).text == 'Квартал', \
                "По умолчанию выбран период не Квартал"

    @testit.step("Проверка списка выбора периодов")
    @allure.step("Проверка списка выбора периодов")
    def check_chose_period_list(self):
        self.element_is_visible(self.locators.CHOSE_PERIOD_BUTTON).click()
        assert self.get_text_menu_items() == ['Квартал', 'Месяц (по дням)', 'Год'], "Не корректный список выбора периодов"

    @testit.step("Получение выпадающего списка")
    @allure.step("Получение выпадающего списка")
    def get_text_menu_items(self):
        all_items = self.elements_are_visible(self.locators.LI_MENU_ITEM)
        text = []
        for item in all_items:
            text.append(item.text)
        self.action_esc()
        return text

    @testit.step("Проверка наличия блока переключения режима отображения трудозатрат")
    @allure.step("Проверка наличия блока переключения режима отображения трудозатрат")
    def check_resource_plan_tab_radiogroup(self):
        assert self.element_is_displayed(self.locators.RESOURCE_PLAN_RADIOGROUP), ("Нет блока переключения режима"
                                                                                   " отображения трудозатрат")

    @testit.step("Проверка наличия кнопок сохранения и отмены")
    @allure.step("Проверка наличия кнопок сохранения и отмены")
    def check_resource_plan_tab_save_and_break_buttons(self):
        assert self.element_is_displayed(self.locators.SAVE_BUTTON), "Нет кнопки Сохранить"
        assert self.element_is_displayed(self.locators.BREAK_BUTTON), "Нет кнопки Отменить"

    @testit.step("Проверка значения по умолчанию блока переключения режима отображения трудозатрат")
    @allure.step("Проверка значения по умолчанию блока переключения режима отображения трудозатрат")
    def check_default_radiogroup(self):
        assert self.element_is_visible(self.locators.CHECKED_RADIOGROUP).text == 'Часы', ("По умолчанию не корректный"
                                                                                          " режим отображения"
                                                                                          " трудозатрат")

    @testit.step("Проверка наличия кнопки с функционалом добавления процента занятости")
    @allure.step("Проверка наличия кнопки с функционалом добавления процента занятости")
    def check_resource_plan_tab_add_percent_button(self):
        self.action_move_to_element(self.element_is_present(self.locators.ADD_PERCENT_BUTTON))
        assert self.element_is_displayed(self.locators.ADD_PERCENT_BUTTON), ("Отсутствует кнопка с функционалом "
                                                                             "добавления процента занятости")

    @testit.step("Проверка наличия тултипа с указанием номера недели")
    @allure.step("Проверка наличия тултипа с указанием номера недели")
    def check_resource_plan_tab_header_tooltip(self):
        self.action_move_to_element(self.elements_are_visible(self.locators.RESOURCE_PLAN_TAB_HEADER)[1])
        assert 'Неделя №' in self.element_is_visible(
            self.locators.TOOLTIP).text, "В тултипе не отображается номер недели"

    @testit.step("Переход на вкладку Ход выполнения")
    @allure.step("Переход на вкладку Ход выполнения")
    def go_to_progress_tab(self):
        self.element_is_visible(self.locators.PROGRESS_TAB).click()

    @testit.step("Проверка вкладки Ход выполнения")
    @allure.step("Проверка вкладки Ход выполнения")
    def check_progress_tab(self):
        time.sleep(2)
        self.check_default_period_in_progress_tab()
        self.check_chose_period_list_in_progress_tab()
        self.check_team_tab_next_previous_buttons()
        self.check_progress_tab_save_and_break_buttons()
        self.check_progress_tab_headers_text()
        self.check_progress_tab_done_and_clear_icon()
        self.check_progress_tab_action_approve()

    @testit.step("Проверка списка выбора периодов на вкладке Ход выполнения")
    @allure.step("Проверка списка выбора периодов на вкладке Ход выполнения")
    def check_chose_period_list_in_progress_tab(self):
        self.element_is_visible(self.locators.CHOSE_PERIOD_BUTTON).click()
        assert self.get_text_menu_items() == ['Неделя', 'Месяц (по дням)', 'Месяц (по неделям)'], ("Список выбора"
                                                                                                   " периодов не полный")

    @testit.step("Проверка периода по умолчанию на вкладке Ход выполнения")
    @allure.step("Проверка периода по умолчанию на вкладке Ход выполнения")
    def check_default_period_in_progress_tab(self):
        assert self.element_is_visible(self.locators.CHOSE_PERIOD_BUTTON).text == 'Неделя', \
            "По умолчанию выбран период не Неделя"

    @testit.step("Проверка наличия кнопок сохранения и отмены")
    @allure.step("Проверка наличия кнопок сохранения и отмены")
    def check_progress_tab_save_and_break_buttons(self):
        assert self.element_is_displayed(self.locators.SAVE_BUTTON), "Нет кнопки Сохранить"
        assert self.element_is_displayed(self.locators.ABORT_BUTTON), "Нет кнопки Отменить"

    @testit.step("Проверка заголовков таблиц на вкладке Ход выполнения")
    @allure.step("Проверка заголовков таблиц на вкладке Ход выполнения")
    def check_progress_tab_headers_text(self):
        all_items = self.elements_are_present(self.locators.PROGRESS_TAB_HEADER)
        text = []
        for item in all_items:
            text.append(item.text)
        assert sorted(text) == ['', 'Дата', 'Действия', 'Действия', 'Кол-во часов', 'Пользователь', 'Пользователь',
                                'Причина', 'Статус согласования', 'Файл'], ("В таблицах на вкладке Ход выполнения есть"
                                                                            " не все заголовки")

    @testit.step("Проверка наличия иконок согласовать и не согласовать")
    @allure.step("Проверка наличия иконок согласовать и не согласовать")
    def check_progress_tab_done_and_clear_icon(self):
        assert self.element_is_displayed(self.locators.DONE_ICON), "Нет иконки не согласования трудозатрат"
        assert self.element_is_displayed(self.locators.CLEAR_ICON), "Нет иконки согласования трудозатрат"

    @testit.step("Проверка наличия пунктов Подтвердить и Отклонить")
    @allure.step("Проверка наличия пунктов Подтвердить и Отклонить")
    def check_progress_tab_action_approve(self):
        self.elements_are_visible(self.locators.KEBAB_MENU)[0].click()
        menu_item = self.elements_are_visible(self.locators.KEBAB_MENU_ITEM)
        items_text = []
        for element in menu_item:
            items_text.append(element.text)
        assert items_text == ['Подтвердить', 'Отклонить'], "В кебаб меню не все пункты"

    @testit.step("Выбор периода отображения")
    @allure.step("Выбор периода отображения")
    def chose_period(self, period_name):
        self.element_is_visible(self.locators.CHOSE_PERIOD_BUTTON).click()
        self.element_is_visible(self.locators.li_by_text(period_name)).click()

    @testit.step("Получение верхней строки дат заголовков таблицы")
    @allure.step("Получение верхней строки дат заголовков таблицы")
    def get_hire_string_in_header(self):
        time.sleep(1)
        elements = self.elements_are_visible(self.locators.HIRE_HEADER)
        titles_text = []
        for element in elements:
            titles_text.append(element.text)
        return titles_text

    @testit.step("Проверка заголовка таблицы ресурсного плана по дням")
    @allure.step("Проверка заголовка таблицы ресурсного плана по дням")
    def check_resource_plan_tab_title_format_day(self):
        assert self.element_is_visible(self.locators.PROGRESS_TAB_HEADER).text == 'Ресурсы', "Нет столбца ресурсы"
        assert '1' and '15' and '28' in self.get_hire_string_in_header(), "Не указаны даты"
        assert 'пн' and 'вт' and 'ср' and 'чт' and 'пт' and 'сб' and 'вс' in self.get_low_string_in_header(), \
            "Не указаны дни недели"

    @testit.step("Получение нижней строки дат заголовков таблицы")
    @allure.step("Получение нижней строки дат заголовков таблицы")
    def get_low_string_in_header(self):
        time.sleep(1)
        elements = self.elements_are_visible(self.locators.LOW_HEADER)
        titles_text = []
        for element in elements:
            titles_text.append(element.text)
        return titles_text

    @testit.step("Проверка заголовка таблицы ресурсного плана по месяцам")
    @allure.step("Проверка заголовка таблицы ресурсного плана по месяцам")
    def check_resource_plan_tab_title_format_month(self):
        time.sleep(2)
        assert self.element_is_visible(self.locators.PROGRESS_TAB_HEADER).text == 'Ресурсы', "Нет столбца ресурсы"
        assert ('Январь' and 'Февраль' and 'Март' and 'Апрель' and 'Май' and 'Июнь' and 'Июль' and 'Август' and
                'Сентябрь' and 'Октябрь' and 'Ноябрь' and 'Декабрь' in self.get_hire_string_in_header()), \
            "Нет названий месяцев"
        assert datetime.now().strftime("%Y") in self.get_low_string_in_header(), "Не указан год"

    @testit.step("Нажатие кнопки добавить")
    @allure.step("Нажатие кнопки добавить")
    def press_add_button(self):
        time.sleep(1)
        self.element_is_visible(self.locators.ADD_BUTTON).click()

    @testit.step("Получение списка элементов выпадающего меню")
    @allure.step("Получение списка элементов выпадающего меню")
    def get_all_names_in_li_menu(self, element_number):
        time.sleep(1)
        self.elements_are_present(self.locators.FIRST_MEMBER_TEXT_ON_REDACT)[element_number].click()
        all_roles = self.elements_are_visible(self.locators.LI_MENU_ITEM)
        names = []
        for role in all_roles:
            names.append(role.get_attribute('aria-label'))
        return names

    @testit.step("Получение списка пользователей уже назначенных на проект")
    @allure.step("Получение списка пользователей уже назначенных на проект")
    def get_all_user_before_redact_team_tab(self):
        return self.element_is_visible(self.locators.USERS_TEXT).text

    @testit.step("Заполнение поля ресурс")
    @allure.step("Заполнение поля ресурс")
    def field_resource_field(self, name):
        self.elements_are_present(self.locators.FIRST_MEMBER_TEXT_ON_REDACT)[1].send_keys(name)
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()

    @testit.step("Нажатие кнопки удалить слот")
    @allure.step("Нажатие кнопки удалить слот")
    def press_delete_icon(self):
        self.element_is_visible(self.locators.DELETE_ICON).click()

    @testit.step("Заполнение поля роль")
    @allure.step("Заполнение поля роль")
    def field_roles_field(self, name):
        self.elements_are_present(self.locators.FIRST_MEMBER_TEXT_ON_REDACT)[0].send_keys(name)
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()

    @testit.step("Заполнение полей добавления ресурса таб команда")
    @allure.step("Заполнение полей добавления ресурса таб команда")
    def field_add_new_member_string(self):
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        self.elements_are_present(self.locators.FIRST_MEMBER_TEXT_ON_REDACT)[0].click()
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()
        self.elements_are_present(self.locators.FIRST_MEMBER_TEXT_ON_REDACT)[0].click()
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()

    @testit.step("Нажатие кнопки отменить")
    @allure.step("Нажатие кнопки отменить")
    def press_abort_button(self):
        self.element_is_visible(self.locators.ABORT_BUTTON).click()

    @testit.step("Проверка модального окна отмены редактирования")
    @allure.step("Проверка модального окна отмены редактирования")
    def check_abort_add_resource_window(self):
        assert (self.element_is_visible(self.locators.ALERT_DIALOG_DESCRIPTION).text ==
                'Внесенные изменения не сохранятся. Закрыть режим редактирования?'), "Нет сообщения об отмене изменений"
        assert self.element_is_displayed(self.locators.MODAL_ABORT_BUTTON), "В модальном окне нет кнопки Отменить"

    @testit.step("Нажатие кнопки подтвердить модального окна отмены редактирования")
    @allure.step("Нажатие кнопки подтвердить модального окна отмены редактирования")
    def press_modal_submit_button(self):
        self.element_is_visible(self.locators.MODAL_SUBMIT_BUTTON).click()

    @testit.step("Получение даты начала проекта")
    @allure.step("Получение даты начала проекта")
    def get_project_start_date(self):
        return self.element_is_visible(self.locators.BEGIN_DATA_FIELD).get_attribute("value")

    @testit.step("Изменение даты начала проекта")
    @allure.step("Изменение даты начала проекта")
    def change_start_date(self, date):
        self.element_is_visible(self.locators.BEGIN_DATA_FIELD).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.BEGIN_DATA_FIELD).send_keys(date)

    @testit.step("Нажатие кнопки Сохранить")
    @allure.step("Нажатие кнопки Сохранить")
    def press_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Получение сообщения системы")
    @allure.step("Получение сообщения системы")
    def get_alert_message(self):
        return self.element_is_visible(self.locators.ALERT_MESSAGE).text

    @testit.step("Очистка поля код проекта")
    @allure.step("Очистка поля код проекта")
    def clear_code_field(self):
        self.element_is_visible(self.locators.CODE_FIELD).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.CODE_FIELD).send_keys(Keys.BACKSPACE)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Получение текста сообщения об ошибке")
    @allure.step("Получение текста сообщения об ошибке")
    def get_mui_error(self):
        return self.element_is_visible(self.locators.MUI_ERROR).text

    @testit.step("Получение цвета поля код проекта")
    @allure.step("Получение цвета поля код проекта")
    def get_code_field_color(self):
        return self.element_is_visible(self.locators.CODE_FIELD_COLOR).value_of_css_property('border-color')

    @testit.step("Изменение имени проекта")
    @allure.step("Изменение имени проекта")
    def change_project_name(self, name):
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Получение цвета поля имя проекта")
    @allure.step("Получение цвета поля имя проекта")
    def get_name_field_color(self):
        return self.element_is_visible(self.locators.NAME_FIELD_COLOR).value_of_css_property('border-color')
