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