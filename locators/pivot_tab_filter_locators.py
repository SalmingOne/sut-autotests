from selenium.webdriver.common.by import By


class PivotTabFilterPageLocators:
    # Выбранные чек-боксы и радио-кнопки
    CHECKED_ELEMENTS = (By.XPATH, '//span[contains(@class, "Mui-checked")]')
    CHECKED_ELEMENTS_TEXT = (By.XPATH, '//span[contains(@class, "Mui-checked")]//following::p[1]')
    # Чек-боксы и радио-кнопки
    ALL_CHECKBOXES_AND_RADIOBUTTON = (By.XPATH, '//span[contains(@class, "MuiButtonBase-root")]')
    ALL_CHECKBOXES_AND_RADIOBUTTON_TEXT = (By.XPATH, '//span[contains(@class, "MuiButtonBase-root")]//following::p[1]')
    MEMBER_RADIOBUTTON = (By.XPATH, '//p[text()="Участник"]')
    NOT_ACTIV_USER_CHECKBOX = (By.XPATH, '//p[text()="Неактивные пользователи"]')
    NOT_ACTIV_PROJECT_CHECKBOX = (By.XPATH, '//p[text()="Неактивные проекты"]')
    INTEGRATION_CHECKBOX = (By.XPATH, '//p[text()="Активности по интеграциям"]')
    PROJECT_ROLES_INPUT = (By.XPATH, '//label[text()="Проектные роли"]/..//input')
    ELEMENTS_DROPDOWN_TEXT = (By.XPATH, '//p[contains(@class, "MuiTypography-noWrap")]')
    OPEN_FILIAL_DROPDOWN = (By.XPATH, '//label[text()="Филиалы"]/..//input')
    OPEN_INTEGRATION_DROPDOWN = (By.XPATH, '//div[@name="activityTypes"]//input[contains(@class, "MuiOutlinedInput-input")]')
    # Кнопка сбросить все
    RESET_ALL_BUTTON = (By.XPATH, '//button[text()="Сбросить все"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
