from selenium.webdriver.common.by import By


class StacksPageLocators:
    # Переход на таб Стеки
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    REFERENCE_BOOKS = (By.CSS_SELECTOR, 'a[href="/admin/references/personal-qualities"]')
    STACKS_TAB = (By.XPATH, '//div[text()="Стеки"]')
    # Таблица Стеки
    ADD_STACK_BUTTON = (By.XPATH, '//button[text()="Добавить"]')
    KEBABS_REDACT_MENU_ITEM = (By.XPATH, '//span[text()="Редактировать"]')
    KEBABS_VIEW_MENU_ITEM = (By.XPATH, '//span[text()="Просмотр"]')
    # Стек в режиме просмотра
    TITLES = (By.XPATH, '//div[contains(@class,"MuiPaper-elevation0")]//h6')
    REDACT_BUTTON = (By.XPATH, '//button[text()="Редактировать"]')
    CLOSE_BUTTON = (By.XPATH, '//button[text()="Закрыть"]')
    # Страница добавления стека
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    NAME_FIELD_COLOR = (By.XPATH, '//input[@name="name"]//following-sibling::fieldset')
    DEPARTMENT_FIELD = (By.XPATH, '//div[@name="departmentId"]//input')
    DEPARTMENT_FIELD_COLOR = (By.XPATH, '//div[@name="departmentId"]//input//following-sibling::fieldset')
    CLEAR_DEPARTMENT_FIELD = (By.CSS_SELECTOR, 'svg[data-testid="CloseIcon"]')
    ADD_SKILL_BUTTON = (By.XPATH, '//button[text()="Добавить знание/навык"]')
    SKILLS_NAMES = (By.XPATH, '//div[@col-id="name"]//p')
    DELETE_SKILL_BUTTON = (By.CSS_SELECTOR, 'button[title="Удалить"]')
    # Дровер добавления навыка/знания в стек
    SKILL_NAME_INPUT = (By.XPATH, '//div[@name="name"]//input')
    SKILL_TYPE_INPUT = (By.XPATH, '//div[@name="type"]//input')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'input[name="description"]')
    BREAK_BUTTON = (By.XPATH, '//div[@name="name"]//following::button[text()="Отменить"]')

    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Подтвердить"]')
    MODAL_BREAK_BUTTON = (By.XPATH, '//div[@role="dialog"]//following::button[text()="Отменить"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "MuiFormHelperText-root Mui-error")]')
    TOOLTIP = (By.XPATH, '//div[contains(@class,"MuiTooltip-tooltip")]')

    def text_on_page(self, name):
        return (By.XPATH, f'//*[text()="{name}"]')

    def li_by_text(self, name):
        return (By.XPATH, f'//li[text()="{name}"]')

    def kebab_by_stack_name(self, name):
        return (By.XPATH, f'//p[text()="{name}"]/..//following-sibling::div[@aria-colindex="3"]//button')