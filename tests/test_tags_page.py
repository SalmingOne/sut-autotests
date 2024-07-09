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
        assert tags_page.check_tag_on_tag_tab('AAABBB'), "Имени группы знаний нет на вкладке группы знаний"
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
        assert tags_page.check_tag_on_tag_tab('ASBEST'), "Имени группы знаний нет на вкладке группы знаний"
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

    @testit.workItemIds(10592)
    @testit.displayName("10.4.2.2 Добавление данных в справочник Группы знаний с несколькими знаниями")
    @pytest.mark.regress
    @allure.title("id-10592 10.4.2.2 Добавление данных в справочник Группы знаний с несколькими знаниями")
    def test_adding_the_tag_with_multiple_skills(self, create_skill, create_second_skill, login, driver):
        tags_page = TagsPage(driver)
        tags_endpoint = TagsEndpoint()
        skills_page = SkillsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.check_create_tag_with_two_skills('AA Два скила', create_skill, create_second_skill)
        tags_page.sort_tags()
        assert tags_page.check_tag_on_tag_tab('AA Два скила'), "Имени группы знаний нет на вкладке группы знаний"
        skills_page.go_to_skill_tab()
        time.sleep(1)
        skills_page.sort_skills()
        skills_page.check_tag_on_skill_tab(create_skill, 'AA Два скила')
        skills_page.check_tag_on_skill_tab(create_second_skill, 'AA Два скила')
        tags_endpoint.delete_tag_by_name_api('AA Два скила')

    @testit.workItemIds(10587)
    @testit.displayName("10.4.2.2 Отмена добавления значения в справочник Группы знаний")
    @pytest.mark.regress
    @allure.title("id-10587 10.4.2.2 Отмена добавления значения в справочник Группы знаний")
    def test_cansel_adding_tag(self, login, driver):
        tags_page = TagsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.check_cancel_adding_tag('aaa Для отмены')

    @testit.workItemIds(10588)
    @testit.displayName("10.4.2.2 Добавление знания в справочник Группы знаний без заполнения обязательных полей")
    @pytest.mark.regress
    @allure.title("id-10588 10.4.2.2 Добавление знания в справочник Группы знаний без заполнения обязательных полей")
    def test_adding_tag_without_filling_in_a_required_field(self, login, driver):
        tags_page = TagsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.check_adding_tag_without_filling_in_a_required_field()

    @testit.workItemIds(10589)
    @testit.displayName("10.4.2.2 Неуникальное значение поля при добавлении знания в справочник Группы знаний")
    @pytest.mark.regress
    @allure.title("id-10589 10.4.2.2 Неуникальное значение поля при добавлении знания в справочник Группы знаний")
    def test_adding_tag_with_non_unique_name(self, create_tag, login, driver):
        tags_page = TagsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.check_add_tag_not_unique_name(create_tag[0])

    @testit.workItemIds(10590)
    @testit.displayName("10.4.2.2 Превышение допустимого количества символов в полях при добавлении знания в справочник Группы знаний")
    @pytest.mark.regress
    @allure.title("id-10590 10.4.2.2 Превышение допустимого количества символов в полях при добавлении знания в справочник Группы знаний")
    def test_maximum_field_length_when_adding_the_tag(self, login, driver):
        tags_page = TagsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.press_add_tag_button()
        tags_page.check_drawer_fields_max_length()

    @testit.workItemIds(10594)
    @testit.displayName("10.4.2.3 Редактирование данных в справочнике Группы знаний с неуникальным значением")
    @pytest.mark.regress
    @allure.title("id-10594 10.4.2.3 Редактирование данных в справочнике Группы знаний с неуникальным значением")
    def test_editing_the_tag_with_non_unique_name(self, create_tag, login, driver):
        tags_page = TagsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.sort_tags()
        time.sleep(1)
        tags_page.redact_tag_by_name(create_tag[0])
        tags_page.check_redact_tag_no_unique_name(create_tag[1])
        error = tags_page.get_error()
        toast = tags_page.get_alert_message()
        assert toast == ['Группа уже добавлена'], "Нет сообщения"
        assert error == 'Укажите уникальноe название группы знаний', "Нет предупреждения"

    @testit.workItemIds(10595)
    @testit.displayName("10.4.2.3 Редактирование данных в справочнике Группы знаний без заполнения обязательного поля")
    @pytest.mark.regress
    @allure.title("id-10595 10.4.2.3 Редактирование данных в справочнике Группы знаний без заполнения обязательного поля")
    def test_editing_the_tag_without_filling_in_the_required_fields(self, create_tag, login, driver):
        tags_page = TagsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.sort_tags()
        time.sleep(1)
        tags_page.redact_tag_by_name(create_tag[0])
        tags_page.check_redact_tag_empty_field()

    @testit.workItemIds(10596)
    @testit.displayName("10.4.2.3 Редактирование данных в справочнике Группы знаний с превышением максимального количества символов")
    @pytest.mark.regress
    @allure.title(
        "id-10596 10.4.2.3 Редактирование данных в справочнике Группы знаний с превышением максимального количества символов")
    def test_maximum_field_length_when_editing_the_tag(self, create_tag, login, driver):
        tags_page = TagsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.sort_tags()
        time.sleep(1)
        tags_page.redact_tag_by_name(create_tag[0])
        tags_page.check_drawer_fields_max_length()

    @testit.workItemIds(10598)
    @testit.displayName("10.4.2.3 Отмена редактирования данных в справочнике Группы знаний")
    @pytest.mark.regress
    @allure.title("id-10598 10.4.2.3 Отмена редактирования данных в справочнике Группы знаний")
    def test_cancel_editing_the_tag(self, create_tag, login, driver):
        tags_page = TagsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.sort_tags()
        time.sleep(1)
        tags_page.redact_tag_by_name(create_tag[0])
        tags_page.check_cancel_editing_tag('AA Измененное имя')

    @testit.workItemIds(10599)
    @testit.displayName("10.4.2.4 Удаление неиспользуемых в профиле значений из справочника Группы знаний")
    @pytest.mark.regress
    @allure.title("id-10599 10.4.2.4 Удаление неиспользуемых в профиле значений из справочника Группы знаний")
    def test_delete_unused_in_the_profile_tag(self, create_tag_to_delete, login, driver):
        tags_page = TagsPage(driver)
        tags_page.go_to_tags_page()
        time.sleep(2)  # Нужно время на анимацию
        tags_page.sort_tags()
        time.sleep(1)
        assert tags_page.check_tag_on_tag_tab(create_tag_to_delete), "Группы знаний нет на вкладке группы знаний"
        tags_page.delete_tag(create_tag_to_delete)
        time.sleep(1)
        assert not tags_page.check_tag_on_tag_tab(create_tag_to_delete), "Группа знаний не удалилась"

