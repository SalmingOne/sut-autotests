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

    @testit.workItemIds(64974)
    @testit.displayName("10.4.2.3.2 Удаление/отмена удаления навыка или знания из стека")
    @pytest.mark.regress
    @allure.title("id-64974 10.4.2.3.2 Удаление/отмена удаления навыка или знания из стека")
    def test_removing_unremoving_a_skill_or_knowledge_from_the_stack(self, login, driver):
        stacks_page = StacksPage(driver)
        stacks_page.go_to_stacks_page()
        stacks_page.press_add_stack_button()
        stacks_page.add_skill_to_stack()
        before = stacks_page.get_all_skills_name_in_tab()
        stacks_page.press_delete_skill_button()
        stacks_page.check_delete_skill_modal_window()
        stacks_page.press_modal_break_button()
        after_break = stacks_page.get_all_skills_name_in_tab()
        assert before == after_break, "После отмены удаления навыка таблица изменилась"
        stacks_page.delete_one_skill_from_stack()
        after_delete = stacks_page.get_all_skills_name_in_tab()
        assert before != after_delete, "Навык не удалился"

    @testit.workItemIds(12933)
    @testit.displayName("10.4.2.2. Просмотр стека")
    @pytest.mark.regress
    @allure.title("id-12933 10.4.2.2. Просмотр стека")
    def test_stack_view(self, create_stack, login, driver):
        stacks_page = StacksPage(driver)
        stacks_page.go_to_stacks_page()
        stacks_page.press_view_stack_button(create_stack['name'])
        time.sleep(1)
        titles = stacks_page.get_h6_titles()
        assert create_stack['name'] in titles, "Нет поля Название"
        assert create_stack['department']['name'] in titles, "Нет поля Отдел"
        assert 'Название' and 'Тип' and 'Описание' in titles, "Есть не все заголовки таблицы"
        stacks_page.check_view_tab_buttons()

    @testit.workItemIds(64977)
    @testit.displayName("10.4.2.4. Редактирование стека")
    @pytest.mark.regress
    @allure.title("id-64977 10.4.2.4. Редактирование стека")
    def test_editing_a_stack(self, create_stack, login, driver):
        stacks_page = StacksPage(driver)
        stacks_page.go_to_stacks_page()
        stacks_page.press_edit_stack_button(create_stack['name'])
        time.sleep(2)
        before = stacks_page.get_stack_field_values()
        stack_name, department = stacks_page.change_stack_name_and_department()
        stacks_page.delete_one_skill_from_stack()
        skill = stacks_page.add_skill_to_stack()
        after_redact = stacks_page.get_stack_field_values()
        stacks_page.press_submit_button()
        stacks_page.press_close_button()
        assert stacks_page.check_stack_name_on_page(stack_name), "Новое имя стека не отображается в таблице"
        stacks_page.press_edit_stack_button(stack_name)
        after_save = stacks_page.get_stack_field_values()
        assert before != after_save, "Стек не изменился"
        assert stack_name == after_redact[0], "Новое имя стека не отобразилось в поле"
        assert department == after_redact[1], "Новый отдел не отобразился в поле"
        assert [skill] == after_redact[2], "Новый навык/знание не отобразилось в поле"
        assert after_redact == after_save, "Внесенные изменения не сохранились"
