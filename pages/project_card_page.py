import allure
from selenium.common import StaleElementReferenceException

from locators.project_card_locators import ProjectCardLocators
from pages.base_page import BasePage


class ProjectCardPage(BasePage):
    locators = ProjectCardLocators()

    @allure.step("Переход на вкладку описание проекта")
    def go_to_description_tab(self):
        self.element_is_visible(self.locators.DESCRIPTION_TAB).click()

    @allure.step("Получаем имя автора проекта")
    def get_project_autor_name(self):
        output_autor_name = self.element_is_visible(self.locators.AUTOR_NAME).text
        return output_autor_name

    @allure.step("Получаем значения полей вкладки описание проекта")
    def get_project_description(self):
        output_project_name = self.element_is_visible(self.locators.NAME_FIELD).get_attribute("defaultValue")
        output_project_code = self.element_is_visible(self.locators.CODE_FIELD).get_attribute("defaultValue")
        output_project_status = self.element_is_visible(self.locators.STATUS_FIELD).get_attribute("value")
        output_project_begin_data = self.element_is_visible(self.locators.BEGIN_DATA_FIELD).get_attribute("value")
        output_project_manager = self.element_is_visible(self.locators.MANAGER_LABEL).text
        return output_project_name, output_project_code, output_project_status, output_project_begin_data, output_project_manager

    @allure.step("Получаем роль, ресурс и ставку на первой строке команды до редактирования")
    def get_first_team_member(self):
        member_list = self.elements_are_present(self.locators.FIRST_MEMBER_TEXT)
        data = []
        for member in member_list:
            data.append(member.text)
        return data

    @allure.step("Получаем роль, ресурс и ставку на первой строке команды в режиме редактирования")
    def get_first_team_member_on_redact(self):
        member_list = self.elements_are_present(self.locators.FIRST_MEMBER_TEXT_ON_REDACT)
        data = []
        for member in member_list:
            data.append(member.get_attribute("value"))
        return data

    @allure.step("Переходим в режим редактирования команды")
    def go_to_redact_team(self):
        self.element_is_visible(self.locators.REDACT_BUTTON).click()

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

    @allure.step("Переход на вкладку команды проекта")
    def go_to_team_tab(self):
        self.element_is_visible(self.locators.TEAM_TAB).click()
