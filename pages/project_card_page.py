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

