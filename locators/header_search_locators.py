from selenium.webdriver.common.by import By




class HeaderSearchLocators:
    # Поле поиска в хедере
    SEARCH_HEADER_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')
    SEARCH_RESULTS_LIST = (By.CSS_SELECTOR, 'ul[role="menu"]')
    SEARCH_RESULTS_PROJECTS = (By.XPATH, '//ul//div[text()="Проекты"]')
    SEARCH_RESULTS_USERS = (By.XPATH, '//ul//div[text()="Пользователи"]')
    SEARCH_RESULTS_PROJECTS_LIST = (By.XPATH, '//li//a[contains(@href, "/projects/")]')
    SEARCH_RESULTS_USERS_LIST = (By.XPATH, '//li//a[contains(@href, "/kk/")]')

    # Тултип
    TOOLTIP = (By.XPATH, '//div[contains(@class, "MuiTooltip-tooltipPlacementBottom")]')
    NOTHING_FOUND_TEXT = (By.XPATH, '//div[@role="tooltip"]//p')

    # Страница результатов быстрого поиска
    TAB_ALL = (By.XPATH, '//button[text()="ВСЕ"]')
    TAB_USERS = (By.XPATH, '//button[text()="ПОЛЬЗОВАТЕЛИ"]')
    TAB_PROJECTS = (By.XPATH, '//button[text()="ПРОЕКТЫ"]')
    QUICK_SEARCH_USERS_LIST = (By.XPATH, '//div//a[contains(@href, "/kk/")]')
    QUICK_SEARCH_PROJECTS_LIST = (By.XPATH, '//a[contains(@href, "/projects/")]//span')
    GO_TO_USER_PAGE = (By.XPATH, '//div[text()="Информация о сотруднике"]/..')
