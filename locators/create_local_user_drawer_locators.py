from selenium.webdriver.common.by import By


class CreateLocalUserDrawerLocators:
    # Локаторы для перехода на дровер
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    SYSTEM_ROLE = (By.CSS_SELECTOR, 'a[href="/admin/system-roles/users"]')
    ADD_LOCAL_USER_BUTTON = (By.XPATH, '//button[text()="Пользователь"]')
    # Локаторы полей на дровере
    ALL_DRAWER_FIELDS = (By.XPATH, '//input[contains(@class, "MuiOutlinedInput-input")]')
    INPUT_NAME_FIELDS = (By.XPATH, '//input[contains(@class, "MuiOutlinedInput-input")][@name]')
    INPUT_PLACEHOLDER_FIELDS = (By.XPATH, '//input[contains(@class, "MuiOutlinedInput-input")][@placeholder]')
    HOUR_PAY_CHECKBOX = (By.XPATH, '//span[text()="Почасовая оплата"]')
    TAB_PROJECTS = (By.XPATH, '//button[text()="ПРОЕКТЫ"]')
    TAB_CONTACTS = (By.XPATH, '//button[text()="КОНТАКТЫ"]')
    ADD_PROJECTS_BUTTON = (By.XPATH, '//button[text()="Добавить проект"]')
    PROJECTS_FIELDS = (By.XPATH, '//label[contains(@class, "MuiInputLabel-outlined")]')
    PROJECT_MANAGER_CHECKBOX = (By.XPATH, '//span[text()="Руководитель проекта"]')




