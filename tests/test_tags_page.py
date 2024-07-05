import time

import allure
import pytest
import testit

from endpoints.tags_endpoint import TagsEndpoint
from pages.skills_page import SkillsPage
from pages.tags_page import TagsPage


@allure.suite("Страница группы знаний")
class TestTagsPage:

    @testit.workItemIds(10584)
    @testit.displayName("10.4.2.2 Добавление данных в справочник группы знаний")
    @pytest.mark.smoke
    @allure.title("id-10584 10.4.2.2 Добавление данных в справочник группы знаний")
    def test_adding_data_to_the_knowledge_groups_directory(self, create_skill, skills, login, driver):
        tags_page = TagsPage(driver)
        skills_page = SkillsPage(driver)
        tags_endpoint = TagsEndpoint()
        tags_page.go_to_tags_page()
        time.sleep(1)  # Нужно время на анимацию
        tags_page.press_add_tag_button()
        tags_page.check_name_field()
        tags_page.create_tag('AAABBB', create_skill)
        tags_page.sort_tags()
        tags_page.check_tag_on_tag_tab('AAABBB')
        skills_page.go_to_skill_tab()
        time.sleep(1)
        skills_page.sort_skills()
        skills_page.check_tag_on_skill_tab(create_skill, 'AAABBB')
        # Удаление тега после теста
        tags_endpoint.delete_tag_by_name_api('AAABBB')

    @testit.workItemIds(10593)
    @testit.displayName("10.4.2.3 Редактирование данных в справочнике группы знаний")
    @pytest.mark.smoke
    @allure.title("id-10593 10.4.2.3 Редактирование данных в справочнике группы знаний")
    def test_editing_data_to_the_knowledge_groups_directory(self, create_skill, create_tag, login, driver):
        tags_page = TagsPage(driver)
        skills_page = SkillsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.sort_tags()
        time.sleep(1)
        tags_page.edit_tag(create_tag[0], 'ASBEST', create_skill)
        tags_page.check_tag_on_tag_tab('ASBEST')
        skills_page.go_to_skill_tab()
        time.sleep(1)
        skills_page.sort_skills()
        time.sleep(1)
        skills_page.check_tag_on_skill_tab(create_skill, 'ASBEST')

    @testit.workItemIds(10563)
    @testit.displayName("10.4.2.1 Просмотр страницы справочника Группы знаний")
    @pytest.mark.regress
    @allure.title("id-10563 10.4.2.1 Просмотр страницы справочника Группы знаний")
    def test_viewing_the_tags_page(self, create_tag, login, driver):
        tags_page = TagsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.check_add_teg_button()
        tags_page.check_columns_headers()
        tags_page.check_kebab_menu_item()
