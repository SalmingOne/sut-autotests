from selenium.webdriver.common.by import By


class AllProjectPageLocators:
    # Пункты меню для перехода на страницу все проекты
    TAB_PROJECTS = (By.CSS_SELECTOR, "div[id='projects']")
    TAB_ALL_PROJECTS = (By.CSS_SELECTOR, 'a[href="/admin/projects?displayOnlyMyProjects=false&create=false"]')
    ALL_PROJECTS_MENU_ITEMS = (By.XPATH, '//li[@role="menuitem"]/a')
    # Локатор проверки, что имя проекта есть на странице
    def check_project_name_on_tab(self, project_name):
        return By.XPATH, f'//div[text()="{project_name}"]'

    ALL_PROJECTS_NAMES = (By.XPATH, '//div[@col-id="name"][@role="gridcell"]/div')
    CREATE_PROJECT_BUTTON = (By.XPATH, '//button[text()="Создать проект"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ALL_ACTION_BUTTONS = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    ACTION_MENU_ITEMS = (By.XPATH, '//li[@role="menuitem"]/span[contains(@class,"MuiTypography-caption")]')
    def project_action_button(self, project_name):
        return (By.XPATH, f'//div[text()="{project_name}"]//ancestor::div[contains(@class,"ag-row-level-0")]//button')

    PROJECT_DELETE_BUTTON = (By.XPATH, '//span[text()="Удалить"]')
    # Локаторы фильтрации проектов по статусам
    STATUS_FILTER_BUTTON = (By.XPATH, '//div[@aria-colindex="5"]//button')
    MARK_ALL_STATUS = (By.XPATH, '//div[text()="Выделить всё"]')
    #
    TAB_TITLE = (By.XPATH, '//h6[text()="Проекты"]')
    ONLY_MY_PROJECTS_CHECKBOX = (By.XPATH, '//p[text()="Отображать только мои проекты"]')
    TAT_COLUMN_TITLES = (By.CSS_SELECTOR, 'span[class="ag-header-cell-text"]')



