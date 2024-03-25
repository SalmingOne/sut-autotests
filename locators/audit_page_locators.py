from selenium.webdriver.common.by import By


class AuditPageLocators:
    # Переход на страницу аудит
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    AUDIT_PAGE = (By.CSS_SELECTOR, 'a[href="/admin/logging"]')

    AUDIT_TAB_COLUMN_TITLES = (By.XPATH, '//div[@class="ag-header-cell-comp-wrapper"]/div')
    RESET_ALL_BUTTON = (By.XPATH, '//button[contains(@class," MuiButton-outlinedSizeSmall MuiButton-disableElevation")]')