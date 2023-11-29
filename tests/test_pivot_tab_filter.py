import time

import allure

from pages.pivot_tab_filter_page import PivotTabFilterPage
from pages.pivot_tab_page import PivotTabPage


@allure.suite("Дровер фильтрации сводной таблицы по проектам")
class TestPivotTabFilterPage:

    #  id-1194 3.2.2.15.1 Реакция системы на нажатие кнопки "Сбросить все" на табе "По проектам".
    @allure.title("id-1194 3.2.2.15.1 Реакция системы на нажатие кнопки Сбросить все на табе По проектам.")
    def test_reset_all_button_on_filter(self, login, driver):
        pivot_tab_page = PivotTabPage(driver)
        pivot_tab_page.go_to_pivot_page()
        time.sleep(1)  # Без ожидания открывается фильтр на странице трудозатрат вместо сводной таблицы
        pivot_tab_page.open_filter()
        pivot_tab_filter_page = PivotTabFilterPage(driver)
        before_changes = pivot_tab_filter_page.get_checked_element_text()
        pivot_tab_filter_page.click_random_checkbox()
        outer_changes = pivot_tab_filter_page.get_checked_element_text()
        pivot_tab_filter_page.click_reset_button()
        outer_reset = pivot_tab_filter_page.get_checked_element_text()
        assert before_changes != outer_changes, "Настройки фильтров не изменились"
        assert outer_reset == ['Bсе проекты', 'Почасовая оплата', 'По окладу', 'Пользователи без филиалов',
                               'Показывать активность пользователя'], ("После сброса не все фильтры восстановились по "
                                                                       "умолчанию")
