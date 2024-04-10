import time

import allure
import testit

from locators.create_local_user_drawer_locators import CreateLocalUserDrawerLocators
from pages.base_page import BasePage


class CreateLocalUserDrawerPage(BasePage):
    locators = CreateLocalUserDrawerLocators()

    @testit.step("Переход на дровер создания локального пользователя")
    @allure.step("Переход на дровер создания локального пользователя")
    def go_to_create_local_user_drawer(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_ROLE).click()
        self.element_is_visible(self.locators.ADD_LOCAL_USER_BUTTON).click()

    @testit.step("Есть поля с именем")
    @allure.step("Есть поля с именем")
    def check_names_text(self):
        names_list = self.elements_are_visible(self.locators.INPUT_NAME_FIELDS)
        data = []
        for name in names_list:
            data.append(name.get_attribute("name"))
        assert data == ['username', 'secondName', 'name', 'thirdName', 'metadata'], ("Отсутствуют поля с именем на "
                                                                                     "вкладке личные данные")

    @testit.step("Есть поля с плейсхолдером")
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

    @testit.step("Есть чекбокс почасовая оплата")
    @allure.step("Есть чекбокс почасовая оплата")
    def check_hour_pay_checkbox(self):
        assert self.element_is_displayed(self.locators.HOUR_PAY_CHECKBOX), "Чекбокс почасовая оплата отсутствует"

    @testit.step("Переход на вкладку проекты")
    @allure.step("Переход на вкладку проекты")
    def go_to_tab_projects(self):
        self.element_is_visible(self.locators.TAB_PROJECTS).click()

    @testit.step("Переход на вкладку контакты")
    @allure.step("Переход на вкладку контакты")
    def go_to_tab_contacts(self):
        self.element_is_visible(self.locators.TAB_CONTACTS).click()

    @testit.step("Есть все поля на вкладке контакты")
    @allure.step("Есть все поля на вкладке контакты")
    def check_add_project_button_and_fields(self):
        self.element_is_visible(self.locators.ADD_PROJECTS_BUTTON).click()
        fields_list = self.elements_are_visible(self.locators.PROJECTS_FIELDS)
        data = []
        for field in fields_list:
            data.append(field.text)
        assert data == ['Проект\u2009*', 'Роль в проекте\u2009*'], "Некоторые поля на вкладке проекты отсутствуют"

    @testit.step("Есть чекбокс руководитель проекта")
    @allure.step("Есть чекбокс руководитель проекта")
    def check_project_manager_checkbox(self):
        assert self.element_is_displayed(self.locators.PROJECT_MANAGER_CHECKBOX), "Чекбокс руководитель проекта отсутствует"

    @testit.step("Есть все поля на вкладке контакты")
    @allure.step("Есть все поля на вкладке контакты")
    def check_names_on_contacts_text(self):
        names_list = self.elements_are_visible(self.locators.INPUT_NAME_FIELDS)
        data = []
        for name in names_list:
            data.append(name.get_attribute("name"))
        assert data == ['phone', 'email'], "Некоторые поля на вкладке контакты отсутствуют"

    @testit.step("Есть кнопка удаления проекта")
    @allure.step("Есть кнопка удаления проекта")
    def check_delete_project_button(self):
        assert self.element_is_displayed(self.locators.DELETE_PROJECTS_BUTTON), "Кнопка удаления проекта"

    @testit.step("Есть кнопка закрытия дровера")
    @allure.step("Есть кнопка закрытия дровера")
    def check_clear_icon_button(self):
        assert self.element_is_displayed(self.locators.CLEAR_BUTTON), "Кнопка закрытия дровера отсутствует"

    @testit.step("Есть кнопка сохранения")
    @allure.step("Есть кнопка сохранения")
    def check_save_button(self):
        assert self.element_is_displayed(self.locators.SAVE_BUTTON), "Кнопка сохранения отсутствует"

    @testit.step("Есть кнопка отмены")
    @allure.step("Есть кнопка отмены")
    def check_abort_button(self):
        assert self.element_is_displayed(self.locators.ABORT_BUTTON), "Кнопка отмены отсутствует"

    @testit.step("Выбираем в дровере первое значение")
    @allure.step("Выбираем в дровере первое значение")
    def input_dropdown(self, locator):
        self.action_move_to_element(self.element_is_visible(locator))
        self.element_is_visible(locator).click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[0].click()

    @testit.step("Создаем локального пользователя")
    @allure.step("Создаем локального пользователя")
    def field_required_fields(self, login, second_name, email, save):
        self.element_is_visible(self.locators.LOGIN_FIELD).send_keys(login)
        self.element_is_visible(self.locators.SECOND_NAME_FIELD).send_keys(second_name)
        self.element_is_visible(self.locators.NAME_FIELD).send_keys('Автомат')
        self.action_move_to_element(self.element_is_visible(self.locators.GENDER_FIELD))
        self.element_is_visible(self.locators.GENDER_FIELD).click()
        self.element_is_visible(self.locators.GENDER_MAILE).click()
        time.sleep(0.2)  # Без ожидания иногда скрипт срабатывает раньше анимации
        self.input_dropdown(self.locators.PROJECT_ROLES_FIELD)
        self.action_esc()
        self.input_dropdown(self.locators.DEPARTMENT_FIELD)
        self.input_dropdown(self.locators.POSITION_FIELD)
        self.go_to_tab_projects()
        time.sleep(1)
        self.element_is_visible(self.locators.ADD_PROJECTS_BUTTON).click()
        time.sleep(0.1)  # Без ожидания иногда скрипт срабатывает раньше анимации
        self.element_is_visible(self.locators.PROJECT_FIELD).click()
        self.elements_are_visible(self.locators.DROPDOWN_ITEMS)[0].click()
        self.go_to_tab_contacts()
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
        if save == 'yes':
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
        elif save == 'no':
            self.element_is_visible(self.locators.ABORT_BUTTON).click()

    @testit.step("Берем текст сообщения системы")
    @allure.step("Берем текст сообщения системы")
    def check_massage(self):
        return self.element_is_visible(self.locators.ALERT_MESSAGE).text
