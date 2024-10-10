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

