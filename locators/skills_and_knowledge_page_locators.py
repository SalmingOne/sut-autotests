from selenium.webdriver.common.by import By


class SkillsAndKnowledgePageLocators:
    # Переход на таб Знания
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    REFERENCE_BOOKS = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    SKILLS_TAB = (By.XPATH, '//div[text()="Навыки и знания"]')
    # Таблица
    COLUMN_TITLES = (By.XPATH, '//div[@role="presentation"]//h6')
    COLUMN_ACTION_TITLE = (By.XPATH, '//span[@class="ag-header-cell-text"]')
    ADD_SKILLS_BUTTON = (By.XPATH, '//button[contains(@class,"MuiButton-root MuiButton-text MuiButton-textPrimary")]')
    SORT_SKILLS_BUTTON = (By.XPATH, '//div[@col-id="name"]//*[text()="Название"]')
    KEBAB_MENU = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    KEBAB_MENU_ITEM = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption"]')
    KEBABS_REDACT_MENU_ITEM = (By.XPATH, '//span[text()="Редактировать"]')
    KEBABS_DELETE_MENU_ITEM = (By.XPATH, '//span[text()="Удалить"]')
    # Дровер добавления знания
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    NAME_FIELD_COLOR = (By.XPATH, '//input[@name="name"]//following-sibling::fieldset')
    TYPE_FIELD = (By.XPATH, '//div[@name="type"]//input')
    TYPE_FIELD_COLOR = (By.XPATH, '//div[@name="type"]//following-sibling::fieldset')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'input[name="description"]')
    DESCRIPTION_FIELD_COLOR = (By.XPATH, '//input[@name="description"]//following-sibling::fieldset')


    CANSEL_ICON = (By.CSS_SELECTOR, 'svg[data-testid="CancelIcon"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    BREAK_BUTTON = (By.XPATH, '//div[contains(@class,"MuiDrawer-paper")]//button[text()="Отменить"]')
    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    MAX_LENGTH_PRESENTATION = (By.XPATH, '//div[text()="Превышено допустимое количество символов"]')

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

    def skill_name_on_page(self, name):
        return (By.XPATH, f'//div[@col-id="name"]//p[text()="{name}"]')
