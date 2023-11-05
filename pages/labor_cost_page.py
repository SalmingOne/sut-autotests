from locators.labor_cost_page_locators import LaborCostPageLocators
from pages.base_page import BasePage


class LaborCostPage(BasePage):
    locators = LaborCostPageLocators()

    def go_to_labor_cost_page(self):
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_ACTIVITY))
        self.element_is_visible(self.locators.TAB_LABOR_COST_TABLE).click()

    def check_project_code_at_labor(self):
        check_code_at_labor = self.element_is_present(self.locators.CHECK_CODE_PROJECT).text
        print(check_code_at_labor)
        return check_code_at_labor
