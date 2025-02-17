import time

import allure
import pytest
import testit

from pages.create_local_user_drawer_page import CreateLocalUserDrawerPage
from pages.user_page import UserPage


@allure.suite("Дровер создания нового локального пользователя")
class TestCreateLocalUser:

    @testit.workItemIds(280)
    @testit.displayName("4.2 Содержание дровера Добавление нового пользователя при создании локального пользователя")
    @pytest.mark.regress
    @allure.title("id-280 4.2 Содержание дровера Добавление нового пользователя при создании локального пользователя")
    def test_create_local_user_drawer(self, login, driver):
        create_local_user_page = CreateLocalUserDrawerPage(driver)
        create_local_user_page.go_to_create_local_user_drawer()
        # Проверяем вкладку Личные данные
        create_local_user_page.check_names_text()
        create_local_user_page.check_placeholder_text()
        create_local_user_page.check_hour_pay_checkbox()
        # Проверяем вкладку Контакты
        create_local_user_page.go_to_tab_contacts()
        create_local_user_page.check_names_on_contacts_text()
        # Общие кнопки
        create_local_user_page.check_clear_icon_button()
        create_local_user_page.check_save_button()
        create_local_user_page.check_abort_button()

    @testit.workItemIds(288)
    @testit.displayName("4.2 Отмена добавления нового пользователя")
    @pytest.mark.regress
    @allure.title("id-288 4.2 Отмена добавления нового пользователя")
    def test_cansel_adding_new_user(self, login, driver):
        create_local_user_page = CreateLocalUserDrawerPage(driver)
        create_local_user_page.go_to_create_local_user_drawer()
        create_local_user_page.field_required_fields('AutoUser', 'Автоматов', 'auto@mail.ruru', 'no')
        user_page = UserPage(driver)
        assert not user_page.check_user_is_not_in_table('Автоматов'), "Пользователь есть в таблице"

    @testit.workItemIds(289)
    @testit.displayName("Совпадение логинов пользователей")
    @pytest.mark.regress
    @allure.title("id-289 Совпадение логинов пользователей")
    def test_matching_user_logins(self, create_work_user, login, driver):
        user_page = UserPage(driver)
        create_local_user_page = CreateLocalUserDrawerPage(driver)
        user_page.go_to_user_page()
        create_local_user_page.go_to_create_local_user_drawer()
        create_local_user_page.field_required_fields('AutoTester1', 'Автоматов', 'auto@mail.ruru', 'yes')
        assert create_local_user_page.check_massage() == 'Пользователь с таким логином/почтой уже добавлен в систему', "Не появилось сообщение о совпадении логинов"
        time.sleep(10)  # Следующий тест падает каждый прогон. Возможно это ожидание поможет
