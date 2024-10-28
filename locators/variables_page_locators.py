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
    KEBABS_DEL_MENU_ITEM = (By.XPATH, '//span[text()="Удалить"]')
    KEBABS_EDIT_MENU_ITEM = (By.XPATH, '//span[text()="Редактировать"]')
    DEL_ACCEPT_BUTTON = (By.XPATH, '//p[@id="alert-dialog-description"]//following::button[@type="submit"]')
    CANCEL_ACCEPT_BUTTON = (By.XPATH, '//p[@id="alert-dialog-description"]//following::button[text()="Отменить"]')
    ALL_SEARCH_FIELDS = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')

    # Дровер создания переменной
    FIELD_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    VARIABLE_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="systemName"]')
    VARIABLE_VALUE_INPUT = (By.CSS_SELECTOR, 'input[name="value"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    TEMPLATE_WITH_VARIABLE = (By.CSS_SELECTOR, 'svg[data-testid="ArrowDropDownIcon"]')
    TEMPLATE_VALUE = (By.XPATH, '//li[text()="Ежегодный отпуск"]')

    SAVE_VALUE_CHECKBOX = (By.XPATH, '//span[text()="Хранить значение поля"]/../span/input')
    ASK_VALUE_CHECKBOX = (By.XPATH, '//span[text()="Запрашивать значение у пользователя"]')

    ALERT_TEXT = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
    TEMPLATES_INPUT_FIELD = (By.XPATH, '//input[contains(@class," MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused")]')
    CHIPS_IN_TEMPLATES_INPUT_FIELD = (By.XPATH, '//div[contains(@class,"MuiChip-deletable")]')
    DROPDOWN_ITEMS_NOT_SELECTED = (By.CSS_SELECTOR, 'li[role="option"][aria-selected="false"]')
    # Ошибки
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    ALERT_INCORRECT_TEMPLATE = (By.XPATH, '//div[text()="Неверный тип шаблона"]')

    # Блок с шаблонами
    DELETE_ICON = (By.CSS_SELECTOR, 'svg[data-testid="DeleteIcon"]')
    ADD_DOC = (By.CSS_SELECTOR, 'input[type="file"]')

    def check_text(self, text):
        return (By.XPATH, f'//*[text()="{text}"]')

    def get_value_from_column(self, variable_name, column_number):
        return (By.XPATH, f'//div[@aria-label="{variable_name}"]//ancestor::div[contains(@class,"ag-row-position-absolute")]//div[@aria-colindex="{column_number}"]//div')
