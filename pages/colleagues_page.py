
import allure
import testit

from locators.colleagues_page_locators import ColleaguesPageLocators
from pages.base_page import BasePage


class ColleaguesPage(BasePage):
    locators = ColleaguesPageLocators()

    @testit.step("Переход на страницу все коллеги")
    @allure.step("Переход на страницу все коллеги")
    def go_colleagues_page(self):
        self.element_is_visible(self.locators.COLLEAGUES_TAB).click()
        self.element_is_visible(self.locators.ALL_COLLEAGUES).click()

    @testit.step("Проверка заголовка Коллеги")
    @allure.step("Проверка заголовка Коллеги")
    def check_colleagues_title(self):
        assert self.element_is_displayed(self.locators.COLLEAGUES_TITLE), "Нет заголовка Коллеги"

    @testit.step("Проверка вкладок на странице Коллеги")
    @allure.step("Проверка вкладок на странице Коллеги")
    def check_colleagues_page_tabs(self):
        colleagues_page_tabs = self.elements_are_visible(self.locators.ALL_COLLEAGUES_TABS_BUTTONS)
        tabs_names = []
        for i in colleagues_page_tabs:
            tabs_names.append(i.text)
        assert tabs_names == ['ОТДЕЛ', 'ФИЛИАЛ', 'ВСЕ'], "Есть не все вкладки"

    @testit.step("Проверка поля поиска")
    @allure.step("Проверка поля поиска")
    def check_search_field(self):
        assert self.element_is_displayed(self.locators.SEARCH_FIELD), "Нет поля поиска"

    @testit.step("Проверка кнопки перехода на расширенный поиск")
    @allure.step("Проверка кнопки перехода на расширенный поиск")
    def check_to_advanced_search_button(self):
        assert self.element_is_displayed(self.locators.TO_ADVANCED_SEARCH), "Нет кнопки расширенного поиска"

    @testit.step("Проверка подзаголовка")
    @allure.step("Проверка подзаголовка")
    def check_subtitle(self):
        assert self.element_is_displayed(self.locators.SUBTITLE), "Нет подзаголовка"

    @testit.step("Проверка иконки настройки отображения столбцов")
    @allure.step("Проверка иконки настройки отображения столбцов")
    def check_setting_icon(self):
        assert self.element_is_displayed(self.locators.SETTING_ICON), "Нет иконки настройки отображения"

    @testit.step("Проверка заголовков столбцов таблицы Коллеги")
    @allure.step("Проверка заголовков столбцов таблицы Коллеги")
    def check_column_titles(self):
        column_titles = self.elements_are_visible(self.locators.COLUMN_TITLES)
        titles_text = []
        for i in column_titles:
            titles_text.append(i.text)
        try:
            titles_text.remove('Действия')
        except ValueError:
            pass
        assert titles_text == ['ФИО', 'Должность', 'Контакты', 'Статус'], "Не все заголовки таблицы Коллеги"

    @testit.step("Проверка перехода на страницу пользователя")
    @allure.step("Проверка перехода на страницу пользователя")
    def check_user_name_link(self):
        self.elements_are_visible(self.locators.USER_NAME_LINK)[0].click()
        assert self.element_is_displayed(self.locators.CHECK_GO_TO_USER_PAGE), "Мы не перешли на страницу пользователя"

    @testit.step("Поиск пользователя по фамилии")
    @allure.step("Поиск пользователя по фамилии")
    def search_user(self, second_name):
        self.element_is_visible(self.locators.ALL_COLLEAGUES_TAB).click()
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(second_name)

    @testit.step("Просмотр системы глазами пользователя")
    @allure.step("Просмотр системы глазами пользователя")
    def check_watch_the_user_eyes(self):
        self.element_is_visible(self.locators.WATCH_USER_EYES_BUTTONS).click()
        assert self.element_is_displayed(self.locators.check_text_on_page('Трудозатраты')), 'Мы не на странице трудозатрат'
        self.element_is_visible(self.locators.RETURN_TO_PROFILE_BUTTON).click()
        assert self.element_is_displayed(self.locators.check_text_on_page('Коллеги')), 'Мы не на странице коллеги'

    @testit.step("Переход на таб заметки на странице коллеги")
    @allure.step("Переход на таб заметки на странице коллеги")
    def go_to_colleague_profile(self):
        self.element_is_visible(self.locators.USER_NAME_LINK).click()
        self.element_is_visible(self.locators.TAB_NOTE).click()

    @testit.step("Проверка содержания таба заметки")
    @allure.step("Проверка содержания таба заметки")
    def check_note_tab(self):
        assert self.element_is_displayed(self.locators.MESSAGE_ON_TAB, 1), "Нет сообщения на странице"
        assert self.element_is_displayed(self.locators.TEXT_FIELD_WITH_VISIVIG, 1), "Нет визивига"
        #Раскомментировать после решения вопроса об удалении заметки из бд
        #assert not self.element_is_clickable(self.locators.SAVE_BUTTON, 1), "Кнопка сохранения не задизейблена"

    @testit.step("Проверка что поле заметки пустое")
    @allure.step("Проверка что поле заметки пустое")
    def check_note_empty(self):
        assert self.element_is_present(self.locators.NOTE_TEXT_EMPTY, 1), "Поле заметки не пустое"

    @testit.step("Ввод текста в поле заметки")
    @allure.step("Ввод текста в поле заметки")
    def put_text_in_note(self, put_text):
        self.element_is_present(self.locators.NOTE_TEXT_EMPTY).send_keys(put_text)

    @testit.step("Сохранение заметки")
    @allure.step("Сохранение заметки")
    def save_note(self):
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

    @testit.step("Проверка что заметка сохранилась")
    @allure.step("Проверка что заметка сохранилась")
    def check_save_note(self, put_text):
        self.element_is_visible(self.locators.TAB_EXPERIENCE).click()
        self.element_is_visible(self.locators.TAB_NOTE).click()
        assert self.locators.check_text_on_page(put_text), 'Заметка не сохранилась'

    @testit.step("Проверка что заметка не видна адресату")
    @allure.step("Проверка что заметка не видна адресату")
    def check_note_not_visible_addressee(self):
        self.element_is_visible(self.locators.WATCH_USER_EYES_BUTTONS).click()
        self.element_is_visible(self.locators.PROFILE_BUTTON).click()
        self.element_is_visible(self.locators.MY_PROFILE_MENU_ITEM).click()
        self.element_is_visible(self.locators.TAB_NOTE).click()
        assert self.element_is_present(self.locators.NOTE_TEXT_EMPTY, 1), "Заметка видна адресату"
        self.element_is_visible(self.locators.RETURN_TO_PROFILE_BUTTON).click()

    @testit.step("Проверка что заметка не видна не автору")
    @allure.step("Проверка что заметка не видна не автору")
    def check_note_not_visible_non_author(self, name):
        self.element_is_visible(self.locators.WATCH_USER_EYES_BUTTONS).click()
        self.element_is_visible(self.locators.COLLEAGUES_TAB).click()
        self.element_is_visible(self.locators.ALL_COLLEAGUES).click()
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(name)
        self.element_is_visible(self.locators.USER_NAME_LINK).click()
        self.element_is_visible(self.locators.TAB_NOTE).click()
        assert self.element_is_present(self.locators.NOTE_TEXT_EMPTY, 1), "Заметка видна не автору"
        self.element_is_visible(self.locators.RETURN_TO_PROFILE_BUTTON).click()

