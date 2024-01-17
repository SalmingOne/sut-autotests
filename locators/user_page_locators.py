from selenium.webdriver.common.by import By


class UserPageLocators:
    # Переход на страницу Пользователи
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    SYSTEM_ROLE = (By.CSS_SELECTOR, 'a[href="/admin/system-roles/users"]')
    ADD_LOCAL_USER_BUTTON = (By.XPATH, '//button[text()="Пользователь"]')

    SEARCH_TAB_FIELDS = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')

    USER_KEBABS = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    USER_FULL_INFO_BUTTON = (By.XPATH, '//span[text()="Полная информация"]')

    CLEAR_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ClearIcon"]')
    USER_CARD_LABEL = (By.XPATH, '//label[contains(@class, "")]')
    USER_CARD_TITLE = (By.XPATH, '//h6[text()="Просмотр полной информации"]')

    TAB_PROJECTS = (By.XPATH, '//button[text()="ПРОЕКТЫ"]')
    TAB_CONTACTS = (By.XPATH, '//button[text()="КОНТАКТЫ"]')
