import time

import allure
import pytest
import testit

from pages.template_page import TemplatePage


@allure.suite("Страница Шаблоны")
class TestTemplatePage:

    @testit.workItemIds(1274)
    @testit.displayName("6.3.1.1. Загрузка шаблонов заявлений в систему")
    @pytest.mark.smoke
    @allure.title("id-1274 6.3.1.1. Загрузка шаблонов заявлений в систему")
    def test_add_template_application(self, login, driver):
        template_page = TemplatePage(driver)
        template_page.go_to_template_page()
        template_page.check_template_is_empty()
        template_page.add_template_file()
        #уходим из шаблонов чтобы проверить что он сохранился
        template_page.go_to_template_page()
        template_page.check_template_file()

    @testit.workItemIds(1276)
    @testit.displayName("6.3.1.1. Удаление шаблонов заявлений в системе")
    @pytest.mark.smoke
    @allure.title("id-1276 6.3.1.1. Удаление шаблонов заявлений в системе")
    def test_delete_template_application(self, login, driver):
        template_page = TemplatePage(driver)
        template_page.go_to_template_page()
        template_page.add_template_file()
        template_page.check_template_is_empty()
        # уходим из шаблонов, чтобы проверить что он удалился
        template_page.go_to_template_page()
        template_page.check_template_file_delete()