from locators.project_card_locators import ProjectCardLocators
from pages.base_page import BasePage


class ProjectCardPage(BasePage):
    locators = ProjectCardLocators()

    def go_to_description_tab(self):
        self.element_is_visible(self.locators.DESCRIPTION_TAB).click()

    def get_project_autor_name(self):
        output_autor_name = self.element_is_visible(self.locators.AUTOR_NAME).text
        return output_autor_name

    def get_project_description(self):
        output_project_name = self.element_is_visible(self.locators.NAME_FIELD).get_attribute("defaultValue")
        output_project_code = self.element_is_visible(self.locators.CODE_FIELD).get_attribute("defaultValue")
        output_project_status = self.element_is_visible(self.locators.STATUS_FIELD).get_attribute("value")
        output_project_begin_data = self.element_is_visible(self.locators.BEGIN_DATA_FIELD).get_attribute("value")
        output_project_manager = self.element_is_visible(self.locators.MANAGER_LABEL).text
        return output_project_name, output_project_code, output_project_status, output_project_begin_data, output_project_manager





