from selenium.webdriver.common.by import By


class SchedulePageLocators:
    # Переход на страницу графика работы
    TAB_ACTIVITY = (By.CSS_SELECTOR, 'div[id="activity"]')
    TAB_SCHEDULE = (By.CSS_SELECTOR, 'a[href="/schedule"]')

    REDACT_BUTTON = (By.XPATH, '//button[text()="Редактировать"]')
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    TAKE_OFF_BUTTON = (By.XPATH, '//button[text()="Добавить отгул"]')
    THIS_WEEK_NUMBER = (By.XPATH, '//h6[contains(text(),"неделя")]')

    NEXT_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronRightIcon"]')
    PREVIOUS_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronLeftIcon"]')
    THIS_DAY_BUTTON = (By.XPATH, '//button[contains(@class, "DateInterval-setToday")]')

    WORK_HOURS_IN_DAY = (By.XPATH, '//p[contains(@class,"MuiTypography-root MuiTypography-body1")]')
    ALL_CHIPS_BUTTON = (By.CSS_SELECTOR, 'div[aria-label="Нажмите, чтобы редактировать рабочие часы"]')
    ALL_PLUS_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Нажмите, чтобы указать рабочие часы"]')
    CHIPS_TEXT = (By.CSS_SELECTOR, 'span[class^="MuiChip-label MuiChip-labelMedium"]')
    # Дровер редактирования графика работы
    DRAWER_TITLE = (By.XPATH, '//div[contains(@class,"MuiDrawer-paper")]//h6[contains(@class,"MuiTypography-root MuiTypography-subtitle1")]')
    DRAWER_FIELDS_LABELS = (By.XPATH, '//div[contains(@class,"MuiDrawer-paper")]//label')
    DRAWER_SUBMIT_BUTTON = (By.XPATH, '//div[contains(@class,"MuiDrawer-paper")]//button[@type="submit"]')
    DRAWER_BREAK_BUTTON = (By.XPATH, '//div[contains(@class,"MuiDrawer-paper")]//button[text()="Отменить"]')
    WEEK_CHECKBOXES = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    ALL_WEEK_CHECKED_CHECKBOXES = (By.CSS_SELECTOR, 'input[checked][type="checkbox"]')
    ALL_WEEK_CHECKED_CHECKBOXES_TEXT = (By.XPATH, '//input[@checked][@type="checkbox"]/../..//p')
    INDIVIDUAL_DAY_SWITCH = (By.CSS_SELECTOR, 'input[class^="MuiSwitch-input PrivateSwitchBase-input"]')
    ERROR_IN_CHECKBOXES = (By.XPATH, '//p/..//span[contains(@class, "MuiTypography-root MuiTypography-caption")]')
    INDIVIDUAL_DAY_TABS = (By.XPATH, '//label[contains(@class,"MuiFormControlLabel-labelPlacementEnd checked")]/..//label[contains(@class,"MuiFormControlLabel-labelPlacementEnd")]//p[text()]')
    TOOLTIP_SUBMIT_BUTTON = (By.XPATH, '//div[text()="Время перерыва должно быть между границами рабочего дня"]')

    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    START_WORK = (By.XPATH, '//label[text()="Начало рабочего дня"]/..//input')
    END_WORK = (By.XPATH, '//label[text()="Окончание рабочего дня"]/..//input')
    START_BREAK = (By.XPATH, '//div[contains(@name,"breaks")][contains(@name,"startTime")]//input')
    END_BREAK = (By.XPATH, '//div[contains(@name,"breaks")][contains(@name,"endTime")]//input')
    DURATION_FIELDS = (By.XPATH, '//label[text()="Длительность"]/..//input')
    ADD_BREAK_BUTTON = (By.XPATH, '//button[text()="Добавить перерыв"]')

    DELETE_BREAK_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="DeleteIcon"]')
    CLEAR_ICON = (By.CSS_SELECTOR, 'svg[data-testid="ClearIcon"]')
    CLEAR_ICON_IN_REDACT_DRAWER = (By.XPATH, '//h6[text()="Редактирование стандартного графика"]//..//*[@data-testid="ClearIcon"]')
    # Дровер добавления отгула
    SWITCH_BY_DAY = (By.XPATH, '//span[contains(@class,"MuiSwitch-switchBase MuiSwitch-colorSecondary")]')
    TAKE_OFF_DATA_PICKER = (By.XPATH, '//label[text()="Дата отгула"]//..//descendant::button')
    THIS_DAY_PICKER = (By.XPATH, '//button[contains(@class, "MuiPickersDay-today")]')
    DAY_BEFORE_THIS_DAY_PICKER = (By.XPATH, '//button[contains(@class, "MuiPickersDay-today")]//preceding::button[1]')
    ADD_TAKE_OFF_DATA_BUTTON = (By.XPATH, '//button[text()="Добавить дату отработки"]')
    # Модальное окно первичного задания рабочих дней
    TEXT_IN_MODAL = (By.XPATH, '//p[text()="Укажите ваши рабочие дни"]')
    SUBMIT_IN_MODAL = (By.XPATH, '//button[text()="Сохранить"]')

    # Ошибки
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    ALERT_MESSAGE = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
