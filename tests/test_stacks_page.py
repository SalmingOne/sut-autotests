import time

import allure
import pytest
import testit

from pages.stacks_page import StacksPage


@allure.suite("Справочник Стеки")
class TestStacksPage:

    @testit.workItemIds(64970)
    @testit.displayName("10.4.2.3. (Чек-лист) Негативные проверки при добавлении нового стека")
    @pytest.mark.regress
    @allure.title("id-64970 10.4.2.3. (Чек-лист) Негативные проверки при добавлении нового стека")
    def test_negative_checks_when_adding_a_new_stack(self, create_stack, login, driver):
        stacks_page = StacksPage(driver)
        stacks_page.go_to_stacks_page()
        stacks_page.press_add_stack_button()
        stacks_page.check_name_field()
        stacks_page.check_department_field()
        stacks_page.check_not_unique_name(create_stack['name'])
        stacks_page.delete_one_skill_from_stack()
        stacks_page.check_no_skill()
