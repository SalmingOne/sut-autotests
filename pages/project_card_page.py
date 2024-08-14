import time

import allure
import testit
from selenium.common import StaleElementReferenceException

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
                                                  'Автоматическое проставление трудозатрат']

    @testit.step("Проверка заголовка вкладки Описание")
    @allure.step("Проверка заголовка вкладки Описание")
    def check_description_tab_title(self):
        assert self.element_is_displayed(self.locators.DESCRIPTION_TAB_TITLE)

    @testit.step("Проверка наличия поля Имя на вкладке Описание")
    @allure.step("Проверка наличия поля Имя на вкладке Описание")
    def check_description_tab_name_field(self):
        assert self.element_is_displayed(self.locators.NAME_FIELD)

    @testit.step("Проверка наличия поля Код на вкладке Описание")
    @allure.step("Проверка наличия поля Код на вкладке Описание")
    def check_description_tab_code_field(self):
        assert self.element_is_displayed(self.locators.CODE_FIELD)

    @testit.step("Проверка наличия поля Код на вкладке Описание")
    @allure.step("Проверка наличия поля Код на вкладке Описание")
    def check_description_tab_status_field(self):
        assert self.element_is_displayed(self.locators.STATUS_FIELD)

    def check_description_tab_manager_field(self):
        assert self.element_is_displayed(self.locators.MANAGER_FIELD)

    def check_description_tab_start_field(self):
        assert self.element_is_displayed(self.locators.BEGIN_DATA_FIELD)

    def check_description_tab_end_field(self):
        assert self.element_is_displayed(self.locators.END_DATA_FIELD)

    def check_description_tab_description_field(self):
        assert self.element_is_displayed(self.locators.DESCRIPTION_FIELD)

    def check_description_tab_file_description_field(self):
        assert self.element_is_displayed(self.locators.FILE_DESCRIPTION_FIELD)

    def check_description_tab_save_button(self):
        assert self.element_is_displayed(self.locators.SAVE_BUTTON)

    def check_description_tab_break_button(self):
        assert self.element_is_displayed(self.locators.BREAK_BUTTON)

    def get_all_checkboxes_text(self):
        all_checkboxes = self.elements_are_visible(self.locators.CHECKBOXES_TEXT)
        checkboxes_text = []
        for checkbox in all_checkboxes:
            checkboxes_text.append(checkbox.text)
        return checkboxes_text

    def go_to_project_hierarchy_tab(self):
        self.element_is_visible(self.locators.PROJECT_HIERARCHY_TAB).click()

    def check_project_hierarchy_tab(self):
        time.sleep(1)
        self.check_project_hierarchy_tab_title()
        self.check_project_hierarchy_tab_switch()
        self.check_project_hierarchy_tab_scope_field()
        self.check_project_hierarchy_tab_centre_icon()
        self.check_project_hierarchy_tab_project_node()
        self.check_project_hierarchy_tab_source_icon()

    def check_project_hierarchy_tab_title(self):
        assert self.element_is_displayed(self.locators.PROJECT_HIERARCHY_TAB_TITLE)

    def check_project_hierarchy_tab_switch(self):
        assert self.element_is_displayed(self.locators.LEGEND_SWITCH)

    def check_project_hierarchy_tab_scope_field(self):
        assert self.element_is_displayed(self.locators.SCOPE_FIELD)

    def check_project_hierarchy_tab_centre_icon(self):
        assert self.element_is_displayed(self.locators.CENTER_FOCUS_ICON)

    def check_project_hierarchy_tab_project_node(self):
        assert self.element_is_displayed(self.locators.PROJECT_NODE_ICON)

    def check_project_hierarchy_tab_source_icon(self):
        assert self.element_is_displayed(self.locators.SOURCE_ICON)

    def check_team_tab(self):
        time.sleep(1)
        self.check_team_tab_redact_button()
        self.check_team_tab_to_excel_button()
        self.check_team_tab_filter_button()
        self.check_team_tab_number_of_recourses()
        self.check_team_tab_next_previous_buttons()
        self.check_team_tab_titles()

    def check_team_tab_redact_button(self):
        assert self.element_is_displayed(self.locators.REDACT_BUTTON)

    def check_team_tab_to_excel_button(self):
        assert self.element_is_displayed(self.locators.TO_EXCEL_BUTTON)

    def check_team_tab_filter_button(self):
        assert self.element_is_displayed(self.locators.TEAM_TAB_FILTER_BUTTON)

    def check_team_tab_number_of_recourses(self):
        assert self.element_is_displayed(self.locators.NUMBER_OF_RECOURSES)

    def check_team_tab_next_previous_buttons(self):
        assert self.element_is_displayed(self.locators.NEXT_PERIOD_BUTTON)
        assert self.element_is_displayed(self.locators.PREVIOUS_PERIOD_BUTTON)
        assert self.element_is_displayed(self.locators.THIS_DAY_BUTTON)

    def check_team_tab_titles(self):
        self.element_is_visible(self.locators.REDACT_BUTTON).click()
        all_titles = self.elements_are_visible(self.locators.TEAM_TAB_TITLES)
        titles_text = []
        for titles in all_titles:
            titles_text.append(titles.text)
        self.element_is_visible(self.locators.ABORT_BUTTON).click()
        time.sleep(2)
        assert titles_text == ['Ресурс', 'Ставка привлечения', 'Дата назначения пользователя на слот',
                               'Дата снятия пользователя со слота', 'Проектная роль', 'Действия']

    def go_to_resource_plan_tab(self):
        self.element_is_visible(self.locators.RESOURCE_PLAN_TAB).click()

    def check_resource_plan_tab(self):
        self.check_team_tab_next_previous_buttons()
        self.check_default_period()
        self.check_chose_period_list()

    @testit.step("Проверка периода выбранного по умолчанию")
    @allure.step("Проверка периода выбранного по умолчанию")
    def check_default_period(self):
        assert self.element_is_visible(self.locators.CHOSE_PERIOD_BUTTON).text == 'Квартал', \
            "По умолчанию выбран период не Квартал"

    @testit.step("Проверка списка выбора периодов")
    @allure.step("Проверка списка выбора периодов")
    def check_chose_period_list(self):
        self.element_is_visible(self.locators.CHOSE_PERIOD_BUTTON).click()
        all_items = self.elements_are_visible(self.locators.LI_MENU_ITEM)
        text = []
        for item in all_items:
            text.append(item.text)
        self.action_esc()
        assert text == ['Квартал', 'Месяц (по дням)', 'Год']
