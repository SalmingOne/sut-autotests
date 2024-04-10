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
