from selenium.webdriver.common.by import By


class IntegrationsPageLocators:
    # Переход на страницу интеграций
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    INTEGRATIONS_PAGE = (By.CSS_SELECTOR, 'a[href="/admin/integrations/jira"]')
    # jira
    DELETE_ALL_JIRA_INTEGRATION = (By.XPATH, '//h6[text()="jira"]/..//following-sibling::div//div[@aria-label="Удалить все интеграции"]//button')
    ADD_JIRA_INTEGRATION_BUTTON = (
    By.XPATH, '//h6[text()="jira"]/..//following-sibling::div//div[@aria-label="Добавить интеграцию"]//button')
    URL_INPUT_FIELD = (By.CSS_SELECTOR, 'input[name="url"]')
    LOGIN_INPUT_FIELD = (By.CSS_SELECTOR, 'input[name="login"]')
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    CHECK_ICON = (By.CSS_SELECTOR, 'svg[data-testid="CheckIcon"]')

    DELETE_BUTTON_ON_MODAL = (By.XPATH, '//div[@role="dialog"]//*[@data-testid="DeleteIcon"]')
    EDIT_BUTTON_ON_MODAL = (By.XPATH, '//div[@role="dialog"]//*[@data-testid="EditIcon"]')
    ADD_INTEGRATION_ON_MODAL = (By.XPATH, '//button[text()="Добавить интеграцию"]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ALERT_MESSAGE = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
