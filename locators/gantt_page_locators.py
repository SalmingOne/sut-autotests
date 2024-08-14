from selenium.webdriver.common.by import By


class GanttPageLocators:
    # Переход на вкладку Диаграмма ганта
    GANTT_TAB = (By.XPATH, '//button[text()="Диаграмма Ганта"]')
    # Таблица
    EDIT_GANTT_BUTTON = (By.XPATH, '//button[text()="Редактировать"]')
    CREATE_PHASE_OR_TASK_BUTTON = (By.XPATH, '//button[text()="Создать"]')
    CREATE_PHASE_BUTTON = (By.XPATH, '//span[text()="Создать фазу"]')
    CHECK_COLUMN_TAB = (By.XPATH, '//button[contains(@class,"MuiButtonBase-root MuiIconButton-root")]//*[@data-testid="SettingsIcon"]')
    STATUS_COLUMN_CHECKBOX = (By.XPATH, '//span[text()="Статус"]')
    # Дровер добавления фазы
    PHASE_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    DRAWER_SUBMIT_BUTTON = (By.XPATH, '//div[@name="parent"]//following::button[@type="submit"]')

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
    TUNE_ICON = (By.CSS_SELECTOR, 'svg[data-testid="TuneIcon"]')
    CHOSE_PERIOD_BUTTON = (By.CSS_SELECTOR, 'div[aria-haspopup="listbox"]')
    BASE_PLAN_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="StraightenIcon"]')
    FIELDS_FILTER = (By.XPATH, '//*[@data-testid="TuneIcon"]//following::*[@data-testid="SettingsIcon"]')
    COLUMN_HEADER = (By.CSS_SELECTOR, 'div[role="columnheader"]')
    CHECKBOXES_TEXT = (By.XPATH, '//span[contains(@class,"MuiCheckbox-root")]//following-sibling::span[contains(@class,"MuiTypography-body1")]')


    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')


