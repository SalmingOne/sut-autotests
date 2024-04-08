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

    ALERT_SUBMIT_BUTTON = (By.XPATH, '//div[@role="presentation"]//button[@type="submit"]')
    ALERT_MESSAGE = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')

    INTEGRATIONS_TITLES = (By.CSS_SELECTOR, 'h6[class^="MuiTypography-root MuiTypography-subtitle2 title"]')
    ADD_INTEGRATION_BUTTONS = (By.CSS_SELECTOR, 'div[aria-label="Добавить интеграцию"]')
    EDIT_INTEGRATION_BUTTONS = (By.CSS_SELECTOR, 'div[aria-label="Редактировать интеграции"]')
    DELETE_INTEGRATION_BUTTONS = (By.CSS_SELECTOR, 'div[aria-label="Удалить все интеграции"]')
