from selenium.webdriver.common.by import By


class SystemRolePageLocators:
    # Переход на страницу Пользователи
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    SYSTEM_ROLE = (By.CSS_SELECTOR, 'a[href="/admin/system-roles/users"]')
    ADMIN_SYSTEM_ROLE_TAB = (By.XPATH, '//button[text()="Администрирование"]')
    USERS_SYSTEM_ROLE_TAB = (By.XPATH, '//button[text()="Пользователи"]')

    CREATE_SYSTEM_ROLE_BUTTON = (By.XPATH, '//button[text()="Создать роль"]')
    INPUT_ROLE_FIELD = (By.CSS_SELECTOR, 'input[name="roleName"]')
    BORDER_COLOR = (By.XPATH, '//input[@name="roleName"]//following-sibling::fieldset')
    COPY_SYSTEM_ROLE = (By.XPATH, '//button[@aria-label="Копировать системную роль"]')
    ALL_TAG_CHECKBOXES = (By.CSS_SELECTOR, 'span[class="ag-checkbox-wrapper "]')
    SUBMIT_DELETE_ROLE_BUTTON = (By.XPATH, '//button[text()="Удалить"]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    ALL_NAMES_IN_DROPDOWN = (By.CSS_SELECTOR, 'li[aria-label]')
    ROLE_FIELD = (By.CSS_SELECTOR, 'input[class^="MuiOutlinedInput-input MuiInputBase-input MuiInputBase-inputAdornedEnd"]')
    LI_MENU_ITEM = (By.CSS_SELECTOR, 'button[aria-label="Открыть"]')
    DELETE_ROLE_ICON = (By.XPATH, '//*[@data-testid="DeleteIcon"]/..')
    ALERT_DIALOG = (By.CSS_SELECTOR, 'p[id="alert-dialog-description"]')
    ALERT_DIALOG_ONE_ROLE = (By.XPATH, '//p[contains(@class, "MuiTypography-body2")]')
    REPLACE_SYSTEM_ROLE = (By.XPATH, '//label[text()="Новая системная роль"]/../div/div')
    BORDER_REPLACE_SYSTEM_ROLE = (By.XPATH, '//label[text()="Новая системная роль"]')
    SYSTEM_ROLE_USER = (By.XPATH, '//li[text()="Пользователь"]')

    # Тултип
    TOOLTIP_ROLE_ICON = (By.XPATH, '//*[@data-testid="DeleteIcon"]/../..')
    # Ошибки
    HELPER_TEXT = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    ALERT_MESSAGE = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')

    def get_name_in_dropdown(self, role_name):
        return By.CSS_SELECTOR, f'li[aria-label="{role_name}"]'

    def get_name_in_dialog(self, user_name):
        return By.XPATH, f'//input[@value="{user_name}"]'