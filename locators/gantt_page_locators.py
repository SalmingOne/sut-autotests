from selenium.webdriver.common.by import By


class GanttPageLocators:
    # Переход на вкладку Диаграмма ганта
    GANTT_TAB = (By.XPATH, '//div[text()="Диаграмма Ганта"]')
    # Таблица
    EDIT_GANTT_BUTTON = (By.XPATH, '//button[text()="Редактировать"]')
    CREATE_PHASE_OR_TASK_BUTTON = (By.XPATH, '//button[text()="Создать"]')
    CREATE_PHASE_BUTTON = (By.XPATH, '//span[text()="Создать фазу"]')
    CHECK_COLUMN_TAB = (By.XPATH, '//button[contains(@class,"MuiButtonBase-root MuiIconButton-root")]//*[@data-testid="SettingsIcon"]')
    STATUS_COLUMN_CHECKBOX = (By.XPATH, '//span[text()="Статус"]')
    # Дровер добавления фазы
    PHASE_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    DRAWER_SUBMIT_BUTTON = (By.XPATH, '//div[@name="parent"]//following::button[@type="submit"]')
    ALERT_MESSAGE = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')
    PARENT_PHASE_NAME = (By.XPATH, "//div[@name='parent']//input")
    DROPDOWN_ITEMS = (By.XPATH, "//li")

    def start_date(self, phase_or_task_name):
        return (By.XPATH, f'//div[@aria-label="{phase_or_task_name}"]//following-sibling::*[@data-column-name="start_date"]')

    def end_date(self, phase_or_task_name):
        return (By.XPATH, f'//div[@aria-label="{phase_or_task_name}"]//following-sibling::*[@data-column-name="end_date"]')
    def status(self, phase_or_task_name):
        return (By.XPATH, f'//div[@aria-label="{phase_or_task_name}"]//following-sibling::*[@data-column-name="status"]')

    CALENDAR = (By.CSS_SELECTOR, 'div[class="gantt_layout_cell gantt_layout gantt_layout_y "]')
    PROJECT_LIVE_LINE = (By.CSS_SELECTOR, 'div[class="gantt_task_content"]')
    TODAY_MARKER = (By.CSS_SELECTOR, 'div[class="gantt_marker today_marker"]')
    TODAY_BUTTON = (By.XPATH, '//button[text()="Сегодня"]')

    GANTT_GRID = (By.CSS_SELECTOR, 'div[class="gantt_grid"]')
    GANT_TASK = (By.CSS_SELECTOR, 'div[class="gantt_task"]')
    TUNE_ICON = (By.CSS_SELECTOR, 'svg[data-testid="TuneIcon"]')
    CHOSE_PERIOD_BUTTON = (By.CSS_SELECTOR, 'div[aria-haspopup="listbox"]')
    BASE_PLAN_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="StraightenIcon"]')
    FIELDS_FILTER = (By.XPATH, '//*[@data-testid="TuneIcon"]//following::*[@data-testid="SettingsIcon"]')
    COLUMN_HEADER = (By.CSS_SELECTOR, 'div[role="columnheader"]')
    CHECKBOXES_TEXT = (By.XPATH, '//span[contains(@class,"MuiCheckbox-root")]//following-sibling::span[contains(@class,"MuiTypography-body1")]')
    CHECKBOXES = (By.XPATH, "//input[@type='checkbox']/..")
    PHASES_NAME = (By.XPATH, "//div[contains(@class, 'gantt_grid')]//div[contains(@aria-label, 'Фаза')]")
    TASKS_NAME = (By.XPATH, "//div[contains(@class, 'gantt_grid')]//div[contains(@aria-label, 'Задача')]")

    def get_number_of_task_or_phase_by_name(self, phase_or_task_name):
        return By.XPATH, f"//div[contains(@class, 'gantt_grid')]//div[contains(@aria-label, '{phase_or_task_name}')]//div[@data-column-name='number']"

    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    TABLE_ROWS = (By.XPATH, "//div[contains(@class, 'gantt_row')]")
    GANTT_TOOLTIP = (By.CSS_SELECTOR, 'div[class="gantt_tooltip"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    DISCARD_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    MODAL_SUBMIT_BUTTON = (By.XPATH, '//p[@id="alert-dialog-description"]//following::button[text()="Подтвердить"]')
    MODAL_ABORT_BUTTON = (By.XPATH, '//p[@id="alert-dialog-description"]//following::button[text()="Отменить"]')
    def get_task(self, task_name):
        return By.XPATH, f"//div[contains(@class, 'gantt_row') and contains(@aria-label, 'Задача: {task_name} ')]"

    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    FIELD_BORDER = (By.XPATH, '//input[@name="name"]//following-sibling::fieldset')


