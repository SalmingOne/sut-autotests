from selenium.webdriver.common.by import By


class SkillsPageLocators:
    # Переход на таб Знания
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    REFERENCE_BOOKS = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    SKILLS_TAB = (By.XPATH, '//div[text()="Знания"]')
    TAG_TAB = (By.XPATH, '//div[text()="Группы знаний"]')
    # Таблица
    ADD_SKILLS_BUTTON = (By.XPATH, '//button[contains(@class,"MuiButton-root MuiButton-text MuiButton-textPrimary")]')
    SORT_SKILLS_BUTTON = (By.XPATH, '//span[@class="ag-header-cell-text"][text()="Знания"]')
    AUDIT_TAB_COLUMN_TITLES = (By.XPATH, '//span[@class="ag-header-cell-text"]')
    KEBAB_MENU = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    KEBAB_MENU_ITEM = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption"]')
    KEBABS_REDACT_MENU_ITEM = (By.XPATH, '//span[text()="Редактировать"]')
    # Дровер добавления знания
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    TAG_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Выберите группу знаний"]')
    CANSEL_ICON = (By.CSS_SELECTOR, 'svg[data-testid="CancelIcon"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    BREAK_BUTTON = (By.XPATH, '//div[contains(@class,"MuiDrawer-paper")]//button[text()="Отменить"]')

    MUI_ERROR = (By.XPATH, '//p[contains(@class, "MuiFormHelperText-root Mui-error")]')
    ARROW_DOWN = (By.CSS_SELECTOR, 'svg[data-testid="ArrowDropDownIcon"]')
    ALERT_TEXT = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
    def kebab_by_skill_name(self, name):
        return (By.XPATH, f'//*[text()="{name}"]//ancestor::div[@role="gridcell"]//following-sibling::div[@aria-colindex="4"]//button')
    def text_on_page(self, name):
        return (By.XPATH, f'//*[text()="{name}"]')

    def arrow_by_skill_name(self, name):
        return (By.XPATH, f'//span[text()="{name}"]/..//span[@class="ag-group-contracted "]//span')

    def check_li_item_by_text(self, name):
        return (By.XPATH, f'//li[text()="{name}"]')
