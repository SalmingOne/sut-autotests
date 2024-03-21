from selenium.webdriver.common.by import By


class VariablesPageLocators:
    # Переход на страницу Пользователи
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    SYSTEM_AUDIT_TAB = (By.CSS_SELECTOR, 'a[href="/admin/settings/audit"]')
    TEMPLATES_TAB = (By.XPATH, '//button[text()="Шаблоны"]')

    ADD_VARIABLE_BUTTON = (By.XPATH, '//button[text()="Создать переменную"]')
    COLUMNS_HEADERS = (By.CSS_SELECTOR, 'h6[class^="MuiTypography-root MuiTypography-subtitle2"]')
    ASK_USER_CHECKBOXES = (By.XPATH, '//div[@col-id="0"]//input[@type="checkbox"]')
    SAVE_VALUE_CHECKBOXES = (By.XPATH, '//div[@col-id="1"]//input[@type="checkbox"]')
    ALL_KEBABS = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    KEBAB_MENU_ITEM = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption"]')
    ALL_SEARCH_FIELDS = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')
