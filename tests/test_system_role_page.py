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
        system_role_page.check_create_system_role('Контролер')
        # Проверяем роль в дропдауне
        system_role_page.check_role_name_in_dropdown('Контролер')
        # Удаляем роль после теста
        system_role_page.delete_system_role('Контролер')


    @testit.workItemIds(3529)
    @testit.displayName("7.2.4 Проверка невозможности удаления системной роли 'Пользователь'")
    @pytest.mark.smoke
    @allure.title("id-3529 7.2.4 Проверка невозможности удаления системной роли 'Пользователь'")
    def test_checking_impossibility_deleting_system_role_user(self, login, driver):
        system_role_page = SystemRolePage(driver)
        system_role_page.go_to_system_roles_page()
        system_role_page.select_role_name_in_dropdown('Пользователь')
        system_role_page.check_delete_role_icon_is_disabled()
        assert system_role_page.get_tooltip_text_impossibility_deleting_system_role_user() == \
            'Системную роль "Пользователь" удалить нельзя.', \
            "Отсутствует тултип о невозможности удаления системной роли"
    