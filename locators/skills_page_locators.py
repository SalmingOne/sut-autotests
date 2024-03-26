from selenium.webdriver.common.by import By


class SkillsPageLocators:
    # Переход на таб Знания
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    REFERENCE_BOOKS = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    SKILLS_TAB = (By.XPATH, '//div[text()="Знания"]')
    # Таблица
    ADD_SKILLS_BUTTON = (By.XPATH, '//button[contains(@class,"MuiButton-root MuiButton-text MuiButton-textPrimary")]')
    AUDIT_TAB_COLUMN_TITLES = (By.XPATH, '//span[@class="ag-header-cell-text"]')
    KEBAB_MENU = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    KEBAB_MENU_ITEM = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption"]')

