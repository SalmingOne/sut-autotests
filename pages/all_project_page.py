import time

import allure
import testit
from selenium.webdriver.common.by import By

from locators.all_project_page_locators import AllProjectPageLocators
from pages.base_page import BasePage


class AllProjectPage(BasePage):
    locators = AllProjectPageLocators()

    @testit.step("Переходим через меню на страницу все проекты")
    @allure.step("Переходим через меню на страницу все проекты")
    def go_to_all_project_page(self):
        time.sleep(1)
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_PROJECTS))
        self.element_is_visible(self.locators.TAB_ALL_PROJECTS).click()

    @testit.step("Проверяем, что имя проекта есть на странице")
    @allure.step("Проверяем, что имя проекта есть на странице")
    def check_project_name_at_all(self, project_name):
        check_name_at_all = self.element_is_present(self.locators.check_project_name_on_tab(project_name), 2).text
        return check_name_at_all

    @testit.step("Удаляем проект")
    @allure.step("Удаляем проект")
    def delete_project(self, project_name):

        self.element_is_visible(self.locators.project_action_button(project_name)).click()
        self.element_is_visible(self.locators.PROJECT_DELETE_BUTTON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)  # Если не поставить явное ожидание драйвер закроется раньше чем, удалится проект

    @testit.step("Включаем фильтр проект во всех статусах")
    @allure.step("Включаем фильтр проект во всех статусах")
    def see_all_status_project(self):
        time.sleep(1)
        self.element_is_visible(self.locators.STATUS_FILTER_BUTTON).click()
        self.element_is_visible(self.locators.MARK_ALL_STATUS).click()
        time.sleep(2)
        self.action_esc()
        time.sleep(1)

    @testit.step("Переходим на страницу проекта по имени")
    @allure.step("Переходим на страницу проекта по имени")
    def go_project_page(self, name):
        project_title = (By.XPATH, f'//div[@col-id="name"]//div[text()="{name}"]')
        self.element_is_visible(project_title).click()

    @testit.step("Проверяем меню Проекты в шапке сайта")
    @allure.step("Проверяем меню Проекты в шапке сайта")
    def check_all_projects_tab_menu_item(self):
        time.sleep(1)
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_PROJECTS))
        menu_items = self.elements_are_visible(self.locators.ALL_PROJECTS_MENU_ITEMS)
        menu_items_names = []
        for item in menu_items:
            menu_items_names.append(item.text)
        self.action_move_to_element(self.element_is_visible(self.locators.STATUS_FILTER_BUTTON))
        assert 5 >= len(menu_items_names) >= 3, "В меню отображается более трех проектов"
        assert 'Создать проект' and 'Посмотреть все' in menu_items_names, "В меню отсутствуют пункты Создать проект и Посмотреть все"

    @testit.step("Проверяем заголовок Проекты")
    @allure.step("Проверяем заголовок Проекты")
    def check_title(self):
        assert self.element_is_displayed(self.locators.TAB_TITLE), "Нет заголовка Проекты"

    @testit.step("Проверяем кнопку создания нового проекта")
    @allure.step("Проверяем кнопку создания нового проекта")
    def check_create_project_button(self):
        assert self.element_is_displayed(self.locators.CREATE_PROJECT_BUTTON), "Нет кнопки создания нового проекта"

    @testit.step("Проверяем наличие чекбокса Только мои проекты")
    @allure.step("Проверяем наличие чекбокса Только мои проекты")
    def check_only_my_projects_checkbox(self):
        assert self.element_is_displayed(self.locators.ONLY_MY_PROJECTS_CHECKBOX), "Нет чекбокса Только мои проекты"

    @testit.step("Проверяем наличие всех столбцов таблицы")
    @allure.step("Проверяем наличие всех столбцов таблицы")
    def check_tab_column_titles(self):
        tab_titles = self.elements_are_visible(self.locators.TAT_COLUMN_TITLES)
        tab_title_names = []
        for title in tab_titles:
            tab_title_names.append(title.text)
        assert tab_title_names == ['Название', 'Код', 'Дата начала', 'Дата окончания', 'Статус',
                                   'Действия'], "В таблице есть не все столбцы"

    @testit.step("Проверяем наличие всех пунктов меню Действия")
    @allure.step("Проверяем наличие всех пунктов меню Действия")
    def check_action_menu_items(self):
        self.elements_are_visible(self.locators.ALL_ACTION_BUTTONS)[0].click()
        menu_items = self.elements_are_visible(self.locators.ACTION_MENU_ITEMS)
        menu_items_names = []
        for item in menu_items:
            menu_items_names.append(item.text)
        assert menu_items_names == ['В архив', 'Удалить'], "Есть не все пункты меню Действия"
