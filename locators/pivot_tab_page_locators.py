from selenium.webdriver.common.by import By

from data.data import PROJECT_NAME, USER_NAME


class PivotTabPageLocators:
    #
    ANALYTIC_MENU_BUTTON = (By.XPATH, '//button[text()="Аналитика"]')
    PIVOT_TAB_BUTTON = (By.CSS_SELECTOR, 'a[href="/pivot-table/project"]')
    #
    PERIOD_SELECT_BUTTON = (By.CSS_SELECTOR, 'div[class="MuiInput-root MuiInputBase-root MuiInputBase-colorPrimary onboaring__period-select css-ftxbrz"]')
    WEEK_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="week"]')
    MONTH_BY_DAY_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="monthByDay"]')
    MONTH_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="month"]')
    #
    GET_ROW_ID = (By.XPATH, f'//h6[text()="{PROJECT_NAME}"]//ancestor::div[@row-id]')
    GET_ROW_ID_ON_USER = (By.XPATH, f'//p[text()="{PROJECT_NAME}"]//ancestor::div[@row-id]')

    TEST_1 = (By.XPATH, '//div[@row-id="row-group-383"]//div[@col-id="workdaysHoursSum"]')

    HORIZONTAL_SCROLL = (By.CSS_SELECTOR, 'div[class="ag-body-horizontal-scroll-viewport"]')
    RIGHT_SCROLL = (By.CSS_SELECTOR, 'div[class="ag-horizontal-right-spacer ag-scroller-corner"]')

    BY_USER_BUTTON = (By.XPATH, '//button[text()="По пользователям"]')
    OPEN_PROJECT_LIST = (By.XPATH, f'//h6[@aria-label="{USER_NAME}"]//ancestor::span[1]//preceding::span[2]')

