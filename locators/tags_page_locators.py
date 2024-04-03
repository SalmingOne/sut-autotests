from selenium.webdriver.common.by import By


class TagsPageLocators:
    # Переход на таб группа знаний
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    REFERENCE_BOOKS = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    TAG_TAB = (By.XPATH, '//div[text()="Группы знаний"]')

    ADD_TAG_BUTTON = (By.XPATH, '//button[contains(@class,"MuiButton-root MuiButton-text MuiButton-textPrimary")]')

    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    SKILL_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Выберите знания"]')

    # Ошибки
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')

    def check_li_item_by_text(self, name):
        return (By.XPATH, f'//li[text()="{name}"]')

    def text_on_page(self, name):
        return (By.XPATH, f'//*[text()="{name}"]')