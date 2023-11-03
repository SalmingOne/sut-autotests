from selenium.webdriver.common.by import By


class CreateProjectDrawerLocators:

    TAB_PROJECTS = (By.CSS_SELECTOR, "div[id='projects']")
    TAB_CREATE_PROJECT = (By.CSS_SELECTOR, 'a[href="/admin/projects?displayOnlyMyProjects=false&create=true"]')
    TAB_ALL_PROJECTS = (By.CSS_SELECTOR, 'a[href="/admin/projects?displayOnlyMyProjects=false&create=false"]')
    CREATE_PROJECT_BUTTON = (By.XPATH, '//button[text()="Создать проект"]')

    PROJECT_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    PROJECT_CODE_FIELD = (By.CSS_SELECTOR, 'input[name="code"]')
    PROJECT_BEGIN_DATA_FIELD = (By.XPATH, '//label[text()="Дата начала"]//following::input[1]')
    PROJECT_RECOURSE_FIELD = (By.XPATH, '//div[@name="resources"]//following::input[1]')
    PROJECT_MANAGER_FIELD = (By.XPATH, '//div[@name="projectManagers"]//child::input[1]')

    CHOSE_ADMIN = (By.XPATH, '//p[text()="Администратор Администратор"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    CHECK_CREATE_PROJECT = (By.XPATH, '//h6[text()="Команда"]')
