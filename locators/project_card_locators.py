from selenium.webdriver.common.by import By


class ProjectCardLocators:
    AUTOR_NAME = (By.XPATH, '//a[contains(@class, "MuiTypography-root MuiTypography-button")]')
    # Локаторы вкладки Описание
    DESCRIPTION_TAB = (By.XPATH, '//button[text()="Описание"]')
    DESCRIPTION_TAB_TITLE = (By.XPATH, '//h6[text()="Описание"]')
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    NAME_FIELD_COLOR = (By.XPATH, '//input[@name="name"]//following-sibling::fieldset')
    CODE_FIELD = (By.CSS_SELECTOR, 'input[name="code"]')
    CODE_FIELD_COLOR = (By.XPATH, '//input[@name="code"]//following-sibling::fieldset')
    MANAGER_FIELD = (By.XPATH, '//div[@name="projectManagers"]//input')
    BEGIN_DATA_FIELD = (By.XPATH, '//label[text()="Дата начала"]//following::input[1]')
    BEGIN_DATA_FIELD_COLOR = (By.XPATH, '//label[text()="Дата начала"]//following::input[1]//following-sibling::fieldset')
    END_DATA_FIELD = (By.XPATH, '//label[text()="Дата окончания"]//following::input[1]')
    MANAGER_LABEL = (By.XPATH, '//span[contains(@class, "MuiChip-label MuiChip-labelMedium")]')
    STATUS_FIELD = (By.XPATH, '//div[@name="status"]//input')
    DESCRIPTION_FIELD = (By.XPATH, '//p[text()="Описание"]/..//div[@class="editor-content rdw-editor-main"]')
    FILE_DESCRIPTION_FIELD = (By.XPATH, '//p[text()="Описание для прилагаемых файлов"]/..//div[@class="editor-content rdw-editor-main"]')
    CHECKBOXES_TEXT = (By.XPATH, '//span[contains(@class,"MuiCheckbox-root")]//following-sibling::span[contains(@class,"MuiTypography-body1")]')

    # Локаторы вкладки Проектная иерархия
    PROJECT_HIERARCHY_TAB = (By.XPATH, '//button[text()="Проектная иерархия"]')
    PROJECT_HIERARCHY_TAB_TITLE = (By.XPATH, '//h6[text()="Ресурсы"]')
    LEGEND_SWITCH_INPUT = (By.XPATH, '//input[contains(@class,"MuiSwitch-input PrivateSwitchBase-input")]')
    LEGEND_SWITCH = (By.XPATH, '//label[contains(@class,"MuiFormControlLabel-root MuiFormControlLabel-labelPlacementEnd")]')
    SCOPE_FIELD = (By.CSS_SELECTOR, 'div[variant="outlined"]')
    CENTER_FOCUS_ICON = (By.CSS_SELECTOR, 'svg[data-testid="CenterFocusStrongIcon"]')
    PROJECT_NODE_ICON = (By.XPATH, '//div[contains(@class,"project-node")]')
    SOURCE_ICON = (By.XPATH, '//div[contains(@class,"react-flow__node")]')

    # Локаторы вкладки Команда
    TEAM_TAB = (By.XPATH, '//button[text()="Команда"]')
    REDACT_BUTTON = (By.XPATH, '//button[text()="Редактировать"]')
    TO_EXCEL_BUTTON = (By.XPATH, '//button[text()="Экспорт в Excel"]')
    TEAM_TAB_FILTER_BUTTON = (By.XPATH, '//h6[text()="Отображение"]/..')
    NUMBER_OF_RECOURSES = (By.XPATH, '//h6[text()="Количество назначений:"]/span')
    TEAM_TAB_TITLES = (By.CSS_SELECTOR, 'span[class="ag-header-cell-text"]')
    ADD_BUTTON = (By.XPATH, '//button[text()="Добавить"]')
    FIRST_MEMBER_TEXT = (By.XPATH, '//div[@row-index="0"]//p')
    ALL_MEMBERS_TEXT = (By.XPATH, '//div[@row-index]//p')
    FIRST_MEMBER_TEXT_ON_REDACT = (By.XPATH, '//div[@row-index="0"]//input[contains(@class, "MuiOutlinedInput-input")]')
    SECOND_MEMBER_TEXT_ON_REDACT = (By.XPATH, '//div[@row-index="1"]//input[contains(@class, "MuiOutlinedInput-input")]')
    ALL_MEMBERS_TEXT_ON_REDACT = (By.XPATH, '//div[@row-index]//input[contains(@class, "MuiOutlinedInput-input")]')
    FIRST_NOT_CHOOSE = (By.XPATH, '//li[@aria-selected="false"][1]')
    APPOINTMENT_DATE_DATEPICKER = (By.XPATH, '//div[@aria-colindex="5"]//*[@data-testid="CalendarTodayOutlinedIcon"]')
    THIS_DAY_PICKER = (By.XPATH, '//button[contains(@class, "MuiPickersDay-today")]')
    USERS_TEXT = (By.XPATH, '//div[@col-id="userId"]//p')
    DELETE_ICON = (By.CSS_SELECTOR, 'svg[data-testid="DeleteIcon"]')

    ALERT_DIALOG_DESCRIPTION = (By.CSS_SELECTOR, 'p[id="alert-dialog-description"]')
    MODAL_SUBMIT_BUTTON = (By.XPATH, '//p[@id="alert-dialog-description"]//following::button[text()="Подтвердить"]')
    MODAL_ABORT_BUTTON = (By.XPATH, '//p[@id="alert-dialog-description"]//following::button[text()="Отменить"]')

    # Локаторы вкладки Ресурсный план
    RESOURCE_PLAN_TAB = (By.XPATH, '//button[text()="Ресурсный план"]')
    CHOSE_PERIOD_BUTTON = (By.CSS_SELECTOR, 'div[aria-haspopup="listbox"]')
    RESOURCE_PLAN_RADIOGROUP = (By.CSS_SELECTOR, 'div[role="radiogroup"]')
    CHECKED_RADIOGROUP = (By.XPATH, '//span[contains(@class, "Mui-checked")]//following-sibling::span[contains(@class, "MuiTypography-caption")]')
    ADD_PERCENT_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="CalendarTodayOutlinedIcon"]')
    RESOURCE_PLAN_TAB_HEADER = (By.CSS_SELECTOR, 'div[class="ag-header-cell-comp-wrapper"]')
    HIRE_HEADER = (By.XPATH, '//div[@class="ag-header-cell-comp-wrapper"]//h6')
    LOW_HEADER = (By.XPATH, '//div[@class="ag-header-cell-comp-wrapper"]//span[contains(@class,"MuiTypography-caption")]')
    CHANGE_RADIOGROUP = (By.XPATH, '//span[contains(text(), "Проценты")]/..')
    TEXT_NO_RESOURCES = (By.XPATH, '//*[contains(@class,"ag-react-container")]/div/p')
    LINK_NO_RESOURCES = (By.XPATH, '//*[contains(@class,"ag-react-container")]/div/p/a')
    CELLS = (By.XPATH, '//*[contains(@class,"ag-cell-value")]')
    DROVER_TITLE = (By.XPATH, '//div[contains(@class, "MuiDrawer-paper")]//h6')
    DROVER_INPUT = (By.XPATH, '//div[contains(@class, "MuiDrawer-paper")]//input[@placeholder="Выберите процент"]')
    DROVER_MENU = (By.XPATH, '//div[contains(@class, "MuiDrawer-paper")]//button[@title="Открыть"]')
    DROVER_MENU_ITEM = (By.XPATH, '//li[contains(@class,"MuiAutocomplete-option")]')
    DROVER_SUBMIT_BUTTON = (By.XPATH, '//div[contains(@class, "MuiDrawer-paper")]//button[text()="Сохранить"]')
    DROVER_ABORT_BUTTON = (By.XPATH, '//div[contains(@class, "MuiDrawer-paper")]//button[text()="Отменить"]')
    DROVER_START_DATE = (By.XPATH, '//label[text()="Дата начала"]//following-sibling::div/input')
    DROVER_END_DATE = (By.XPATH, '//label[text()="Дата окончания"]//following-sibling::div/input')
    DROVER_HELP_TEXT_END_DATE = (By.XPATH, '//label[text()="Дата окончания"]//following-sibling::p')
    PERCENT_50 = (By.XPATH, '//li[contains(@class,"MuiAutocomplete-option")][text()="50"]')

    # Локаторы вкладки Ход выполнения
    PROGRESS_TAB = (By.XPATH, '//button[text()="Ход выполнения"]')
    PROGRESS_TAB_HEADER = (By.CSS_SELECTOR, 'span[class="ag-header-cell-text"]')
    CHECKED_CHECKBOXES = (By.XPATH, '//span[contains(@class, "Mui-checked")]')
    LABOR_COLOR = (By.XPATH, '//div[@aria-colindex="1"]/div[contains(@class,"MuiBox-root")]//descendant::div')
    DONE_ICON = (By.CSS_SELECTOR, 'svg[data-testid="DoneIcon"]')
    CLEAR_ICON = (By.CSS_SELECTOR, 'svg[data-testid="ClearIcon"]')
    KEBAB_MENU = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    KEBAB_MENU_ITEM = (By.XPATH, '//li//span[contains(@class,"MuiTypography-root MuiTypography-caption")]')
    # Тултип
    TOOLTIP = (By.XPATH, '//div[contains(@class, "MuiTooltip-tooltipPlacementTop")]')

    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    LI_MENU_ITEM_TEXT = (By.XPATH, '//li[@role="option"]/p')
    def li_by_text(self, text):
        return (By.XPATH, f'//li[text()="{text}"]')

    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    APPLY_BUTTON = (By.XPATH, '//button[text()="Применить"]')
    BREAK_BUTTON = (By.XPATH, '//button[text()="Отмена"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')

    NEXT_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronRightIcon"]')
    PREVIOUS_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronLeftIcon"]')
    THIS_DAY_BUTTON = (By.XPATH, '//button[contains(@class, "DateInterval-setToday")]')
    DISPLAYED_PERIOD = (By.XPATH, '//button[contains(@class, "DateInterval-openPicker")]/h6')
    # Ошибки
    MUI_ERROR = (By.XPATH, '//p[contains(@class, "Mui-error")]')
    ALERT_MESSAGE = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')

    CANSEL_ICON = (By.CSS_SELECTOR, 'svg[data-testid="CancelIcon"]')

    SUBMIT_BUTTON_IN_DIALOG = (By.XPATH, '//div[@role="dialog"]//button[@type="submit"]')
    ABORT_BUTTON_IN_DIALOG = (By.XPATH, '//div[@role="dialog"]//button[text()="Отменить"]')
    REASON_TEXTAREA = (By.CSS_SELECTOR, 'textarea[name="reason"]')
    INTEGRATIONS_TOOLTIP_TEXTS = (By.CSS_SELECTOR, 'p[class^="MuiTypography-root MuiTypography-inherit"]')
    OVERTIME_APPROVAL_STATUS = (By.XPATH, '//div[@col-id="overtimeApprovalStatus"]/span')
    def text_on_page(self, text):
        return (By.XPATH, f'//*[contains(text(), "{text}")]')

    def checbox_by_text(self, text):
        return (By.XPATH, f'//span[contains(@class, "MuiTypography-root MuiTypography-body1")][contains(text(), "{text}")]')

    def labor_reason_on_modal_by_text(self, text):
        return (By.XPATH, f'//*[@type="button"][contains(text(), "{text}")][@tabindex="0"]')

    def labor_reason_by_text(self, text):
        return (By.XPATH, f'//*[@type="button"][contains(text(), "{text}")]')
