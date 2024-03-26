
import allure
import pytest
import testit

from pages.skills_page import SkillsPage


@allure.suite("Справочник Знания")
class TestSkillsPage:

    @testit.workItemIds(10562)
    @testit.displayName("10.4.1.1 Просмотр страницы справочника Знания")
    @pytest.mark.smoke
    @allure.title("id-10562 10.4.1.1 Просмотр страницы справочника Знания")
    def test_viewing_the_knowledge_reference_page(self, skills, login, driver):
        skills_page = SkillsPage(driver)
        skills_page.go_to_skills_page()
        skills_page.check_add_skills_button()
        skills_page.check_columns_headers()
        skills_page.check_kebab_menu_item()
