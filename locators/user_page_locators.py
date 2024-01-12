from selenium.webdriver.common.by import By


class UserPageLocators:
    # Переход на страницу трудозатрат
    TAB_ACTIVITY = (By.CSS_SELECTOR, 'div[id="activity"]')

    SEARCH_TAB_FIELDS = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')
    USER_KEBABS = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')