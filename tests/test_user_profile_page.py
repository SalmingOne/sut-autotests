import time

import allure
import pytest
import testit

from pages.colleagues_page import ColleaguesPage
from pages.create_local_user_drawer_page import CreateLocalUserDrawerPage
from pages.user_page import UserPage
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
        time.sleep(1)
        user_profile_page.go_to_education_tab()
        alert_messages = user_profile_page.get_alert_message()
        tab_color = user_profile_page.get_education_tab_color()
        errors = user_profile_page.get_mui_errors_text()
        assert 'Не все поля были заполнены корректно на табе "Образование"' in alert_messages, "Не появилось сообщение об ошибке"
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
        user_profile_page.go_to_certificate_tab()
        alert_message = user_profile_page.get_alert_message()
        tab_color = user_profile_page.get_certificate_tab_color()
        errors = user_profile_page.get_mui_errors_text()
        assert 'Не все поля были заполнены корректно на табе "Сертификаты"' in alert_message, "Не появилось сообщение об ошибке"
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
        user_profile_page.go_to_experience_tab()
        alert_message = user_profile_page.get_alert_message()
        tab_color = user_profile_page.get_experience_tab_color()
        errors = user_profile_page.get_mui_errors_text()

        assert 'Не все поля были заполнены корректно на табе "Опыт работы"' in alert_message, "Не появилось сообщение об ошибке"
        assert tab_color == 'rgba(255, 236, 229, 1)', "Цвет вкладки не красный"
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
        time.sleep(2)
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
        user_profile_page.go_to_education_tab()
        user_profile_page.press_redact_button()
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
        before = user_profile_page.get_additional_information()
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.input_additional_information()
        user_profile_page.press_save_button()
        time.sleep(1)
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
        user_profile_page.go_to_education_tab()
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
        user_profile_page.press_save_button()
        time.sleep(2)
        # Проверяем сообщение
        message = user_profile_page.get_alert_message()
        user_profile_page.go_to_education_tab()
        time.sleep(1)
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
        user_profile_page.go_to_certificate_tab()
        user_profile_page.press_redact_button()
        time.sleep(1)
        # Добавляем сертификат
        user_profile_page.press_add_icon_button()
        time.sleep(1)
        user_profile_page.check_and_field_certificate_form()
        user_profile_page.add_file('сертификат.pdf', 'Сертификат FANG')
        user_profile_page.check_add_file('сертификат.pdf')
        user_profile_page.press_save_button()
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
    def test_adding_a_diploma_card_in_the_education_section_in_someone_else_profile(self, create_work_user, login, driver):
        user_profile_page = UserProfilePage(driver)
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
        time.sleep(1)
        colleagues_page.check_user_name_link()
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
    def test_adding_a_diploma_file_in_the_education_section_in_someone_else_profile(self, create_work_user, login, driver):
        user_profile_page = UserProfilePage(driver)
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
    @testit.displayName("10.2.2. Удаление карточки диплома в разделеОбразование в чужом профиле")
    @pytest.mark.regress
    @allure.title("id-2102 10.2.2. Удаление карточки диплома в разделе Образование в чужом профиле")
    def test_delete_a_diploma_cart_from_the_education_section_in_someone_else_profile(self, create_work_user, login,
                                                                                    driver):
        user_profile_page = UserProfilePage(driver)
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