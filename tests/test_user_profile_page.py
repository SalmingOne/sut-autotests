import time

import allure
import pytest
import testit

from data.data import USER_NAME
from endpoints.project_endpoint import ProjectEndpoint
from pages.advanced_search_page import AdvancedSearchPage
from pages.colleagues_page import ColleaguesPage
from pages.schedule_page import SchedulePage
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
        time.sleep(5)
        user_profile_page.go_to_education_tab()
        # Удаляем диплом если есть
        if user_profile_page.check_diploma_title():
            user_profile_page.press_redact_button()
            time.sleep(1)
            user_profile_page.press_delete_icon()
            user_profile_page.press_save_button()
            user_profile_page.go_to_education_tab()
        else:
            pass
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_add_icon_button()
        user_profile_page.press_save_button()
        user_profile_page.go_to_education_tab()
        alert_messages = user_profile_page.get_alert_message()
        errors = user_profile_page.get_mui_errors_text()
        tab_color = user_profile_page.get_education_tab_color()
        assert 'На табе "Образование" не все поля были заполнены корректно' in alert_messages, "Не появилось сообщение об ошибке"
        assert tab_color == 'rgba(211, 47, 47, 1)', "Цвет вкладки не красный"
        assert 'Поле обязательно' in errors, "Нет сообщений об обязательности поля"

    @testit.workItemIds(4159)
    @testit.displayName("10.2.1. Пустой ввод в обязательные для заполнения поля при редактировании таба Сертификаты")
    @pytest.mark.regress
    @allure.title("id-4159 10.2.1. Пустой ввод в обязательные для заполнения поля при редактировании таба Сертификаты")
    def test_blank_entry_on_certificate_tab(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_certificate_tab()
        time.sleep(1)
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_add_icon_button()
        user_profile_page.press_save_button()
        time.sleep(1)
        user_profile_page.go_to_certificate_tab()
        alert_message = user_profile_page.get_alert_message()
        time.sleep(1)
        errors = user_profile_page.get_mui_errors_text()
        tab_color = user_profile_page.get_certificate_tab_color()
        assert 'На табе "Сертификаты" не все поля были заполнены корректно' in alert_message, "Не появилось сообщение об ошибке"
        assert tab_color == 'rgba(211, 47, 47, 1)', "Цвет вкладки не красный"
        assert 'Поле обязательно' in errors, "Нет сообщений об обязательности поля"

    @testit.workItemIds(4160)
    @testit.displayName("10.2.3. Пустой ввод в обязательные для заполнения поля при редактировании таба Опыт работы")
    @pytest.mark.regress
    @allure.title("id-4160 10.2.3. Пустой ввод в обязательные для заполнения поля при редактировании таба Опыт работы")
    def test_blank_entry_on_experience_tab(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_experience_tab()
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_add_icon_button()
        user_profile_page.press_save_button()
        time.sleep(1)
        user_profile_page.go_to_experience_tab()
        alert_message = user_profile_page.get_alert_message()
        tab_color = user_profile_page.get_experience_tab_color()
        errors = user_profile_page.get_mui_errors_text()

        assert 'На табе "Опыт работы" не все поля были заполнены корректно' in alert_message, "Не появилось сообщение об ошибке"
        assert tab_color == 'rgba(211, 47, 47, 1)', "Цвет вкладки не красный"
        assert 'Поле обязательно' in errors, "Нет сообщений об обязательности поля"

    @testit.workItemIds(3196)
    @testit.displayName("10.6.1.4. Содержание страницы Создания резюме")
    @pytest.mark.smoke
    @allure.title("id-3196 10.6.1.4. Содержание страницы Создания резюме")
    def test_contents_of_the_resume_creation_page(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_name = user_profile_page.get_title()
        start_work = user_profile_page.get_start_work_date()
        user_profile_page.go_to_resume_tab()
        user_profile_page.press_create_resume_button()
        time.sleep(2)
        user_profile_page.check_disable_save_button()
        user_profile_page.check_default_values(user_name, start_work)
        user_profile_page.check_max_symbol()
        user_profile_page.check_post_tooltip()
        user_profile_page.check_direction_tooltip()
        user_profile_page.check_ready_to_work_dropdown()
        user_profile_page.check_date_pikers()
        user_profile_page.check_delete_icon()
        user_profile_page.check_wysiwyg_titles()
        user_profile_page.check_wysiwyg_functions_titles()
        user_profile_page.check_break_button()
        user_profile_page.current_employer_checkbox()

    @testit.workItemIds(3201)
    @testit.displayName("10.6.1.4. Сохранение резюме")
    @pytest.mark.smoke
    @allure.title("id-3201 10.6.1.4. Сохранение резюме")
    def test_saving_your_resume(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(1)
        user_profile_page.go_to_resume_tab()
        user_profile_page.press_create_resume_button()
        time.sleep(1)
        resume_title = user_profile_page.save_resume()
        time.sleep(2)
        message = user_profile_page.get_alert_message()
        driver.refresh()
        titles = user_profile_page.get_names_resume_on_tab()
        kebab_menu_items = user_profile_page.delete_resume(resume_title)

        assert message == ['Резюме создано'], 'Не появилось сообщение о создании резюме'
        assert resume_title in titles, 'Названия резюме нет в таблице'
        assert kebab_menu_items == ['Редактирование', 'Просмотр резюме', 'Копировать', 'Удалить'], \
            'Созданное резюме не доступно для редактирования, удаления, скачивания и копирования'

    @testit.workItemIds(1102)
    @testit.displayName("10.2.2. Отмена внесенных изменений в личном профиле сотрудника")
    @pytest.mark.regress
    @allure.title("id-1102 10.2.2. Отмена внесенных изменений в личном профиле сотрудника")
    def test_cancel_changes_to_personal_profile(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()

        before = user_profile_page.get_children_text()
        user_profile_page.press_redact_button()
        user_profile_page.change_children_text('Измененный текст')

        after = user_profile_page.get_children_text()
        user_profile_page.check_cansel_changes()

        after_cansel = user_profile_page.get_children_text()
        assert before != after, 'Значение в поле не изменилось после редактирования'
        assert before == after_cansel, 'Значение в поле изменилось после отмены редактирования'

    @testit.workItemIds(4162)
    @testit.displayName("10.2.1. Переход на другой таб, если не заполнены обязательные поля")
    @pytest.mark.regress
    @allure.title("id-4162 10.2.1. Переход на другой таб, если не заполнены обязательные поля")
    def test_move_to_another_tab_if_required_fields_are_not_filled_in(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_education_tab()
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_add_icon_button()
        user_profile_page.go_to_user_profile_tab()
        have_start_work_field = user_profile_page.check_start_work_is_visible()
        assert have_start_work_field, "Не произошел переход на другой таб"

    @testit.workItemIds(1146)
    @testit.displayName("10.2.2. Редактирование раздела Дополнительная информация в личном профиле сотрудника")
    @pytest.mark.regress
    @allure.title("id-1146 10.2.2. Редактирование раздела Дополнительная информация в личном профиле сотрудника")
    def test_editing_the_additional_information_section_in_personal_profile(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(3)
        before = user_profile_page.get_additional_information()
        user_profile_page.press_redact_button()
        time.sleep(2)
        user_profile_page.input_additional_information()
        user_profile_page.press_save_button()
        time.sleep(2)
        after = user_profile_page.get_additional_information()
        assert before[0] != after[0], 'Семейное положение не изменилось'
        assert before[1] != after[1], 'Информация о детях не изменилась'
        assert before[2] != after[2], 'Дата рождения не изменилась'

    @testit.workItemIds(1134)
    @testit.displayName("10.2.2. Добавление файла диплома в разделе Образование в личном профиле сотрудника")
    @pytest.mark.regress
    @allure.title("id-1134 10.2.2. Добавление файла диплома в разделе Образование в личном профиле сотрудника")
    def test_adding_a_diploma_file_in_the_education_section(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_education_tab()
        time.sleep(1)
        # Создаем диплом если его нет
        if user_profile_page.check_diploma_title():
            pass
        else:
            user_profile_page.add_simple_diploma()
            time.sleep(1)
            user_profile_page.go_to_education_tab()
        user_profile_page.press_redact_button()
        time.sleep(1)
        # Проверяем поля раздела образование
        user_profile_page.check_education_form()
        # Добавляем диплом
        user_profile_page.add_file('диплом.docx', 'Диплом')
        user_profile_page.check_add_file('диплом.docx')
        time.sleep(1)
        user_profile_page.press_save_button()
        time.sleep(1)
        # Проверяем сообщение
        message = user_profile_page.get_alert_message()
        user_profile_page.check_download_file_icon()
        # Удаляем файл с сайта
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.delete_file_from_site()
        user_profile_page.press_save_button()
        user_profile_page.delete_file('диплом.docx')
        assert 'Файл сохранен' in message, "Не появилось сообщение файл сохранен"

    @testit.workItemIds(1143)
    @testit.displayName("10.2.2. Добавление сертификата в разделе Сертификаты в личном профиле сотрудника")
    @pytest.mark.regress
    @allure.title("id-1143 10.2.2. Добавление сертификата в разделе Сертификаты в личном профиле сотрудника")
    def test_adding_a_certificate_file_in_the_certificate_tab(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_certificate_tab()
        if user_profile_page.check_certificate_title():
            user_profile_page.press_redact_button()
            time.sleep(1)
            user_profile_page.press_delete_icon()
            user_profile_page.press_save_button()
        else:
            pass

        user_profile_page.press_redact_button()
        time.sleep(1)
        # Добавляем сертификат
        user_profile_page.press_add_icon_button()
        time.sleep(1)
        user_profile_page.check_and_field_certificate_form()
        user_profile_page.add_file('сертификат.pdf', 'Сертификат FAANG')
        user_profile_page.check_add_file('сертификат.pdf')
        user_profile_page.press_save_button()

        time.sleep(1)
        # Проверяем сообщение
        message = user_profile_page.get_alert_message()
        user_profile_page.go_to_certificate_tab()
        time.sleep(1)
        user_profile_page.check_download_file_icon()
        # Удаляем сертификат
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()
        user_profile_page.delete_file('сертификат.pdf')
        assert 'Файл сохранен' in message, "Не появилось сообщение файл сохранен"

    @testit.workItemIds(2106)
    @testit.displayName("10.2.2. Редактирование раздела Информация о сотруднике в чужом профиле")
    @pytest.mark.regress
    @allure.title("id-2106 10.2.2. Редактирование раздела Информация о сотруднике в чужом профиле")
    def test_editing_the_employee_information_section_in_someone_else_profile(self, create_work_user, login, driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        # Проводим тест
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        time.sleep(1)
        colleagues_page.check_user_name_link()

        user_name = user_profile_page.get_title()
        before = user_profile_page.get_additional_information()
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.input_additional_information()
        user_profile_page.press_save_button()
        time.sleep(1)
        after = user_profile_page.get_additional_information()
        assert 'АвтоСПроектом' in user_name, "Не произошел переход на страницу пользователя"
        assert before[0] != after[0], 'Семейное положение не изменилось'
        assert before[1] != after[1], 'Информация о детях не изменилась'
        assert before[2] != after[2], 'Дата рождения не изменилась'

    @testit.workItemIds(2099)
    @testit.displayName("10.2.2. Добавление карточки нового диплома в разделе Образование в чужом профиле")
    @pytest.mark.regress
    @allure.title("id-2099 10.2.2. Добавление карточки нового диплома в разделе Образование в чужом профиле")
    def test_adding_a_diploma_card_in_the_education_section_in_someone_else_profile(self, create_work_user, login,
                                                                                    driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        colleagues_page.go_to_watch_the_user_eyes()
        time.sleep(3)  
        user_profile_page.go_to_user_profile()
        time.sleep(3)        
        user_name = user_profile_page.get_title()
        user_profile_page.go_to_education_tab()
        # Удаляем диплом если есть
        if user_profile_page.check_diploma_title():
            user_profile_page.press_redact_button()
            time.sleep(1)
            user_profile_page.press_delete_icon()
            user_profile_page.press_save_button()
        else:
            pass
        # Добавляем диплом
        user_profile_page.add_simple_diploma()
        time.sleep(1)
        # Удаляем диплом после теста
        user_profile_page.go_to_education_tab()
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()

        assert 'АвтоСПроектом' in user_name, "Не произошел переход на страницу пользователя"

    @testit.workItemIds(2101)
    @testit.displayName("10.2.2. Добавление файла диплома в разделе Образование в чужом профиле")
    @pytest.mark.regress
    @allure.title("id-2101 10.2.2. Добавление файла диплома в разделе Образование в чужом профиле")
    def test_adding_a_diploma_file_in_the_education_section_in_someone_else_profile(self, create_work_user, login,
                                                                                    driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        # Проводим тест
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        colleagues_page.go_to_watch_the_user_eyes()
        time.sleep(3)  
        user_profile_page.go_to_user_profile()
        time.sleep(3)        
        user_name = user_profile_page.get_title()
        user_profile_page.go_to_education_tab()
        # Создаем диплом если его нет
        if user_profile_page.check_diploma_title():
            pass
        else:
            user_profile_page.add_simple_diploma()
            time.sleep(2)
            user_profile_page.go_to_education_tab()
        user_profile_page.press_redact_button()
        time.sleep(1)
        # Добавляем диплом
        user_profile_page.add_file('диплом.docx', 'Диплом')
        user_profile_page.check_add_file('диплом.docx')
        time.sleep(1)
        user_profile_page.press_save_button()
        time.sleep(1)
        # Проверяем сообщение
        message = user_profile_page.get_alert_message()
        time.sleep(1)
        user_profile_page.check_download_file_icon()
        # Удаляем файл с сайта
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.delete_file_from_site()
        user_profile_page.press_save_button()
        user_profile_page.delete_file('диплом.docx')

        assert 'Файл сохранен' in message, "Не появилось сообщение файл сохранен"
        assert 'АвтоСПроектом' in user_name, "Не произошел переход на страницу пользователя"

    @testit.workItemIds(2102)
    @testit.displayName("10.2.2. Удаление карточки диплома в разделе Образование в чужом профиле")
    @pytest.mark.regress
    @allure.title("id-2102 10.2.2. Удаление карточки диплома в разделе Образование в чужом профиле")
    def test_delete_a_diploma_cart_from_the_education_section_in_someone_else_profile(self, create_work_user, login,
                                                                                      driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        time.sleep(1)
        colleagues_page.check_user_name_link()
        user_name = user_profile_page.get_title()
        user_profile_page.go_to_education_tab()
        # Создаем диплом если его нет
        if user_profile_page.check_diploma_title():
            pass
        else:
            user_profile_page.add_simple_diploma()
            time.sleep(1)
            user_profile_page.go_to_education_tab()
        user_profile_page.press_redact_button()
        # Удаляем диплом
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()
        time.sleep(1)
        assert not user_profile_page.check_diploma_title(), "Карточка диплома не удалилась "
        assert 'АвтоСПроектом' in user_name, "Не произошел переход на страницу пользователя"

    @testit.workItemIds(2103)
    @testit.displayName("10.2.2. Добавление сертификата в разделе Сертификаты в чужом профиле")
    @pytest.mark.regress
    @allure.title("id-2103 10.2.2. Добавление сертификата в разделе Сертификаты в чужом профиле")
    def test_adding_a_certificate_file_in_the_certificate_tab_in_someone_else_profile(self, create_work_user, login,
                                                                                      driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        time.sleep(1)
        colleagues_page.check_user_name_link()
        user_name = user_profile_page.get_title()
        user_profile_page.go_to_certificate_tab()
        if user_profile_page.check_certificate_title():
            user_profile_page.press_redact_button()
            time.sleep(1)
            user_profile_page.press_delete_icon()
            user_profile_page.press_save_button()
        else:
            pass
        user_profile_page.press_redact_button()
        time.sleep(1)
        # Добавляем сертификат
        user_profile_page.press_add_icon_button()
        time.sleep(1)
        user_profile_page.check_and_field_certificate_form()
        user_profile_page.add_file('сертификат.pdf', 'Сертификат FAANG')
        user_profile_page.check_add_file('сертификат.pdf')
        user_profile_page.press_save_button()
        time.sleep(1)
        # Проверяем сообщение
        message = user_profile_page.get_alert_message()
        user_profile_page.go_to_certificate_tab()
        time.sleep(1)
        user_profile_page.check_download_file_icon()
        # Удаляем сертификат
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()
        user_profile_page.delete_file('сертификат.pdf')

        assert 'Файл сохранен' in message, "Не появилось сообщение файл сохранен"
        assert 'АвтоСПроектом' in user_name, "Не произошел переход на страницу пользователя"

    @testit.workItemIds(11620)
    @testit.displayName("10.2.2. Удаление карточки с сертификатом в чужом профиле")
    @pytest.mark.regress
    @allure.title("id-11620 10.2.2. Удаление карточки с сертификатом в чужом профиле")
    def test_deleting_a_certificate_in_someone_else_profile(self, create_work_user, login, driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        colleagues_page.go_to_watch_the_user_eyes()
        time.sleep(3)
        user_profile_page.go_to_user_profile()
        time.sleep(3)        
        user_name = user_profile_page.get_title()
        time.sleep(3)
        user_profile_page.go_to_certificate_tab()
        # Если нет сертификата создаем его
        if user_profile_page.check_certificate_title():
            pass
        else:
            user_profile_page.press_redact_button()
            user_profile_page.press_add_icon_button()
            time.sleep(1)
            user_profile_page.check_and_field_certificate_form()
            user_profile_page.press_save_button()
        # Удаляем сертификат
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()

        assert not user_profile_page.check_certificate_title()
        assert 'АвтоСПроектом' in user_name, "Не произошел переход на страницу пользователя"

    @testit.workItemIds(2095)
    @testit.displayName("10.2.2. Отмена внесенных изменений в чужом профиле")
    @pytest.mark.regress
    @allure.title("id-2095 10.2.2. Отмена внесенных изменений в чужом профиле")
    def test_undoing_changes_made_to_someone_else_profile(self, create_work_user, login, driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        time.sleep(1)
        colleagues_page.check_user_name_link()
        user_name = user_profile_page.get_title()
        # Получаем значения до
        email_before = user_profile_page.get_email_text()
        phone_before = user_profile_page.get_phone_text()
        # Редактируем телефон и адрес почты
        user_profile_page.press_redact_button()
        user_profile_page.change_email_text('test_changes@webbee.ruu')
        user_profile_page.change_phone_text('+55555555555')
        phone_in = user_profile_page.get_phone_text_on_redact()
        user_profile_page.check_cansel_changes()
        # Получаем значения после отмены
        email_after = user_profile_page.get_email_text()
        phone_after = user_profile_page.get_phone_text()
        assert email_before == email_after, "Адрес изменился"
        assert phone_before == phone_after, "Телефон изменился"
        assert phone_in == '+55555555555', "В поле номер телефона не отображается введенное значение"
        assert 'АвтоСПроектом' in user_name, "Не произошел переход на страницу пользователя"

    @testit.workItemIds(1935)
    @testit.displayName("10.2.3. Добавление проекта в разделе Опыт работы в чужом профиле")
    @pytest.mark.regress
    @allure.title("id-1935 10.2.3. Добавление проекта в разделе Опыт работы в чужом профиле")
    def test_adding_a_project_in_the_work_experience_section_someone_else_profile(self, login, project_with_two_resources, create_filial, driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        time.sleep(2)
        colleagues_page.check_user_name_link()
        time.sleep(6)
        user_name = user_profile_page.get_title()
        user_profile_page.go_to_experience_tab()
        time.sleep(1)
        if user_profile_page.check_experience_title():
            user_profile_page.press_redact_button()
            time.sleep(2)
            user_profile_page.press_delete_icon()
            user_profile_page.press_save_button()
        else:
            pass
        # Проверяем создание с выбором работодателя
        user_profile_page.check_work_experience_form()
        assert user_profile_page.check_experience_title(), "Карточка проекта не добавлена"

        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()
        # Проверяем создание с добавлением работодателя
        user_profile_page.field_work_experience_form_with_new_employer()
        assert user_profile_page.check_experience_title(), "Карточка проекта не добавлена"

        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()
        time.sleep(0.2)
        assert 'АвтоСПроектом' in user_name, "Не произошел переход на страницу пользователя"

    @testit.workItemIds(2104)
    @testit.displayName("10.2.3. Удаление карточки проекта в разделе Опыт работы в чужом профиле")
    @pytest.mark.regress
    @allure.title("id-2104 10.2.3. Удаление карточки проекта в разделе Опыт работы в чужом профиле")
    def test_deleting_a_project_in_the_work_experience_section_someone_else_profile(self, login, create_work_user,
                                                                                    create_filial, driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        time.sleep(1)
        colleagues_page.check_user_name_link()
        time.sleep(4)
        user_name = user_profile_page.get_title()
        user_profile_page.go_to_experience_tab()
        time.sleep(1)
        # Создаем карточку проекта если нет
        if user_profile_page.check_experience_title():
            pass
        else:
            user_profile_page.field_work_experience_form_with_new_employer()
        # Удаляем карточку проекта
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()
        time.sleep(0.2)
        # Проверяем удаление карточки
        assert not user_profile_page.check_experience_title(), "Карточка проекта не удалилась"
        assert 'АвтоСПроектом' in user_name, "Не произошел переход на страницу пользователя"

    @testit.workItemIds(3200)
    @testit.displayName("10.6.1.4. Удаление блока с опытом работы")
    @pytest.mark.regress
    @allure.title("id-3200 10.6.1.4. Удаление блока с опытом работы")
    def test_delete_a_block_with_work_experience_in_resume(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        user_profile_page.press_create_resume_button()
        time.sleep(1)
        user_profile_page.check_delete_block_experience_in_resume()

    @testit.workItemIds(3241)
    @testit.displayName("10.6.1.4. Неуникальное название резюме")
    @pytest.mark.regress
    @allure.title("id-3241 10.6.1.4. Неуникальное название резюме")
    def test_create_non_unique_resume_name(self, create_resume, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        user_profile_page.press_create_resume_button()
        error = user_profile_page.check_resume_with_non_unique_name(create_resume)
        assert error == 'Название резюме должно быть уникальным', "Не отображается сообщение об неуникальности резюме"

    @testit.workItemIds(3243)
    @testit.displayName("10.6.1.4. Пустой ввод в обязательные поля")
    @pytest.mark.regress
    @allure.title("id-3243 10.6.1.4. Пустой ввод в обязательные поля")
    def test_adding_the_resume_without_filling_in_a_required_field(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        user_profile_page.press_create_resume_button()
        time.sleep(1)
        user_profile_page.check_adding_the_resume_without_filling_in_a_required_field()

    @testit.workItemIds(3204)
    @testit.displayName("10.6.1.4. Отмена сохранения резюме")
    @pytest.mark.regress
    @allure.title("id-3204 10.6.1.4. Отмена сохранения резюме")
    def test_cancel_adding_the_resume(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        user_profile_page.press_create_resume_button()
        resume_name = user_profile_page.check_cancel_adding_resume()
        assert not user_profile_page.check_resume_name(resume_name), "Резюме сохранилось"

    @testit.workItemIds(3269)
    @testit.displayName("10.6.1.4. (Чек-лист)Превышение допустимого количества символов в полях")
    @pytest.mark.regress
    @allure.title("id-3269 10.6.1.4. (Чек-лист)Превышение допустимого количества символов в полях")
    def test_check_fields_max_length(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        user_profile_page.press_create_resume_button()
        user_profile_page.check_max_symbol()

    @testit.workItemIds(4296)
    @testit.displayName("10.6.1.4. Реакция системы при выборе даты окончания раньше даты начала в блоке Опыт работы")
    @pytest.mark.regress
    @allure.title("id-4296 10.6.1.4. Реакция системы при выборе даты окончания раньше даты начала в блоке Опыт работы")
    def test_selecting_an_end_date_earlier_than_the_start_date(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        user_profile_page.press_create_resume_button()
        user_profile_page.check_selecting_an_end_date_earlier_than_the_start_date()

    @testit.workItemIds(4297)
    @testit.displayName("10.6.1.4. Выбор даты начала позже даты окончания в блоке Опыт работы")
    @pytest.mark.regress
    @allure.title("id-4297 10.6.1.4. Выбор даты начала позже даты окончания в блоке Опыт работы")
    def test_selecting_an_start_date_after_than_the_end_date(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        user_profile_page.press_create_resume_button()
        user_profile_page.check_selecting_an_end_date_earlier_than_the_start_date()

    @testit.workItemIds(4298)
    @testit.displayName("10.6.1.4. Ввод даты позже текущего дня в поле Дата начала работы в компании")
    @pytest.mark.regress
    @allure.title("id-4298 10.6.1.4. Ввод даты позже текущего дня в поле Дата начала работы в компании")
    def test_entering_a_date_after_that_day_in_the_start_date_of_work_at_the_company_field(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_resume_tab()
        user_profile_page.press_create_resume_button()
        user_profile_page.check_entering_a_date_after_that_day_in_the_start_date_of_work_at_the_company_field()

    @testit.workItemIds(3247)
    @testit.displayName("10.6.1.5. Выход из режима просмотра резюме")
    @pytest.mark.regress
    @allure.title("id-3247 10.6.1.5. Выход из режима просмотра резюме")
    def test_exit_resume_viewing_mode(self, create_resume, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        user_profile_page.check_exit_resume_viewing_mode(create_resume)

    @testit.workItemIds(3210)
    @testit.displayName("10.6.1.6. Копирование резюме")
    @pytest.mark.regress
    @allure.title("id-3210 10.6.1.6. Копирование резюме")
    def test_copy_resume(self, create_resume, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        user_profile_page.copy_resume(create_resume)
        assert user_profile_page.check_resume_name('Копия 1 ' + create_resume), "Копия резюме не сохранилась"
        time.sleep(1)
        assert 'Резюме скопировано' in user_profile_page.get_alert_message(), \
            "Не отображается сообщение: Резюме скопировано"
        kebab_menu_titles = user_profile_page.delete_resume('Копия 1 ' + create_resume)
        assert kebab_menu_titles == ['Редактирование', 'Просмотр резюме', 'Копировать', 'Удалить'], \
            "Не все действия доступны для работы в резюме "

    @testit.workItemIds(3251)
    @testit.displayName("10.6.1.7. Удаление резюме")
    @pytest.mark.regress
    @allure.title("id-3251 10.6.1.7. Удаление резюме")
    def test_delete_resume(self, create_resume_to_delete, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_resume_tab()
        time.sleep(1)
        user_profile_page.delete_resume(create_resume_to_delete)
        assert not user_profile_page.check_resume_name(create_resume_to_delete), "Резюме не удалилось"
        time.sleep(1)
        assert 'Резюме удалено' in user_profile_page.get_alert_message(), "Не отображается сообщение: Резюме удалено"

    @testit.workItemIds(3212)
    @testit.displayName("10.6.1.7. Отмена удаления резюме")
    @pytest.mark.regress
    @allure.title("id-3212 10.6.1.7. Отмена удаления резюме")
    def test_cancel_delete_resume(self, create_resume, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        time.sleep(1)
        user_profile_page.cancel_delete_resume(create_resume)
        assert user_profile_page.check_resume_name(create_resume), "Резюме удалилось"

    @testit.workItemIds(3213)
    @testit.displayName("10.6.1.8. Сохранение изменений в резюме")
    @pytest.mark.regress
    @allure.title("id-3213 10.6.1.8. Сохранение изменений в резюме")
    def test_saving_changes_to_your_resume(self, create_resume, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        time.sleep(0.5)
        user_profile_page.redact_resume(create_resume)
        user_profile_page.change_resume('Новое имя резюме')
        time.sleep(1)
        assert user_profile_page.check_resume_name('Новое имя резюме'), "Имя резюме не изменилось"

    @testit.workItemIds(3214)
    @testit.displayName("10.6.1.8. Пустой ввод при редактировании резюме")
    @pytest.mark.regress
    @allure.title("id-3214 10.6.1.8. Пустой ввод при редактировании резюме")
    def test_blank_input_when_editing_resume(self, create_resume, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        time.sleep(3)
        user_profile_page.redact_resume(create_resume)
        user_profile_page.clear_required_fields()
        time.sleep(1)
        len_errors = user_profile_page.len_required_errors()
        alert = user_profile_page.get_alert_message()
        assert 'Заполнены не все обязательные поля' in alert, "Не появился алерт"
        assert len_errors == 6, "Отображаются не все сообщения Поле обязательно"

    @testit.workItemIds(3215)
    @testit.displayName("10.6.1.8. Изменение названия резюме на неуникальное")
    @pytest.mark.regress
    @allure.title("id-3215 10.6.1.8. Изменение названия резюме на неуникальное")
    def test_changing_the_resume_title_to_something_non_unique(self, create_resume, create_second_resume, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        time.sleep(0.5)
        user_profile_page.redact_resume(create_resume)
        time.sleep(1)
        user_profile_page.change_resume(create_second_resume)
        error = user_profile_page.get_mui_error()
        assert error == 'Название резюме должно быть уникальным', "Не отображается сообщение о не уникальности названия"

    @testit.workItemIds(3216)
    @testit.displayName("10.6.1.8. Отмена редактирования резюме")
    @pytest.mark.regress
    @allure.title("id-3216 10.6.1.8. Отмена редактирования резюме")
    def test_cancel_editing_resume(self, create_resume, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_resume_tab()
        user_profile_page.editing_resume()
        user_profile_page.check_cansel_changes()

    @testit.workItemIds(3217)
    @testit.displayName("10.6.1.8. Реакция системы при нажатии на кнопку Сохранить как новое")
    @pytest.mark.regress
    @allure.title("id-3217 10.6.1.8. Реакция системы при нажатии на кнопку Сохранить как новое")
    def test_save_as_new_resume(self, create_resume, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        user_profile_page.go_to_resume_tab()
        user_profile_page.editing_resume()
        user_profile_page.check_disable_save_button()
        user_profile_page.check_disable_save_as_new_button()
        user_profile_page.change_resume_title()
        user_profile_page.check_disable_save_button_able()
        user_profile_page.check_disable_save_as_new_button_able()
        user_profile_page.press_save_as_new_button()
        assert user_profile_page.get_modal_title() == "Введите название нового резюме", 'Заголовок некорректный'
        user_profile_page.check_resume_name_placeholder()
        user_profile_page.check_disable_save_button_able()
        user_profile_page.check_break_button()

    @testit.workItemIds(1512)
    @testit.displayName("10.2.3. Заполнение полей дополнительных контактов в блоке Контакты")
    @pytest.mark.regress
    @allure.title("id-1512 10.2.3. Заполнение полей дополнительных контактов в блоке Контакты")
    def test_filling_additional_contact_in_contacts(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        user_profile_page.press_redact_button()
        time.sleep(5)       # без слип тайм не успевает прогрузиться
        user_profile_page.add_contact_form()
        user_profile_page.filling_contact_form()
        user_profile_page.press_save_button()
        user_profile_page.check_added_contact()
        user_profile_page.press_redact_button()
        time.sleep(2)       # без слип тайм не успевает прогрузиться
        user_profile_page.delete_added_contact()
        user_profile_page.press_save_button()

    @testit.workItemIds(4161)
    @testit.displayName("10.2.1. Пустой ввод в обязательные для заполнения поля при редактировании таба Информация о сотруднике")
    @pytest.mark.regress
    @allure.title("id-4161 10.2.1. Пустой ввод в обязательные для заполнения поля при редактировании таба Информация о сотруднике")
    def test_blank_entry_into_required_fields_on_employee_information_tab(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.add_contact_form()
        user_profile_page.press_save_button()
        mui_errors = user_profile_page.get_all_mui_errors()
        alert_message = user_profile_page.get_alert_message()
        color = user_profile_page.get_my_profile_tab_color()
        assert color == 'rgba(211, 47, 47, 1)', "Таб Информация о сотруднике подсвечивается красным цветом."
        assert alert_message == ['На табе "Информация о сотруднике" не все поля были заполнены корректно'], \
            "Нет сообщения о некорректном заполнении полей"
        assert mui_errors == ['Поле обязательно', 'Поле обязательно'], "Нет сообщения об обязательности полей"

    @testit.workItemIds(1514)
    @testit.displayName("10.2.3. Пустой ввод в поля дополнительных контактов в блоке Контакты")
    @pytest.mark.regress
    @allure.title("id-1514 10.2.3. Пустой ввод в поля дополнительных контактов в блоке Контакты")
    def test_empty_filling_additional_contact_in_contacts(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        user_profile_page.press_redact_button()
        time.sleep(5)  # без слип тайм не успевает прогрузиться
        user_profile_page.add_contact_form()
        user_profile_page.press_save_button()
        assert user_profile_page.get_all_mui_errors() == ['Поле обязательно',
                                                          'Поле обязательно'], "Нет сообщения об обязательности полей"
        assert user_profile_page.get_my_profile_tab_color() == 'rgba(211, 47, 47, 1)', "Таб Информация о сотруднике не подсвечивается красным цветом."
        assert user_profile_page.get_alert_message() == ['На табе "Информация о сотруднике" не все поля были заполнены корректно'], "Нет сообщения о некорректном заполнении полей"

    @testit.workItemIds(1516)
    @testit.displayName("10.2.3. Ввод пробела в  поля дополнительных контактов в разделе Контакты")
    @pytest.mark.regress
    @allure.title("id-1516 10.2.3. Ввод пробела в  поля дополнительных контактов в разделе Контакты")
    def test_filling_additional_contact_in_contacts_with_space(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.press_redact_button()
        time.sleep(2)  # без слип тайм не успевает прогрузиться
        user_profile_page.add_contact_form()
        user_profile_page.space_input_contact_form()
        user_profile_page.press_save_button()
        assert user_profile_page.get_all_mui_errors() == ['Поле обязательно', 'Поле обязательно'], "Нет сообщения об обязательности полей"
        assert user_profile_page.get_my_profile_tab_color() == 'rgba(211, 47, 47, 1)', "Таб Информация о сотруднике не подсвечивается красным цветом."
        assert user_profile_page.get_alert_message() == ['На табе "Информация о сотруднике" не все поля были заполнены корректно'], "Нет сообщения о некорректном заполнении полей"

    @testit.workItemIds(1517)
    @testit.displayName("10.2.4. Удаление дополнительных контактов в разделе Контакты")
    @pytest.mark.regress
    @allure.title("id-1517 10.2.4. Удаление дополнительных контактов в разделе Контакты")
    def test_delete_additional_contact_in_contacts(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.press_redact_button()
        time.sleep(2)  # без слип тайм не успевает прогрузиться
        user_profile_page.add_contact_form()
        user_profile_page.filling_contact_form()
        user_profile_page.press_save_button()
        user_profile_page.check_added_contact()
        user_profile_page.press_redact_button()
        time.sleep(2)  # без слип тайм не успевает прогрузиться
        user_profile_page.delete_added_contact()
        user_profile_page.press_save_button()
        user_profile_page.check_delete_contact()

    @testit.workItemIds(1429)
    @testit.displayName("10.10.1. Сохранение заметки")
    @pytest.mark.regress
    @allure.title("id-1429 10.10.1. Сохранение заметки")
    def test_saving_note(self, create_work_user, create_user_whit_one_project_role_and_no_assignments, login, driver):
        colleagues_page = ColleaguesPage(driver)
        user_profile_page = UserProfilePage(driver)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user(create_work_user)
        colleagues_page.check_user_name_link()
        user_profile_page.go_to_colleague_profile()
        user_profile_page.check_note_tab()
        user_profile_page.put_text_in_note("Текст заметки")
        user_profile_page.save_note()
        user_profile_page.check_save_note("Текст заметки")
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user(create_work_user)
        time.sleep(2)  # если не успевает прогрузиться переходит по первому пользователю из списка
        colleagues_page.go_to_watch_the_user_eyes()
        user_profile_page.check_note_not_visible_addressee("Текст заметки")
        colleagues_page.go_back_to_profile()
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user(create_user_whit_one_project_role_and_no_assignments)
        time.sleep(2)  # если не успевает прогрузиться переходит по первому пользователю из списка
        colleagues_page.go_to_watch_the_user_eyes()
        user_profile_page.check_note_not_visible_non_author("Текст заметки")
        colleagues_page.go_back_to_profile()
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user(create_work_user)
        time.sleep(2)  # если не успевает прогрузиться переходит по первому пользователю из списка
        colleagues_page.check_user_name_link()
        user_profile_page.go_to_colleague_profile()
        user_profile_page.put_text_in_note('-')
        user_profile_page.save_note()

    @testit.workItemIds(1428)
    @testit.displayName("10.10.1. Редактирование заметки")
    @pytest.mark.regress
    @allure.title("id-1428 10.10.1. Редактирование заметки")
    def test_editing_note(self, create_work_user, login, driver):
        colleagues_page = ColleaguesPage(driver)
        user_profile_page = UserProfilePage(driver)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user(create_work_user)
        colleagues_page.check_user_name_link()
        user_profile_page.go_to_colleague_profile()
        user_profile_page.check_note_tab()
        user_profile_page.take_previously_saved_note()
        user_profile_page.put_text_in_note('Новый текст заметки')
        user_profile_page.save_note()
        user_profile_page.check_save_note("Новый текст заметки")
        user_profile_page.notes_comparison("Новый текст заметки")
        user_profile_page.put_text_in_note('-')
        user_profile_page.save_note()

    @testit.workItemIds(11924)
    @testit.displayName("10.2.3. Редактирование полей если выбранный Работодатель не существует в системе")
    @pytest.mark.regress
    @allure.title("id-11924 10.2.3. Редактирование полей если выбранный Работодатель не существует в системе")
    def test_editing_fields_if_the_selected_employer_does_not_exist(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_experience_tab()
        time.sleep(2)
        # Проверяем что есть карточка опыта
        if user_profile_page.check_experience_title():
            pass
        else:
            user_profile_page.field_work_experience_form_with_new_employer()
        before_fields_text = user_profile_page.get_all_fields()
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.field_custom_employer_field("Прошлый работодатель")
        assert user_profile_page.get_employer_field_text() == "Прошлый работодатель", \
            "В поле работодатель не отображается введенное значение"
        user_profile_page.field_project_field('Интересный проект')
        assert user_profile_page.get_project_field_text() == 'Интересный проект', \
            "В поле проект не отображается введенное значение"
        user_profile_page.field_project_role_field('Важная роль')
        assert user_profile_page.get_project_role_field_text() == 'Важная роль', \
            "В поле проектная роль не отображается введенное значение"
        user_profile_page.check_custom_begin_data_field()
        user_profile_page.check_custom_end_data_field()
        user_profile_page.field_knowledge_field()
        user_profile_page.press_save_button()
        after_fields_text = user_profile_page.get_all_fields()
        assert user_profile_page.check_experience_title(), "Карточка проекта отсутствует"
        assert before_fields_text != after_fields_text, "Карточка опыта не изменилась"
        # Удаляем карточку проекта
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()
        time.sleep(0.2)

    @testit.workItemIds(1083)
    @testit.displayName("Общий шаг. Перейти в 'Мой профиль'")
    @pytest.mark.regress
    @allure.title("id-1083 Общий шаг. Перейти в 'Мой профиль'")
    def test_go_to_my_profile(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        menu_items = user_profile_page.go_to_user_profile_with_check_menu_items()
        # Верхняя часть страницы
        user_profile_page.check_foto()
        user_name = user_profile_page.get_title()
        user_profile_page.check_header_post()
        user_profile_page.check_redact_button()
        # Вкладки
        user_profile_page.check_tab_text()
        activ_tab_name = user_profile_page.get_activ_tab()
        # Информацию о сотруднике
        all_labels = user_profile_page.get_all_labels_text()
        all_input = user_profile_page.get_all_input_values_text()
        # Теги
        user_profile_page.check_tags_title()
        assert menu_items == ['Мой профиль', 'Редактирование профиля', 'Сменить пароль', 'Выйти'], \
            "Выпадающий список содержит не все вкладки"
        assert ('Должность' and 'Подразделение' and 'Непосредственный руководитель' and 'Статус' and 'Формат работы' and
                'Прием в компанию' and 'Вступление в должность' and 'Увольнение из компании' in all_labels,
                "Есть не все Общие данные")
        assert 'E-mail' and 'Телефон' and 'Telegram' and 'Discord' in all_input, "Есть не все поля в разделе Контакты"
        assert ('Семейное положение' and 'Дети' and 'Дата рождения' and 'Интересные факты о себе' and 'Хобби' in
                all_labels, "Есть не все поля в разделе Дополнительная информация")
        assert USER_NAME in user_name, "В заголовке отсутствует ФИО пользователя"
        assert activ_tab_name == 'ИНФОРМАЦИЯ О СОТРУДНИКЕ', "По умолчанию не открыта вкладка Информация о сотруднике"

    @testit.workItemIds(1167)
    @testit.displayName("Общий шаг. Нажать кнопку Редактировать в личном профиле сотрудника")
    @pytest.mark.regress
    @allure.title("id-1167 10.2.3. Общий шаг. Нажать кнопку Редактировать в личном профиле сотрудника")
    def test_click_edit_button_in_user_profile(self, create_work_user, create_resume_to_autotest_user,
                                               put_label_to_auto_user, login, driver):
        colleagues_page = ColleaguesPage(driver)
        user_profile_page = UserProfilePage(driver)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user(create_work_user)
        colleagues_page.go_to_watch_the_user_eyes()
        schedule_page = SchedulePage(driver)
        schedule_page.go_to_schedule_page()
        time.sleep(3)
        if schedule_page.check_text_on_modal():
            schedule_page.press_submit_button_in_modal()
        else:
            pass
        time.sleep(4)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.press_redact_button()
        # Информация о сотруднике
        user_profile_page.check_tab_text_on_user()
        user_profile_page.check_save_and_break_buttons()
        activ_tab_name = user_profile_page.get_activ_tab()
        assert activ_tab_name == 'ИНФОРМАЦИЯ О СОТРУДНИКЕ', "По умолчанию не открыта вкладка Информация о сотруднике"
        # Общая информация
        user_profile_page.check_not_clickable_information_bloc_fields()
        assert user_profile_page.return_all_job_format() == ['Активен', 'В декрете', 'Внештатник', 'Неактивен',
                                                             'Удалённо', 'Частичная занятость'], \
            "В дропдауне есть не все форматы работы"
        user_profile_page.check_not_clickable_start_work_fields()
        # Контакты
        all_input = user_profile_page.get_all_input_values_text()
        assert 'E-mail' and 'Телефон' and 'Telegram' and 'Discord' in all_input, "Есть не все поля в разделе Контакты"
        user_profile_page.check_add_contact_button()
        # Дополнительная информация
        user_profile_page.check_family_status()
        all_labels = user_profile_page.get_all_labels_text()
        assert ('Семейное положение' and 'Дети' and 'Дата рождения' and 'Интересные факты о себе' and 'Хобби' in
                all_labels, "Есть не все поля в разделе Дополнительная информация")
        # Образование
        user_profile_page.go_to_education_tab()
        user_profile_page.check_add_icon()
        # Сертификаты
        user_profile_page.go_to_certificate_tab()
        user_profile_page.check_add_icon()
        # Опыт работы
        user_profile_page.go_to_experience_tab()
        user_profile_page.check_add_icon()
        # Заметки
        user_profile_page.go_to_colleague_profile()
        user_profile_page.check_wisivig()
        user_profile_page.check_submit_button()
        # Резюме
        user_profile_page.go_to_resume_tab()
        user_profile_page.check_resume_tab_column()
        user_profile_page.check_resume_kebab_menu()
        user_profile_page.check_create_resume_button()
        # График работы
        user_profile_page.go_to_schedule_tab()
        before_break = user_profile_page.get_text_on_chips(0)
        after_break = user_profile_page.get_text_on_chips(1)
        assert [before_break, after_break] == ['09:00 - 13:00', '14:00 - 18:00'], "По умолчанию график не с 09 до 18"
        user_profile_page.check_hours_in_day_fields()
        # Контакты
        user_profile_page.go_to_labels_tab()
        assert user_profile_page.get_all_labels_text() == ['Дата создания', 'ФИО автора', 'Проект',
                                                           'Почему вы решили выдать такую метку?'], \
            "В метке есть не все поля(заголовки)"

    @testit.workItemIds(1168)
    @testit.displayName("10.2.3. Добавление карточки проекта в табе Опыт работы")
    @pytest.mark.regress
    @allure.title("id-1168 10.2.3. Добавление карточки проекта в табе Опыт работы")
    def test_click_adding_project_card_in_work_experience_tab(self, project_with_two_resources, create_filial, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_experience_tab()
        time.sleep(2)
        if user_profile_page.check_experience_title():
            user_profile_page.press_redact_button()
            time.sleep(2)
            user_profile_page.press_delete_icon()
            user_profile_page.press_save_button()
        # Проверяем создание с выбором работодателя
        user_profile_page.check_work_experience_form()
        assert user_profile_page.check_experience_title(), "Карточка проекта не добавлена"
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()
        # Проверяем создание с добавлением работодателя
        user_profile_page.field_work_experience_form_with_new_employer()
        assert user_profile_page.check_experience_title(), "Карточка проекта не добавлена"
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()
        time.sleep(0.2)

    @testit.workItemIds(12566)
    @testit.displayName("10.2.1. (Чек лист) Просмотр профиля сотрудника с разными статусами: Работает/Уволен")
    @pytest.mark.regress
    @allure.title("id-12566 10.2.1. (Чек лист) Просмотр профиля сотрудника с разными статусами: Работает/Уволен")
    def test_viewing_employees_profile_with_statuses_working_fired(self, create_next_week_fired_user, login, driver):
        user_profile_page = UserProfilePage(driver)
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.open_status_filter()
        advanced_search_page.press_work_checkbox()
        advanced_search_page.action_esc()
        advanced_search_page.press_user_name()
        advanced_search_page.open_status_filter()
        advanced_search_page.press_work_checkbox()
        advanced_search_page.press_fired_checkbox()
        advanced_search_page.action_esc()
        advanced_search_page.press_user_name()
        advanced_search_page.open_status_filter()
        advanced_search_page.press_fired_checkbox()
        advanced_search_page.action_esc()
        advanced_search_page.search_by_second_name(create_next_week_fired_user)
        advanced_search_page.press_user_name()
        time.sleep(10)
        open_windows = driver.window_handles
        time.sleep(2)
        driver.switch_to.window(open_windows[1])
        time.sleep(3)
        assert user_profile_page.get_user_status() == 'Работает', "Статус пользователя не Работает"
        driver.switch_to.window(open_windows[2])
        time.sleep(3)
        assert user_profile_page.get_user_status() == 'Уволен', "Статус пользователя не Уволен"
        driver.switch_to.window(open_windows[3])
        time.sleep(3)
        assert user_profile_page.get_user_status() == 'Работает', "Статус пользователя не Работает"

    @testit.workItemIds(12592)
    @testit.displayName("10. Просмотр Формата работы в профиле сотрудника")
    @pytest.mark.regress
    @allure.title("id-12592 10. Просмотр Формата работы в профиле сотрудника")
    def test_viewing_job_format_in_employees_profile(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.press_redact_button()
        assert user_profile_page.return_all_job_format() == ['Активен', 'В декрете', 'Внештатник', 'Неактивен',
                                                             'Удалённо', 'Частичная занятость'], \
            "В дропдауне есть не все форматы работы"
        user_profile_page.abort_redact()
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.go_advanced_search_page()
        advanced_search_page.open_status_filter()
        advanced_search_page.press_work_checkbox()
        advanced_search_page.action_esc()
        advanced_search_page.press_user_name()
        open_windows = driver.window_handles
        time.sleep(2)
        driver.switch_to.window(open_windows[1])
        assert user_profile_page.get_job_format() == 'Не работает', "Отображается не корректный формат работы"

    @testit.workItemIds(1141)
    @testit.displayName("10.2.2. Удаление карточки диплома в разделе Образование в личном профиле сотрудника")
    @pytest.mark.regress
    @allure.title("id-1141 10.2.2. Удаление карточки диплома в разделе Образование в личном профиле сотрудника")
    def test_deleting_diploma_card_in_profile(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_education_tab()
        if user_profile_page.check_diploma_title():
            pass
        else:
            user_profile_page.add_simple_diploma()
            time.sleep(1)
            user_profile_page.go_to_education_tab()
        assert user_profile_page.check_diploma_title(), "Отсутствует диплом для удаления"
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()
        assert not user_profile_page.check_diploma_title(), "Диплом не удалился"

    @testit.workItemIds(1271)
    @testit.displayName("10.7.2. Выбор личного качества при редактировании профиля")
    @pytest.mark.regress
    @allure.title("id-1271 10.7.2. Выбор личного качества при редактировании профиля")
    def test_selecting_personal_quality_when_editing_profile(self, create_personal_quality,
                                                             create_second_personal_quality, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.check_search_qualities(create_personal_quality['name'], create_second_personal_quality['name'])
        user_profile_page.check_choose_qualities(create_personal_quality['name'], create_second_personal_quality['name'])
        user_profile_page.delete_qualiti(create_personal_quality['name'])
        time.sleep(2)

    @testit.workItemIds(1130)
    @testit.displayName("10.2.2. Добавление карточки нового диплома в разделе Образование в личном профиле")
    @pytest.mark.regress
    @allure.title("id-1130 10.2.2. Добавление карточки нового диплома в разделе Образование в личном профиле")
    def test_adding_diploma_to_education_tab_your_profile(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_education_tab()
        if user_profile_page.check_diploma_title():
            pass
        else:
            user_profile_page.add_simple_diploma()
            time.sleep(1)
            user_profile_page.go_to_education_tab()
        time.sleep(1)
        user_profile_page.press_redact_button()
        time.sleep(1)
        # Проверяем поля раздела образование
        user_profile_page.check_education_form()
        user_profile_page.press_delete_icon()
        user_profile_page.press_save_button()
        time.sleep(1)
        before_save = user_profile_page.add_diploma('НИИЧАВО',
                                      'Отдел Линейного Счастья',
                                      'магистр-академик')
        message = user_profile_page.get_alert_message()
        time.sleep(2)
        after_save = user_profile_page.get_all_value_diploma_card()
        assert 'НИИЧАВО' and 'Отдел Линейного Счастья' and 'магистр-академик' in before_save, \
            "В полях не отображаются введенные данные"
        assert sorted(before_save[0:7]) == sorted(after_save), "Изменения не сохранились"
        assert 'Данные сохранены' in message, "Не появилось сообщение Данные сохранены"

    @testit.workItemIds(3254)
    @testit.displayName("10.6.1.8. Сохранение изменений в резюме")
    @pytest.mark.regress
    @allure.title("id-3254 10.6.1.8. Сохранение изменений в резюме")
    def test_saving_changes_to_resume(self, create_resume, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_resume_tab()
        time.sleep(0.5)
        user_profile_page.redact_resume(create_resume)
        time.sleep(1)
        before = user_profile_page.get_all_fields()
        user_profile_page.change_mandatory_fields_in_resume('Новое имя резюме',
                                                            'Новое имя сотрудника',
                                                            '10.10.2024',
                                                            '10.10.2023')
        time.sleep(1)
        after_redact = user_profile_page.get_all_fields()
        user_profile_page.press_save_button()
        user_profile_page.search_resume('Новое имя резюме')
        user_profile_page.check_resume_kebab_menu()
        user_profile_page.redact_resume('Новое имя резюме')
        time.sleep(1)
        after = user_profile_page.get_all_fields()
        assert after == after_redact, "Изменения не сохранились после нажатия кнопки сохранить"
        assert 'Новое имя резюме' and 'Новое имя сотрудника' and '10.10.2024' and '10.10.2023' in after, \
            "В полях разделов структуры резюме не отображаются изменения"
        assert before != after, "Данные в резюме не изменились после редактирования"

    @testit.workItemIds(12214)
    @testit.displayName("10.2.3. Проверка условий заполнения полей в карточке проекта если выбран работодатель на табе Опыт работы")
    @pytest.mark.regress
    @allure.title("id-12214 10.2.3. Проверка условий заполнения полей в карточке проекта если выбран работодатель на табе Опыт работы")
    def test_checking_conditions_of_fields_if_employer_selected(self, project_with_assignment,
                                                                project_with_assignment_and_no_end_date, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_experience_tab()
        time.sleep(2)
        if user_profile_page.check_experience_title():
            user_profile_page.press_redact_button()
            time.sleep(2)
            user_profile_page.press_delete_icon()
            user_profile_page.press_save_button()
        # Сравниваем проекты на которые назначен пользователь
        project_names = user_profile_page.check_conditions_of_fields_if_employer_selected()
        project_endpoint = ProjectEndpoint()
        project_names_api = project_endpoint.get_project_name_for_current_user()
        assert sorted(project_names) == sorted(project_names_api), \
            "Отображаются не все проекты на которые в текущий момент назначен пользователь"
        # Сравниваем проектные роли первого проекта
        first_project_role = project_with_assignment[0]['slots'][0]['role']['name']
        first_project_role_ui = user_profile_page.get_project_roles(project_with_assignment[0]['name'])
        assert [first_project_role] == first_project_role_ui, "Проектные роли из API и UI не совпадают"
        # Сравниваем проектные роли второго проекта
        second_project_role = project_with_assignment_and_no_end_date['slots'][0]['role']['name']
        second_project_role_ui = user_profile_page.get_project_roles(project_with_assignment_and_no_end_date['name'])
        assert [second_project_role] == second_project_role_ui, "Проектные роли из API и UI не совпадают"
        # Проверка даты начала и конца работы проекта с датой окончания
        user_profile_page.check_start_and_end_fields(project_with_assignment[0]['name'])
        # Проверка даты начала и конца работы проекта без даты окончания. Закомментировано до решения бага
        # user_profile_page.check_start_and_end_fields(project_with_assignment_and_no_end_date['name'])

    @testit.workItemIds(11923)
    @testit.displayName("10.2.3. Редактирование полей если выбранный Работодатель существует в системе")
    @pytest.mark.regress
    @allure.title("id-11923 10.2.3. Редактирование полей если выбранный Работодатель существует в системе")
    def test_editing_fields_if_the_selected_employer_exists(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(6)
        user_profile_page.go_to_experience_tab()
        time.sleep(1)
        # Создаем карточку проекта если нет
        if user_profile_page.check_experience_title():
            pass
        else:
            user_profile_page.field_experience_form_with_exists_employer()

        before = user_profile_page.get_all_fields()
        project_endpoint = ProjectEndpoint()
        project_names_api = project_endpoint.get_project_name_for_current_user()
        user_profile_page.press_redact_button()
        project_names = user_profile_page.get_experience_projects_value()
        assert sorted(project_names) == sorted(project_names_api)
        # Блокируется багом
        user_profile_page.check_change_experience_projects()
