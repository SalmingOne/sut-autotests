from selenium.webdriver.common.by import By


class AdvancedSearchPageLocators:
    # Переход на страницу расширенного поиска
    COLLEAGUES_TAB = (By.CSS_SELECTOR, 'div[id="colleagues"]')
    ALL_COLLEAGUES = (By.CSS_SELECTOR, 'a[href="/users/department"]')
    TO_ADVANCED_SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[class^="MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeSmall"]')

    NEW_SEARCH_BUTTON = (By.XPATH, '//button[text()="Новый поиск"]')
    OPEN_BUTTONS = (By.CSS_SELECTOR, 'button[title="Открыть"]')
    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    SAVE_SEARCH_BUTTON = (By.XPATH, '//button[text()="Сохранить поиск"]')
    DELETE_SEARCH_BUTTON = (By.XPATH, '//button[text()="Удалить сохраненный поиск"]')

    SEARCH_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="textValue"]')
    CHECK_ICON = (By.CSS_SELECTOR, 'svg[data-testid="CheckIcon"]')

    SEARCH_CHIPS = (By.XPATH, '//button[@role="tab"]//div')

    ALL_FIELDS = (By.CSS_SELECTOR, 'input[role="combobox"]')
    TOOLTIP = (By.XPATH, '//div[contains(@class, "MuiTooltip-tooltipPlacementTop")]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    def chips_by_name(self, name):
        return (By.XPATH, f'//div[text()="{name}"]')