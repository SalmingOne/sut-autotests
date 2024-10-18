from selenium.webdriver.common.by import By


class HolidaysReferencePageLocators:
    # Переход на таб Праздничные дни
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    REFERENCE_BOOKS = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    HOLIDAYS_TAB = (By.XPATH, '//div[text()="Праздничные дни"]')
    
    # Таблица праздничных дней
    ADD_HOLIDAY_BUTTON = (By.XPATH, '//button[contains(@class,"MuiButton-root MuiButton-text MuiButton-textPrimary")]')
    KEBAB_EDIT_BUTTON = (By.XPATH, '//span[text()="Редактировать"]')
    KEBAB_DELETE_BUTTON = (By.XPATH, '//span[text()="Удалить"]')
    FIRST_MEMBER_TEXT_ON_REDACT = (By.XPATH, '//div[@row-index="0"]//input[contains(@class, "MuiOutlinedInput-input")]')
    
    # Дровер добавления праздничного дня
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    DATE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="ДД.MM.ГГГГ"]')
    ANNUALITY_FIELD = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    TYPE_DROPDOWN = (By.CSS_SELECTOR, 'div[name="type"]')
    TYPE_VALUE = (By.XPATH, '//div[@name="type"]//input')
    CLEAR_TYPE_DROPDOWN_BUTTON = (By.XPATH, '//div[@name="type"]//button[@aria-label="Очистить поле"]')
    PRIORITY_DROPDOWN = (By.CSS_SELECTOR, 'div[name="source"]')
    PRIORITY_VALUE = (By.XPATH, '//div[@name="source"]//input')
    CLEAR_PRIORITY_DROPDOWN_BUTTON = (By.XPATH, '//div[@name="source"]//button[@aria-label="Очистить поле"]')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'textarea[name="description"]')
    CANCEL_BUTTON = (By.XPATH, '//div[contains(@class,"MuiDrawer-paper")]//button[text()="Отменить"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    DROPDOWN_ITEMS = (By.CSS_SELECTOR, 'li[class^="MuiAutocomplete-option"]')
    GOAL_REASON_FIELD_IS_REQUIRED = (By.XPATH, "//div/p[contains(text(),'Поле обязательно')]")

    # Модальное окно при удалении
    ALERT_DIALOG_DESCRIPTION = (By.CSS_SELECTOR, 'p[id="alert-dialog-description"]')
    MODAL_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    MODAL_CANCEL_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    def kebab_by_holiday_name(self, name):
        return (By.XPATH, f'//div[text()="{name}"]/..//following-sibling::div[@col-id="1"]')

    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')