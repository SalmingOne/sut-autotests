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
    ALL_DAYS_VALUE = (By.XPATH, '//div[@class="MuiBox-root css-j7qwjs"]//div//input')
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
    ADD_OVERTIME_WORK_BUTTON_FIELD = (By.XPATH, '//button[@aria-label="Нажмите, чтобы добавить отпуск или переработку"]//parent::div')
    ADD_OVERTIME_BUTTON_FIELD = (
    By.XPATH, '//button[@aria-label="Нажмите, чтобы добавить отпуск или переработку"]//child::*')
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
    # Поле ввода часов для окна с обязательным указанием причин трудозатрат
    INPUT_HOUR_FIELD = (By.CSS_SELECTOR, 'input[name="hours"]')
    # Кнопка "Сохранить" в окне с обязательным указанием причин трудозатрат
    SAVE_WINDOW_BUTTON = (By.XPATH, "//form/div/div/div/button[contains(text(),'Сохранить')]")
    # Подсказка "Поле обязательно" при попытке сохранить окно с пустым полем причины списания трудозатрат
    GOAL_REASON_FIELD_IS_REQUIRED = (By.XPATH, "//div/p[contains(text(),'Поле обязательно')]")
    # Подсказка "Максимальное количество символов: 255" при попытке сохранить окно с количеством сиволов превышающим максимальное (255 максимальное) в поле причины списания 
    GOAL_NUMBER_OF_CHARACTERS_OVER_MAX = (By.XPATH, "//div/p[contains(text(),'Максимальное количество символов: 255')]")
    
    def get_random_day_by_project(self, project_name: str ):
        return  (By.XPATH, f'//div[@aria-label="{project_name}"]//ancestor::div[@class="MuiBox-root css-j7qwjs"]//div[{random.randint(2, 29)}]//input')
    # Локаторы окна уведомления о не сохранении данных
    UNSAVED_WINDOW_TITLE = (By.XPATH, '//h6[text()="Подтвердите действие"]')
    UNSAVED_WINDOW_ACCEPT_BUTTON = (By.XPATH, '//h6[text()="Подтвердите действие"]//following::button[1]')
    UNSAVED_WINDOW_ABORT_BUTTON = (By.XPATH, '//h6[text()="Подтвердите действие"]//following::button[2]')
    # Локаторы строки Итого
    ALL_IN_TOTAL = (By.XPATH, '//p[text()="Итого"]//parent::div//parent::div//p')
    # Кнопка открытия дровера переработки
    OPEN_ABSENCE_CHOOSE_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Открыть"]')
    # Выбираем переработку или отсутствия
    OVERTIME_WORK = (By.CSS_SELECTOR, 'li[data-option-index="0"]')
    VACATION = (By.CSS_SELECTOR, 'li[data-option-index="1"]')
    ADMINISTRATIVE_LEAVE = (By.CSS_SELECTOR, 'li[data-option-index="2"]')
    SICK_LEAVE = (By.CSS_SELECTOR, 'li[data-option-index="3"]')
    MATERNITY_LEAVE = (By.CSS_SELECTOR, 'li[data-option-index="4"]')
    # Дровер добавления отсутствия
    BEGIN_LEAVE_DATA_INPUT = (By.XPATH, '//div[contains(@class, "MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-adornedEnd")]//input')
    END_LEAVE_DATA_INPUT = (By.XPATH, '//div[contains(@class, "MuiFormControl-root MuiTextField-root")][2]//input')
    FILE_INPUT = (By.CSS_SELECTOR, 'input[type="file"]')
    DRAWER_SAVE_BUTTON = (By.XPATH, '//button[contains(@class, "MuiButtonBase-root onboarding__save-button onboarding__form-footer-save-button")]')
    DRAWER_ABORT_BUTTON = (By.XPATH, '//p[contains(@class, "MuiTypography-body2 ")]//following::button[contains(@class, "MuiButton-outlinedSizeSmall MuiButton-disableElevation")][2]')
    # Сообщения о наложении отсутствий
    HAVE_REASON = (By.XPATH, '//span[contains(text(), "На выбранном периоде есть заполненные трудозатраты")]')
    HAVE_OUTER_LEAVE = (By.XPATH, '//span[contains(text(), "Наложение отсутствий, выберите другие даты")]')

