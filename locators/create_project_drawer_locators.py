from selenium.webdriver.common.by import By
from data import data

class CreateProjectDrawerLocators:
    # Переходим на вкладку создания пректа и все проекты
    TAB_PROJECTS = (By.CSS_SELECTOR, "div[id='projects']")
    TAB_CREATE_PROJECT = (By.CSS_SELECTOR, 'a[href="/admin/projects?displayOnlyMyProjects=false&create=true"]')
    TAB_ALL_PROJECTS = (By.CSS_SELECTOR, 'a[href="/admin/projects?displayOnlyMyProjects=false&create=false"]')
    CREATE_PROJECT_BUTTON = (By.XPATH, '//button[text()="Создать проект"]')
    #Поля дровера создания проекта
    PROJECT_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    PROJECT_CODE_FIELD = (By.CSS_SELECTOR, 'input[name="code"]')
    PROJECT_BEGIN_DATA_FIELD = (By.XPATH, '//label[text()="Дата начала"]//following::input[1]')
    PROJECT_RECOURSE_FIELD = (By.XPATH, '//div[@name="resources"]//following::input[1]')
    PROJECT_MANAGER_FIELD = (By.XPATH, '//div[@name="projectManagers"]//child::input[1]')
    REASON_CHECKBOX = (By.XPATH, '//span[text()="Обязательно указание причины списания трудозатрат"]')
    DRAFT_CHECKBOX = (By.XPATH, '//span[text()="Черновик"]')
    CHOSE_ADMIN = (By.XPATH, f'//p[text()="{data.USER_NAME}"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    # Локатор проверки что мы оказались на вкладке команда после создания проекта
    CHECK_CREATE_PROJECT = (By.XPATH, '//h6[text()="Команда"]')
