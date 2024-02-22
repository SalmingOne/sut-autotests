import allure
import pytest
import testit

from pages.user_profile_page import UserProfilePage


@allure.suite("Профиль пользователя")
class TestUserProfilePage:

    @testit.workItemIds(4158)
    @testit.displayName("10.2.1. Пустой ввод в обязательные для заполнения поля при редактировании таба Образование")
    @pytest.mark.regress
    @allure.title("id-4158 10.2.1. Пустой ввод в обязательные для заполнения поля при редактировании таба Образование")
    def test_blank_entry_on_education_tab(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        user_profile_page.go_to_education_tab()
        user_profile_page.press_redact_button()
        user_profile_page.press_add_icon_button()
        user_profile_page.press_save_button()
        alert_message = user_profile_page.get_alert_message()
        tab_color = user_profile_page.get_education_tab_color()
        errors = user_profile_page.get_mui_errors_text()
        assert alert_message == 'Не все поля были заполнены корректно на табе "Образование"', "Не появилось сообщение об ошибке"
        assert tab_color == 'rgba(255, 236, 229, 1)', "Цвет вкладки не красный"
        assert 'Поле обязательно' in errors, "Нет сообщений об обязательности поля"

    @testit.workItemIds(4159)
    @testit.displayName("10.2.1. Пустой ввод в обязательные для заполнения поля при редактировании таба Сертификаты")
    @pytest.mark.regress
    @allure.title("id-4159 10.2.1. Пустой ввод в обязательные для заполнения поля при редактировании таба Сертификаты")
    def test_blank_entry_on_certificate_tab(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        user_profile_page.go_to_certificate_tab()
        user_profile_page.press_redact_button()
        user_profile_page.press_add_icon_button()
        user_profile_page.press_save_button()
        alert_message = user_profile_page.get_alert_message()
        tab_color = user_profile_page.get_certificate_tab_color()
        errors = user_profile_page.get_mui_errors_text()
        assert alert_message == 'Не все поля были заполнены корректно на табе "Сертификаты"', "Не появилось сообщение об ошибке"
        assert tab_color == 'rgba(255, 236, 229, 1)', "Цвет вкладки не красный"
        assert 'Поле обязательно' in errors, "Нет сообщений об обязательности поля"

    @testit.workItemIds(4160)
    @testit.displayName("10.2.3. Пустой ввод в обязательные для заполнения поля при редактировании таба Опыт работы")
    @pytest.mark.regress
    @allure.title("id-4160 10.2.3. Пустой ввод в обязательные для заполнения поля при редактировании таба Опыт работы")
    def test_blank_entry_on_experience_tab(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        user_profile_page.go_to_experience_tab()
        user_profile_page.press_redact_button()
        user_profile_page.press_add_icon_button()
        user_profile_page.press_save_button()
        alert_message = user_profile_page.get_alert_message()
        tab_color = user_profile_page.get_experience_tab_color()
        errors = user_profile_page.get_mui_errors_text()

        assert alert_message == 'Не все поля были заполнены корректно на табе "Опыт работы"', "Не появилось сообщение об ошибке"
        assert tab_color == 'rgba(255, 236, 229, 1)', "Цвет вкладки не красный"
        assert 'Поле обязательно' in errors, "Нет сообщений об обязательности поля"

