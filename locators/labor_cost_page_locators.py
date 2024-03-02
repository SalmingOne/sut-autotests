import random

from selenium.webdriver.common.by import By

from data.data import PROJECT_CODE, PROJECT_NAME


class LaborCostPageLocators:
    # Переход на страницу трудозатрат
    TAB_ACTIVITY = (By.CSS_SELECTOR, 'div[id="activity"]')
    TAB_LABOR_COST_TABLE = (By.CSS_SELECTOR, 'a[href="/"]')
    # Проверка, что код проекта есть на странице
    CHECK_CODE_PROJECT = (By.XPATH, f'//a[text()="{PROJECT_CODE}"]')
    def check_code_project(self, project_code):
        return (By.XPATH, f'//a[text()="{project_code}"]')

    ALL_PROJECT_NAMES = (By.CSS_SELECTOR, 'div[basewrapprops]')
    # Дни в привязке к проекту
    ALL_DAYS_BY_PROJECT = (
        By.XPATH, f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div//input')
    RANDOM_DAYS_BY_PROJECT = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div[{random.randint(2, 29)}]//input')
    FIRST_DAY_BY_PROJECT = (
        By.XPATH, f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div[2]//input')
    LAST_28_DAY_BY_PROJECT = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div[29]//input')
    LAST_7_DAY_BY_PROJECT = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div[8]//input')
    PROJECT_STRING = (By.XPATH, '//div[contains(@class,"project-row MuiBox-root")]')
    ALL_DAYS_VALUE = (By.XPATH, '//ancestor::div[contains(@class,"project-row MuiBox-root")]//div//input')
    # Локаторы для проверки цветов ячеек
    FIRST_DAY_BY_PROJECT_COLOR = (
        By.XPATH,
        f'//div[@aria-label="{PROJECT_NAME}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div[2]//input//parent::div')
    ALL_DAY_COLORS = (By.XPATH, '//ancestor::div[contains(@class,"project-row MuiBox-root")]//div//input//parent::div')
    # Кнопки подтверждения и отмены
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Подтвердить"]')
    DISABLE_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    # Проверка что в аллерте есть поле для указания причины списания
    CHECK_LABOR_REASON_FIELD = (By.XPATH, '//label[text()="Причина"]')
    # Выбор периода на странице
    PERIOD_SELECT_BUTTON = (By.XPATH, '//div[contains(@class, "MuiSelect-select MuiSelect-standard MuiInput-input MuiInputBase-input")]')
    WEEK_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="week"]')
    MONTH_PERIOD_SELECT = (By.CSS_SELECTOR, 'li[data-value="month"]')
    PREVIOUS_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronLeftIcon"]')
    NEXT_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronRightIcon"]')
    PERIOD_MENU_ITEM = (By.XPATH, '//li[contains(@class,"MuiMenuItem-gutters")]')
    THIS_DAY_BUTTON = (By.XPATH, '//button[contains(@class, "DateInterval-setToday")]')
    # Датапикер с выбором месяца
    MONTH_DATEPICKER = (By.XPATH, '//button[contains(@class, "DateInterval-openPicker")]')
    # Локатор для определения количества дней в месяце
    ALL_DAY_NUMBER = (By.XPATH, '//h6[contains(@class, "MuiTypography-root")]')
    # Заголовок страницы
    TITLE_PAGE = (By.XPATH, '//h6[contains(@class,"MuiTypography-root MuiTypography-subtitle1")]')
    # Кнопка добавления себя на проект
    ADD_TO_PROJECT_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Добавление на новый проект"]')
    # Кнопка добавления переработки и отсутствий
    ADD_OVERTIME_WORK_BUTTON = (By.XPATH, '//button[text()="Переработка"]')
    ADD_ABSENSE_BUTTON = (By.XPATH, '//button[text()="Отсутствие"]')

    # Фильтрация
    FILTER_BUTTON = (By.XPATH, '//button[contains(@class, "MuiButton-text MuiButton-textPrimary")]')
    ELEMENTS_ON_FILTER = (By.XPATH, '//div[contains(@class, "MuiPaper-elevation8")]//span[contains(@class, "MuiTypography-body1")]')
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
    BREAK_LABOR_REASON_WINDOW = (By.XPATH,
                                 '//h6[contains(text(), "Списание")]//following::button[contains(@class, "MuiButton-outlinedSecondary")]')
    SAVE_LABOR_REASON_WINDOW_BUTTON = (
    By.XPATH, '//h6[contains(text(), "Списание")]//following::button[contains(@class, "MuiButton-sizeSmall MuiButton-containedSizeSmall")]')
    # Поле ввода часов для окна с обязательным указанием причин трудозатрат
    INPUT_HOUR_FIELD = (By.CSS_SELECTOR, 'input[name="hours"]')
    # Кнопка "Сохранить" в окне с обязательным указанием причин трудозатрат
    SAVE_WINDOW_BUTTON = (By.XPATH, "//form/div/div/div/button[contains(text(),'Сохранить')]")
    # Подсказка "Поле обязательно" при попытке сохранить окно с пустым полем причины списания трудозатрат
    GOAL_REASON_FIELD_IS_REQUIRED = (By.XPATH, "//div/p[contains(text(),'Поле обязательно')]")
    # Подсказка "Максимальное количество символов: 255" при попытке сохранить окно с количеством сиволов превышающим максимальное (255 максимальное) в поле причины списания 
    GOAL_NUMBER_OF_CHARACTERS_OVER_MAX = (By.XPATH, "//div/p[contains(text(),'Максимальное количество символов: 255')]")

    def get_random_day_by_project(self, project_name: str):
        return (By.XPATH,
                f'//div[@aria-label="{project_name}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div[{random.randint(2, 29)}]//input')

    def get_day_by_project(self, project_name, number_day):
        return (By.XPATH,
                f'//div[@aria-label="{project_name}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div[{number_day}]//input')

    def all_day_by_project(self, project_name):
        return By.XPATH, f'//div[@aria-label="{project_name}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//input'
    def total_by_project(self, project_name):
        return By.XPATH, f'//div[@aria-label="{project_name}"]//ancestor::div[contains(@class,"project-row MuiBox-root")]//div//p'
    # Локаторы окна уведомления о не сохранении данных
    UNSAVED_WINDOW_TITLE = (By.XPATH, '//h6[text()="Подтвердите действие"]')
    UNSAVED_WINDOW_ACCEPT_BUTTON = (By.XPATH, '//h6[text()="Подтвердите действие"]//following::button[1]')
    UNSAVED_WINDOW_ABORT_BUTTON = (By.XPATH, '//h6[text()="Подтвердите действие"]//following::button[2]')
    # Локаторы строки Итого
    ALL_IN_TOTAL = (By.XPATH, '//p[text()="Итого"]//parent::div//parent::div//p')
    # Кнопка открытия дровера переработки
    OPEN_ABSENCE_CHOOSE_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Открыть"]')
    # Выбираем переработку или отсутствия
    ALL_OVERTIME_WORK_AND_LEAVE = (By.CSS_SELECTOR, 'li[data-option-index]')

    VACATION = (By.CSS_SELECTOR, 'li[data-option-index="0"]')
    SICK_LEAVE = (By.CSS_SELECTOR, 'li[data-option-index="1"]')
    ADMINISTRATIVE_LEAVE = (By.CSS_SELECTOR, 'li[data-option-index="2"]')
    MATERNITY_LEAVE = (By.CSS_SELECTOR, 'li[data-option-index="3"]')
    # Дровер добавления отсутствия
    BEGIN_LEAVE_DATA_INPUT = (By.XPATH,
                              '//div[contains(@class, "MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-adornedEnd")]//input')
    BEGIN_LEAVE_DATA_PICKER_BUTTON = (By.XPATH,
                              '//div[contains(@class, "MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-adornedEnd")]//button')
    ALL_DATA_IN_DATA_PICKER = (By.XPATH, '//button[contains(@class, "MuiPickersDay-dayWithMargin")]')
    PREVIOUS_MONTH_IN_DATA_PICKER = (By.CSS_SELECTOR, 'svg[data-testid="ArrowLeftIcon"]')
    END_LEAVE_DATA_INPUT = (By.XPATH, '//div[contains(@class, "MuiFormControl-root MuiTextField-root")][2]//input')
    FILE_INPUT = (By.CSS_SELECTOR, 'input[type="file"]')
    CHECK_TASK_FIELD = (By.XPATH, '//label[text()="Задача"]')
    DRAWER_SAVE_BUTTON = (By.XPATH, '//div[@name="type"]//following::button[@type="submit"]')
    DRAWER_SAVE_BUTTON_DISABLE = (By.XPATH,
                                  '//div[@aria-label="Заполните все обязательные поля"]//button[contains(@class, "Mui-disabled onboarding__save-button onboarding__form-footer-save-button")]')
    OVERTIME_WORK_SAVE_BUTTON_DISABLE = (By.XPATH,
                                  '//div[@name="task"]//following::button[contains(@class, "MuiButton-disableElevation MuiButtonBase-root Mui-disabled ")]')
    DRAWER_ALERT_DIALOG_SAVE_BUTTON = (By.XPATH, '//p[@id="alert-dialog-description"]//following::button[@type="submit"]')
    OVERTIME_WORK_SAVE_BUTTON = (By.XPATH, '//div[@name="task"]//following::button[@type="submit"]')
    DRAWER_ABORT_BUTTON = (By.XPATH,
                           '//p[contains(@class, "MuiTypography-body2 ")]//following::button[contains(@class, "MuiButton-outlinedSizeSmall MuiButton-disableElevation")][2]')
    OVERTIME_WORK_DATA_PICKER = (By.CSS_SELECTOR, 'svg[data-testid="CalendarTodayOutlinedIcon"]')
    OVERTIME_WORK_INPUT = (By.CSS_SELECTOR, 'input[name="overtimeWork"]')
    PROJECT_NAME_DRAWER_INPUT = (By.CSS_SELECTOR, 'div[name="project"]')
    def chose_project_on_overtime_work_drawer(self, project_mame):
        return By.XPATH, f'//p[text()="{project_mame}"]'

    ALL_PROJECT_ON_DRAWER_INPUT = (By.CSS_SELECTOR, 'li[role="option"]')
    DRAWER_OVERTIME_WORK_SAVE_BUTTON = (By.XPATH,
                                        '//p[contains(@class, "MuiTypography-body2 ")]//following::button[contains(@class, "MuiButtonBase-root onboarding__save-button onboarding__form-footer-save-button")][2]')
    OVERTIME_REASON_INPUT = (By.CSS_SELECTOR, 'textarea[name="overtimeReason"]')
    # Сообщения о наложении отсутствий
    HAVE_REASON = (By.XPATH, '//span[contains(text(), "На выбранном периоде есть заполненные трудозатраты")]')
    HAVE_OUTER_LEAVE = (By.XPATH, '//span[contains(text(), "Наложение отсутствий, выберите другие даты")]')
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    ALERT_TEXT = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')

    # Отсутствия
    STATEMENT_TABS_HEADERS = (By.CSS_SELECTOR, 'span[class="ag-header-cell-text"]')
    DOWNLOAD_FILE_TEXT = (By.XPATH, '//p[contains(text(), "Скачать файлы")]')
    ALL_ABSENCE_KEBABS = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    PREVIOUS_ABSENCE_CHECKBOX = (By.XPATH, '//label[contains(@class, "MuiFormControlLabel-labelPlacementEnd")]')
    CHECKED_PREVIOUS_ABSENCE_CHECKBOX = (By.XPATH, '//span[contains(@class,"Mui-checked")]')

    KEBABS_DEL_MENU_ITEM = (By.XPATH, '//span[text()="Удалить"]')
    DEL_ACCEPT_BUTTON = (By.XPATH, '//p[@id="alert-dialog-description"]//following::button[@type="submit"]')
    DEL_CANSEL_BUTTON = (
    By.XPATH, '//p[@id="alert-dialog-description"]//following::button[contains(@class, "MuiButton-outlinedSizeSmall MuiButton-disableElevation")]')
    KEBABS_REDACT_MENU_ITEM = (By.XPATH, '//span[text()="Редактировать"]')
    FIRST_AND_LAST_ABSENCE_DAY = (By.XPATH, '//input[contains(@class, "MuiInputBase-inputAdornedEnd")]')
    ABSENCE_START_DATE_ON_TAB = (By.CSS_SELECTOR,
                                 'div[col-id="startDate"][class="ag-cell ag-cell-not-inline-editing ag-cell-normal-height ag-cell-value"]')
    ABSENCE_END_DATE_ON_TAB = (By.CSS_SELECTOR,
                               'div[col-id="endDate"][class="ag-cell ag-cell-not-inline-editing ag-cell-normal-height ag-cell-value"]')
    DRAWER_DESCRIPTION_TEXT = (By.CSS_SELECTOR, 'p[id="alert-dialog-description"]')
    ALL_DATES_OVERTIME_WORK = (By.XPATH,
                               '//h6[text()="Переработки"]//following::div[contains(@class, "ag-cell ag-cell-not-inline-editing ag-cell-normal-height ag-cell-value")][@col-id="date"]')

    REASON_TAB_TITLE = (By.XPATH, '//h6[text()="Причины"]')
    def check_projeck_on_reason_tab(self, project_mame):
        return By.XPATH, f'//div[@class="ag-cell ag-cell-not-inline-editing ag-cell-normal-height ag-cell-value"]//div[@aria-label="{project_mame}"]'
