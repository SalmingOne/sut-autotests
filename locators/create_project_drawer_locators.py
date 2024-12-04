from selenium.webdriver.common.by import By
from data import data


class CreateProjectDrawerLocators:
    # Переходим на вкладку создания проекта и все проекты
    TAB_PROJECTS = (By.CSS_SELECTOR, "div[id='projects']")
    TAB_CREATE_PROJECT = (By.CSS_SELECTOR, 'a[href="/admin/projects?displayOnlyMyProjects=false&create=true"]')
    TAB_ALL_PROJECTS = (By.CSS_SELECTOR, 'a[href="/admin/projects?displayOnlyMyProjects=false&create=false"]')
    CREATE_PROJECT_BUTTON = (By.XPATH, '//button[text()="Создать проект"]')
    # Поля дровера создания проекта
    PROJECT_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    PROJECT_CODE_FIELD = (By.CSS_SELECTOR, 'input[name="code"]')
    PROJECT_BEGIN_DATA_FIELD = (By.XPATH, '//label[text()="Дата начала"]//following::input[1]')
    PROJECT_END_DATA_FIELD = (By.XPATH, '//label[text()="Дата начала"]//following::input[2]')
    PRIORITY_FIELD = (By.XPATH, '//label[text()="Приоритет"]/../div/span')
    FIRST_NOT_CHOOSE = (By.XPATH, '//li[@aria-selected="false"][1]')
    COLOR_MENU_ITEM = (By.CSS_SELECTOR, 'svg[data-testid="CircleIcon"]')
    PROJECT_RECOURSE_FIELD = (By.XPATH, '//div[@name="resources"]//following::input[1]')
    PROJECT_MANAGER_FIELD = (By.XPATH, '//div[@name="projectManagers"]//child::input[1]')
    REASON_CHECKBOX = (By.XPATH, '//span[text()="Обязательно указание причины списания трудозатрат"]')
    DRAFT_CHECKBOX = (By.XPATH, '//span[text()="Черновик"]')
    CHOSE_ADMIN = (By.XPATH, f'//p[text()="{data.USER_NAME}"]')
    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    BREAK_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Подтвердить"]')
    # Локатор проверки, что мы оказались на вкладке команда после создания проекта
    CHECK_CREATE_PROJECT = (By.XPATH, '//h6[text()="Команда"]')

    # Ошибки
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    ALERT_MESSAGE = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
