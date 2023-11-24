from locators.create_local_user_drawer_locators import CreateLocalUserDrawerLocators
from pages.base_page import BasePage


class CreateLocalUserDrawerPage(BasePage):
    locators = CreateLocalUserDrawerLocators()

    def go_to_create_local_user_drawer(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_ROLE).click()
        self.element_is_visible(self.locators.ADD_LOCAL_USER_BUTTON).click()

    def check_names_text(self):
        names_list = self.elements_are_visible(self.locators.INPUT_NAME_FIELDS)
        data = []
        for name in names_list:
            field_name = name.get_attribute("name")
            data.append(field_name)
        assert data == ['username', 'secondName', 'name', 'thirdName']

    def check_placeholder_text(self):
        names_list = self.elements_are_visible(self.locators.INPUT_PLACEHOLDER_FIELDS)
        data = []
        for name in names_list:
            field_name = name.get_attribute("placeholder")
            data.append(field_name)
        assert data == ['ДД.MM.ГГГГ', 'Начните вводить пол', 'ДД.MM.ГГГГ',
                                      'Начните вводить проектную роль', 'Начните вводить системную роль',
                                      'Начните вводить подразделение', 'Начните вводить должность',
                                      'Начните вводить Филиал']

    def check_hour_pay_checkbox(self):
        checkbox_text = self.element_is_visible(self.locators.HOUR_PAY_CHECKBOX).text
        assert checkbox_text == 'Почасовая оплата'

    def go_to_tab_projects(self):
        self.element_is_visible(self.locators.TAB_PROJECTS).click()

    def go_to_tab_contacts(self):
        self.element_is_visible(self.locators.TAB_CONTACTS).click()

    def check_add_project_button_and_fields(self):
        self.element_is_visible(self.locators.ADD_PROJECTS_BUTTON).click()
        fields_list = self.elements_are_visible(self.locators.PROJECTS_FIELDS)
        data = []
        for field in fields_list:
            data.append(field.text)
        assert data == ['Проект\u2009*', 'Роль в проекте\u2009*']

    def check_project_manager_checkbox(self):
        checkbox_text = self.element_is_visible(self.locators.PROJECT_MANAGER_CHECKBOX).text
        assert checkbox_text == 'Руководитель проекта'

    def check_names_on_contacts_text(self):
        names_list = self.elements_are_visible(self.locators.INPUT_NAME_FIELDS)
        data = []
        for name in names_list:
            field_name = name.get_attribute("name")
            data.append(field_name)
        assert data == ['phone', 'email']
