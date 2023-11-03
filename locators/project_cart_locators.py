from selenium.webdriver.common.by import By


class ProjectCardLocators:
    #
    DESCRIPTION_TAB = (By.XPATH, '//button[text()="Описание"]')
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    CODE_FIELD = (By.CSS_SELECTOR, 'input[name="code"]')
    BEGIN_DATA_FIELD = (By.CSS_SELECTOR, 'input[id="mui-502"]')
    AUTOR_NAME_FIELD = (By.XPATH, '//a[contains(@class, "MuiTypography-root MuiTypography-button")]')

    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')

    TEAM_TAB = (By.XPATH, '//button[text()="Команда"]')
