import time

from selenium.webdriver import Keys

from locators.create_project_drawer_locators import CreateProjectDrawerLocators
from pages.base_page import BasePage


class CreateProjectDrawerPage(BasePage):
    locators = CreateProjectDrawerLocators()

    def go_to_create_project_drawer_from_menu(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_PROJECTS))
        self.element_is_visible(self.locators.TAB_CREATE_PROJECT).click()

    def create_project(self):
        project_name = 'AutoTestProject'
        self.element_is_visible(self.locators.PROJECT_NAME_FIELD).send_keys(project_name)

        project_code = 'ATP'
        self.element_is_visible(self.locators.PROJECT_CODE_FIELD).send_keys(project_code)
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).click()
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(Keys.BACK_SPACE)

        project_data = '01.10.2023'
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(project_data)

        project_worker = 'Администратор Администратор'
        self.element_is_visible(self.locators.PROJECT_MANAGER_FIELD).send_keys(project_worker)
        self.element_is_visible(self.locators.CHOSE_ADMIN).click()
        self.element_is_visible(self.locators.PROJECT_RECOURSE_FIELD).send_keys(project_worker)
        self.element_is_visible(self.locators.CHOSE_ADMIN).click()

        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

        output_text = self.element_is_visible(self.locators.CHECK_CREATE_PROJECT).text
        # print(output_text)
        assert output_text == 'Команда', "Не отображается вкладка Команда карточки только что добавленного проекта"
        return project_name, project_code, project_data, project_worker
