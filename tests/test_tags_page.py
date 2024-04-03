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
    @testit.displayName("12.1.1 Добавление не валидной интеграции")
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
        tags_page.create_tag('Тег для авто-теста', create_skill)
        tags_page.check_tag_on_tag_tab('Тег для авто-теста')
        skills_page.go_to_skill_tab()
        skills_page.check_tag_on_skill_tab(create_skill, 'Тег для авто-теста')
        # Удаление тега после теста
        tags_endpoint.delete_tag_by_name_api('Тег для авто-теста')


