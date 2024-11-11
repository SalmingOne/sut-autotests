from selenium.webdriver.common.by import By


class SystemRolePageLocators:
    # Переход на страницу Пользователи
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    SYSTEM_ROLE = (By.CSS_SELECTOR, 'a[href="/admin/system-roles/users"]')
    ADMIN_SYSTEM_ROLE_TAB = (By.XPATH, '//button[text()="Администрирование"]')

    CREATE_SYSTEM_ROLE_BUTTON = (By.XPATH, '//button[text()="Создать роль"]')
    INPUT_ROLE_FIELD = (By.CSS_SELECTOR, 'input[name="roleName"]')
    ALL_TAG_CHECKBOXES = (By.CSS_SELECTOR, 'span[class="ag-checkbox-wrapper "]')
    SUBMIT_DELETE_ROLE_BUTTON = (By.XPATH, '//button[text()="Удалить"]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ALL_NAMES_IN_DROPDOWN = (By.CSS_SELECTOR, 'li[aria-label]')
    ROLE_FIELD = (By.CSS_SELECTOR, 'input[class^="MuiOutlinedInput-input MuiInputBase-input MuiInputBase-inputAdornedEnd"]')
    LI_MENU_ITEM = (By.CSS_SELECTOR, 'button[aria-label="Открыть"]')
    DELETE_ROLE_ICON = (By.XPATH, '//*[@data-testid="DeleteIcon"]/..')

    # Тултип
    TOOLTIP_ROLE_ICON = (By.XPATH, '//*[@data-testid="DeleteIcon"]/../..')

    def get_name_in_dropdown(self, role_name):
        return By.CSS_SELECTOR, f'li[aria-label="{role_name}"]'