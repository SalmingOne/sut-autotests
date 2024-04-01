from datetime import datetime, timedelta

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    @allure.step("открыть")
    def open(self):
        self.driver.get(self.url)

    @allure.step("элемент видим")
    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("элементы видимы")
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("элемент представлен")
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("элемент представлен долгое ожидание")
    def element_is_present_long_wait(self, locator, timeout=20):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("элементы представлены")
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step("элемент не видим")
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    @allure.step("по элементу можно кликнуть")
    def element_is_clickable(self, locator, timeout=5):
        try:
            wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False


    @allure.step("перейти к элементу")
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("двойной клик")
    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step("правый клик")
    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @allure.step("перетянуть предмет на позицию")
    def action_drag_and_drop_by_offset(self, element, x_coord, y_coord):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coord, y_coord)
        action.perform()

    @allure.step("перетянуть предмет на элемент")
    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    @allure.step("перейти к элементу")
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step("нажатие ESC")
    def action_esc(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE)
        action.perform()

    @allure.step("элемент отображён")
    def element_is_displayed(self, locator, timeout=5):
        try:
            wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Получение предыдущей даты отличной от текущей на N дней (DD.MM.YYYY)")
    def get_day_before(self, amount_of_days):
        day_before = datetime.now() - timedelta(days=amount_of_days)
        return day_before.strftime("%d.%m.%Y")

    @allure.step("Получение предыдущей даты отличной от текущей на N дней (MM.DD.YYYY)")
    def get_day_before_m_d_y(self, amount_of_days):
        day_before = datetime.now() - timedelta(days=amount_of_days)
        return day_before.strftime("%m.%d.%Y")

    @allure.step("Получение предыдущей даты отличной от текущей на N дней (YYYY.MM.DD)")
    def get_day_before_y_m_d(self, amount_of_days):
        day_before = datetime.now() - timedelta(days=amount_of_days)
        return day_before.strftime("%Y.%m.%d")