import time

import allure
import pytest
import testit

from endpoints.skills_and_knowledge_endpoint import SkillsAndKnowledgeEndpoint
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

    @testit.workItemIds(10464)
    @testit.displayName("10.4.1.2 Добавление данных в справочник Навыки и знания")
    @pytest.mark.smoke
    @allure.title("id-10464 10.4.1.2 Добавление данных в справочник Навыки и знания")
    def test_adding_data_to_skills_and_knowledge_directory(self, login, driver):
        skills_and_knowledge_page = SkillsAndKnowledgePage(driver)
        skills_endpoint = SkillsAndKnowledgeEndpoint()
        skills_and_knowledge_page.go_to_skills_page()
        time.sleep(2)
        skills_and_knowledge_page.press_add_skill_button()
        skills_and_knowledge_page.check_drawer_fields()
        assert skills_and_knowledge_page.get_name_and_description_values() == ['AAA', 'AAA'], \
            "В полях не отображаются введенные данные"
        skills_and_knowledge_page.press_submit_button()
        assert skills_and_knowledge_page.check_skill_name_on_page('AAA'), \
            "Имя знания не отображается на странице справочника"
        skills_endpoint.delete_skills_and_knowledge_by_name_api('AAA')

    @testit.workItemIds(10481)
    @testit.displayName("10.4.1.2 (Чек-лист) Негативные проверки при добавлении данных в справочник Знания и навыки")
    @pytest.mark.regress
    @allure.title("id-10481 10.4.1.2 (Чек-лист) Негативные проверки при добавлении данных в справочник Знания и навыки")
    def test_negative_checks_when_adding_data_to_skills_and_knowledge_directory(self, create_skill, login, driver):
        skills_and_knowledge_page = SkillsAndKnowledgePage(driver)
        skills_and_knowledge_page.go_to_skills_page()
        time.sleep(2)
        skills_and_knowledge_page.press_add_skill_button()
        skills_and_knowledge_page.check_empty_mandatory_fields()
        skills_and_knowledge_page.press_add_skill_button()
        skills_and_knowledge_page.check_skill_same_name(create_skill['name'])
        skills_and_knowledge_page.press_add_skill_button()
        skills_and_knowledge_page.check_exceeded_characters_in_fields()

    @testit.workItemIds(10484)
    @testit.displayName("10.4.1.3 Редактирование данных в справочнике Знания и навыки")
    @pytest.mark.smoke
    @allure.title("id-10484 10.4.1.3 Редактирование данных в справочнике Знания и навыки")
    def test_editing_data_in_the_skills_and_knowledge_directory(self, create_skill, login, driver):
        skills_and_knowledge_page = SkillsAndKnowledgePage(driver)
        skills_and_knowledge_page.go_to_skills_page()
        time.sleep(2)
        skills_and_knowledge_page.open_skill_to_redact(create_skill['name'])
        before = skills_and_knowledge_page.get_name_and_description_values()
        skills_and_knowledge_page.check_redact_drawer_fields('Новое Имя', 'Новое Описание')
        after = skills_and_knowledge_page.get_name_and_description_values()
        skills_and_knowledge_page.press_submit_button()
        assert skills_and_knowledge_page.check_skill_name_on_page('Новое Имя'), "Новое имя знания не отображается в таблице"
        assert before != after, "Данные не изменились"
        assert 'Новое Имя' and 'Новое Описание' in after, "В полях не отображаются введенные данные"

    @testit.workItemIds(10558)
    @testit.displayName("10.4.1.3 (Чек-лист) Негативные проверки редактирования данных в справочнике Знания и навыки")
    @pytest.mark.regress
    @allure.title("id-10558 10.4.1.3 (Чек-лист) Негативные проверки редактирования данных в справочнике Знания и навыки")
    def test_negative_checks_when_editing_data_to_skills_and_knowledge_directory(self, create_skill, create_second_skill, login, driver):
        skills_and_knowledge_page = SkillsAndKnowledgePage(driver)
        skills_and_knowledge_page.go_to_skills_page()
        time.sleep(2)
        # Проверка дровера редактирования
        skills_and_knowledge_page.open_skill_to_redact(create_skill['name'])
        skills_and_knowledge_page.check_redact_drawer_fields('Новое Имя', 'Новое Описание')
        # Не заполнены обязательные поля
        skills_and_knowledge_page.clear_name_field()
        skills_and_knowledge_page.check_empty_mandatory_fields()
        # В поле “Название” введено не уникальное значение
        skills_and_knowledge_page.open_skill_to_redact(create_skill['name'])
        skills_and_knowledge_page.clear_name_field()
        skills_and_knowledge_page.check_skill_same_name(create_second_skill['name'])
        # Превышено количество допустимых символов
        skills_and_knowledge_page.open_skill_to_redact(create_skill['name'])
        skills_and_knowledge_page.check_exceeded_characters_in_fields()

    @testit.workItemIds(10597)
    @testit.displayName("10.4.1.3 Отмена редактирования данных в справочнике Знания и навыки")
    @pytest.mark.regress
    @allure.title("id-10597 10.4.1.3 Отмена редактирования данных в справочнике Знания и навыки")
    def test_cancel_editing_data_to_skills_and_knowledge_directory(self, create_skill, login, driver):
        skills_and_knowledge_page = SkillsAndKnowledgePage(driver)
        skills_and_knowledge_page.go_to_skills_page()
        time.sleep(2)
        skills_and_knowledge_page.open_skill_to_redact(create_skill['name'])
        before = skills_and_knowledge_page.get_name_and_description_values()
        skills_and_knowledge_page.check_redact_drawer_fields('Новое Имя', 'Новое Описание')
        after = skills_and_knowledge_page.get_name_and_description_values()
        skills_and_knowledge_page.press_break_button()
        skills_and_knowledge_page.open_skill_to_redact(create_skill['name'])
        after_break = skills_and_knowledge_page.get_name_and_description_values()
        assert before != after, "Новые данные не отображаются в полях"
        assert before == after_break, "Данные в полях изменились после отмены редактирования"

    @testit.workItemIds(10549)
    @testit.displayName("10.4.1.4 Удаление данных из справочника Знания и навыки")
    @pytest.mark.regress
    @allure.title("id-10549 10.4.1.4 Удаление данных из справочника Знания и навыки")
    def test_removing_data_from_skills_and_knowledge_directory(self, create_skill_to_delete, login, driver):
        skills_and_knowledge_page = SkillsAndKnowledgePage(driver)
        skills_and_knowledge_page.go_to_skills_page()
        time.sleep(2)
        skills_and_knowledge_page.press_delete_skill_button(create_skill_to_delete['name'])
        skills_and_knowledge_page.check_delete_modal_window()
        skills_and_knowledge_page.press_submit_button()
        assert skills_and_knowledge_page.get_message() == f'Знание или навык {create_skill_to_delete['name']} удален', \
            "Не появилось сообщение о удалении знания/навыка"
        time.sleep(1)
        assert not skills_and_knowledge_page.check_skill_name_on_page(create_skill_to_delete['name']), \
            "Знание/навык отображается в таблице после удаления"
