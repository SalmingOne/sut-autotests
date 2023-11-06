import random

from selenium.webdriver.common.by import By

from data.data import PROJECT_CODE, PROJECT_NAME


class LaborCostPageLocators:
    TAB_ACTIVITY = (By.CSS_SELECTOR, 'div[id="activity"]')
    TAB_LABOR_COST_TABLE = (By.CSS_SELECTOR, 'a[href="/"]')

    CHECK_CODE_PROJECT = (By.XPATH, f'//a[text()="{PROJECT_CODE}"]')
    ALL_DAYS_BY_PROJECT = (
    By.XPATH, f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div//input')
    RANDOM_DAYS_BY_PROJECT = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[{random.randint(1, 28)}]//input')
    CHECK_LABOR_REASON_FIELD = (By.XPATH, '//label[text()="Причина"]')
    BREAK_LABOR_REASON_WINDOW = (By.XPATH, '//div[@aria-label="Заполните все обязательные поля"]//following::button')
