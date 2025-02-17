from selenium.webdriver.common.by import By


class ProjectRolesPageLocators:
    name = None
    # Локаторы для перехода на табу Проектные роли
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    PERSONAL_QUALITIES_PAGE = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    PROJECT_ROLES_TAB = (By.XPATH, '//div[text()="Проектные роли"]')

    CREATE_ROLE_BUTTON = (By.XPATH, '//button[text()="Создать роль"]')

    INPUT_ROLE_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "MuiFormHelperText-root Mui-error")]')
    BORDER_COLOR = (By.XPATH, '//input[@name="name"]/../fieldset')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    DRAWER_CLEAR_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ClearIcon"]')
    COLOR_INPUT_FIELD = (By.CSS_SELECTOR, 'input[name="color"]')
    COLOR_INPUT_BUTTON = (By.XPATH, '//button[contains(@style,"background-color")]')
    SALARY_RATE_FIELD = (By.CSS_SELECTOR, 'input[name="salaryRate"]')
    ATTRACTION_RATE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Выберите ставку привлечения"]')
    ALL_ATTRACTION_RATES = (By.XPATH, '//li[contains(@data-option-index,"")]')
    MANAGER_ROLE_CHECKBOX = (By.XPATH, '//span[text()="Руководящая роль"]')

    @staticmethod
    def get_role_by_name(name):
        return By.XPATH, f'//div[text()="{name}"]'
    ROLE_SEARCH_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')
    ROLE_KEBABS = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    DEL_BUTTON_IN_KEBAB_MENU = (By.XPATH, '//span[text()="Удалить"]')
    REDACT_BUTTON_IN_KEBAB_MENU = (By.XPATH, '//span[text()="Редактировать"]')
    KEBAB_MENU_ITEMS = (By.XPATH, '//li[contains(@class, "MuiMenuItem-gutters")]/span[contains(@class,"MuiTypography-caption")]')
    PROJECT_ROLES_TAB_HEADERS = (By.XPATH, '//div[@class="ag-header-cell-comp-wrapper"]//h6')
    FILTER_ICONS = (By.CSS_SELECTOR, 'span[class="ag-icon ag-icon-filter"]')

    def get_role_kebab_menu_by_name(self, name):
        return By.XPATH, f'//div[text()="{name}"]/../following-sibling::div[@aria-colindex="5"]//button'

    OPEN_ICON_ATTRACTION_RATES_FIELD = (By.CSS_SELECTOR, 'svg[data-testid="ArrowDropDownIcon"]')
    ATTRACTION_RATES = (By.XPATH, "//ul[contains(@class, 'MuiAutocomplete-listbox')]//li")
