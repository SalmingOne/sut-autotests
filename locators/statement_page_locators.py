from selenium.webdriver.common.by import By


class StatementPageLocators:
    # Переход на страницу трудозатрат
    TAB_ACTIVITY = (By.CSS_SELECTOR, 'div[id="activity"]')
    TAB_APPLICATION = (By.CSS_SELECTOR, 'a[href="/statements"]')
    # Отсутствия
    ALL_ABSENCE_KEBABS = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    PREVIOUS_ABSENCE_CHECKBOX = (By.XPATH, '//label[contains(@class, "MuiFormControlLabel-labelPlacementEnd")]')
    KEBABS_DEL_MENU_ITEM = (By.XPATH, '//span[text()="Удалить"]')
    DEL_ACCEPT_BUTTON = (By.XPATH, '//button[contains(@class, "onboarding__save-button ")]')
    KEBABS_REDACT_MENU_ITEM = (By.XPATH, '//span[text()="Редактировать"]')

    FIRST_AND_LAST_ABSENCE_DAY = (By.XPATH, '//input[contains(@class, "MuiInputBase-inputAdornedEnd")]')

    DRAWER_SAVE_BUTTON = (By.XPATH,
                          '//button[contains(@class, "MuiButtonBase-root onboarding__save-button onboarding__form-footer-save-button")]')

    ABSENCE_START_DATE_ON_TAB = (By.CSS_SELECTOR,
                                 'div[col-id="startDate"][class="ag-cell ag-cell-not-inline-editing ag-cell-normal-height ag-cell-value"]')
    ABSENCE_END_DATE_ON_TAB = (By.CSS_SELECTOR,
                           'div[col-id="endDate"][class="ag-cell ag-cell-not-inline-editing ag-cell-normal-height ag-cell-value"]')
