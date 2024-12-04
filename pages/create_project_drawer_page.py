import time

import allure
import testit
from selenium.webdriver import Keys
from locators.create_project_drawer_locators import CreateProjectDrawerLocators
from pages.base_page import BasePage
from utils.concat_testit_allure_step import allure_testit_step


class CreateProjectDrawerPage(BasePage):
    locators = CreateProjectDrawerLocators()

    @testit.step("Переход на дровер создания проекта")
    @allure.step("Переход на дровер создания проекта")
    def go_to_create_project_drawer_from_menu(self):
        time.sleep(2)  # без этого ожидания иногда падает тест
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_PROJECTS))
        self.element_is_visible(self.locators.TAB_PROJECTS).click()
        self.element_is_visible(self.locators.TAB_CREATE_PROJECT).click()

    @testit.step("Создание проекта")
    @allure.step("Создание проекта")
    def create_project(self, project_name, project_code, project_worker, checkbox, begin_date, end_date=None):
        self.element_is_visible(self.locators.PROJECT_NAME_FIELD).send_keys(project_name)
        self.element_is_visible(self.locators.PROJECT_CODE_FIELD).send_keys(project_code)
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).click()
        self.action_select_all_text(self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD))
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(Keys.BACK_SPACE)
        project_data = '01.10.2022'
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(begin_date)
        if end_date is not None:
            self.element_is_visible(self.locators.PROJECT_END_DATA_FIELD).send_keys(end_date)
        else:
            pass
        # выбор вариантов чекбокса (черновик, обязательное указание причины списания)
        if checkbox == "reason":
            self.element_is_visible(self.locators.REASON_CHECKBOX).click()
        elif checkbox == "draft":
            self.element_is_visible(self.locators.DRAFT_CHECKBOX).click()
        elif checkbox == "no":
            print('no checkboxes')

        self.element_is_visible(self.locators.PROJECT_MANAGER_FIELD).send_keys(project_worker)
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()
        self.element_is_visible(self.locators.PROJECT_RECOURSE_FIELD).send_keys(project_worker)
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()

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

    @testit.step("Нажатие кнопки отмены добавления проекта")
    @allure.step("Нажатие кнопки отмены добавления проекта")
    def press_break_button(self):
        self.element_is_visible(self.locators.BREAK_BUTTON).click()

    @allure_testit_step("Нажатие кнопки подтвердить")
    def press_confirm_button(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()

    @allure_testit_step("Нажатие кнопки сохранить")
    def press_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @allure_testit_step("Ввод данных в обязательные поля в дровере создания проекта")
    def enter_data_in_fields(self, project_name, project_code, start_date):
        self.element_is_visible(self.locators.PROJECT_NAME_FIELD).send_keys(project_name)
        self.element_is_visible(self.locators.PROJECT_CODE_FIELD).send_keys(project_code)
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).click()
        self.action_select_all_text(self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD))
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(Keys.BACK_SPACE)
        self.element_is_visible(self.locators.PROJECT_BEGIN_DATA_FIELD).send_keys(start_date)

    @allure_testit_step("Выбираем приоритет в дровере создания проекта")
    def select_priority_in_drover(self):
        self.element_is_visible(self.locators.PRIORITY_FIELD).click()
        self.element_is_visible(self.locators.FIRST_NOT_CHOOSE).click()

    @allure_testit_step("Проверка поля приоритет вкладки описание проекта")
    def check_priority_field_in_drover(self):
        assert self.get_all_priority_in_drover() == {'Низкий (1)': 'rgba(76, 175, 80, 1)',
                                                              'Низкий (2)': 'rgba(76, 175, 80, 1)',
                                                              'Низкий (3)': 'rgba(76, 175, 80, 1)',
                                                              'Средний (4)': 'rgba(255, 193, 7, 1)',
                                                              'Средний (5)': 'rgba(255, 193, 7, 1)',
                                                              'Средний (6)': 'rgba(255, 193, 7, 1)',
                                                              'Средний (7)': 'rgba(255, 193, 7, 1)',
                                                              'Высокий (8)': 'rgba(255, 87, 34, 1)',
                                                              'Высокий (9)': 'rgba(255, 87, 34, 1)',
                                                              'Высокий (10)': 'rgba(255, 87, 34, 1)'}, \
            'В выпадающем списке не все значения приоритетов'

    @allure_testit_step("Получаем все приоритеты вкладки описание проекта")
    def get_all_priority_in_drover(self):
        elem = self.element_is_present(self.locators.PRIORITY_FIELD)
        self.go_to_element(elem)
        elem.click()
        time.sleep(1)
        all_priority = self.elements_are_present(self.locators.LI_MENU_ITEM)
        all_colors = self.elements_are_present(self.locators.COLOR_MENU_ITEM)
        if len(all_priority) != len(all_colors):
            raise ValueError('Количество приоритетов и цветов не совпадает!')
        data = {}
        for priority, color in zip(all_priority, all_colors):
            data[priority.text] = color.value_of_css_property('color')
        self.action_esc()
        return data

    @allure_testit_step('Получить все сообщения системы')
    def get_all_messages(self):
        return self.get_all_alert_message(self.locators.ALERT_MESSAGE)
