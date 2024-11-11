from locators.system_role_page_locators import SystemRolePageLocators
from utils.concat_testit_allure_step import allure_testit_step
from pages.base_page import BasePage


class SystemRolePage(BasePage):
    locators = SystemRolePageLocators()

    @allure_testit_step("Переход на таблицу Системные роли")
    def go_to_system_roles_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_ROLE).click()
        self.element_is_visible(self.locators.ADMIN_SYSTEM_ROLE_TAB).click()

    @allure_testit_step("Проверка создания системной роли")
    def check_create_system_role(self, role_name):
        self.element_is_visible(self.locators.CREATE_SYSTEM_ROLE_BUTTON).click()
        self.element_is_visible(self.locators.INPUT_ROLE_FIELD).send_keys(role_name)
        self.elements_are_visible(self.locators.ALL_TAG_CHECKBOXES)[1].click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        
    @allure_testit_step("Проверка наличия системной роли в дропдауне")
    def check_role_name_in_dropdown(self, role_name):
        assert role_name in self.get_all_role_names(), 'Роли нет в дропдауне'

    @allure_testit_step("Получение списка системных ролей в дропдауне")
    def get_all_role_names(self):
        self.element_is_visible(self.locators.ROLE_FIELD).click()
        all_roles_element = self.elements_are_visible(self.locators.ALL_NAMES_IN_DROPDOWN)
        data =[]
        for element in all_roles_element:
            self.action_move_to_element(element)
            data.append(element.get_attribute('aria-label'))
        return data

    @allure_testit_step("Выбор системной роли в дропдауне")
    def select_role_name_in_dropdown(self, role_name):
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()
        self.element_is_visible(self.locators.get_name_in_dropdown(role_name)).click()

    @allure_testit_step("Проверка неактивности кнопки удаления системной роли")
    def check_delete_role_icon_is_disabled(self):
        assert self.element_is_visible(self.locators.DELETE_ROLE_ICON).get_attribute('disabled'), \
            "Кнопка удаления системной роли активна"

    @allure_testit_step("Получение тултипа невозможности удаления системной роли")
    def get_tooltip_text_impossibility_deleting_system_role_user(self):
        return self.element_is_visible(self.locators.TOOLTIP_ROLE_ICON).get_attribute('aria-label')
    
    @allure_testit_step("Удаление системной роли")
    def delete_system_role(self, role_name):
        self.element_is_visible(self.locators.get_name_in_dropdown(role_name)).click()
        self.element_is_visible(self.locators.DELETE_ROLE_ICON).click()
        self.element_is_visible(self.locators.SUBMIT_DELETE_ROLE_BUTTON).click()
    