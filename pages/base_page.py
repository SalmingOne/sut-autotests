import platform
from datetime import datetime, timedelta

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from endpoints.calendar_endpoint import CalendarEndpoint


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

    @allure.step("тройной клик")
    def action_triple_click(self, element):
        actions = ActionChains(self.driver)
        actions.click(element).click().click()
        actions.perform()

    @allure.step("Выделение всего текста в текстовом поле")
    def action_select_all_text(self, element):
        actions = ActionChains(self.driver)
        if platform.system() == "Darwin":  # для macOS
            actions.click(element).key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND)
        else:
            actions.click(element).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        actions.perform()

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
        
    @allure.step("Получение сообщений системы")
    def get_all_alert_message(self, locator):
        all_alerts = self.elements_are_visible(locator)
        data = []
        for alert in all_alerts:
            data.append(alert.text)
        return data

    @allure.step("Получение предыдущей даты отличной от текущей на N дней (DD.MM.YYYY)")
    def get_day_before(self, amount_of_days):
        day_before = datetime.now() - timedelta(days=amount_of_days)
        return day_before.strftime("%d.%m.%Y")

    @allure.step("Получение предыдущей даты отличной от текущей на N дней (MM.DD.YYYY)")
    def get_day_before_m_d_y(self, amount_of_days):
        day_before = datetime.now() - timedelta(days=amount_of_days)
        return day_before.strftime("%m.%d.%Y")

    @allure.step("Получение предыдущей даты отличной от текущей на N дней (DD.MM)")
    def get_day_before_d_m(self, amount_of_days):
        day_before = datetime.now() - timedelta(days=amount_of_days)
        return day_before.strftime("%d.%m")

    @allure.step("Получение предыдущей даты отличной от текущей на N дней (YYYY.MM.DD)")
    def get_day_before_y_m_d(self, amount_of_days):
        day_before = datetime.now() - timedelta(days=amount_of_days)
        return day_before.strftime("%Y.%m.%d")

    @allure.step("Получение предыдущей даты отличной от текущей на N дней (YYYY-MM-DD)")
    def get_day_before_ymd(self, amount_of_days):
        day_before = datetime.now() - timedelta(days=amount_of_days)
        return day_before.strftime("%Y-%m-%d")

    @allure.step("Получение номера дня недели")
    def get_number_day_week(self):
        return datetime.now().isoweekday()
    
    @allure.step("Получение следующей даты отличной от текущей на N дней (DD.MM.YYYY)")
    def get_day_after(self, amount_of_days):
        day_after = datetime.now() + timedelta(days=amount_of_days)
        return day_after.strftime("%d.%m.%Y")

    @allure.step("Проверка и замена даты, если она выпадает на 1-е число")
    def check_and_replace_start_date(self, date_str):
        date_obj = datetime.strptime(date_str, "%m.%d.%Y")
        if date_obj.day == 1:
            new_date = datetime.now() + timedelta(days=1)
            return new_date.strftime("%m.%d.%Y")
        return date_str

    @allure.step("Получение следующей даты отличной от текущей на N дней (YYYY-MM-DD)")
    def get_day_after_ymd(self, amount_of_days):
        day_after = datetime.now() + timedelta(days=amount_of_days)
        return day_after.strftime("%Y-%m-%d")

    @allure.step("Получение первого и последнего дней текущей недели")
    def get_current_week_start_end(self):
        first_day_of_week = datetime.now() - timedelta(days=datetime.now().weekday())
        last_day_of_week = first_day_of_week + timedelta(days=6)
        return first_day_of_week, last_day_of_week
    
    @allure.step("Получение первого и последнего дней текущего месяца")
    def get_current_month_start_end(self):
        first_day_of_month = datetime.now().replace(day=1)
        next_month = datetime.now().month % 12 + 1
        next_month_year = datetime.now().year + (1 if datetime.now().month == 12 else 0)
        first_day_next_month = datetime(next_month_year, next_month, 1)
        last_day_of_month = first_day_next_month - timedelta(days=1)
        return first_day_of_month, last_day_of_month
    
    @allure.step("Получение следующей недели от заданной начальной даты")
    def get_next_week(self, start_date):
        first_day_of_week = start_date + timedelta(days=7 - start_date.weekday())
        last_day_of_week = first_day_of_week + timedelta(days=6)
        return first_day_of_week, last_day_of_week

    @allure.step("Проверяем, есть ли в неделе праздничные или укороченные рабочие дни")
    def is_week_shortened(self, start_date, end_date):
        calendar = CalendarEndpoint()
        holidays_data = calendar.get_production_api(start_date, end_date)
        # Извлекаем списки с праздничными и предпраздничными днями
        holidays = set(holidays_data.get("holidays", []))
        preholidays = set(holidays_data.get("preholidays", []))

        # Проверяем каждый день недели
        for day in (start_date + timedelta(days=i) for i in range(0, 7)):
            # Если день есть в праздничных или предпраздничных, неделя сокращена
            if day.strftime("%Y-%m-%d") in holidays or day.strftime("%Y-%m-%d") in preholidays:
                return True
        return False

    @allure.step("Получаем неделю без праздников или укороченных дней")
    def get_full_work_week(self):
        start_date, end_date = self.get_current_week_start_end()
        while self.is_week_shortened(start_date, end_date):
            start_date, end_date = self.get_next_week(start_date)
        return start_date, end_date

    @allure.step("Убираем фокус с элемента")
    def remove_focus_from_element(self):
        self.driver.execute_script("document.activeElement.blur();")