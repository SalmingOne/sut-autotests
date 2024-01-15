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
    # Локаторы вкладки проекты
    TAB_PROJECTS = (By.XPATH, '//button[text()="ПРОЕКТЫ"]')
    ADD_PROJECTS_BUTTON = (By.XPATH, '//button[text()="Добавить проект"]')
    DELETE_PROJECTS_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Удалить проект"]')
    PROJECTS_FIELDS = (By.XPATH, '//label[contains(@class, "MuiInputLabel-outlined")]')
    PROJECT_MANAGER_CHECKBOX = (By.XPATH, '//span[text()="Руководитель проекта"]')
    # Локаторы вкладки контакты
    TAB_CONTACTS = (By.XPATH, '//button[text()="КОНТАКТЫ"]')
    # Кнопки на всех вкладках
    CLEAR_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ClearIcon"]')
    SAVE_BUTTON = (By.XPATH, '//button[contains(@class, "onboarding__save-button")]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    # Обязательные поля
    LOGIN_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')
    SECOND_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="secondName"]')
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    GENDER_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Начните вводить пол"]')
    GENDER_MAILE = (By.XPATH, '//li[text()="Мужской"]')
    PROJECT_ROLES_FIELD = (By.CSS_SELECTOR, 'div[name="projectRoles"]')

    DEPARTMENT_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Начните вводить подразделение"]')
    POSITION_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Начните вводить должность"]')

    PROJECT_FIELD = (By.XPATH, '//label[text()="Проект"]/../div')

    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')

    DROPDOWN_ITEMS = (By.XPATH, '//li[contains(@class, "MuiAutocomplete-option MuiBox-root")]')
    ALERT_MESSAGE = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
