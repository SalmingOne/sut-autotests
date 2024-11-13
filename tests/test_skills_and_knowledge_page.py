import allure
import pytest
import testit

from pages.skills_and_knowledge_page import SkillsAndKnowledgePage


@allure.suite("Справочник Знания и навыки")
class TestSkillsAndKnowledgePage:

    @testit.workItemIds(10562)
    @testit.displayName("10.4.1.1 Просмотр страницы справочника Знания")
    @pytest.mark.smoke
    @allure.title("id-10562 10.4.1.1 Просмотр страницы справочника Знания")
    def test_viewing_the_knowledge_reference_page(self, skills_and_knowledge, login, driver):
        skills_and_knowledge_page = SkillsAndKnowledgePage(driver)
        skills_and_knowledge_page.go_to_skills_page()
        skills_and_knowledge_page.check_add_skills_button()
        skills_and_knowledge_page.check_columns_headers()
        skills_and_knowledge_page.check_kebab_menu_item()
