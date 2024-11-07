import time

import allure
import testit
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from locators.all_project_page_locators import AllProjectPageLocators
from pages.base_page import BasePage
from utils.concat_testit_allure_step import allure_testit_step


class AllProjectPage(BasePage):
    locators = AllProjectPageLocators()

    @testit.step("Переходим через меню на страницу все проекты")
    @allure.step("Переходим через меню на страницу все проекты")
    def go_to_all_project_page(self):
        time.sleep(2)
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_PROJECTS))
        self.element_is_visible(self.locators.TAB_ALL_PROJECTS).click()
        try:
            self.element_is_visible(self.locators.KEBAB_MENU, 10)
        except TimeoutException:
            pass

    @testit.step("Проверяем, что имя проекта есть на странице")
    @allure.step("Проверяем, что имя проекта есть на странице")
    def check_project_name_at_all(self, project_name):
        assert self.element_is_displayed(self.locators.check_project_name_on_tab(project_name)), \
            "Имя созданного проекта отсутствует на странице все проекты"

    @testit.step("Удаляем проект")
    @allure.step("Удаляем проект")
    def delete_project(self, project_name):
        time.sleep(0.5)
        self.element_is_visible(self.locators.project_action_button(project_name)).click()
        time.sleep(1)
        self.element_is_visible(self.locators.PROJECT_DELETE_BUTTON).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON, 15).click()
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
        time.sleep(2)
        self.action_move_to_element(self.element_is_visible(self.locators.TAB_PROJECTS))
        time.sleep(2)
        menu_items = self.elements_are_visible(self.locators.ALL_PROJECTS_MENU_ITEMS)
        menu_items_names = []
        for item in menu_items:
            menu_items_names.append(item.text)
        time.sleep(1)
        assert 5 >= len(menu_items_names) >= 3, "В меню отображается более трех проектов"
        assert 'Создать проект' and 'Посмотреть все' in menu_items_names, "В меню отсутствуют пункты Создать проект и Посмотреть все"
        self.element_is_visible(self.locators.TAB_ALL_PROJECTS).click()

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
        assert tab_title_names == ['Название', 'Код', 'Руководитель проекта', 'Дата начала', 'Дата окончания',
                                   'Приоритет', 'Статус', 'Действия'], "В таблице есть не все столбцы"

    @testit.step("Проверяем наличие всех пунктов меню Действия")
    @allure.step("Проверяем наличие всех пунктов меню Действия")
    def check_action_menu_items(self):
        self.elements_are_visible(self.locators.ALL_ACTION_BUTTONS)[0].click()
        menu_items = self.elements_are_visible(self.locators.ACTION_MENU_ITEMS)
        menu_items_names = []
        for item in menu_items:
            menu_items_names.append(item.text)
        assert menu_items_names == ['В архив', 'Удалить'], "Есть не все пункты меню Действия"
        self.action_esc()

    @testit.step("Получаем все имена проектов на странице")
    @allure.step("Получаем все имена проектов на странице")
    def get_all_project_names_on_page(self):
        all_project = self.elements_are_visible(self.locators.ALL_PROJECTS_NAMES)
        names = []
        for name in all_project:
            names.append(name.text)
        return names

    @testit.step("Выбираем чекбокс только мои проекты")
    @allure.step("Выбираем чекбокс только мои проекты")
    def press_only_my_projects_checkbox(self):
        self.element_is_visible(self.locators.ONLY_MY_PROJECTS_CHECKBOX).click()

    @testit.step("Проверка удаления проекта")
    @allure.step("Проверка удаления проекта")
    def check_delete_project(self, project_name):
        time.sleep(4)
        self.element_is_visible(self.locators.project_action_button(project_name)).click()
        time.sleep(0.5)
        self.element_is_visible(self.locators.PROJECT_DELETE_BUTTON).click()
        dialog_text = self.element_is_visible(self.locators.ALERT_DIALOG_DESCRIPTION, 25).text
        assert self.element_is_displayed(self.locators.MODAL_ABORT_BUTTON)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        assert dialog_text == f'Вы уверены, что хотите удалить проект "{project_name}"?'
        time.sleep(1)  # Если не поставить явное ожидание драйвер закроется раньше чем, удалится проект

    @testit.step("Берем текст всех сообщений системы")
    @allure.step("Берем текст всех сообщений системы")
    def get_alert_message(self):
        all_alerts = self.elements_are_visible(self.locators.ALERT_MESSAGE)
        data = []
        for alert in all_alerts:
            data.append(alert.text)
        return data

    @testit.step("Проверка наличия имени проекта на странице")
    @allure.step("Проверка наличия имени проекта на странице")
    def get_project_on_tab(self, project_name):
        return self.element_is_displayed(self.locators.check_project_name_on_tab(project_name), 2)

    @testit.step("Проверка удаления проекта со списанными трудозатратами")
    @allure.step("Проверка удаления проекта со списанными трудозатратами")
    def check_delete_project_with_work(self, project_name):
        time.sleep(2)
        self.element_is_visible(self.locators.project_action_button(project_name)).click()
        time.sleep(0.5)
        self.element_is_visible(self.locators.PROJECT_DELETE_BUTTON).click()
        dialog_text = self.element_is_visible(self.locators.ALERT_TEXT, 25).text
        assert dialog_text == ('Удаление невозможно так как в проект списаны трудозатраты.'
                               ' Для скрытия проекта используйте архивацию.'), \
            "Не появилось сообщение о невозможности удаления проекта"

    @testit.step("Проверка архивирования проекта")
    @allure.step("Проверка архивирования проекта")
    def archiving_a_project(self, project_name):
        time.sleep(3)
        self.element_is_visible(self.locators.project_action_button(project_name)).click()
        time.sleep(0.5)
        self.element_is_visible(self.locators.PROJECT_ARCHIVING_BUTTON).click()
        dialog_text = self.element_is_visible(self.locators.ALERT_DIALOG_DESCRIPTION, 25).text
        assert dialog_text == (f'Вы уверены, что хотите переместить проект '
                               f'"{project_name}" в архив? Просмотр информации о проекте будет недоступен'), \
            "Не корректное сообщение в модальном окне"
        assert self.element_is_displayed(self.locators.MODAL_ABORT_BUTTON), \
            "В модальном окне отсутствует кнопка отменить"
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Проверка отображения архивного проекта в таблице")
    @allure.step("Проверка отображения архивного проекта в таблице")
    def check_archiving_a_project_on_tab(self, project_name):
        time.sleep(2)
        assert not self.element_is_displayed(self.locators.check_project_name_on_tab(project_name), 2), \
            "Проект виден без фильтра Архивный"
        self.see_all_status_project()
        assert self.element_is_visible(self.locators.check_project_status(project_name)).text == 'В архиве', \
            "У проекта статус не В архиве"
        assert self.element_is_displayed(self.locators.check_project_name_on_tab(project_name), 2), \
            "Проект не виден с фильтром Архивный"
        text_color = self.element_is_visible(self.locators.check_project_name_cojor_on_tab(project_name)).get_attribute('style')
        assert 'rgba(0, 0, 0, 0.4)' in text_color, "Цвет проекта не серый"
        self.element_is_visible(self.locators.check_project_name_on_tab(project_name)).click()

    @testit.step("Отмена архивации проекта")
    @allure.step("Отмена архивации проекта")
    def cancel_archiving_a_project(self, project_name):
        time.sleep(3)
        self.element_is_visible(self.locators.project_action_button(project_name)).click()
        time.sleep(0.5)
        self.element_is_visible(self.locators.PROJECT_ARCHIVING_BUTTON).click()
        self.element_is_visible(self.locators.MODAL_ABORT_BUTTON).click()

    @testit.step("Разархивация проекта")
    @allure.step("Разархивация проекта")
    def unzipping_the_project(self, project_name):
        time.sleep(3)
        self.element_is_visible(self.locators.project_action_button(project_name)).click()
        time.sleep(0.5)
        self.element_is_visible(self.locators.PROJECT_UNZIPPING_BUTTON).click()
        dialog_text = self.element_is_visible(self.locators.ALERT_DIALOG_DESCRIPTION, 25).text
        assert dialog_text == (f'Вы уверены, что хотите восстановить проект '
                               f'"{project_name}" из архива?'), \
            "Не корректное сообщение в модальном окне"
        assert self.element_is_displayed(self.locators.MODAL_ABORT_BUTTON), \
            "В модальном окне отсутствует кнопка отменить"
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Получение статуса проекта")
    @allure.step("Получение статуса проекта")
    def get_project_status(self, project_name):
        return self.element_is_visible(self.locators.check_project_status(project_name)).text

    @testit.step("Отмена разархивации проекта")
    @allure.step("Отмена разархивации проекта")
    def cansel_unzipping_the_project(self, project_name):
        time.sleep(3)
        self.element_is_visible(self.locators.project_action_button(project_name)).click()
        time.sleep(0.5)
        self.element_is_visible(self.locators.PROJECT_UNZIPPING_BUTTON).click()
        dialog_text = self.element_is_visible(self.locators.ALERT_DIALOG_DESCRIPTION, 25).text
        assert dialog_text == (f'Вы уверены, что хотите восстановить проект '
                               f'"{project_name}" из архива?'), \
            "Не корректное сообщение в модальном окне"
        assert self.element_is_displayed(self.locators.SUBMIT_BUTTON), \
            "В модальном окне отсутствует кнопка подтвердить"
        self.element_is_visible(self.locators.MODAL_ABORT_BUTTON).click()

    @allure_testit_step("Получение текста тултипа")
    def get_tooltip(self):
        return self.element_is_visible(self.locators.TOOLTIP).text

    @allure_testit_step("Наведение курсора на имя проекта")
    def move_to_project_name(self, project_name):
        self.action_move_to_element(self.element_is_visible(self.locators.check_project_name_on_tab(project_name)))
