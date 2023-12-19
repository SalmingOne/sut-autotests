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


