import time
from datetime import datetime

import allure
import testit
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import Keys
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')
from utils.concat_testit_allure_step import allure_testit_step

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
        time.sleep(1)
        output_project_name = self.element_is_visible(self.locators.NAME_FIELD).get_attribute("defaultValue")
        output_project_code = self.element_is_visible(self.locators.CODE_FIELD).get_attribute("defaultValue")
        output_project_status = self.element_is_visible(self.locators.STATUS_FIELD).get_attribute("value")
        output_project_begin_data = self.element_is_visible(self.locators.BEGIN_DATA_FIELD).get_attribute("value")
        output_project_manager = self.element_is_visible(self.locators.MANAGER_LABEL).text
        return output_project_name, output_project_code, output_project_status, output_project_begin_data, output_project_manager

    @allure_testit_step("Получаем значения выпадающего списка поля статус вкладки описание проекта")
    def get_available_status_on_description_tab(self):
        self.element_is_visible(self.locators.STATUS_FIELD).click()
        return self.get_text_menu_items()

    @allure_testit_step("Изменяем статус проекта")
    def change_status_project(self, status):
        self.element_is_visible(self.locators.STATUS_FIELD).click()
        self.element_is_visible(self.locators.li_by_text(status)).click()
        self.press_submit_button()

    @allure_testit_step("Получаем значение поля приоритет вкладки описание проекта")
    def get_priority_on_description_tab(self):
        return self.element_is_visible(self.locators.PRIORITY_FIELD).text

    @allure_testit_step("Получаем все приоритеты вкладки описание проекта")
    def get_all_priority_on_description_tab(self):
        self.element_is_visible(self.locators.PRIORITY_FIELD).click()
        all_priority = self.elements_are_visible(self.locators.LI_MENU_ITEM)
        all_colors = self.elements_are_visible(self.locators.COLOR_MENU_ITEM)

        if len(all_priority) != len(all_colors):
            raise ValueError('Количество приоритетов и цветов не совпадает!')
        data = {}
        for priority, color in zip(all_priority, all_colors):
            data[priority.text] = color.value_of_css_property('color')
        self.action_esc()
        return data

    @allure_testit_step("Выбираем приоритет вкладки описание проекта")
    def select_priority(self):
        self.element_is_visible(self.locators.PRIORITY_FIELD).click()
        self.element_is_visible(self.locators.FIRST_NOT_CHOOSE).click()

    @allure_testit_step("Проверка поля приоритет вкладки описание проекта")
    def check_description_tab_priority_field(self):
        assert self.get_all_priority_on_description_tab() == {'Низкий (1)': 'rgba(76, 175, 80, 1)',
                                                              'Низкий (2)': 'rgba(76, 175, 80, 1)',
                                                              'Низкий (3)': 'rgba(76, 175, 80, 1)',
                                                              'Средний (4)': 'rgba(255, 193, 7, 1)',
                                                              'Средний (5)': 'rgba(255, 193, 7, 1)',
                                                              'Средний (6)': 'rgba(255, 193, 7, 1)',
                                                              'Средний (7)': 'rgba(255, 193, 7, 1)',
                                                              'Высокий (8)': 'rgba(255, 87, 34, 1)',
                                                              'Высокий (9)': 'rgba(255, 87, 34, 1)',
                                                              'Высокий (10)': 'rgba(255, 87, 34, 1)'},\
            'В выпадающем списке не все значения приоритетов'

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
        time.sleep(1)
        self.elements_are_visible(self.locators.APPOINTMENT_DATE_DATEPICKER)[1].click()
        time.sleep(1)
        self.element_is_visible(self.locators.THIS_DAY_PICKER).click()
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
        assert titles_text == ['Проектная роль', 'Ресурс', 'Ставка привлечения', 'Дата назначения пользователя на слот', 'Дата снятия пользователя со слота', 'Действия'], "Не корректные заголовки таблицы"

    @allure_testit_step("Переход на вкладку Ресурсный план")
    def go_to_resource_plan_tab(self):
        self.element_is_visible(self.locators.RESOURCE_PLAN_TAB, 15).click()
        self.element_is_present(self.locators.ADD_EMPLOYMENT_BUTTON, 25)

    @allure_testit_step("Переход на вкладку Ресурсный план без ожидания")
    def go_to_resource_plan_tab_not_wait(self):
        self.element_is_visible(self.locators.RESOURCE_PLAN_TAB, 15).click()

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

    @testit.step("Проверка вкладки Ресурсный план без ресурсов")
    @allure.step("Проверка вкладки Ресурсный план без ресурсов")
    def check_resource_plan_tab_without_resources(self):
        time.sleep(1)
        self.check_message_without_resources()
        self.check_link_to_add_new_resources()

    @testit.step("Проверка сообщения в табе Ресурсный план без ресурсов")
    @allure.step("Проверка сообщения в табе Ресурсный план без ресурсов")
    def check_message_without_resources(self):
        all_messages = self.elements_are_visible(self.locators.TEXT_NO_RESOURCES, 25)
        data = []
        for message in all_messages:
            data.append(message.text)
        assert data == ['В проекте нет добавленных ресурсов', 'Перейдите по ссылке, чтобы добавить новые ресурсы в проект'], \
        "Отсутствует/не соответствует текст сообщения в табе Ресурсный план без ресурсов"

    @testit.step("Проверка ссылки на добавление новых ресурсов в проект")
    @allure.step("Проверка ссылки на добавление новых ресурсов в проект")
    def check_link_to_add_new_resources(self):
        self.element_is_visible(self.locators.LINK_NO_RESOURCES).click()
        assert self.element_is_visible(self.locators.TEAM_TAB, 15).get_attribute('aria-selected') == 'true', \
            "Ссылка не ведет на вкладку Команда"

    @allure_testit_step("Переключение радиобаттона на значение 'Проценты'")
    def change_radiobutton_percent(self):
        self.element_is_visible(self.locators.CHANGE_RADIOGROUP_PERCENT, 15).click()

    @allure_testit_step("Переключение радиобаттона на значение 'Часы'")
    def change_radiobutton_hour(self):
        self.element_is_visible(self.locators.CHANGE_RADIOGROUP_HOUR, 15).click()


    @testit.step("Нажатие на кнопку добавления процента занятости")
    @allure.step("Нажатие на кнопку добавления процента занятости")
    def press_add_employment_button(self):
        self.element_is_present(self.locators.ADD_EMPLOYMENT_BUTTON, 25).click()   

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
        self.action_move_to_element(self.element_is_present(self.locators.ADD_EMPLOYMENT_BUTTON))
        assert self.element_is_displayed(self.locators.ADD_EMPLOYMENT_BUTTON), ("Отсутствует кнопка с функционалом "
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
        self.element_is_visible(self.locators.LABOR_COLOR, 15)

    @testit.step("Проверка вкладки Ход выполнения")
    @allure.step("Проверка вкладки Ход выполнения")
    def check_progress_tab(self):
        time.sleep(2)
        self.check_default_period_in_progress_tab()
        self.check_chose_period_list_in_progress_tab()
        self.check_team_tab_next_previous_buttons()
        self.check_progress_tab_save_and_break_buttons()
        time.sleep(1)
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
        assert self.element_is_visible(self.locators.ALERT_DIALOG_TITLE).text in ['Подтвердите действие', 'Подтверждение действия'], \
            "Нет заголовка модального окна"
        assert (self.element_is_visible(self.locators.ALERT_DIALOG_DESCRIPTION).text ==
                'Внесенные изменения не сохранятся. Закрыть режим редактирования?'), "Нет сообщения об отмене изменений"
        assert self.element_is_displayed(self.locators.MODAL_SUBMIT_BUTTON), "В модальном окне нет кнопки Подтвердить"
        assert self.element_is_displayed(self.locators.MODAL_ABORT_BUTTON), "В модальном окне нет кнопки Отменить"

    @testit.step("Нажатие кнопки подтвердить модального окна отмены редактирования")
    @allure.step("Нажатие кнопки подтвердить модального окна отмены редактирования")
    def press_modal_submit_button(self):
        self.element_is_visible(self.locators.MODAL_SUBMIT_BUTTON).click()

    @testit.step("Нажатие кнопки отменить модального окна отмены редактирования")
    @allure.step("Нажатие кнопки отменить модального окна отмены редактирования")
    def press_modal_abort_button(self):
        self.element_is_visible(self.locators.MODAL_ABORT_BUTTON).click()

    @testit.step("Получение даты начала проекта")
    @allure.step("Получение даты начала проекта")
    def get_project_start_date(self):
        return self.element_is_visible(self.locators.BEGIN_DATA_FIELD).get_attribute("value")
    
    @allure_testit_step("Проверка даты начала проекта в заголовке")
    def check_project_start_date_in_title(self, start_date):
        assert self.element_is_visible(self.locators.text_on_page(start_date)), \
            f"В заголовке не новая дата начала проекта"
    
    @testit.step("Получение даты окончания проекта")
    @allure.step("Получение даты окончания проекта")
    def get_project_end_date(self):
        return self.element_is_visible(self.locators.END_DATA_FIELD).get_attribute("value")

    @allure_testit_step("Проверка даты окончания проекта в заголовке")
    def check_project_end_date_in_title(self, end_date):
        assert self.element_is_visible(self.locators.text_on_page(end_date)), \
            f"В заголовке не новая дата окончания проекта"

    @testit.step("Изменение даты начала проекта")
    @allure.step("Изменение даты начала проекта")
    def change_start_date(self, date):
        self.action_select_all_text(self.element_is_visible(self.locators.BEGIN_DATA_FIELD))
        self.element_is_visible(self.locators.BEGIN_DATA_FIELD).send_keys(date)

    @testit.step("Изменение даты окончания проекта")
    @allure.step("Изменение даты окончания проекта")
    def change_end_date(self, date):
        self.action_select_all_text(self.element_is_visible(self.locators.END_DATA_FIELD))
        self.element_is_visible(self.locators.END_DATA_FIELD).send_keys(date)

    @testit.step("Нажатие кнопки Сохранить")
    @allure.step("Нажатие кнопки Сохранить")
    def press_submit_button(self):
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

    @testit.step("Нажатие кнопки Отмена")
    @allure.step("Нажатие кнопки Отмена")
    def press_break_button(self):
        self.element_is_visible(self.locators.BREAK_BUTTON).click()

    @testit.step("Получение сообщения системы")
    @allure.step("Получение сообщения системы")
    def get_alert_message(self):
        return self.element_is_visible(self.locators.ALERT_MESSAGE).text

    @testit.step("Очистка поля код проекта")
    @allure.step("Очистка поля код проекта")
    def clear_code_field(self):
        self.action_select_all_text(self.element_is_visible(self.locators.CODE_FIELD))
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
        self.action_select_all_text(self.element_is_visible(self.locators.NAME_FIELD))
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Получение цвета поля имя проекта")
    @allure.step("Получение цвета поля имя проекта")
    def get_name_field_color(self):
        return self.element_is_visible(self.locators.NAME_FIELD_COLOR).value_of_css_property('border-color')

    @testit.step("Изменение кода проекта")
    @allure.step("Изменение кода проекта")
    def change_project_code(self, code):
        self.action_select_all_text(self.element_is_visible(self.locators.CODE_FIELD))
        self.element_is_visible(self.locators.CODE_FIELD).send_keys(code)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Очистка поля имя проекта")
    @allure.step("Очистка поля имя проекта")
    def clear_name_field(self):
        self.action_select_all_text(self.element_is_visible(self.locators.NAME_FIELD))
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.BACKSPACE)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Очистка поля дата начала проекта")
    @allure.step("Очистка поля дата начала проекта")
    def clear_start_project_date_field(self):
        self.action_select_all_text(self.element_is_visible(self.locators.BEGIN_DATA_FIELD))
        self.element_is_visible(self.locators.BEGIN_DATA_FIELD).send_keys(Keys.BACKSPACE)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Получение цвета поля дата начала проекта")
    @allure.step("Получение цвета поля дата начала проекта")
    def get_start_project_date_field_color(self):
        return self.element_is_visible(self.locators.BEGIN_DATA_FIELD_COLOR).value_of_css_property('border-color')

    @testit.step("Удаление чипсы менеджера проекта")
    @allure.step("Удаление чипсы менеджера проекта")
    def remove_manager_chips(self):
        self.element_is_visible(self.locators.CANSEL_ICON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка удаления чипсы менеджера проекта")
    @allure.step("Проверка удаления чипсы менеджера проекта")
    def check_manager_label(self):
        assert not self.element_is_displayed(self.locators.MANAGER_LABEL, 1), "Чипса менеджера проекта не удалилась"

    @testit.step("Проверка наличия текста на странице")
    @allure.step("Проверка наличия текста на странице")
    def check_text_on_page(self, text):
        assert self.element_is_displayed(self.locators.text_on_page(text)), f"На странице нет текста {text}"

    @testit.step("Проверка отсутствия вкладки ресурсный план на странице")
    @allure.step("Проверка отсутствия вкладки ресурсный план на странице")
    def check_resource_plan_tab_on_page(self):
        assert not self.element_is_displayed(self.locators.RESOURCE_PLAN_TAB, 1)

    @testit.step("Добавление менеджера на проект")
    @allure.step("Добавление менеджера на проект")
    def add_manager(self, number_li_element):
        self.element_is_visible(self.locators.MANAGER_FIELD).click()
        time.sleep(0.5)
        manager = self.elements_are_visible(self.locators.LI_MENU_ITEM)[number_li_element].text
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[number_li_element].click()
        return manager

    @testit.step("Получение всех менеджеров проекта")
    @allure.step("Получение всех менеджеров проекта")
    def get_all_manger(self):
        all_manager = self.elements_are_visible(self.locators.MANAGER_LABEL)
        manager_list = []
        for manager in all_manager:
            manager_list.append(manager.text)
        return manager_list

    @testit.step("Получение сообщений системы")
    @allure.step("Получение сообщений системы")
    def get_all_alert_message(self):
        all_alerts = self.elements_are_visible(self.locators.ALERT_MESSAGE)
        data = []
        for alert in all_alerts:
            data.append(alert.text)
        return data

    @testit.step("Проверка невозможности снять себя с менеджера проекта")
    @allure.step("Проверка невозможности снять себя с менеджера проекта")
    def check_manager_can_not_delete_himself(self):
        self.element_is_visible(self.locators.CANSEL_ICON).click()
        time.sleep(2)
        assert ('Невозможно снять себя с должности Руководителя, обратитесь к администратору' in
                self.get_all_alert_message()), "Не появилось сообщение о невозможности снятия себя с проекта"

    @testit.step("Открытие фильтра")
    @allure.step("Открытие фильтра")
    def open_filter(self):
        self.element_is_visible(self.locators.TEAM_TAB_FILTER_BUTTON).click()

    @testit.step("Нажатие кнопки Выбрать все")
    @allure.step("Нажатие кнопки Выбрать все")
    def press_choose_all_checkbox(self):
        self.element_is_visible(self.locators.text_on_page('Выбрать всё')).click()

    @testit.step("Проверка отсутствия выбранных чекбоксов")
    @allure.step("Проверка отсутствия выбранных чекбоксов")
    def check_no_checked_checkboxes(self):
        assert not self.element_is_displayed(self.locators.CHECKED_CHECKBOXES, 1), "Есть выбранные чекбоксы"

    @testit.step("Нажатие кнопки Применить")
    @allure.step("Нажатие кнопки Применить")
    def press_apply_button(self):
        time.sleep(0.5)
        self.element_is_visible(self.locators.APPLY_BUTTON).click()

    @testit.step("Нажатие чекбокса Согласовано")
    @allure.step("Нажатие чекбокса Согласовано")
    def press_approved_checkbox(self):
        time.sleep(1)
        self.element_is_present(self.locators.checbox_by_text('Согласовано')).click()

    @testit.step("Получение цвета согласования трудозатрат")
    @allure.step("Получение цвета согласования трудозатрат")
    def get_labor_color(self, number_element):
        time.sleep(0.5)
        return self.elements_are_visible(self.locators.LABOR_COLOR)[number_element].value_of_css_property('background-color')

    @testit.step("Проверка цвета кружка Согласовано")
    @allure.step("Проверка цвета кружка Согласовано")
    def check_approved_reason_on_tab(self):
        assert self.get_labor_color(0) == 'rgba(46, 125, 50, 1)', "Кружок согласованно не зеленого цвета"

    @testit.step("Нажатие чекбокса Ожидает согласования")
    @allure.step("Нажатие чекбокса Ожидает согласования")
    def press_wait_approved_checkbox(self):
        time.sleep(1)
        self.element_is_present(self.locators.checbox_by_text('Ожидает согласования')).click()

    @testit.step("Нажатие чекбокса Отклонено")
    @allure.step("Нажатие чекбокса Отклонено")
    def press_rejected_checkbox(self):
        time.sleep(1)
        self.element_is_present(self.locators.checbox_by_text('Отклонено')).click()

    @testit.step("Проверка цвета кружка Отклонено")
    @allure.step("Проверка цвета кружка Отклонено")
    def check_rejected_on_tab(self):
        assert self.get_labor_color(0) == 'rgba(211, 47, 47, 1)', "Кружок Отклонено не красного цвета"

    @testit.step("Проверка цвета кружка Ожидает согласования")
    @allure.step("Проверка цвета кружка Ожидает согласования")
    def check_wait_approved_reason_on_tab(self):
        assert self.get_labor_color(0) == 'rgba(217, 217, 217, 1)', "Кружок Ожидает согласования не серого цвета"

    @testit.step("Переход на следующий период")
    @allure.step("Переход на следующий период")
    def go_to_next_period(self):
        time.sleep(0.5)
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        time.sleep(0.5)

    @testit.step("Нажатие иконки согласования трудозатрат")
    @allure.step("Нажатие иконки согласования трудозатрат")
    def press_done_icon(self):
        self.element_is_visible(self.locators.DONE_ICON).click()

    @testit.step("Нажатие иконки отклонения трудозатрат")
    @allure.step("Нажатие иконки отклонения трудозатрат")
    def press_clear_icon(self):
        self.element_is_visible(self.locators.CLEAR_ICON).click()

    @testit.step("Получение кликабельности кнопки Сохранить модального окна")
    @allure.step("Получение кликабельности кнопки Сохранить модального окна")
    def check_dialog_submit_button_clickable(self):
        return self.element_is_clickable(self.locators.SUBMIT_BUTTON_IN_DIALOG)

    @testit.step("Заполнение поля Причина отклонения")
    @allure.step("Заполнение поля Причина отклонения")
    def field_modal_reason_field(self, text):
        self.action_select_all_text(self.element_is_visible(self.locators.REASON_TEXTAREA))
        self.element_is_visible(self.locators.REASON_TEXTAREA).send_keys(text)

    @testit.step("Клик на ячейку со списанием по тексту")
    @allure.step("Клик на ячейку со списанием по тексту")
    def press_cell_with_labor_reason_by_text(self, text):
        self.element_is_visible(self.locators.labor_reason_on_modal_by_text(text)).click()

    @testit.step("Нажатие кнопки отмены отклонения трудозатрат")
    @allure.step("Нажатие кнопки отмены отклонения трудозатрат")
    def press_dialog_abort_button(self):
        self.element_is_visible(self.locators.ABORT_BUTTON_IN_DIALOG).click()

    @testit.step("Нажатие кнопки сохранить в диалоговом окне")
    @allure.step("Нажатие кнопки сохранить в диалоговом окне")
    def press_dialog_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON_IN_DIALOG).click()

    @testit.step("Получение тултипа причины отклонения трудозатрат")
    @allure.step("Получение тултипа причины отклонения трудозатрат")
    def get_tooltip_text_reject_labor_cost(self):
        self.action_move_to_element(self.elements_are_visible(self.locators.LABOR_COLOR)[1])
        return self.element_is_visible(self.locators.TOOLTIP).text

    @testit.step("Получение тултипа интеграций")
    @allure.step("Получение тултипа интеграций")
    def get_integrations_tooltip_text(self, text):
        self.action_move_to_element(self.elements_are_visible(self.locators.labor_reason_by_text(text))[0])
        all_tooltip_strings = self.elements_are_visible(self.locators.INTEGRATIONS_TOOLTIP_TEXTS)
        strings_text = []
        for string in all_tooltip_strings:
            strings_text.append(string.text)
        return strings_text

    @testit.step("Получение тултипа статуса согласования переработки")
    @allure.step("Получение тултипа статуса согласования переработки")
    def get_tooltip_text_on_approval_status(self):
        self.action_move_to_element(self.element_is_visible(self.locators.OVERTIME_APPROVAL_STATUS))
        return self.element_is_visible(self.locators.TOOLTIP).text
    
    @testit.step("Получение списка значений из дропдауна на вкладке 'Ресурсный план'")
    @allure.step("Получение списка значений из дропдауна на вкладке 'Ресурсный план'")
    def get_list_values_dropdown_resource_plan_tab(self):
        self.element_is_visible(self.locators.DROVER_MENU).click()
        menu_title_list = self.elements_are_visible(self.locators.DROVER_MENU_ITEM)
        data = []
        for title in menu_title_list:
            data.append(title.text)
        self.action_esc()
        return data

    @testit.step("Проверка дровера 'Добавление процента занятости' на вкладке 'Ресурсный план'")
    @allure.step("Проверка дровера 'Добавление процента занятости' на вкладке 'Ресурсный план'")
    def check_drover_resource_plan_tab(self):
        assert (self.element_is_visible(self.locators.DROVER_TITLE).text ==
                'Добавление процента занятости'), "Нет заголовка дровера"
        assert self.element_is_visible(self.locators.DROVER_INPUT).get_attribute("value") == '100', "В поле по умолчанию не 100"
        assert self.get_list_values_dropdown_resource_plan_tab() == ['0', '12.5', '25', '37.5', '50', '62.5', '75', '87.5', '100'], \
            "Не все значения отображены для выбора"
        assert self.element_is_visible(self.locators.DROVER_START_DATE).get_attribute('value') == datetime.now().strftime('%d.%m.%Y'), \
            "Дата начала по умолчанию не текущая дата"
        assert self.element_is_visible(self.locators.DROVER_END_DATE).get_attribute('value') == '', \
            "Дата окончания по умолчанию не пустое" 
        self.element_is_visible(self.locators.DROVER_END_DATE).send_keys(f"{self.get_day_before(1)}")
        assert self.element_is_visible(self.locators.DROVER_HELP_TEXT_END_DATE).text == \
            'Указанная дата не может быть раньше даты начала периода привлечения', "Дата окончания раньше Даты начала"
        assert self.element_is_displayed(self.locators.DROVER_SUBMIT_BUTTON), "В дровере нет кнопки Сохранить"
        assert self.element_is_displayed(self.locators.DROVER_ABORT_BUTTON), "В дровере нет кнопки Отменить"

    @testit.step("Внесение периода привлечения занятости")
    @allure.step("Внесение периода привлечения занятости")
    def set_period_and_employment(self):
        self.element_is_visible(self.locators.DROVER_MENU).click()
        (self.elements_are_visible(self.locators.DROVER_MENU_ITEM))[8].click()
        self.element_is_visible(self.locators.DROVER_START_DATE).send_keys(self.get_day_after(1))
        self.element_is_visible(self.locators.DROVER_END_DATE).send_keys(self.get_day_after(5))
    
    @allure_testit_step("Внесение периода привлечения занятости c заданными параметрами")
    def set_period_and_busy(self, start_date, end_date, period=8):
        # period это порядковый номер элемента, в зависимости от выбора радиобаттона
        # 8 - это 100% или 8 часов если не переключен радиобаттон (4 это 50% или 4 часа)
        time.sleep(1)
        self.action_select_all_text(self.element_is_visible(self.locators.DROVER_START_DATE))
        self.element_is_visible(self.locators.DROVER_START_DATE).send_keys(start_date)
        time.sleep(1)
        self.element_is_visible(self.locators.DROVER_END_DATE).click()
        self.element_is_visible(self.locators.DROVER_END_DATE).send_keys(end_date)
        self.element_is_visible(self.locators.DROVER_MENU, 10).click()
        (self.elements_are_visible(self.locators.DROVER_MENU_ITEM, 10))[period].click()

    @allure_testit_step("Получение процентов/часов привлечения")
    def get_busy(self, start_date):
        date_obj = datetime.strptime(start_date, "%d.%m.%Y")
        formatted_date = f"resultHours.{date_obj.strftime('%d-%m-%Y')}"
        busy = self.element_is_visible(self.locators.busy(formatted_date)).text        
        return busy
    
    @testit.step("Нажатие на поле 'Дата начала' в дровере")
    @allure.step("Нажатие на поле 'Дата начала' в дровере")
    def press_start_date_in_drover(self):
        self.element_is_visible(self.locators.DROVER_START_DATE).click()

    @testit.step("Нажатие на поле 'Дата окончания' в дровере")
    @allure.step("Нажатие на поле 'Дата окончания' в дровере")
    def press_end_date_in_drover(self):
        self.element_is_visible(self.locators.DROVER_END_DATE).click()

    @testit.step("Проверка отображения выпадающего календаря")
    @allure.step("Проверка отображения выпадающего календаря")
    def check_dropdown_calendar(self):
        assert self.element_is_displayed(self.locators.DROVER_DROPDOWN_CALENDAR), "Нет выпадающего календаря"

    @testit.step("Проверка дат за границами проекта")
    @allure.step("Проверка дат за границами проекта")
    def check_dates_outside_project_boundaries(self, start_date, end_date):
        day_start = int(start_date.split('.')[0])
        day_end = int(end_date.split('.')[0])
        day_before_start = day_start - 1
        day_after_end = day_end + 1
        time.sleep(1)
        assert not self.element_is_clickable(self.locators.buttons_day_calendar(str(day_before_start)), 0.5), \
            "Дата до начала проекта доступна для выбора"
        assert not self.element_is_clickable(self.locators.buttons_day_calendar(str(day_after_end)), 0.5), \
            "Дата после окончания проекта доступна для выбора"
        
    @testit.step("Нажатие кнопки 'Сохранить' в дровере")
    @allure.step("Нажатие кнопки 'Сохранить' в дровере")
    def press_save_in_drover(self):
        self.element_is_visible(self.locators.DROVER_SUBMIT_BUTTON).click()
        
    @testit.step("Нажатие кнопки 'Отмена' в дровере")
    @allure.step("Нажатие кнопки 'Отмена' в дровере")
    def press_cancel_in_drover(self):
        self.element_is_visible(self.locators.DROVER_ABORT_BUTTON).click()
        
    @allure_testit_step("Получение данных таблицы 'Ресурсный план'")
    def displaying_table_resource_plan(self):
        list_cells = []
        cells = self.elements_are_visible(self.locators.CELLS, 30)
        for cell in cells:
            list_cells.append(cell.text)
        return list_cells

    @testit.step("Проверка значения ячейки в табе 'Ресурсный план' по умолчанию")
    @allure.step("Проверка значения ячейки в табе 'Ресурсный план' по умолчанию")
    def checking_cell_default_value(self):
        assert (self.displaying_table_resource_plan())[2] == '0%', "Процент привлечения по умолчанию не равен '0'"

    @testit.step("Проверка значений выпадающего списка ячейки в табе 'Ресурсный план'")
    @allure.step("Проверка значений выпадающего списка ячейки в табе 'Ресурсный план'")
    def checking_cell_dropdown_list_values(self):
        self.action_double_click(self.elements_are_visible(self.locators.CELLS)[2])
        assert self.get_text_menu_items() == ['0%', '12.5%', '25%', '37.5%', '50%', '62.5%', '75%', '87.5%', '100%',], \
            "Некорректные значения в выпадающем меню ячейки"

    @testit.step("Проверка окрашивания ячеек в зависимости от выбранного значения")
    @allure.step("Проверка окрашивания ячеек в зависимости от выбранного значения")
    def checking_color_cell(self):
        color_cell = []
        for i in range(9):
            self.action_double_click(self.elements_are_visible(self.locators.CELLS)[2])
            self.elements_are_visible(self.locators.LI_MENU_ITEM)[i].click()
            time.sleep(0.2)
            color = self.elements_are_visible(self.locators.CELLS)[2].value_of_css_property('background-color')
            color_cell.append(color)
        assert color_cell == ['rgba(0, 0, 0, 0)', 'rgba(223, 244, 255, 0.3)', 'rgba(223, 244, 255, 0.3)',
                              'rgba(223, 244, 255, 0.3)', 'rgba(223, 244, 255, 0.6)', 'rgba(223, 244, 255, 0.6)',
                              'rgba(223, 244, 255, 0.6)', 'rgba(223, 244, 255, 0.6)', 'rgba(204, 231, 246, 1)'], \
            "Цвет заливки ячеек не соответствует"

    @testit.step("Внести изменения в таблицу 'Ресурсный план'")
    @allure.step("Внести изменения в таблицу 'Ресурсный план'")
    def change_table_resource_plan(self):
        self.action_double_click(self.elements_are_visible(self.locators.CELLS)[1])
        #выбираем последнее значение в выпадающем списке
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[8].click()

    @allure_testit_step("Получение данных из 1й ячейки таблицы 'Ресурсный план'")
    def get_value_cell(self):
        return (self.elements_are_visible(self.locators.CELLS))[1].text

    @testit.step("Переключение временных интервалов")
    @allure.step("Переключение временных интервалов")
    def switching_time_intervals(self, period):
        self.check_time_intervals(0, period)
        self.element_is_visible(self.locators.PREVIOUS_PERIOD_BUTTON).click()
        self.check_time_intervals(-1, period)
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()
        self.element_is_visible(self.locators.NEXT_PERIOD_BUTTON).click()
        self.check_time_intervals(1, period)
        self.element_is_visible(self.locators.THIS_DAY_BUTTON).click()

    @testit.step("Проверка отображения временных интервалов")
    @allure.step("Проверка отображения временных интервалов")
    def check_time_intervals(self, difference, period):
        if period == 'quarter':
            #Логика проверки для квартала
            displayed_interval = self.element_is_visible(self.locators.DISPLAYED_PERIOD).text
            current_quarter = (datetime.now().month - 1) // 3 + 1
            new_quarter = (current_quarter + difference - 1) % 4 + 1
            start_month = displayed_interval.split(" ")[0]
            end_month = displayed_interval.split(" ")[2]
            quarter_start_month = (datetime.strptime(start_month, '%B').month - 1) // 3 + 1
            quarter_end_month = (datetime.strptime(end_month, '%B').month - 1) // 3 + 1
            assert new_quarter == quarter_start_month == quarter_end_month, "Не отображается выбранный квартал"
            assert set([start_month, end_month]).issubset(set(self.get_low_string_in_header())), \
                "Не отображаются месяца выбранного квартала в столбцах"

        elif period == 'month':
            #Логика проверки для месяца
            day = self.get_hire_string_in_header()
            displayed_interval = self.element_is_visible(self.locators.DISPLAYED_PERIOD).text
            month_number = int(datetime.now().month) + difference
            date_object = datetime(2024, month_number, 1)
            assert '1' and '15' and '28' in day, "Не отображаются дни в столбцах"
            assert date_object.strftime('%B') == displayed_interval.split(" ")[0], "Не отображается выбранный месяц"

        elif period == 'year':
            #Логика проверки для года
            displayed_interval = self.element_is_visible(self.locators.DISPLAYED_PERIOD, 5).text
            assert set(['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',\
                    'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']) == set(self.get_hire_string_in_header()),\
                        "Не отображаются месяцы в столбцах"
            assert displayed_interval == str(datetime.now().year + difference), \
                "Не отображается выбранный год"
            assert set(self.get_low_string_in_header()) == set([displayed_interval]), \
                "Не отображается выбранный год в столбцах"

    @allure_testit_step("Проверка цвета ячейки превышающей максимальную занятость")
    def check_color_cell(self, maximum='100%'):
        if maximum == 'hours':
            maximum = '40'
        color_cell = self.element_is_visible(self.locators.text_on_cell(maximum)).value_of_css_property('background-color')
        assert color_cell == 'rgba(255, 236, 229, 1)', "Цвет ячейки превышающей максимальную занятость, не красного цвета"
    
    @allure_testit_step("Проверка кликабельности кнопки Сохранить")
    def check_save_button_is_clickable(self):
        return self.element_is_clickable(self.locators.SAVE_BUTTON)

    @allure_testit_step("Преобразование списка часов по дням в список по неделям")
    def converting_list_hours_day_to_list_week(self, list_month):
        list_week = []
        summa = 0
        for i in list_month:
            if i != '-':
                summa += int(i)
            else:
                if summa != 0:
                    list_week.append(summa)
                    summa = 0
        return list_week
    
    @allure_testit_step("Проверка модального окна 'Границы проекта'")
    def check_project_boundaries_modal_window(self):
        assert self.element_is_visible(self.locators.ALERT_DIALOG_TITLE).text in ['Границы проекта'], \
            "Нет заголовка модального окна"
        assert self.element_is_visible(self.locators.ALERT_DIALOG_DESCRIPTION).text == ("Существуют периоды привлечения,"
            " выходящие за новую дату начала/дату окончания проекта. В результате выполнения данной операции,"
             " такие периоды привлечения будут удалены и восстановить их будет невозможно."), \
                "Нет сообщения о выхождение за границы проекта"
        assert self.element_is_displayed(self.locators.MODAL_SUBMIT_BUTTON), "В модальном окне нет кнопки Подтвердить"
        assert self.element_is_displayed(self.locators.MODAL_ABORT_BUTTON), "В модальном окне нет кнопки Отменить"

    @allure_testit_step("Получить доступные пользователю ставки привлечения")
    def get_attraction_rates_by_user(self, user_name):
        self.element_is_visible(self.locators.get_attraction_rate_by_user(user_name)).click()
        return [element.text for element in self.elements_are_visible(self.locators.ATTRACTION_RATES)]

    @allure_testit_step("Получение списка Проектных ролей пользователя на табе 'Команда'")
    def get_list_project_roles_for_user(self, user_name):
        self.element_is_visible(self.locators.get_project_roles_by_user(user_name)).click()
        return [element.text for element in self.elements_are_visible(self.locators.LI_MENU_ITEM_TEXT)]