from selenium.webdriver.common.by import By


class FilialPageLocators:
    # Переход на таб филиалы
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    REFERENCE_BOOKS = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    FILIAL_TAB = (By.XPATH, '//div[text()="Филиалы"]')
    # Таблица филиалы
    ADD_FILIAL_BUTTON = (By.XPATH, '//button[contains(@class,"MuiButton-root MuiButton-text MuiButton-textPrimary")]')
    REDACT_BUTTON = (By.XPATH, '//span[text()="Редактировать"]')
    KEBAB_VIEW_FULL_INFO_BUTTON = (By.XPATH, '//span[text()="Просмотр полной информации"]')
    KEBAB_DELETE_BUTTON = (By.XPATH, '//span[text()="Удалить"]')
    KEBAB_MENU = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    NAME_HEADING = (By.XPATH, '//h6[text()="Название"]')
    ADDRESS_HEADING = (By.XPATH, '//h6[text()="Адрес"]')
    PARENT_FILIAL_HEADING = (By.XPATH, '//h6[text()="Родительский филиал"]')
    ACTIONS_HEADING = (By.XPATH, '//span[text()="Действия"]')
    # Дровер добавления/редактирования филиала
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[name="address"]')
    ATTRACTION_RATE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Выберите ставку привлечения"]')
    ATTRACTION_RATE_SIZE_FIELD = (By.CSS_SELECTOR, 'input[name="attractionRateSize"]')
    EMPLOYEES_FIELD = (By.CSS_SELECTOR, 'div[name="employees"]')
    EMPLOYEES_CHIPS = (By.XPATH, '//div[@name="employees"]//span[contains(@class,"MuiChip-label")]')
    EMPLOYEES_CHIPS_DELETE_ICON = (By.XPATH, '//div[@name="employees"]//span[contains(@class,"MuiChip-label")]/..//*[@data-testid="CancelIcon"]')
    DIRECTOR_FIELD = (By.CSS_SELECTOR, 'div[name="director"]')
    CLEAR_DIRECTOR_FIELD_BUTTON = (By.XPATH, '//div[@name="director"]//button[@aria-label="Очистить поле"]')
    AFFILIATE_FIELD = (By.CSS_SELECTOR, 'div[name="affiliate"]')
    PHONE_FIELD = (By.CSS_SELECTOR, 'input[name="phone"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    # Ошибки
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    # Элементы дропдауна
    DROPDOWN_ITEMS = (By.CSS_SELECTOR, 'li[class^="MuiAutocomplete-option"]')
    def text_on_page(self, name):
        return (By.XPATH, f'//*[text()="{name}"]')

    def address_by_filial_name(self, name):
        return (By.XPATH, f'//div[text()="{name}"]/..//following-sibling::div[@col-id="address"]/div')

    def kebab_by_filial_name(self, name):
        return (By.XPATH, f'//div[text()="{name}"]/..//following-sibling::div[@aria-colindex="4"]//button')

    OPEN_ICON_ATTRACTION_RATES_FIELD = (By.XPATH, '//div[@name="attractionRate"]//button')
    ATTRACTION_RATES = (By.XPATH, "//ul[contains(@class, 'MuiAutocomplete-listbox')]//li")