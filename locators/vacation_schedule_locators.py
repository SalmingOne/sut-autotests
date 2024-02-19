from selenium.webdriver.common.by import By


class VacationSchedulePageLocators:
    # Переход на страницу графика отпусков
    TAB_MORE = (By.CSS_SELECTOR, 'div[id="more"]')
    TAB_VACATION_SCHEDULE = (By.CSS_SELECTOR, 'a[href="/vacation-schedule"]')
    # Заголовок таблицы
    VACATION_SCHEDULE_HEADER = (By.CSS_SELECTOR, 'div[class="ag-header-container"]')
    WEEKS_IN_VACATION_SCHEDULE_HEADER = (By.CSS_SELECTOR, 'div[aria-label^="Неделя №"]')
    FIRST_WEEK_IN_VACATION_SCHEDULE_HEADER = (By.CSS_SELECTOR, 'div[aria-label="Неделя №1"]')
    TODAY_WEEK = (By.XPATH, '//p[contains(@class, "today")]')
    # Тултип
    TOOLTIP = (By.XPATH, '//div[contains(@class, "MuiTooltip-tooltipPlacementTop")]')
    # Кнопки выбора периода
    PREVIOUS_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronLeftIcon"]')
    NEXT_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronRightIcon"]')
    THIS_DAY_BUTTON = (By.XPATH, '//button[contains(@class, "DateInterval-setToday")]')
    # Фильтрация
    FILTER_BUTTON = (By.XPATH, '//button[contains(@class, "MuiButton-text MuiButton-textPrimary")]')
    CHECKBOX_ON_FILTER = (By.XPATH, '//span[contains(@class, "MuiTypography-body1")]//p')
    FILTER_INPUT_PLACEHOLDERS = (By.CSS_SELECTOR, 'input[aria-invalid="false"]')
    # Строки таблицы
    ALL_PROJECTS_ROLES = (By.XPATH, '//span[contains(@class, "MuiTypography-root MuiTypography-subtitle2")]')
    ALL_USER_NAMES = (By.XPATH, '//div[@col-id="ag-Grid-AutoColumn"]//p[contains(@class, "MuiTypography-body2")]')
