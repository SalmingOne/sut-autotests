from selenium.webdriver.common.by import By


class TagsPageLocators:
    # Переход на таб группа знаний
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    REFERENCE_BOOKS = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    TAG_TAB = (By.XPATH, '//div[text()="Группы знаний"]')
    # Таб группа знаний
    ADD_TAG_BUTTON = (By.XPATH, '//button[contains(@class,"MuiButton-root MuiButton-text MuiButton-textPrimary")]')
    KEBABS_REDACT_MENU_ITEM = (By.XPATH, '//span[text()="Редактировать"]')
    KEBAB_MENU_ITEM = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption"]')
    KEBAB_MENU = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    SORT_TAGS_BUTTON = (By.XPATH, '//span[@class="ag-header-cell-text"][text()="Группы знаний"]')
    COLUMN_TITLES = (By.XPATH, '//span[@class="ag-header-cell-text"]')
    # Дровер добавления и редактирования группы знаний
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    SKILL_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Выберите знания"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    # Ошибки
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    def check_li_item_by_text(self, name):
        return (By.XPATH, f'//li[text()="{name}"]')

    def text_on_page(self, name):
        return (By.XPATH, f'//*[text()="{name}"]')
    def kebab_by_tag_name(self, name):
        return (By.XPATH, f'//*[text()="{name}"]//ancestor::div[@role="gridcell"]//following-sibling::div[@aria-colindex="4"]//button')