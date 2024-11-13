from selenium.webdriver.common.by import By


class EconomyPageLocators:
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    ECONOMY_PAGE = (By.CSS_SELECTOR, 'a[href="/admin/economics"]')

    def get_kebab_menu_by_name(self, attraction_rate_name):
        return By.XPATH, f"//p[text()='{attraction_rate_name}']/../following-sibling::div[@aria-colindex='5']//button"

    def get_kebab_action(self, action):
        return By.XPATH, f"//span[text()='{action}']"

    APPLY_DELETING_BUTTON = (By.XPATH, f"//button[text()='Подтвердить']")
    DISCARD_DELETING_BUTTON = (By.XPATH, f"//button[text()='Отменить']")
    DELETING_MODAL_WINDOW_TEXT = (By.CSS_SELECTOR, 'p[id="alert-dialog-description"]')
    ALERT_TEXT = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
    ATTRACTION_RATES = (By.XPATH, f"//div[@col-id='name' and not(@aria-sort)]")
    FILTER_ICON = (By.CSS_SELECTOR, 'svg[data-testid="TuneIcon"]')
    CHECKBOXES = (By.XPATH, "//h6[text()='Отображение']/../..//input[@type='checkbox']/..")
    ATTRACTION_RATES_TYPES = (By.XPATH, f"//div[@col-id='type' and not(@aria-sort)]")