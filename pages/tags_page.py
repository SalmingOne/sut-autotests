import allure
import testit
from selenium.webdriver import Keys

from locators.tags_page_locators import TagsPageLocators
from pages.base_page import BasePage


class TagsPage(BasePage):
    locators = TagsPageLocators()

    @testit.step("Переход на справочник группы знаний")
    @allure.step("Переход на справочник группы знаний")
    def go_to_tags_page(self):
        self.element_is_visible(self.locators.SETTING_ICON).click()
        self.element_is_visible(self.locators.REFERENCE_BOOKS).click()
        self.element_is_visible(self.locators.TAG_TAB).click()

    @testit.step("Нажатие кнопки добавить группу знаний")
    @allure.step("Нажатие кнопки добавить группу знаний")
    def press_add_tag_button(self):
        self.element_is_visible(self.locators.ADD_TAG_BUTTON).click()

    @testit.step("Проверка поля Имя дровера добавления группы знаний")
    @allure.step("Проверка поля Имя дровера добавления группы знаний")
    def check_name_field(self):
        bad_value = ('Loremipsumdolorsitametconsectetueradipiscingelitseddiamnonummynibheuismodtinciduntutlaoreetdoloremagnaaliquam12345678901234567890')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(bad_value)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        error_text = self.element_is_visible(self.locators.MUI_ERROR).text
        self.element_is_visible(self.locators.ABORT_BUTTON).click()
        assert error_text == 'Максимальное количество символов: 128',\
            "Не появилось сообщение о превышении максимального количества символов"

    @testit.step("Добавление группы знаний")
    @allure.step("Добавление группы знаний")
    def create_tag(self, name, skill_name):
        self.element_is_visible(self.locators.ADD_TAG_BUTTON).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.SKILL_FIELD).click()
        self.element_is_visible(self.locators.check_li_item_by_text(skill_name)).click()
        self.action_esc()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @testit.step("Переход на вкладку группы знаний")
    @allure.step("Переход на вкладку группы знаний")
    def go_to_tag_tab(self):
        self.element_is_visible(self.locators.TAG_TAB).click()

    @testit.step("Проверка наличия группы знаний на вкладке группы знаний")
    @allure.step("Проверка наличия группы знаний на вкладке группы знаний")
    def check_tag_on_tag_tab(self, name):
        assert self.element_is_displayed(self.locators.text_on_page(name)),\
            "Имени группы знаний нет на вкладке группы знаний"

    @testit.step("Изменение группы знаний")
    @allure.step("Изменение группы знаний")
    def edit_tag(self, name_before, name, skill_name):
        self.element_is_visible(self.locators.kebab_by_tag_name(name_before)).click()
        self.element_is_visible(self.locators.KEBABS_REDACT_MENU_ITEM).click()
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(Keys.CONTROL + 'a')
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.SKILL_FIELD).click()
        self.element_is_visible(self.locators.check_li_item_by_text(skill_name)).click()
        self.action_esc()
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
