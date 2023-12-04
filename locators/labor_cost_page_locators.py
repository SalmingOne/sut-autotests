import random

from selenium.webdriver.common.by import By

from data.data import PROJECT_CODE, PROJECT_NAME


class LaborCostPageLocators:
    # Переход на страницу трудозатрат
    TAB_ACTIVITY = (By.CSS_SELECTOR, 'div[id="activity"]')
    TAB_LABOR_COST_TABLE = (By.CSS_SELECTOR, 'a[href="/"]')
    # Проверка, что код проекта есть на странице
    CHECK_CODE_PROJECT = (By.XPATH, f'//a[text()="{PROJECT_CODE}"]')
    # Дни в привязке к проекту
    ALL_DAYS_BY_PROJECT = (
        By.XPATH, f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div//input')
    RANDOM_DAYS_BY_PROJECT = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[{random.randint(2, 29)}]//input')
    FIRST_DAY_BY_PROJECT = (
        By.XPATH, f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[2]//input')
    LAST_28_DAY_BY_PROJECT = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[29]//input')
    LAST_7_DAY_BY_PROJECT = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[8]//input')
    PROJECT_STRING = (By.CSS_SELECTOR, 'div[class="MuiBox-root css-j7qwjs"]')
    # Локаторы для проверки цветов ячеек
    FIRST_DAY_BY_PROJECT_COLOR = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[2]//input//parent::div')
    ALL_DAY_COLORS = (By.XPATH, '//div[@class="MuiBox-root css-j7qwjs"]//div//input//parent::div')
    # Кнопки подтверждения и отмены
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Подтвердить"]')
    DISABLE_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    # Проверка что в аллерте есть поле для указания причины списания
    CHECK_LABOR_REASON_FIELD = (By.XPATH, '//label[text()="Причина"]')
    # Выбор периода на странице
    PERIOD_SELECT_BUTTON = (By.XPATH, '//div[contains(@class, "onboaring__period-select")]')
    WEEK_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="week"]')
    MONTH_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="month"]')
    PREVIOUS_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronLeftIcon"]')
    NEXT_PERIOD_BUTTON = (By.XPATH, '//button[contains(@class,"onboarding__next-quarter")]')
    PERIOD_MENU_ITEM = (By.XPATH, '//li[contains(@class,"onboarding__period-menu-item")]')
    THIS_DAY_BUTTON = (By.XPATH, '//button[contains(@class, "onboarding__show-today")]')
    # Датапикер с выбором месяца
    MONTH_DATEPICKER = (By.XPATH, '//h6[contains(@class, "MuiTypography-root MuiTypography-subtitle2 css-1mh2yc1")]')
    # Локатор для определения количества дней в месяце
    ALL_DAY_NUMBER = (By.XPATH, '//h6[contains(@class, "MuiTypography-root")]')
    # Заголовок страницы
    TITLE_PAGE = (By.XPATH, '//h6[contains(@class,"MuiTypography-root MuiTypography-subtitle1")]')
    # Кнопка добавления себя на проект
    ADD_TO_PROJECT_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Добавление на новый проект"]')
    # Кнопка добавления переработки
    ADD_OVERTIME_WORK_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Нажмите, чтобы добавить отпуск или переработку"]')
    # Фильтрация
    FILTER_BUTTON = (By.XPATH, '//button[contains(@class, "MuiButton-textSizeSmall MuiButton-disableElevation")]')
    ELEMENTS_ON_FILTER = (By.XPATH, '//span[contains(@class, "MuiTypography-body1")]')
    FILTER_BY_PROJECT_NAME = (By.XPATH, '//span[text()="Название проекта"]')
    # Кнопка открытия панели виджетов
    OPEN_WIDGET_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="KeyboardTabIcon"]')
    # Дни недели в заголовке таблицы
    SEVEN_DAY_ON_HEAD = (By.XPATH, '//span[contains(@class, "MuiTypography-root MuiTypography-caption")]')
    # Выбранные дни
    SELECTED_DAYS = (By.XPATH, '//div[contains(@class, "selected")]')
    # Первый столбец с названиями и кодами проектов
    PROJECT_TITLE = (By.XPATH, '//a[contains(@class, "MuiTypography-subtitle2")]')
    # Тултип
    TOOLTIP = (By.XPATH, '//div[contains(@class, "MuiTooltip-tooltipPlacementTop")]')
    # Модальное окно обязательного списания
    TITLE_MODAL_REASON_WINDOW = (By.XPATH, '//h6[contains(text(), "Списание")]')
    INPUT_REASON_TIME_FIELD = (By.XPATH, '//input[contains(@class, "MuiOutlinedInput-input MuiInputBase-input")]')
    INPUT_REASON_DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'textarea[name="reason"]')
    # Кнопки сохранения и сброса модального окна обязательного списания
    BREAK_LABOR_REASON_WINDOW = (By.XPATH, '//div[contains(@class, "MuiPaper-elevation24")]//button[contains(@class, "MuiButton-outlinedSecondary")]')
    SAVE_LABOR_REASON_WINDOW_BUTTON = (By.XPATH, '//div[contains(@class, "MuiPaper-elevation24")]//button[contains(@class, "onboarding__save-button")]')