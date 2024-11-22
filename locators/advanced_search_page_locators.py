from selenium.webdriver.common.by import By


class AdvancedSearchPageLocators:
    # Переход на страницу расширенного поиска
    COLLEAGUES_TAB = (By.CSS_SELECTOR, 'div[id="colleagues"]')
    ALL_COLLEAGUES = (By.CSS_SELECTOR, 'a[href="/users/department"]')
    ADVANCED_SEARCH = (By.CSS_SELECTOR, 'a[href="/kk/user-search"]')
    ALL_PROFILE_MENU_ITEMS_TEXT = (By.XPATH, '//li[@role="menuitem"]//a')
    TO_ADVANCED_SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[class^="MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeSmall"]')
    BREAK_SEARCH_BUTTON = (By.XPATH, '//button[text()="Сбросить поиск"]')
    EXPORT_TO_EXEL_BUTTON = (By.XPATH, '//p[text()="Экспорт в Excel"]')
    COLUMNS_TITLES = (By.CSS_SELECTOR, 'span[class="ag-header-cell-text"]')

    NEW_SEARCH_BUTTON = (By.XPATH, '//button[text()="Новый поиск"]')
    OPEN_BUTTONS = (By.CSS_SELECTOR, 'button[title="Открыть"]')
    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    MENU_ITEM_TEXT = (By.XPATH, '//li[@role="menuitem"]//span[contains(@class,"MuiTypography-root MuiTypography-caption")]')
    SAVE_SEARCH_BUTTON = (By.XPATH, '//button[text()="Сохранить поиск"]')
    DELETE_SEARCH_BUTTON = (By.XPATH, '//button[text()="Удалить сохраненный поиск"]')
    RESET_ALL_BUTTON = (By.XPATH, '//button[text()="Сбросить все"]')
    SEARCH_BUTTON = (By.XPATH, '//button[text()="Найти"]')

    SEARCH_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="textValue"]')
    CHECK_ICON = (By.CSS_SELECTOR, 'svg[data-testid="CheckIcon"]')
    CLOSE_ICON = (By.XPATH, '//label[text()="Название поиска"]/../..//*[@data-testid="CloseIcon"]')

    SEARCH_CHIPS = (By.XPATH, '//button[@role="tab"]//div')
    SAVED_SEARCH_TITLE = (By.XPATH, '//div[@role="dialog"]//h6')
    ALL_FIELDS = (By.CSS_SELECTOR, 'input[role="combobox"]')
    CRITERION_FIELD = (By.XPATH, '//label[text()="Выберите критерий поиска"]/..//input')
    RUL_FIELD = (By.XPATH, '//label[text()="Правило"]/..//input')
    STATUS_VALUE_FIELD = (By.XPATH, '//div[contains(@class,"rule-value")]//input')
    DELETE_ICON = (By.CSS_SELECTOR, 'svg[data-testid="DeleteIcon"]')
    TOOLTIP = (By.XPATH, '//div[contains(@class, "MuiTooltip-tooltipPlacementTop")]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отмена"]')

    def chips_by_name(self, name):
        return (By.XPATH, f'//div[text()="{name}"]')

    def li_by_aria_label(self, name):
        return (By.CSS_SELECTOR, f'li[aria-label="{name}"]')

    KEBAB_MENU_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    ADD_RULES_BUTTON = (By.XPATH, '//span[text()="Добавить правило"]')
    ADD_GROUP_BUTTON = (By.XPATH, '//span[text()="Добавить группу"]')
    DELETE_GROUP_BUTTON = (By.XPATH, '//span[text()="Удалить группу"]')

    AND_SWITCH = (By.CSS_SELECTOR, 'button[value="and"]')
    OR_SWITCH = (By.CSS_SELECTOR, 'button[value="or"]')

    ALERT_MESSAGE = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')

    COLUMN_HEADER = (By.CSS_SELECTOR, 'div[role="columnheader"]')
    SEARCH_FIELDS = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')
    DEPARTMENTS_COLUMN = (By.CSS_SELECTOR, 'div[col-id="department"][role="gridcell"]')

    NAME_SEARCH = (By.XPATH, '//div[@aria-colindex="2"]//input[@placeholder="Поиск"]')
    STATUS_FILTER_BUTTON = (By.XPATH, '//div[@aria-colindex="5"]//button')
    WORK_CHECKBOX = (By.XPATH, '//div[contains(@class,"ag-checkbox-label")][text()="Работает"]')
    FIRED_CHECKBOX = (By.XPATH, '//div[contains(@class,"ag-checkbox-label")][text()="Уволен"]')
    USER_LINK = (By.CSS_SELECTOR, 'a[target="_blank"]')

    def text_on_page(self, name):
        return (By.XPATH, f'//*[text()="{name}"]')