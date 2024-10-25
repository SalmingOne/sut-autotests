import time

import allure
import pytest
import testit

from endpoints.affiliates_endpoint import AffiliatesEndpoint
from pages.filial_page import FilialPage


class TestFilialPage:

    @testit.workItemIds(10716)
    @testit.displayName("6.1.3.2. Создание ЮЛ в структуре организации")
    @pytest.mark.smoke
    @allure.title("id-10716 6.1.3.2. Создание ЮЛ в структуре организации")
    def test_adding_the_filial(self, delete_filial_after, login, driver):
        filial_page = FilialPage(driver)
        filial_endpoint = AffiliatesEndpoint()
        filial_page.go_to_filial_page()
        time.sleep(1)
        # Проверка полей дровера добавления филиала
        filial_page.open_add_filial_drawer()
        filial_page.check_clickable_save_button()
        filial_page.check_max_lait()
        filial_page.check_attraction_rate()
        filial_page.check_affiliate_field()
        filial_page.check_phone_field()
        filial_page.check_email_field()
        filial_page.press_abort_button()
        # Создание филиала
        filial_page.add_filial('Центральный филиал',
                               'Москва, Красная площадь',
                               '+77777777777',
                               'vip@vip.vip')
        assert filial_page.check_filial_on_tab('Центральный филиал'), "Филиал не создался"

    @testit.workItemIds(10720)
    @testit.displayName("6.1.3.3. Изменение данных в ЮЛ")
    @pytest.mark.smoke
    @allure.title("id-10720 6.1.3.3. Изменение данных в ЮЛ")
    def test_changing_the_filial(self, create_filial, login, driver):
        filial_page = FilialPage(driver)
        filial_page.go_to_filial_page()
        time.sleep(1)  # Нужно для отработки анимации
        address_before = filial_page.get_address_on_tab(create_filial)
        filial_page.change_filial_address(create_filial, 'Саратов')
        time.sleep(1)  # Нужно для отработки анимации
        address_after = filial_page.get_address_on_tab(create_filial)
        assert address_after == 'Саратов', 'Новый адрес не сохранился'
        assert address_after != address_before, 'Адрес не изменился'

    @testit.workItemIds(10729)
    @testit.displayName("6.1.3.5. Удаление ЮЛ")
    @pytest.mark.smoke
    @allure.title("id-10729 6.1.3.5. Удаление ЮЛ")
    def test_deleting_the_filial(self, create_filial_to_delete, login, driver):
        filial_page = FilialPage(driver)
        filial_page.go_to_filial_page()
        time.sleep(1)
        filial_page.delete_filial('Для удаления')
        time.sleep(2)
        assert not filial_page.check_filial_on_tab('Для удаления'), 'Филиал остался в таблице'

    @testit.workItemIds(1483)
    @testit.displayName("6.1.3.1. Просмотр вкладки ЮЛ в структуре организации")
    @pytest.mark.regress
    @allure.title("id-1483 6.1.3.1. Просмотр вкладки ЮЛ в структуре организации")
    def test_view_filial_tab(self, login, driver):
        filial_page = FilialPage(driver)
        filial_page.go_to_filial_page()
        filial_page.check_table_column_headings()
        filial_page.check_buttons_on_tab_filial()

    @testit.workItemIds(10717)
    @testit.displayName("6.1.3.2. Отмена создания ЮЛ")
    @pytest.mark.regress
    @allure.title("id-10717 6.1.3.2. Отмена создания ЮЛ")
    def test_cancel_add_filial(self, login, driver):
        filial_page = FilialPage(driver)
        filial_page.go_to_filial_page()
        time.sleep(1)
        filial_page.add_filial_with_fields_from_table_only('Центральный филиал',
                               'Москва, Красная площадь')
        filial_page.press_abort_button()
        assert not filial_page.check_filial_on_tab('Центральный филиал'), "Филиал сохранился"

    @testit.workItemIds(10718)
    @testit.displayName("6.1.3.2. Создание ЮЛ в структуре организации, если не заполнены обязательные поля")
    @pytest.mark.regress
    @allure.title("id-10718 6.1.3.2. Создание ЮЛ в структуре организации, если не заполнены обязательные поля")
    def test_add_filial_without_required_fields(self, login, driver):
        filial_page = FilialPage(driver)
        filial_page.go_to_filial_page()
        time.sleep(1)
        filial_page.open_add_filial_drawer()
        filial_page.check_clickable_save_button()
        filial_page.add_filial_without_required_fields('Москва, Красная площадь',
                                                       '+77777777777',
                                                       'vip@vip.vip')
        filial_page.check_clickable_save_button()

    @testit.workItemIds(10730)
    @testit.displayName("6.1.3.5. Отмена удаления ЮЛ")
    @pytest.mark.regress
    @allure.title("id-10730 6.1.3.5. Отмена удаления ЮЛ")
    def test_cancel_delete_filial(self, create_filial, login, driver):
        filial_page = FilialPage(driver)
        filial_page.go_to_filial_page()
        time.sleep(1)  # Нужно для отработки анимации
        filial_page.cansel_delete_filial(create_filial)
        assert filial_page.check_filial_on_tab(create_filial), "Филиал удалился"

    @testit.workItemIds(10723)
    @testit.displayName("6.1.3.3. Изменение данных в ЮЛ, если обязательные поля не заполнены")
    @pytest.mark.regress
    @allure.title("id-10723 6.1.3.3. Изменение данных в ЮЛ, если обязательные поля не заполнены")
    def test_changing_data_in_a_filial_if_required_fields_are_not_filled(self, create_filial, login, driver):
        filial_page = FilialPage(driver)
        filial_page.go_to_filial_page()
        time.sleep(2)  # Нужно для отработки анимации
        filial_page.open_redact_filial(create_filial)
        filial_page.clearing_required_fields()
        filial_page.check_clickable_save_button()

    @testit.workItemIds(10724)
    @testit.displayName("6.1.3.3. Изменение названия ЮЛ")
    @pytest.mark.regress
    @allure.title("id-10724 6.1.3.3. Изменение названия ЮЛ")
    def test_changing_filial_name(self, create_filial, login, driver):
        filial_page = FilialPage(driver)
        filial_page.go_to_filial_page()
        time.sleep(2)  # Нужно для отработки анимации
        filial_page.open_redact_filial(create_filial)
        filial_page.change_filial_name('Новое имя')
        filial_page.press_save_button()
        assert filial_page.check_filial_on_tab('Новое имя'), "Имя филиала не изменилось"

    @testit.workItemIds(10719)
    @testit.displayName("6.1.3.2. Создание ЮЛ в структуре организации, если уникальные поля НЕ уникальны")
    @pytest.mark.regress
    @allure.title("id-10719 6.1.3.2. Создание ЮЛ в структуре организации, если уникальные поля НЕ уникальны")
    def test_create_filial_with_not_unique_fields(self, create_filial, login, driver):
        filial_page = FilialPage(driver)
        filial_page.go_to_filial_page()
        time.sleep(2)  # Нужно для отработки анимации
        filial_page.add_filial_with_fields_from_table_only('Для редактирования', 'г. Москва')
        filial_page.press_save_button()
        filial_page.check_warning_text('Укажите уникальноe название филиала', 'Укажите уникальный адрес филиала')

    @testit.workItemIds(10722)
    @testit.displayName("6.1.3.3. Отмена изменения данных в ЮЛ")
    @pytest.mark.regress
    @allure.title("id-10722 6.1.3.3. Отмена изменения данных в ЮЛ")
    def test_cancel_data_changes_in_filial(self, create_filial, login, driver):
        filial_page = FilialPage(driver)
        filial_page.go_to_filial_page()
        time.sleep(2)  # Нужно для отработки анимации
        filial_page.open_redact_filial(create_filial)
        filial_page.change_filial_name('Новое имя')
        filial_page.press_abort_button()
        driver.refresh()
        assert not filial_page.check_filial_on_tab('Новое имя'), "Имя филиала изменилось"
        assert filial_page.check_filial_on_tab('Для редактирования'), "Имя филиала изменилось"

    @testit.workItemIds(10726)
    @testit.displayName("6.1.3.4. Отмена удаления пользователя из ЮЛ")
    @pytest.mark.regress
    @allure.title("id-10726 6.1.3.4. Отмена удаления пользователя из ЮЛ")
    def test_cancel_user_deletion_from_filial(self, create_work_user, create_filial_with_director, login, driver):
        filial_page = FilialPage(driver)
        filial_page.go_to_filial_page()
        time.sleep(2)  # Нужно для отработки анимации
        filial_page.open_redact_filial(create_filial_with_director)
        employees_before_delete = filial_page.get_employees_in_field()
        filial_page.delete_employs_from_filial()
        filial_page.press_abort_button()
        filial_page.open_redact_filial(create_filial_with_director)
        employees_after_delete = filial_page.get_employees_in_field()
        assert employees_before_delete == employees_after_delete, 'Изменения сохранились'

