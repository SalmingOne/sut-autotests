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

    @allure_testit_step('Нажатие кнопки добавить знание/навык')
    def press_add_skill_button(self):
        self.element_is_visible(self.locators.ADD_SKILL_BUTTON).click()

    @allure_testit_step('Проверка дровера добавления знания/навыка')
    def check_add_skill_drawer(self):
        self.check_skill_type_field()
        # Навыки
        self.element_is_visible(self.locators.text_on_page('Знание')).click()
        self.element_is_visible(self.locators.SKILL_NAME_INPUT).click()
        knowledge = [element.text for element in self.elements_are_visible(self.locators.LI_MENU_ITEM)]
        self.action_esc()
        # Знания
        self.element_is_visible(self.locators.SKILL_TYPE_INPUT).click()
        self.element_is_visible(self.locators.text_on_page('Навык')).click()
        self.element_is_visible(self.locators.SKILL_NAME_INPUT).click()
        skills = [element.text for element in self.elements_are_visible(self.locators.LI_MENU_ITEM)]
        self.action_esc()
        assert not self.element_is_clickable(self.locators.DESCRIPTION_FIELD), "Поле описание кликабельно"
        assert self.element_is_displayed(self.locators.ADD_STACK_BUTTON), "Отсутствует кнопка Добавить"
        assert self.element_is_displayed(self.locators.BREAK_BUTTON), "Отсутствует кнопка Отменить"
        return skills, knowledge

    @allure_testit_step('Проверка поля тип')
    def check_skill_type_field(self):
        default_value = self.element_is_visible(self.locators.SKILL_TYPE_INPUT).get_attribute('value')
        self.element_is_visible(self.locators.SKILL_TYPE_INPUT).click()
        types = [element.text for element in self.elements_are_visible(self.locators.LI_MENU_ITEM)]
        assert default_value == 'Навык', "По умолчанию в поле тип выбрано не значение Навык"
        assert types == ['Навык', 'Знание'], "В дропдауне есть не все доступные значения"

    @allure_testit_step('Проверка выбора типа')
    def check_choose_type(self):
        self.element_is_visible(self.locators.SKILL_TYPE_INPUT).click()
        item_in_drawer = self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].text
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        item_in_field = self.element_is_visible(self.locators.SKILL_TYPE_INPUT).get_attribute('value')
        assert item_in_drawer == item_in_field, "Выбранный тип не отображается в поле"

    @allure_testit_step('Проверка выбора названия')
    def check_choose_name(self):
        self.element_is_visible(self.locators.SKILL_NAME_INPUT).click()
        item_in_drawer = self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].text
        self.elements_are_visible(self.locators.LI_MENU_ITEM)[0].click()
        item_in_field = self.element_is_visible(self.locators.SKILL_NAME_INPUT).get_attribute('value')
        self.element_is_visible(self.locators.text_on_page('Добавление навыка/знания в стек')).click()
        assert item_in_drawer == item_in_field, "Выбранное название не отображается в поле"
        return item_in_field

    @allure_testit_step('Получение имен всех добавленных в стек знаний/навыков')
    def get_all_skills_name_in_tab(self):
        if self.element_is_displayed(self.locators.SKILLS_NAMES, 2):
            return [element.get_attribute('aria-label') for element in self.elements_are_visible(self.locators.SKILLS_NAMES)]
        else:
            return []

    @allure_testit_step('Нажатие кнопки отменить')
    def press_break_button(self):
        self.element_is_visible(self.locators.BREAK_BUTTON).click()

    @allure_testit_step('Проверка отображения описания знания/навыка')
    def check_description(self, skill_json):
        self.element_is_visible(self.locators.SKILL_TYPE_INPUT).click()
        if skill_json['type'] == 'skill':
            self.element_is_visible(self.locators.li_by_text('Навык')).click()
        else:
            self.element_is_visible(self.locators.li_by_text('Знание')).click()
        self.element_is_visible(self.locators.SKILL_NAME_INPUT).click()
        self.element_is_visible(self.locators.li_by_text(skill_json['name'])).click()
        in_field = self.element_is_visible(self.locators.DESCRIPTION_FIELD).get_attribute('value')
        self.element_is_visible(self.locators.text_on_page('Добавление навыка/знания в стек')).click()
        assert in_field == skill_json['description'], "В поле описание не подтянулось соответствующее значение"

    @allure_testit_step('Проверка отсутствия уже добавленного знания/навыка в дровере Название')
    def check_selected_skill_not_in_drawer(self, skill_json):
        self.element_is_visible(self.locators.SKILL_TYPE_INPUT).click()
        time.sleep(1)
        if skill_json['type'] == 'skill':
            self.element_is_visible(self.locators.li_by_text('Навык')).click()
        else:
            self.element_is_visible(self.locators.li_by_text('Знание')).click()
        self.element_is_visible(self.locators.SKILL_NAME_INPUT).click()
        skills = [element.text for element in self.elements_are_visible(self.locators.LI_MENU_ITEM)]
        assert skill_json['name'] not in skills, "Добавленный навык доступен для выбора в дровере"

    @allure_testit_step('Нажатие кнопки удаления первого навыка в таблице')
    def press_delete_skill_button(self):
        self.elements_are_visible(self.locators.DELETE_SKILL_BUTTON)[0].click()

    @allure_testit_step('Проверка элементов модального окна')
    def check_delete_skill_modal_window(self):
        assert self.element_is_displayed(self.locators.text_on_page('Вы уверены, что хотите удалить')), \
            "Нет текста сообщения в модальном окне"
        assert self.element_is_displayed(self.locators.CONFIRM_BUTTON), "Нет кнопки Подтвердить"
        assert self.element_is_displayed(self.locators.MODAL_BREAK_BUTTON), "Нет кнопки Отменить"

    @allure_testit_step('Нажатие кнопки отмены удаления в модальном окне')
    def press_modal_break_button(self):
        self.element_is_visible(self.locators.MODAL_BREAK_BUTTON).click()

    @allure_testit_step('Нажатие кнопки Просмотр стека')
    def press_view_stack_button(self, stack_name):
        self.element_is_visible(self.locators.kebab_by_stack_name(stack_name)).click()
        self.element_is_visible(self.locators.KEBABS_VIEW_MENU_ITEM).click()

    @allure_testit_step('Получение заголовков страницы просмотра стека')
    def get_h6_titles(self):
        return [element.text for element in self.elements_are_present(self.locators.TITLES)]

    @allure_testit_step('Проверка наличия кнопок Редактировать и Закрыть')
    def check_view_tab_buttons(self):
        assert self.element_is_displayed(self.locators.REDACT_BUTTON), "Нет кнопки Редактировать"
        assert self.element_is_displayed(self.locators.CLOSE_BUTTON), "Нет кнопки Закрыть"
