from selenium.webdriver.common.by import By


class ProductionCalendarPageLocators:
    # Переход на Производственный календарь
    TAB_MORE = (By.CSS_SELECTOR, 'div[id="more"]')
    TAB_PRODUCTION_CALENDAR = (By.CSS_SELECTOR, 'a[href="/calendar"]')
    # Производственный календарь
    TITLES = (By.CSS_SELECTOR, 'h6[class^="MuiTypography-root MuiTypography-subtitle1"]')
    PREVIOUS_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronLeftIcon"]')
    NEXT_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronRightIcon"]')
    WEEK_TITLES = (By.XPATH, '//div[contains(@class,"MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1")][1]//span[contains(@class,"MuiTypography-root MuiTypography-overline")]')
    WORK_HOUR_TITLES = (By.XPATH,
                   '//div[contains(@class,"MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1")][1]//span[contains(@class,"MuiTypography-root MuiTypography-caption")]')
    CALENDAR_TODAY = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-body2 today calendar"]')
    CALENDAR_HOLIDAY = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-body2 holiday calendar"]')
    CALENDAR_WEEKEND = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-body2 weekend calendar"]')
    CALENDAR_PRE_HOLIDAY = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-body2 pre-holiday calendar"]')
    QUARTER_CALENDAR_DAYS = (By.XPATH, '//p[text()="Календарных:"]')
    QUARTER_WORK_DAYS = (By.XPATH, '//p[text()="Рабочих:"]')
    QUARTER_HOLIDAY_DAYS = (By.XPATH, '//p[text()="Вых./праздн.:"]')
    QUARTER_PRE_HOLIDAY_DAYS = (By.XPATH, '//p[text()="Предпраздничных:"]')
    # Легенда
    LEGEND_TODAY = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption today legend"]')
    LEGEND_HOLIDAY = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption holiday legend"]')
    LEGEND_WEEKEND = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption weekend legend"]')
    LEGEND_PRE_HOLIDAY = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption pre-holiday legend"]')