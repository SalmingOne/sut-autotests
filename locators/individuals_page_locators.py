from selenium.webdriver.common.by import By


class IndividualsPageLocators:
    # Переход на таб Физические лица
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    REFERENCE_BOOKS = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    INDIVIDUALS_TAB = (By.XPATH, '//div[text()="Физические лица"]')

    ADD_INDIVIDUALS_BUTTON = (By.XPATH, '//button[text()="Добавить физическое лицо"]')
    # Дровер добавления физического лица
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    SECOND_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="secondname"]')
    TIRD_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="thirdname"]')
    INN_FIELD = (By.CSS_SELECTOR, 'input[name="inn"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[name="address"]')
    PHONE_FIELD = (By.CSS_SELECTOR, 'input[name="phone"]')
    DOCUMENT_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="documentName"]')
    DOCUMENT_SECOND_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="documentSecondname"]')
    DOCUMENT_TIRD_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="documentThirdname"]')
    SERIES_FIELD = (By.CSS_SELECTOR, 'input[name="series"]')
    NUMBER_FIELD = (By.CSS_SELECTOR, 'input[name="number"]')
    AUTHORITY_FIELD = (By.CSS_SELECTOR, 'input[name="authority"]')
    BANK_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="bankName"]')
    BANK_INN_FIELD = (By.CSS_SELECTOR, 'input[name="bankInn"]')
    BANK_ACCOUNT_FIELD = (By.CSS_SELECTOR, 'input[name="bankAccount"]')
    BANK_CORRESPONDENT_ACCOUNT_FIELD = (By.CSS_SELECTOR, 'input[name="bankCorrespondentAccount"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
    ROLE_DROPDOWN = (By.CSS_SELECTOR, 'div[name="role"]')
    DOCUMENT_TYPE_DROPDOWN = (By.CSS_SELECTOR, 'div[name="documentType"]')
    DATE_PIKERS = (By.CSS_SELECTOR, 'input[type="tel"]')
    DROPDOWN_ITEMS = (By.CSS_SELECTOR, 'li[class^="MuiAutocomplete-option"]')
    BANK_BIC_FIELD = (By.CSS_SELECTOR, 'input[name="bankBic"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    # Ошибки
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    # Поля поиска
    SEARCH_TAB_FIELDS = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')
    # Кебаб меню
    KEBABS = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    KEBAB_MENU_ITEM = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption"]')
    FULL_INFO_BUTTON = (By.XPATH, '//span[text()="Просмотр полной информации"]')
    REDACT_BUTTON = (By.XPATH, '//span[text()="Редактировать"]')
    DELETE_BUTTON = (By.XPATH, '//span[text()="Удалить"]')


    def check_name_in_tab(self, name):
        return (By.XPATH, f'//div[@col-id="fullName"]//div[@aria-label="{name}"]')
