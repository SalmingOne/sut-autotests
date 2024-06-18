import time

import allure
import testit
from selenium.webdriver import Keys

from locators.user_profile_page_locators import UserProfilePageLocators
from pages.base_page import BasePage


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
        return self.element_is_visible(self.locators.EDUCATION_TAB_BUTTON).value_of_css_property('background-color')

    @testit.step("Берем цвет вкладки Сертификаты")
    @allure.step("Берем цвет вкладки Сертификаты")
    def get_certificate_tab_color(self):
        return self.element_is_visible(self.locators.CERTIFICATE_TAB_BUTTON).value_of_css_property('background-color')

    @testit.step("Берем цвет вкладки Опыт работы")
    @allure.step("Берем цвет вкладки Опыт работы")
    def get_experience_tab_color(self):
        return self.element_is_visible(self.locators.EXPERIENCES_TAB_BUTTON).value_of_css_property('background-color')

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

    @testit.step("Получение даты начала работы")
    @allure.step("Получение даты начала работы")
    def get_start_work_date(self):
        return self.element_is_visible(self.locators.START_WORK).get_attribute('value')

    @testit.step("Нажатие кнопки создать резюме")
    @allure.step("Нажатие кнопки создать резюме")
    def press_create_resume_button(self):
        self.element_is_visible(self.locators.CREATE_RESUME_BUTTON).click()

    @testit.step("Проверка значений по умолчанию")
    @allure.step("Проверка значений по умолчанию")
    def check_default_values(self, name, start_work):
        resume_title = self.element_is_visible(self.locators.RESUME_TITLE_FIELD).get_attribute('value')
        full_name = self.element_is_visible(self.locators.RESUME_FULL_NAME_FIELD).get_attribute('value')
        start_work_resume = self.element_is_visible(self.locators.START_WORK_IN_RESUME).get_attribute('value')

        assert self.get_day_before_y_m_d(0) and name in resume_title,\
            'Название резюме по умолчанию не содержит ФИО пользователя или текущую дату'
        assert name == full_name, 'ФИО не подтянулось из карточки пользователя'
        assert start_work == start_work_resume, 'Дата начала работы в компании не подтянулась из профиля'

    @testit.step("Проверка ограничения в 255 символов для поля")
    @allure.step("Проверка ограничения в 255 символов для поля")
    def check_255_symbol_in_field(self, locator):
        bed_value = ('Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt'
                     ' ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci'
                     ' tation ullamcorper suscipit lobortis nisl ut aliquip ex ea co')
        self.element_is_visible(locator).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(locator).send_keys(bed_value)
        self.element_is_visible(self.locators.START_WORK_IN_RESUME).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        time.sleep(2)
        self.element_is_visible(locator).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(locator).send_keys('1')
        self.element_is_visible(self.locators.START_WORK_IN_RESUME).click()
        assert error_text == 'Максимальное количество символов: 255', \
            "Не появилось сообщение о превышении максимального количества символов"

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
        assert self.element_is_visible(self.locators.TOOLTIP).text == 'Пример: Разработчик, Developer, Аналитик, Lead QA и т.д.',\
            'Не корректный тултип при наведении на поле должность'

    @testit.step("Проверка тултипа поля Место проживания")
    @allure.step("Проверка тултипа поля Место проживания")
    def check_direction_tooltip(self):
        self.action_move_to_element(self.element_is_visible(self.locators.RESUME_DIRECTION_FIELD))
        assert self.element_is_visible(self.locators.TOOLTIP).text == 'Пример: Россия, Москва',\
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

    @testit.step("Проверка кнопки Сохранить")
    @allure.step("Проверка кнопки Сохранить")
    def check_disable_save_button(self):
        assert not self.element_is_clickable(self.locators.SAVE_BUTTON), 'Кнопка сохранить не задизейблена'

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
        self.elements_are_visible(self.locators.DATE_PIKERS)[1].send_keys(Keys.CONTROL + 'a')
        self.elements_are_visible(self.locators.DATE_PIKERS)[1].send_keys('01.02.1990')
        self.elements_are_visible(self.locators.DATE_PIKERS)[2].send_keys(Keys.CONTROL + 'a')
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
        self.elements_are_visible(self.locators.SEARCH_FIELDS)[1].send_keys(name)
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

    @testit.step("Получение текста с поля дети")
    @allure.step("Получение текста с поля дети")
    def get_children_text(self):
        return self.element_is_visible(self.locators.CHILDREN_TEXT_AREA).text

    @testit.step("Добавление текста в поле дети")
    @allure.step("Добавление текста в поле дети")
    def change_children_text(self, text):
        self.element_is_visible(self.locators.CHILDREN_TEXT_AREA).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.CHILDREN_TEXT_AREA).send_keys(text)

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

