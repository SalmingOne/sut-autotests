from selenium.webdriver.common.by import By


class ProjectCardLocators:
    AUTOR_NAME = (By.XPATH, '//a[contains(@class, "MuiTypography-root MuiTypography-button")]')
    # Локаторы вкладки Описание
    DESCRIPTION_TAB = (By.XPATH, '//button[text()="Описание"]')
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    CODE_FIELD = (By.CSS_SELECTOR, 'input[name="code"]')
    BEGIN_DATA_FIELD = (By.XPATH, '//label[text()="Дата начала"]//following::input[1]')
    MANAGER_LABEL = (By.XPATH, '//span[contains(@class, "MuiChip-label MuiChip-labelMedium")]')
    STATUS_FIELD = (By.XPATH,
                    '//input[contains(@class, "MuiOutlinedInput-input MuiInputBase-input MuiInputBase-inputAdornedEnd MuiAutocomplete-input")]')

    # Локаторы вкладки Команда
    TEAM_TAB = (By.XPATH, '//button[text()="Команда"]')
    REDACT_BUTTON = (By.XPATH, '//button[text()="Редактировать"]')
    ADD_BUTTON = (By.XPATH, '//button[text()="Добавить"]')
    FIRST_MEMBER_TEXT = (By.XPATH, '//div[@row-index="0"]//p')
    ALL_MEMBERS_TEXT = (By.XPATH, '//div[@row-index]//p')
    FIRST_MEMBER_TEXT_ON_REDACT = (By.XPATH, '//div[@row-index="0"]//input[contains(@class, "MuiOutlinedInput-input")]')
    SECOND_MEMBER_TEXT_ON_REDACT = (By.XPATH, '//div[@row-index="1"]//input[contains(@class, "MuiOutlinedInput-input")]')
    ALL_MEMBERS_TEXT_ON_REDACT = (By.XPATH, '//div[@row-index]//input[contains(@class, "MuiOutlinedInput-input")]')
    FIRST_NOT_CHOOSE = (By.XPATH, '//li[@aria-selected="false"][1]')

    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
