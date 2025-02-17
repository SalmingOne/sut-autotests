import time

import allure
import testit
from selenium.webdriver import Keys
from datetime import datetime

from locators.header_search_locators import HeaderSearchLocators
from pages.base_page import BasePage

class HeaderSearchPage(BasePage):
    locators = HeaderSearchLocators()

    @testit.step("Выбор поля Поиск в хедере")
    @allure.step("Выбор поля Поиск в хедере")
    def select_search_field_header(self):
        self.element_is_visible(self.locators.SEARCH_HEADER_FIELD).click()

    @testit.step("Проверка тултипа поля Поиск в хедере")
    @allure.step("Проверка тултипа поля Поиск в хедере")
    def check_tooltip_in_header_search(self):
        self.element_is_visible(self.locators.SEARCH_HEADER_FIELD).send_keys(Keys.RETURN)
        assert self.element_is_visible(self.locators.TOOLTIP).text == 'Введите значение для поиска', "Не появился тултип или его текст не корректен"

    @testit.step("Проверка сообщения Ничего не найдено")
    @allure.step("Проверка сообщения Ничего не найдено")
    def check_nothing_found_text(self):
        self.element_is_visible(self.locators.SEARCH_HEADER_FIELD).send_keys('ацывжы')
        assert self.element_is_visible(self.locators.NOTHING_FOUND_TEXT).text == 'Ничего не найдено', "Не появилось сообщение"

    @testit.step("Ввод пробела в поле поиска")
    @allure.step("Ввод пробела в поле поиска")
    def entering_a_space_in_the_header_search(self):
        self.element_is_visible(self.locators.SEARCH_HEADER_FIELD).send_keys(' ')

    @testit.step("Ввод 2 символов в поле поиска")
    @allure.step("Ввод 2 символов в поле поиска")
    def entering_2_letters_in_header_search(self):
        self.element_is_visible(self.locators.SEARCH_HEADER_FIELD).send_keys('пр')

    @testit.step("Проверка отсутствия дропдауна при введении менее 3 символов")
    @allure.step("Проверка отсутствия дропдауна при введении менее 3 символов")
    def check_dropdown_not_visible(self):
        assert not self.element_is_displayed(self.locators.SEARCH_RESULTS_LIST, timeout=1), "Дропдаун отображается при введении менее 3 символов"

    @testit.step("Ввод третьего символа в поле поиска")
    @allure.step("Ввод третьего символа в поле поиска")
    def entering_3th_letter_in_header_search(self):
        self.element_is_visible(self.locators.SEARCH_HEADER_FIELD).send_keys('о')

    @testit.step("Проверка наличия двух и менее проектов")
    @allure.step("Проверка наличия двух и менее проектов")
    def check_projects_in_dropdown_2_or_less(self):
        assert len(self.elements_are_visible(self.locators.SEARCH_RESULTS_PROJECTS_LIST)) <= 2, "Проектов в дропдауне больше двух"

    @testit.step("Проверка наличия двух и менее пользователей")
    @allure.step("Проверка наличия двух и менее пользователей")
    def check_users_in_dropdown_2_or_less(self):
        assert len(self.elements_are_visible(self.locators.SEARCH_RESULTS_USERS_LIST)) <= 2, "Пользователей в дропдауне больше двух"

    @testit.step("Переход на страницу Быстрый поиск")
    @allure.step("Переход на страницу Быстрый поиск")
    def go_to_quick_search_page(self):
        self.element_is_visible(self.locators.SEARCH_HEADER_FIELD).send_keys(Keys.ENTER)

    @testit.step("Проверка наличия табов на странице Быстрый поиск")
    @allure.step("Проверка наличия табов на странице Быстрый поиск")
    def quick_search_page_tab(self):
        assert self.element_is_displayed(self.locators.TAB_ALL), "Нет таба Все"
        assert self.element_is_displayed(self.locators.TAB_USERS), "Нет таба Пользователи"
        assert self.element_is_displayed(self.locators.TAB_PROJECTS), "Нет таба Проекты"

    @testit.step("Проверка отображения пользователей в алфавитном порядке")
    @allure.step("Проверка отображения пользователей в алфавитном порядке")
    def check_users_in_alphabetical_order(self):
        users_list = self.elements_are_visible(self.locators.QUICK_SEARCH_USERS_LIST)
        users = []
        for user in users_list:
            users.append(user.text)
        assert users == sorted(users), "Пользователи не в алфавитном порядке"

    @testit.step("Проверка отображения проектов в хронологическом порядке")
    @allure.step("Проверка отображения проектов в хронологическом порядке")
    def check_projects_in_chronological_order(self):
        projects_list = self.elements_are_visible(self.locators.QUICK_SEARCH_PROJECTS_LIST)
        projects = []
        for project in projects_list:
            projects.append(project.text[0:10])
        new = []
        for a in projects:
            new.append(datetime.strptime(a, '%d.%m.%Y'))
        assert new == sorted(new), 'Проекты не в хронологическом порядке'

    @testit.step("Переход на страницу пользователя")
    @allure.step("Переход на страницу пользователя")
    def go_to_user_page_from_quick_search(self):
        self.element_is_visible(self.locators.QUICK_SEARCH_USERS_LIST).click()

    @testit.step("Проверка открытия страницы пользователя")
    @allure.step("Проверка открытия страницы пользователя")
    def check_page_after_redirect(self):
        assert self.element_is_displayed(self.locators.GO_TO_USER_PAGE), 'Страница пользователя не открылась'







