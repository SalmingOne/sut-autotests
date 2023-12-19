import allure

from locators.create_local_user_drawer_locators import CreateLocalUserDrawerLocators
from pages.base_page import BasePage


class CreateLocalUserDrawerPage(BasePage):
    locators = CreateLocalUserDrawerLocators()

    # Переход на дровер создания локального пользователя
    @allure.step("Переход на дровер создания локального пользователя")
    def go_to_create_local_user_drawer(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_ROLE).click()
        self.element_is_visible(self.locators.ADD_LOCAL_USER_BUTTON).click()

    # Есть поля с именем
    @allure.step("Есть поля с именем")
    def check_names_text(self):
        names_list = self.elements_are_visible(self.locators.INPUT_NAME_FIELDS)
        data = []
        for name in names_list:
            data.append(name.get_attribute("name"))
        assert data == ['username', 'secondName', 'name', 'thirdName', 'metadata'], ("Отсутствуют поля с именем на "
                                                                                     "вкладке личные данные")

    # Есть поля с плейсхолдером
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

    # Есть чекбокс почасовая оплата
    @allure.step("Есть чекбокс почасовая оплата")
    def check_hour_pay_checkbox(self):
        checkbox_text = self.element_is_visible(self.locators.HOUR_PAY_CHECKBOX).text
        assert checkbox_text == 'Почасовая оплата', "Чекбокс почасовая оплата отсутствует"

    # Переход на вкладку проекты
    @allure.step("Переход на вкладку проекты")
    def go_to_tab_projects(self):
        self.element_is_visible(self.locators.TAB_PROJECTS).click()

    # Переход на вкладку контакты
    @allure.step("Переход на вкладку контакты")
    def go_to_tab_contacts(self):
        self.element_is_visible(self.locators.TAB_CONTACTS).click()

    # Есть все поля на вкладке контакты
    @allure.step("Есть все поля на вкладке контакты")
    def check_add_project_button_and_fields(self):
        self.element_is_visible(self.locators.ADD_PROJECTS_BUTTON).click()
        fields_list = self.elements_are_visible(self.locators.PROJECTS_FIELDS)
        data = []
        for field in fields_list:
            data.append(field.text)
        assert data == ['Проект\u2009*', 'Роль в проекте\u2009*'], "Некоторые поля на вкладке проекты отсутствуют"

    # Есть чекбокс руководитель проекта
    @allure.step("Есть чекбокс руководитель проекта")
    def check_project_manager_checkbox(self):
        checkbox_text = self.element_is_visible(self.locators.PROJECT_MANAGER_CHECKBOX).text
        assert checkbox_text == 'Руководитель проекта', "Чекбокс руководитель проекта отсутствует"

    # Есть все поля на вкладке контакты
    @allure.step("Есть все поля на вкладке контакты")
    def check_names_on_contacts_text(self):
        names_list = self.elements_are_visible(self.locators.INPUT_NAME_FIELDS)
        data = []
        for name in names_list:
            data.append(name.get_attribute("name"))
        assert data == ['phone', 'email'], "Некоторые поля на вкладке контакты отсутствуют"

    # Есть кнопка удаления проекта
    @allure.step("Есть кнопка удаления проекта")
    def check_delete_project_button(self):
        button_text = self.element_is_visible(self.locators.DELETE_PROJECTS_BUTTON).get_attribute('aria-label')
        assert button_text == 'Удалить проект', "Кнопка удаления проекта"

    # Есть кнопка закрытия дровера
    @allure.step("Есть кнопка закрытия дровера")
    def check_clear_icon_button(self):
        button_text = self.element_is_visible(self.locators.CLEAR_BUTTON).get_attribute('data-testid')
        assert button_text == 'ClearIcon', "Кнопка закрытия дровера отсутствует"

    # Есть кнопка сохранения
    @allure.step("Есть кнопка сохранения")
    def check_save_button(self):
        button_text = self.element_is_visible(self.locators.SAVE_BUTTON).get_attribute('type')
        assert button_text == "submit", "Кнопка сохранения отсутствует"

    # Есть кнопка отмены
    @allure.step("Есть кнопка отмены")
    def check_abort_button(self):
        button_text = self.element_is_visible(self.locators.ABORT_BUTTON).text
        assert button_text == 'ОТМЕНИТЬ', "Кнопка отмены отсутствует"
