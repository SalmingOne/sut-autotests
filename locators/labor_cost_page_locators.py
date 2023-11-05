from selenium.webdriver.common.by import By


class LaborCostPageLocators:

    TAB_ACTIVITY = (By.CSS_SELECTOR, 'div[id="activity"]')
    TAB_LABOR_COST_TABLE = (By.CSS_SELECTOR, 'a[href="/"]')

    CHECK_CODE_PROJECT = (By.XPATH, '//a[text()="ATP"]')  # вынести код проекта в отдельную переменную