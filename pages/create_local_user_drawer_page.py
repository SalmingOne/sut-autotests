import time

import allure

from locators.create_local_user_drawer_locators import CreateLocalUserDrawerLocators
from pages.base_page import BasePage


class CreateLocalUserDrawerPage(BasePage):
    locators = CreateLocalUserDrawerLocators()

    @allure.step("Переход на дровер создания локального пользователя")
    def go_to_create_local_user_drawer(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_ROLE).click()
        self.element_is_visible(self.locators.ADD_LOCAL_USER_BUTTON).click()

    @allure.step("Есть поля с именем")
    def check_names_text(self):
        names_list = self.elements_are_visible(self.locators.INPUT_NAME_FIELDS)
        data = []
        for name in names_list:
            data.append(name.get_attribute("name"))
        assert data == ['username', 'secondName', 'name', 'thirdName', 'metadata'], ("Отсутствуют поля с именем на "
                                                                                     "вкладке личные данные")

    @allure.step("Есть поля с плейсхолдером")
    def check_placeholder_text(self):
        names_list = self.elements_are_visible(self.locators.INPUT_PLACEHOLDER_FIELDS)
        data = []
        for name in names_list:
            data.append(name.get_attribute("placeholder"))
        assert data == ['ДД.MM.ГГГГ', 'Начните вводить пол', 'ДД.MM.ГГГГ',
                        'Начните вводить проектную роль', 'Начните вводить системную роль',
                        'Начните вводить подразделение', 'Начните вводить должность',
                        'Начните вводить Филиал'], "Отсутствуют поля с плейсхолдером на вкладке личные данные"

    @allure.step("Есть чекбокс почасовая оплата")
    def check_hour_pay_checkbox(self):
        checkbox_text = self.element_is_visible(self.locators.HOUR_PAY_CHECKBOX).text
        assert checkbox_text == 'Почасовая оплата', "Чекбокс почасовая оплата отсутствует"

    @allure.step("Переход на вкладку проекты")
    def go_to_tab_projects(self):
        self.element_is_visible(self.locators.TAB_PROJECTS).click()

    @allure.step("Переход на вкладку контакты")
    def go_to_tab_contacts(self):
        self.element_is_visible(self.locators.TAB_CONTACTS).click()

    @allure.step("Есть все поля на вкладке контакты")
    def check_add_project_button_and_fields(self):
        self.element_is_visible(self.locators.ADD_PROJECTS_BUTTON).click()
        fields_list = self.elements_are_visible(self.locators.PROJECTS_FIELDS)
        data = []
        for field in fields_list:
            data.append(field.text)
        assert data == ['Проект\u2009*', 'Роль в проекте\u2009*'], "Некоторые поля на вкладке проекты отсутствуют"

    @allure.step("Есть чекбокс руководитель проекта")
    def check_project_manager_checkbox(self):
        checkbox_text = self.element_is_visible(self.locators.PROJECT_MANAGER_CHECKBOX).text
        assert checkbox_text == 'Руководитель проекта', "Чекбокс руководитель проекта отсутствует"

    @allure.step("Есть все поля на вкладке контакты")
    def check_names_on_contacts_text(self):
        names_list = self.elements_are_visible(self.locators.INPUT_NAME_FIELDS)
        data = []
        for name in names_list:
            data.append(name.get_attribute("name"))
        assert data == ['phone', 'email'], "Некоторые поля на вкладке контакты отсутствуют"

    @allure.step("Есть кнопка удаления проекта")
    def check_delete_project_button(self):
        button_text = self.element_is_visible(self.locators.DELETE_PROJECTS_BUTTON).get_attribute('aria-label')
        assert button_text == 'Удалить проект', "Кнопка удаления проекта"

    @allure.step("Есть кнопка закрытия дровера")
    def check_clear_icon_button(self):
        button_text = self.element_is_visible(self.locators.CLEAR_BUTTON).get_attribute('data-testid')
        assert button_text == 'ClearIcon', "Кнопка закрытия дровера отсутствует"

    @allure.step("Есть кнопка сохранения")
    def check_save_button(self):
        button_text = self.element_is_visible(self.locators.SAVE_BUTTON).get_attribute('type')
        assert button_text == "submit", "Кнопка сохранения отсутствует"

    @allure.step("Есть кнопка отмены")
    def check_abort_button(self):
        button_text = self.element_is_visible(self.locators.ABORT_BUTTON).text
        assert button_text == 'ОТМЕНИТЬ', "Кнопка отмены отсутствует"

    def input_dropdown(self, locator):
        self.action_move_to_element(self.element_is_visible(locator))
        self.element_is_visible(locator).click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[0].click()

    @allure.step("")
    def field_required_fields(self, abort=None):
        self.element_is_visible(self.locators.LOGIN_FIELD).send_keys('AutoUser')
        self.element_is_visible(self.locators.SECOND_NAME_FIELD).send_keys('Автоматов')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys('Автомат')
        self.action_move_to_element(self.element_is_visible(self.locators.GENDER_FIELD))
        self.element_is_visible(self.locators.GENDER_FIELD).click()
        self.element_is_visible(self.locators.GENDER_MAILE).click()
        time.sleep(0.1)
        self.input_dropdown(self.locators.PROJECT_ROLES_FIELD)
        self.action_esc()
        self.input_dropdown(self.locators.DEPARTMENT_FIELD)
        self.input_dropdown(self.locators.POSITION_FIELD)
        self.go_to_tab_projects()
        self.element_is_visible(self.locators.ADD_PROJECTS_BUTTON).click()
        self.element_is_visible(self.locators.PROJECT_FIELD).click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[0].click()
        self.go_to_tab_contacts()
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys('auto@mail.ru')
        if abort == 'yes':
            self.element_is_visible(self.locators.ABORT_BUTTON).click()
        else:
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
