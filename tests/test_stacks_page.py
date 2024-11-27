import time

import allure
import pytest
import testit

from endpoints.skills_and_knowledge_endpoint import SkillsAndKnowledgeEndpoint
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

    @testit.workItemIds(64972)
    @testit.displayName("10.4.2.3.1 Добавление/отмена добавления навыка или знания в стек")
    @pytest.mark.regress
    @allure.title("id-64972 10.4.2.3.1 Добавление/отмена добавления навыка или знания в стек")
    def test_add_undo_add_a_skill_or_knowledge_to_the_stack(self, create_skill, login, driver):
        stacks_page = StacksPage(driver)
        stacks_page.go_to_stacks_page()
        stacks_page.press_add_stack_button()
        stacks_page.press_add_skill_button()
        skills, knowledge = stacks_page.check_add_skill_drawer()
        skills_endpoint = SkillsAndKnowledgeEndpoint()
        skills_api, knowledge_api = skills_endpoint.get_skills_and_knowledge_lists_api()
        assert set(skills) == set(skills_api), "В дровере есть не все навыки"
        assert set(knowledge) == set(knowledge_api), "В дровере есть не все знания"
        stacks_page.check_choose_type()
        choose_name = stacks_page.check_choose_name()
        stacks_page.press_break_button()
        name_in_tab = stacks_page.get_all_skills_name_in_tab()
        assert choose_name not in name_in_tab, "Знание/навык добавился в стек"
        stacks_page.press_add_skill_button()
        stacks_page.check_description(create_skill)
        stacks_page.press_add_stack_button()
        name_in_tab = stacks_page.get_all_skills_name_in_tab()
        assert create_skill['name'] in name_in_tab, "Знание/навык не добавился в стек"
        stacks_page.press_add_skill_button()
        time.sleep(1)
        stacks_page.check_selected_skill_not_in_drawer(create_skill)
