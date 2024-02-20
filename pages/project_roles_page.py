import time

import allure
import testit
from selenium.webdriver import Keys

from locators.project_roles_page_locators import ProjectRolesPageLocators
from pages.base_page import BasePage


class ProjectRolesPage(BasePage):
    locators = ProjectRolesPageLocators()

    @testit.step("Переход на таблицу Проектные роли")
    @allure.step("Переход на таблицу Проектные роли")
    def go_to_project_roles_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.PERSONAL_QUALITIES_PAGE).click()
        self.element_is_visible(self.locators.PROJECT_ROLES_TAB).click()

    @testit.step("Открываем дровер создания проектной роли")
    @allure.step("Открываем дровер создания проектной роли")
    def open_create_role_drawer(self):
        self.element_is_visible(self.locators.CREATE_ROLE_BUTTON).click()

    @testit.step("Заполняем поле Проектная роль с превышением максимального количества символов")
    @allure.step("Заполняем поле Проектная роль с превышением максимального количества символов")
    def check_max_size_role_name(self):
        self.element_is_visible(self.locators.INPUT_ROLE_NAME_FIELD).send_keys(
            'роль роль роль роль роль роль роль роль роль роль р')
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_visible(self.locators.INPUT_ROLE_NAME_FIELD).clear()
        assert error_text == 'Максимальное количество символов: 50', "Не появилось сообщение о превышении максимального количества символов"

    @testit.step("Проверяем, что отображается введенный цвет")
    @allure.step("Проверяем, что отображается введенный цвет")
    def check_color_on_color_input(self):
        self.element_is_visible(self.locators.COLOR_INPUT_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.COLOR_INPUT_FIELD).send_keys('#7f11e0')
        output_color = self.element_is_visible(self.locators.COLOR_INPUT_BUTTON).value_of_css_property(
            'background-color')
        assert output_color == 'rgba(127, 17, 224, 1)', "Введенный цвет не отображается на элементе"

    @testit.step("Проверяем, что поле Размер ставки не активно")
    @allure.step("Проверяем, что поле Размер ставки не активно")
    def salary_rate_not_clickable(self):
        assert not self.element_is_clickable(self.locators.SALARY_RATE_FIELD, 2), 'Поле размер ставки активно'

    @testit.step("Проверяем, что есть чекбокс Руководящая роль")
    @allure.step("Проверяем, что есть чекбокс Руководящая роль")
    def manger_role_checkbox_is_present(self):
        assert self.element_is_displayed(self.locators.MANAGER_ROLE_CHECKBOX), "Нет чекбокса Руководящая роль"

    @testit.step("Заполняем поле проектная роль")
    @allure.step("Заполняем поле проектная роль")
    def field_role_name(self, name):
        self.element_is_visible(self.locators.INPUT_ROLE_NAME_FIELD).send_keys(f"{name}")

    @testit.step("Выбираем первую ставу привлечения")
    @allure.step("Выбираем первую ставу привлечения")
    def field_first_attraction_rate(self):
        self.element_is_visible(self.locators.ATTRACTION_RATE_FIELD).click()
        self.elements_are_visible(self.locators.ALL_ATTRACTION_RATES)[0].click()

    @testit.step("Проверяем, что есть кнопка отмены")
    @allure.step("Проверяем, что есть кнопка отмены")
    def abort_button_is_present(self):
        assert self.element_is_displayed(self.locators.ABORT_BUTTON), "Нет кнопки отмены"

    @testit.step("Проверяем, что есть кнопка закрыть")
    @allure.step("Проверяем, что есть кнопка закрыть")
    def clear_drawer_button_is_present(self):
        assert self.element_is_displayed(self.locators.DRAWER_CLEAR_BUTTON), "Нет кнопки закрыть дровер"

    @testit.step("Нажимаем кнопку сохранить")
    @allure.step("Нажимаем кнопку сохранить")
    def submit_create_role(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверяем, что роль есть в таблице")
    @allure.step("Проверяем, что роль есть в таблице")
    def check_role_name_on_tab(self, name):
        return self.element_is_displayed(self.locators.get_role_by_name(name))

    @testit.step("Удаляем роль после прохождения тест-кейса")
    @allure.step("Удаляем роль после прохождения тест-кейса")
    def delete_project_role(self, name):
        self.elements_are_visible(self.locators.ROLE_SEARCH_FIELD)[1].send_keys(f"{name}")
        self.element_is_visible(self.locators.ROLE_KEBABS).click()
        self.element_is_visible(self.locators.DEL_BUTTON_IN_KEBAB_MENU).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)  # Без этого ожидания роль не успевает удалиться

    @testit.step("Проверяем, что кнопка сохранить задизейблена")
    @allure.step("Проверяем, что кнопка сохранить задизейблена")
    def submit_button_not_clickable(self):
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 2), "Кнопка Сохранить не задизейблена"

    @testit.step("Проверяем, что есть кнопка создания новой роли")
    @allure.step("Проверяем, что есть кнопка создания новой роли")
    def create_role_button_is_present(self):
        assert self.element_is_displayed(self.locators.CREATE_ROLE_BUTTON), "Нет кнопки создания роли"

    @testit.step("Проверяем заголовки таблицы Список ролей")
    @allure.step("Проверяем заголовки таблицы Список ролей")
    def check_roles_tab_headers(self):
        all_column = self.elements_are_present(self.locators.PROJECT_ROLES_TAB_HEADERS)
        column_names = []
        for name in all_column:
            column_names.append(name.text)
        assert column_names == ['Цвет', 'Роль', 'Ставка привлечения', 'Размер ставки'], "Есть не все заголовки таблицы"

    @testit.step("Проверяем, что есть кнопка создания новой роли")
    @allure.step("Проверяем, что есть кнопка создания новой роли")
    def check_search_fields(self):
        assert len(self.elements_are_visible(self.locators.ROLE_SEARCH_FIELD)) >= 3

    @testit.step("Проверяем, что есть три поля поиска")
    @allure.step("Проверяем, что есть три поля поиска")
    def check_filter_icons(self):
        assert len(self.elements_are_present(self.locators.FILTER_ICONS)) >= 3

    @testit.step("Проверяем, что есть кнопка действия и пункты кебаб меню")
    @allure.step("Проверяем, что есть кнопка действия и пункты кебаб меню")
    def check_kebab_menu_items(self):
        self.elements_are_visible(self.locators.ROLE_KEBABS)[0].click()
        all_menu_items = self.elements_are_visible(self.locators.KEBAB_MENU_ITEMS)
        item_names = []
        for name in all_menu_items:
            item_names.append(name.text)
        assert item_names == ['Редактировать', 'Удалить'], "Не все пункты есть в кебаб меню"
