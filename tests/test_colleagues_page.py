import allure
import pytest
import testit

from pages.colleagues_page import ColleaguesPage
from pages.create_local_user_drawer_page import CreateLocalUserDrawerPage
from pages.user_page import UserPage


@allure.suite("Пользователи")
class TestUsersPage:

    @testit.workItemIds(981)
    @testit.displayName("4.9.1. Просмотр страницы коллег пользователя в разделе Коллеги")
    @pytest.mark.smoke
    @allure.title("id-981 4.9.1. Просмотр страницы коллег пользователя в разделе Коллеги")
    def test_view_colleagues_page(self, login, driver):
        colleagues_page = ColleaguesPage(driver)
        colleagues_page.go_colleagues_page()
        colleagues_page.check_colleagues_title()
        colleagues_page.check_colleagues_page_tabs()
        colleagues_page.check_search_field()
        colleagues_page.check_to_advanced_search_button()
        colleagues_page.check_subtitle()
        colleagues_page.check_setting_icon()
        colleagues_page.check_column_titles()
        colleagues_page.check_user_name_link()

    @testit.workItemIds(3184)
    @testit.displayName("4.17.Просмотр системы глазами пользователя")
    @pytest.mark.smoke
    @allure.title("id-3184 4.17.Просмотр системы глазами пользователя")
    def test_viewing_the_system_users_eyes(self, login, driver):
        colleagues_page = ColleaguesPage(driver)
        user_page = UserPage(driver)
        user_page.go_to_user_page()
        # Проверяем, что есть нужный пользователь
        if not user_page.check_user_is_not_in_table('АвтоСПроектом'):
            create_local_user_page = CreateLocalUserDrawerPage(driver)
            create_local_user_page.go_to_create_local_user_drawer()
            create_local_user_page.field_required_fields('AutoTester1', 'АвтоСПроектом', 'auto_testt@mail.rruu', 'yes')
        else:
            pass
        # Проводим тест
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        colleagues_page.check_watch_the_user_eyes()




