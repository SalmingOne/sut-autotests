import time

from locators.stacks_page_locators import StacksPageLocators
from pages.base_page import BasePage
from utils.concat_testit_allure_step import allure_testit_step


class StacksPage(BasePage):
    locators = StacksPageLocators()

    @allure_testit_step('Переход на справочник Стеки')
    def go_to_stacks_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.REFERENCE_BOOKS).click()
        self.element_is_visible(self.locators.STACKS_TAB).click()

    @allure_testit_step('Нажатие кнопки добавить стек')
    def press_add_stack_button(self):
        self.element_is_visible(self.locators.ADD_STACK_BUTTON).click()

    @allure_testit_step('Проверка максимальной длины поля')
    def check_max_field_length(self, locator, max_length, locator_to_color, locator_to_click, new_value):
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys('A' * (max_length + 1))
        self.element_is_visible(locator_to_click).click()
        error = self.element_is_visible(self.locators.MUI_ERROR).text
        name_field_color = self.element_is_present(locator_to_color).value_of_css_property('border-color')
        assert name_field_color == 'rgb(211, 47, 47)', "Цвет поля не красный"
        time.sleep(1)
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 2), \
            "Кнопка Добавить активна при не корректном заполнении поля"
        self.action_select_all_text(self.element_is_visible(locator))
        self.element_is_visible(locator).send_keys(new_value)
        self.element_is_visible(locator_to_click).click()
        return error

    @allure_testit_step('Негативные проверки поля Стек')
    def check_name_field(self):
        self.element_is_visible(self.locators.DEPARTMENT_FIELD).click()
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        self.add_skill_to_stack()
        self.element_is_visible(self.locators.NAME_FIELD).click()
        self.element_is_visible(self.locators.text_on_page('Действия')).click()
        assert self.element_is_visible(self.locators.MUI_ERROR).text == 'Поле обязательно', \
            "Нет сообщения об обязательности поля"
        name_field_color = self.element_is_present(self.locators.NAME_FIELD_COLOR).value_of_css_property('border-color')
        assert name_field_color == 'rgb(211, 47, 47)', "Цвет поля Стек не красный"
        time.sleep(1)
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 2), \
            "Кнопка Сохранить активна при не корректном заполнении поля Стек"
        error = self.check_max_field_length(
            self.locators.NAME_FIELD,
            255,
            self.locators.NAME_FIELD_COLOR,
            self.locators.text_on_page('Действия'),
            'AAA'
        )
        assert error == 'Превышено допустимое количество символов: 255', \
            "Не появилось сообщение о превышении допустимого количества символов в поле Стек"

    @allure_testit_step('Проверка поля Отдел')
    def check_department_field(self):
        self.action_move_to_element(self.element_is_visible(self.locators.DEPARTMENT_FIELD))
        self.element_is_visible(self.locators.CLEAR_DEPARTMENT_FIELD).click()
        self.element_is_visible(self.locators.text_on_page('Действия')).click()
        assert self.element_is_visible(
            self.locators.MUI_ERROR).text == 'Поле обязательно', "Нет сообщения об обязательности поля Отдел"
        name_field_color = self.element_is_present(self.locators.DEPARTMENT_FIELD_COLOR).value_of_css_property('border-color')
        assert name_field_color == 'rgb(211, 47, 47)', "Цвет поля Отдел не красный"
        time.sleep(1)
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 2), \
            "Кнопка Сохранить активна при не корректном заполнении поля Отдел"
        self.element_is_visible(self.locators.DEPARTMENT_FIELD).click()
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()

    @allure_testit_step('Проверка с неуникальным названием стека')
    def check_not_unique_name(self, new_name):
        self.action_select_all_text(self.element_is_visible(self.locators.NAME_FIELD))
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(new_name)
        self.element_is_visible(self.locators.text_on_page('Действия')).click()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        assert self.element_is_visible(self.locators.MUI_ERROR).text == "Cтек c данным названием существует", \
            "Не появилось сообщение о не уникальном названии стека"
        name_field_color = self.element_is_present(self.locators.NAME_FIELD_COLOR).value_of_css_property(
            'border-color')
        assert name_field_color == 'rgb(211, 47, 47)', "Цвет поля Стек не красный"
        time.sleep(1)
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 2), \
            "Кнопка Сохранить активна при не корректном заполнении поля Стек"
        self.action_select_all_text(self.element_is_visible(self.locators.NAME_FIELD))
        self.element_is_visible(self.locators.NAME_FIELD).send_keys('Уникальное имя')

    @allure_testit_step('Добавление одного знания в стек')
    def add_skill_to_stack(self):
        self.element_is_visible(self.locators.ADD_SKILL_BUTTON).click()
        self.element_is_visible(self.locators.SKILL_NAME_INPUT).click()
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        self.element_is_visible(self.locators.text_on_page('Добавление навыка/знания в стек')).click()
        self.element_is_visible(self.locators.ADD_STACK_BUTTON).click()

    @allure_testit_step('Удаление одного знания из стека')
    def delete_one_skill_from_stack(self):
        self.element_is_visible(self.locators.DELETE_SKILL_BUTTON).click()
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()

    @allure_testit_step('Проверка отображения тултипа при отсутствии знаний')
    def check_no_skill(self):
        assert not self.element_is_clickable(self.locators.SUBMIT_BUTTON, 2), \
            "Кнопка Сохранить активна при отсутствии знаний"
        self.action_move_to_element(self.element_is_visible(self.locators.SUBMIT_BUTTON))
        assert self.element_is_visible(self.locators.TOOLTIP).text == 'Необходимо добавить хотя бы один навык или знание', \
            "Не появился тултип или текст тултипа не корректен"
