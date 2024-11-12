import allure
import pytest
import testit

from pages.system_role_page import SystemRolePage


@allure.suite("Системные роли")
class TestSystemRolePage:

    @testit.workItemIds(3503)
    @testit.displayName("7.2.2 Создание системной роли")
    @pytest.mark.smoke
    @allure.title("id-3503 7.2.2 Создание системной роли")
    def test_create_new_system_role(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        # Создаем роль
        system_role_page.create_system_role('Контролер')
        system_role_page.press_submit_button()
        # Проверяем роль в дропдауне
        system_role_page.check_role_name_in_dropdown('Контролер')
        # Удаляем роль после теста
        system_role_page.delete_system_role('Контролер')


    @testit.workItemIds(3529)
    @testit.displayName("7.2.4 Проверка невозможности удаления системной роли 'Пользователь'")
    @pytest.mark.regress
    @allure.title("id-3529 7.2.4 Проверка невозможности удаления системной роли 'Пользователь'")
    def test_checking_impossibility_deleting_system_role_user(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown('Пользователь')
        system_role_page.check_delete_role_icon_is_disabled()
        assert system_role_page.get_tooltip_text_impossibility_deleting_system_role_user() == \
            'Системную роль "Пользователь" удалить нельзя.', \
            "Отсутствует тултип о невозможности удаления системной роли"
        
    @testit.workItemIds(3504)
    @testit.displayName("7.2.2 (Чек-лист) Проверка ограничений при создании системной роли")
    @pytest.mark.regress
    @allure.title("id-3504 7.2.2 (Чек-лист) Проверка ограничений при создании системной роли")
    def test_checking_restrictions_when_creating_system_role(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.press_add_system_role_button()
        # Проверка на обязательные поля
        system_role_page.check_required_fields()
        # Проверка на обязательность тэгов
        system_role_page.check_required_tags('Контролер')
        # Проверка на уникальность названия системной роли
        system_role_page.check_uniqueness_system_role_name('Пользователь')
        # Проверка на превышение символов в названии системной роли
        system_role_page.check_char_limit_system_role_name()

    @testit.workItemIds(3520)
    @testit.displayName("7.2.2 Отмена создания системной роли")
    @pytest.mark.regress
    @allure.title("id-3520 7.2.2 Отмена создания системной роли")
    def test_cancel_create_new_system_role(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.create_system_role('Контролер')
        system_role_page.press_abort_button()
        system_role_page.check_role_name_not_in_dropdown('Контролер')
    