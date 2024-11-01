from selenium.webdriver.common.by import By

from data.data import PROJECT_NAME, USER_NAME


class PivotTabPageLocators:
    # Переход на сводную таблицу
    ANALYTIC_MENU_BUTTON = (By.XPATH, '//button[text()="Аналитика"]')
    PIVOT_TAB_BUTTON = (By.CSS_SELECTOR, 'a[href="/pivot-table/project"]')
    # Выбор периода отображения
    PERIOD_SELECT_BUTTON = (
    By.XPATH, '//div[contains(@class, "MuiSelect-select MuiSelect-standard MuiInput-input MuiInputBase-input")]')
    WEEK_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="week"]')
    MONTH_BY_DAY_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="monthByDay"]')
    MONTH_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="month"]')
    YEAR_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="year"]')
    # Берем номер строки по имени объекта
    GET_ROW_ID = (By.XPATH, f'//h6[text()="{PROJECT_NAME}"]//ancestor::div[@row-id]')
    GET_ROW_ID_ON_USER = (By.XPATH, f'//p[text()="{PROJECT_NAME}"]//ancestor::div[@row-id]')
    # Скроллер при отображении месяца по дням
    HORIZONTAL_SCROLL = (By.CSS_SELECTOR, 'div[class="ag-body-horizontal-scroll-viewport"]')
    RIGHT_SCROLL = (By.CSS_SELECTOR, 'div[class="ag-horizontal-right-spacer ag-scroller-corner"]')
    # Отображение по пользователю
    BY_USER_BUTTON = (By.XPATH, '//button[text()="По пользователям"]')
    BY_PROJECT_BUTTON = (By.XPATH, '//button[text()="По проектам"]')
    OPEN_PROJECT_LIST = (By.XPATH, f'//h6[contains(@aria-label,"{USER_NAME}")]//ancestor::span[1]//preceding::span[2]')
    ICON_TREE_CLOSED = (By.CSS_SELECTOR, 'span[class="ag-icon ag-icon-tree-closed"]')
    EXPORT_TO_JSON_BUTTON = (By.XPATH, '//button[text()="Экспорт в JSON"]')
    EXPORT_TO_EXEL_BUTTON = (By.XPATH, '//button[text()="Экспорт в Excel"]')
    def project_color_on_user(self, project_name):
        return (By.XPATH, f'//p[text()="{project_name}"]')

    # Кнопка фильтрации
    FILTER_BUTTON = (By.XPATH,
                     '//button[contains(@class, "MuiButton-textPrimary MuiButton-sizeSmall MuiButton-textSizeSmall MuiButton-disableElevation")]')
    HEADER_TODAY = (By.XPATH, '//div[contains(@class,"header-today")]')
    NOT_ACTIV_PROJECT_CHECKBOX = (By.XPATH, '//p[text()="Неактивные проекты"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    def get_row_id_on_project(self, project_name):
        return (By.XPATH, f'//h6[text()="{project_name}"]//ancestor::div[@row-id]')

    def get_row_id_on_user(self, project_name):
        return (By.XPATH, f'//p[text()="{project_name}"]//ancestor::div[@row-id]')

    def intersection_field(self, row_id, col_index):
        return (By.XPATH, f'//div[@row-id="{row_id}"]//div[@aria-colindex="{col_index}"]//p')

    def check_name_project_color(self, project_name):
        return (By.XPATH, f'//h6[text()="{project_name}"]')

    CHOSE_PERIOD_BUTTON = (By.CSS_SELECTOR, 'div[aria-haspopup="listbox"]')
    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')

    NEXT_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronRightIcon"]')
    PREVIOUS_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronLeftIcon"]')
    THIS_DAY_BUTTON = (By.XPATH, '//button[contains(@class, "DateInterval-setToday")]')

    USERS_COLUMN = (By.XPATH, '//span[text()="Пользователь"]')
    OPEN_FILTER_BUTTON_USER_COLUMN = (By.CSS_SELECTOR, 'span[ref="eMenu"')
    FILTER_USER_COLUMN = (By.CSS_SELECTOR, 'span[aria-label="filter"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[aria-label="Search filter values"]')
    LISTBOX_ITEMS = (By.CSS_SELECTOR, 'div[role="option"]')

    TAB_TITLE = (By.CSS_SELECTOR, 'span[class="ag-header-cell-text"]')
    COLUMN_TITLES = (By.XPATH, '//div[contains(@class,"ag-header-cell-")]//h6')
    TAB_HEADER_WEEK_TEXT = (By.XPATH, '//div[contains(@class,"ag-header-cell")]//span[contains(@class,"MuiTypography-caption")]')