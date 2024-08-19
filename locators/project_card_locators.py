from selenium.webdriver.common.by import By


class ProjectCardLocators:
    AUTOR_NAME = (By.XPATH, '//a[contains(@class, "MuiTypography-root MuiTypography-button")]')
    # Локаторы вкладки Описание
    DESCRIPTION_TAB = (By.XPATH, '//button[text()="Описание"]')
    DESCRIPTION_TAB_TITLE = (By.XPATH, '//h6[text()="Описание"]')
    NAME_FIELD = (By.CSS_SELECTOR, 'input[name="name"]')
    CODE_FIELD = (By.CSS_SELECTOR, 'input[name="code"]')
    MANAGER_FIELD = (By.XPATH, '//div[@name="projectManagers"]//input')
    BEGIN_DATA_FIELD = (By.XPATH, '//label[text()="Дата начала"]//following::input[1]')
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
    # Локаторы вкладки Ход выполнения
    PROGRESS_TAB = (By.XPATH, '//button[text()="Ход выполнения"]')
    PROGRESS_TAB_HEADER = (By.CSS_SELECTOR, 'span[class="ag-header-cell-text"]')

    DONE_ICON = (By.CSS_SELECTOR, 'svg[data-testid="DoneIcon"]')
    CLEAR_ICON = (By.CSS_SELECTOR, 'svg[data-testid="ClearIcon"]')
    KEBAB_MENU = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    KEBAB_MENU_ITEM = (By.XPATH, '//li//span[contains(@class,"MuiTypography-root MuiTypography-caption")]')
    # Тултип
    TOOLTIP = (By.XPATH, '//div[contains(@class, "MuiTooltip-tooltipPlacementTop")]')

    LI_MENU_ITEM = (By.CSS_SELECTOR, 'li[role="option"]')
    def li_by_text(self, text):
        return (By.XPATH, f'//li[text()="{text}"]')

    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    BREAK_BUTTON = (By.XPATH, '//button[text()="Отмена"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')

    NEXT_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronRightIcon"]')
    PREVIOUS_PERIOD_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ChevronLeftIcon"]')
    THIS_DAY_BUTTON = (By.XPATH, '//button[contains(@class, "DateInterval-setToday")]')