import allure
import testit
from selenium.webdriver import Keys
from data.data import PROJECT_NAME, USER_NAME, PROJECT_CODE
from locators.create_project_drawer_locators import CreateProjectDrawerLocators
from pages.base_page import BasePage


class CreateProjectDrawerPage(BasePage):
    locators = CreateProjectDrawerLocators()

    @testit.step("Переход на дровер создания проекта")
    @allure.step("Переход на дровер создания проекта")
    def go_to_create_project_drawer_from_menu(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_PROJECTS))
        self.element_is_visible(self.locators.TAB_CREATE_PROJECT).click()

    @testit.step("Создание проекта")
    @allure.step("Создание проекта")
    def create_project(self, project_name, project_code, project_worker, checkbox):
        self.element_is_visible(self.locators.PROJECT_NAME_FIELD).send_keys(project_name)
        self.element_is_visible(self.locators.PROJECT_CODE_FIELD).send_keys(project_code)
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).click()
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(Keys.BACK_SPACE)

        project_data = '01.10.2022'
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(project_data)
        # выбор вариантов чекбокса (черновик, обязательное указание причины списания)
        if checkbox == "reason":
            self.element_is_visible(self.locators.REASON_CHECKBOX).click()
        elif checkbox == "draft":
            self.element_is_visible(self.locators.DRAFT_CHECKBOX).click()
        elif checkbox == "no":
            print('no checkboxes')

        self.element_is_visible(self.locators.PROJECT_MANAGER_FIELD).send_keys(project_worker)
        self.element_is_visible(self.locators.CHOSE_ADMIN).click()
        self.element_is_visible(self.locators.PROJECT_RECOURSE_FIELD).send_keys(project_worker)
        self.element_is_visible(self.locators.CHOSE_ADMIN).click()

        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return project_name, project_code, project_data, project_worker

    @testit.step("Проверяем что после создания перешли на вкладку Команда карточки проекта")
    @allure.step("Проверяем что после создания перешли на вкладку Команда карточки проекта")
    def check_created_project(self):
        output_text = self.element_is_visible(self.locators.CHECK_CREATE_PROJECT).text
        assert output_text == 'Команда', "Не отображается вкладка Команда карточки только что добавленного проекта"

    @testit.step("Берем текст ошибок с полей")
    @allure.step("Берем текст ошибок с полей")
    def get_mui_error_text(self):
        return self.element_is_visible(self.locators.MUI_ERROR).text

