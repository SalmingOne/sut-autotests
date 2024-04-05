from selenium.webdriver.common.by import By


class FilialPageLocators:
    # Переход на таб Знания
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    REFERENCE_BOOKS = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    FILIAL_TAB = (By.XPATH, '//div[text()="Филиалы"]')
    # Таблица филиалы
    ADD_FILIAL_BUTTON = (By.XPATH, '//button[contains(@class,"MuiButton-root MuiButton-text MuiButton-textPrimary")]')
    # Дровер добавления/редактирования филиала
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[name="address"]')
    ATTRACTION_RATE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Выберите ставку привлечения"]')
    ATTRACTION_RATE_SIZE_FIELD = (By.CSS_SELECTOR, 'input[name="attractionRateSize"]')
    EMPLOYEES_FIELD = (By.CSS_SELECTOR, 'div[name="employees"]')
    DIRECTOR_FIELD = (By.CSS_SELECTOR, 'div[name="director"]')
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