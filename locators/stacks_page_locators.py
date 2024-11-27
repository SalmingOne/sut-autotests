from selenium.webdriver.common.by import By


class StacksPageLocators:
    # Переход на таб Стеки
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    REFERENCE_BOOKS = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    STACKS_TAB = (By.XPATH, '//div[text()="Стеки"]')
    # Таблица Стеки
    ADD_STACK_BUTTON = (By.XPATH, '//button[text()="Добавить"]')
    # Страница добавления стека
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    NAME_FIELD_COLOR = (By.XPATH, '//input[@name="name"]//following-sibling::fieldset')
    DEPARTMENT_FIELD = (By.XPATH, '//div[@name="departmentId"]//input')
    DEPARTMENT_FIELD_COLOR = (By.XPATH, '//div[@name="departmentId"]//input//following-sibling::fieldset')
    CLEAR_DEPARTMENT_FIELD = (By.CSS_SELECTOR, 'svg[data-testid="CloseIcon"]')
    ADD_SKILL_BUTTON = (By.XPATH, '//button[text()="Добавить знание/навык"]')
    DELETE_SKILL_BUTTON = (By.CSS_SELECTOR, 'button[title="Удалить"]')
    # Дровер добавления навыка/знания в стек
    SKILL_NAME_INPUT = (By.XPATH, '//div[@name="name"]//input')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Подтвердить"]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "MuiFormHelperText-root Mui-error")]')
    TOOLTIP = (By.XPATH, '//div[contains(@class,"MuiTooltip-tooltip")]')

    def text_on_page(self, name):
        return (By.XPATH, f'//*[text()="{name}"]')