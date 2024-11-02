import os
import random
import time
from datetime import datetime, timedelta

import allure
import testit
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from endpoints.project_endpoint import ProjectEndpoint
from locators.user_profile_page_locators import UserProfilePageLocators
from pages.base_page import BasePage
from utils.concat_testit_allure_step import allure_testit_step


class UserProfilePage(BasePage):
    locators = UserProfilePageLocators()

    @testit.step("Переходим в профиль пользователя")
    @allure.step("Переходим в профиль пользователя")
    def go_to_user_profile(self):
        self.element_is_visible(self.locators.PROFILE_BUTTON).click()
        self.element_is_visible(self.locators.MY_PROFILE_MENU_ITEM).click()

    @testit.step("Переходим на вкладку образование")
    @allure.step("Переходим на вкладку образование")
    def go_to_education_tab(self):
        self.element_is_visible(self.locators.EDUCATION_TAB_BUTTON).click()

    @testit.step("Переходим на вкладку профиль пользователя")
    @allure.step("Переходим на вкладку профиль пользователя")
    def go_to_user_profile_tab(self):
        self.element_is_visible(self.locators.MY_PROFILE_TAB_BUTTON).click()

    @testit.step("Переходим на вкладку резюме")
    @allure.step("Переходим на вкладку резюме")
    def go_to_resume_tab(self):
        self.element_is_visible(self.locators.RESUME_TAB_BUTTON).click()

    @testit.step("Переходим на вкладку Сертификаты")
    @allure.step("Переходим на вкладку Сертификаты")
    def go_to_certificate_tab(self):
        self.element_is_visible(self.locators.CERTIFICATE_TAB_BUTTON).click()

    @testit.step("Переходим на вкладку Опыт работы")
    @allure.step("Переходим на вкладку Опыт работы")
    def go_to_experience_tab(self):
        self.element_is_visible(self.locators.EXPERIENCES_TAB_BUTTON).click()

    @testit.step("Нажимаем кнопку редактировать")
    @allure.step("Нажимаем кнопку редактировать")
    def press_redact_button(self):
        time.sleep(1)  # Без этого ожидания не всегда нажимается кнопка
        self.element_is_visible(self.locators.REDACT_BUTTON).click()

    @testit.step("Нажимаем иконку добавления нового диплома")
    @allure.step("Нажимаем иконку добавления нового диплома")
    def press_add_icon_button(self):
        self.action_move_to_element(self.element_is_visible(self.locators.ADD_ICON))
        self.element_is_visible(self.locators.ADD_ICON).click()

    @testit.step("Нажимаем кнопку сохранения")
    @allure.step("Нажимаем кнопку сохранения")
    def press_save_button(self):
        time.sleep(1)  # Без этого ожидания не всегда нажимается кнопка
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

    @testit.step("Берем текст сообщения системы")
    @allure.step("Берем текст сообщения системы")
    def get_alert_message(self):
        all_messages = self.elements_are_visible(self.locators.ALERT_TEXT)
        data = []
        for message in all_messages:
            data.append(message.text)
        return data

    @testit.step("Берем цвет вкладки Образование")
    @allure.step("Берем цвет вкладки Образование")
    def get_education_tab_color(self):
        self.element_is_visible(self.locators.EXPERIENCES_TAB_BUTTON).click()
        time.sleep(1)
        color = self.element_is_visible(self.locators.EDUCATION_TAB_BUTTON).value_of_css_property('background-color')
        time.sleep(1)
        self.element_is_visible(self.locators.EDUCATION_TAB_BUTTON).click()
        return color

    @testit.step("Берем цвет вкладки Сертификаты")
    @allure.step("Берем цвет вкладки Сертификаты")
    def get_certificate_tab_color(self):
        self.element_is_visible(self.locators.EXPERIENCES_TAB_BUTTON).click()
        time.sleep(1)
        color = self.element_is_visible(self.locators.CERTIFICATE_TAB_BUTTON).value_of_css_property('background-color')
        time.sleep(1)
        self.element_is_visible(self.locators.CERTIFICATE_TAB_BUTTON).click()
        return color

    @testit.step("Берем цвет вкладки Опыт работы")
    @allure.step("Берем цвет вкладки Опыт работы")
    def get_experience_tab_color(self):
        self.element_is_visible(self.locators.CERTIFICATE_TAB_BUTTON).click()
        color = self.element_is_visible(self.locators.EXPERIENCES_TAB_BUTTON).value_of_css_property('background-color')
        self.element_is_visible(self.locators.EXPERIENCES_TAB_BUTTON).click()
        return color

    @testit.step("Берем цвет вкладки Информация о сотруднике")
    @allure.step("Берем цвет вкладки Информация о сотруднике")
    def get_my_profile_tab_color(self):
        self.element_is_visible(self.locators.CERTIFICATE_TAB_BUTTON).click()
        time.sleep(1)
        color = self.element_is_visible(self.locators.MY_PROFILE_TAB_BUTTON).value_of_css_property('background-color')
        self.element_is_visible(self.locators.MY_PROFILE_TAB_BUTTON).click()
        return color

    @testit.step("Берем текст ошибок с незаполненных обязательных полей")
    @allure.step("Берем текст ошибок с незаполненных обязательных полей")
    def get_mui_errors_text(self):
        error_messages = self.elements_are_visible(self.locators.MUI_ERROR)
        data = []
        for message in error_messages:
            data.append(message.text)
        return data

    @testit.step("Получение текста заголовка")
    @allure.step("Получение текста заголовка")
    def get_title(self):
        return self.element_is_visible(self.locators.PROFILE_TITLE).text

    @testit.step("Получение текста заголовка модального окна")
    @allure.step("Получение текста заголовка модального окна")
    def get_modal_title(self):
        return self.element_is_visible(self.locators.MODAL_TITLE).text

    @testit.step("Получение даты начала работы")
    @allure.step("Получение даты начала работы")
    def get_start_work_date(self):
        return self.element_is_visible(self.locators.START_WORK).get_attribute('value')

    @testit.step("Нажатие кнопки создать резюме")
    @allure.step("Нажатие кнопки создать резюме")
    def press_create_resume_button(self):
        self.element_is_visible(self.locators.CREATE_RESUME_BUTTON).click()

    @testit.step("Нажатие кнопки Сохранить как новое")
    @allure.step("Нажатие кнопки Сохранить как новое")
    def press_save_as_new_button(self):
        self.element_is_visible(self.locators.SAVE_AS_NEW_BUTTON).click()

    @testit.step("Проверка плейсхолдера поля Название резюме")
    @allure.step("Проверка плейсхолдера поля Название резюме")
    def check_resume_name_placeholder(self):
        assert self.element_is_displayed(self.locators.PLACEHOLDER_RESUME_SAVE_AS), 'Название плейсхолдера отличается'

    @testit.step("Проверка значений по умолчанию")
    @allure.step("Проверка значений по умолчанию")
    def check_default_values(self, name, start_work):
        resume_title = self.element_is_visible(self.locators.RESUME_TITLE_FIELD).get_attribute('value')
        full_name = self.element_is_visible(self.locators.RESUME_FULL_NAME_FIELD).get_attribute('value')
        start_work_resume = self.element_is_visible(self.locators.START_WORK_IN_RESUME).get_attribute('value')

        assert self.get_day_before_y_m_d(0) and name in resume_title, \
            'Название резюме по умолчанию не содержит ФИО пользователя или текущую дату'
        assert name == full_name, 'ФИО не подтянулось из карточки пользователя'
        assert start_work == start_work_resume, 'Дата начала работы в компании не подтянулась из профиля'

    @testit.step("Проверка ограничения в 255 символов для поля")
    @allure.step("Проверка ограничения в 255 символов для поля")
    def check_255_symbol_in_field(self, locator):
        bed_value = 'a' * 256
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys(bed_value)
        self.element_is_visible(self.locators.START_WORK_IN_RESUME).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        time.sleep(2)
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys('1')
        self.element_is_visible(self.locators.START_WORK_IN_RESUME).click()
        assert error_text == 'Максимальное количество символов: 255', \
            "Не появилось сообщение о превышении максимального количества символов" + locator

    @testit.step("Проверка всех полей с ограничением в 255 символов")
    @allure.step("Проверка всех полей с ограничением в 255 символов")
    def check_max_symbol(self):
        self.element_is_visible(self.locators.ADD_EXPERIENCE_BUTTON).click()
        fields = [self.locators.RESUME_TITLE_FIELD, self.locators.RESUME_FULL_NAME_FIELD,
                  self.locators.RESUME_POST_FIELD, self.locators.RESUME_DIRECTION_FIELD,
                  self.locators.EXPERIENCE_PROJECT_NAME, self.locators.EXPERIENCE_CUSTOMER,
                  self.locators.EXPERIENCE_PROJECT_POST]
        for field in fields:
            self.check_255_symbol_in_field(field)

    @testit.step("Проверка тултипа поля должность")
    @allure.step("Проверка тултипа поля должность")
    def check_post_tooltip(self):
        self.action_move_to_element(self.element_is_visible(self.locators.RESUME_POST_FIELD))
        assert self.element_is_visible(
            self.locators.TOOLTIP).text == 'Пример: Разработчик, Developer, Аналитик, Lead QA и т.д.', \
            'Не корректный тултип при наведении на поле должность'

    @testit.step("Проверка тултипа поля Место проживания")
    @allure.step("Проверка тултипа поля Место проживания")
    def check_direction_tooltip(self):
        self.action_move_to_element(self.element_is_visible(self.locators.RESUME_DIRECTION_FIELD))
        assert self.element_is_visible(self.locators.TOOLTIP).text == 'Пример: Россия, Москва', \
            'Не корректный тултип при наведении на полеМесто проживания'

    @testit.step("Проверка дропдауна готовность к работе")
    @allure.step("Проверка дропдауна готовность к работе")
    def check_ready_to_work_dropdown(self):
        self.element_is_visible(self.locators.READY_TO_WORK_DROPDOWN).click()
        dropdown_items = self.elements_are_visible(self.locators.LI_MENU_ITEM)
        names = []
        for item in dropdown_items:
            self.action_move_to_element(item)
            names.append(item.text)
        assert names == ['Готов к удаленной работе', 'Не готов к удаленной работе', 'Готов к переезду',
                         'Не готов к переезду', 'Готов к командировкам', 'Готов к редким командировкам',
                         'Не готов к командировкам'], 'В дропдауне есть не все значения'

    @testit.step("Проверка дата-пикеров в дровере")
    @allure.step("Проверка дата-пикеров в дровере")
    def check_date_pikers(self):
        assert len(self.elements_are_visible(self.locators.DATE_PIKERS)) == 5, "В дровере не пять дата-пикеров"

    @testit.step("Проверка визивигов в дровере")
    @allure.step("Проверка визивигов в дровере")
    def check_wysiwyg_titles(self):
        all_wysiwyg = self.elements_are_visible(self.locators.WYSIWYG_TITLES)
        titles = []
        for wysiwyg in all_wysiwyg:
            titles.append(wysiwyg.text)
        assert titles == ['Профессиональный стек', 'Личные качества', 'Обязанности', 'Полученный опыт и навыки',
                          'Высшее образование', 'Другое', 'О себе', 'Иностранные языки'], 'В дровере не все визивиги'

    @testit.step("Проверка функций визивига")
    @allure.step("Проверка функций визивига")
    def check_wysiwyg_functions_titles(self):
        all_functions = self.elements_are_visible(self.locators.WYSIWYG_INCLUDES_FUNCTION_TITLES)
        titles = []
        for functions in all_functions:
            titles.append(functions.get_attribute('title'))
        assert titles == ['Жирный', 'Курсив', 'Неупорядоченный', 'Упорядоченный', 'Форматирование', 'Ссылка',
                          'Убрать ссылку'], 'В визивиге есть не все функции'

    @testit.step("Проверка кнопки Сохранить задизейбленна")
    @allure.step("Проверка кнопки Сохранить задизейбленна")
    def check_disable_save_button(self):
        assert not self.element_is_clickable(self.locators.SAVE_BUTTON, 1), 'Кнопка сохранить не задизейблена'

    @testit.step("Проверка кнопки Сохранить доступна")
    @allure.step("Проверка кнопки Сохранить доступна")
    def check_disable_save_button_able(self):
        assert self.element_is_clickable(self.locators.SAVE_BUTTON), 'Кнопка сохранить задизейблена'

    @testit.step("Проверка кнопки Сохранить как новое задизейбленна")
    @allure.step("Проверка кнопки Сохранить как новое задизейбленна")
    def check_disable_save_as_new_button(self):
        assert not self.element_is_clickable(self.locators.SAVE_AS_NEW_BUTTON,
                                             1), 'Кнопка сохранить как новое не задизейблена'

    @testit.step("Проверка кнопки Сохранить как новое доступна")
    @allure.step("Проверка кнопки Сохранить как новое доступна")
    def check_disable_save_as_new_button_able(self):
        assert self.element_is_clickable(self.locators.SAVE_AS_NEW_BUTTON), 'Кнопка сохранить как новое задизейблена'

    @testit.step("Проверка кнопки отменить")
    @allure.step("Проверка кнопки отменить")
    def check_break_button(self):
        assert self.element_is_displayed(self.locators.BREAK_BUTTON), 'Нет кнопки отменить'

    @testit.step("Проверка чекбокса текущий работодатель")
    @allure.step("Проверка чекбокса текущий работодатель")
    def current_employer_checkbox(self):
        assert self.element_is_displayed(self.locators.CURRENT_EMPLOYER_CHECKBOX), 'Нет чекбокса текущий работодатель'

    @testit.step("Сохранение резюме")
    @allure.step("Сохранение резюме")
    def save_resume(self):
        resume_title = self.element_is_visible(self.locators.RESUME_TITLE_FIELD).get_attribute('value')
        self.element_is_visible(self.locators.RESUME_POST_FIELD).send_keys('Администратор')
        self.action_select_all_text(self.elements_are_visible(self.locators.DATE_PIKERS)[1])
        self.elements_are_visible(self.locators.DATE_PIKERS)[1].send_keys('01.02.1990')
        self.action_select_all_text(self.elements_are_visible(self.locators.DATE_PIKERS)[2])
        self.elements_are_visible(self.locators.DATE_PIKERS)[2].send_keys(self.get_day_before(0))
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(1)
        return resume_title

    @testit.step("Получение всех названий резюме из таблицы")
    @allure.step("Получение всех названий резюме из таблицы")
    def get_names_resume_on_tab(self):
        resume_titles_on_tab = self.elements_are_visible(self.locators.RESUME_TITLES_ON_TAB)
        titles = []
        for resume in resume_titles_on_tab:
            titles.append(resume.text)
        return titles

    @testit.step("Удаление резюме")
    @allure.step("Удаление резюме")
    def delete_resume(self, name):
        self.action_select_all_text(self.element_is_visible(self.locators.SEARCH_RESUME_NAME_FIELDS))
        self.element_is_visible(self.locators.SEARCH_RESUME_NAME_FIELDS).send_keys(name)
        time.sleep(1)
        self.elements_are_visible(self.locators.KEBAB_MENU)[0].click()
        menu_item = self.elements_are_visible(self.locators.KEBAB_MENU_ITEM)
        items_text = []
        for element in menu_item:
            items_text.append(element.text)
        self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)
        return items_text

    @testit.step("Открытие резюме в режиме редактирования")
    @allure.step("Открытие резюме в режиме редактирования")
    def editing_resume(self):
        self.elements_are_visible(self.locators.KEBAB_MENU)[0].click()
        self.element_is_visible(self.locators.KEBABS_EDIT_MENU_ITEM).click()
        time.sleep(1)

    @testit.step("Внесение изменений в резюме")
    @allure.step("Внесение изменений в резюме")
    def change_resume_title(self):
        self.element_is_visible(self.locators.RESUME_TITLE_FIELD).send_keys(' new')
        time.sleep(1)

    @testit.step("Получение текста с поля дети")
    @allure.step("Получение текста с поля дети")
    def get_children_text(self):
        return self.element_is_visible(self.locators.CHILDREN_TEXT_AREA).text

    @testit.step("Добавление текста в поле дети")
    @allure.step("Добавление текста в поле дети")
    def change_children_text(self, text):
        time.sleep(1)
        self.action_select_all_text(self.element_is_visible(self.locators.CHILDREN_TEXT_AREA))
        self.element_is_visible(self.locators.CHILDREN_TEXT_AREA).send_keys(text)

    @testit.step("Добавление текста в поле email")
    @allure.step("Добавление текста в поле email")
    def change_email_text(self, text):
        self.action_select_all_text(self.element_is_visible(self.locators.EMAIL_FIELD))
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(text)

    @testit.step("Добавление текста в поле телефон")
    @allure.step("Добавление текста в поле телефон")
    def change_phone_text(self, text):
        self.action_select_all_text(self.element_is_visible(self.locators.PHONE_FIELD))
        self.element_is_visible(self.locators.PHONE_FIELD).send_keys(text)

    @testit.step("Получение текста с поля email")
    @allure.step("Получение текста с поля email")
    def get_email_text(self):
        return self.element_is_visible(self.locators.EMAIL_TEXT_AREA).text

    @testit.step("Получение текста с поля телефон")
    @allure.step("Получение текста с поля телефон")
    def get_phone_text(self):
        return self.element_is_visible(self.locators.PHONE_TEXT_AREA).text

    @testit.step("Получение текста с поля телефон во время редактирования")
    @allure.step("Получение текста с поля телефон во время редактирования")
    def get_phone_text_on_redact(self):
        return self.element_is_visible(self.locators.PHONE_FIELD).get_attribute('value')

    @testit.step("Проверка модального окна при отмене изменений")
    @allure.step("Проверка модального окна при отмене изменений")
    def check_cansel_changes(self):
        self.element_is_visible(self.locators.BREAK_BUTTON).click()
        assert self.element_is_visible(self.locators.SUBMIT_BUTTON), 'Отсутствует кнопка Подтвердить'
        assert self.element_is_visible(self.locators.CANSEL_BUTTON), 'Отсутствует кнопка Отменить'
        assert self.element_is_visible(self.locators.ALERT_DIALOG_DESCRIPTION).text == ('Внесенные изменения не '
                                                                                        'сохранятся. Закрыть режим '
                                                                                        'редактирования?'), \
            'Не корректный текст в модальном окне'
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка перехода на другой таб")
    @allure.step("Проверка перехода на другой таб")
    def check_start_work_is_visible(self):
        return self.element_is_displayed(self.locators.START_WORK)

    @testit.step("Получение дополнительной информации профиля")
    @allure.step("Получение дополнительной информации профиля")
    def get_additional_information(self):
        family_statys = self.element_is_visible(self.locators.FAMILY_STATUS).get_attribute('value')
        children = self.element_is_visible(self.locators.CHILDREN_TEXT_AREA).text
        born_date = self.element_is_visible(self.locators.BORN_DATE).get_attribute('value')
        return family_statys, children, born_date

    @testit.step("Изменение дополнительной информации профиля")
    @allure.step("Изменение дополнительной информации профиля")
    def input_additional_information(self):
        self.element_is_visible(self.locators.FAMILY_STATUS).click()
        self.elements_are_visible(self.locators.NOT_SELECTED_LI)[0].click()
        self.change_children_text(f'сын {random.randint(1, 10000)}')
        self.action_double_click(self.element_is_visible(self.locators.BORN_DATE))
        self.element_is_visible(self.locators.BORN_DATE).send_keys(f'02.03.{random.randint(1, 2000)}')

    @testit.step("Проверка заголовка диплом")
    @allure.step("Проверка заголовка диплом")
    def check_diploma_title(self):
        return self.element_is_displayed(self.locators.CHECK_DIPLOMA_TITLE, 2)

    @testit.step("Проверка заголовка сертификата")
    @allure.step("Проверка заголовка сертификата")
    def check_certificate_title(self):
        return self.element_is_displayed(self.locators.CERTIFICATE_TITLE, 1)

    @testit.step("Проверка заголовка опыт работы")
    @allure.step("Проверка заголовка опыт работы")
    def check_experience_title(self):
        return self.element_is_displayed(self.locators.EXPERIENCES_TITLE, 1)

    @testit.step("Добавление простого диплома")
    @allure.step("Добавление простого диплома")
    def add_simple_diploma(self):
        self.press_redact_button()
        time.sleep(1)
        self.element_is_visible(self.locators.ADD_ICON).click()
        self.element_is_visible(self.locators.EDUCATION_FORM).click()
        self.elements_are_visible(self.locators.NOT_SELECTED_LI)[0].click()
        self.element_is_visible(self.locators.EDUCATION_LEVEL).click()
        self.elements_are_visible(self.locators.NOT_SELECTED_LI)[0].click()
        self.element_is_visible(self.locators.FACULTY).click()
        self.press_save_button()
        try:
            self.press_save_button()
        except TimeoutException:
            pass

    @testit.step("Получение значений выпадающего списка")
    @allure.step("Получение значений выпадающего списка")
    def get_dropdown_menu_items(self, locator):
        self.element_is_visible(locator).click()
        time.sleep(1)
        all_items = self.elements_are_visible(self.locators.LI_MENU_ITEM)
        menu_item_text = []
        for item in all_items:
            self.action_move_to_element(item)
            menu_item_text.append(item.text)
        self.element_is_visible(locator).send_keys(Keys.RETURN)
        return menu_item_text

    @testit.step("Проверка ограничения в 128 символов для поля")
    @allure.step("Проверка ограничения в 128 символов для поля")
    def check_128_symbol_in_field(self, locator, locator_to_click):
        bed_value = ('Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt'
                     ' ut laoreet dolore magna aliquam')
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys(bed_value)
        self.element_is_visible(locator_to_click).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        time.sleep(2)
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys('1')
        self.element_is_visible(locator_to_click).click()
        assert error_text == 'Максимальное количество символов: 128', \
            "Не появилось сообщение о превышении максимального количества символов"

    @testit.step("Проверка поля дата окончания")
    @allure.step("Проверка поля дата окончания")
    def check_year_of_graduation_field(self):
        self.action_double_click(self.element_is_visible(self.locators.YEAR_OF_GRADUATION))
        self.element_is_visible(self.locators.YEAR_OF_GRADUATION).send_keys('1949')
        self.element_is_visible(self.locators.EDUCATION_FORM).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        assert error_text == 'Введите год не ранее 1950', 'Можно ввести год ранее 1950'
        plus_11_year = datetime.now() + timedelta(days=4015)
        self.action_double_click(self.element_is_visible(self.locators.YEAR_OF_GRADUATION))
        self.element_is_visible(self.locators.YEAR_OF_GRADUATION).send_keys(plus_11_year.strftime("%Y"))
        self.element_is_visible(self.locators.EDUCATION_FORM).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.action_double_click(self.element_is_visible(self.locators.YEAR_OF_GRADUATION))
        self.element_is_visible(self.locators.YEAR_OF_GRADUATION).send_keys(datetime.now().strftime("%Y"))
        assert 'Введите год не позднее' in error_text, 'Можно ввести год позднее текущий год плюс 10 лет'

    @testit.step("Проверка содержания раздела образование")
    @allure.step("Проверка содержания раздела образование")
    def check_education_form(self):
        time.sleep(1)
        educations = self.get_dropdown_menu_items(self.locators.EDUCATION_FORM)
        time.sleep(1)
        directions = self.get_dropdown_menu_items(self.locators.DIRECTION)
        levels = self.get_dropdown_menu_items(self.locators.EDUCATION_LEVEL)
        self.check_128_symbol_in_field(self.locators.FACULTY_NAME, self.locators.EDUCATION_FORM)
        self.check_128_symbol_in_field(self.locators.SPECIALIZATION_NAME, self.locators.EDUCATION_FORM)
        self.check_year_of_graduation_field()

        assert educations == ['Заочное', 'Очное', 'Очно-заочное'], 'Не корректный список в дропдауне Форма обучения'
        assert directions == ['Гуманитарное', 'Техническое'], 'Не корректный список в дропдауне Направление'
        assert levels == ['Студент', 'Среднее профессиональное', 'Повышение квалификации', 'Неполное высшее',
                          'Специалист', 'Начальное профессиональное образование', 'Бакалавр', 'Доктор наук',
                          'Кандидат наук',
                          'Магистр'], 'Не корректный список в дропдауне Образовательно-квалификационный уровень'
        assert self.element_is_displayed(
            self.locators.INSTITUTION_NAME), 'Нет поля Название образовательного учреждения'
        assert self.element_is_displayed(self.locators.DELETE_ICON), 'Нет иконки удаления'
        assert self.element_is_displayed(self.locators.ADD_ICON), 'Нет иконки добавления'

    @testit.step("Добавление файла")
    @allure.step("Добавление файла")
    def add_file(self, name, text):
        file = open(os.path.abspath(rf'../{name}'), 'w+')
        file.write(f'{text}')
        file.close()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(os.path.abspath(rf'../{name}'))

    @testit.step("Проверка добавления файла")
    @allure.step("Проверка добавления файла")
    def check_add_file(self, name):
        file_name = self.element_is_visible(self.locators.FILE_INPUT_CHECK).text
        assert file_name == name, "Файл не добавился или добавился не сте именем"

    @testit.step("Удаление файла")
    @allure.step("Удаление файла")
    def delete_file(self, name):
        os.remove(rf'../{name}')

    @testit.step("Проверка иконки скачивания файла")
    @allure.step("Проверка иконки скачивания файла")
    def check_download_file_icon(self):
        assert self.element_is_displayed(self.locators.FILE_DOWNLOAD_ICON), "Нет иконки скачивания файла"

    @testit.step("Удаление файла с сайта")
    @allure.step("Удаление файла с сайта")
    def delete_file_from_site(self):
        self.elements_are_visible(self.locators.DELETE_ICON)[1].click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка и заполнение формы сертификата")
    @allure.step("Проверка и заполнение формы сертификата")
    def check_and_field_certificate_form(self):
        self.element_is_visible(self.locators.CERTIFICATE_NAME).send_keys(f'Сертификат {random.randint(1, 1000)}')
        self.element_is_visible(self.locators.CERTIFICATE_DATA_PICKER).click()
        assert not self.element_is_clickable(self.locators.DAY_AFTER_THIS_DAY_PICKER, 2), \
            'Можно выбрать завтрашнюю дату'
        self.element_is_visible(self.locators.CERTIFICATE_DATA_PICKER).click()
        self.element_is_visible(self.locators.THIS_DAY_PICKER).click()
        assert self.element_is_displayed(self.locators.DELETE_ICON), 'Нет иконки удаления'

    @testit.step("Нажимаем иконку удаления")
    @allure.step("Нажимаем иконку удаления")
    def press_delete_icon(self):
        self.elements_are_visible(self.locators.DELETE_ICON)[0].click()

    @testit.step("Проверка иконки удаления")
    @allure.step("Проверка иконки удаления")
    def check_delete_icon(self):
        assert self.element_is_displayed(self.locators.DELETE_ICON), "Нет иконки удаления"

    @testit.step("Проверка некликабельности полей до заполнения поля работодатель")
    @allure.step("Проверка некликабельности полей до заполнения поля работодатель")
    def check_disable_fields_in_work_experience_form(self):
        assert not self.element_is_clickable(self.locators.EXPERIENCES_PROJECT_FIELD,
                                             1), "Поле Название проекта кликабельно"
        assert not self.element_is_clickable(self.locators.EXPERIENCES_SPECIALIZATION_ACTION,
                                             1), "Поле Вид деятельности кликабельно"
        assert not self.element_is_clickable(self.locators.EXPERIENCES_SPECIALIZATION_SLOT,
                                             1), "Поле Проектная роль кликабельно"
        assert not self.element_is_clickable(self.locators.EXPERIENCES_DESCRIPTION_TEXT, 1), "Поле Описание кликабельно"
        assert not self.element_is_clickable(self.elements_are_visible(self.locators.EXPERIENCES_DATA_PICKER)[0],
                                             1), "Поле Дата начала работы кликабельно"
        assert not self.element_is_clickable(self.elements_are_visible(self.locators.EXPERIENCES_DATA_PICKER)[1],
                                             1), "Поле Дата окончания работы кликабельно"
        assert not self.element_is_clickable(self.locators.EXPERIENCES_KNOWLEDGE_FIELD, 1), "Поле Знание кликабельно"

    @testit.step("Проверка максимальной длины поля работодатель")
    @allure.step("Проверка максимальной длины поля работодатель")
    def check_128_in_experience_tab(self):
        bed_value = ('Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt'
                     ' ut laoreet dolore magna aliquam')
        self.element_is_visible(self.locators.EXPERIENCES_EMPLOYER_FIELD).send_keys(bed_value)
        li_text = self.element_is_visible(self.locators.LI_MENU_ITEM).get_attribute('aria-label')
        self.action_select_all_text(self.element_is_visible(self.locators.EXPERIENCES_EMPLOYER_FIELD))
        self.element_is_visible(self.locators.EXPERIENCES_EMPLOYER_FIELD).clear()
        assert li_text == 'Максимальное количество символов: 128', "Не появилось сообщение о превышении максимальной длины"

    @testit.step("Получение даты за день до создания проекта")
    @allure.step("Получение даты за день до создания проекта")
    def get_day_before_create_project(self, project_name):
        project_endpoint = ProjectEndpoint()
        date = project_endpoint.get_project_start_date_by_name(project_name)[0]
        f_date = date[8:10] + '.' + date[5:7] + '.' + date[0:4]
        day_before = datetime.strptime(f_date, "%d.%m.%Y") - timedelta(days=1)
        return day_before.strftime("%d.%m.%Y")

    @testit.step("Получение даты после создания проекта")
    @allure.step("Получение даты после создания проекта")
    def get_day_after_create_project(self, project_name):
        project_endpoint = ProjectEndpoint()
        date = project_endpoint.get_project_start_date_by_name(project_name)[0]
        f_date = date[8:10] + '.' + date[5:7] + '.' + date[0:4]
        day_before = datetime.strptime(f_date, "%d.%m.%Y") + timedelta(days=1)
        return day_before.strftime("%d.%m.%Y")

    @testit.step("Получение даты после окончания проекта")
    @allure.step("Получение даты после окончания  проекта")
    def get_day_after_end_project(self, project_name):
        project_endpoint = ProjectEndpoint()
        date = project_endpoint.get_project_start_date_by_name(project_name)[1]
        if date is None:
            return False
        f_date = date[8:10] + '.' + date[5:7] + '.' + date[0:4]
        day_before = datetime.strptime(f_date, "%d.%m.%Y") + timedelta(days=1)
        return day_before.strftime("%d.%m.%Y")

    @testit.step("Проверка поля Дата начала проекта")
    @allure.step("Проверка поля Дата начала проекта")
    def check_start_date_field(self):
        project_name = self.element_is_visible(self.locators.EXPERIENCES_PROJECT_FIELD).get_attribute('value')
        before_create_project = self.get_day_before_create_project(project_name)
        self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT).send_keys(before_create_project)
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        time.sleep(2)
        self.action_double_click(self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT))
        self.action_select_all_text(self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT))
        after_end_project = self.get_day_after_end_project(project_name)
        if after_end_project:
            self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT).send_keys(after_end_project)
            self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
            second_error_text = self.element_is_visible(self.locators.MUI_ERROR).text
            assert second_error_text == 'Дата начала работы некорректна', "Можно ввести дату позже окончания проекта"
            self.action_double_click(self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT))
        self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT).send_keys(
            self.get_day_after_create_project(project_name))
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
        assert error_text == 'Дата начала работы некорректна', "Можно ввести дату раньше начала проекта"

    @testit.step("Проверка поля Дата окончания проекта")
    @allure.step("Проверка поля Дата окончания проекта")
    def check_end_date_field(self):
        project_name = self.element_is_visible(self.locators.EXPERIENCES_PROJECT_FIELD).get_attribute('value')
        before_create_project = self.get_day_before_create_project(project_name)
        # Дата до начала работы
        start_date = self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT).get_attribute('value')
        day_before = datetime.strptime(start_date, "%d.%m.%Y") - timedelta(days=1)
        self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT).send_keys(day_before.strftime("%d.%m.%Y"))
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
        assert self.element_is_visible(self.locators.MUI_ERROR).text == 'Дата окончания работы не может быть раньше начала'
        # Дата до начала проекта
        time.sleep(2)
        self.action_double_click(self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT))
        self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT).send_keys(before_create_project)
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
        assert self.element_is_visible(self.locators.MUI_ERROR).text == 'Дата окончания работы не может быть раньше начала', \
            "Можно ввести дату раньше начала проекта"
        # Дата позже конца проекта или позже текущей
        time.sleep(2)
        self.action_double_click(self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT))
        after_end_project = self.get_day_after_end_project(project_name)
        if after_end_project:
            self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT).send_keys(after_end_project)
            self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
            assert self.element_is_visible(self.locators.MUI_ERROR).text == 'Дата окончания работы некорректна', \
                "Можно ввести дату позже окончания проекта"
            self.action_double_click(self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT))
        else:
            self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT).send_keys(self.get_day_before(-1))
            self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
            assert self.element_is_visible(self.locators.MUI_ERROR).text == 'Дата окончания работы некорректна'
            self.action_double_click(self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT))

        self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT).send_keys(self.get_day_before(0))
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()

    @testit.step("Проверка формы Опыт работы с выбором работодателя")
    @allure.step("Проверка формы Опыт работы с выбором работодателя")
    def check_work_experience_form(self):
        self.press_redact_button()
        time.sleep(1)
        self.press_add_icon_button()
        self.check_disable_fields_in_work_experience_form()
        self.check_128_in_experience_tab()
        self.element_is_visible(self.locators.EXPERIENCES_EMPLOYER_FIELD).click()
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        time.sleep(0.5)
        self.element_is_visible(self.locators.EXPERIENCES_PROJECT_FIELD).click()
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()

        specializations = self.get_dropdown_menu_items(self.locators.EXPERIENCES_SPECIALIZATION_ACTION)
        assert specializations == ['Инжиниринг', 'Административно-управленческий персонал',
                                   'Блок ИТ'], "Не все значения в дропдауне Вид деятельности"
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_ACTION).click()
        time.sleep(1)
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
        time.sleep(1)
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        self.check_start_date_field()
        self.check_end_date_field()
        self.element_is_visible(self.locators.EXPERIENCES_KNOWLEDGE_FIELD).click()
        time.sleep(1)
        try:
            self.elements_are_visible(self.locators.LI_MENU_ITEM, 2)[0].click()
        except TimeoutException:
            assert self.element_is_displayed(self.locators.check_text('Нет данных')), \
                "При отсутствии знаний не отображается сообщение нет данных"
        self.press_save_button()

    @testit.step("Проверка максимального значения символов 64")
    @allure.step("Проверка максимального значения символов 64")
    def check_64_symbol(self, locator, locator_to_click):
        bed_value = ('Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed dia')
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys(bed_value)
        self.element_is_visible(locator_to_click).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        time.sleep(2)
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys('1')
        self.element_is_visible(locator_to_click).click()
        assert error_text == 'Максимальное количество символов: 64', \
            "Не появилось сообщение о превышении максимального количества символов"

    @testit.step("Проверка поля Работодатель при самостоятельном заполнении")
    @allure.step("Проверка поля Работодатель при самостоятельном заполнении")
    def field_custom_employer_field(self, employer_name):
        self.action_select_all_text(self.element_is_visible(self.locators.EXPERIENCES_EMPLOYER_FIELD))
        self.element_is_visible(self.locators.EXPERIENCES_EMPLOYER_FIELD).send_keys(employer_name)
        li_text = self.element_is_visible(self.locators.LI_MENU_ITEM).get_attribute('aria-label')
        assert li_text == f'Добавить работодателя "{employer_name}"'
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()

    @testit.step("Проверка поля Дата начала при самостоятельном заполнении")
    @allure.step("Проверка поля Дата начала при самостоятельном заполнении")
    def check_custom_begin_data_field(self):
        self.action_double_click(self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT))
        self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT).send_keys(self.get_day_before(-1))
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
        assert self.element_is_visible(self.locators.MUI_ERROR).text == 'Дата начала работы некорректна', \
            "Не появилось сообщение о некорректной дате"
        self.action_select_all_text(self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT))
        self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT).send_keys(self.get_day_before(22000))
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        time.sleep(2)
        self.action_select_all_text(self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT))
        self.element_is_visible(self.locators.EXPERIENCES_BEGIN_DATA_INPUT).send_keys(self.get_day_before(2))
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
        assert error_text == 'Дата начала работы некорректна', "Не появилось сообщение о некорректной дате"

    @testit.step("Проверка формы Опыт работы с самостоятельным заполнением")
    @allure.step("Проверка формы Опыт работы с самостоятельным заполнением")
    def field_work_experience_form_with_new_employer(self):
        self.press_redact_button()
        time.sleep(1)
        self.press_add_icon_button()
        time.sleep(2)
        self.field_custom_employer_field("Новый работодатель")
        assert self.get_employer_field_text() == "Новый работодатель"
        self.check_128_symbol_in_field(self.locators.EXPERIENCES_CUSTOM_PROJECT_FIELD, self.locators.check_text('Проект'))
        self.check_64_symbol(self.locators.EXPERIENCES_SPECIALIZATION_SLOT, self.locators.check_text('Проект'))
        self.check_custom_begin_data_field()
        self.element_is_visible(self.locators.EXPERIENCES_KNOWLEDGE_FIELD).click()
        time.sleep(1)
        try:
            self.elements_are_visible(self.locators.LI_MENU_ITEM, 2)[0].click()
        except TimeoutException:
            print("В системе нет знаний")
        self.press_save_button()

    @testit.step("Проверка удаления блока опыт работы в резюме")
    @allure.step("Проверка удаления блока опыт работы в резюме")
    def check_delete_block_experience_in_resume(self):
        self.action_move_to_element(self.elements_are_visible(self.locators.WYSIWYG_TITLES)[3])
        self.element_is_visible(self.locators.ADD_EXPERIENCE_BUTTON).click()
        assert self.element_is_displayed(self.locators.EXPERIENCE_PROJECT_NAME), "Не добавлен блок опыт работы"
        self.element_is_visible(self.locators.DELETE_ICON).click()
        assert not self.element_is_displayed(self.locators.EXPERIENCE_PROJECT_NAME, 1), "Блок опыт работы не удалился"

    @testit.step("Проверка создания резюме с неуникальным именем")
    @allure.step("Проверка создания резюме с неуникальным именем")
    def check_resume_with_non_unique_name(self, name):
        self.action_select_all_text(self.element_is_visible(self.locators.RESUME_TITLE_FIELD))
        self.element_is_visible(self.locators.RESUME_TITLE_FIELD).send_keys(name)
        self.element_is_visible(self.locators.RESUME_POST_FIELD).send_keys('Администратор')
        self.action_double_click(self.elements_are_visible(self.locators.DATE_PIKERS)[1])
        self.elements_are_visible(self.locators.DATE_PIKERS)[1].send_keys('01.02.1990')
        self.action_double_click(self.elements_are_visible(self.locators.DATE_PIKERS)[2])
        self.elements_are_visible(self.locators.DATE_PIKERS)[2].send_keys(self.get_day_before(0))
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        return self.element_is_visible(self.locators.MUI_ERROR).text

    @testit.step("Проверка создания резюме без заполнения обязательных полей")
    @allure.step("Проверка создания резюме без заполнения обязательных полей")
    def check_adding_the_resume_without_filling_in_a_required_field(self):
        assert not self.element_is_clickable(self.locators.SAVE_BUTTON, 1), "Кнопка сохранить не задизейблена"
        self.element_is_visible(self.locators.RESUME_DIRECTION_FIELD).send_keys('1')
        assert self.element_is_clickable(self.locators.SAVE_BUTTON, 1), "Кнопка сохранить задизейблена"
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(1)
        assert len(self.elements_are_visible(self.locators.MUI_ERROR)) == 2, \
            "Под обязательными полями не отображаются сообщения"
        assert self.elements_are_visible(self.locators.MUI_ERROR)[0].text == 'Поле обязательно', \
            "Не корректные сообщения под обязательными полями"
        assert 'Заполнены не все обязательные поля' in self.get_alert_message(), \
            "Не появился тост об обязательности полей"

    @testit.step("Проверка отмены создания резюме")
    @allure.step("Проверка отмены создания резюме")
    def check_cancel_adding_resume(self):
        resume_title = self.element_is_visible(self.locators.RESUME_TITLE_FIELD).get_attribute('value')
        self.element_is_visible(self.locators.BREAK_BUTTON).click()
        assert self.element_is_displayed(self.locators.check_text('Резюме не сохранится. Закрыть режим создания?')), \
            "Отсутствует сообщение о несохранении резюме"
        assert self.element_is_displayed(self.locators.BREAK_IN_MODAL), "Отсутствует кнопка отменить"
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return resume_title

    @testit.step("Проверка наличия имени резюме")
    @allure.step("Проверка наличия имени резюме")
    def check_resume_name(self, name):
        return self.element_is_displayed(self.locators.check_text(name), 2)

    @testit.step("Проверка выборы даты окончания работы на проекте раньше даты начала")
    @allure.step("Проверка выборы даты окончания работы на проекте раньше даты начала")
    def check_selecting_an_end_date_earlier_than_the_start_date(self):
        self.element_is_visible(self.locators.ADD_EXPERIENCE_BUTTON).click()
        self.element_is_visible(self.locators.RESUME_EXPERIENCE_START_DATE).send_keys(self.get_day_before(0))
        self.element_is_visible(self.locators.RESUME_EXPERIENCE_END_DATE).send_keys(self.get_day_before(1))
        self.element_is_visible(self.locators.EXPERIENCE_PROJECT_NAME).click()
        assert (self.elements_are_visible(self.locators.MUI_ERROR)[0].text ==
                'Дата начала работы на проекте не должна быть позже даты завершения'), \
            "Нет сообщения о не корректной дате начала работы на проекте"
        assert (self.elements_are_visible(self.locators.MUI_ERROR)[1].text ==
                'Дата окончания работы на проекте не должна быть раньше даты начала'), \
            "Нет сообщения о не корректной дате окончания работы на проекте"

    @testit.step("Проверка выбора даты начала работы в компании после текущего дня")
    @allure.step("Проверка выбора даты начала работы в компании после текущего дня")
    def check_entering_a_date_after_that_day_in_the_start_date_of_work_at_the_company_field(self):
        self.action_select_all_text(self.element_is_visible(self.locators.START_WORK_IN_RESUME))
        self.element_is_visible(self.locators.START_WORK_IN_RESUME).send_keys(self.get_day_before(-1))
        self.element_is_visible(self.locators.RESUME_DIRECTION_FIELD).click()
        assert self.element_is_visible(self.locators.MUI_ERROR).text == 'Нельзя выбрать будущую дату', \
            "Нет сообщения о невозможности выбора будущей даты"
        self.elements_are_visible(self.locators.DATE_PIKERS_ICON)[0].click()
        assert not self.element_is_clickable(self.locators.NEXT_DAY_IN_PICKER, 1), \
            "Можно выбрать будущую дату в дата-пикере"

    @testit.step("Проверка выхода из просмотра резюме")
    @allure.step("Проверка выхода из просмотра резюме")
    def check_exit_resume_viewing_mode(self, resume_name):
        time.sleep(1)
        self.element_is_visible(self.locators.SEARCH_RESUME_NAME_FIELDS).send_keys(resume_name)
        time.sleep(1)
        self.elements_are_visible(self.locators.KEBAB_MENU)[0].click()
        self.element_is_visible(self.locators.KEBABS_VIEW_ITEM).click()
        assert self.element_is_displayed(
            self.locators.PRINT_BUTTON), "Не произошел переход на страницу просмотра резюме"
        self.element_is_visible(self.locators.BREAK_VIEW_BUTTON).click()
        assert self.element_is_displayed(self.locators.CREATE_RESUME_BUTTON), "Не произошло возвращение в таб резюме"

    @testit.step("Копирование резюме")
    @allure.step("Копирование резюме")
    def copy_resume(self, name):
        time.sleep(1)
        self.element_is_visible(self.locators.SEARCH_RESUME_NAME_FIELDS).send_keys(name)
        time.sleep(1)
        self.elements_are_visible(self.locators.KEBAB_MENU)[0].click()
        self.element_is_visible(self.locators.KEBABS_COPY_ITEM).click()

    @testit.step("Отмена удаления резюме")
    @allure.step("Отмена удаления резюме")
    def cancel_delete_resume(self, name):
        self.action_select_all_text(self.element_is_visible(self.locators.SEARCH_RESUME_NAME_FIELDS))
        self.element_is_visible(self.locators.SEARCH_RESUME_NAME_FIELDS).send_keys(name)
        time.sleep(0.5)
        self.elements_are_visible(self.locators.KEBAB_MENU)[0].click()
        time.sleep(0.5)
        self.element_is_visible(self.locators.KEBABS_DEL_MENU_ITEM).click()
        self.element_is_visible(self.locators.BREAK_BUTTON).click()

    @testit.step("Редактирование резюме")
    @allure.step("Редактирование резюме")
    def redact_resume(self, name):
        self.action_select_all_text(self.element_is_visible(self.locators.SEARCH_RESUME_NAME_FIELDS))
        self.element_is_visible(self.locators.SEARCH_RESUME_NAME_FIELDS).send_keys(name)
        time.sleep(0.5)
        self.elements_are_visible(self.locators.KEBAB_MENU, 7)[0].click()
        time.sleep(0.5)
        self.element_is_visible(self.locators.KEBABS_REDACT_ITEM).click()

    @testit.step("Изменение данных в резюме")
    @allure.step("Изменение данных в резюме")
    def change_resume(self, new_name):
        time.sleep(1)
        self.action_select_all_text(self.element_is_visible(self.locators.RESUME_TITLE_FIELD))
        self.element_is_visible(self.locators.RESUME_TITLE_FIELD).send_keys(new_name)
        time.sleep(1)
        self.action_double_click(self.elements_are_visible(self.locators.DATE_PIKERS)[1])
        self.elements_are_visible(self.locators.DATE_PIKERS)[1].send_keys('01.02.1990')
        self.action_double_click(self.elements_are_visible(self.locators.DATE_PIKERS)[2])
        self.elements_are_visible(self.locators.DATE_PIKERS)[2].send_keys(self.get_day_before(0))
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

    @testit.step("Очистка обязательных полей в резюме")
    @allure.step("Очистка обязательных полей в резюме")
    def clear_required_fields(self):
        time.sleep(2)
        self.action_select_all_text(self.element_is_visible(self.locators.RESUME_FULL_NAME_FIELD))
        self.element_is_visible(self.locators.RESUME_FULL_NAME_FIELD).send_keys(Keys.BACK_SPACE)
        time.sleep(0.5)
        self.action_select_all_text(self.element_is_visible(self.locators.RESUME_TITLE_FIELD))
        self.element_is_visible(self.locators.RESUME_TITLE_FIELD).send_keys(Keys.BACK_SPACE)
        time.sleep(0.5)
        self.action_select_all_text(self.element_is_visible(self.locators.RESUME_POST_FIELD))
        self.element_is_visible(self.locators.RESUME_POST_FIELD).send_keys(Keys.BACK_SPACE)
        time.sleep(0.5)
        self.action_select_all_text(self.element_is_visible(self.locators.START_WORK_IN_RESUME))
        self.element_is_visible(self.locators.START_WORK_IN_RESUME).send_keys(Keys.BACK_SPACE)
        time.sleep(0.5)
        self.action_double_click(self.elements_are_visible(self.locators.DATE_PIKERS)[2])
        self.elements_are_visible(self.locators.DATE_PIKERS)[2].send_keys(Keys.BACK_SPACE)
        time.sleep(0.5)
        self.action_double_click(self.elements_are_visible(self.locators.DATE_PIKERS)[1])
        self.elements_are_visible(self.locators.DATE_PIKERS)[1].send_keys(Keys.BACK_SPACE)
        time.sleep(0.5)
        self.element_is_visible(self.locators.RESUME_FULL_NAME_FIELD).click()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(3)

    @testit.step("Получение количества предупреждения об обязательности поля")
    @allure.step("Получение количества предупреждения об обязательности поля")
    def len_required_errors(self):
        return len(self.elements_are_present(self.locators.REQUIRED_FIELD_ERROR))

    @testit.step("Получение текста ошибки")
    @allure.step("Получение текста ошибки")
    def get_mui_error(self):
        return self.element_is_visible(self.locators.MUI_ERROR).text

    @testit.step("Добавление пустой формы заполнения контакта")
    @allure.step("Добавление пустой формы заполнения контакта")
    def add_contact_form(self):
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        assert self.element_is_displayed(self.locators.CONTACT_DETAILS_FIELD), "Нет поля реквизит контакта"
        assert self.element_is_displayed(self.locators.CONTACT_DELETE_BUTTON), "Нет кнопки удаления"

    @testit.step("Заполнение добавленной формы контакта")
    @allure.step("Заполнение добавленной формы контакта")
    def filling_contact_form(self):
        self.element_is_visible(self.locators.CONTACT_TYPE_FIELD).send_keys('Контакт')
        self.element_is_visible(self.locators.CONTACT_DETAILS_FIELD).send_keys('123')

    @testit.step("Проверка отображения добавленного контакта")
    @allure.step("Проверка отображения добавленного контакта")
    def check_added_contact(self):
        assert self.element_is_displayed(self.locators.CONTACT_TYPE_FIELD), "Тип контакта не сохранился"
        assert self.element_is_displayed(self.locators.CONTACT_DETAILS_FIELD), "Реквизит контакта не сохранился"

    @testit.step("Удаление добавленного контакта")
    @allure.step("Удаление добавленного контакта")
    def delete_added_contact(self):
        self.element_is_visible(self.locators.CONTACT_DELETE_BUTTON).click()

    @testit.step("Получение текстов всех ошибок")
    @allure.step("Получение текстов всех ошибок")
    def get_all_mui_errors(self):
        mui_errors = self.elements_are_visible(self.locators.MUI_ERROR)
        errors_text = []
        for error in mui_errors:
            errors_text.append(error.text)
        return errors_text

    @testit.step("Ввод пробела в поля формы контакта")
    @allure.step("Ввод пробела в поля формы контакта")
    def space_input_contact_form(self):
        self.element_is_visible(self.locators.CONTACT_TYPE_FIELD).send_keys(' ')
        self.element_is_visible(self.locators.CONTACT_DETAILS_FIELD).send_keys(' ')

    @testit.step("Проверка что удаленный контакт удален")
    @allure.step("Проверка что удаленный контакт удален")
    def check_delete_contact(self):
        assert not self.element_is_displayed(self.locators.CONTACT_TYPE_FIELD, 2), "Тип контакта не удалился"
        assert not self.element_is_displayed(self.locators.CONTACT_DETAILS_FIELD,2), "Реквизит контакта не удалился"

    @testit.step("Переход на таб заметки на странице коллеги")
    @allure.step("Переход на таб заметки на странице коллеги")
    def go_to_colleague_profile(self):
        self.element_is_visible(self.locators.TAB_NOTE).click()

    @testit.step("Проверка содержания таба заметки")
    @allure.step("Проверка содержания таба заметки")
    def check_note_tab(self):
        assert self.element_is_displayed(self.locators.MESSAGE_ON_TAB), "Нет сообщения на странице"
        assert self.element_is_displayed(self.locators.TEXT_FIELD_WITH_VISIVIG), "Нет визивига"

    @testit.step("Ввод текста в пустое поле заметки")
    @allure.step("Ввод текста в пустое поле заметки")
    def put_text_in_note(self, put_text):
        self.action_select_all_text(self.element_is_visible(self.locators.EDITOR_CONTENT))
        self.element_is_visible(self.locators.EDITOR_CONTENT).send_keys(put_text)

    @testit.step("Сохранение заметки")
    @allure.step("Сохранение заметки")
    def save_note(self):
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(1)

    @testit.step("Проверка что заметка сохранилась")
    @allure.step("Проверка что заметка сохранилась")
    def check_save_note(self, put_text):
        self.element_is_visible(self.locators.TAB_EXPERIENCE).click()
        self.element_is_visible(self.locators.TAB_NOTE).click()
        assert self.element_is_displayed(self.locators.check_text(put_text)), 'Заметка не сохранилась'

    @testit.step("Проверка что заметка не видна адресату")
    @allure.step("Проверка что заметка не видна адресату")
    def check_note_not_visible_addressee(self, put_text):
        self.element_is_visible(self.locators.PROFILE_BUTTON).click()
        self.element_is_visible(self.locators.MY_PROFILE_MENU_ITEM).click()
        self.element_is_visible(self.locators.TAB_NOTE).click()
        assert not self.element_is_displayed(self.locators.check_text(put_text)), "Заметка видна адресату"

    @testit.step("Проверка что заметка не видна не автору")
    @allure.step("Проверка что заметка не видна не автору")
    def check_note_not_visible_non_author(self, put_text):
        self.element_is_visible(self.locators.PROFILE_BUTTON).click()
        self.element_is_visible(self.locators.MY_PROFILE_MENU_ITEM).click()
        self.element_is_visible(self.locators.TAB_NOTE).click()
        assert not self.element_is_displayed(self.locators.check_text(put_text)), "Заметка видна не автору"

    @testit.step("Взять текст ранее сохраненной заметки")
    @allure.step("Взять текст ранее сохраненной заметки")
    def take_previously_saved_note(self):
        return self.element_is_visible(self.locators.EDITOR_CONTENT).text

    @testit.step("Сравнение текстов заметок")
    @allure.step("Сравнение текстов заметок")
    def notes_comparison(self, put_text):
        assert self.take_previously_saved_note != put_text, 'Заметка не изменилась'

    @testit.step("Получение текста поля работодатель")
    @allure.step("Получение текста поля работодатель")
    def get_employer_field_text(self):
        return self.element_is_visible(self.locators.EXPERIENCES_EMPLOYER_FIELD).get_attribute('value')

    @testit.step("Заполнение поля проект")
    @allure.step("Заполнение поля проект")
    def field_project_field(self, project_name):
        self.action_select_all_text(self.element_is_visible(self.locators.EXPERIENCES_CUSTOM_PROJECT_FIELD))
        self.element_is_visible(self.locators.EXPERIENCES_CUSTOM_PROJECT_FIELD).send_keys(project_name)

    @testit.step("Получение текста поля проект")
    @allure.step("Получение текста поля проект")
    def get_project_field_text(self):
        return self.element_is_visible(self.locators.EXPERIENCES_CUSTOM_PROJECT_FIELD).get_attribute('value')

    @testit.step("Заполнение поля проектная роль")
    @allure.step("Заполнение поля проектная роль")
    def field_project_role_field(self, role_name):
        self.action_select_all_text(self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT))
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).send_keys(role_name)

    @testit.step("Получение текста поля проектная роль")
    @allure.step("Получение текста поля проектная роль")
    def get_project_role_field_text(self):
        return self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).get_attribute('value')

    @testit.step("Заполнение поля знания")
    @allure.step("Заполнение поля знания")
    def field_knowledge_field(self):
        self.element_is_visible(self.locators.EXPERIENCES_KNOWLEDGE_WHEN_FIELD).click()
        time.sleep(1)
        try:
            self.elements_are_visible(self.locators.LI_MENU_ITEM, 2)[0].click()
        except TimeoutException:
            print("В системе нет знаний")

    @testit.step("Проверка поля Дата окончания работы при самостоятельном заполнении")
    @allure.step("Проверка поля Дата окончания работы при самостоятельном заполнении")
    def check_custom_end_data_field(self):
        self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT).send_keys(self.get_day_before(3))
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        time.sleep(2)
        self.action_select_all_text(self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT))
        self.element_is_visible(self.locators.EXPERIENCES_END_DATA_INPUT).send_keys(self.get_day_before(0))
        self.element_is_visible(self.locators.EXPERIENCES_SPECIALIZATION_SLOT).click()
        assert error_text == 'Дата окончания работы не может быть раньше начала', \
            "Не появилось сообщение о некорректной дате"

    @testit.step("Получение текста полей input")
    @allure.step("Получение текста полей input")
    def get_all_fields(self):
        all_fields = self.elements_are_visible(self.locators.INPUT_PLACEHOLDER)
        text_list = []
        for field in all_fields:
            text_list.append(field.get_attribute('value'))
        return text_list

    @allure_testit_step('Проверка наличия Аватара')
    def check_foto(self):
        assert self.element_is_displayed(self.locators.AVATAR_CHECK), "Нет аватара пользователя"

    @allure_testit_step('Проверка наличия должности в верхней части страницы')
    def check_header_post(self):
        assert self.element_is_displayed(self.locators.HEADER_POST), "Нет должности пользователя"

    @allure_testit_step('Проверка наличия кнопки редактирования')
    def check_redact_button(self):
        assert self.element_is_displayed(self.locators.REDACT_BUTTON), "Нет кнопки редактирования"

    @allure_testit_step('Проверка наличия вкладок в профиле пользователя')
    def check_tab_text(self):
        tab_titles = [element.text for element in self.elements_are_visible(self.locators.TAB_TITLES)]
        assert tab_titles == ['ИНФОРМАЦИЯ О СОТРУДНИКЕ', 'ГРАФИК РАБОТЫ', 'ОБРАЗОВАНИЕ', 'СЕРТИФИКАТЫ', 'ОПЫТ РАБОТЫ',
                              'ЗАМЕТКИ', 'МЕТКИ', 'РЕЗЮМЕ', 'АКТИВНОСТЬ', 'ПОДРАЗДЕЛЕНИЯ И ДОЛЖНОСТИ', 'HR-КАРТОЧКА']

    @allure_testit_step('Проверка наличия вкладок в профиле пользователя глазами пользователя')
    def check_tab_text_on_user(self):
        tab_titles = [element.text for element in self.elements_are_visible(self.locators.TAB_TITLES)]
        assert tab_titles == ['ИНФОРМАЦИЯ О СОТРУДНИКЕ', 'ГРАФИК РАБОТЫ', 'ОБРАЗОВАНИЕ', 'СЕРТИФИКАТЫ', 'ОПЫТ РАБОТЫ',
                              'ЗАМЕТКИ', 'МЕТКИ', 'РЕЗЮМЕ', 'HR-КАРТОЧКА']

    @allure_testit_step('Получение названия активной вкладки')
    def get_activ_tab(self):
        return self.element_is_visible(self.locators.ACTIV_TAB).text

    @allure_testit_step('Получение названий всех полей')
    def get_all_labels_text(self):
        return [element.text for element in self.elements_are_visible(self.locators.LABELS)]

    @allure_testit_step('Получение значений всех полей')
    def get_all_input_values_text(self):
        return [element.get_attribute('value') for element in self.elements_are_present(self.locators.ALL_INPUT_VALUES)]

    @allure_testit_step('Проверка наличия заголовка Теги')
    def check_tags_title(self):
        assert self.element_is_displayed(self.locators.check_text('Теги')), "Нет заголовка теги"

    @allure_testit_step('Переход на страницу мой профиль с проверкой пунктов меню')
    def go_to_user_profile_with_check_menu_items(self):
        self.element_is_visible(self.locators.PROFILE_BUTTON).click()
        items = [element.text for element in self.elements_are_visible(self.locators.ALL_PROFILE_MENU_ITEMS_TEXT)]
        self.element_is_visible(self.locators.MY_PROFILE_MENU_ITEM).click()
        return items

    @allure_testit_step('Проверка наличия кнопок сохранить и отмены')
    def check_save_and_break_buttons(self):
        assert self.element_is_displayed(self.locators.SAVE_BUTTON)
        assert self.element_is_displayed(self.locators.BREAK_BUTTON)

    @allure_testit_step('Проверка некликабельности полей в разделе Общие данные')
    def check_not_clickable_information_bloc_fields(self):
        assert not self.element_is_clickable(self.locators.POST_FIELD, 1), "Поле должность можно редактировать"
        assert not self.element_is_clickable(self.locators.DEPARTMENT_FIELD, 1), "Поле подразделение можно редактировать"
        assert not self.element_is_clickable(self.locators.HEAD_FIELD, 1), "Поле Непосредственный руководитель можно редактировать"
        assert not self.element_is_clickable(self.locators.STATUS_FIELD, 1), "Поле статус можно редактировать"

    @allure_testit_step('Проверка формата работы')
    def return_all_job_format(self):
        chips_text = [element.text for element in self.elements_are_visible(self.locators.JOB_FORMAT_CHIPS)]
        self.element_is_visible(self.locators.JOB_FORMAT_FIELD).click()
        dropdown_text = [element.text for element in self.elements_are_visible(self.locators.LI_MENU_ITEM)]
        dropdown_text.extend(chips_text)
        self.action_esc()
        return sorted(dropdown_text)

    @allure_testit_step('Проверка некликабельности полей в Прием в компанию и Вступление в должность')
    def check_not_clickable_start_work_fields(self):
        assert self.elements_are_visible(self.locators.START_WORK_ON_USER)[0].get_attribute('disabled'), \
            "Поле прием в компанию можно редактировать"
        assert self.elements_are_visible(self.locators.START_WORK_ON_USER)[1].get_attribute('disabled'), \
            "Поле вступление в должность можно редактировать"

    @allure_testit_step('Проверка присутствия кнопки Добавить контакт')
    def check_add_contact_button(self):
        assert self.element_is_displayed(self.locators.ADD_BUTTON), "Кнопка добавить контакт отсутствует"

    @allure_testit_step('Проверка дропдауна семейное положение')
    def check_family_status(self):
        self.element_is_visible(self.locators.FAMILY_STATUS).click()
        dropdown_text = [element.text for element in self.elements_are_visible(self.locators.LI_MENU_ITEM)]
        self.action_esc()
        assert dropdown_text == ['Не в браке', 'В браке'], "Есть не все варианты семейного положения"

    @allure_testit_step('Проверка наличия иконки Добавить')
    def check_add_icon(self):
        assert self.element_is_displayed(self.locators.ADD_ICON), "Отсутствует иконка Добавить"

    @allure_testit_step('Проверка наличия визивига')
    def check_wisivig(self):
        assert self.element_is_displayed(self.locators.TEXT_FIELD_WITH_VISIVIG), "Нет визивига"

    @allure_testit_step('Проверка наличия кнопки сохранить')
    def check_submit_button(self):
        assert self.element_is_displayed(self.locators.SUBMIT_BUTTON), "Нет кнопки Сохранить"

    @allure_testit_step('Проверка заголовков таблицы вкладки Резюме')
    def check_resume_tab_column(self):
        column_text = [element.text for element in self.elements_are_visible(self.locators.RESUME_TAB_COLUMN)]
        assert column_text == ['Название', 'Дата создания', 'Дата редактирования', 'Действия'], \
            "В таблице есть не все заголовки"

    @allure_testit_step('Проверка элементов кебаб меню вкладки Резюме')
    def check_resume_kebab_menu(self):
        self.elements_are_visible(self.locators.KEBAB_MENU)[0].click()
        assert [element.text for element in self.elements_are_visible(self.locators.KEBAB_MENU_ITEM)] == [
            'Редактирование', 'Просмотр резюме', 'Копировать', 'Удалить'], "Есть не все элементы кебаб меню"
        self.action_esc()

    @allure_testit_step('Проверка наличия кнопки создать резюме')
    def check_create_resume_button(self):
        assert self.element_is_displayed(self.locators.CREATE_RESUME_BUTTON), "Нет кнопки создать резюме"

    @allure_testit_step('Переход на вкладку График работы')
    def go_to_schedule_tab(self):
        self.element_is_visible(self.locators.SCHEDULE_TAB_BUTTON).click()

    @allure_testit_step('Переход на вкладку Метки')
    def go_to_labels_tab(self):
        self.element_is_visible(self.locators.LABELS_TAB_BUTTON).click()

    @allure_testit_step('Получение текста с чипсы рабочего дня')
    def get_text_on_chips(self, number_element):
        return self.elements_are_visible(self.locators.ALL_CHIPS_BUTTON)[number_element].text

    @allure_testit_step('Проверка полей с рабочими часами')
    def check_hours_in_day_fields(self):
        assert len(self.elements_are_visible(self.locators.WORK_HOURS_IN_DAY)) == 24, \
            'Не над каждым днем отображаются рабочие часы'

    @allure_testit_step('Получение статуса пользователя')
    def get_user_status(self):
        return self.element_is_visible(self.locators.STATUS_FIELD).get_attribute('value')

    @allure_testit_step('Получение формата работы пользователя')
    def get_job_format(self):
        return self.element_is_visible(self.locators.JOB_FORMAT_CHIPS).text

    @allure_testit_step('Отмена редактирования профиля пользователя')
    def abort_redact(self):
        time.sleep(1)  # Без этого ожидания не всегда нажимается кнопка
        self.element_is_visible(self.locators.BREAK_BUTTON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()