from selenium.webdriver.common.by import By


class AllProjectPageLocators:

    TAB_PROJECTS = (By.CSS_SELECTOR, "div[id='projects']")
    TAB_ALL_PROJECTS = (By.CSS_SELECTOR, 'a[href="/admin/projects?displayOnlyMyProjects=false&create=false"]')
    CREATE_PROJECT_BUTTON = (By.XPATH, '//button[text()="Создать проект"]')

    ALL_PROJECT_NAMES_AND_CODS = (By.XPATH, '//div[contains(@class, "ag-center-cols-container")]//div[@class="MuiBox-root css-0"]')
    CHECK_NAME_PROJECT = (By.XPATH, '//div[text()="AutoTestProject"]')# вынести название проекта в отдельную переменную





