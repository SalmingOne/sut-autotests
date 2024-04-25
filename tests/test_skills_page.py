import time

import allure
import pytest
import testit

from endpoints.skills_endpoint import SkillsEndpoint
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

    @testit.workItemIds(10484)
    @testit.displayName("10.4.1.3 Редактирование данных в справочнике Знания")
    @pytest.mark.smoke
    @allure.title("id-10484 10.4.1.3 Редактирование данных в справочнике Знания")
    def test_editing_the_knowledge_directory(self, create_skill, login, driver):
        skills_page = SkillsPage(driver)
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        skills_page.redact_skill_by_name(create_skill)
        skills_page.check_max_name_field()
        skills_page.redact_skill_by_name(create_skill)
        skills_page.change_the_skill('AAABBB')
        time.sleep(1)
        skills_page.check_skill_name_on_page('AAABBB')
        skills_page.check_skill_name_on_tag_tab('AAABBB')

    @testit.workItemIds(10464)
    @testit.displayName("10.4.1.2 Добавление данных в справочник Знания")
    @pytest.mark.smoke
    @allure.title("id-10464 10.4.1.2 Добавление данных в справочник Знания")
    def test_adding_the_knowledge_directory(self, create_tag, login, driver):
        skills_page = SkillsPage(driver)
        skills_endpoint = SkillsEndpoint()
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        skills_page.create_skill('AAAДобавленное знание', create_tag)
        skills_page.check_skill_name_on_page('AAAДобавленное знание')
        skills_page.check_skill_name_on_tag_tab('AAAДобавленное знание')

        skills_endpoint.delete_skill_by_name_api('AAAДобавленное знание')
