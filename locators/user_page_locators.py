from selenium.webdriver.common.by import By


class UserPageLocators:
    # Переход на страницу Пользователи
    SETTING_ICON = (By.CSS_SELECTOR, 'svg[data-testid="SettingsIcon"]')
    SYSTEM_ROLE = (By.CSS_SELECTOR, 'a[href="/admin/system-roles/users"]')
    USER_PAGE_TITLE = (By.XPATH, '//h6[text()="Все пользователи"]')
    ADD_LOCAL_USER_BUTTON = (By.XPATH, '//button[text()="Пользователь"]')
    ADD_FREEIPA_USER_BUTTON = (By.XPATH, '//button[text()="Пользователь из Freeipa"]')
    NO_DATA_IMAGE = (By.CSS_SELECTOR, 'img[alt="Нет данных"]')
    # Поля поиска
    SEARCH_TAB_FIELDS = (By.CSS_SELECTOR, 'input[placeholder="Поиск"]')
    USER_SEARCH_FIELD = (By.XPATH, '//div[@aria-colindex="1"]//input[@placeholder="Поиск"]')
    USER_STATUS = (By.XPATH, '//span[contains(@class, "MuiChip-label MuiChip-labelSmall")]')
    # Кебаб меню
    USER_KEBABS = (By.CSS_SELECTOR, 'svg[data-testid="MoreHorizIcon"]')
    KEBAB_MENU_ITEM = (By.CSS_SELECTOR, 'span[class^="MuiTypography-root MuiTypography-caption"]')
    USER_FULL_INFO_BUTTON = (By.XPATH, '//span[text()="Полная информация"]')
    REDACT_BUTTON = (By.XPATH, '//span[text()="Редактировать"]')
    FIRED_BUTTON = (By.XPATH, '//span[text()="Уволить"]')
    RESTORE_BUTTON = (By.XPATH, '//span[text()="Восстановить"]')
    # Увольнение пользователя
    CALENDAR_BUTTON = (By.CSS_SELECTOR, 'button[aria-label^="Choose date, selected"]')
    FIRED_ALERT_FIELD = (By.CSS_SELECTOR, 'input[type="tel"]')
    THIS_DAY_PICKER = (By.XPATH, '//button[contains(@class, "MuiPickersDay-today")]')
    SELECTED_DAY_PICKER = (By.XPATH, '//button[contains(@class, "Mui-selected MuiPickersDay-dayWithMargin")]')
    DAY_BEFORE_SELECTED_DAY_PICKER = (By.XPATH, '//button[contains(@class, "Mui-selected MuiPickersDay-dayWithMargin")]//preceding::button[1]')
    DAY_AFTER_THIS_DAY_PICKER = (By.XPATH, '//button[contains(@class, "MuiPickersDay-today")]//following::button[1]')
    SAVE_BUTTON = (
    By.XPATH, '//p[contains(@class, "MuiTypography-root MuiTypography-body2")]//following::button[@type="submit"]')
    # Карточка пользователя
    CLEAR_BUTTON = (By.CSS_SELECTOR, 'svg[data-testid="ClearIcon"]')
    USER_CARD_LABEL = (By.XPATH, '//label[contains(@class, "")]')
    USER_CARD_TITLE = (By.XPATH, '//h6[text()="Просмотр полной информации"]')
    TAB_PROJECTS = (By.XPATH, '//button[text()="ПРОЕКТЫ"]')
    TAB_CONTACTS = (By.XPATH, '//button[text()="КОНТАКТЫ"]')
    ABORT_BUTTON = (By.XPATH, '//button[text()="Отменить"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    # Фильтрация
    FILTER_BUTTON = (By.XPATH, '//h6[text()="Отображение"]/..')
    TAB_FILTER_BUTTONS = (By.XPATH, '//div[@class="ag-floating-filter-button"]/button')
    HOUR_WAGE_CHECKBOX = (By.XPATH, '//p[text()="Почасовая оплата"]')
    BY_SALARY_CHECKBOX = (By.XPATH, '//p[text()="По окладу"]')
    CHECKED_CHECKBOXES_TEXT = (By.XPATH, '//span[contains(@class, "Mui-checked")]//following::p[1]')

    COLUMNS_HEADERS = (By.CSS_SELECTOR, 'span[ref="eText"]')
    HIRING_DATA_DATA_PICKER = (By.XPATH, '//label[text()="Дата принятия на работу"]//..//descendant::button')
    DISMISSAL_DATA_DATA_PICKER = (By.XPATH, '//input[@name="dismissalDate"]/..//*[@data-testid="CalendarTodayOutlinedIcon"]')
    DISMISSAL_DATA = (By.XPATH, '//input[@name="dismissalDate"]')
    HIRING_DATA_INPUT = (By.XPATH, '//label[text()="Дата принятия на работу"]//..//descendant::input')
    PROJECT_ROLE_FIELD = (By.XPATH, '//div[@name="projectRoles"]//button[@title="Открыть"]')
    SYSTEM_ROLE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Начните вводить системную роль"]')
    SELECTED_SYSTEM_ROLE = (By.CSS_SELECTOR, 'li[aria-label][aria-selected="true"]')
    ALL_SYSTEM_ROLE_IN_DROPDOWN = (By.CSS_SELECTOR, 'li[aria-label]')
    NOT_SELECTED_SYSTEM_ROLE = (By.CSS_SELECTOR, 'li[aria-label][aria-selected="false"]')
    USER_SYSTEM_ROLE_DISABLE_INDICATOR = (By.XPATH, '//div[@name="systemRoleIds"]//span[contains(@class,"MuiChip-label MuiChip-labelMedium")]/..')
    DELETE_PROJECT_ROLE_ICONS = (By.XPATH, '//div[@name="projectRoles"]//*[local-name()="svg"][@data-testid="CancelIcon"]')
    DELETE_ALL_SYSTEM_ROLE_ICONS = (By.XPATH, '//div[@name="systemRoleIds"]//button[@aria-label="Очистить поле"]')

    ALERT_TEXT = (By.XPATH, '//div[contains(@class, "MuiAlert-message")]')

    def delete_system_role_button(self, system_role_name):
        return By.XPATH, f'//div[@name="systemRoleIds"]//span[text()="{system_role_name}"]//..//*[local-name()="svg"]'

    def kebab_user_name(self, user_name):
        return By.XPATH, f'//div[@aria-label="{user_name}"]/../../div[@col-id="actions"]/div/button'
