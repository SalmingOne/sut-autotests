import time

import allure
import pytest
import testit

from pages.colleagues_page import ColleaguesPage
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
        user_profile_page.press_add_icon_button()
        user_profile_page.press_save_button()
        time.sleep(1)
        user_profile_page.go_to_education_tab()
        alert_messages = user_profile_page.get_alert_message()
        tab_color = user_profile_page.get_education_tab_color()
        errors = user_profile_page.get_mui_errors_text()
        assert 'На табе "Образование" не все поля были заполнены корректно' in alert_messages, "Не появилось сообщение об ошибке"
        assert tab_color == 'rgba(255, 236, 229, 1)', "Цвет вкладки не красный"
        assert 'Поле обязательно' in errors, "Нет сообщений об обязательности поля"

    @testit.workItemIds(4159)
    @testit.displayName("10.2.1. Пустой ввод в обязательные для заполнения поля при редактировании таба Сертификаты")
    @pytest.mark.regress
    @allure.title("id-4159 10.2.1. Пустой ввод в обязательные для заполнения поля при редактировании таба Сертификаты")
    def test_blank_entry_on_certificate_tab(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_certificate_tab()
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_add_icon_button()
        user_profile_page.press_save_button()
        user_profile_page.go_to_certificate_tab()
        alert_message = user_profile_page.get_alert_message()
        tab_color = user_profile_page.get_certificate_tab_color()
        time.sleep(1)
        errors = user_profile_page.get_mui_errors_text()
        assert 'На табе "Сертификаты" не все поля были заполнены корректно' in alert_message, "Не появилось сообщение об ошибке"
        assert tab_color == 'rgba(255, 236, 229, 1)', "Цвет вкладки не красный"
        assert 'Поле обязательно' in errors, "Нет сообщений об обязательности поля"

    @testit.workItemIds(4160)
    @testit.displayName("10.2.3. Пустой ввод в обязательные для заполнения поля при редактировании таба Опыт работы")
    @pytest.mark.regress
    @allure.title("id-4160 10.2.3. Пустой ввод в обязательные для заполнения поля при редактировании таба Опыт работы")
    def test_blank_entry_on_experience_tab(self, login, driver):
        user_profile_page = UserProfilePage(driver)
        user_profile_page.go_to_user_profile()
        time.sleep(2)
        user_profile_page.go_to_experience_tab()
        user_profile_page.press_redact_button()
        time.sleep(1)
        user_profile_page.press_add_icon_button()
        user_profile_page.press_save_button()
        user_profile_page.go_to_experience_tab()
        alert_message = user_profile_page.get_alert_message()
        tab_color = user_profile_page.get_experience_tab_color()
        errors = user_profile_page.get_mui_errors_text()

        assert 'На табе "Опыт работы" не все поля были заполнены корректно' in alert_message, "Не появилось сообщение об ошибке"
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
        time.sleep(2)
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
        time.sleep(2)
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
        time.sleep(2)
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
    def test_adding_a_diploma_file_in_the_education_section_in_someone_else_profile(self, create_work_user, login,
                                                                                    driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
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
        time.sleep(1)
        colleagues_page.check_user_name_link()
        user_name = user_profile_page.get_title()
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
    def test_adding_a_project_in_the_work_experience_section_someone_else_profile(self, login, create_filial, driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        time.sleep(1)
        colleagues_page.check_user_name_link()
        user_name = user_profile_page.get_title()
        user_profile_page.go_to_experience_tab()
        time.sleep(1)
        if user_profile_page.check_experience_title():
            user_profile_page.press_redact_button()
            time.sleep(1)
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
    def test_deleting_a_project_in_the_work_experience_section_someone_else_profile(self, login, create_work_user, create_filial, driver):
        user_profile_page = UserProfilePage(driver)
        colleagues_page = ColleaguesPage(driver)
        time.sleep(1)
        colleagues_page.go_colleagues_page()
        colleagues_page.search_user('АвтоСПроектом')
        time.sleep(1)
        colleagues_page.check_user_name_link()
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
        time.sleep(2)
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
        time.sleep(2)
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
        time.sleep(0.5)
        user_profile_page.redact_resume(create_resume)
        user_profile_page.clear_required_fields()
        len_errors = user_profile_page.len_required_errors()
        alert = user_profile_page.get_alert_message()
        assert 'Заполнены не все обязательные поля' in alert, "Не появился алерт"
        assert len_errors == 6, "Отображаются не все сообщения Поле обязательно"
