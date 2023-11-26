from selenium.webdriver.common.by import By

from data.data import PROJECT_NAME, USER_NAME


class PivotTabPageLocators:
    # Переход на сводную таблицу
    ANALYTIC_MENU_BUTTON = (By.XPATH, '//button[text()="Аналитика"]')
    PIVOT_TAB_BUTTON = (By.CSS_SELECTOR, 'a[href="/pivot-table/project"]')
    # Выбор периода отображения
    PERIOD_SELECT_BUTTON = (By.XPATH, '//div[contains(@class, "onboaring__period-select")]')
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
    OPEN_PROJECT_LIST = (By.XPATH, f'//h6[@aria-label="{USER_NAME}"]//ancestor::span[1]//preceding::span[2]')
    # Кнопка фильтрации
    FILTER_BUTTON = (By.XPATH, '//button[contains(@class, " MuiButton-textSizeSmall MuiButton-disableElevation")]')

