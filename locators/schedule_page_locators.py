from selenium.webdriver.common.by import By


class SchedulePageLocators:
    # Переход на страницу графика работы
    TAB_ACTIVITY = (By.CSS_SELECTOR, 'div[id="activity"]')
    TAB_SCHEDULE = (By.CSS_SELECTOR, 'a[href="/schedule"]')

    REDACT_BUTTON = (By.XPATH, '//button[text()="Редактировать"]')

    NEXT_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronRightIcon"]')

    ALL_CHIPS_BUTTON = (By.CSS_SELECTOR, 'div[aria-label="Нажмите, чтобы редактировать рабочие часы"]')
    # Дровер редактирования графика работы
    DRAWER_TITLE = (By.XPATH, '//div[contains(@class,"MuiDrawer-paper")]//h6[contains(@class,"MuiTypography-root MuiTypography-subtitle1")]')
    DRAWER_FIELDS_LABELS = (By.XPATH, '//div[contains(@class,"MuiDrawer-paper")]//label')
    DRAWER_SUBMIT_BUTTON = (By.XPATH, '//div[contains(@class,"MuiDrawer-paper")]//button[@type="submit"]')
    DRAWER_BREAK_BUTTON = (By.XPATH, '//div[contains(@class,"MuiDrawer-paper")]//button[text()="Отменить"]')

    START_BREAK = (By.XPATH, '//div[contains(@name,"breaks")][contains(@name,"startTime")]//input')
    END_BREAK = (By.XPATH, '//div[contains(@name,"breaks")][contains(@name,"endTime")]//input')
    ADD_BREAK_BUTTON = (By.XPATH, '//button[text()="Добавить перерыв"]')

    DELETE_BREAK_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="DeleteIcon"]')

