from locators.system_role_page_locators import SystemRolePageLocators
from utils.concat_testit_allure_step import allure_testit_step
from pages.base_page import BasePage
import time


class SystemRolePage(BasePage):
    locators = SystemRolePageLocators()

    @allure_testit_step("Переход на таблицу Системные роли")
    def go_to_system_roles_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.SYSTEM_ROLE).click()
        time.sleep(2)
        self.element_is_visible(self.locators.ADMIN_SYSTEM_ROLE_TAB).click()

    @allure_testit_step("Создание системной роли")
    def create_system_role(self, role_name):
        self.element_is_visible(self.locators.CREATE_SYSTEM_ROLE_BUTTON).click()
        self.element_is_visible(self.locators.INPUT_ROLE_FIELD).send_keys(role_name)
        self.elements_are_visible(self.locators.ALL_TAG_CHECKBOXES)[1].click()
        
    @allure_testit_step("Нажатие на кнопку добавления системной роли")
    def press_add_system_role_button(self):
        self.element_is_visible(self.locators.CREATE_SYSTEM_ROLE_BUTTON).click()

    @allure_testit_step("Нажатие кнопки Удаление системной роли")
    def press_delete_system_role(self):
        self.element_is_visible(self.locators.DELETE_ROLE_ICON).click()

    @allure_testit_step("Нажатие на кнопку Сохранить")
    def press_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @allure_testit_step("Нажатие на кнопку Отменить")
    def press_abort_button(self):
        self.element_is_visible(self.locators.ABORT_BUTTON).click()

    @allure_testit_step("Проверка отсутствия кнопки Сохранить")
    def check_submit_button_is_not_visible(self):
        self.element_is_not_visible(self.locators.SUBMIT_BUTTON)
        
    @allure_testit_step("Проверка наличия системной роли в дропдауне")
    def check_role_name_in_dropdown(self, role_name):
        assert role_name in self.get_all_role_names(), 'Роли нет в дропдауне'

    @allure_testit_step("Проверка отсутствия системной роли в дропдауне")
    def check_role_name_not_in_dropdown(self, role_name):
        assert not role_name in self.get_all_role_names(), 'Роль есть в дропдауне'

    @allure_testit_step("Получение списка системных ролей в дропдауне")
    def get_all_role_names(self):
        self.element_is_visible(self.locators.ROLE_FIELD).click()
        all_roles_element = self.elements_are_visible(self.locators.ALL_NAMES_IN_DROPDOWN)
        data =[]
        for element in all_roles_element:
            data.append(element.text)
        self.action_esc()
        return data

    @allure_testit_step("Выбор системной роли в дропдауне")
    def select_role_name_in_dropdown(self, role_name):
        self.element_is_visible(self.locators.LI_MENU_ITEM).click()
        self.element_is_visible(self.locators.get_name_in_dropdown(role_name)).click()

    @allure_testit_step("Проверка неактивности кнопки удаления системной роли")
    def check_delete_role_icon_is_disabled(self):
        assert self.element_is_visible(self.locators.DELETE_ROLE_ICON).get_attribute('disabled'), \
            "Кнопка удаления системной роли активна"

    @allure_testit_step("Получение тултипа невозможности удаления системной роли")
    def get_tooltip_text_impossibility_deleting_system_role_user(self):
        return self.element_is_visible(self.locators.TOOLTIP_ROLE_ICON).get_attribute('aria-label')
    
    @allure_testit_step("Удаление системной роли")
    def delete_system_role(self, role_name):
        self.element_is_visible(self.locators.ROLE_FIELD).click()
        self.element_is_visible(self.locators.get_name_in_dropdown(role_name)).click()
        self.element_is_visible(self.locators.DELETE_ROLE_ICON).click()
        self.element_is_visible(self.locators.SUBMIT_DELETE_ROLE_BUTTON).click()

    @allure_testit_step("Проверка на обязательные поля")
    def check_required_fields(self):
        self.press_submit_button()
        assert self.get_color_field() == 'rgb(211, 47, 47)', "Поле 'Название системной роли' не выделятся красным цветом"
        assert self.element_is_visible(self.locators.HELPER_TEXT).text == 'Поле обязательно', \
            "Под полем не отображается подсказка 'Поле обязательно'"
        
    @allure_testit_step("Проверка на обязательность тэгов")
    def check_required_tags(self, role_name):        
        self.element_is_visible(self.locators.INPUT_ROLE_FIELD).send_keys(role_name)
        self.press_submit_button()
        assert ('У новой роли должен быть хотя бы один тег' in self.get_all_alert_message(self.locators.ALERT_MESSAGE)), \
            "Не появилось сообщение о необходимости выбрать хотя бы один тег"
        
    @allure_testit_step("Проверка на уникальность названия системной роли")
    def check_uniqueness_system_role_name(self, role_name):
        self.elements_are_visible(self.locators.ALL_TAG_CHECKBOXES)[1].click()
        self.action_double_click(self.element_is_visible(self.locators.INPUT_ROLE_FIELD))
        self.element_is_visible(self.locators.INPUT_ROLE_FIELD).send_keys(role_name)
        self.press_submit_button()
        assert self.element_is_visible(self.locators.HELPER_TEXT).text == 'Системная роль с таким названием уже существует', \
            "Под полем не отображается подсказка что системная роль с таким названием уже существует"
        assert self.get_color_field() == 'rgb(211, 47, 47)', "Поле 'Название системной роли' не выделятся красным цветом"
        assert ('Системная роль с таким названием уже существует' in self.get_all_alert_message(self.locators.ALERT_MESSAGE)), \
            "Не появилось сообщение о существовании роли с таким названием"
        
    @allure_testit_step("Проверка на превышение символов в названии системной роли")
    def check_char_limit_system_role_name(self):
        self.action_double_click(self.element_is_visible(self.locators.INPUT_ROLE_FIELD))
        self.element_is_visible(self.locators.INPUT_ROLE_FIELD).send_keys('A'*101)
        self.press_submit_button()
        assert self.get_color_field() == 'rgb(211, 47, 47)', "Поле 'Название системной роли' не выделятся красным цветом"
        assert self.element_is_visible(self.locators.HELPER_TEXT).text == 'Максимальное количество символов: 100', \
            "Под полем не появилось сообщение о превышении допустимого количества символов"
        
    @allure_testit_step("Получение цвета выделения поля")
    def get_color_field(self):
        return self.element_is_present(self.locators.BORDER_COLOR).value_of_css_property('border-color')
    
    @allure_testit_step("Создание копии системной роли")
    def creating_copy_system_role(self, role_name):
        self.press_copy()
        self.check_modal_window_creating_copy(role_name)
        self.press_submit_button()
        role_name_copy = f'{role_name}_копия'
        assert role_name_copy in (self.element_is_visible(self.locators.INPUT_ROLE_FIELD)).get_attribute('value')
        self.press_submit_button()
        return role_name_copy

    @allure_testit_step("Нажатие на кнопку Копия")
    def press_copy(self):
        self.element_is_visible(self.locators.COPY_SYSTEM_ROLE).click()
    
    @allure_testit_step('Проверка модального окна создания копии')
    def check_modal_window_creating_copy(self, role_name):
        assert self.element_is_displayed(self.locators.SUBMIT_BUTTON), "Нет кнопки Подтвердить"
        assert self.element_is_displayed(self.locators.ABORT_BUTTON), 'Нет кнопки Отменить'
        assert f'Вы действительно хотите создать копию системной роли "{role_name}"?' \
            == self.element_is_visible(self.locators.ALERT_DIALOG).text, 'Некорректный вопрос подтверждения'

    @allure_testit_step(
        'Проверка модального окна при удалении системной роли, которая единственная присвоенная у пользователя')
    def check_modal_window_delete_only_one_system_role(self, role_name, user_name):
        assert self.element_is_displayed(self.locators.SUBMIT_BUTTON), "Нет кнопки Удалить"
        assert self.element_is_displayed(self.locators.ABORT_BUTTON), 'Нет кнопки Отменить'
        all_descriptions = self.elements_are_visible(self.locators.ALERT_DIALOG_ONE_ROLE)
        data = []
        for description in all_descriptions:
            data.append(description.text)
        assert f'Вы уверены, что хотите удалить системную роль {role_name}?' and \
               'У 1 пользователей эта роль единственная, необходимо выбрать новую системную роль.'\
               in data, 'Некорректный вопрос подтверждения'
        assert self.element_is_displayed(self.locators.get_name_in_dialog(user_name))

    @allure_testit_step(
        'Проверка модального окна если роль на замену не выбрана')
    def check_modal_window_delete_without_select_role(self):
        time.sleep(1)
        assert self.element_is_visible(self.locators.HELPER_TEXT).text == 'Поле обязательно', \
            "Под полем не отображается подсказка 'Поле обязательно'"
        assert self.element_is_visible(self.locators.BORDER_REPLACE_SYSTEM_ROLE).value_of_css_property('border-color') \
               == 'rgba(211, 47, 47, 1)', "Поле 'Новая системная роль' не выделятся красным цветом"

    @allure_testit_step(
        'Проверка модального окна при удалении системной роли, не назначенной пользователям')
    def check_modal_window_delete_not_assigned_system_role(self, role_name):
        assert self.element_is_displayed(self.locators.SUBMIT_BUTTON), "Нет кнопки Удалить"
        assert self.element_is_displayed(self.locators.ABORT_BUTTON), 'Нет кнопки Отменить'
        data = self.element_is_visible(self.locators.ALERT_DIALOG_ONE_ROLE).text
        assert f'Вы уверены, что хотите удалить системную роль "{role_name}"?' == data, \
            'Некорректный вопрос подтверждения'

    @allure_testit_step('Нажатие на кнопку Удаления в модальном окне единственной системной роли')
    def press_delete_button_one_system_role(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @allure_testit_step('Выбрать системную роль "Пользователь" при удалении в диалоговом окне')
    def choose_new_system_role_in_dialog(self):
        self.element_is_visible(self.locators.REPLACE_SYSTEM_ROLE).click()
        self.element_is_visible(self.locators.SYSTEM_ROLE_USER).click()
        return 'Пользователь'