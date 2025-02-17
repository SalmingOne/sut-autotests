from selenium.webdriver.common.by import By


class EconomyPageLocators:
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    ECONOMY_PAGE = (By.CSS_SELECTOR, 'a[href="/admin/economics"]')

    def get_kebab_menu_by_name(self, attraction_rate_name):
        return By.XPATH, f"//p[text()='{attraction_rate_name}']/../following-sibling::div[@aria-colindex='5']//button"

    def get_attraction_rate_type(self, attraction_rate_name):
        return By.XPATH, f"//p[text()='{attraction_rate_name}']/../following-sibling::div[@col-id='type']"

    def get_attraction_rate_size(self, attraction_rate_name):
        return By.XPATH, f"//p[text()='{attraction_rate_name}']/../following-sibling::div[@col-id='size']"

    def get_attraction_rate(self, attraction_rate_name):
        return By.XPATH, f"//p[text()='{attraction_rate_name}']"

    def get_kebab_action(self, action):
        return By.XPATH, f"//span[text()='{action}']"

    APPLY_MODAL_WINDOW_BUTTON = (By.XPATH, f"//button[text()='Подтвердить']")
    DISCARD_DELETING_BUTTON = (By.XPATH, f"//button[text()='Отменить']")
    DELETING_MODAL_WINDOW_TEXT = (By.CSS_SELECTOR, 'p[id="alert-dialog-description"]')
    ALERT_TEXT = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
    ATTRACTION_RATES = (By.XPATH, f"//div[@col-id='name' and not(@aria-sort)]")
    FILTER_ICON = (By.CSS_SELECTOR, 'svg[data-testid="TuneIcon"]')
    CHECKBOXES = (By.XPATH, "//h6[text()='Отображение']/../..//input[@type='checkbox']/..")
    ATTRACTION_RATES_TYPES = (By.XPATH, f"//div[@col-id='type' and not(@aria-sort)]")
    CREATE_ATTRACTION_RATE_BUTTON = (By.XPATH, "//button[text()='ставка']")
    ATTRACTION_RATE_NAME_FIELD = (By.CSS_SELECTOR, "input[name='name']")
    ATTRACTION_RATE_TARGET_FIELD = (By.XPATH, "//div[@name='targetIds']//input")
    ATTRACTION_RATE_SIZE_FIELD = (By.CSS_SELECTOR, "input[name='size']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    DISCARD_BUTTON = (By.XPATH, "//button[text()='Отменить']")
    DISCARD_MODAL_WINDOW_BUTTON = (By.XPATH, f"//button[text()='Отмена']")
    MODAL_WINDOW_TITLE = (By.XPATH, "//h6[text()='Внесенные изменения не сохранятся']")
    MODAL_WINDOW_SUBTITLE = (By.XPATH, "//p[text()='Закрыть режим редактирования?']")
    ATTRACTION_RATE_TYPE_DROPDOWN = (By.XPATH, "//div[@name='type']//button")
    DRAWER_LI_ITEMS = (By.TAG_NAME, 'li')
    UPDATE_DATE = (By.CSS_SELECTOR, "div[col-id='updateDate'][role='gridcell']")
    START_DATE = (By.CSS_SELECTOR, "div[col-id='startDate'][role='gridcell']")
    END_DATE = (By.CSS_SELECTOR, "div[col-id='endDate'][role='gridcell']")
    ATTRACTION_RATE_SIZE_MODAL_VIEW = (By.XPATH, "//div[@col-id='updateDate'][@role='gridcell']//following-sibling::div[@col-id='size']")
    ATTRACTION_RATE_STATUS_MODAL_VIEW = (By.XPATH, "//div[@col-id='updateDate'][@role='gridcell']//following-sibling::div[@aria-colindex='5']")
    FOT_INPUT = (By.CSS_SELECTOR, "input[name='salary']")
    ADDITIONAL_EXPENSES_INPUT = (By.CSS_SELECTOR, "input[name='additionalExpenses']")
    PROFITABILITY_RATIO_INPUT = (By.CSS_SELECTOR, "input[name='profitabilityRatio']")
    TAXES_INPUT = (By.CSS_SELECTOR, "input[name='taxes']")
    PRE_CALCULATION_BUTTON = (By.XPATH, "//button[text()='Предварительный расчёт']")
