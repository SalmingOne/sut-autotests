from selenium.webdriver.common.by import By


class AdvancedSearchPageLocators:
    # Переход на страницу расширенного поиска
    COLLEAGUES_TAB = (By.CSS_SELECTOR, 'div[id="colleagues"]')
    ALL_COLLEAGUES = (By.CSS_SELECTOR, 'a[href="/users/department"]')
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

    ALL_FIELDS = (By.CSS_SELECTOR, 'input[role="combobox"]')
    CRITERION_FIELD = (By.XPATH, '//label[text()="Выберите критерий поиска"]/..//input')
    RUL_FIELD = (By.XPATH, '//label[text()="Правило"]/..//input')
    STATUS_VALUE_FIELD = (By.XPATH, '//label[text()="Статус"]/..//input')
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