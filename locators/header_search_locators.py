from selenium.webdriver.common.by import By


class HeaderSearchLocators:
    # Поле поиска в хедере
    SEARCH_HEADER_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')
    SEARCH_RESULTS_LIST = (By.CSS_SELECTOR, 'div[class="MuiBox-root css-1p7vog0"]')
    SEARCH_RESULTS_PROJECTS = (By.XPATH, '//ul//div[text()="Проекты"]')
    SEARCH_RESULTS_USERS = (By.XPATH, '//ul//div[text()="Пользователи"]')

    # Тултип
    TOOLTIP = (By.XPATH, '//div[contains(@class, "MuiTooltip-tooltipPlacementBottom")]')
