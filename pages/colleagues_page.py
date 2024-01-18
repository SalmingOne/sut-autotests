
import allure

from locators.colleagues_page_locators import ColleaguesPageLocators
from pages.base_page import BasePage


class ColleaguesPage(BasePage):
    locators = ColleaguesPageLocators()

    @allure.step("Переход на страницу все коллеги")
    def go_colleagues_page(self):
        self.element_is_visible(self.locators.COLLEAGUES_TAB).click()
        self.element_is_visible(self.locators.ALL_COLLEAGUES).click()

    @allure.step("Проверка заголовка Коллеги")
    def check_colleagues_title(self):
        assert self.element_is_displayed(self.locators.COLLEAGUES_TITLE), "Нет заголовка Коллеги"

    @allure.step("Проверка вкладок на странице Коллеги")
    def check_colleagues_page_tabs(self):
        colleagues_page_tabs = self.elements_are_visible(self.locators.ALL_COLLEAGUES_TABS_BUTTONS)
        tabs_names = []
        for i in colleagues_page_tabs:
            tabs_names.append(i.text)
        assert tabs_names == ['ОТДЕЛ', 'ФИЛИАЛ', 'ВСЕ'], "Есть не все вкладки"

    @allure.step("Проверка поля поиска")
    def check_search_field(self):
        assert self.element_is_displayed(self.locators.SEARCH_FIELD), "Нет поля поиска"

    @allure.step("Проверка кнопки перехода на расширенный поиск")
    def check_to_advanced_search_button(self):
        assert self.element_is_displayed(self.locators.TO_ADVANCED_SEARCH), "Нет кнопки расширенного поиска"

    @allure.step("Проверка подзаголовка")
    def check_subtitle(self):
        assert self.element_is_displayed(self.locators.SUBTITLE), "Нет подзаголовка"

    @allure.step("Проверка иконки настройки отображения столбцов")
    def check_setting_icon(self):
        assert self.element_is_displayed(self.locators.SETTING_ICON), "Нет иконки настройки отображения"

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

    @allure.step("Проверка перехода на страницу пользователя")
    def check_user_name_link(self):
        self.elements_are_visible(self.locators.USER_NAME_LINK)[0].click()
        assert self.element_is_displayed(self.locators.CHECK_GO_TO_USER_PAGE), "Мы не перешли на страницу пользователя"

