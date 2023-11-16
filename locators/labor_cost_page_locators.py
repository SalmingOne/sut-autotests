import random

from selenium.webdriver.common.by import By

from data.data import PROJECT_CODE, PROJECT_NAME


class LaborCostPageLocators:
    # Переход на страницу трудозатрат
    TAB_ACTIVITY = (By.CSS_SELECTOR, 'div[id="activity"]')
    TAB_LABOR_COST_TABLE = (By.CSS_SELECTOR, 'a[href="/"]')
    # Проверка, что код проекта есть на странице
    CHECK_CODE_PROJECT = (By.XPATH, f'//a[text()="{PROJECT_CODE}"]')
    # Дни в привязке к проекту
    ALL_DAYS_BY_PROJECT = (
        By.XPATH, f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div//input')
    RANDOM_DAYS_BY_PROJECT = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[{random.randint(2, 29)}]//input')
    FIRST_DAY_BY_PROJECT = (
        By.XPATH, f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[2]//input')
    LAST_28_DAY_BY_PROJECT = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[29]//input')
    LAST_7_DAY_BY_PROJECT = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[8]//input')

    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    PREVIOUS_PERIOD_BUTTON = (By.CSS_SELECTOR,
                              'button[class="MuiButtonBase-root MuiIconButton-root MuiIconButton-colorPrimary '
                              'MuiIconButton-sizeMedium css-18wlvvu"]')
    NEXT_PERIOD_BUTTON = (By.XPATH, '//button[contains(@class,"onboarding__next-quarter")]')

    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Подтвердить"]')
    THIS_DAY_BUTTON = (By.XPATH,
                       '//button[contains(@class, " MuiButton-disableElevation MuiButtonBase-root onboarding__show-today css-1mttzxf")]')

    # Проверка что в аллерте есть поле для указания причины списания
    CHECK_LABOR_REASON_FIELD = (By.XPATH, '//label[text()="Причина"]')
    # Кнопка сброса аллерта
    BREAK_LABOR_REASON_WINDOW = (By.XPATH, '//div[@aria-label="Заполните все обязательные поля"]//following::button')

    # Выбор периода на странице
    PERIOD_SELECT_BUTTON = (By.XPATH, '//div[contains(@class, "onboaring__period-select")]')
    WEEK_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="week"]')
    MONTH_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="month"]')
