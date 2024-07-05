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
        assert skills_page.check_skill_name_on_page('AAABBB'), "В справочнике Знания не сохранились изменения"
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
        skills_page.create_skill('AAAДобавленное знание', create_tag[0])
        assert skills_page.check_skill_name_on_page('AAAДобавленное знание'), "В справочнике Знания не сохранились изменения"
        skills_page.check_skill_name_on_tag_tab('AAAДобавленное знание')

        skills_endpoint.delete_skill_by_name_api('AAAДобавленное знание')

    @testit.workItemIds(10591)
    @testit.displayName("10.4.1.2 Добавление данных в справочник Знания с несколькими группами знаний")
    @pytest.mark.regress
    @allure.title("id-10591 10.4.1.2 Добавление данных в справочник Знания с несколькими группами знаний")
    def test_adding_the_two_knowledge_directory(self, create_tag, login, driver):
        skills_page = SkillsPage(driver)
        skills_endpoint = SkillsEndpoint()
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        len_tags = skills_page.create_skill('AAAДобавленное знание', create_tag[0], create_tag[1])
        assert skills_page.check_skill_name_on_page('AAAДобавленное знание'), "В справочнике Знания не сохранились изменения"
        skills_page.check_skill_name_on_tag_tab('AAAДобавленное знание')
        skills_endpoint.delete_skill_by_name_api('AAAДобавленное знание')
        assert len_tags == 2, "В поле не отобразилось несколько групп знаний"

    @testit.workItemIds(10467)
    @testit.displayName("10.4.1.2 Отмена добавления знания в справочник Знания")
    @pytest.mark.regress
    @allure.title("id-10467 10.4.1.2 Отмена добавления знания в справочник Знания")
    def test_cancel_adding_the_skill(self, login, driver):
        skills_page = SkillsPage(driver)
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        skills_page.check_cancel_add_skill('AAAДобавленное знание')
        assert not skills_page.check_skill_name_on_page('AAAДобавленное знание'), "Знание сохранилось"

    @testit.workItemIds(10481)
    @testit.displayName("10.4.1.2 Добавление знания в справочник Знания без заполнения обязательных полей")
    @pytest.mark.regress
    @allure.title("id-10481 10.4.1.2 Добавление знания в справочник Знания без заполнения обязательных полей")
    def test_adding_skill_without_filling_in_the_required_fields(self, login, driver):
        skills_page = SkillsPage(driver)
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        skills_page.check_empty_filling_in_the_required_fields()

    @testit.workItemIds(10548)
    @testit.displayName("10.4.1.2 Неуникальное значение поля при добавлении знания в справочник Знания")
    @pytest.mark.regress
    @allure.title("id-10548 10.4.1.2 Неуникальное значение поля при добавлении знания в справочник Знания")
    def test_non_unique_field_value_when_adding_skill(self, create_skill, login, driver):
        skills_page = SkillsPage(driver)
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        skills_page.check_add_skill_not_unique_name(create_skill)

    @testit.workItemIds(10482)
    @testit.displayName("10.4.1.2 Превышение допустимого количества символов в полях при добавлении знания в справочник Знания")
    @pytest.mark.regress
    @allure.title("id-10482 10.4.1.2 Превышение допустимого количества символов в полях при добавлении знания в справочник Знания")
    def test_maximum_field_length_when_adding_skill(self, login, driver):
        skills_page = SkillsPage(driver)
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        skills_page.check_drawer_fields_max_length()

    @testit.workItemIds(10558)
    @testit.displayName("10.4.1.3 Редактирование данных в справочнике Знания с неуникальным значением знания")
    @pytest.mark.regress
    @allure.title("id-10558 10.4.1.3 Редактирование данных в справочнике Знания с неуникальным значением знания")
    def test_editing_skill_non_unique_knowledge_value(self, create_skill, create_second_skill, login, driver):
        skills_page = SkillsPage(driver)
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        skills_page.redact_skill_by_name(create_skill)
        skills_page.change_the_skill(create_second_skill)
        assert skills_page.get_error() == 'Укажите уникальноe название знания',\
            "Нет сообщения о не уникальности названия знания"

    @testit.workItemIds(10559)
    @testit.displayName("10.4.1.3 Редактирование данных в справочнике Знания  без заполнения обязательного поля")
    @pytest.mark.regress
    @allure.title("id-10559 10.4.1.3 Редактирование данных в справочнике Знания  без заполнения обязательного поля")
    def test_editing_skill_without_filling_in_a_required_field(self, create_skill, login, driver):
        skills_page = SkillsPage(driver)
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        skills_page.redact_skill_by_name(create_skill)
        skills_page.check_redact_with_empty_fields()
        assert skills_page.get_error() == 'Поле обязательно', "Не отображается сообщение с предупреждением"

    @testit.workItemIds(10560)
    @testit.displayName(
        "10.4.1.3 Редактирование данных в справочнике Знания с превышением максимального количества символов")
    @pytest.mark.regress
    @allure.title(
        "id-10560 10.4.1.3 Редактирование данных в справочнике Знания с превышением максимального количества символов")
    def test_maximum_field_length_when_editing_skill(self, create_skill, login, driver):
        skills_page = SkillsPage(driver)
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        skills_page.redact_skill_by_name(create_skill)
        skills_page.check_drawer_fields_max_length_when_redact()

    @testit.workItemIds(10597)
    @testit.displayName("10.4.1.3 Отмена редактирования данных в справочнике Знания")
    @pytest.mark.regress
    @allure.title("id-10597 10.4.1.3 Отмена редактирования данных в справочнике Знания")
    def test_cancel_editing_the_skill(self, create_skill, login, driver):
        skills_page = SkillsPage(driver)
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        skills_page.redact_skill_by_name(create_skill)
        skills_page.check_cancel_redact_skill('АА Отредактированное знание')
        assert not skills_page.check_skill_name_on_page('АА Отредактированное знание'), "Знание изменилось"

    @testit.workItemIds(10549)
    @testit.displayName("10.4.1.4 Удаление неиспользуемых в профиле значений из справочника Знания")
    @pytest.mark.regress
    @allure.title("id-10549 10.4.1.4 Удаление неиспользуемых в профиле значений из справочника Знания")
    def test_deleting_unused_in_the_profile_skill(self, create_skill_to_delete, login, driver):
        skills_page = SkillsPage(driver)
        skills_page.go_to_skills_page()
        skills_page.sort_skills()
        assert skills_page.check_skill_name_on_page(create_skill_to_delete), "Знания нет на странице"
        skills_page.delete_skill_by_name(create_skill_to_delete)
        time.sleep(1)
        assert not skills_page.check_skill_name_on_page(create_skill_to_delete), "Знание не удалилось"
